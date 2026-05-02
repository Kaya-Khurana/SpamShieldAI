from flask import Flask, render_template, request
import joblib
import re

app = Flask(__name__)

# Load trained model + vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Scam / suspicious regex patterns
suspicious_patterns = [
    r"transfer.*account",
    r"send.*money",
    r"pay.*fee",
    r"deposit.*amount",
    r"bank account",
    r"account number",
    r"upi",
    r"wallet",
    r"otp",
    r"\b\d+\s?(usd|inr|rs|dollar|eur)\b",
    r"click.*link",
    r"verify.*account",
    r"urgent action",
    r"password expired",
    r"you won",
    r"claim prize",
    r"virus detected",
    r"windows has virus",
    r"transfer"
]

# Legitimate business / meeting keywords
legit_patterns = [
    "appointment",
    "meeting",
    "interview",
    "hr",
    "schedule",
    "teams.microsoft.com",
    "google meet",
    "zoom",
    "reschedule",
    "calendar"
]

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    confidence = ""
    message = ""

    if request.method == "POST":
        message = request.form["message"]
        text = message.lower()

        suspicious_found = any(re.search(p, text) for p in suspicious_patterns)
        legit_found = any(word in text for word in legit_patterns)

        # Mixed-content scam detection
        if suspicious_found and legit_found:
            result = "Suspicious Scam ⚠️"
            confidence = "99%"

        # Direct spam/scam
        elif suspicious_found:
            result = "Spam 🚨"
            confidence = "98%"

        else:
            # ML model prediction
            data = vectorizer.transform([text])

            try:
                prob = model.predict_proba(data)[0][1]   # spam probability
            except:
                pred = model.predict(data)[0]
                prob = 0.8 if pred == 1 else 0.2

            if prob >= 0.70:
                result = "Spam 🚨"
                confidence = str(round(prob * 100, 2)) + "%"
            else:
                result = "Not Spam ✅"
                confidence = str(round((1 - prob) * 100, 2)) + "%"

    return render_template(
        "index.html",
        result=result,
        confidence=confidence,
        message=message
    )

if __name__ == "__main__":
    app.run(debug=True) 