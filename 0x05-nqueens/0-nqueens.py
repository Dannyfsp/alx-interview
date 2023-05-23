#!/usr/bin/python
'''
A program that solves the N Queen problem
'''


import sys


def print_board(board):
    '''
    function that prints board in form of list or Array
    Args:
        board - list of list with length sys.argv[1]
    '''
    board_list = []
    for i, row in enumerate(board):
        value = []
        for j, col in enumerate(row):
            if col == 1:
                value.append(i)
                value.append(j)
        board_list.append(value)
    print(board_list)


def isSafe(board, row, col, number):
    '''
    function that checks movement in the board
    Args:
        board - list of list with length sys.argv[1]
        row - row to check if it is safe doing a movement in row position
        col - col to check if it's safe doing a movement in col position
        number - size of the board
    '''

    # Check row in the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, number, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def soleNQUtil(board, col, number):
    '''
    Auxiliar method to find the possibilities of answer
    Args:
        board - Board to resolve
        col - Number of col
        number - size of the board
    Returns:
        All the possibilities to solve the problem
    '''

    if (col == number):
        print_board(board)
        return True
    res = False
    for i in range(number):
        if (isSafe(board, i, col, number)):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Make result true if any placement is possible
            res = solveNQUtil(board, col + 1, number) or res

            board[i][col] = 0  # Backtrack

    return res


def solve(number):
    '''
    Find all the possibilities if exists
    Args:
        number - size of the board
    '''
    board = [[0 for i in range(number)]for i in range(number)]
    if not solveNQUtil(board, 0, number):
        return False

    return True
