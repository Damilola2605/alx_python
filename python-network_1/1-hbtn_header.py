#!/usr/bin/python3
"""
URL that takes,sends and displays variable value
"""


import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))