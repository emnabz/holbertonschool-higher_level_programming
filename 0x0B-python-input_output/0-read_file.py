#!/usr/bin/python3
def read_file(filename="", text=""):
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
