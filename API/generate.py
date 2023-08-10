import numpy as np
from tensorflow.keras.models import load_model, Model
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.layers import Input, LSTM, Dense, Embedding, Concatenate
import logging

# Load the model and tokenizer
model = load_model('model.h5')

with open("tokenizer.json", "r") as file:
    tokenizer_config = file.read()
    tokenizer = tokenizer_from_json(tokenizer_config)

# Validate presence of <start> token
assert '<start>' in tokenizer.word_index, "<start> token not found in tokenizer"

encoder_inputs = [model.get_layer('input_3').output, model.get_layer('input_4').output]
encoder_states = model.get_layer('lstm_2').output[1:]

encoder_model = Model(inputs=model.input, outputs=encoder_states)

latent_dim = model.get_layer('lstm_2').units

decoder_state_input_h = Input(shape=(latent_dim,))
decoder_state_input_c = Input(shape=(latent_dim,))
decoder_states_inputs = [decoder_state_input_h, decoder_state_input_c]

decoder_embedding_layer = model.get_layer('embedding_1')
decoder_inputs = model.get_layer('input_3').output
decoder_embedding_ = decoder_embedding_layer(decoder_inputs)

decoder_lstm_layer = model.get_layer('lstm_3')
decoder_outputs_, state_h_, state_c_ = decoder_lstm_layer(decoder_embedding_, initial_state=decoder_states_inputs)

decoder_dense = model.get_layer('dense_1')
decoder_outputs_ = decoder_dense(decoder_outputs_)

decoder_model = Model([decoder_inputs] + decoder_states_inputs, [decoder_outputs_] + [state_h_, state_c_])

def generate_text(input_sequence):
    try:
        states_value = encoder_model.predict(input_sequence)
        target_sequence = np.zeros((1, 1))
        target_sequence[0, 0] = tokenizer.word_index['<start>']

        stop_condition = False
        generated_text = []

        while not stop_condition:
            output_tokens, h, c = decoder_model.predict([target_sequence] + states_value)
            sampled_token_index = np.argmax(output_tokens[0, -1, :])
            sampled_word = tokenizer.index_word.get(sampled_token_index, '')

            if sampled_word == 'end':
                stop_condition = True
            else:
                generated_text.append(sampled_word)

            target_sequence = np.zeros((1, 1))
            target_sequence[0, 0] = sampled_token_index
            states_value = [h, c]

        return ' '.join(generated_text)

    except Exception as e:
        logging.error("Exception occurred in generate_text", exc_info=True)
        raise e
