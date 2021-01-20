#!/usr/bin/python3
"""no module"""
import json


def save_to_json_file(my_obj, filename):
    """write an object to a txt file"""
    with open(filename, encoding="utf-8", mode="w") as file:
        file.write(json.dumps(my_obj))
