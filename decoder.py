import re

class Decoder:
    separator = '\n-weird-\n'

    def __init__(self, word_list: str) -> None:
        self.re_all_words = re.compile(r'(\w+)', re.U)
        self.re_all_encoded_words = re.compile(r'(?:-weird-)', re.U)
        self.word_list = word_list
        self.encoded_word_list = list()


    def decode(self, data_in: str) -> str:
        """
        :param data: 
        :return:
        """

        # for match in re.finditer(self.re_all_encoded_words, data_in):
        #     word = match.group()
        #     print(word)

        data_out = data_in

        if self.separator in data_in:
            data_to_decode = data_in.split(self.separator)
            data_out = data_to_decode[1]

            for match in re.finditer(self.re_all_words, data_to_decode[1]):
                encoded_word = match.group()
                self.encoded_word_list.append(encoded_word)

                for word in self.word_list:
                    if len(word) == len(encoded_word):
                        number_of_confirmed_chars = 0

                        for char in encoded_word:
                            if char in word:
                                number_of_confirmed_chars += 1
                        
                        if number_of_confirmed_chars == len(encoded_word):
                            # print (f'{encoded_word} -> {word}')

                            data_out = data_out.replace(encoded_word, word)
        
        print(data_out)

    # def _words_matcher(self) -> str:
    #     for word_in_list in self.word_list:
    #         if len(word_in_list) == len(word):
    #             number_of_confirmed_chars = 0

    #             for char in word:
    #                 if char in word_in_list:
    #                     number_of_confirmed_chars += 1

    #             if number_of_confirmed_chars == len(word):
    #                 return word_in_list

    #     return ''
