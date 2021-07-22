import load_phrase as lp
from nltk.tokenize import TreebankWordTokenizer

import csv
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.text import Tokenizer

from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical

import util


def load_data(word_len, padding):
    # 토큰화 도구
    tokenizer = TreebankWordTokenizer()

    # 불용어 로드
    stop_words = util.load_stop_word()

    # 훈련 데이터 로드
    x_train = util.csv_load('x_train.csv')
    y_train = util.csv_load('y_train.csv')

    # 토큰화 및 불용어 제거
    for i in range(len(x_train)):
        result = []
        for w in tokenizer.tokenize(x_train[i]):
            if w not in stop_words and len(w) > 1:
                result.append(w)
        x_train[i] = result

    # 카테고리 인덱싱
    y_mapper = util.csv_load('category.csv')
    y_mapper = {word: index + 1 for index, word in enumerate(y_mapper)}
    y_train = [y_mapper[y] for y in y_train]

    # 정수 인덱싱
    tokenizer = Tokenizer(num_words=word_len)
    tokenizer.fit_on_texts(x_train)
    x_train = tokenizer.texts_to_sequences(x_train)

    print('슬라이드의 최대 길이 :{}'.format(max(len(l) for l in x_train)))
    print('슬라이드의 평균 길이 :{}'.format(sum(map(len, x_train)) / len(x_train)))
    print(tokenizer.index_word)
    plt.hist([len(s) for s in x_train], bins=50)
    plt.xlabel('length of samples')
    plt.ylabel('number of samples')
    plt.show()

    # 패딩
    x_train = pad_sequences(x_train, padding)

    # 원 핫 인코딩
    max_len = max(i for i in y_train)
    y_train = to_categorical(y_train, max_len + 1)

    return [x_train, y_train, len(y_mapper)]


load_data(1000, 45)

