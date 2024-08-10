import sqlite3
table_name = 'passwodrs'
db_name = '../passwords.db'

def table_exists(connection, table_name):
    cursor = connection.cursor()
    cursor.execute(f'''
        SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';
    ''')
    return cursor.fetchone() is not None

def createTABLE(connection):
    cursor = connection.cursor()
    cursor.execute(f'''
        CREATE TABLE {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            society TEXT NOT NULL,
            login TEXT NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')        
    connection.commit()

def createDB():
    connection = sqlite3.connect(db_name)
    if not table_exists(connection, table_name):
        createTABLE(connection)
    return connection

def addPSWRD(connection, society, login, hash_password):
    cursor = connection.cursor()
    cursor.execute(f'''
        INSERT INTO {table_name} (society, login, hash_password) VALUES (?, ?, ?)
    ''', (society, login, hash_password))
    connection.commit()

def findPSWRD(connection, society):
    cursor = connection.cursor()
    cursor.execute(f'''
        SELECT * FROM {table_name} WHERE society IN VALUES (?)                 
    ''', (society))