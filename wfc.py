import pygame
from sys import exit
import Tileboard
import math


width = 800
hieght = 400
pygame.init()
screen = pygame.display.set_mode((width, hieght))
pygame.display.set_caption("Wave-Function-Colapse")
clock = pygame.time.Clock()

test_surface = pygame.Surface((40,40))
test_surface.fill('Red')


#create the board
cols = 4
rows = 4

board = Tileboard.createBoard(cols, rows)

squareWidth = math.ceil(width / cols)
squareHeight = math.ceil(hieght / rows)
print(squareHeight)



def drawBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if len(board[i][j].options) > 1:
                pygame.draw.rect(
                    screen, 
                    'red',
                    (squareWidth * j , squareHeight * i, squareWidth, squareHeight),
                    0)
            else:
                pygame.draw.rect(
                    screen, 
                    'Green',
                    (squareWidth * j , squareHeight * i, squareWidth, squareHeight),
                    0)




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # here is where we draw all the elements for the program
    # pygame.draw.rect(Surface, color, rect, boarderWidth)
    board[0][1].randomCollapse()
    board[1][2].randomCollapse()
    board[2][3].randomCollapse()

    drawBoard(board)
    
    pygame.display.update()
    clock.tick(60)



