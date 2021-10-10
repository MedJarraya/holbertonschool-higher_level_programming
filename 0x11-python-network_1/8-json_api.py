#!/usr/bin/python3
"""8. Search API
"""
import requests
import sys
if __name__ == "__main__":
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        X = r.json()
        if not X:
            print("No result")
        else:
            print("[{}] {}".format(X.get("id"), X.get("name")))
    except ValueError:
        print("Not a valid JSON")
