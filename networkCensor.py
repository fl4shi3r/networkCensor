# import login
import os, pygame


os.system('clear')


print(
'''
                  __      __      _____
                 /~/|    /~/     /  ___|  
                / / |   / /     |  /
               / /  |  / /      | |
              / /   | / /       |  \___
             /_/    |/_/  (*)    \_____| (*)
                   (Network Censor)
''' )

print("Please Select from the following:")
print("1.Use default Setting")
print("2.View Default Setting")
print("3.Manual Setup")
print("4.Update Manually")
print("0.Exit")
choice = int(input("Enter your choice: "))
if choice == 1:
      import default
elif choice == 2:
      import viewdefault

elif choice == 3:
      import addManually
elif choice == 4:
      import updateManually
elif choice == 0:
      print("Bye..Bye........")
      exit(0)
else:
      print("Wrong Option Selected :(:(")
      exit(1)