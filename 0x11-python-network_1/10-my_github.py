#!/usr/bin/python3
"""9. My GitHub!
"""
from requests import get
from requests.auth import HTTPBasicAuth
import sys
if __name__ == '__main__':
    X = get('https://api.github.com/user',
            auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    print(X.json().get('id'))
