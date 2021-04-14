#!/usr/bin/python3
"""a  script that takes in a URL, sends a request to the URL and displays
the body of the response."""
if __name__ == "__main__":
    import requests
    from sys import argv
    x = requests.get(argv[1])
    if x.status_code >= 400:
        print("Error code: {}".format(x.status_code))
    else:
        print(x.text)
