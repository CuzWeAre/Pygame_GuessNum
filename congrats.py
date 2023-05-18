import pygame, sys
from pygame.locals import *


class Congrats():
    def __init__(self, score):
        # 游戏祝贺窗口
        self.screen = pygame.display.set_mode((500, 400))
        pygame.display.set_caption("恭喜！")

        self.font = pygame.font.SysFont("Microsoft YaHei", 25, bold = True)
        text = f"您一共获得了 {score} 分，手气斐然啊！"  # 替换为你的游戏规则文本
        text_render = self.font.render(text, True, (0, 0, 0))
        text_rect = text_render.get_rect()
        text_rect.y = 50
        text_rect.centerx = self.screen.get_rect().centerx


        # 设置屏幕颜色
        self.screen.fill((255, 255, 255))
        # 绘制祝贺图片
        self.image = pygame.image.load('images/congrats.bmp')
        image_rect = self.image.get_rect()
        image_rect.y = 90
        image_rect.centerx = self.screen.get_rect().centerx
        self.screen.blit(self.image, image_rect)
        # 绘制游戏规则文本
        self.screen.blit(text_render, text_rect)

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return


if __name__ == '__main__':
    pygame.init()
    a = Congrats(1)


