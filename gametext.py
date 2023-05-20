import pygame


class GameText:

    def __init__(self, game):
        self.screen = game.screen
        self.font = pygame.font.SysFont("Microsoft YaHei", 30)  # 创建字体对象，设置字体和大小

        # 渲染游戏规则文本
        rule_text = self.font.render('游戏规则：这里是游戏规则的内容', True, (0, 0, 0))
        self.screen.blit(rule_text, (128, 512))  # 绘制到屏幕上，设置位置

        # 渲染得分文本
        score_text = self.font.render('得分情况：这里是得分情况的内容', True, (0, 0, 0))
        self.screen.blit(score_text, (10, 50))  # 绘制到屏幕上，设置位置
