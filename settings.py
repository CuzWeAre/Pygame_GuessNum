class Settings:
    """游戏设置"""
    def __init__(self):
        """初始化游戏设置"""
        self.screen_width = 640
        self.screen_height = 640
        self.bg_color = (230, 230, 230)
        self.hints_limit = 2   #提示次数
        self.size = 3

        self.dic_award = {
        6: 10000,
        16: 72,
        7: 36,
        17: 180,
        8: 720,
        18: 119,
        9: 360,
        19: 36,
        10: 80,
        20: 306,
        11: 252,
        21: 1080,
        12: 108,
        22: 144,
        13: 72,
        23: 1800,
        14: 54,
        24: 3600,
        15: 180,
    }
