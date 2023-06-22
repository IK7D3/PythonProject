name = []
userName = []
passWord = []
i = 0


def SignUp(i):
    name1 = input("Enter your name:\t\n")
    name.append(name1)

    while 1 == 1:
        x = True
        m = 0
        username = input("Enter your username:\t")
        for j in range(i):
            if (userName[j] == username):
                m = input("This username is available\n"
                          "1) Try again\n"
                          "2)Back\n")
                x = False
                break

        if (x == False and m == 1):
            continue
        elif (x == False and m == 2):
            welcome()
        else:
            userName.append(username)
            i = i + 1
            break

    while 1 == 1:
        x = True
        password = input("Enter your password:\t\n")
        m = 0
        if (len(password) > 8):
            m = m + 1
        if (password.count('.') > 0 or password.count('*') > 0 or password.count('&') > 0 or password.count(
                '$') > 0 or password.count('#') > 0 or password.count('@') > 0 or password.count('!') > 0):
            m = m + 1
        if (password.count('0') > 0 or password.count('1') > 0 or password.count('2') > 0 or password.count(
                '3') > 0 or password.count('4') > 0 or password.count('5') > 0 or password.count('6') > 0
                or password.count('7') > 0 or password.count('8') > 0 or password.count('9') > 0):
            m = m + 1

        has_upper = False
        has_lower = False
        for char in password:
            if char.isupper():
                has_upper = True
                m = m + 1
                break
        for char in password:
            if char.islower():
                has_lower = True
                m = m + 1
                break

        if (m == 5):
            passWord.append(password)
            break
        else:
            k = input("invalid password!\n"
                      "1) Try again\n"
                      "2)Back\n")
            x = False

        if (x == False and k == 1):
            continue

        elif (x == False and k == 2):
            n = welcome()
            break

print("iman kheyli khari")