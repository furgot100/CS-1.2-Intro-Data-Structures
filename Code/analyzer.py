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

def unique_words(histogram):
    counter = 0
    for list in histogram:
        counter += 1
    return counter

def frequency(word, histogram):
    for list in histogram:
        if list[0] == word:
            return list[1]


if __name__ == "__main__":
    histogram = (histogram('texts/test.txt'))
    unique_words = unique_words(histogram)
    word = 'sleep' 
    word_frequency = frequency(word,histogram)

    print(histogram)
    print(f'Unique words: {unique_words}')
    print(f'Amount of "{word}": {word_frequency}' )
