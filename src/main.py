from blanks import MENU, language
from create_pswrd import createPSWRD, savePSWRD, collctSOC, collctLOGIN
from dbQueries import addPSWRD, createDB, changePSWRD, check
connection = createDB()

control = True

while control:
    print(MENU)
    choice = int(input())
    if choice == 1:
        soc, login = collctSOC(), collctLOGIN()
        password = createPSWRD()
        if savePSWRD():
            addPSWRD(connection, soc, login, password)  # хэширование пароля

    elif choice == 2:
        changePSWRD(connection)
    elif choice == 3:
        check(connection)
    elif choice == 4:
        break
    else:
        print("Введите числа от 1 до ?????")

connection.close()
