import sqlite3
from datetime import datetime


#define connection and cursor

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

def get_data_connection():
    connection = sqlite3.connect('data.db')
    return connection

#create stores table
def create_tables(db):
    cur = cursor
    cur.execute("""CREATE TABLE IF NOT EXISTS counter (
        name TEXT PRIMARY KEY,
        description TEXT)""")

    cur.execute("""CREATE TABLE IF NOT EXISTS tracker (
        date TEXT,
        counterName TEXT,
        FOREIGN KEY (counterName) REFERENCES counter(name)
    )""")

    connection.commit()

#add habit name and description
def add_counter(db, name, description):
    cur = cursor
    try:
        cur.execute("INSERT INTO counter VALUES (?,?)", (name, description))
    except sqlite3.IntegrityError:
        cur.execute("UPDATE counter SET description = ? WHERE name = ?", (description, name))
    connection.commit()

#increment counter for habit 
def increment_counter(connection, name, instance_date = None):
    cur = cursor
    if not instance_date:
        from datetime import datetime
        instance_date = str(datetime.now())
    cur.execute("INSERT INTO tracker VALUES (?,?)", (instance_date, name, ))
    connection.commit()

def get_counter_data(name):
    cur = cursor
    cur.execute("SELECT * FROM tracker WHERE counterName = ?", (name,))
    result = cur.fetchall()
    connection.commit()
    return result


def output_table():
    cur = cursor
    cur.execute("SELECT * FROM counter WHERE name")
    table = cur.fetchall()
    return table
    

def update_counter():
    cur = cursor
    cur.execute("UPDATE ")
    pass


def test_data():
    get_data_connection()
    cur = cursor
    create_tables(connection)
    add_counter(connection, "Drink Water", "daily")
    add_counter(connection, "Study 1 hour", "daily")
    add_counter(connection, "Do household chores", "daily")
    add_counter(connection, "Do a physical activity", "daily")
    add_counter(connection, "Go to therapy", "weekly")
    increment_counter(connection, "counter1", "description")
    cursor.execute("SELECT * FROM counter")
    results = cursor.fetchall()
    print(results)











