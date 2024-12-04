import random
import numpy as np
import copy

def valid(table, row, col, num):
    if num in table[row]:
        return False

    if num in [table[i][col] for i in range(9)]:
        return False

    startRow = 3 * (row//3)
    startCol = 3 * (col//3)
    for i in range(3):
        for j in range(3):
            if table[startRow + i][startCol+j] == num:
                return False

    return True

def fill(table):
    for row in range(9):
        for col in range(9):
            if table[row][col] == 0:
                for number in random.sample(range(1,10), 9):
                    if valid(table, row, col, number):
                        table[row][col] = number
                        if fill(table):
                            return True
                        table[row][col] = 0
                return False
    return True


def generate():
    table = np.zeros((9,9), dtype=int)
    fill(table)
    return table

def remove(grid, numRemove):
    for i in range(numRemove):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        while grid[row][col] == 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
        grid[row][col] = 0
    return grid

def getPuzzle(numRemove = 52):
    sudokuGrid = generate()
    sudokuSolver = copy.deepcopy(sudokuGrid)
    puzzle = copy.deepcopy(remove(sudokuGrid, numRemove))
    return puzzle, sudokuSolver, sudokuGrid