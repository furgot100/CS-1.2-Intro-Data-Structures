from dictogram import Dictogram, read_file
import random


def next_chain(word_list, new_word):
    chain_list = []
    for i in range(len(word_list)-1):
        if new_word == word_list[i]:
            chain_list.append(word_list[i + 1])
    chain = Dictogram(chain_list)
    return chain

def path(word_list, ammount):
    sentence = []
    histogram = Dictogram(word_list)
    nxt_word = histogram.sample()
    sentence.append(nxt_word)
    for i in range(ammount):
        chain = next_chain(word_list, nxt_word)
        next_word = chain.sample()
        sentence.append(next_word)

    return sentence

def create_sentence(words):
    words[0] = words[0].capitalize()
    final_sentence = ' '.join(words) + '.'

    return final_sentence


if __name__ == '__main__':
    word_list = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
    print(create_sentence(path(word_list, 15)))