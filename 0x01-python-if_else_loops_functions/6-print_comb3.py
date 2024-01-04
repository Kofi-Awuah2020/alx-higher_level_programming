#!/usr/bin/python3
for first_number in range(0, 9):
    for second_number in range(first_number + 1, 10):
        if first_number + second_number != 17: 
            print(f"{first_number}{second_number},", end=' ')
        else:
            print(f"{first_number}{second_number}")
