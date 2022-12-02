init python early:

    class MedInfo:
        def __init__(self, med):
            self.med = med
            self.res = 0
            self.lastuse = -4

        def afterSleepAction(self, player):
            punish = 1.0
            if self.lastuse > 0:
                punish = 0.75
            else:
                punish = 2
                self.res = max(self.res - 1, 0)
            self.lastuse = -4
            kinds = len(player.medinfo)
            if rra(player, 50 * punish * kinds - player.week * 6):
                self.res = max(self.res - 1, 0)
                
            
        def getFormatOperableTime(self, player):  # 起床时：0->1，早上规划日程时：2->2，午休时：6->3，睡觉前：10->4
            dictTakeMedTime = {0: 1, 2: 2, 6: 3, 10: 4,
                            101: 1, 102: 2, 103: 3, 104: 4}
            if player.times not in dictTakeMedTime:
                if player.times < 2:
                    return dictTakeMedTime[0]
                if player.times < 6:
                    return dictTakeMedTime[2]
                if player.times < 10:
                    return dictTakeMedTime[6]
                if player.times >= 10:
                    return dictTakeMedTime[10]
            else:
                return dictTakeMedTime[player.times]

        def getInterval(self, player):
            return self.getFormatOperableTime(player) - self.lastuse

        def updateTime(self, player):
            self.lastuse = self.getFormatOperableTime(player)




        

