from string import ascii_letters, digits
from random import choices


def settingsPasswords():
    print("Введите количество необходимых паролей")
    count_of_pswrds = int(input())
    print("Введите длину пароля")
    length_of_pswrds = int(input())
    return count_of_pswrds, length_of_pswrds


def collectingDATA():
    print("Введите название сети для которой будет создан пароль")
    society = input()
    print("Введите логин")
    login = input()
    return society, login


def genegatePSWRD():
    # creating password
    passwords = []

    count, length = settingsPasswords
    for _ in range(count):
        passwords.append(choices(ascii_letters + digits, length))
    return passwords


def createPSWRD():
    flag = True
    while flag:
        passwords = genegatePSWRD()
        print("Выберите пароль, для повторной генерации пароля нажмите 0(ноль)")
        choice = int(input())
