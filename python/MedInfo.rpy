init python early:

    class MedInfo:
        def __init__(self, med):
            self.med = med
            self.res = 0
            self.lastuse = -5

        def afterSleepAction(self, player):

            if rra(player, self.updateResistenceChance(player)):
                self.res = max(self.res - 1, 0)

            self.lastuse = max(-5, self.lastuse - 5)

            if player.week == 0 or Despair.has(player) or player.cured > -1:
                return

            if rra(player, self.giveDependenceChance(player)):
                self.med.d_.add(player)

            

        def punish(self):
            punish = 1.0
            if self.lastuse > 0:
                punish = 0.5
            elif self.lastuse == -5:
                punish = 1.5
            return punish
        
        def time(self):
            d = {
                -5:'近期未使用',

                -4:'昨天早上',
                -3:'昨天上午',
                -2:'昨天下午',
                -1:'昨天晚上',
                
                1:'今天早上',
                2:'今天上午',
                3:'今天下午',
                4:'今天晚上',
                
            }
            return d[self.lastuse]

        
        def kind(self, player):
            return len(player.medinfo)-1

        def updateResistenceChance(self, player):
            return 60 * self.punish() * (1 + self.kind(player)*0.5) - player.week * 6
        
        def giveDependenceChance(self, player):
            return (10 * player.week) * self.punish() ** 3 * (100 - self.res) * 0.01 * 0.5 / (1 + self.kind(player))
            

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




        

