"""This module contains the encoder class only."""

import re
import random

class Encoder:  # pylint: disable=too-few-public-methods
    """
    A class to represent a encoder.
    """
    separator = '\n-weird-\n'

    def __init__(self) -> None:
        self.tokenize_re = re.compile(r'(\w+)', re.U)

        self.word_list = []

    def encode(self, data_in: str) -> str:
        """
        Main encoding function. Creates an ordered list of
        all original words. Returns words with shuffled
        characters in them, but preserves the original order
        of words and punctuation. Returns unencoded text if
        text is empty.
        """

        if len(data_in) == 0:
            return data_in

        data_out = data_in

        # Iterate over all words in the input text.
        # This will not include special characters and punctuation.
        for match in re.finditer(self.tokenize_re, data_in):
            word = match.group()

            self.word_list.append(word)

            word_shuffled = self._shuffle(word)

            data_out = data_out.replace(word, word_shuffled)

            # print(f'{word} -> {word_shuffled}')

        self.word_list.sort(key=str.lower)
        return self.separator + data_out + self.separator

    @staticmethod
    def _shuffle(word: str) -> str:
        """Shuffle the characters in a word."""
        word_characters = list(word)

        # Just making sure that shuffle produces
        # the same word as the original.
        shuffled_word = word
        while shuffled_word == word:
            random.shuffle(word_characters)
            shuffled_word = ''.join(word_characters)

        return shuffled_word
