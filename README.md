# 🧠 AI Mind Reader Game

An interactive AI-powered game that analyzes user responses and predicts behavioral patterns.

The app continuously asks random questions, analyzes the answers using a machine learning model, and generates a final **mind-reading style analysis** of the user's behavior.

---

## 🚀 Features

* Random question generation
* AI-based lie detection
* Behavioral pattern tracking
* Real-time probability analysis
* Interactive gameplay (stop anytime)
* Question counter
* Mind-reading prediction at the end
* Clean light-themed UI

---

## 🧠 How It Works

1. The user answers psychological questions.
2. Each response is analyzed using an NLP model.
3. The system tracks behavioral traits such as:

* Procrastination
* Discipline
* Phone addiction

4. When the user stops the game, the AI generates a behavioral analysis.

---

## 🛠 Tech Stack

* Python
* Streamlit
* Scikit-learn
* TF-IDF Vectorization
* Naive Bayes Classifier

---

## 📂 Project Structure

```
AI_lie_detector
│
├── app.py
├── train_model.py
├── generate_data.py
├── requirements.txt
├── lie_detector_model.pkl
│
└── dataset
      └── lie_truth_dataset.csv
```

---

## ▶️ Running the App

Install dependencies:

```
pip install -r requirements.txt
```

Run the app:

```
streamlit run app.py
```

---

## 🎮 Gameplay

* The AI asks random questions continuously.
* Each answer is analyzed in real time.
* The user can stop the game anytime.
* A final **AI behavioral analysis** is generated.

---

## 📊 Example Output

```
Questions Answered: 8

AI Analysis:
⚠️ You tend to procrastinate under pressure.
📱 Your phone distracts you more than you realize.

Mind Reading Accuracy: 86%
```

---

## 📌 Future Improvements

* Personality radar charts
* Sentiment analysis
* AI-generated questions
* Better NLP models
* Mobile app version

---

## 👨‍💻 Author

Built as part of a series of daily AI projects focused on machine learning and interactive applications.
