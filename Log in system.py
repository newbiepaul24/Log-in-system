Usernames = open("names.txt", "r").readlines()
UsernamesAdd = open("names.txt", "a")
Passwords = open("passw.txt", "r").readlines()
PasswordsAdd = open("Passw.txt", "a")
usersList = []
passList = []

for u in Usernames:
    usersList.append(u.strip())

for p in Passwords:
    passList.append(p.strip())


def SignUp():
    key = True
    while key:
        print("Sign up")
        Username = input("Username: ")
        Password = input("Password: ")
        if not Password.isalpha():
            if not len(Password) <= 8:
                print("success you may now log in")
                UsernamesAdd.write("\n" + Username)
                usersList.append(Username)
                UsernamesAdd.close()
                PasswordsAdd.write("\n" + Password)
                passList.append(Password)
                PasswordsAdd.close()
                key = False
                LogIn()
            else:
                print("Password must have not less than 8 \n")
        else:
            print("password must contain number\n")


def LogIn():
    print("Log in")
    Username = input("Username: ")
    Password = input("Password: ")

    if Username in usersList:
        if Password in passList:
            print("Welcome", Username)
        else:
            print("wrong password")
    else:
        print("no username registered")

print("Log in | Sign up")
print("(1) Log in")
print("(2) Sign up")
select = int(input("Enter: "))

selected = 3
while selected >= 3:
    if select == 1:
        selected = 1
        LogIn()
    elif select == 2:
        selected = 2
        SignUp()
