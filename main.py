# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# import numpy as np]
import pygame
import sys
from enum import Enum
import pong
import gamefunc

pygame.init()

vec = pygame.math.Vector2  # 2 for two dimensional
# clock = pygame.time.Clock()


# def deltaTime():
#     return clock.get_time() / 1000


# white = (255, 255, 255)
# black = (0, 0, 0)
# red = (255, 0, 0)
# green = (0, 255, 0)
# blue = (0, 0, 255)

# HEIGHT = 600
# WIDTH = 800
# FPS = 60


# p1Score = 0
# p2Score = 0

# class playstate(Enum):
#     active = 0
#     p1turn = 1
#     p2turn = 2


# currentPlaystate = playstate.p1turn

# class ControlMap():
#     def __init__(self,player,up,down,left,right,action1,action2):
#         self.player = player
#         self.up = up
#         self.down = down
#         self.left = left
#         self.right = right
#         self.action1 = action1
#         self.action2 = action2


# class Entity(pygame.sprite.Sprite):
#     def __init__(self, name, width, height, posX, posY, colour):
#         super().__init__()
#         self.width = width
#         self.height = height
#         self.name = name
#         self.pos = vec((posX, posY))
#         self.surf = pygame.Surface((width, height))
#         self.surf.fill(colour)
#         self.rect = self.surf.get_rect(center=(posX, posY))
#
#         print("Entity " + self.name + " generated.")



# class Player(gamefunc.Entity):
#     def __init__(self,name, controlmap, width, height, posX, posY, colour, speed):
#         super().__init__(name, width, height, posX, posY, colour)
#         self.controlmap = controlmap
#         self.vel = vec(0, 0)
#         self.spd = speed
#
#     def update(self):
#
#         pressed_keys = pygame.key.get_pressed()
#
#         # if pressed_keys[pygame.K_LEFT]:
#         #     self.vel += vec(-1, 0)
#         # if pressed_keys[pygame.K_RIGHT]:
#         #     self.vel += vec(1, 0)
#         if pressed_keys[self.controlmap.up]:
#             self.vel += vec(0, -1)
#         if pressed_keys[self.controlmap.down]:
#             self.vel += vec(0, 1)
#         #else:
#         if not pressed_keys[self.controlmap.left] and not pressed_keys[self.controlmap.right] and not pressed_keys[self.controlmap.up] and not pressed_keys[self.controlmap.down]:
#             self.vel = vec(0,0)
#         #else:
#         #self.vel *= self.spd * clock.get_time() / 1000
#         if self.vel != vec(0,0):    self.vel = self.vel.normalize() * self.spd * deltaTime()
#
#         self.pos += self.vel
#
#         #if self.pos.x > WIDTH:
#         #    self.pos.x = 0
#         #if self.pos.x < 0:
#         #    self.pos.x = WIDTH
#
#         self.rect.center = self.pos


# class Ball(gamefunc.Entity):
#     def __init__(self,name, width, height, posX, posY, colour, speed):
#         super().__init__(name, width, height, posX, posY, colour)
#
#         self.speed = speed
#         self.vel = vec(0,0)
#         #global currentPlaystate
#
#     def launch(self):
#
#         global currentPlaystate
#         if pygame.key.get_pressed()[paddle1.controlmap.action1] and currentPlaystate == playstate.p1turn:
#             self.vel = vec(1,0) * self.speed
#             currentPlaystate = playstate.active
#             print("playstate0")
#         if pygame.key.get_pressed()[paddle2.controlmap.action1] and currentPlaystate == playstate.p2turn:
#             self.vel = vec(-1,0) * self.speed
#             currentPlaystate = playstate.active
#             print("playstate0")
#
#     def bounce(self, direction):
#         if self.vel.magnitude() != 0:
#             self.vel = direction.normalize() * self.speed
#
#     def update(self):
#         global currentPlaystate
#         for entity in entities:
#             if entity.name != self.name:
#
#                 collide = self.rect.colliderect(entity)
#                 if collide:
#                     self.bounce((self.pos - entity.pos).normalize())
#
#         if self.pos.y + self.width/2 > HEIGHT or self.pos.y - self.width/2 < 0:
#             self.bounce(vec(self.vel.x,-self.vel.y))
#
#         if self.pos.x > WIDTH:
#             self.pos = vec(WIDTH / 2, HEIGHT / 2)
#             self.vel = vec(0, 0)
#
#             global p1Score
#             p1Score += 1
#             print("p1score = " + str(p1Score))
#
#             currentPlaystate = playstate.p2turn
#             print("player 2 turn")
#         if self.pos.x < 0:
#             self.pos = vec(WIDTH/2,HEIGHT/2)
#             self.vel = vec(0,0)
#
#             global p2Score
#             p2Score += 1
#             print("p2score = " + str(p2Score))
#             #global currentPlaystate
#             currentPlaystate = playstate.p1turn
#             print("player 1 turn")
#
#         self.pos += self.vel * deltaTime()
#         self.rect.center = self.pos




# entities = pygame.sprite.Group()

# player1controls = gamefunc.ControlMap(1, pygame.K_w, pygame.K_s,pygame.K_a, pygame.K_d, pygame.K_f, pygame.K_g)
# player2controls = gamefunc.ControlMap(2, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_k,pygame.K_l)
#
# paddle1 = Player("Player1",player1controls, 32,160,16,300, white, 300)
# paddle2 = Player("Player2",player2controls, 32,160,WIDTH - 16,300, white, 300)
#
# ball = Ball("Ball",32,32,WIDTH / 2, HEIGHT / 2, white, 500)





fpsFont = pygame.font.Font('RobotoBold-Xdoj.ttf', 16)
fpsText = fpsFont.render('FPS', True, gamefunc.green)
fpsTextRect = fpsText.get_rect()


# scoreFont = pygame.font.Font('RobotoBold-Xdoj.ttf', 32)
# displayp1score = scoreFont.render(str(p1Score), True, gamefunc.white)
# displayp2score = scoreFont.render(str(p2Score), True, gamefunc.white)
# displayp1scorerect = displayp1score.get_rect(center=(gamefunc.WIDTH/2 - 50, 50)).center
# displayp2scorerect = displayp2score.get_rect(center=(gamefunc.WIDTH/2 + 50, 50)).center




def init():

    # entityCount = int(input("How many sprites to spawn?"))
    # entityColour = input("r = red, g = green, b = blue:")
    #
    #
    # if entityColour == "r":
    #     entityColour = red
    # elif entityColour == "g":
    #     entityColour = green
    # elif entityColour == "b":
    #     entityColour = blue
    # else: entityColour = white
    #
    #
    # i = 0
    # while i < entityCount:
    #     ent = Entity(f"Entity {str(i)}", 32, 32, 0 + 32 * i, 0 + 32 * i, entityColour)
    #     entities.add(ent)
    #     i += 1

    # entities.add(paddle1)
    # entities.add(paddle2)
    # entities.add(ball)
    # #currentPlaystate = playstate.p1turn
    #
    # #print(str(len(entities)) + " entities present")
    # print(f"{str(len(entities))} entities present")
    pong.init()


def main():
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

        fpsText = fpsFont.render(str(int(gamefunc.clock.get_fps())), True, gamefunc.green)
        # fpsText = font.render(str(pygame.time.Clock.get_time(clock)),True,green,blue)
        screen.blit(fpsText, fpsTextRect)
        # paddle1.update()
        # paddle2.update()
        # ball.launch()
        # ball.update()
        #
        #
        # # for entity in entities:
        # #     entity.rect.center += vec(2,0)
        #
        # for entity in entities:
        #     screen.blit(entity.surf, entity.rect)
        #
        #
        #
        #
        # fpsText = fpsFont.render(str(int(clock.get_fps())),True,green)
        # #fpsText = font.render(str(pygame.time.Clock.get_time(clock)),True,green,blue)
        # screen.blit(fpsText,fpsTextRect)
        #
        # displayp1score = scoreFont.render(str(p1Score), True, white)
        # displayp2score = scoreFont.render(str(p2Score), True, white)
        # screen.blit(displayp1score,displayp1scorerect)
        # screen.blit(displayp2score,displayp2scorerect)
        #
        #
        # screen.blit(paddle1.surf, paddle1.rect)
        # screen.blit(paddle2.surf, paddle2.rect)

        pong.update(screen)

        pygame.display.update()
        gamefunc.clock.tick(gamefunc.FPS)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    init()
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
