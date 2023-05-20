from pygame import image
from pygame.sprite import Sprite


class Array(Sprite):
    """管理箭头的类"""

    def __init__(self, game, pos: tuple, array_type: str, number: int, pixels=128):
        """初始化箭头并设置其初始位置，pos接受绝对位置"""
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.number = number

        # 加载图像并获取其外接矩形
        self.image = image.load(f'images/{array_type}.bmp')
        self.rect = self.image.get_rect()

        # 记录每个箭头的相对位置和绝对位置
        self.row, self.column = pos
        self.rect.x = self.column * pixels
        self.rect.y = self.row * pixels
    # def update(self):
    #     """更新箭头对象，模拟点击反馈"""
    #     self.screen.blit(self.image, self.rect)
