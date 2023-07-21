#!/usr/bin/python3
'''for num1 in range(0, 10):
    for num2 in range(num1 + 1, 10):
       # print("{:02d}, ".format(num1 * 10 + num2),end="")
       print("{}{}".format(num1, + num2), end=", ")'''
for i in range(10):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print("{}{}".format(i, j))
        else:
            print("{}{}".format(i, j), end=", ")