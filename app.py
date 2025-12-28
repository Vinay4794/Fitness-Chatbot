from flask import Flask, render_template, request, jsonify
import json, pickle, random
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

model = load_model("model/chatbot_model.h5")
tokenizer = pickle.load(open("model/tokenizer.pickle", "rb"))
encoder = pickle.load(open("model/label_encoder.pickle", "rb"))

with open("intents.json") as file:
    intents = json.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json["message"]
    seq = tokenizer.texts_to_sequences([msg])
    padded = pad_sequences(seq, maxlen=10)

    prediction = model.predict(padded)
    tag = encoder.inverse_transform([np.argmax(prediction)])

    for intent in intents["intents"]:
        if intent["tag"] == tag[0]:
            return jsonify({"reply": random.choice(intent["responses"])})

    return jsonify({"reply": "Sorry, I didn't understand that."})

if __name__ == "__main__":
    app.run(debug=True)
