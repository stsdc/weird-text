"""
This module contains the decoder class only.
"""

import re

from decoder_exceptions import NoSeparatorError, NoMatchWordFoundError, EmptyWordListError


class Decoder:
    """
    A class to represent a encoder.
    """
    separator = '\n-weird-\n'

    def __init__(self) -> None:
        self.re_all_words = re.compile(r'(\w+)', re.U)
        self.re_all_encoded_words = re.compile(r'(?:-weird-)', re.U)

    @property
    def word_list(self) -> str:
        """Holds ordered list of original words."""
        return self._word_list

    @word_list.setter
    def word_list(self, word_list: str) -> None:
        if len(word_list) != 0:
            self._word_list = word_list
        else:
            raise EmptyWordListError()

    def decode(self, data_in: str) -> str:
        """
        Main decoding function. Returns decoded text. If
        there are no separators, it returns the original text.
        """

        try:
            data_to_decode = self._extract_encoded_text(data_in)

            for match in re.finditer(self.re_all_words, data_to_decode):
                encoded_word = match.group()

                decoded_word = self._match_word(encoded_word)

                data_to_decode = data_to_decode.replace(encoded_word, decoded_word)

            return data_to_decode

        except NoSeparatorError as error:
            print(error)
            return data_in

    def _extract_encoded_text(self, data_in: str) -> str:
        """
        Strips off encoded text from the separators.
        Returns the text without separators. If there
        are no separators, it raises an exception.
        """
        if self.separator in data_in:
            data_to_decode = data_in.split(self.separator)
            return data_to_decode[1]

        raise NoSeparatorError()

    def _match_word(self, encoded_word: str) -> str:
        """
        Function tries to match the encoded word with the
        original word. If it can't find a match, it raises
        an exception.
        """
        for word in self.word_list:
            if len(word) == len(encoded_word):
                number_of_confirmed_chars = 0

                word_copy = word
                for char in encoded_word:
                    if char in word_copy:
                        number_of_confirmed_chars += 1

                        # Removing confirmed chars. It will prevent false
                        # positives in the next iterations.
                        # (e.g. 'aaabc' and 'cba' will return aaabc as a match)
                        word_copy = word_copy.replace(char, '', 1)

                if number_of_confirmed_chars == len(encoded_word):
                    # print (f'{encoded_word} -> {word}')
                    return word

        raise NoMatchWordFoundError()
