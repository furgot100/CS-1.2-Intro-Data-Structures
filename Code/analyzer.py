import re

def read_words(file):
    with open(file, "r") as f:
        words = f.read().split()
    return words

def histogram(file):
    text = read_words(file)
    histogram = []
    for word in text:
        is_updated = False
        for list in histogram:
            if list[0] == word:
                list[1] += 1
                is_updated = True
        if is_updated == False:
            histogram.append([word,1])
    return histogram

def histogram_dict(file):
    text = read_words(file)
    histogram = {}
    for word in text:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram


def histogram_tuple(file):
    text = read_words(file)
    histogram = []
    amount = 0
    for word in text:
        print(histogram)
        is_updated = False
        for tuple in histogram:
            if tuple[0] == word:
                amount = tuple[1] +1
                histogram.remove(tuple)
                histogram.append((word,amount))
                is_updated = True
        if is_updated == False:
            histogram.append((word, 1))
    return histogram

def unique_words(histogram):
    return len(histogram)

def frequency(word, histogram):
    for list in histogram:
        if list[0] == word:
            return list[1]

def frequency_dic(word,histogram):
    for i, keys in histogram.items():
        if i == word:
            return keys

if __name__ == "__main__":
    histogram = (histogram('texts/test.txt'))
    unique_words = unique_words(histogram)
    word = 'fish' 
    word_frequency = frequency(word,histogram)

    # print(histogram)
    print(f'Unique words: {unique_words}')
    print(f'Amount of "{word}": {word_frequency}' )

    histogram_dict = (histogram_dict('texts/test.txt'))
    word_frequency_dict = frequency_dic(word, histogram_dict)
    print(histogram_dict)
    # print(word_frequency_dict)