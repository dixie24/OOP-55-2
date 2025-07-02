import sqlite3

import sqlite3

connect = sqlite3.connect("cars.db")
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cars(
        car_model VARCHAR (40) NOT NULL,
        release_date INTEGER NOT NULL,
        description TEXT)
''')

connect.commit()


def add_new_car(car_model, release_date, desciption):
    cursor.execute(
        'INSERT INTO cars(car_model, release_date, desciption) VALUES (?,?,?)',
        (car_model, release_date, desciption)
    )
    connect.commit()
    print("new car(s) added")
    
    add_new_car('mazda rx-7', 1995, "rotor engine car")
    
    
    def get_all_cars():
        cursor.execute('SELECT car_model, release_date, desciption')

    cars = cursor.fetchall()
    print("all cars")
    
    
def update_list(car_model, rowid):
    cursor.execute(
    'UPDATE cars SET car_model = ? WHERE rowid = ?',
    (car_model, rowid)
    )

    connect.commit()
    print("cars list updated")
    
    
# def delete_car(rowid):
#     cursor.execute('DELETE FROM cars WHERE rowid = ?', (rowid,))
#     connect.commit()
# print('car deleted')
