#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lastdig = number % 10
else:
    lastdig = ((-1 * number) % 10) * -1
if lastdig > 5:
    print(f"Last digit of {number:d} is {lastdig:d} and is greater than 5")
elif lastdig == 0:
    print(f"Last digit of {number:d} is {lastdig:d} and is 0")
else:
    print(f"Last digit of {number:d} is {lastdig:d} and is less than 6 not 0")
