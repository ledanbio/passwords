import sqlite3
from create_pswrd import collctSOC, collctLOGIN, createPSWRD, newPSWRD

table_name = "passwodrs"
db_name = "../passwords.db"


def table_exists(connection, table_name):
    cursor = connection.cursor()
    cursor.execute(
        f"""
        SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';
    """
    )
    return cursor.fetchone() is not None


def createTABLE(connection):
    cursor = connection.cursor()
    cursor.execute(
        f"""
        CREATE TABLE {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            society TEXT NOT NULL,
            login TEXT NOT NULL,
            hash_password TEXT NOT NULL
        )
    """
    )
    connection.commit()


def createDB():
    connection = sqlite3.connect(db_name)
    if not table_exists(connection, table_name):
        createTABLE(connection)
    return connection


def addPSWRD(connection, society, login, hash_password):
    cursor = connection.cursor()
    cursor.execute(
        f"""
        INSERT INTO {table_name} (society, login, hash_password) VALUES (?, ?, ?)
    """, (society, login, hash_password)
    )
    connection.commit()


def findPSWRD(connection, society):
    cursor = connection.cursor()
    cursor.execute(
        f"""
        SELECT * FROM {table_name} WHERE society IN VALUES (?)                 
    """,
        (society),
    )

    return cursor.fetchall()


# asdasd
def changePSWRD(connection):
    cursor = connection.cursor()
    soc = ""
    login = ""
    new_pswrd = ""
    while True:
        soc = collctSOC()
        login = collctLOGIN()
        cursor.execute(
            f'''
            SELECT id FROM {table_name} WHERE society = ? AND login = ?
        ''', (soc,) + (login,))
        result = cursor.fetchone()
        new_pswrd = newPSWRD()

        if result:
            cursor.execute(
                f"""
                UPDATE {table_name} SET hash_password = ? WHERE id = ?
            """, (new_pswrd, result[0]))
            break
        else:
            print("Пароль не найден")
            choice = input()
            if choice == "Y" or choice == "y":
                continue
            else:
                break

    connection.commit()


def check(connection):
    cursor = connection.cursor()
    cursor.execute(
        f"""
        SELECT * FROM {table_name}        
    """
    )
    result = cursor.fetchall()
    print(result)
