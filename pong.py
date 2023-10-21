import pygame
import gamefunc
from enum import Enum
vec = pygame.math.Vector2

class playstate(Enum):
    active = 0
    p1turn = 1
    p2turn = 2

currentPlaystate = playstate.p1turn

class Player(gamefunc.Entity):
    def __init__(self,name, controlmap, width, height, posX, posY, colour, speed):
        super().__init__(name, width, height, posX, posY, colour)
        self.controlmap = controlmap
        self.vel = vec(0, 0)
        self.spd = speed

    def update(self):

        pressed_keys = pygame.key.get_pressed()

        # if pressed_keys[pygame.K_LEFT]:
        #     self.vel += vec(-1, 0)
        # if pressed_keys[pygame.K_RIGHT]:
        #     self.vel += vec(1, 0)
        if pressed_keys[self.controlmap.up]:
            self.vel += vec(0, -1)
        if pressed_keys[self.controlmap.down]:
            self.vel += vec(0, 1)
        #else:
        if not pressed_keys[self.controlmap.left] and not pressed_keys[self.controlmap.right] and not pressed_keys[self.controlmap.up] and not pressed_keys[self.controlmap.down]:
            self.vel = vec(0,0)
        #else:
        #self.vel *= self.spd * clock.get_time() / 1000
        if self.vel != vec(0,0):    self.vel = self.vel.normalize() * self.spd * gamefunc.deltaTime()

        self.pos += self.vel

        #if self.pos.x > WIDTH:
        #    self.pos.x = 0
        #if self.pos.x < 0:
        #    self.pos.x = WIDTH

        self.rect.center = self.pos

class Ball(gamefunc.Entity):
    def __init__(self,name, width, height, posX, posY, colour, speed):
        super().__init__(name, width, height, posX, posY, colour)

        self.speed = speed
        self.vel = vec(0,0)
        #global currentPlaystate

    def launch(self):

        global currentPlaystate
        if pygame.key.get_pressed()[paddle1.controlmap.action1] and currentPlaystate == playstate.p1turn:
            self.vel = vec(1,0) * self.speed
            currentPlaystate = playstate.active
            print("playstate0")
        if pygame.key.get_pressed()[paddle2.controlmap.action1] and currentPlaystate == playstate.p2turn:
            self.vel = vec(-1,0) * self.speed
            currentPlaystate = playstate.active
            print("playstate0")

    def bounce(self, direction):
        if self.vel.magnitude() != 0:
            self.vel = direction.normalize() * self.speed

    def update(self):
        global currentPlaystate
        for entity in gamefunc.entities:
            if entity.name != self.name:

                collide = self.rect.colliderect(entity)
                if collide:
                    self.bounce((self.pos - entity.pos).normalize())

        if self.pos.y + self.width/2 > gamefunc.HEIGHT or self.pos.y - self.width/2 < 0:
            self.bounce(vec(self.vel.x,-self.vel.y))

        if self.pos.x > gamefunc.WIDTH:
            self.pos = vec(gamefunc.WIDTH / 2, gamefunc.HEIGHT / 2)
            self.vel = vec(0, 0)

            global p1Score
            p1Score += 1
            print("p1score = " + str(p1Score))

            currentPlaystate = playstate.p2turn
            print("player 2 turn")
        if self.pos.x < 0:
            self.pos = vec(gamefunc.WIDTH/2,gamefunc.HEIGHT/2)
            self.vel = vec(0,0)

            global p2Score
            p2Score += 1
            print("p2score = " + str(p2Score))
            #global currentPlaystate
            currentPlaystate = playstate.p1turn
            print("player 1 turn")

        self.pos += self.vel * gamefunc.deltaTime()
        self.rect.center = self.pos


player1controls = gamefunc.ControlMap(1, pygame.K_w, pygame.K_s,pygame.K_a, pygame.K_d, pygame.K_f, pygame.K_g)
player2controls = gamefunc.ControlMap(2, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_k,pygame.K_l)

paddle1 = Player("Player1",player1controls, 32,160,16,300, gamefunc.white, 300)
paddle2 = Player("Player2",player2controls, 32,160,gamefunc.WIDTH - 16,300, gamefunc.white, 300)

ball = Ball("Ball",32,32,gamefunc.WIDTH / 2, gamefunc.HEIGHT / 2, gamefunc.white, 500)

global scoreFont
global displayp1score
global displayp2score
global displayp1scorerect
global displayp2scorerect

def init():
    p1Score = 0
    p2Score = 0
    scoreFont = pygame.font.Font('RobotoBold-Xdoj.ttf', 32)

    displayp1score = scoreFont.render(str(p1Score), True, gamefunc.white)
    displayp2score = scoreFont.render(str(p2Score), True, gamefunc.white)
    displayp1scorerect = displayp1score.get_rect(center=(gamefunc.WIDTH / 2 - 50, 50)).center
    displayp2scorerect = displayp2score.get_rect(center=(gamefunc.WIDTH / 2 + 50, 50)).center

    gamefunc.entities.add(paddle1)
    gamefunc.entities.add(paddle2)
    gamefunc.entities.add(ball)
    #currentPlaystate = playstate.p1turn

    #print(str(len(entities)) + " entities present")
    print(f"{str(len(gamefunc.entities))} entities present")

def update(screen):
    paddle1.update()
    paddle2.update()
    ball.launch()
    ball.update()

    # for entity in entities:
    #     entity.rect.center += vec(2,0)

    for entity in gamefunc.entities:
        screen.blit(entity.surf, entity.rect)



    displayp1score = scoreFont.render(str(p1Score), True, gamefunc.white)
    displayp2score = scoreFont.render(str(p2Score), True, gamefunc.white)
    screen.blit(displayp1score, displayp1scorerect)
    screen.blit(displayp2score, displayp2scorerect)

    screen.blit(paddle1.surf, paddle1.rect)
    screen.blit(paddle2.surf, paddle2.rect)