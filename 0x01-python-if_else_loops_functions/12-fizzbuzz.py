#!/usr/bin/python3

def fizzbuzz():
    """print the numbers from 1 to 100 separated by a space
    Multiples of 3, print Fizz
    Multiples of 5, print Buzz
    Multiples of both 3 & 5, print FizzBuzz"""

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print ("FizzBuzz ", end="")
    elif number % 3 == 0:
        print("Fizz ", end="")
    elif number % 5 == 0:
        print("Buzz ", end="")
    else:
        print("{} ".format(number), end="")

