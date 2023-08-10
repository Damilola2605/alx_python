#!/usr/bin/python3

"""
This module on a script that fetches a link
"""

from urllib import request

url = 'https://alu-intranet.hbtn.io/status'
response = request.get(url)

if response.status_code == 200:
    data = response.json()
    print("Body response:")
    print("\t- type:", type(data))
    print("\t- content:", data)
else:
    print("Error:", response.status_code)