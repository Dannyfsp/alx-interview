#!/usr/bin/python3
'''
Module that calculates minimum operations
'''


def minOperations(n):
    '''
    Method that calculates the fewest number of operations needed
    '''
    if n < 2 or type(n) is not int:
        return 0
    check = []
    value = n
    i = 1
    while value != 1:
        i += 1
        if value % i == 0:
            while (value % i == 0 and value != 1):
                value = value / i
                check.append(i)
    return sum(check)
