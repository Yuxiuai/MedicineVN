init python early:
    class Stat:

        basenames = {
            'Task': (1,_("进行过的日程")),
            'Effect': (2,_("获得过的效果")),
            'Item': (3,_("使用过的道具")),
            'object': (99,_("其他")),
            'None': (100,"????")
        }

        stato = [
            'rec', 'con', 'worup', 'wordown', 'wriup', 'wridown', 'phyup', 'phydown', 'sevup', 'sevdown',
        ]
        
        @classmethod
        def write(cls, key, dic):# 将数据写入dic中
            if key in dic:
                dic[key] += 1
            else:
                dic[key] = 1

        @classmethod
        def getbase(cls, key):# 查找合适的base
            if key in (GymTask, CuredTask, DespairTask):
                return Task
            if key.__name__ in cls.basenames:
                return key
            return cls.getbase(key.__base__)

        @classmethod
        def record(cls, player, key):# 将数据分别写入独立数据，仅本局游戏的，被存档影响
            cls.write(key, player.LocalStatistics)
            cls.write(key, persistent.GlobalStatistics)

        @classmethod
        def get(cls, dic):
            
            items = list(dic.items())
            
            val = [list(filter(lambda x: cls.getbase(x[0]) == i, items)) for i in list(set([cls.getbase(i[0]) for i in items]))]
            for i in val:
                i.sort(key=lambda x: x[0].id)
                i.sort(key=lambda x: x[1], reverse=True)
            val.sort(key=lambda x: Stat.basenames[cls.getbase(x[0][0]).__name__][0])
            #items.sort(key=lambda x: x[1], reverse=True)
            return val
        
        @classmethod
        def clear(cls):# 将数据分别写入独立数据，仅本局游戏的，被存档影响
            persistent.GlobalStatistics = {} 
        
        @classmethod
        def stato_check(cls, player):
            if len(persistent.GlobalStatisticso) != len(Stat.stato) or len(player.LocalStatisticso) != len(Stat.stato):
                cls.stato_fix(player)


        @classmethod
        def stato_fix(cls, player):
            for key in Stat.stato:
                if key not in persistent.GlobalStatisticso:
                    persistent.GlobalStatisticso[key] = 0
                if key not in player.LocalStatisticso:
                    player.LocalStatisticso[key] = 0
    
        @classmethod
        def stato_record(cls, player, key, a):
            cls.stato_check(player)
            persistent.GlobalStatisticso[key] += a
            player.LocalStatisticso[key] += a
        