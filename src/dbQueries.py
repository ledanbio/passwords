import sqlite3
from create_pswrd import collctSOC, collctLOGIN

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
    """,
        (society, login, hash_password),
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

    print("Введите название сети и логин, в которой вы хотите изменить пароль")
    soc = ""
    login = ""
    new_pswrd = ""
    while True:
        soc = collctSOC()
        login = collctLOGIN()
        cursor.execute(
            f"""
            SELECT id FROM {table_name} WHERE (society, login) IN VALUES(?,?)
        """,
            soc,
            login,
        )
        result = cursor.fetchone()

        if result:
            cursor.execute(
                f"""
                UPDATE {table_name} SET password = ? WHERE id = ?
            """,
                new_pswrd,
                result,
            )
        else:
            print()
    # connection.commit()
