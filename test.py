import pygame
from pygame.locals import *

# 创建自定义精灵类
class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()

    def update(self):
        super().update(self)
        self.rect.x += 1

# 初始化Pygame
pygame.init()

# 创建屏幕和精灵组
screen = pygame.display.set_mode((400, 400))
sprites = pygame.sprite.Group()

# 创建精灵对象并添加到精灵组
for i in range(screen.get_rect().height//50):
    sprite = MySprite()
    sprite.rect.y = sprite.rect.height + sprite.rect.height * (i-1)
    sprites.add(sprite)

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # 更新精灵
    sprites.update()

    # 绘制精灵和屏幕
    screen.fill((255, 255, 255))
    sprites.draw(screen)
    pygame.display.flip()

# 退出游戏
pygame.quit()
