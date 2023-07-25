#!/usr/bin/python3
import sys


def arguments():
    num_arguments = len(sys.argv)

    # Print the number of arguments
    if num_arguments == 1: 
        print ("Number of arguments:{}." format(num_arguments))