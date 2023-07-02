import sqlite3


def get_db_connection(name= "main.db"):
    con = sqlite3.connect(name)
    cur= con.cursor()
    create_tables(con)
    return con


def create_tables(db):
    cur = db.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS counter (
        name TEXT PRIMARY KEY,
        description TEXT)""")

    cur.execute("""CREATE TABLE IF NOT EXISTS tracker (
        date TEXT,
        counterName TEXT,
        FOREIGN KEY (counterName) REFERENCES counter(name)
    )""")

    db.commit()


def add_counter(db, name, description):
    cur = db.cursor()
    cur.execute("INSERT INTO counter VALUES (?,?)", (name, description))
    db.commit()

def increment_counter(db, name, instance_date = None):
    cur = db.cursor()
    if not instance_date:
        from datetime import datetime
        instance_date = str(datetime.datetime.now())
    cur.execute("INSERT INTO tracker VALUES (?,?)", (instance_date, name))
    db.commit()

def get_counter_data(db, name):
    cur = db.cursor()
    cur.execute("SELECT * FROM tracker WHERE counterName = ??", (name, ))
    return cur.fetchall()


data = get_db_connection()
print(data)


