# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# import numpy as np]
import pygame
import sys
from enum import Enum
import pong
import spaceInvaders
import gamefunc

pygame.init()

vec = pygame.math.Vector2  # 2 for two dimensional


def init():

    gameselect = input("p = pong, i = invaders")
    if gameselect == "p":
        pong.init()
        main(pong)
    if gameselect == "i":
        spaceInvaders.init()
        main(spaceInvaders)



def main(gameModule):
    # initialize the pygame module

    # load and set the logo
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("Iungo")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((gamefunc.WIDTH, gamefunc.HEIGHT))

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
                pygame.quit()
                sys.exit()

        screen.fill((0,0,0))
        gameModule.update(screen)

        gamefunc.fpsDisplay(screen)
        pygame.display.update()
        gamefunc.clock.tick(gamefunc.FPS)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    init()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
