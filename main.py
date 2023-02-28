import pygame
import random
from sprite import *
from Settings import *

WIDTH = 800
HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Game:
    def __init__(self):
        # initialize game window, etc
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_icon(pygame.transform.scale(pygame.image.load(('images/Base pack/HUD/hud_gem_blue.png')), (32, 32)))
        pygame.display.set_caption("Lil Brute")
        self.clock = pygame.time.Clock()
        self.running = True
        self.level = 1
        #self.font_name = pygame.font.Font("Fonts\Inkfree.ttf", font_size)
        self.load_data()
        self.last_update = 0
        self.time = TIME

    def load_data(self):
        self.image1 = pygame.image.load(G_PATH + "LEVEL 1.png")
        self.image2 = pygame.image.load(G_PATH + "LEVEL 2.png")
        self.image3 = pygame.image.load(G_PATH + "LEVEL 3.png")
        self.image4 = pygame.image.load(G_PATH + "LEVEL 4.png")
        self.image5 = pygame.image.load(G_PATH + "LEVEL 5.png")

    def level_1(self):
        self.score = 0
        self.level = 1
        self.time = 100
        pygame.mixer.music.load(G_PATH_MBF + "Level 1.wav")
        self.spikes = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.scrolling_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.swords = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.winning_elements = pygame.sprite.Group()
        self.sky = Sky(WIDTH / 2)
        self.sky2 = Sky(WIDTH + 400)
        self.sky3 = Sky(WIDTH + 1000)
        self.all_sprites.add(self.sky2)
        self.all_sprites.add(self.sky3)
        self.scrolling_sprites.add(self.sky2)
        self.scrolling_sprites.add(self.sky3)
        self.ground = Ground(WIDTH / 2)
        self.ground2 = Ground(WIDTH + 600)
        self.ground3 = Ground(WIDTH + 800)
        self.ground4 = Ground(WIDTH + 1200)
        self.player = Player(self.ground, self.all_sprites, self.swords, self)
        self.snail = Enemy(self.player, WIDTH - 100, self)
        self.winning_element = WinningElement(WIDTH + 950)
        self.all_sprites.add(self.sky)
        self.enemies.add(self.snail)
        self.all_sprites.add(self.ground)
        self.all_sprites.add(self.ground2)
        self.all_sprites.add(self.ground3)
        self.all_sprites.add(self.ground4)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.snail)
        for COIN in COIN_LIST:
            self.coin = Coin(*COIN, self)
            self.all_sprites.add(self.coin)
            self.scrolling_sprites.add(self.coin)
            self.coins.add(self.coin)
        self.scrolling_sprites.add(self.sky)
        self.scrolling_sprites.add(self.ground)
        self.scrolling_sprites.add(self.ground2)
        self.scrolling_sprites.add(self.ground3)
        self.scrolling_sprites.add(self.ground4)
        self.scrolling_sprites.add(self.player)
        self.scrolling_sprites.add(self.snail)
        self.all_sprites.add(self.winning_element)
        self.scrolling_sprites.add(self.winning_element)
        self.winning_elements.add(self.winning_element)
        self.run()

    def level_2(self):
        self.level = 2
        self.time = 100
        pygame.mixer.music.load(G_PATH_MBF + "Level 2.wav")
        self.all_sprites = pygame.sprite.Group()
        self.spikes = pygame.sprite.Group()
        self.scrolling_sprites = pygame.sprite.Group()
        self.swords = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.buttons = pygame.sprite.Group()
        self.winning_elements = pygame.sprite.Group()
        self.sky = Sky(WIDTH / 2)
        self.sky3 = Sky(WIDTH + 400)
        self.sky4 = Sky(WIDTH + 1200)
        self.all_sprites.add(self.sky2)
        self.all_sprites.add(self.sky3)
        self.all_sprites.add(self.sky4)
        self.scrolling_sprites.add(self.sky2)
        self.scrolling_sprites.add(self.sky3)
        self.scrolling_sprites.add(self.sky4)
        self.ground = GroundAlt(WIDTH / 2)
        self.ground2 = GroundAlt(WIDTH + 600)
        self.ground3 = GroundAlt(WIDTH + 1000)
        self.ground4 = GroundAlt(WIDTH + 1000)
        self.player = Player(self.ground, self.all_sprites, self.swords, self)
        self.snail = Enemy(self.player, WIDTH + 1200, self)
        self.snail2 = Enemy(self.player, WIDTH + 900, self)
        self.winning_element = WinningElement(WIDTH + 950)
        self.button = Button(100, self)
        self.spike = Spike(WIDTH + 400, self)
        self.spike2 = Spike(WIDTH + 470, self)
        self.all_sprites.add(self.sky)
        self.enemies.add(self.snail)
        self.enemies.add(self.snail2)
        self.all_sprites.add(self.spike)
        self.scrolling_sprites.add(self.spike)
        self.spikes.add(self.spike)
        self.all_sprites.add(self.spike2)
        self.scrolling_sprites.add(self.spike2)
        self.spikes.add(self.spike2)
        self.all_sprites.add(self.ground)
        self.all_sprites.add(self.ground2)
        self.all_sprites.add(self.ground3)
        self.all_sprites.add(self.ground4)
        self.all_sprites.add(self.button)
        self.scrolling_sprites.add(self.button)
        self.buttons.add(self.button)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.snail)
        self.all_sprites.add(self.snail2)
        for COIN in COIN_LIST:
            self.coin = Coin(*COIN, self)
            self.all_sprites.add(self.coin)
            self.scrolling_sprites.add(self.coin)
            self.coins.add(self.coin)
        self.scrolling_sprites.add(self.sky)
        self.scrolling_sprites.add(self.ground)
        self.scrolling_sprites.add(self.ground2)
        self.scrolling_sprites.add(self.ground3)
        self.scrolling_sprites.add(self.ground4)
        self.scrolling_sprites.add(self.player)
        self.scrolling_sprites.add(self.snail)
        self.scrolling_sprites.add(self.snail2)
        self.all_sprites.add(self.winning_element)
        self.scrolling_sprites.add(self.winning_element)
        self.winning_elements.add(self.winning_element)
        self.run()

    def level_3(self):
        self.level = 3
        self.time = 100
        pygame.mixer.music.load(G_PATH_MBF + "Level 3.wav")
        self.all_sprites = pygame.sprite.Group()
        self.scrolling_sprites = pygame.sprite.Group()
        self.swords = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.winning_elements = pygame.sprite.Group()
        self.sky = SkyAlt(WIDTH / 2)
        self.sky3 = SkyAlt(WIDTH + 400)
        self.sky4 = SkyAlt(WIDTH + 1200)
        self.all_sprites.add(self.sky2)
        self.all_sprites.add(self.sky3)
        self.all_sprites.add(self.sky4)
        self.scrolling_sprites.add(self.sky2)
        self.scrolling_sprites.add(self.sky3)
        self.scrolling_sprites.add(self.sky4)
        self.ground = GroundAlt_2(WIDTH / 2)
        self.ground2 = GroundAlt_2(WIDTH + 600)
        self.ground3 = GroundAlt_2(WIDTH + 1000)
        self.ground4 = GroundAlt_2(WIDTH + 1000)
        self.player = Player(self.ground, self.all_sprites, self.swords, self)
        self.snail = Enemy(self.player, 0, self)
        self.snail2 = Enemy(self.player, WIDTH + 1000, self)
        self.winning_element = WinningElement(WIDTH + 950)
        self.all_sprites.add(self.sky)
        self.enemies.add(self.snail)
        self.enemies.add(self.snail2)
        self.all_sprites.add(self.ground)
        self.all_sprites.add(self.ground2)
        self.all_sprites.add(self.ground3)
        self.all_sprites.add(self.ground4)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.snail)
        self.all_sprites.add(self.snail2)
        for COIN in COIN_LIST:
            self.coin = Coin(*COIN, self)
            self.all_sprites.add(self.coin)
            self.scrolling_sprites.add(self.coin)
            self.coins.add(self.coin)
        self.scrolling_sprites.add(self.sky)
        self.scrolling_sprites.add(self.ground)
        self.scrolling_sprites.add(self.ground2)
        self.scrolling_sprites.add(self.ground3)
        self.scrolling_sprites.add(self.ground4)
        self.scrolling_sprites.add(self.player)
        self.scrolling_sprites.add(self.snail)
        self.scrolling_sprites.add(self.snail2)
        self.all_sprites.add(self.winning_element)
        self.scrolling_sprites.add(self.winning_element)
        self.winning_elements.add(self.winning_element)
        self.run()

    def level_4(self):
        self.level = 4
        self.time = 50
        pygame.mixer.music.load(G_PATH_MBF + "Level 1.wav")
        self.all_sprites = pygame.sprite.Group()
        self.scrolling_sprites = pygame.sprite.Group()
        self.swords = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.winning_elements = pygame.sprite.Group()
        self.sky = SkyAlt(WIDTH / 2)
        self.sky3 = SkyAlt(WIDTH + 400)
        self.sky4 = SkyAlt(WIDTH + 1200)
        self.all_sprites.add(self.sky3)
        self.all_sprites.add(self.sky4)
        self.scrolling_sprites.add(self.sky3)
        self.scrolling_sprites.add(self.sky4)
        self.scrolling_sprites.add(self.sky)
        self.snail = Enemy(self.player, WIDTH + 500, self)
        self.all_sprites.add(self.snail)
        self.enemies.add(self.snail)
        self.scrolling_sprites.add(self.snail)
        self.snail2 = Enemy(self.player, WIDTH + 1200, self)
        self.all_sprites.add(self.snail2)
        self.enemies.add(self.snail2)
        self.scrolling_sprites.add(self.snail2)
        self.player = Player(self.ground, self.all_sprites, self.swords, self)
        self.winning_element = WinningElement(WIDTH + 950)
        self.ground = GroundAlt_3(WIDTH / 2)
        self.ground2 = GroundAlt_3(WIDTH + 400)
        self.ground3 = GroundAlt_3(WIDTH + 1000)
        self.ground4 = GroundAlt_3(WIDTH + 1000)
        self.all_sprites.add(self.sky)
        self.all_sprites.add(self.ground)
        self.all_sprites.add(self.ground2)
        self.all_sprites.add(self.ground3)
        self.all_sprites.add(self.ground4)
        self.scrolling_sprites.add(self.ground)
        self.scrolling_sprites.add(self.ground2)
        self.scrolling_sprites.add(self.ground3)
        self.scrolling_sprites.add(self.ground4)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.winning_element)
        self.scrolling_sprites.add(self.winning_element)
        self.winning_elements.add(self.winning_element)
        self.run()

    def level_5(self):
        self.level = 5
        self.time = 100
        pygame.mixer.music.load(G_PATH_MBF + "Level 2.wav")
        self.all_sprites = pygame.sprite.Group()
        self.buttons = pygame.sprite.Group()
        self.scrolling_sprites = pygame.sprite.Group()
        self.swords = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.winning_elements = pygame.sprite.Group()
        self.sky = SkyAlt(WIDTH / 2)
        self.sky3 = SkyAlt(WIDTH + 400)
        self.sky4 = SkyAlt(WIDTH + 1200)
        self.button = Button(100, self)
        self.all_sprites.add(self.sky)
        self.all_sprites.add(self.sky3)
        self.all_sprites.add(self.sky4)
        self.scrolling_sprites.add(self.sky3)
        self.scrolling_sprites.add(self.sky4)
        self.scrolling_sprites.add(self.sky)
        self.snail = Enemy(self.player, WIDTH + 500, self)
        self.all_sprites.add(self.snail)
        self.enemies.add(self.snail)
        self.scrolling_sprites.add(self.snail)
        self.spike = Spike(WIDTH + 800, self)
        self.spike.rect.bottom = HEIGHT - 150
        self.player = Player(self.ground, self.all_sprites, self.swords, self)
        self.winning_element = WinningElement(WIDTH + 950)
        self.ground = GroundAlt_2(WIDTH / 2)
        self.ground2 = GroundAlt_2(WIDTH)
        self.ground3 = GroundAlt(WIDTH + 1000)
        self.ground3.rect.y = HEIGHT - 150
        self.all_sprites.add(self.spike)
        self.scrolling_sprites.add(self.spike)
        self.spikes.add(self.spike)
        self.all_sprites.add(self.ground)
        self.all_sprites.add(self.ground2)
        self.all_sprites.add(self.ground3)
        self.scrolling_sprites.add(self.ground)
        self.scrolling_sprites.add(self.ground2)
        self.scrolling_sprites.add(self.ground3)
        self.all_sprites.add(self.button)
        self.scrolling_sprites.add(self.button)
        self.buttons.add(self.button)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.winning_element)
        self.scrolling_sprites.add(self.winning_element)
        self.winning_elements.add(self.winning_element)
        self.run()

    def run(self):
        # Game Loop
        pygame.mixer.music.play(-1)
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        pygame.mixer.music.fadeout(500)

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 500:
            self.time -= 1
            self.last_update = now
        hits = pygame.sprite.groupcollide(self.swords, self.enemies, True, True)
        for hit in hits:
            self.score += 10
        hits = pygame.sprite.spritecollide(self.player, self.winning_elements, True)
        if hits:
            self.playing = False
            self.level += 1
        hits = pygame.sprite.spritecollide(self.player, self.coins, True)
        for hit in hits:
            self.score += 10
            hit.kill()
        hits = pygame.sprite.spritecollide(self.player, self.enemies, False)
        for hit in hits:
            if not self.player.hurt:
                self.player.get_hurt()
            if self.player.health == 0:
                self.playing = False
                self.score = 0
        hits = pygame.sprite.spritecollide(self.player, self.spikes, False)
        for hit in hits:
            if not self.player.hurt:
                self.player.get_hurt()
            if self.player.health == 0:
                self.playing = False
                self.score = 0
        if not self.ground.rect.left <= -1200:
            if self.player.rect.right > WIDTH / 4 * 3:
                for sprite in self.scrolling_sprites:
                    self.player.rect.right = WIDTH / 4 * 3
                    sprite.rect.x -= 5
        if not self.ground.rect.left == 0:
            if self.player.rect.left < WIDTH / 4:
                for sprite in self.scrolling_sprites:
                    self.player.rect.left = WIDTH / 4
                    sprite.rect.x += 5
        if (self.player.rect.bottom > self.ground.rect.top
            and self.player.rect.left <= self.ground.rect.right
            and self.player.rect.right >= self.ground.rect.left
            and self.player.rect.top + self.player.rect.height < self.ground.rect.bottom):
            self.player.rect.bottom = self.ground.rect.top
            self.player.dy = 0
            self.player.jumped = False
        elif (self.player.rect.bottom > self.ground2.rect.top
             and self.player.rect.left <= self.ground2.rect.right
             and self.player.rect.right >= self.ground2.rect.left
             and self.player.rect.top + self.player.rect.height < self.ground2.rect.bottom):
            self.player.rect.bottom = self.ground2.rect.top
            self.player.dy = 0
            self.player.jumped = False
        elif (self.player.rect.bottom > self.ground3.rect.top and self.player.rect.left <= self.ground3.rect.right and self.player.rect.right >= self.ground3.rect.left
              and self.player.rect.top + self.player.rect.height < self.ground3.rect.bottom):
            self.player.rect.bottom = self.ground3.rect.top
            self.player.dy = 0
            self.player.jumped = False
        else:
            self.player.vel_y += 1
            self.player.jumped = True

        if self.player.rect.top > HEIGHT:
            self.playing = False
            self.score = 0

        if self.time == 0:
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
                pygame.quit()

    def draw(self):
        # Game Loop - draw
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)
        self.draw_text("SCORE: " + str(self.score), 25, BLACK, 75, 40)
        self.draw_text("PLAYER: " + str(self.player.health), 25, BLACK, 75, 10)
        self.draw_text("TIME: " + str(self.time), 25, BLACK, WIDTH - 75, 25)
        # *after* drawing everything, flip the display
        pygame.display.flip()

    def show_start_screen(self):
        pygame.mixer.music.load(G_PATH_MBF + "Title Screen.wav")
        self.screen.fill((150, 150, 255))
        self.draw_text("Lil Brute (Legacy)", 100, WHITE, WIDTH / 2, 100)
        self.draw_text("Press P to play", 20, WHITE, WIDTH / 2, HEIGHT - 100)
        pygame.display.flip()
        pygame.mixer.music.play(-1)
        self.wait_for_key()
        pygame.mixer.music.fadeout(500)
    
    def show_end_screen(self):
        pygame.mixer.music.load(G_PATH_MBF + "Ending.wav")
        self.screen.fill((150, 150, 255))
        self.draw_text("Thanks for playing", 90, WHITE, WIDTH / 2, 100)
        self.draw_text("Press P to Exit", 20, WHITE, WIDTH / 2, HEIGHT - 100)
        pygame.display.flip()
        pygame.mixer.music.play(-1)
        self.wait_for_key()
        pygame.mixer.music.fadeout(500)

    def show_level_screen(self):
        self.screen.fill((150, 150, 255))
        if self.level == 1:
            self.screen.blit(self.image1, (0, 0))
            self.draw_text("The Adventure Begins", 25, BLACK, WIDTH / 2, 225)
        if self.level == 2:
            self.screen.blit(self.image2, (0, 0))
            self.draw_text("Traps and Snails", 25, BLACK, WIDTH / 2, 225)
        if self.level == 3:
            self.screen.blit(self.image3, (0, 0))
            self.draw_text("At the Docks", 25, BLACK, WIDTH / 2, 225)
        if self.level == 4:
            self.screen.blit(self.image4, (0, 0))
            self.draw_text("Doomed Vessel", 25, BLACK, WIDTH / 2, 225)
        if self.level == 5:
            self.screen.blit(self.image5, (0, 0))
            self.draw_text("Onto the Island", 25, BLACK, WIDTH / 2, 225)
        self.draw_text("Level " + str(self.level), 100, BLACK, WIDTH / 2, 100)
        self.draw_text("Press P to continue", 20, BLACK, WIDTH / 2, HEIGHT - 100)
        pygame.display.flip()
        self.wait_for_key()

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
                    if event.key == pygame.K_p:
                        waiting = False

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font("Fonts\Inkfree.ttf", size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


g = Game()
g.show_start_screen()
g.show_level_screen()
while g.running:
    if g.level == 1:
        g.level_1()
        g.show_level_screen()
    elif g.level == 2:
        g.level_2()
        g.show_level_screen()
    elif g.level == 3:
        g.level_3()
        g.show_level_screen()
    elif g.level == 4:
        g.level_4()
        g.show_level_screen()
    elif g.level == 5:
        g.level_5()
    else:
        g.show_end_screen()
        g.running = False
pygame.quit()
