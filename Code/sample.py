from analyzer import histogram_dict, read_words
import random
import sys


def randomizer(histogram):
    random_number = random.randint(0, len(histogram)-1)
    key = list(histogram.keys())
    return key[random_number]



if __name__ == "__main__":
    arg = f'../Code/texts/{sys.argv[1]}'
    words = histogram_dict(arg)
    print(randomizer(words))