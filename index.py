log = ["asd", "andrey"]
passlist = ["12345678", "qwertyuiop"]
login_authorize = ""


def login():
    checkLogIsEmpty()
    x = -1
    print("Input login: ")
    login = input()
    for lists_log in log:
        x =  x + 1
        if (lists_log == login):
            print("Login input successfully! \n")
            break
    while (1):
        print("Input password:")
        password = input()
        if passlist[x] == password:
            print("You have successfully entered! \n")
            login_authorize = login
            menu()
        elif password == "0":
            startmenu()
        else:
            print("Password is not valid, please try again or print 0 for exit")

def reg():
    password = ""

    print("Input your login: ")
    login = input()
    n = 0
    while 1:
        for lists_log in log:
            if (lists_log == login):
                n = n + 1
        if (n > 0):
            print("Login busy, please try again")
            n = 0
            login = input()
        else:
            break
    while (len(password) < 8):
        print("Input password: ")
        password = input()
        if (len(password) < 8):
            print("\nEnter a password longer than 8 characters")

    print("\nYou have successfully registered! \n")
    log.append(login)
    passlist.append(password)
    login_authorize = login
    startmenu()

def printUsers():
    checkLogIsEmpty()
    for lists_log in log:
        print(lists_log)

def deleteUsers():
    checkLogIsEmpty()
    x = -1
    print("Input login for delete User: ")
    login = input()
    for lists_log in log:
        x =  x + 1
        if (lists_log == login):
            print("Login input successfully! \n")
            break
    while (1):
        print("Input password for delete User:")
        password = input()
        if passlist[x] == password:
            print("You have successfully entered! User delete\n")
            log.remove(login)
            passlist.remove(password)
            if (login_authorize == login):
                startmenu()
            else:
                menu()
        elif password == "0":
            menu()
        else:
            print("Password is not valid, please try again or print 0 for exit")

def changePassword():
    x = -1
    print("Input login for change password: ")
    login = input()
    for lists_log in log:
        x =  x + 1
        if (lists_log == login):
            print("Login input successfully! \n")
            break
    while (1):
        print("Input old password:")
        password = input()
        if passlist[x] == password:
            print("You have successfully entered password! Input new password\n")
            password = input()
            passlist[x] = password
            menu()
        elif password == "0":
            menu()
        else:
            print("Password is not valid, please try again or print 0 for exit")

def checkLogIsEmpty():
    if len(log) == 0:
        print("The list of Users is empty, please registration! \n")
        menu()

def menu():
    while (1):
        print("1 - print users; \n2 - delete users; \n3 - change password,\n4 - go out, \n5 - break")
        value = int(input())
        if (value == 1):
            printUsers()
        elif (value == 2):
            deleteUsers()
        elif (value == 3):
            changePassword()
        elif (value == 4):
            startmenu()
        elif (value == 5):
            break

def startmenu():
    while (1):
        print("1 - login; \n2 - registration")
        value = int(input())
        if (value == 1):
            login()
        elif (value == 2):
            reg()

startmenu()