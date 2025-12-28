The Fitness Chatbot is an intelligent, interactive web-based application designed to assist users with fitness-related queries such as workouts, exercises, diet plans, nutrition, daily fitness habits, and healthy lifestyle guidance.

The chatbot uses Natural Language Processing (NLP) and Deep Learning (RNN/LSTM) techniques to understand user intent and respond appropriately.
The frontend is built using HTML and CSS, while the backend is developed using Python (Flask).
No database is used in this project.


# Key Features

Interactive fitness chatbot interface

Supports beginner, intermediate, and advanced fitness queries

Exercise guidance by body part (chest, back, legs, arms, core, shoulders)

Diet and nutrition guidance including:

Protein-rich foods

Carbohydrates, fats, vitamins, and minerals

Weight loss and weight gain diets

Handles day-to-day fitness questions

Uses intent classification with NLP and LSTM

Simple and responsive UI

Lightweight and easy to run locally


# Technologies Used

Frontend

HTML

CSS

Backend

Python

Flask

AI / ML

Natural Language Processing (NLP)

Recurrent Neural Network (RNN)

Long Short-Term Memory (LSTM)

Tools

VS Code

GitHub


# Project Structure

fitness-chatbot/
│
├── app.py                 # Flask backend
├── train_model.py         # Model training script
├── intents.json           # All chatbot intents
├── chatbot_model.h5       # Trained LSTM model
├── words.pkl              # Vocabulary
├── classes.pkl            # Intent classes
│
├── templates/
│   └── index.html         # Frontend HTML
│
├── static/
│   └── style.css          # CSS styling
│
└── README.md              # Project documentation


# How It Works

User enters a fitness-related query in the chatbot UI

The input is preprocessed using NLP techniques

The trained LSTM model predicts the intent

A suitable response is selected from intents.json

The response is displayed in the chatbot interface


# How to Run the Project (VS Code)

## 1️⃣ Clone the Repository
git clone https://github.com/your-username/fitness-chatbot.git
cd fitness-chatbot

## 2️⃣ Install Required Libraries
pip install flask numpy nltk tensorflow

## 3️⃣ Train the Model (Optional – only once)
python train_model.py

## 4️⃣ Run the Application
python app.py

## 5️⃣ Open in Browser
http://127.0.0.1:5000/


# Sample Queries

“Workout for beginners”

“Chest exercises”

“Protein rich foods”

“How to lose weight”

“Diet plan for muscle gain”

“Is walking enough for fitness?”

“Exercises for abs”


# Dataset

The chatbot uses a custom intents.json file

Contains hundreds of fitness-related patterns

Covers:

Common questions

Exercises

Diet plans

Nutrition details

Lifestyle guidance


# Academic Relevance

This project demonstrates:

Practical application of NLP

Use of Deep Learning (LSTM) for intent classification

Integration of ML models with a web application

Clean separation of frontend and backend

## Suitable for:

Mini projects

Final year projects

NLP / AI coursework

Project demonstrations and viva


# Future Enhancements

Add user authentication

Integrate calorie and BMI calculators

Store chat history using a database

Deploy on cloud platforms (Render, Heroku, AWS)

Add voice input support


# License

This project is for educational purposes only.
