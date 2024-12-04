import pygame
import settings as s
import numpy as np

pygame.display.set_caption("Судоку")
s.screen.fill(s.white)

selectedCell = None

def drawGrid(screen):
   for i in range(10):
    if i % 3 == 0:
        lineThickness = 3
    else:
        lineThickness = 1
    pygame.draw.line(screen, s.black, (0, i*s.cellSize), (s.width, i*s.cellSize), lineThickness)
    pygame.draw.line(screen, s.black, (i*s.cellSize, 0), (i*s.cellSize, s.width), lineThickness)

def drawNumbers(puzzle, screen):
    font = pygame.font.Font(None, 40)
    for row in range(9):
        for col in range(9):
            num = puzzle[row][col]
            if num != 0:
                text = font.render(str(num),True, s.black)
                screen.blit(text, (col * s.cellSize + s.cellSize // 4, row * s.cellSize + s.cellSize // 8))

def getCell(pos):
    x, y = pos
    return y // s.cellSize, x // s.cellSize

def higlightCell(selectedCell, screen):
    if selectedCell:
            row, col = selectedCell
            pygame.draw.rect(screen, s.blue, (col * s.cellSize, row * s.cellSize, s.cellSize, s.cellSize), 4)

def finish(puzzle, sudokuSolver, screen):
    if solved(puzzle, sudokuSolver):
        text = s.font.render("Поздравляю, Вы победили!", True, s.green)
    else:
        text = s.font.render("Судоку решен неверно", True, s.red)
    screen.blit(text, (20, s.height - 50))
def handleEvents(puzzle, sudokuSolver, sudokuGrid,screen):
    global selectedCell
    key_number = {pygame.K_1: 1,
            pygame.K_2: 2,
            pygame.K_3: 3,
            pygame.K_4: 4,
            pygame.K_5: 5,
            pygame.K_6: 6,
            pygame.K_7: 7,
            pygame.K_8: 8,
            pygame.K_9: 9
                  }

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    finish(puzzle, sudokuSolver, screen)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    selectedCell = getCell(pygame.mouse.get_pos())
            if event.type == pygame.KEYDOWN and selectedCell:
                row, col = selectedCell
                if event.key in key_number:
                    if sudokuGrid[row][col] == 0:
                        puzzle[row][col] = key_number[event.key]

        screen.fill(s.white)
        drawGrid(screen)
        drawNumbers(puzzle, screen)
        higlightCell(selectedCell, screen)
        pygame.display.update()

def solved(puzzle, sudokuSolver):
    return np.array_equal(puzzle, sudokuSolver)