# Pygame template - skeleton for a new pygame project
# import random
# from typing import Sequence
from sys import exit
import pyautogui
import pygame

width, height = pyautogui.size()
shots = False
WIDTH = width
HEIGHT = height - 60
FPS = 60
G_PATH = "images/graphics/"
# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize pygame and create window
# turn on pygame
pygame.init()
pygame.display.set_caption("Cool Project")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/Base pack/Tiles/boxEmpty.png')#.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def update(self):
        pass


class Spike(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        pygame.image.load('images/Base pack/Items/spikes.png')#.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def update(self):
        pass


class Player(pygame.sprite.Sprite):
    def __init__(self, ground):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(G_PATH + "Player/player_stand.png")##.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.dx = 0
        self.dy = 0
        self.vel_y = 0
        self.ground = ground
        self.jumped = True
        self.hurt = False
        self.health = 100
        self.hurt_timer = 100
        self.last_update = 0
        self.last_shoot = 0
        self.left = False
        self.right = True

    def update(self):
        self.dx = 0
        self.dy = 0
        self.dy += self.vel_y
        if self.vel_y > 10:
            self.vel_y = 10
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
            self.dx = 7
            self.left = False
            self.right = True
        if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
            self.dx = -7
            self.right = False
            self.left = True
        if keystate[pygame.K_DOWN] or keystate[pygame.K_s]:
            if pygame.time.get_ticks() - self.last_shoot > 500:
                self.shoot()
                self.last_shoot = pygame.time.get_ticks()
        if (keystate[pygame.K_UP] or keystate[pygame.K_w]) and not self.jumped:
            self.jump()
        if self.rect.bottom > self.ground.rect.top:
            self.rect.bottom = self.ground.rect.top
            self.jumped = False
        else:
            self.vel_y += 1
            self.jumped = True
        self.rect.y += self.dy
        self.rect.x += self.dx
        if self.health <= 0:
            self.health = 0
            self.kill()
        now = pygame.time.get_ticks()
        if now - self.last_update > self.hurt_timer:
            self.hurt = False
            self.last_update = now
            self.image = pygame.image.load(G_PATH + "Player/player_stand.png")#.convert_alpha()

    def jump(self):
        self.vel_y = -15
        self.jumped = True

    def get_hurt(self):
        self.hurt = True
        self.image = pygame.image.load(G_PATH + "Player/player_stand_hurt.png")#.convert_alpha()
        self.jump()

    def shoot(self):
        global shots
        if self.right:
            sword = Sword(self.rect.centerx, self.rect.midleft, 10)
            all_sprites.add(sword)
        if self.left:
            sword = Sword(self.rect.centerx, self.rect.midleft, -10)
            all_sprites.add(sword)
        shots = True


class Sky(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(G_PATH + 'Sky.png'), (WIDTH, HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2

    def update(self):
        pass


class Sword(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        self.move = False
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.rotate(pygame.image.load(G_PATH + 'Player/sword.png'), -45)
        self.rect = self.image.get_rect()
        self.rect.midleft = y
        self.rect.centerx = x
        self.dx = 0
        self.dy = 0
        self.speedx = speed
        self.last_update = 0

    def update(self):
        self.rect.x += self.speedx
        # kill if it moves off the top of the screen
        if self.rect.x < 0 or self.rect.x > WIDTH:
            self.kill()
        if self.speedx < 0:
            self.image = pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load(G_PATH + 'Player/sword.png'), -45), True,
                False)


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(G_PATH + 'ground.png'), (WIDTH, 168))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.rect.y = HEIGHT - 100

    def update(self):
        pass


class Snail(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(G_PATH + "snail/snail1.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 100
        self.rect.bottom = HEIGHT - 100
        self.dx = 0
        self.dy = 0
        self.player = player
        self.move = False
        self.hurt = False
        self.last_update = 0

    def get_hurt(self):
        self.hurt = True

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        now = pygame.time.get_ticks()
        if now - self.last_update > 2000:
            self.move = True
        if self.player.rect.centerx > self.rect.centerx and self.move:
            self.dx = 2
            self.image = pygame.transform.flip(pygame.image.load(G_PATH + "snail/snail1.png"), True, False)
        if self.player.rect.centerx < self.rect.centerx and self.move:
            self.dx = -2
            self.image = pygame.image.load(G_PATH + "snail/snail1.png")


all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
plat = Platform(0, 500)
sky = Sky()
ground = Ground()
player = Player(ground)
snail = Snail(player)



def run():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Update
        all_sprites.update()
        # Draw / render
        screen.fill(BLACK)
        all_sprites.draw(screen)
        # *after* drawing everything, flip the display
        pygame.display.flip()


pygame.quit()
