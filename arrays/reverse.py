#!/usr/bin/env python3

def reverse(str):
    reversed = ""
    length = len(str)

    for i in range(len(str)):
        reversed += str[length - 1 - i]

    return reversed

result = reverse('Hello')

print(result)
