import pygame
import numpy as np
import time
import math

pygame.init()
sizeTable = width, height = 1380, 700
numberXCells = 120
numberYCells = 60

sizeCellWidth = (width-1)/numberXCells
sizeCellHeight = (height-1)/numberYCells

backgroundTable = 25,25,25

screen = pygame.display.set_mode((height, width), pygame.RESIZABLE)
screen.fill(backgroundTable)

gameState = np.zeros((numberXCells,numberYCells))
print(gameState)
pauseExecution = False

gameState[21,21]=1
gameState[21,22]=1
gameState[21,23]=1




while 1:
    newGameState = np.copy(gameState)
    event_1 = pygame.event.get()
    for event in event_1:
        if event.type == pygame.KEYDOWN:
            pauseExecution = not pauseExecution
        mouseClick = pygame.mouse.get_pressed()
        if sum(mouseClick) > 0:
            positionX, positionY = pygame.mouse.get_pos()
            if positionX > 0 and positionX < (width -1) and positionY > 0 and positionY < (height-1):
                newGameState[math.floor(positionX / sizeCellWidth),
                            math.floor(positionY / sizeCellHeight)] = mouseClick[0] and not mouseClick[2]
    screen.fill(backgroundTable)

    for y in range(0, numberYCells):
        for x in range(0, numberXCells):
            if not pauseExecution:
                numberNeigh = gameState[(x-1)% numberXCells, (y-1) % numberYCells] +\
                            gameState[(x) % numberXCells, (y-1) % numberYCells] +\
                            gameState[(x+1)% numberXCells, (y-1) % numberYCells] +\
                            gameState[(x-1)% numberXCells, (y) % numberYCells] +\
                            gameState[(x+1)% numberXCells, (y) % numberYCells] +\
                            gameState[(x-1)% numberXCells, (y+1) % numberYCells] +\
                            gameState[(x)% numberXCells, (y+1) % numberYCells] +\
                            gameState[(x+1)% numberXCells, (y+1) % numberYCells]

                # R1 : Una celula muerta con exactamente 3 celulas vecinas vivas nace
                if gameState[x,y] == 0 and numberNeigh == 3:
                    newGameState[x,y] = 1
                # R2 : Una celula viva con 2 o 3 celulas vecinas vivas sigue viva, en otro caso muere
                elif gameState[x,y] == 1 and (numberNeigh < 2 or numberNeigh > 3):
                    newGameState[x,y] = 0

            poly = [((x) * sizeCellWidth, (y) * sizeCellHeight),
                    ((x + 1) * sizeCellWidth, (y) * sizeCellHeight),
                    ((x + 1) * sizeCellWidth, (y + 1) * sizeCellHeight),
                    ((x) * sizeCellWidth, (y + 1) * sizeCellHeight)]
            if newGameState[x,y] == 0:
                pygame.draw.polygon(screen, (128,128,128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255,255,255), poly, 0)
    time.sleep(0.1)
    gameState = np.copy(newGameState)
    pygame.display.flip()



