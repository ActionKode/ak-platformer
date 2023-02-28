import pygame
from Settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, ground, all_sprites, swords, game):
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
        self.last_shoot = 0
        self.swords = swords
        self.all_sprites = all_sprites
        self.left = False
        self.right = True
        self.game = game

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
        if keystate[pygame.K_s] or keystate[pygame.K_DOWN]:
            if pygame.time.get_ticks() - self.last_shoot > 500:
                self.shoot()
                self.last_shoot = pygame.time.get_ticks()
        if (keystate[pygame.K_UP] or keystate[pygame.K_w]) and not self.jumped:
            self.jump()

        if self.rect.left < 7:
            self.rect.left = 7
        if self.rect.right > WIDTH - 7:
            self.rect.right = WIDTH - 7
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
        self.health -= 10
        self.image = pygame.image.load(G_PATH + "Player/player_stand_hurt.png").convert_alpha()
        self.jump()

    def shoot(self):
        global shots
        if self.right:
            sword = Sword(self.rect.centerx, self.rect.midleft, 10)
            self.all_sprites.add(sword)
            self.swords.add(sword)
        if self.left:
            sword = Sword(self.rect.centerx, self.rect.midleft, -10)
            self.all_sprites.add(sword)
            self.swords.add(sword)
        shots = True


class Sky(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(G_PATH + 'Sky.png').convert_alpha(), (WIDTH, HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = HEIGHT / 2

    def update(self):
        pass


class SkyAlt(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(G_PATH + 'Sky_two.png').convert_alpha(), (WIDTH, HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = HEIGHT / 2

    def update(self):
        pass


class SkyAlt_2(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(G_PATH + 'Sky_Three.png').convert_alpha(), (WIDTH, HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = HEIGHT / 2

    def update(self):
        pass


class SkyAlt_3(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(G_PATH + 'Sky_Four.png').convert_alpha(), (WIDTH, HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = HEIGHT / 2

    def update(self):
        pass


class Sword(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        self.move = False
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.rotate(pygame.image.load(G_PATH + 'Player/sword.png').convert_alpha(),
                                             -45)
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
                pygame.transform.rotate(pygame.image.load(G_PATH + 'Player/sword.png').convert_alpha(),
                                        -45), True, False)


class Ground(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(G_PATH + 'ground.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = HEIGHT - 100

    def update(self):
        pass


class GroundAlt(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(G_PATH + 'ground_two.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = HEIGHT - 100

    def update(self):
        pass


class GroundAlt_2(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(G_PATH + 'ground_three.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = HEIGHT - 100

    def update(self):
        pass


class GroundAlt_3(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(G_PATH + 'ground_four.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (WIDTH, 150))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = HEIGHT - 150
        self.dy = 0
        self.last_update = pygame.time.get_ticks()

    def update(self):
        self.rect.y += self.dy
        now = pygame.time.get_ticks()
        if now - self.last_update > 4000:
            self.dy = 1
            self.last_update = now


class WinningElement(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/Base pack/HUD/hud_gem_blue.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = HEIGHT / 2
        self.dy = 1

    def update(self):
        self.rect.y += self.dy
        if self.rect.y >= HEIGHT / 2 + 10:
            self.dy = -1
        if self.rect.y <= HEIGHT / 2 - 10:
            self.dy = 1


class Enemy(pygame.sprite.Sprite):
    def __init__(self, player, x, game):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(G_PATH + "snail/snail1.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.game = game
        self.rect.bottom = self.game.ground.rect.top
        self.dx = 0
        self.dy = 0
        self.player = player
        self.move = False
        self.last_update = 0

    def update(self):
        self.rect.bottom = self.game.ground.rect.top
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


class Boss(pygame.sprite.Sprite):
    def __init__(self, x, y, game, all_sprites):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/Boss_sprites/Ufo_1.png').convert_alpha()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = 200
        self.dx = -5
        self.dy = 0
        self.hurt = False
        self.health = 100
        self.hurt_timer = 100
        self.last_update = 0
        self.last_shoot = 0
        self.all_sprites = all_sprites
        self.left = True
        self.right = False
        self.game = game
        self.shooting = False
        self.shoot_time = 0

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.left <= 0:
            self.dx = 5
        if self.rect.right >= WIDTH:
            self.dx = -5
        now = pygame.time.get_ticks()
        if now - self.last_update > 2000:
            self.shoot_bomb()
            self.last_update = now

    def shoot_bomb(self):
        self.shooting = False
        if self.right:
            b = Bomb(self.rect.centerx, self.rect.centery, self.game.player, self.game)
            self.game.all_sprites.add(b)
            self.game.enemies.add(b)
        elif self.left:
            b = Bomb(self.rect.centerx, self.rect.centery, self.game.player, self.game)
            self.game.all_sprites.add(b)
            self.game.enemies.add(b)


class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y, target, game):
        pygame.sprite.Sprite.__init__(self)
        self.load_imgs()
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.dy = 2
        self.dx = 0
        self.game = game
        self.target = target
        self.last_update = 0

    def update(self):
        now = pygame.time.get_ticks()
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.centerx > self.target.rect.centerx:
            self.dx = -2
        if self.rect.centerx < self.target.rect.centerx:
            self.dx = 2
        if self.rect.left < 0 or self.rect.right > WIDTH or self.rect.bottom > self.game.ground.rect.top:
            self.kill()
        if now - self.last_update > 80 and self.dx < 0:
            if self.current_frame < (len(self.frames) - 1):
                self.current_frame += 1
                self.image = self.frames[self.current_frame]
                self.image.set_colorkey((0, 128, 128))
            else:
                self.current_frame = 0
                self.image = self.frames[self.current_frame]
                self.image.set_colorkey((0, 128, 128))
            self.last_update = now
        if now - self.last_update > 80 and self.dx > 0:
            if self.current_frame < (len(self.frames) - 1):
                self.current_frame += 1
                self.image = pygame.transform.flip(self.frames[self.current_frame], True, False)
                self.image.set_colorkey((0, 128, 128))
            else:
                self.current_frame = 0
                self.image = pygame.transform.flip(self.frames[self.current_frame], True, False)
                self.image.set_colorkey((0, 128, 128))
            self.last_update = now

    def load_imgs(self):
        self.h = 30
        self.w = 30
        self.frames = [pygame.transform.scale(pygame.image.load(G_PATH_boss + "Pirate_Bomb1.png"), (self.w, self.h)),
                       pygame.transform.scale(pygame.image.load(G_PATH_boss + "Pirate_Bomb2.png"), (self.w, self.h))]


class Button(pygame.sprite.Sprite):
    def __init__(self, x, game):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(G_PATH + "buttonRed.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = HEIGHT - 100
        self.state = "ready"
        self.game = game

    def update(self):
        if self.state == "ready":
            self.image = pygame.image.load(G_PATH + "buttonRed.png").convert_alpha()
        elif self.state == "pressed":
            self.image = pygame.image.load(G_PATH + "buttonRed_pressed.png").convert_alpha()
        hits = pygame.sprite.spritecollide(self.game.player, self.game.buttons, False)
        if hits:
            self.state = "pressed"
        else:
            self.image = pygame.image.load(G_PATH + "buttonRed.png").convert_alpha()


class Spike(pygame.sprite.Sprite):
    def __init__(self, x, game):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(G_PATH + 'spikes.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = HEIGHT - 100
        self.game = game

    def update(self):
        if self.game.button.state == "pressed":
            self.rect.y += 2


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, game):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(G_PATH + 'hud_coins.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (47, 47))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.origin = y
        self.game = game
        self.dy = 1

    def update(self):
        self.rect.y += self.dy
        if self.rect.y >= self.origin + 10:
            self.dy = -1
        if self.rect.y <= self.origin - 10:
            self.dy = 1
