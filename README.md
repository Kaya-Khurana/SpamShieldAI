# 🛡️ SpamShield AI

An intelligent **Email Spam Detection Web Application** built using **Python, Flask, Machine Learning, and NLP**.
SpamShield AI helps users detect **Spam**, **Not Spam**, and **Suspicious Scam** emails using a hybrid detection system.

---

## 🚀 Live Features

✅ Detect Spam Emails
✅ Detect Legitimate Emails
✅ Detect Suspicious Scam Emails
✅ Confidence Score Prediction
✅ Rule-Based Fraud Detection
✅ Machine Learning Prediction Model
✅ Clean Responsive UI
✅ Reset Button
✅ Real-Time Email Analysis

---

## 🧠 How It Works

SpamShield AI uses a **Hybrid Detection Model**:

### 🔹 Machine Learning Layer

Uses:

* TF-IDF Vectorization
* Logistic Regression / Naive Bayes Model
* Text Classification

### 🔹 Smart Rule Engine

Detects suspicious phrases such as:

* transfer money
* pay fee
* click link
* verify account
* OTP request
* virus warning
* fake interview scams

This combination improves real-world scam detection.

---

## 🛠️ Tech Stack

| Technology   | Used For        |
| ------------ | --------------- |
| Python       | Backend Logic   |
| Flask        | Web Framework   |
| Scikit-learn | ML Model        |
| Pandas       | Data Handling   |
| Joblib       | Model Saving    |
| HTML         | Frontend        |
| CSS          | Styling         |
| GitHub       | Version Control |

---

## 📁 Project Structure

```text
SpamShieldAI/
│── app.py
│── train_model.py
│── dataset.csv
│── model.pkl
│── vectorizer.pkl
│── templates/
│   └── index.html
│── static/
│   └── style.css
│── README.md
```

---

## ⚙️ Installation & Run

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Kaya-Khurana/SpamShieldAI.git
cd SpamShieldAI
```

### 2️⃣ Install Dependencies

```bash
pip install flask pandas scikit-learn joblib
```

### 3️⃣ Run Application

```bash
python app.py
```

### 4️⃣ Open Browser

```text
http://127.0.0.1:5000
```

---

## 📊 Sample Test Emails

### 🚨 Spam Example

```text
Congratulations! You won $5000. Click here now.
```

### ⚠️ Suspicious Scam Example

```text
You are selected for interview. Transfer 5K to my account.
```

### ✅ Not Spam Example

```text
Your interview is scheduled for tomorrow at 10 AM.
```

---

## 🔥 Future Enhancements

* User Login System
* Email History Dashboard
* Dark / Light Theme
* Deep Learning Model (BERT)
* Bulk Email Scanner
* API Integration
* Deployment on Render / Railway

---

## 👨‍💻 Developed By

**Kaya Khurana**

GitHub: [https://github.com/Kaya-Khurana](https://github.com/Kaya-Khurana)

---
