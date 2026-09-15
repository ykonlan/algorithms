""" Given an integer, find the sum of all its individual digits """

def sum_of_digits(digit:int):
    if digit < 10:
        return digit
    return (digit % 10) + sum_of_digits(digit // 10)

print(sum_of_digits(54321))
    