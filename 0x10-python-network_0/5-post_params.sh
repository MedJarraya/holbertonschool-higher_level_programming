#!/bin/bash
# This script takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -s "$1" -X POST -H 'test@gmail.com: email' 'I will always be here for PLD: subject'
