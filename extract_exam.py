import csv
import random
import util


f = open('link.csv', 'r', encoding='utf-8')
fr = csv.reader(f)
exams = []

for x in fr:
    exams.append(x[0])
f.close()

result = []
for i in range(201):
    result.append(random.choice(exams))

util.array_to_csv(result,'test_data.csv')
