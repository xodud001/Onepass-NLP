
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

from sklearn.model_selection import train_test_split


from tensorflow.keras import optimizers

import data_loader

word_len = 1000
padding = 45
[x_train, y_train, label_len] = data_loader.load_data(word_len, padding)

x_train, x_valid, y_train, y_valid = train_test_split(x_train, y_train, test_size=0.15, shuffle=True, stratify=y_train, random_state=34)

model = Sequential()
model.add(Embedding(word_len, 40))
model.add(LSTM(40))
model.add(Dense(label_len + 1, activation='softmax'))

es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=4)
mc = ModelCheckpoint('best_model.h5', monitor='val_acc', mode='max', verbose=1, save_best_only=True)

model.compile(loss='binary_crossentropy',
  optimizer=optimizers.RMSprop(lr=2e-5),
  metrics=['acc'])

history = model.fit(x_train, y_train, batch_size=32, epochs=100, callbacks=[es, mc], validation_data=(x_valid, y_valid))

print(history)





