#!/usr/bin/python3

def print_last_digit(number):
    """print the last digit of a number"""
    print(abs(number) % 10, end="")
    return (abs(number) % 10)
