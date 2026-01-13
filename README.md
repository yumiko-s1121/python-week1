# Score Manager Web App (Week 2)

This is a secure, full-stack CRUD web application for managing score records.
The backend uses MySQL and the frontend communicates with the API via HTTP.
User authentication is implemented with hashed passwords.

---

## What is this?

This web app lets users:

- Log in with a username and password
- Save name and score data
- View all saved records
- Search records by name
- Sort records by score
- Edit a score
- Delete a record

It is a small but realistic example of a business-style web application with authentication.

---

## Features

- User login (authentication)
- Only logged-in users can add, edit, or delete records
- Add a new score record (via web UI)
- List all records
- Search records by name
- Sort records by score (ascending / descending)
- Update a record (edit score)
- Delete a record
- Input validation and error messages
- Secure password storage using hashing and salt
- Data is stored in a MySQL database

---

## Technologies

- Python (Flask)
- JavaScript (Vanilla JS)
- HTML
- MySQL
- hashlib / secrets (for password hashing)
- Git / GitHub

---

## Project Structure

```

 python-week1/
 ├── week2_day1_api.py
 ├── week2_day2_api.py
 ├── week2_day3_api.py
 ├── week2_day4_api.py
 ├── week2_day5_api.py   # MySQL + validation
 ├── week2_day6_api.py   # Login + access control
 └── week2_day7_api.py   # Hashed passwords (final)

js-week1/
├── week2_day1.html
├── week2_day1.js
├── week2_day2.html
├── week2_day2.js
├── week2_day3.html
├── week2_day3.js
├── week2_day4.html
├── week2_day4.js
├── week2_day5.html    # UI with error messages
├── week2_day5.js
├── week2_day6.html    # UI with login
└── week2_day6.js

```

---

## How to run

### 1. Initialize the database

```bash
python3 init_db.py
```
This will:
	-	Create the score_app database
	-	Create the scores and users tables
	-	Insert a demo user

⸻

### 2. Start the Python API (MySQL backend)

```bash
python3 week2_day7_api.py
```

The API will run at:

```
http://127.0.0.1:5000
```
---

### 2. Open the Web UI

Open `week2_day6.html` with Live Server (VS Code).

Click **Load Records** to see saved data.

---

## Demo Account

You can log in with:

username: demo
password: demo123

⸻

## API Endpoints
### Login

```
GET /login?username=demo&password=demo123
```

### Add a record

```
GET /add?name=Yumiko&score=80&user_id=1
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
GET /update?id=1&score=95&user_id=1
```

### Delete a record

```
GET /delete?id=1&user_id=1
```

---

## Data Storage (MySQL)

All data is stored in:

```sql
CREATE TABLE scores (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) UNIQUE,
  score INT CHECK (score BETWEEN 0 AND 100)
);

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50) UNIQUE,
  salt VARCHAR(32),
  password_hash VARCHAR(64)
);

Passwords are never stored in plain text.
They are hashed using SHA-256 with a unique salt per user.

```
```json
Example record(scores):
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
* How to add validation and database constraints
* How to display API errors in the web UI
* How to connect JavaScript to a Python backend
* How to implement user authentication
* How to store passwords securely using hashing and salt
* How to build a secure, database-backed web application
