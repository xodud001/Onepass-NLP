
from tensorflow.keras.models import load_model
import numpy as np

import data_loader


# 훈련 데이터 로드
word_len = 1500
padding = 40
[x_train, y_train, label_len] = data_loader.load_data(word_len, padding)

loaded_model = load_model('best_model.h5')
print("\n 테스트 정확도: %.4f" % (loaded_model.evaluate(x_train, y_train)[1]))
print(loaded_model.summary())

# predictions = loaded_model.predict(x_train)

# print(x_train[0])
# np.argmax(predictions[0])
#
# print(predictions[0][3])
