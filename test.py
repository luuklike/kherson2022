import time as ua
from random import randint as shit
a = int(input("size: "))
for i in range(4):
    if a == 1:
        print("_*_*_*_*_*_*_*_*")
        print("*_*_*_*_*_*_*_*_")
    elif a == 2:
        print("__**__**__**__**__**__**__**__**")
        print("**__**__**__**__**__**__**__**__")
    elif a == 3:
        print("___***___***___***___***___***___***___***___***")
        print("***___***___***___***___***___***___***___***___")
    elif a > 3:
        print("Shut up!")
    elif a < 0:
        print("Shut up!")