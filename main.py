#!/usr/bin/env python

from encoder import Encoder
from decoder import Decoder

if __name__ == '__main__':
    encoder = Encoder()

    encoded_text = encoder.encode('This is a long looong test sentence,\nwith some big (biiiiig) words!')
    print(encoded_text)

    decoder = Decoder(encoder.word_list)

    decoded_text = decoder.decode(encoded_text)