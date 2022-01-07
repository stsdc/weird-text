import re
import random

class Encoder:
    separator = '\n-weird-\n'
    
    def __init__(self) -> None:
        self.tokenize_re = re.compile(r'(\w+)', re.U)

        self.word_list = list()

    def encode(self, data_in: str) -> str:
        """
        :param data: 
        :return:
        """

        data_out = data_in

        # self.word_list = re.findall(self.tokenize_re, data)
        for match in re.finditer(self.tokenize_re, data_in):
            word = match.group()
            self.word_list.append(word)

            word_shuffled = self._shuffle(word)

            data_out = data_out.replace(word, word_shuffled)

            # print(f'{word} -> {word_shuffled}')
            
        self.word_list.sort(key=str.lower)
        return self.separator + data_out + self.separator


    def _shuffle(self, word: str) -> str:
        word_characters = list(word)
        random.shuffle(word_characters)
        return ''.join(word_characters)
