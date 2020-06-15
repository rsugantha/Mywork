import pygame, sys, os
from pygame.locals import *   #load constants
import time


red=[255,0,0]                 #RGB [RED,GREEN,BLUE]
SHADOW = (192, 192, 192)
PURPLE = (102, 0, 102)
LPURPLE= (153, 0, 153)
LBLUE= (0, 0, 255)
GREEN = (0, 200, 0 )

#Initialize PYGAME
pygame.init()

#set up window

window1 = pygame.display.set_mode((800,800))
pygame.display.set_caption('First pygame-yay!')

#set up surface

screen1= pygame.display.get_surface()
screen1.fill(red)                                   #fills the screen with base colour
pygame.draw.rect(screen1,LBLUE,(100,150,100,10))    #draws the shape
pygame.display.flip()

#delay creation
clock = pygame.time.Clock()
clock.tick(1)       #Frames per second=1
pygame.time.delay(500)          #delay for milliseconds

# #insert image
screen1.fill(LPURPLE)    #create new background
pygame.display.flip()

image = pygame.image.load(r'C:\Users\Rishav\Documents\GitHub\Mywork\DSC_0199.jpg')
image = pygame.transform.scale(image, (1000, 1000))   #adjust image size
screen1.blit(image, (0, 0))                           #display image


'''#pixal array
pixobj=pygame.PixelArray(screen1)
pixobj[380][280] = red'''

#Loop to tract inputs - mouse/keyborad/joystick

running = True

while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:               #quits the loop
            #running = False
            pygame.quit()                           #shut down pygame (this includes closing the window)
            sys.exit()                              #shut down the program (this exits the infinite loop)
    pygame.display.update()