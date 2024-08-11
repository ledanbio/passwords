from string import ascii_letters, digits
from random import choices


def settingsPasswords():
    # Добавить проверки
    print("Введите количество необходимых паролей")
    count_of_pswrds = int(input())
    if count_of_pswrds > 52:
        count_of_pswrds = 52
    print("Введите длину пароля")
    length_of_pswrds = int(input())
    return count_of_pswrds, length_of_pswrds


def genegatePSWRD(count, length):
    passwords = []

    for _ in range(count):
        passwords.append("".join(choices(ascii_letters + digits, k=length)))
    return passwords


def createPSWRD():
    flag = True
    count, length = settingsPasswords()
    passwords = genegatePSWRD(count, length)
    while flag:
        print("Выберите пароль, для повторной генерации пароля нажмите 0(ноль)")
        for index, item in enumerate(passwords, start=1):
            print(f"{index}. {item}")
        choice = int(input())
        if (choice < 0) or (choice > len(passwords)):
            print("Введите число в диапазоне от 0 до", len(passwords))
            continue
        elif choice == 0:
            print("Новые пароли генерируются")
            passwords = genegatePSWRD(count, length)
            continue
        else:
            return passwords[choice - 1]


def savePSWRD():
    choice = ""
    while True:
        print("Хотите сохранить пароль (Y/N)?")
        choice_1 = input()
        if choice_1 == "Y":
            return 47
        elif choice_1 == "N":
            return False
        else:
            print("Введите Y / N")
            continue


def collctSOC():
    print("Введите название сети для которой будет создан пароль")
    society = input()
    return society


def collctLOGIN():
    print("Введите логин")
    login = input()
    return login
