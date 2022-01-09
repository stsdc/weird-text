"""This module contains tests for Encoder class."""

# pylint: disable=protected-access

from encoder import Encoder


def test_encoder():
    """Test the encoder class."""
    decoder = Encoder()
    assert decoder


def test_encoder__shuffle():
    """Test the encoder's _shuffle function."""
    decoder = Encoder()
    assert decoder._shuffle("word") != "word"


def test_encoder_encode():
    """Test the encoder's encode function."""
    encoder = Encoder()
    encoded_text = encoder.encode("One, two, three!")
    assert len(encoder.word_list) == 3
    assert Encoder.separator in encoded_text
