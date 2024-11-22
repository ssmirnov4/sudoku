import pygame
import settings as s
import random
import numpy as np

pygame.init()

screen = pygame.display.set_mode((s.width, s.height))
pygame.display.set_caption("Судоку")

def drawGrid():
   for i in range(10):
    if i % 3 == 0:
        lineThickness = 3
    else:
        lineThickness = 1
    pygame.draw.line(screen, s.black, (0, i*s.cellSize), (s.width, i*s.cellSize), lineThickness)
    pygame.draw.line(screen, s.black, (i*s.cellSize, 0), (i*s.cellSize, s.width), lineThickness)


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
                for number in random.sample((1,9), 9):
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

def remove(table, numCells):
    return True