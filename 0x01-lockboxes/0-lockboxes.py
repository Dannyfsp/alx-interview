#!/usr/bin/python3
''' Function that checks locked boxes '''


def canUnlockAll(boxes):
    ''' Method that determines if all boxes can be opened '''

    if boxes == 0:
        return False

    if not isinstance(boxes, list):
        return False

    if len(boxes) == 0:
        return False

    check = [0]
    all_list = [i for i in range(len(boxes))]

    for i in check:
        for y in boxes[i]:
            if y not in check and y in all_list:
                if y >= len(boxes):
                    return False
                check.append(y)

    if len(check) == len(check):
        return True
    else:
        return False
