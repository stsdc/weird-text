"""This module contains tests for Decoder class."""

# pylint: disable=protected-access

import pytest

from decoder import Decoder
from decoder_exceptions import NoSeparatorError, NoMatchWordFoundError, EmptyWordListError


def test_decoder():
    """Test the decoder class."""
    decoder = Decoder()
    decoder.word_list = ["abc"]
    assert decoder
    assert decoder.word_list == ["abc"]

    with pytest.raises(EmptyWordListError):
        decoder = Decoder()
        decoder.word_list = []


def test_decoder__extract_encoded_text():
    """Test the decoder's extract_encoded_text function."""
    decoder = Decoder()
    decoder.word_list = ["abc"]
    assert decoder._extract_encoded_text("\n-weird-\ncba\n-weird-\n") == "cba"

    with pytest.raises(NoSeparatorError):
        decoder._extract_encoded_text("cba")


def test_decoder__match_word():
    """Test the decoder's _match_word function."""
    decoder = Decoder()
    decoder.word_list = ["abc"]
    assert decoder._match_word("bac") == "abc"

    with pytest.raises(NoMatchWordFoundError):
        decoder._match_word("abcd")

    decoder = Decoder()
    decoder.word_list = ["aaaabc"]
    with pytest.raises(NoMatchWordFoundError):
        decoder._match_word("abc")


def test_decoder_decode():
    """Test the decoder's decode function."""
    decoder = Decoder()
    decoder.word_list = ["abc"]
    assert decoder.decode("cba") == "cba"

    decoder = Decoder()
    decoder.word_list = ["abc"]
    assert decoder.decode("\n-weird-\ncba\n-weird-\n") == "abc"
