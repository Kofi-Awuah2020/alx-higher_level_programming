#!/usr/bin/python3
import sys


def main():
    result = 0
    for args in sys.argv[1:]:
        result += int(args)
    print(result)


if __name__ == "__main__":
    main()
