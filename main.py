# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# import numpy as np]
import pygame
import sys

pygame.init()

vec = pygame.math.Vector2  # 2 for two dimensional

clock = pygame.time.Clock()
def deltaTime():
    return clock.get_time() / 1000


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)



class Entity(pygame.sprite.Sprite):
    def __init__(self, name, width, height, posX, posY, colour):
        super().__init__()

        self.name = name
        self.pos = vec((posX, posY))
        self.surf = pygame.Surface((width, height))
        self.surf.fill(colour)
        self.rect = self.surf.get_rect(center=(posX, posY))

        print("Entity " + self.name + " generated.")


class Player(Entity):
    def __init__(self,name, width, height, posX, posY, colour, speed):
        super().__init__(name, width, height, posX, posY, colour)

        self.vel = vec(0, 0)
        self.spd = speed

    def move(self):

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_LEFT]:
            self.vel += vec(-1, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.vel += vec(1, 0)
        if pressed_keys[pygame.K_UP]:
            self.vel += vec(0, -1)
        if pressed_keys[pygame.K_DOWN]:
            self.vel += vec(0, 1)
        #else:
        if not pressed_keys[pygame.K_LEFT] and not pressed_keys[pygame.K_RIGHT] and not pressed_keys[pygame.K_UP] and not pressed_keys[pygame.K_DOWN]:
            self.vel = vec(0,0)
        else:
        #self.vel *= self.spd * clock.get_time() / 1000
            self.vel = self.vel.normalize() * self.spd * deltaTime()

        self.pos += self.vel

        #if self.pos.x > WIDTH:
        #    self.pos.x = 0
        #if self.pos.x < 0:
        #    self.pos.x = WIDTH

        self.rect.midbottom = self.pos






entities = pygame.sprite.Group()


player = Player("Player1", 32,32,400,300, white, 15)



HEIGHT = 600
WIDTH = 800
FPS = 60




font = pygame.font.Font('RobotoBold-Xdoj.ttf', 16)
fpsText = font.render('FPS', True, green, blue)
fpsTextRect = fpsText.get_rect()




def init():

    entityCount = int(input("How many sprites to spawn?"))
    entityColour = input("r = red, g = green, b = blue:")


    if entityColour == "r":
        entityColour = red
    elif entityColour == "g":
        entityColour = green
    elif entityColour == "b":
        entityColour = blue
    else: entityColour = white


    i = 0
    while i < entityCount:
        ent = Entity(f"Entity {str(i)}", 32, 32, 0 + 32 * i, 0 + 32 * i, entityColour)
        entities.add(ent)
        i += 1

    entities.add(player)

    #print(str(len(entities)) + " entities present")
    print(f"{str(len(entities))} entities present")


def main():
    # initialize the pygame module

    # load and set the logo
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("Iungo")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

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

        player.move()

        for entity in entities:
            entity.rect.center += vec(2,0)

        for entity in entities:
            screen.blit(entity.surf, entity.rect)




        fpsText = font.render(str(int(clock.get_fps())),True,green,blue)
        #fpsText = font.render(str(pygame.time.Clock.get_time(clock)),True,green,blue)
        screen.blit(fpsText,fpsTextRect)


        screen.blit(player.surf, player.rect)

        pygame.display.update()
        clock.tick(FPS)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    init()
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
