
from tensorflow.keras.models import load_model
import numpy as np

import data_loader
import util
import csv
import matplotlib.pyplot as plt
import pandas as pd

# 훈련 데이터 로드
word_len = 1200
padding = 43
[x_train, y_train, label_len] = data_loader.load_data(word_len, padding)

loaded_model = load_model('./models/2021_07_23_1245.h5')
print("\n 테스트 정확도: %.4f" % (loaded_model.evaluate(x_train, y_train)[1]))
print(loaded_model.summary())

x_test = data_loader.load_test_data(1200, 53)
predictions = loaded_model.predict(x_test)

# x_train = util.csv_load('x_train.csv')
# y_train = util.csv_load('y_train.csv')
y_mapper = util.csv_load('category.csv')

x_test = util.csv_load('cleared_text.csv')

graph = [0 for i in range(len(y_mapper))]

# for i, prediction in enumerate(predictions):
#     result = list(prediction)
#     index = result.index(max(result))
#     print(x_train[i])
#     print('expected : ' + y_mapper[index])
#     print('real : ' + y_train[i])
#     if y_mapper[index] != y_train[i]:
#         graph[index] += 1

for i, prediction in enumerate(predictions):
    result = list(prediction)
    index = result.index(max(result))
    print(x_test[i])
    print('expected : ' + y_mapper[index])



# file = open('plot_test2.csv', 'w', newline='')
# wr = csv.writer(file)
# wr.writerow(['c1'])
# for i, x in enumerate(graph):
#     wr.writerow([x])





