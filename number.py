from pygame import image
from pygame.sprite import Sprite

class Number(Sprite):
    """管理数字的类"""

    def __init__(self, game, pos: tuple, pixels = 128):
        """初始化数字并设置其初始位置"""
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.is_cued = False

        #加载数字并获取其外接矩形
        self.image = image.load('images/0_blue.bmp')
        self.rect = self.image.get_rect()

        #记录每个数字的相对位置和绝对位置
        self.row = pos[0]-1
        self.column = pos[1]-1
        self.rect.x = pos[1] * pixels
        self.rect.y = pos[0] * pixels

    #功能已被sprite类自带draw方法替代
    # def blitme(self):
    #     """在指定位置绘制数字"""
    #     self.screen.blit(self.image, self.rect)

    def update(self, game) -> None:
        if not self.is_cued:
            self.image = image.load(f'images/{game.canvas[self.row][self.column]}_green.bmp')

    def cueing(self, game):
        self.is_cued = True
        self.image = image.load(f'images/{game.canvas[self.row][self.column]}_green_reversed.bmp')
