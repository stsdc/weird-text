#!/usr/bin/env python

from encoder import Encoder
from decoder import Decoder

if __name__ == '__main__':
    encoder = Encoder()

    encoded_text = encoder.encode('Lorem Ipsum is simply dummy text of the printing and typesetting industry.')
    print(encoded_text)

    decoder = Decoder(encoder.word_list)

    decoded_text = decoder.decode(encoded_text)
    print(decoded_text)