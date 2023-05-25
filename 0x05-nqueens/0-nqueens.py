#!/usr/bin/python3
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


def solveNQUtil(board, col, number):
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

def validate(args):
    '''
    validate to comfirm the input data to verify if the size to answer
    is possible
    Args:
        args - sys.argv
    '''
    if (len(args) == 2):
        # validate data
        try:
            number = int(args[1])
        except Exception:
            print("N must be a number")
            exit(1)
        if number < 4:
            print("N must be at least 4")
            exit(1)
        return number
    else:
        print("Usage: nqueens N")
        exit(1)


if __name__ == "__main__":
    '''Main method to execute the application'''
    number = validate(sys.argv)
    solve(number)
