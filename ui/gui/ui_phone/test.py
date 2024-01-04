class MineSweeper():
    
    ##
    #  status：游戏状态 0正常 1获胜 -1失败
    #  minemap：实际雷区图 0为无雷 1为有雷
    #  gamemap：游戏雷区图 0为不可见 1为可见 -1为已插旗
    #  hard：每个方块有多少概率是地雷
    ##



    def __init__(self, x=None, y=None, hard=None):
        self.status = 0  
        self.maxmines = 0
        self.flags = 0
        self.init_map(x, y)
        self.set_mine(hard)

    def init_map(self, x, y):  # default x = 10
        self.x = x
        self.y = y
        if not self.x:
            self.x = 10
        if not self.y:
            self.y = 20
        self.minemap = [[0 for _ in range(self.x)] for _ in range(self.y)]  # create matrix with x y
        self.gamemap = [[0 for _ in range(self.x)] for _ in range(self.y)]
        print('已创建大小为%s * %s 的雷区。'%(self.x,self.y))

    def set_mine(self, hard):
        import random
        self.hard = hard
        if not self.hard:
            self.hard = random.randint(10, 30)*0.01
        #  hard：每个方块有多少概率是地雷
        for i in range(self.x):
            for j in range(self.y):
                if self.hard >= random.random():
                    self.minemap[i][j] = 1
                    self.maxmines += 1
                    print('已在(%s, %s)放置地雷。'%(i,j))

    def is_lose(self, x, y):
        #  检查游戏失败
        if self.minemap[x][y] == 1:
            self.status = -1

    def get_around(self, x, y):
        if self.minemap[x][y] == 1:
            return -1  #  当此处为雷时

        mines = 0
        dire = [(-1,-1),(-1,1),(1,-1),(1,1),(-1,0),(0,-1),(1,0),(0,1)]
        for i in dire:
            _x = x + i[0]
            _y = y + i[1]
            if -1 < _x < self.x and -1 < _y < self.y:
                if self.minemap[_x][_y] == 1:
                    mines += 1
        return mines

    def set_flag(self, x, y):
        self.gamemap[x][y] = -1
        self.flags += 1

    def remove_flag(self, x, y):
        self.gamemap[x][y] = 0
        self.flags -= 1
    
    def check_win(self):
        win = False
        for i in range(self.x):
            for j in range(self.y):
                if self.minemap[i][j] == 1 and self.gamemap[i][j] == 0:
                    win = True
                elif self.minemap[i][j] == 0 and self.gamemap[i][j] == 1:
                    win = True
                else:
                    win = False
        if win:
            self.status == 1


    def touch(self, x, y):
        if self.gamemap[x][y] == 1:
            return  #  触碰空地时 后续增加触碰数字自动翻开
        if self.gamemap[x][y] == -1:
            self.remove_flag(x, y)
        self.gamemap[x][y] = 1
        print('翻开(%s, %s)。'%(x,y))
        self.is_lose(x, y)
        if self.status == -1:
            return

        if self.get_around(x,y)!=0:
            return
        dire = [(-1,0),(0,-1),(1,0),(0,1)]

        for i in dire:
            _x = x + i[0]
            _y = y + i[1]
            if -1 < _x < self.x and -1 < _y < self.y:
                #if self.get_around(_x,_y)==0:
                self.touch(_x,_y)
        
    def print_map(self):
        for i in range(self.x):
            for j in range(self.y):
                if self.gamemap[i][j]==0:
                    print('土',end='')
                elif self.minemap[i][j]==1:
                    print('雷',end='')
                else:
                    mines = self.get_around(i,j)
                    if mines:
                        print(mines,end='')
                    else:
                        print('空',end='')
            print()
    
    def print_minemap(self):
        for i in range(self.x):
            for j in range(self.y):
                if self.minemap[i][j]==1:
                    print('雷',end='')
                else:
                    print('空',end='')
            print()


if __name__ == '__main__':
    game = MineSweeper()
    game.print_minemap()
    print("游戏难度：%s"%game.hard)
    while game.status==0:
        game.print_map()
        print('输入挖开的位置。')
        inputs = input().split()
        game.touch(int(inputs[0]), int(inputs[1]))
        game.check_win()
    if game.status == 1:
        game.print_map()
        print('你赢了！')
    elif game.status == -1:
        game.print_map()
        print('你输了！')