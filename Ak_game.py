# I dont know what this is 

import pygame
import random
from sprites import *
import pyautogui
import sys
gwidth, gheight = pyautogui.size()

WIDTH = gwidth
HEIGHT = gheight
FPS = 120
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FONT_NAME = 'arial'
pygame.mixer.init()
pygame.mixer.music.load('audio/level 1.wav')


class Game:
    def __init__(self):
        # initialize game window, etc
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Lil Brute")
        self.clock = pygame.time.Clock()
        self.running = True
        self.font_name = pygame.font.match_font(FONT_NAME)
        self.load_data()

    def load_data(self):
        pass

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.swords = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.sky = Sky()
        self.ground = Ground()
        self.player = Player(ground)
        self.snail = Snail(player)
        self.all_sprites.add(sky)
        self.enemies.add(snail)
        self.all_sprites.add(ground)
        self.all_sprites.add(player)
        self.all_sprites.add(snail)
        self.run()

    def run(self):
        # Game Loop
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(.5)
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            
        pygame.mixer.music.fadeout(500)

    def update(self):
        hits = pygame.sprite.groupcollide(self.swords, self.enemies, True, True)
        hits = pygame.sprite.spritecollide(self.player, self.enemies, False)
        for hit in hits:
            self.player.health -= 10
            self.player.get_hurt()
            if self.player.health == 0:
                self.playing = False
        # Game Loop - Update
        self.all_sprites.update()

    def events(self):
        # Game Loop - events
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    global shots
                    if player.right:
                        sword = Sword(player.rect.centerx, player.rect.midleft, 10)
                        self.all_sprites.add(sword)
                        self.swords.add(sword)
                    if player.left:
                        sword = Sword(player.rect.centerx, player.rect.midleft, -10)
                        self.all_sprites.add(sword)
                        self.swords.add(sword)
                    shots = True
                if event.key == pygame.K_ESCAPE:
                    g.running = False
                    pygame.quit()
                    sys.exit()

    def draw(self):
        # Game Loop - draw
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)
        self.draw_text("PLAYER HEALTH: " + str(self.player.health), 50, BLACK, WIDTH / 2, 15)
        self.draw_text("I DONT NKOW THAT IHIS IS. press 'esc' to exit" , 50, BLACK, WIDTH / 2, 75)
        # *after* drawing everything, flip the display
        pygame.display.flip()

    def show_start_screen(self):
        pass

    def show_level_screen(self):
        pass

    def show_go_screen(self):
        pass

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYUP:
                    waiting = False

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


g = Game()
g.show_start_screen()
g.show_level_screen()
while g.running:
    g.new()
    g.show_level_screen()
pygame.quit()
