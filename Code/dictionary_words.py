
import random, sys

def randomize_word(filename):
    # Gets a random word from the file
    # taken from space man project
    with open(filename, "r") as f:
        dict_line = f.readlines()
        lines_stripped = [word.strip() for word in dict_line]
    return lines_stripped
    # '''Demo code 
    # file = open(filename, 'r')
    # data = file.read()
    # line = data.splitlines()
    # line = file.read().split('\n')
    # return line '''
    


''' list comprehension word_list= [random-word for _ in range(number)] '''
def word_ammount():
    line = randomize_word("/usr/share/dict/words")
    word_list = []
    for _ in range(number):
        word_list.append(random.choice(line))
    return(' '.join(word_list))


if __name__ == "__main__":
    number = int(sys.argv[1])
    print(word_ammount())