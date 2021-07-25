import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from numpy import nan as NA
import matplotlib.pyplot as plt

import util

df1 = pd.read_csv('plot_test.csv')

category = util.csv_load('category.csv')
df1.index = category

df1.columns.names = ['failure']

df1.index.names = ['category']

fig, ax = plt.subplots(1, 1)

df1.plot(kind='barh', ax=ax)  # bar(수직막대)

plt.show()


