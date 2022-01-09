import pytest

from encoder import Encoder

def test_Encoder():
    decoder = Encoder()
    assert decoder

def test_Encoder__shuffle():
    decoder = Encoder()
    assert decoder._shuffle("word") != "word"

def test_Encoder_encode():
    encoder = Encoder()
    encoded_text = encoder.encode("One, two, three!")
    assert len(encoder.word_list) == 3
    assert Encoder.separator in encoded_text

