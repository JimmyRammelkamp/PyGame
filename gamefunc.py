import pygame
vec = pygame.math.Vector2

HEIGHT = 600
WIDTH = 800
FPS = 60

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

entities = pygame.sprite.Group()

clock = pygame.time.Clock()
def deltaTime():
    return clock.get_time() / 1000

class Entity(pygame.sprite.Sprite):
    def __init__(self, name, width, height, posX, posY, colour):
        super().__init__()
        self.width = width
        self.height = height
        self.name = name
        self.pos = vec((posX, posY))
        self.surf = pygame.Surface((width, height))
        self.surf.fill(colour)
        self.rect = self.surf.get_rect(center=(posX, posY))

        print("Entity " + self.name + " generated.")


class ControlMap():
    def __init__(self,player,up,down,left,right,action1,action2):
        self.player = player
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.action1 = action1
        self.action2 = action2