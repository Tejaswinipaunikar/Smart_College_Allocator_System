# 🎓 Smart College Allocator System

The **Smart College Allocator System** is a web-based application that helps students find the best colleges based on their **JEE or CET scores**. It provides a user-friendly interface to enter scores and displays relevant colleges with details like **College name, branches, official websites and locations**.

---

## 🚀 Features

- 🏫 **College Finder** - Enter your JEE/CET percentile to get a list of matching colleges.
- 🔍 **Search & Filter** - Find colleges based on entrance cutoff marks.
- 💾 **Database Support** - Uses **SQLite** for efficient data management.
- 🎨 **User-Friendly Interface** - Built with **HTML, CSS, JavaScript, Flask**.

---

## 🛠️ Installation Guide

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/your-repo-url.git

## 📜 Requirements

*Before running the project, make sure you have the following installed:*

- **Python 3.x** (Recommended: Python 3.8 or later)
- **pip** (Python package manager)
- **Flask** (Web framework)
- **Flask-SQLAlchemy** (Database management)
- **Flask-WTF** (Form handling)

### Install Required Dependencies:-
    pip install flask flask-sqlalchemy flask-wtf

##Create and activate a virtual environment to manage dependencies:-
    python -m venv venv
    source venv/bin/activate   # macOS/Linux
    venv\Scripts\activate      # Windows

##Run the database update script:
    bash:- python update_db.py

##Run the Project:
    bash:- python app.py
