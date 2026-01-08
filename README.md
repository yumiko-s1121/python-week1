# Score Manager Web App (Week 2)

This is a simple CRUD web application for managing score records.
You can add, view, update, and delete name & score data through a web interface.

---

## What is this?

This web app lets users:

- Save name and score data
- View all saved records
- Edit a score
- Delete a record

It is a small but realistic example of a business-style web application.

---

## Features

- Add a new score record
- List all records
- Update a record (edit score)
- Delete a record
- Data is stored in a JSON file on the server

---

## Technologies

- Python (Flask)
- JavaScript (Vanilla JS)
- HTML
- JSON (as a simple database)
- Git / GitHub

---

## Project Structure

```

python-week1/
├── week2_day1_api.py
├── week2_day2_api.py
├── data.json
└── ...

js-week1/
├── week2_day1.html
├── week2_day1.js
├── week2_day2.html
└── week2_day2.js

```

---

## How to run

### 1. Start the Python API

```bash
python3 week2_day2_api.py
```

The API will run at:

```
http://127.0.0.1:5000
```

---

### 2. Open the Web UI

Open `week2_day2.html` with Live Server (VS Code).

Click **Load Records** to see saved data.

---

## API Endpoints

### Add a record

```
GET /add?name=Yumiko&score=80
```

### List records

```
GET /list
```

### Update a record

```
GET /update?id=1&score=95
```

### Delete a record

```
GET /delete?id=1
```

---

## Data Storage

All data is stored in:

```
data.json
```

Each record has this format:

```json
{
  "id": 1,
  "name": "Yumiko",
  "score": 80
}
```

---

## What I learned

* How to build REST-style APIs using Flask
* How to store and manage data using JSON files
* How to implement full CRUD (Create, Read, Update, Delete)
* How to connect JavaScript to a Python backend
* How to build a simple but realistic web application
