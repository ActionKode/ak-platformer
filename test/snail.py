# Pygame template - skeleton for a new pygame project
import pygame
import random
from sys import exit
WIDTH = 800
HEIGHT = 600
FPS = 30
G_PATH = "images/graphics/"

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self, ground):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(G_PATH + "Player/player_stand.png").convert_alpha()
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

    def update(self):
        self.dx = 0
        self.dy = 0
        self.dy += self.vel_y
        if self.vel_y > 10:
            self.vel_y = 10
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
            self.dx = 7
        if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
            self.dx = -7
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
            self.image = pygame.image.load(G_PATH + "Player/player_stand.png").convert_alpha()

    def jump(self):
        self.vel_y = -15
        self.jumped = True

    def get_hurt(self):
        self.hurt = True
        self.image = pygame.image.load(G_PATH + "Player/player_stand_hurt.png").convert_alpha()
        self.jump()


class Sky(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(G_PATH + 'Sky.png').convert_alpha(), (WIDTH, HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2

    def update(self):
        pass


class Sword(pygame.sprite.Sprite):
    def __init__(self, x, y, dx):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 10))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
        self.dx = dx

    def update(self):
        self.rect.x += self.dx


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(G_PATH + 'ground.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.y = HEIGHT - 100

    def update(self):
        pass


class Enemy(pygame.sprite.Sprite):
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
        self.last_update = 0

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
sky = Sky()
ground = Ground()
player = Player(ground)
snail = Enemy(player)
all_sprites.add(sky)
enemies.add(snail)
all_sprites.add(ground)
all_sprites.add(player)
all_sprites.add(snail)
# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    hits = pygame.sprite.spritecollide(player, enemies, False)
    for hit in hits:
        if not player.hurt:
            player.health -= 10
            player.get_hurt()

    # Update
    all_sprites.update()
    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()