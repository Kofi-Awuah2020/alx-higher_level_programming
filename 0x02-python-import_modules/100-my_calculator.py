#!/usr/bin/python3
import calculator_1 as calc
import sys


def main():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    operators = {'+': calc.add(a, b),
                 '-': calc.sub(a, b),
                 '*': calc.mul(a, b),
                 '/': calc.div(a, b),
                 }

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    for key, value in operators.items():
        if key == operator:
            print(f"{a} {operator} {b} = {value}")


if __name__ == "__main__":
    main()
