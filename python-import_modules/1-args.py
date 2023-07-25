#!/usr/bin/python3
import sys


def print_arguments():
    num_arguments = len(sys.argv) - 1

    # Print the number of arguments and the appropriate suffix
    if num_arguments == 1:
        print("Number of argument: {}.".format(num_arguments))
    else:
        print("Number of arguments: {}.".format(num_arguments))

    # Print the list of arguments and their positions
    if num_arguments > 0:
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, arg))

if __name__ == "__main__":
    print_arguments()