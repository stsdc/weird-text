import re

from decoder_exceptions import *

class Decoder:
    separator = '\n-weird-\n'

    def __init__(self, word_list: str) -> None:
        self.re_all_words = re.compile(r'(\w+)', re.U)
        self.re_all_encoded_words = re.compile(r'(?:-weird-)', re.U)
        self.word_list = word_list

    def decode(self, data_in: str) -> str:
        """
        :param data: 
        :return:
        """

        try:
            data_to_decode = self._extract_encoded_text(data_in)

            for match in re.finditer(self.re_all_words, data_to_decode):
                encoded_word = match.group()

                decoded_word = self._match_word(encoded_word)

                data_to_decode = data_to_decode.replace(encoded_word, decoded_word)
            
            return data_to_decode

        except NoSeparatorError as e:
            print(e)
            return data_in


        
        # print(data_out)

    def _extract_encoded_text(self, data_in: str) -> str:
        if self.separator in data_in:
            data_to_decode = data_in.split(self.separator)
            return data_to_decode[1]
        else:
            raise NoSeparatorError()

    def _match_word(self, encoded_word: str) -> str:
        for word in self.word_list:
            if len(word) == len(encoded_word):
                number_of_confirmed_chars = 0

                # checking for the same characters;
                # it will not take in count if there
                # are more than one same character
                # TODO: remove chars after confirming
                for char in encoded_word:
                    if char in word:
                        number_of_confirmed_chars += 1

                if number_of_confirmed_chars == len(encoded_word):
                    # print (f'{encoded_word} -> {word}')
                    return word

