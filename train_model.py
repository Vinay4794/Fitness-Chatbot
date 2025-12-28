import json, pickle, numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder

with open("intents.json") as file:
    data = json.load(file)

texts, labels = [], []
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        texts.append(pattern)
        labels.append(intent["tag"])

tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)
X = pad_sequences(tokenizer.texts_to_sequences(texts), maxlen=10)

encoder = LabelEncoder()
y = encoder.fit_transform(labels)

model = Sequential()
model.add(Embedding(1000, 64, input_length=10))
model.add(LSTM(64))
model.add(Dense(len(set(labels)), activation="softmax"))

model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(X, y, epochs=200, verbose=0)

model.save("model/chatbot_model.h5")
pickle.dump(tokenizer, open("model/tokenizer.pickle", "wb"))
pickle.dump(encoder, open("model/label_encoder.pickle", "wb"))
