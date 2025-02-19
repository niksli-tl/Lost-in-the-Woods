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
        self.x2 = self.rect.x + 200

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
        self.y2 = self.rect.y + 200

    def update(self):
        if self.direction:
            self.rect.y += self.step
            if self.rect.y == self.y2:
                self.direction = False
        else:
            self.rect.y -= self.step
            if self.rect.y == self.y1:
                self.direction = True


main_sprite = PlayerSprite('images/running_010.png', 100, 250, 10)
enemy_sprite1 = EnemyHSprite('images/fly1.png', 500, 450, 2, True)
enemy_sprite2 = EnemyVSprite('images/fly1.png', 1000, 300, 2, True)
game = True
# 0-game 1-lose 2-win 3-end
state = 0
while game:
    window.blit(background, (0, 0))
    main_sprite.reset()
    main_sprite.update()
    enemy_sprite1.reset()
    enemy_sprite1.update()
    enemy_sprite2.reset()
    enemy_sprite2.update()
    if state == 0:
        pass
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
