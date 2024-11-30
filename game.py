import pygame
import settings as s
import sudoku as su
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

def drawNumbers(puzzle):
    font = pygame.font.Font(None, 40)
    for row in range(9):
        for col in range(9):
            num = puzzle[row][col]
        if num != 0:
            text = font.render(str(num),True, s.black)
            screen.blit(text,(col * s.cellSize + s.cellSize // 4, row * s.cellSize + s.cellSize // 8))

def getCell(pos):
#определение ячейки
    return True

selectedCell = None

def higlightCell(selectedCell):
    if selectedCell:
            row, col = selectedCell
            pygame.draw.rect(screen,s.blue, (col*s.cellSize, row * s.cellSize, s.cellSize, s.cellSize), 4)

def handleEvents(puzzle):
#логика поля
    return True

def solved(puzzle, sudokuSolver):
    return np.array_equal(puzzle, sudokuSolver)