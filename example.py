#!/usr/bin/env python

"""Example usage"""

from encoder import Encoder
from decoder import Decoder

if __name__ == '__main__':
    encoder = Encoder()

    ENCODED_TEXT = encoder.encode('''
    Lorem Ipsum is simply dummy text of the printing and typesetting industry.
    ''')

    print(ENCODED_TEXT)
    print(encoder.word_list)

    decoder = Decoder()
    decoder.word_list = encoder.word_list


    decoded_text = decoder.decode(ENCODED_TEXT)
    print(decoded_text)
