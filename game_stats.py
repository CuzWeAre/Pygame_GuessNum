class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self,game):
        """初始化统计信息"""
        self.settings = game.settings
        self.reset_stats()

    def reset_stats(self):
        """初始化游戏运行期间可能变化的统计信息"""
        self.hints_left = self.settings.hints_limit
        self.numbers = 0