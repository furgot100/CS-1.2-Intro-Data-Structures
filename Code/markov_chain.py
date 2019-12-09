from dictogram import Dictogram, read_file
import random


class Markov():
    def __init__(self, word_list, amount,order=2):
        """Initilize starting variables"""
        self.word_list = word_list
        self.amount = amount
        self.order = order

    def higher_order(self, new_words):
        dictionary = dict()
        key_words = new_words.split()
        words = []
        next_words = []
        pairs = []

        for i in range(len(self.word_list)- 1):
            words.clear
            for x in range(self.order):
                if i < (len(self.word_list) - self.order):    
                    words.append(self.word_list[i + x])
            if words == key_words:
                next_words.clear()
                for x in range(self.order):
                    next_words.append(self.word_list[i + (x + 1)])
                next_words_str = ' '.join(next_words)
                pairs.append(next_words_str)  

        dictionary[new_words] = Dictogram(pairs)
        return dictionary  



    def next_chain(word_list, new_word):
        chain_list = []
        for i in range(len(word_list)-1):
            if new_word == word_list[i]:
                chain_list.append(word_list[i + 1])
        chain = Dictogram(chain_list)
        return chain


    def create_sentence(words):
        words[0] = words[0].capitalize()
        final_sentence = ' '.join(words) + '.'

        return final_sentence


if __name__ == '__main__':
    word_list = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
    print(create_sentence(path(word_list, 15)))