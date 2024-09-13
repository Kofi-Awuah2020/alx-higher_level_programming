#!/usr/bin/python3
import hidden_4


def main():
    names = (dir(hidden_4))
    filtered_names = [name for name in names if not name.starstwith('__')]
    sorted_names = filtered_names.sort()

    for name in sorted_names:
        print(name)


if __name__ == "__main__":
    main()