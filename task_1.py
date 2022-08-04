#!/usr/bin/env python3

def compute(x: int, y: int):
    return ((int(x) ** int(y)) / int(x))

x = input("Enter the first number")
y = input("Enter the second number")
print(compute(x, y))