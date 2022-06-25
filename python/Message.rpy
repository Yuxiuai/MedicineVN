init python:

    ret_mes = { # 空字符串代表只会已读
        'Pathos': ['', '', '', '别叫'],
        'Acolas': ['','嗯？', '什么意思？', '我不习惯用某信，有什么重要的事打电话和我说吧？'],
        'Halluke': ['','？', '……', '什么？'],
        'Depline': ['','……']
    }

    class Message:

        def __init__(self, what, mon, day, fro, to, h, m, seen=False):
            self.what = what
            self.mon = mon
            self.day = day
            self.fro = fro
            self.to = to
            self.h = h
            self.m = m
            self.seen = seen

        @classmethod
        def new(cls, player, fro, to, what, h=None, m=None, seen=False):
            if what!='':
                if to == 'Halluke' and player.hal_p == 11 and seen==False:
                    seen = None
                    renpy.music.stop()
                if to == 'Halluke' and player.hal_p == 99:
                    seen = None
                if h == None:
                    h = player.st()[0]
                if m == None:
                    m = player.st()[1]
                mes = cls(what, player.mon, player.day, fro, to, h, m, seen)
                player.messages[to].append(mes)

        def info(self):
            if self.seen == True:
                seeninfo = '已读'
            elif self.seen == False:
                seeninfo = '未读'
            else:
                seeninfo = '{color=#ff0000}发送失败{/color}'

            return '%s月%s日 %s:%s %s' % (self.mon, self.day, self.h, self.m, seeninfo)

        @classmethod
        def clear(cls, to):
            player.messages[to] = []

        @classmethod
        def see(cls, player, fro ,to):
            for i in player.messages[to]:
                if i.seen == False and i.fro == fro:
                    i.seen = True

        @classmethod
        def hasNew(cls, player, to): # 是否单个人有新消息
            return False in [i.seen for i in list(filter(lambda x: x.fro != player.name, player.messages[to]))]
        
        @classmethod
        def hasNewMes(cls, player): # 是否所有人有新消息
            return True in [Message.hasNew(player, i) for i in player.messages]

        @classmethod
        def allret(cls, player):
            for i in player.messages:
                if False in [mes.seen for mes in list(filter(lambda x: x.fro == player.name, player.messages[i]))]:
                    Message.ret(player, i)

        @classmethod
        def ret(cls, player, who):
            Message.see(player, player.name, who)
            Message.new(player, who, who, rca(player, ret_mes[who]))
