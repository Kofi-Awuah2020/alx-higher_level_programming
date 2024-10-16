#!/usr/bin/python3
import os


def read_file(filename=""):
    with open(filename, mode="r", encoding="utf-8") as file:
        content = file.read()
        print(content)

