from blanks import MENU, language
from create_pswrd import createPSWRD, savePSWRD, collctSOC, collctLOGIN
from dbQueries import addPSWRD, createDB, changePSWRD
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
        changePSWRD()
    elif choice == 3:

        break
    else:
        print("Введите числа от 1 до ?????")

connection.close()
