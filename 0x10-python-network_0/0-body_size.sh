#!/usr/bin/python3
# A bash script that in a URL sends a request to that URL, and displays the size of the body of the response
echo $"$(curl -sI "$1" | grep 'Content-Length' | cut  -d ':' -f '2' | cut -d ' ' -f '2')"