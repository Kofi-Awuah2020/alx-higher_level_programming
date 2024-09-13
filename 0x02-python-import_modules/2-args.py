#!/usr/bin/python3
import sys


def main():
    length = len(sys.argv) - 1
    if length == 0:
        print(f"{length} arguments.")
    else:
        if length == 1:
            print(f"{length} argument:")
        else: 
            print(f"{length} arguments:")
        for index, argument in enumerate(sys.argv):
            if index == 0:
                continue
            print(index, ":", argument)


if __name__ == "__main__":
    main()
