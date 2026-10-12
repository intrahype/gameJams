import pygame
import sys

pygame.init()

black = 0,0,0
#returns a tuple for detected screensize [(height, width)]
screenSize = pygame.display.get_desktop_sizes()

screen = pygame.display.set_mode((screenSize[0][0],screenSize[0][1]))
gameFont = pygame.font.SysFont("Comic Sans", 50)

def welcome():
    greet = gameFont.render("Welcome to Forest Park", 1, (255,255,255))
    screen.blit(greet, (10,10))

    if event.type == pygame.KEYDOWN:
        if event.mod == pygame.K_RETURN:
            return

def parkLeft():
    parkLeft = gameFont.render("On your left you see a small gate leading to the old carousel", 1, (255,255,255))
    screen.fill(black)
    screen.blit(parkLeft, (10,10))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    welcome()
    
    parkLeft()

    

    pygame.display.flip()
pygame.QUIT()