from blanks import MENU, language
from create_pswrd import createPSWRD

control = True


while control:
    print(MENU)
    choice = int(input())
    # selector
    if choice == 1:
        a = 1
    elif choice == 2:
        break
    else:
        print("Введите числа от 1 до ?????")
