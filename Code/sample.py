from analyzer import histogram_dict, read_words
import random
import sys
import pytest

# def randomizer(histogram):
#     random_number = random.randint(0, len(histogram)-1)
#     key = list(histogram.keys())
#     return key[random_number]

def sample_frequency(histogram):
    frequency_list = []
    
    for key, value in histogram.items():
        [frequency_list.append(key) for i in range(value)]
    random_index = random.randint(0, len(frequency_list) - 1)

    return frequency_list[random_index]


def test_sample_frequency():
    frequency_dict = {}
    words = histogram_dict('../Code/texts/test.txt')
    for i in range(100000):
        sample_word = sample_frequency(words)
        if sample_word in frequency_dict:
            frequency_dict[sample_word] += 1
        else:
            frequency_dict[sample_word] = 1
    return frequency_dict


def sentences(histogram, ammount=10):
    word = []
    for i in range(ammount):
        word.append(sample_frequency(histogram))
    sentence = ' '.join(word)

    return sentence



if __name__ == "__main__":
    arg = f'../Code/texts/{sys.argv[1]}'
    words = histogram_dict(arg)
    print(sentences(words, 15))