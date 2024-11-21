import pygame
import settings as s
import random

pygame.init()

screen = pygame.display.set_mode((s.width, s.height))
pygame.display.set_caption("Судоку")

def drawGrid():
   for i in range(10):
    if(i % 3 == 0):
        lineThickness = 3
    else:
        lineThickness = 1
    pygame.draw.line(screen, s.black, (0, i*s.cellSize), (s.width, i*s.cellSize), lineThickness)
    pygame.draw.line(screen, s.black, (i*s.cellSize, 0), (i*s.cellSize, s.width), lineThickness)


def is_valid(table, row, col, num):
    if num in table[row]:
        return False
    if num in [table[i][col] for i in range(9)]:
        return False



