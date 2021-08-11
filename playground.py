
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

from sklearn.model_selection import train_test_split

from pymongo import MongoClient

from tensorflow.keras import optimizers
from tensorflow.python.keras.layers import Dropout

import data_loader

word_len = 1200
padding = 53
[x_train, y_train, label_len] = data_loader.load_data(word_len, padding)

x_train, x_valid, y_train, y_valid = train_test_split(x_train, y_train, test_size=0.15, shuffle=True, stratify=y_train, random_state=34)

model = Sequential()
model.add(Embedding(word_len, 80))
model.add(LSTM(80))
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(label_len, activation='softmax'))



es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=4)
mc = ModelCheckpoint('best_model.h5', monitor='val_acc', mode='max', verbose=1, save_best_only=True)
#
# model.compile(loss='binary_crossentropy',
#   optimizer=optimizers.RMSprop(lr=2e-5),
#   metrics=['acc'])

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])

history = model.fit(x_train, y_train, batch_size=32, epochs=100, callbacks=[es, mc], validation_data=(x_valid, y_valid))

print(history)


# connection_string = "mongodb://user1:1528@52.78.23.245/train"
# client = MongoClient(connection_string)
#
# db_handle = client['train']
# collection_name = db_handle['model']

layers = []
for layer in history.model.layers:
    layers.append(layer.name)

trained_model = {
    'epoch': len(history.epoch),
    'loss': history.history['loss'],
    'acc': history.history['acc'],
    'val_loss': history.history['val_loss'],
    'val_acc': history.history['val_acc'],
    'model_layer': layers
}

print(trained_model)
# collection_name.insert()
# count = collection_name.count()
