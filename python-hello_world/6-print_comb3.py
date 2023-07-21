#!/usr/bin/python3
for num1 in range(9):
    for num2 in range(num1 + 1, 9):
        print("{:02d}, ".format(num1 * 9 + num2), end=" ")
