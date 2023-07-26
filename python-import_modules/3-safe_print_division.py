#!/usr/bin/python3

def safe_print_division(a ,b):
    a = 12
    b = 2
    try:
        result = a / b

    except ZeroDivisionError:
        result = None
        
    finally:
        print("Inside result: {}".format(result))
        return result