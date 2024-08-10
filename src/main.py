from blanks import MENU, language
from create_pswrd import createPSWRD
from dbQueries import add_password, createDB
import sqlite3



connection = createDB()

def collectingDATA():
    print("Введите название сети для которой будет создан пароль")
    society = input()
    print("Введите логин")
    login = input()
    return society, login
control = True

while control:
    print(MENU)
    choice = int(input())
    if choice == 1:
        soc, login = collectingDATA()
        password = createPSWRD()
        print("Хотите сохранить пароль (Y/N)?")
        choice_1 = input() 
        if choice_1 == "Y":
            add_password(connection, soc, login, password) #хэширование пароля
        elif choice_1 == "N":
            continue
        else:
            print()
    elif choice == 2:
        print
    elif choice == 3:
        break
        connection.close()
    else:
        print("Введите числа от 1 до ?????")
