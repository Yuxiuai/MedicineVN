init python:
    class Workgame_Log:
        def __init__(self, pos, time=0.0):
            self.pos = pos  # 位置
            self.time = time  # 变换等待时间

        def info(self):
            pass

    class Workgame_Waiting(Workgame_Log):
        def __init__(self, pos, time=0.0):
            super(type(self), self).__init__(pos, time)

        def info(self):
            print('【%.2fs时】等待中。' % self.time)

    class Workgame_Dissovle(Workgame_Log):
        def __init__(self, pos, time=0.0):
            super(type(self), self).__init__(pos, time)

        def info(self):
            print('【%.2fs时】方块%s溶解了。' % (self.time, (self.pos+1)))

    class Workgame_Leftmove(Workgame_Log):
        def __init__(self, pos, move, time=0.0):
            super(type(self), self).__init__(pos, time)
            self.move = move

        def info(self):
            print('【%.2fs时】方块%s左移%s格。' % (self.time, (self.pos+1), self.move))

    class Workgame_End(Workgame_Log):
        def __init__(self, pos, time=0.0):
            super(type(self), self).__init__(pos, time)

        def info(self):
            print('【%.2fs时】等待玩家操作。' % (self.time))

    class Workgame_Cleared(Workgame_Log):
        def __init__(self, pos, value, time=0.0):
            super(type(self), self).__init__(pos, time)
            self.value = value

        def info(self):
            print('【%.2fs时】消耗方块%s个。' % (self.time, self.value))

    class Workgame_Score(Workgame_Log):
        def __init__(self, pos, value, chain, time=0.0):
            super(type(self), self).__init__(pos, time)
            self.value = value
            self.chain = chain

        def info(self):
            print('【%.2fs时】上一次行动共消耗方块%s个，连锁%s次。' % (self.time, self.value, self.chain))

    class Workgame_Win(Workgame_Log):
        def __init__(self, pos, value, time=0.0):
            super(type(self), self).__init__(pos, time)
            self.value = value

        def info(self):
            print('【0.00s时】游戏结束，共消耗步数%s。' % (self.value))

    class Workgame_Start(Workgame_Log):
        def __init__(self, pos, time=0.0):
            super(type(self), self).__init__(pos, time)

        def info(self):
            print('【0.00s时】游戏开始。')