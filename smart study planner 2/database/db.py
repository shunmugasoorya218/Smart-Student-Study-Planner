import sqlite3

def connect():
    return sqlite3.connect("student.db", check_same_thread=False)

def create_tables():
    conn = connect()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        age INTEGER,
        grade TEXT,
        study_hours INTEGER
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        subject TEXT,
        level TEXT
    )
    """)

    conn.commit()
    conn.close()

# 🔥 NEW: Check existing student
def get_student(name):
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM students WHERE name=?", (name,))
    data = c.fetchone()
    conn.close()
    return data

def add_student(name, age, grade, study_hours):
    conn = connect()
    c = conn.cursor()

    existing = get_student(name)

    if existing:
        conn.close()
        return existing[0]  # return existing ID

    c.execute(
        "INSERT INTO students (name, age, grade, study_hours) VALUES (?, ?, ?, ?)",
        (name, age, grade, study_hours)
    )

    conn.commit()
    student_id = c.lastrowid
    conn.close()
    return student_id

def add_subject(student_id, subject, level):
    conn = connect()
    c = conn.cursor()
    c.execute(
        "INSERT INTO subjects (student_id, subject, level) VALUES (?, ?, ?)",
        (student_id, subject, level)
    )
    conn.commit()
    conn.close()

def get_subjects(student_id):
    conn = connect()
    c = conn.cursor()
    c.execute(
        "SELECT subject, level FROM subjects WHERE student_id=?",
        (student_id,)
    )
    data = c.fetchall()
    conn.close()
    return data
