#!/usr/bin/python3
def uppercase(str):
    newstr = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            newstr = chr(ord(char) - 32)
        else:
            newstr = char
        print("{}".format(newstr), end="")