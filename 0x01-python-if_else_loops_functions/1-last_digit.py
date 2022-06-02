#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = 0
if number < 0:
    number *= -1
    sign = -1
lastdigit = number % 10
if sign == -1:
    number *= -1
    lastdigit *= -1

print("Last digit of {} is ".format(number), end="")
if lastdigit > 5:
    print("{} and is greater than 5".format(lastdigit), "\n")
elif lastdigit == 0:
    print("{} and is 0".format(lastdigit), "\n")
else:
    print("{} and is less than 6 and not 0".format(lastdigit), "\n")