init python early:
    class GymTask:
        id = None
        name = None
        kind = _('无难度')
        unlocked = True
        info = None
        ad = None

        @classmethod
        def unlockClass(cls, player):
            if not cls.isUnlocked(player):
                if cls.unlockCond(player) == True:
                    player.unlockedTasks.add(cls)
                    showNotice([_('已解锁日程：%s！') % cls.name])
                else:
                    showNotice([_('未达到日程%s的解锁条件：\n%s') % (cls.name, cls.unlockCond(player))])
            else:
                showNotice([_('该日程：%s已解锁！') % cls.name])

        @classmethod
        def isUnlocked(cls, player):
            if cls in player.unlockedTasks:
                return True
            return cls.unlocked

        @classmethod
        def unlockCond(cls, player):
            return True

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
            scale += player.basicConcentration / 3
            scale += player.sportConcentration
            scale += 15 * player.phy() - 20
            scale /= player.sev()
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
                Notice.add(_('你在运动中受伤了。'))



        @classmethod
        def checkAvailable(cls, player, day, time):
            return cls.isUnlocked(player)

        @classmethod
        def executeTask(cls, player):
            if not GymTicket.has(player):
                player.money -= r2(0.4*player.price)
                GymTicket.add(player)
                Notice.show()
            for i in range(len(player.gymplan)):
                if player.gymplan[i] == NoSport:
                    continue
                Stat.record(p,player.gymplan[i])
                renpy.say(None, _("准备进行%s……")%player.gymplan[i].name)
                renpy.show_screen(_screen_name="Task_processing_screen",player=p)
                renpy.say(None, _("{cps=3}。。。。。。"))
                player.gymplan[i].executeTask(player)
                if Injured.has(player):
                    player.updateAfterTask(cls)
                    Notice.show()
                    renpy.jump("gym_injured")
                else:
                    Notice.show()
                    temp = rd(1,4)
                    if temp == 1:
                        renpy.say(None, _("呼，算是比较成功地做完了……"))
                    elif temp == 2:
                        renpy.say(None, _("幸好没受伤……看来我得稍微小心点。"))
                    elif temp == 3:
                        renpy.say(None, _("刚才坐在旁边的狼兽人穿着白袜哦，不会是男同吧……"))
                    else:
                        renpy.say(None, _("好累啊……好想休息……"))
            GymSport.executeTask(player)
            Notice.show()
            renpy.jump("gym_result")