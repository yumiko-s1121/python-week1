# Score Manager Web App (Week 2)

This is a simple CRUD web application for managing score records.
The backend uses MySQL, and the frontend communicates with the API via HTTP.

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

- Add a new score record (via web UI)
- List all records
- Search records by name
- Sort records by score (ascending / descending)
- Update a record (edit score)
- Delete a record
- Data is stored in a MySQL database

---

## Technologies

- Python (Flask)
- JavaScript (Vanilla JS)
- HTML
- MySQL
- Git / GitHub

---

## Project Structure

```

python-week1/
├── week2_day1_api.py
├── week2_day2_api.py
├── week2_day3_api.py
├── week2_day4_api.py   # MySQL backend
└── ...

js-week1/
├── week2_day1.html
├── week2_day1.js
├── week2_day2.html
├── week2_day2.js
├── week2_day3.html
├── week2_day3.js
├── week2_day4.html    # Add + Search + Sort UI
└── week2_day4.js

```

---

## How to run

### 1. Start the Python API

```bash
python3 week2_day4_api.py
```

The API will run at:

```
http://127.0.0.1:5000
```

---

### 2. Open the Web UI

Open `week2_day4.html` with Live Server (VS Code).

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

### Search by name
```
GET /list?name=Yu
```

### Sort by score (ascending)
```
GET /list?sort=score
```

### Sort by score (descending)
```
GET /list?sort=score_desc
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

## Data Storage (My SQL)

All data is stored in:

```sql
CREATE TABLE scores (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  score INT
);
```
```json
Example record:
{
  "id": 1,
  "name": "Yumiko",
  "score": 80
}
```

---

## What I learned

* How to build REST-style APIs using Flask
* How to store and manage data using a MySQL database
* How to implement full CRUD (Create, Read, Update, Delete)
* How to connect JavaScript to a Python backend
* How to build a simple but realistic web application
* How to implement searching and sorting in an API
