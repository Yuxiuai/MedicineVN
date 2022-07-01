init python early:
    class GymTask:
        id = None
        name = None
        kind = '无难度'
        unlocked = True
        info = None
        ad = None

        @classmethod
        def unlockClass(cls, player):
            if not cls.unlocked:
                if cls.unlockCond(player) == True:
                    cls.unlocked = True
                    showNotice(['已解锁日程：%s！' % cls.name])
                else:
                    showNotice(['未达到日程%s的解锁条件：\n%s' % (cls.name, cls.unlockCond(player))])

        @classmethod
        def unlockCond(cls, player):
            return True

        @classmethod
        def defaultClass(cls):
            cls.unlocked = True

        @classmethod
        def getConsScale(cls, player):
            scale = 1.0
            scale *= player.basicConsumption
            scale *= player.phyCons()
            scale *= player.sev()
            scale = max(0.2, scale)
            return scale

        @classmethod
        def getConcScale(cls, player):
            scale = 0
            scale += player.basicConcentration/2
            scale += player.sportConcentration
            scale += 15 * player.phy() - 20
            scale /= player.sev()
            scale = max(0.2, scale)
            return scale

        @classmethod
        def getRecoScale(cls, player):
            scale = 1.0
            scale *= player.basicRecovery
            scale *= player.phyReco()
            scale *= player.sportRecovery
            scale /= player.sev()
            scale = max(0.2, scale)
            return scale

        @classmethod
        def setInjured(cls, player, per=20):
            perf = ra(player, 1, 100) + cls.getConcScale(player)
            if perf < per:
                Injured.add(player)
                Notice.add('你在运动中受伤了。')



        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.unlocked:
                return '日程未解锁！'
            return True

        @classmethod
        def executeTask(cls, player):
            for i in player.gymplan:
                if Injured.has(player):
                    renpy.jump("gym_injured")
                else:
                    i.executeTask(player)
            Notice.show()
            renpy.jump("gym_result")