# Score Checking Web App (Week 2)

<!--
This repository contains a simple web application
that saves scores and checks whether a user passes or fails.
-->

## What is this?
This is a simple score checking web app.
Users enter a name, a score, and a pass line.
The app tells whether the user passed or failed.

---

## Technologies
- Python (Flask)
- JavaScript
- HTML
- GitHub

---

## How to run

### 1. Start the Python API
```bash
python3 week2_day1_api.py
```

### 2. Open day7.html with Live Server

### 3. Enter name, score, and pass line

## API

### Add a record
GET /add?name=Yumiko&score=80

### List records
GET /list

Data is stored in a JSON file (data.json).