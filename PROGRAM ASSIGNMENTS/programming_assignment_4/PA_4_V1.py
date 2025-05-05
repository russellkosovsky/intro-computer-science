# Program Assignment 4
# Russell Kosovsky

def byFreq(pair):
    return pair[1]


def main():
    
    print('This program analyzes wor frequency in a file')
    print('and prints a report on the n most frequent words.\n')

    # get the sequence of words from the file
    fname = input("file to analyze: ")
    text = open(fname, 'r').read()
    for ch in "!'\"#$%&()*+,-./:;<=>?@[\\]^_{|}~":
        text = text.replace(ch, '')

    words = text.split()
    
    stopwords = open('stopwords.txt', "r").read()
    stopwords = stopwords.lower()
    stopwords = stopwords.split()


    # create dictionary of word counts
    counts = {}

    for w in words:
        if w not in stopwords:
            counts[w] = counts.get(w, 0) + 1

    # output analysis of n most frequent words
    n = eval(input('Output analysis of how many words? '))
    items = list(counts.items())
    items.sort()
    items.sort(key=byFreq, reverse=True)
    for i in range(n):
        word, count = items[i]
        print("{0:<15}{1:>5}".format(word, count))


if __name__ == '__main__': main()
