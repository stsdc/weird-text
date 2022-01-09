import pytest

from decoder import Decoder
from decoder_exceptions import *

def test_Decoder():
    decoder = Decoder(["abc"])
    assert decoder
    assert decoder.word_list == ["abc"]

    with pytest.raises(EmptyWordListError):
        decoder = Decoder([])

def test_Decoder__extract_encoded_text():
    decoder = Decoder(["abc"])
    assert decoder._extract_encoded_text("\n-weird-\ncba\n-weird-\n") == "cba"

    with pytest.raises(NoSeparatorError):
        decoder._extract_encoded_text("cba")

def test_Decoder__match_word():
    decoder = Decoder(["abc"])
    assert decoder._match_word("bac") == "abc"

    with pytest.raises(NoMatchWordFoundError):
        decoder._match_word("abcd")

    decoder = Decoder(["aaaabc"])
    with pytest.raises(NoMatchWordFoundError):
        decoder._match_word("abc")

def test_Decoder_decode():
    decoder = Decoder(["abc"])
    assert decoder.decode("cba") == "cba"

    decoder = Decoder(["abc"])
    assert decoder.decode("\n-weird-\ncba\n-weird-\n") == "abc"