#!/usr/bin/python3
'''
Module to determine whether a given data is valid UTF-8
'''


def validUTF8(data):
    '''
    function that determines a given set of data representing a valid
    UTF-8 encoding and returns True if data is a valid UTF-8 encoding
    and False if not
    '''

    noOfBytes = 0

    m1 = 1 << 7
    m2 = 1 << 6

    for i in data:
        m = m1
        if noOfBytes == 0:
            while m & i:
                noOfBytes += 1
                m = m >> 1
            if noOfBytes == 0:
                continue
            if noOfBytes == 1 or noOfBytes > 4:
                return False
        else:
            if not (i & m1 and not (i & m2)):
                return False
        noOfBytes -= 1
    return noOfBytes == 0
