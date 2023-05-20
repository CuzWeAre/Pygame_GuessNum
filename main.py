import sys, pygame
from random import randint
from settings import Settings
from number import Number
from game_stats import GameStats
from logic import Canvas
from myarray import Array
# from gametext import GameText
from congrats import Congrats
# import threading



class GameManager:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("刮刮乐")

        # self.number = Number(self)
        self.stats = GameStats(self)
        self.numbers = pygame.sprite.Group()
        self.arrays = pygame.sprite.Group()
        self.canvas = Canvas(self.settings.size)





    def run_game(self):
        """开始游戏的主循环"""
        self._creat_arrays()
        self._creat_numbers()

        self.numbers.sprites()[randint(1,self.settings.size**2)].cueing(self)

        self._update_screen()
        while True:
            self._check_events()

    def _check_events(self):
        """响应键盘和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
                mouse_pos = pygame.mouse.get_pos()
                print(mouse_pos)
                if self.stats.hints_left > 0:
                    self._check_number(mouse_pos)
                else:
                    self._check_array(mouse_pos)

    def _check_number(self,mouse_pos):
        """在玩家点击数字时切换数字"""
        for number in self.numbers:
            if number.rect.collidepoint(mouse_pos) and not number.is_cued:
                number.cueing(self)
                self._update_screen()
                self.stats.hints_left -= 1
                break

    def _check_array(self,mouse_pos):
        """在玩家点击箭头时执行操作"""
        for array in self.arrays:
            if array.rect.collidepoint(mouse_pos):
                self.numbers.update(self)
                self._update_screen()
                self.score = self.canvas.sum_direct(array.number)
                a = Congrats(self)
                self.screen = pygame.display.set_mode(
                    (self.settings.screen_width, self.settings.screen_height))
                self._update_screen()
                return 0
        print('No More Hints!')
    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕。"""
        self.screen.fill(self.settings.bg_color)
        # self.numbers.update()
        self.screen.blit(self.settings.user_picture, self.settings.user_picture_rect)
        self.numbers.draw(self.screen)
        self.arrays.draw(self.screen)
        self._creat_text()
        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def _creat_numbers(self):
        """创建全部数字"""
        numbers_pos_temp = [[(row, column) for column in range(1, self.settings.size+1)] for row in range(1, self.settings.size+1)]
        numbers_pos = []
        for i in numbers_pos_temp:
            numbers_pos += i
        for i in numbers_pos:
            number = Number(self, i)
            # self.stats.numbers += 1
            self.numbers.add(number)

    def _creat_arrays(self):
        """创建全部箭头"""
        for i in range(1,4):
            array = Array(self, (i, 0), 'Right Arrow', i)
            self.arrays.add(array)
        for i in range(4,7):
            array = Array(self, (0, i-3), 'Down Arrow', i)
            self.arrays.add(array)
        array = Array(self, (0, 0), 'Down-Right Arrow', 7)
        self.arrays.add(array)
        array = Array(self, (4, 0), 'Up-Right Arrow', 8)
        self.arrays.add(array)

    def _creat_text(self):
        """创建文本说明游戏规则及得分情况"""
        pass
        # self.screen = game.screen
        # self.font = pygame.font.SysFont("Microsoft YaHei", 30)  # 创建字体对象，设置字体和大小
        #
        # # 渲染游戏规则文本
        # rule_text = self.font.render('游戏规则：这里是游戏规则的内容', True, (0, 0, 0))
        # self.screen.blit(rule_text, (128, 512))  # 绘制到屏幕上，设置位置
        #
        # # 渲染得分文本
        # score_text = self.font.render('得分情况：这里是得分情况的内容', True, (0, 0, 0))
        # self.screen.blit(score_text, (10, 50))


if __name__ == '__main__':
    #创建游戏实例并运行游戏
    game = GameManager()
    game.run_game()