import sqlite3
my_users = sqlite3.connect('my_users.db', check_same_thread=False)

sql = my_users.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT, number TEXT, latitude REAL, '
            'longitude REAL);')

def register(id, name, number, latitude, longitude):
    sql.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?);', (id, name, number, latitude, longitude))
    my_users.commit()

def check(tg_id):
    if sql.execute('SELECT * FROM users WHERE id = ?', (tg_id,)).fetchone():
        return True
    else:
        return False


