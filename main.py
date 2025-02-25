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

    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y


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
    def __init__(self, x, y):
        super().__init__()
        self.image = transform.scale(image.load('images/wall_block.png'), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class WallH(Wall):
    def __init__(self, x, y):
        self.image = transform.scale(image.load('images/wall_h.png'), (200, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class WallV(Wall):
    def __init__(self, x, y):
        self.image = transform.scale(image.load('images/wall_v.png'), (50, 200))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class MessageSprite(sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = []
        self.images.append(transform.scale(image.load('images/welcome_text.png'), (512, 512)))
        self.images.append(transform.scale(image.load('images/nextlv_text.png'), (512, 512)))
        self.images.append(transform.scale(image.load('images/win_end_text.png'), (512, 512)))
        self.active_image = 0
        self.rect = self.images[0].get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.images[self.active_image], (self.rect.x, self.rect.y))

    def set_active_image(self, index):
        self.active_image = index


def generate_treasure(x, y):
    res = randint(1, 4)
    if res == 1:
        return GeneralSprite('images/gem_red.png', x, y, 0)
    elif res == 2:
        return GeneralSprite('images/gem_white.png', x, y, 0)
    elif res == 3:
        return GeneralSprite('images/gem_blue.png', x, y, 0)
    elif res == 4:
        return GeneralSprite('images/gem_green.png', x, y, 0)


text = MessageSprite(544, 194)
main_sprite = PlayerSprite('images/running_010.png', 100, 250, 5)
treasure = None
levels = []
walls = []
enemies = []


def load_level1():
    global treasure
    enemies.clear()
    walls.clear()
    main_sprite.move(25, 25)
    treasure = generate_treasure(1450, 800)
    enemies.append(EnemyHSprite('images/fly1.png', 300, 600, 2, True))
    enemies.append(EnemyVSprite('images/fly1.png', 600, 50, 2, True))
    enemies.append(EnemyHSprite('images/fly1.png', 1000, 450, 2, True))
    walls.append(WallV(150, 0))
    walls.append(WallH(0, 300))
    walls.append(WallH(300, 200))
    walls.append(WallV(500, 200))
    walls.append(WallV(300, 250))
    walls.append(Wall(300, 450))
    walls.append(WallH(300, 500))
    walls.append(WallH(500, 500))
    walls.append(WallV(700, 350))
    walls.append(WallV(700, 200))
    walls.append(WallH(750, 200))
    walls.append(WallV(900, 200))
    walls.append(WallH(900, 350))
    walls.append(WallV(1050, 0))
    walls.append(WallH(1200, 150))
    walls.append(WallV(1200, 200))
    walls.append(WallH(1200, 350))
    walls.append(WallV(1350, 400))
    walls.append(WallV(1350, 550))
    walls.append(WallH(1400, 700))
    walls.append(WallV(150, 500))
    walls.append(WallH(150, 700))
    walls.append(WallV(300, 700))
    walls.append(WallH(500, 700))
    walls.append(WallH(700, 700))
    walls.append(WallV(900, 550))
    walls.append(WallH(900, 550))
    walls.append(WallH(1000, 550))
    walls.append(WallV(1150, 550))
    walls.append(WallV(1150, 700))


def load_level2():
    global treasure
    enemies.clear()
    walls.clear()
    main_sprite.move(25, 25)
    treasure = generate_treasure(1450, 800)
    enemies.append(EnemyHSprite('images/fly1.png', 300, 600, 2, True))
    enemies.append(EnemyVSprite('images/fly1.png', 1250, 550, 2, True))
    enemies.append(EnemyHSprite('images/fly1.png', 725, 50, 2, True))
    walls.append(WallV(150, 0))
    walls.append(WallV(150,100))
    walls.append(WallH(150, 300))
    walls.append(WallH(350, 300))
    walls.append(WallV(400, 0))
    walls.append(WallH(400,150))
    walls.append(WallH(550, 150))
    walls.append(Wall(750,150))
    walls.append(WallH(200, 475))
    walls.append(WallH(600, 475))
    walls.append(WallV(750, 325))
    walls.append(WallV(750, 200))
    walls.append(WallV(1000, 150))
    walls.append(WallV(1000, 350))
    walls.append(WallH(1200, 150))
    walls.append(WallV(1200, 200))
    walls.append(WallH(1400, 150))
    walls.append(WallV(1350, 400))
    walls.append(WallH(1350, 725))
    walls.append(Wall(1550,725))
    walls.append(WallV(150, 475))
    walls.append(Wall(150,650))
    walls.append(WallH(150, 700))
    walls.append(WallV(300, 700))
    walls.append(WallH(500, 700))
    walls.append(WallH(700, 700))
    walls.append(WallV(900, 550))
    walls.append(WallH(900, 550))
    walls.append(WallH(1100,550))
    walls.append(Wall(1300,550))
    walls.append(WallH(1000, 550))
    walls.append(Wall(1150, 550))
    walls.append(WallV(1150, 750))


levels.append(load_level1)
levels.append(load_level2)
game = True
state_timer = 0
current_level = 0
# 0-game 1-lose 2-win 3-end
state = 2
while game:
    window.blit(background, (0, 0))

    if state == 0:
        main_sprite.reset()
        main_sprite.update()
        treasure.reset()
        if main_sprite.collides_with(treasure):
            state = 2
            state_timer = 0
            current_level += 1
        for wall in walls:
            wall.reset()
            if main_sprite.collides_with(wall):
                state = 1
                state_timer = 0
        for enemy in enemies:
            enemy.update()
            enemy.reset()
            if enemy.collides_with(main_sprite):
                state = 1
                state_timer = 0

    elif state == 1:
        pass
    elif state == 2:
        if state_timer == 0:
            if current_level == 0:
                text.set_active_image(0)
            else:
                text.set_active_image(1)
        elif state_timer == 60:
            state_timer = 0
            if current_level == len(levels):
                state = 3
            else:
                levels[current_level]()
                state = 0
        state_timer += 1
        text.reset()
    elif state == 3:
        pass
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
    display.update()
