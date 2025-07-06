# Personalized-plan-ai
Integrated an AI-powered personalized recovery plan system into the Soul Support app using a trained Decision Tree model. The AI interprets users' psychological test results and generates customized mental health plans in real time.
# 🤖 Personalized AI Recovery Plan – Soul Support App Module

This module powers the core AI feature in the **Soul Support** mental health app. It takes psychological test responses from users and generates a tailored recovery plan using a trained **Decision Tree Machine Learning model**.

## 💡 Goal
To provide users with **customized, evidence-based recovery recommendations** based on their mental health assessments (e.g., anxiety, depression, stress). The goal is to eliminate one-size-fits-all content and create a plan **unique to each user’s emotional state**.

---

## 🧬 How It Works

1. 🧪 The user completes a series of psychological self-assessment tests (multiple choice / Likert scale).
2. 📊 Their answers are processed into numerical features.
3. 🧠 A trained **Decision Tree Classifier** (built in Python) predicts a mental state category.
4. 📋 Based on the prediction, a custom plan is generated:
   - Daily self-care tasks
   - Journaling prompts
   - Breathing exercises
   - Affirmations
   - Referral to a therapist (if severe)

---

## 🧠 Model Overview

- **Algorithm**: Decision Tree Classifier
- **Language**: Python
- **Libraries**: scikit-learn, pandas, joblib
- **Input**: Pre-processed test answers (e.g., stress level, motivation, sleep quality)
- **Output**: Plan category (e.g., Mild Stress → Plan A)

---

## 🛠 Technologies Used

| Tool           | Purpose                           |
|----------------|------------------------------------|
| Python         | Data preprocessing, ML model       |
| scikit-learn   | Training the Decision Tree          |
| pandas         | Data manipulation                  |
| joblib         | Model saving and loading           |
| Flutter        | Frontend display of the final plan |
| Firebase       | Storing test results securely      |

---


