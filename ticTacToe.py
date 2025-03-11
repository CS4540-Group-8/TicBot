#import needed libraries 
import sys
import numpy
import pygame

#create game window
pygame.init()

#color variable
WHITE = (225, 255, 255)
GRAY = (180, 180, 180)
RED = (255, 0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

#Proportions
WIDTH = 300
HEIGHT = 300
LINE_WIDTH = 5
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25

#Define window display
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #Resolution
pygame.display.set_caption('Tic Tac Toe AI') #Window Title
screen.fill(BLACK) #Window background color

board = numpy.zeros((BOARD_ROWS, BOARD_COLS))

def draw_lines(color=WHITE):
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(sceen, color, start_pos:(0, SQUARE_SIZE * i), end_pos:(WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
        pygame.draw.line(sceen, color, start_pos:(SQUARE_SIZE * i, 0), end_pos:(SQUARE_SIZE * i, HEIGHT), LINE_WIDTH)
        




