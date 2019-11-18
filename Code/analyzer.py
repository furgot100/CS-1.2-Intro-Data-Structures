import re

def read_words(file):
    with open(file, "r") as f:
        words = f.read().split()
    return words

def histogram(file):
    '''Reads texts. Counts a specific word in the text, returns a list of list'''
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
    '''Reads a text and counts a specific word while returning a dictionary'''
    text = read_words(file)
    histogram = {}
    for word in text:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram


def histogram_tuple(file):
    '''Reads a text and counts a specific word. Returns a list of tuples'''
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
    '''Returns the amount of unique words'''
    return len(histogram)

def frequency(word, histogram):
    '''Return amount of times a word appears in the histogram set. With list of lists of tuples'''
    for list in histogram:
        if list[0] == word:
            return list[1]

def frequency_dic(word,histogram):
    '''Return ammount of times a word appears in a histogram set. With dictionary'''
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