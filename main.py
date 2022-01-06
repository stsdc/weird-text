#!/usr/bin/env python

from encoder import Encoder

if __name__ == '__main__':
    encoder = Encoder()

    encoded_text = encoder.encode('This is a long looong test sentence,\nwith some big (biiiiig) words!')
    print(encoded_text)