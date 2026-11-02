<div align="center">

# 🛡️ KEYLOOM

### Password Strength Checker & Secure Password Generator

**Check smarter. Generate stronger. Stay safer.**

<p>
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-Web%20App-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JS-EA6B35?style=for-the-badge" alt="Frontend">
  <img src="https://img.shields.io/badge/Status-Mini%20Project-16A085?style=for-the-badge" alt="Project">
</p>

</div>

---

## ✦ Project Overview

**KeyLoom** is a Python mini project built with Flask. It provides two password tools in one responsive, dark-themed web interface:

- **Password Checker** — evaluates a password as **Easy**, **Medium**, or **Difficult** using length, character variety, and common predictable patterns.
- **Password Generator** — creates random passwords using Python's `secrets` module and lets users choose which character groups to include.

The interface includes a live strength meter, improvement suggestions, show/hide, copy, and regenerate controls.

## ⚡ Features

| Feature | What it does |
|---|---|
| Live strength check | Updates the rating as the user types |
| Three strength levels | Easy, Medium, and Difficult |
| Pattern detection | Checks common words, sequences, repeated characters, and predictable layouts |
| Improvement tips | Suggests ways to make a password harder to guess |
| Secure generator | Uses Python's `secrets` module |
| Custom length | Generates passwords from 8 to 15 characters |
| Character options | Uppercase, lowercase, numbers, and symbols |
| Convenience controls | Show/Hide, Copy, and Regenerate |
| Responsive interface | Dark UI designed for desktop and mobile |

## 🧠 How KeyLoom Works

### 1. Password checker

The checker evaluates a password using a simple set of rules:

```text
                 USER PASSWORD
                       │
                       ▼
              CHARACTER ANALYSIS
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
        Length       Variety      Patterns
          │            │            │
          └────────────┼────────────┘
                       ▼
                STRENGTH RATING
                       │
             ┌─────────┼─────────┐
             ▼         ▼         ▼
           EASY     MEDIUM   DIFFICULT
                       │
                       ▼
                IMPROVEMENT TIPS
```

The checker looks for:
- Short passwords and limited character variety
- Common words and simple substitutions
- Sequential patterns such as `123` or `abc`
- Three or more repeated characters
- Predictable arrangements such as a word followed by numbers or symbols

### 2. Password generator

```text
       SELECT PASSWORD OPTIONS
                  │
                  ▼
          PYTHON secrets MODULE
                  │
                  ▼
        SECURE RANDOM SELECTION
                  │
                  ▼
          GENERATED PASSWORD
                  │
           ┌──────┴──────┐
           ▼             ▼
          COPY        REGENERATE
```

The generator uses Python's `secrets` module rather than the ordinary `random` module.

## 🧰 Technology Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Password generation | Python `secrets` |
| Frontend | HTML5, CSS3, JavaScript |
| UI | Responsive dark theme |
| Templating | Jinja2 (included with Flask) |

## 📁 Project Structure

```text
keyloom/
│
├── app.py                 # Flask application and routes
├── password_utils.py      # Password rating and secure generation
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── .gitignore             # Files excluded from Git
│
└── templates/
    └── index.html         # Main responsive web interface
```

## 🚀 Run Locally

### Prerequisites

- Python 3.10 or newer
- pip (Python package installer)
- A web browser

### Step 1 — Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/keyloom.git
cd keyloom
```

### Step 2 — Create a virtual environment

**Windows PowerShell**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3 — Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4 — Start the application

```bash
python app.py
```

### Step 5 — Open KeyLoom

Visit:

```text
http://127.0.0.1:5000
```

## 🔐 Privacy & Security Notes

- Password checking happens in the browser; the checker form does not submit the typed password to Flask.
- Password generation uses Python's `secrets` module.
- Generated passwords are returned to the browser for display. Do not use this demo as a substitute for a professionally audited password manager.
- The strength checker is a rule-based educational estimate, not a guarantee that a password is secure.
- Use unique passwords for every account and store them in a trusted password manager.

## 👥 Team

**KeyLoom was developed as a team mini project.**

- **Sujal Ghorpade** — Project author / team member
- **Additional team contributors:** Add the names of all team members here.

## 🌟 Project Goal

To make basic password awareness practical and accessible through a simple web application that combines password evaluation with secure random password generation.

---

<div align="center">

**KEYLOOM — Make every password count.** 🛡️

</div>
