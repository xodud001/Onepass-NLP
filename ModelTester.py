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
# [x_train, y_train, label_len] = data_loader.load_data(word_len, padding)

loaded_model = load_model('./models/2021_07_23_1245.h5')
# print("\n 테스트 정확도: %.4f" % (loaded_model.evaluate(x_train, y_train)[1]))
# print(loaded_model.summary())

file_path = 'exam.csv'
x_test = data_loader.load_test_data(padding, file_path)
predictions = loaded_model.predict(x_test)

# x_train = util.csv_load('x_train.csv')
# y_train = util.csv_load('y_train.csv')
y_mapper = util.csv_load('category.csv')

# x_test = util.csv_load(file_path)

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
    copied_result = list.copy(result)
    list.sort(copied_result, reverse=True)
    copied_result = copied_result[0:3]
    for j, score in enumerate(copied_result):
        index = result.index(score)
        print(str(i + 1) + '번째, expected : ' + y_mapper[index] + ', percent : ' + str(
            round(copied_result[j] * 100, 2)) + '%')
        obj = {
            'question_id': i + 1,
            'category_id': result.index(score),
            'score': score
        }
        print(obj)
    # print(x_test[i])


# file = open('plot_test2.csv', 'w', newline='')
# wr = csv.writer(file)
# wr.writerow(['c1'])
# for i, x in enumerate(graph):
#     wr.writerow([x])
