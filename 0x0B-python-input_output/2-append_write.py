#!/usr/bin/python3


def append_write(filename="", text=""):
    """write a txt to a file"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
