#!/usr/bin/python3

def remove_char_at(str, n):
    """copy string without char n"""
    if n < 0:
        return (str)

    return (str[:n] + str[n+1:])
