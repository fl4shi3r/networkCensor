import os, getpass

print("     LOGIN    ")
username = input("Username: ")
password = getpass.getpass(prompt='Password: ', stream=None) 

with open("loginDetails/rootLogin.txt", "r") as fobj:
    lines = fobj.readlines()
    if username == lines[0][:-1]  and password ==lines[1]:
        
        pass
    else:
        print("Wrong Login Credentials :(:(:(")
        exit(1)

