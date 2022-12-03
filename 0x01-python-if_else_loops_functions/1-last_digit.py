#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    ldig = number % 10
else:
    ldig = ((-1 * number) % 10) * -1
if ldig > 5:
    print(f"Last digit of {number:d} is {ldig:d} and is greater than 5")
elif ldig == 0:
    print(f"Last digit of {number:d} is {ldig:d} and is 0")
else:
    print(f"Last digit of {number:d} is {ldig:d} and is less than 6 and not 0")
