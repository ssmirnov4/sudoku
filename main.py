import pygame
import sudoku as su
import game as g
import settings as s

def main():

    pygame.init()
    s.initFonts()

    puzzle, sudokuSolver, sudokuGrid = su.getPuzzle()

    s.screen.fill(s.white)
    g.drawGrid(s.screen)
    g.drawNumbers(puzzle, s.screen)
    pygame.display.update()

    g.handleEvents(puzzle, sudokuSolver, sudokuGrid, s.screen)

if __name__ == '__main__':
    
    main()
