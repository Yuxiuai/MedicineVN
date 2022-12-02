init python early:
    class Stat:

        basenames = {
            'Task': (1,"{size=-5}进行过的日程{/size}"),
            'Effect': (2,"{size=-5}获得过的效果{/size}"),
            'Item': (3,"{size=-5}使用过的道具{/size}"),
            'object': (99,"{size=-5}其他{/size}"),
            'None': (100,"{size=-5}????{/size}")
        }
        
        @classmethod
        def write(cls, key, dic):# 将数据写入dic中
            if key in dic:
                dic[key] += 1
            else:
                dic[key] = 1

        @classmethod
        def getbase(cls, key):# 查找合适的base
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