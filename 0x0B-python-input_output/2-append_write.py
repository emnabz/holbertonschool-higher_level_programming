#!/usr/bin/python3
"""no module"""


def append_write(filename="", text=""):
    """append to a file"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
