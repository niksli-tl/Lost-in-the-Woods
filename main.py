from random import randint

from pygame import time, display, transform, image, sprite, event, QUIT, key, K_UP, K_DOWN, K_LEFT, K_RIGHT

FPS = 60
clock = time.Clock()
window = display.set_mode((1600, 900))
display.set_caption("Lost in the Woods")
background = transform.scale(image.load("images/Cartoon_Forest_BG_02.png"), (1600, 900))


class GeneralSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_step):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (50, 50))
        self.step = player_step
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def collides_with(self, enemy):
        return self.rect.colliderect(enemy.rect)


class PlayerSprite(GeneralSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.step
        if keys_pressed[K_DOWN] and self.rect.y < 850:
            self.rect.y += self.step
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.step
        if keys_pressed[K_RIGHT] and self.rect.x < 1550:
            self.rect.x += self.step


class EnemyHSprite(GeneralSprite):
    def __init__(self, player_image, player_x, player_y, player_step, direction):
        super().__init__(player_image, player_x, player_y, player_step)
        self.direction = direction
        self.x1 = self.rect.x
        self.x2 = self.rect.x + 300

    def update(self):
        if self.direction:
            self.rect.x += self.step
            if self.rect.x == self.x2:
                self.direction = False
        else:
            self.rect.x -= self.step
            if self.rect.x == self.x1:
                self.direction = True


class EnemyVSprite(GeneralSprite):
    def __init__(self, player_image, player_x, player_y, player_step, direction):
        super().__init__(player_image, player_x, player_y, player_step)
        self.direction = direction
        self.y1 = self.rect.y
        self.y2 = self.rect.y + 300

    def update(self):
        if self.direction:
            self.rect.y += self.step
            if self.rect.y == self.y2:
                self.direction = False
        else:
            self.rect.y -= self.step
            if self.rect.y == self.y1:
                self.direction = True


class Wall(sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = transform.scale(image.load('images/wall_block.png'), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class WallH(Wall):
    def __init__(self,x,y):
        self.image = transform.scale(image.load('images/wall_h.png'), (200, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class WallV(Wall):
    def __init__(self,x,y):
        self.image = transform.scale(image.load('images/wall_v.png'), (50, 200))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


def generate_treasure(x, y):
    res = randint(1,4)
    if res == 1:
        return GeneralSprite('images/gem_red.png',x,y,0)
    elif res == 2:
        return GeneralSprite('images/gem_white.png',x,y,0)
    elif res == 3:
        return GeneralSprite('images/gem_blue.png',x,y,0)
    elif res == 4:
        return GeneralSprite('images/gem_green.png',x,y,0)


main_sprite = PlayerSprite('images/running_010.png', 100, 250, 5)
treasure = None
levels = []
walls = []
enemies = []

def load_level1():
    global treasure
    enemies.clear()
    walls.clear()
    treasure = generate_treasure(1450,800)
    enemies.append(EnemyHSprite('images/fly1.png', 300, 600, 2, True))
    enemies.append(EnemyVSprite('images/fly1.png', 600, 50, 2, True))
    enemies.append(EnemyHSprite('images/fly1.png', 1000, 450, 2, True))
    walls.append(WallV(150,0))
    walls.append(WallH(0,300))
    walls.append(WallH(300,200))
    walls.append(WallV(500,200))
    walls.append(WallV(300,250))
    walls.append(Wall(300,450))
    walls.append(WallH(300,500))
    walls.append(WallH(500,500))
    walls.append(WallV(700,350))
    walls.append(WallV(700,200))
    walls.append(WallH(750,200))
    walls.append(WallV(900,200))
    walls.append(WallH(900,350))
    walls.append(WallV(1050,0))
    walls.append(WallH(1200,150))
    walls.append(WallV(1200,200))
    walls.append(WallH(1200,350))
    walls.append(WallV(1350,400))
    walls.append(WallV(1350,550))
    walls.append(WallH(1400,700))
    walls.append(WallV(150,500))
    walls.append(WallH(150,700))
    walls.append(WallV(300,700))
    walls.append(WallH(500,700))
    walls.append(WallH(700, 700))
    walls.append(WallV(900, 550))
    walls.append(WallH(900, 550))
    walls.append(WallH(1000, 550))
    walls.append(WallV(1150, 550))
    walls.append(WallV(1150,700))
levels.append(load_level1)
game = True
current_level = 0
# 0-game 1-lose 2-win 3-end
state = 0
load_level1()
while game:
    window.blit(background, (0, 0))

    if state == 0:
        main_sprite.reset()
        main_sprite.update()
        treasure.reset()
        if main_sprite.collides_with(treasure):
            state = 2
        for wall in walls:
            wall.reset()
            if main_sprite.collides_with(wall):
                state = 1
        for enemy in enemies:
            enemy.update()
            enemy.reset()
            if enemy.collides_with(main_sprite):
                state = 1

    elif state == 1:
        pass
    elif state == 2:
        pass
    elif state == 3:
        pass
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
    display.update()
