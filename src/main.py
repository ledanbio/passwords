from blanks import MENU, language
from create_pswrd import createPSWRD

control = True


def collectingDATA():
    print("Введите название сети для которой будет создан пароль")
    society = input()
    print("Введите логин")
    login = input()
    return society, login


while control:
    print(MENU)
    choice = int(input())
    if choice == 1:
        soc, login = collectingDATA()
        password = createPSWRD()
    elif choice == 3:
        break
    else:
        print("Введите числа от 1 до ?????")
