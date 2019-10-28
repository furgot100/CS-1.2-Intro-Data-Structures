import random
import sys

def rearrange(word):
    words = []

    while len(word) != 0:
        shuffle_word = random.choice(word)
        words.append(shuffle_word)
        word.remove(shuffle_word)
    return(' '.join(words))

if __name__ == '__main__':
    params = sys.argv[1:]
    # random.shuffle(params) Eazy way to do it.
    shuffled = rearrange(params)
    print(shuffled)
