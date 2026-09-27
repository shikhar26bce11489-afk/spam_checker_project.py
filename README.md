# 🔐 Local Spam / Scam Message Checker

A simple **Python-based spam and scam message detection system** that analyzes text messages for common suspicious patterns and calculates a **risk score from 0 to 100**.

The project uses **regular expressions (Regex)** to identify warning signs such as urgent language, money requests, fake authority claims, requests for personal information, and suspicious links.

---

## 📌 Features

* 🔍 Detects common spam/scam indicators
* 📊 Calculates a risk score from **0–100**
* ⚠️ Classifies messages into:

  * **LOW RISK**
  * **MEDIUM RISK**
  * **HIGH RISK**
* 🏦 Detects fake authority references such as banks, police, courier companies, etc.
* 💰 Detects money-related requests
* 🔑 Detects requests for sensitive information such as OTP, PIN, CVV, passwords, PAN, Aadhaar, etc.
* 🔗 Detects suspicious URLs and URL-shortening services
* 🚨 Detects urgent or threatening language
* 📝 Displays the reasons why a message was flagged
* 💻 Runs locally using Python — no internet connection or external API required

---

## 🛠️ Technologies Used

* **Python 3**
* **Regular Expressions (`re` module)**

No external Python libraries are required.

---

## 📂 Project Structure

```text
Local-Spam-Scam-Message-Checker/
│
├── spam_checker.py
└── README.md
```

> Replace `spam_checker.py` with the actual filename of your Python program if it is different.

---

## ⚙️ How It Works

The program checks the input message against five major categories.

| Category                    | Risk Points | Examples                                        |
| --------------------------- | ----------: | ----------------------------------------------- |
| Urgent Language             |          65 | `urgent`, `immediately`, `last chance`          |
| Money Related Message       |          80 | `send money`, `transfer`, `gift card`, `crypto` |
| Fake Authority              |          70 | `bank`, `police`, `income tax`, `courier`       |
| Asking Personal Information |          90 | `OTP`, `password`, `PIN`, `CVV`, `PAN`          |
| Suspicious Links            |          60 | `http://`, `https://`, `bit.ly`, `tinyurl`      |

Each category is counted **only once**, even if multiple patterns from the same category are found.

After calculating the score, the program limits it to a maximum of **100**.

---

## 📊 Risk Classification

The final score is classified as follows:

```text
0 – 39     → LOW RISK
40 – 74    → MEDIUM RISK
75 – 100   → HIGH RISK
```

### Low Risk

The message does not contain strong spam/scam indicators.

### Medium Risk

The message contains one or more suspicious indicators. The user should verify the message before taking action.

### High Risk

The message contains multiple strong indicators commonly associated with scams.

> **Note:** This is a rule-based detector and should not be treated as a definitive scam detector. A legitimate message can sometimes contain suspicious keywords, and a scam can avoid the patterns used by this program.

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Local-Spam-Scam-Message-Checker.git
```

### 2. Open the project directory

```bash
cd Local-Spam-Scam-Message-Checker
```

### 3. Make sure Python is installed

Check your Python version:

```bash
python --version
```

Python 3.x is recommended.

---

## ▶️ How to Run

Run the Python file:

```bash
python spam_checker.py
```

The program will display:

```text
===== Local Spam / Scam Message Checker ====
Paste the message below (press Enter twice to check ):
```

Enter the message you want to analyze.

Press **Enter twice** to finish entering the message.

---

## 💡 Example

### Input

```text
URGENT! Your bank account will be blocked immediately.
Send money within 24 hours and provide your OTP.
Click https://example.com to verify your account.
```

### Output

```text
=============================================
Risk Score : 100/100
Status : HIGH RISK (LIKELY SCAM/SCAM)
REASON  : Urgent language, Money related message,
          Fake Authority, Asking personal info,
          Suspicious links
=============================================
```

---

## 🧠 Detection Logic

The project uses Python's built-in `re` module for pattern matching.

For example:

```python
if re.search(pattern, spamnotification):
    score += data["risk points"]
```

This searches the input message for predefined suspicious patterns.

The program uses:

```python
spamnotification.lower().strip()
```

to normalize the message before checking it.

This allows patterns such as:

```text
OTP
Otp
otp
```

to be detected consistently.

---

## 🔎 Example Detection Patterns

### Urgent Language

```python
r"urgent"
r"immediately"
r"within 24 hours"
r"last chance"
```

### Money Related Messages

```python
r"send money"
r"transfer"
r"pay now"
r"gift card"
r"deposit"
r"crypto"
r"account details"
r"wallet"
```

### Fake Authority

```python
r"bank"
r"police"
r"income tax"
r"customs"
r"courier"
r"amazon"
r"flipkart"
r"cyber cell"
r"microsoft"
```

### Personal Information

```python
r"otp"
r"password"
r"pin"
r"cvv"
r"account number"
r"ifsc"
r"adhaar"
r"pan"
```

### Suspicious Links

```python
r"http[s]?://"
r"bit\.ly"
r"tinyurl"
r"goo.gl"
r"check below"
```

---

## 🎯 Project Objective

The main objective of this project is to demonstrate how **rule-based text analysis and regular expressions** can be used to identify potentially suspicious messages.

The project is designed as a simple educational implementation and can serve as a starting point for developing more advanced spam/scam detection systems.

---

## 🔮 Future Improvements

Possible improvements include:

* [ ] Add a graphical user interface (GUI)
* [ ] Add a web-based interface
* [ ] Detect suspicious email addresses
* [ ] Detect phone numbers commonly used in scam messages
* [ ] Improve pattern matching using NLP
* [ ] Add machine-learning-based classification
* [ ] Store scan history
* [ ] Export results to CSV/PDF
* [ ] Add customizable risk scores
* [ ] Support multiple languages
* [ ] Detect suspicious domains more intelligently
* [ ] Add unit tests
* [ ] Improve false-positive handling

---

## ⚠️ Limitations

This project uses a **keyword and regular-expression-based approach**.

Therefore:

* It may produce false positives.
* It may miss sophisticated scams.
* The presence of a keyword does not necessarily mean that a message is malicious.
* It does not verify URLs or websites.
* It does not use machine learning.
* It does not connect to external threat-intelligence databases.

The result should therefore be considered a **risk indication**, not a final determination that a message is a scam.

---

## 🔒 Privacy

This program processes messages **locally on the user's computer**.

The current implementation does not send messages to an external server or API.

---

## 📚 Learning Concepts

This project demonstrates several useful Python concepts:

* Functions
* Dictionaries
* Lists
* Loops
* Conditional statements
* Regular expressions
* String manipulation
* User input
* Risk scoring
* Basic rule-based classification




## 👨‍💻 Author

Shikhar Mishra

