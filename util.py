import csv
import re

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
