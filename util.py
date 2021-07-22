import csv
import re

from nltk.corpus import stopwords


def clear_word(word):
    word = re.sub(r"^\s+", "", word)
    word = word.replace('\\xa0', ' ')
    word = word.replace('\\x0', ' ')
    word = word.replace('', ' ')
    word = word.replace("//", '')
    word = re.sub(r"[^a-zA-Z0-9-\\s]", " ", word)
    return word


def array_to_csv(arr, file_name):
    file = open(file_name, 'w', newline='')
    wr = csv.writer(file)
    for x in arr:
        wr.writerow([x])


def load_stop_word():
    custom_stop_words = []
    f = open('stopword.txt', 'r')
    while True:
        line = f.readline()
        line = line.strip()
        if not line: break
        custom_stop_words.append(line)
    f.close()
    stop_words = stopwords.words('english')
    stop_words.extend(custom_stop_words)
    return stop_words


def csv_load(filename):
    arr = []
    file = open(filename, 'r')
    wr = csv.reader(file)
    for x in wr:
        arr.append(x[0])

    return arr
