import pygame, sys, os
from pygame.locals import *   #load constants
import time

#Initialize PYGAME
pygame.init()

#set up window
winwidth  = 800
winheight = 800
window1 = pygame.display.set_mode((winwidth,winheight))
pygame.display.set_caption('Ping Pong!')

font = pygame.font.SysFont(None, 35 , bold=True)
clock = pygame.time.Clock()


#set up surface
screen1= pygame.display.get_surface()
image = pygame.image.load(r'D:\Priya\Python\img1.jpg')
screen1.blit(image, (0, 0))                           #display image

#def variables
score = 0
max_score = 50

red=[255,0,0]                 #RGB [RED,GREEN,BLUE]
SHADOW = (192, 192, 192)
PURPLE = (102, 0, 102)
LPURPLE= (153, 0, 153)
LBLUE= (0, 0, 255)
GREEN = (0, 200, 0 )

def myquit():
    pygame.quit()  # shut down pygame (this includes closing the window)
    sys.exit()

def newball():
    pass
def moveball():
    pass

def  slider():
    pass

def moveslider():
    pass

def sendmsg(msg,color):
    txt = font.render(msg, True, color)
    screen1.blit(txt, [(int(winwidth) / 2 ), int(winheight) / 2])

def button(msg,x,y,w,h,ic,ac):
    pygame.draw.rect(screen1, ac, (x, y, w, h))
    txt=font.render(msg, True, ic)
    screen1.blit(txt,[x,y])#, [(int(winwidth) / 2), int(winheight) / 2])
    pygame.display.update()

def getmouse():
    mouse = pygame.mouse.get_pos()
    if (x< mouse[0] > x + w) and (y < mouse[1] > y+h):
        print("continue")
    else: myquit()
    click = pygame.mouse.get_pressed()
    print(click)

def gameloop():
    pass


#run the game
running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:               #quits the game
            running = False
        elif score == 0:
            #sendmsg("Game over!",red)
            button("Game over!", 350, 250, 160, 30,  red, SHADOW)
            button(" Play Again", 150, 450, 160, 30,  red, SHADOW)
            button("  Quit  ", 550, 450, 100, 30, red, SHADOW)
            pygame.display.update()
            getmouse()
            clock.tick(15)
        else:
            gameloop()
            myquit()



    pygame.display.update()

