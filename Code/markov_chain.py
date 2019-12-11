from dictogram import Dictogram, read_file
import random


class Markov():
    def __init__(self, word_list, amount,order=2):
        """Initilize starting variables"""
        self.word_list = word_list
        self.amount = amount
        self.order = order

    def higher_order(self, new_words):
        """ Goes through word_list and combines two words in a string.
        The amount of words is based on the order number. Checks if
        string matches and combines with the string"""
        dictionary = dict()
        key_words = new_words.split()
        words = []
        next_words = []
        pairs = []

        for i in range(len(self.word_list)- 1):
            words *= 0
            for x in range(self.order):
                if i < (len(self.word_list) - self.order):    
                    words.append(self.word_list[i + x])
            if words == key_words:
                next_words *= 0
                for x in range(self.order):
                    next_words.append(self.word_list[i + (x + 1)])
                next_words_str = ' '.join(next_words)
                pairs.append(next_words_str)  

        dictionary[new_words] = Dictogram(pairs)
        return dictionary

    def sample(self):
        """The first word to start the chain"""
        next_words = []
        main_histogram = Dictogram(self.word_list)

        next_word = main_histogram.sample()
        next_words.append(next_word)
        chain = self.next_chain(next_word)

        for i in range(self.order - 1):
            if len(chain) > 0:
                word_next = chain.sample()
                next_words.append(word_next)
                chain = self.next_chain(word_next)
        sample = " ".join(next_words)
        return sample  

    def walk(self):
        """Uses initial word and begins chain."""
        sentence = []
        next_words = []

        words_str = self.sample()
        sentence.append(words_str)

        for i in range(self.amount - self.order):
            next_words *= 0
            chain = self.higher_order(words_str)
            if len(chain[words_str]) > 0:
                words_str = chain[words_str].sample()
                next_words = words_str.split()
                sentence.append(next_words[self.order - 1])
        sentence = " ".join(sentence)
        return sentence

    def next_chain(self, new_word):
        """Appends next word in the list if it is equal to new_word
        creates histogram with the words"""
        chain_list = []
        for i in range(len(self.word_list) - 1):
            if new_word == self.word_list[i]:
                chain_list.append(self.word_list[i + 1])
        
        chain = Dictogram(chain_list)
        return chain

    def create_sentence(self, words):
        """Combines word into a 'coherent' sentence"""
        split_words = words.split()
        split_words[0] = split_words[0].capitalize()

        final_sentence = ' '.join(split_words) + '.'

        return final_sentence

    def main(self):
        words = self.walk()
        sentence = self.create_sentence(words)
        return sentence

if __name__ == '__main__':
    word_list = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
    markov = Markov(word_list, 15)
    print(markov.main())