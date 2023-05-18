from random import choice
from os import system


class Canvas:
    def __init__(self, size=3):
        def randcanvas(size: int) -> list[list[int]]:
            """随机生成一个n*n的猜数二维矩阵"""
            init_canvas = [[0 for _ in range(size)] for _ in range(size)]
            lst = list(range(1, size ** 2 + 1))
            for row in range(size):
                for column in range(size):
                    num = choice(lst)
                    lst.remove(num)
                    init_canvas[row][column] = num
            return init_canvas

        self.size = size
        self.map = randcanvas(size)
        self.map_clue = [[0 for _ in range(size)] for _ in range(size)]

    def __getitem__(self, item):
        """类可以使用索引获取值"""
        return self.map[item]

    def __setitem__(self, key, value):
        """类可以使用索引修改值"""
        self.map[key] = value
        print(f'Set {key} to {value}')

    def show(self,n):
        perform = ''
        for i in eval('self.'+n):
            perform += ' '.join(map(str,i)) + '\n'
        # i = system('cls')
        print(perform)

    def __repr__(self):
        """被打印时返回的内容"""

        self.show('map')

    def __len__(self):
        """类可以进行切片操作"""
        return len(self.map)

    def cueing(self,y:int = None,x:int = None):
        """提示，坐标原点为左上，索引从零开始，先行再列，如果不传入坐标值则随机提示"""
        if x is None or y is None:
            pos_temp = [choice(range(self.size)), choice(range(self.size))]
        else:
            pos_temp = [y,x]
        self.map_clue[pos_temp[0]][pos_temp[1]] = self.map[pos_temp[0]][pos_temp[1]]
        # self.show('map_clue')

    def direct_sum(self, direct):
        """计算方向上数字的全部和"""
        ans = 0
        if direct < 4:
            direct -= 1
            ans = sum(self.map[direct])
        elif direct < 7:
            direct -= 1
            for i in range(3):
                ans += self.map[i][direct - 3]
        elif direct == 7:
            for i in range(3):
                ans += self.map[i][i]
        elif direct == 8:
            for i in range(-3, 0, 1):
                ans += self.map[i][-i - 1]
        return ans

if __name__ == '__main__':
    dic_award = {
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
    n = 3
    canvas = Canvas(n)
    canvas.cueing()
    canvas.show('map_clue')
    total = 0  #初始化得分

    print(f'幸运刮刮乐，敢赢你就来！\n分数对照表：{dic_award}')

    hints = int(input('你想看几个数字？\n'))
    for i in range(hints):  #range内为提示的数字个数
        row,column = [int(x)-1 for x in input('输入你想看到的数字叭，先行再列，空格分割，索引从1开始\n').split()]
        canvas.cueing(row,column)
        canvas.show('map_clue')

    direct = int(input(' 你想从哪个方向刮开彩票？\n1 至 3 表示选择横向的第一行、第二行、第三行，4 至 6 表示纵向的第一列、第二列、第三列，7、8分别表示左上到右下的主对角线和右上到左下的副对角线。\n'))
    ans = canvas.direct_sum(direct)

    canvas.show('map')
    print(f'你一共获得了{ans}点，奖励{dic_award[ans]}分！')
