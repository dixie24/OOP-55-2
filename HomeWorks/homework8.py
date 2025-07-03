import sqlite3

connect = sqlite3.connect("students.db")
cursor = connect.cursor()

def create_best_math_students():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students(
            studentsid INTEGER PRIMARY KEY AUTOINCREMENT,
            fio VARCHAR (40) NOT NULL,
            age INTEGER NOT NULL
        )
    ''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades(
        gradeid INTEGER PRIMARY KEY AUTOINCREMENT,
        students INTEGER,
        subject VARCHAR (100) NOT NULL,
        grade INTEGER NOT NULL,
        FOREIGN KEY (students) REFERENCES students(studentsid)
    )
''')

connect.commit()


def add_students(fio, age):
    cursor.execute('INSERT INTO students(fio, age) VALUES (?, ?)', (fio, age))
    connect.commit()
    print(f"Пользователь {fio} добавлен")



add_students('John Doe4', 35)
add_students('John Doe5', 33)


def add_grade(studentsid, subject, grade):
    cursor.execute(
        'INSERT INTO grades(studentsid, subject, grade) VALUES (?,?,?)',
        (studentsid, subject, grade)
    )
    print(f"Оценка добавлена для пользователя с ID {studentsid}")
    connect.commit()
    
    add_grade(99, "Алгебре", 5)

def create_view_young_students():
    cursor.execute('''
        CREATE VIEW IF NOT EXISTS young_students AS
        SELECT fio, age
        FROM students
        WHERE age < 30
    ''')
    connect.commit()
    print('Представление young_students создано')

create_view_young_students()

def get_young_students():
    cursor.execute('SELECT * FROM young_students')
    students = cursor.fetchall()
    print("Молодые студенты:")
    for student in students:
        print(student)

get_young_students()
