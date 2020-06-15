import pygame, sys, os, time
from pygame.locals import *   #load constants
import time
import random

#Initialize PYGAME
pygame.init()

red=[0,0,255]   #RGB [RED,GREEN,BLUE]
black=(100,0,0)
white=(255,255,255)

window_width = 800
window_height = 600


#set up window
gamedisplay = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Slither- Yayy!')
font = pygame.font.SysFont(None, 35 , bold=True)

clock = pygame.time.Clock()
FPS = 5                         #frames per second
blocksize  = 20
noPixel= 0

def myquit():
    pygame.quit()
    sys.exit(0)
#eof

def snake(blocksize,snakelist):
    for size in snakelist:
        pygame.draw.rect(gamedisplay, black, (size[0]+5, size[1], blocksize,blocksize),2)

def message_to_screen(msg,color):
    screen_txt =font.render(msg, True , color)
    gamedisplay.blit(screen_txt,[(int(window_width)/2 - 300),int(window_height)/2])

def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = window_width / 2
    lead_y = window_height / 2

    change_pixels_of_x = 0
    change_pixels_of_y = 0

    snakelist = []    # initial snake
    snakeLength = 1

    #creates target at random places
    randomAppleX = round(random.randrange(0, window_width - blocksize) / 10.0) * 10.0
    randomAppleY = round(random.randrange(0, window_height - blocksize) / 10.0) * 10.0

    while not gameExit:         #Total game close

        while gameOver == True:
            gamedisplay.fill(white)
            message_to_screen("Game over,press c to play again or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False

                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:     #escape key- Quit the program
                    myquit()

                leftArrow  = event.key == pygame.K_LEFT
                rightArrow = event.key == pygame.K_RIGHT
                upArrow    = event.key == pygame.K_UP
                downArrow  = event.key == pygame.K_DOWN

                if leftArrow:
                    change_pixels_of_x = -blocksize
                    change_pixels_of_y = noPixel

                elif rightArrow:
                    change_pixels_of_x = blocksize
                    change_pixels_of_y = noPixel

                elif upArrow:
                    change_pixels_of_y = -blocksize
                    change_pixels_of_x = noPixel

                elif downArrow:
                    change_pixels_of_y = blocksize
                    change_pixels_of_x = noPixel

            #Ends the game on reaching boundry
            if lead_x >= window_width or lead_x < 0 or lead_y >= window_height or lead_y < 0:
                gameOver = True

        lead_x += change_pixels_of_x
        lead_y += change_pixels_of_y
        gamedisplay.fill(white)

        #draw the target
        AppleThickness = 20
        print([int(randomAppleX), int(randomAppleY), AppleThickness, AppleThickness])
        pygame.draw.rect(gamedisplay, red, [randomAppleX, randomAppleY, AppleThickness, AppleThickness])

        allspriteslist = []
        allspriteslist.append(lead_x)
        allspriteslist.append(lead_y)
        snakelist.append(allspriteslist)

        #deletes the current snake
        if len(snakelist) > snakeLength:
            del snakelist[0]

        for eachSegment in snakelist[:-1]:
            if eachSegment == allspriteslist:
                gameOver = True

        snake(blocksize, snakelist)
        pygame.display.update()

        #increase snake length on reaching target
        if lead_x >= randomAppleX and lead_x <= randomAppleX + AppleThickness:
            if lead_y >= randomAppleY and lead_y <= randomAppleY + AppleThickness:
                randomAppleX = round(random.randrange(0, window_width - blocksize) / 10.0) * 10.0
                randomAppleY = round(random.randrange(0, window_height - blocksize) / 10.0) * 10.0
                snakeLength += 1

        clock.tick(FPS)

    myquit()

gameLoop()

