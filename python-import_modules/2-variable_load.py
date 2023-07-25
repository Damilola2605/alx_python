#!/usr/bin/python3
import importlib.util

def main():
 module_name = "variable_load_2"

 # Load the module using importlib
 spec = importlib.util.spec_from_file_location(module_name, f"{module_name}.py")
 module = importlib.util.module_from_spec(spec)
 spec.loader.exec_module(module)

 # Access the variable 'a' and print its value
 print("The value of 'a' is:", module.a)

if __name__ == "__main__":
 main()