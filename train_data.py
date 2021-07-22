import load_phrase as lp
from nltk.corpus import stopwords
from nltk.tokenize import TreebankWordTokenizer
import csv
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.text import Tokenizer

from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.models import load_model

from tensorflow.keras import optimizers

import numpy as np

# 토큰화 도구
tokenizer = TreebankWordTokenizer()

# 사용자 정의 불용어 파일 로드
custom_stop_words = []
f = open('stopword.txt', 'r')
while True:
    line = f.readline()
    line = line.strip()
    if not line: break
    custom_stop_words.append(line)
f.close()

# 불용어 리스트 생성
stop_words = stopwords.words('english')
stop_words.extend(custom_stop_words)

# 훈련 데이터 로드
x_train = []
y_train = []

x_train_file = open('x_train.csv', 'r')
y_train_file = open('y_train.csv', 'r')
wr = csv.reader(x_train_file)
for x in wr:
    x_train.append(x[0])

wr = csv.reader(y_train_file)
for y in wr:
    y_train.append(y[0])

# 토큰화 및 불용어 제거
for i in range(len(x_train)):
    result = []
    for w in tokenizer.tokenize(x_train[i]):
        if w not in stop_words and len(w) > 1:
            result.append(w)
    x_train[i] = result

# 카테고리 인덱싱
y_mapper = set(y_train)
# f = open('category.txt', 'w') 카테고리 텍스트 파일로 저장
# for y in y_mapper:
#     f.write(y+'\n')
y_mapper = {word: index + 1 for index, word in enumerate(y_mapper)}
y_train = [y_mapper[y] for y in y_train]

# 정수 인덱싱
word_len = 1500
tokenizer = Tokenizer(num_words=word_len)
tokenizer.fit_on_texts(x_train)
x_train = tokenizer.texts_to_sequences(x_train)

# print('슬라이드의 최대 길이 :{}'.format(max(len(l) for l in x_train)))
# print('슬라이드의 평균 길이 :{}'.format(sum(map(len, x_train))/len(x_train)))
# print(tokenizer.index_word)
# plt.hist([len(s) for s in x_train], bins=50)
# plt.xlabel('length of samples')
# plt.ylabel('number of samples')
# plt.show()

# 패딩
max_len = 40
x_train = pad_sequences(x_train, max_len)

# 원 핫 인코딩
max_len = max(i for i in y_train)
y_train = to_categorical(y_train, max_len + 1)

# model = Sequential()
# model.add(Embedding(word_len, 120))
# model.add(LSTM(120))
# model.add(Dense(len(y_mapper) + 1, activation='softmax'))
#
# es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=4)
# mc = ModelCheckpoint('best_model.h5', monitor='val_acc', mode='max', verbose=1, save_best_only=True)
#
# model.compile(loss='binary_crossentropy',
#   optimizer=optimizers.RMSprop(lr=2e-5),
#   metrics=['acc'])
#
# history = model.fit(x_train, y_train, batch_size=128, epochs=500, callbacks=[es, mc], validation_data=(x_train, y_train))

loaded_model = load_model('best_model.h5')
print("\n 테스트 정확도: %.4f" % (loaded_model.evaluate(x_train, y_train)[1]))
# print(loaded_model.summary())
#
# predictions = loaded_model.predict(x_train)
#
# print(x_train[0])
# np.argmax(predictions[0])

# print(predictions[0][3])


