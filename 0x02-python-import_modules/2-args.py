#!/usr/bin/python3
import sys


def main():
    length = len(sys.argv)
    if length <= 1:
        print(f"{length - 1} arguments.")
    else:
        print(f"{length - 1} arguments:")
        for index, argument in enumerate(sys.argv):
            if index == 0:
                continue
            print(index, ":", argument)


if __name__ == "__main__":
    main()
