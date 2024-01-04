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
            renpy.jump("GymTask_execute1")




label GymTask_execute1:
    $temp = p.gymplan[0]
    if not temp == NoSport:
        $Stat.record(p, temp)
        "准备进行[temp.name]……"
        call Task_processing from _call_Task_processing_39
        $temp.executeTask(p)
        if Injured.has(p):
            $p.updateAfterTask(temp)
            $Notice.show()
            jump gym_injured
        else:
            $Notice.show()
            $temp = rd(1,5)
            if temp == 1:
                "呼，算是比较成功地做完了……"
            elif temp == 2:
                "幸好没受伤……看来我得稍微小心点。"
            elif temp == 3:
                "刚才坐在旁边的狼兽人穿着白袜哦，不会是男同吧……"
            elif temp == 4:
                "好想喝可乐啊……会不会一口下去，今天的锻炼成果就直接白费了……"
            else:
                "好累啊……好想休息……"

    jump GymTask_execute2

label GymTask_execute2:
    $temp = p.gymplan[1]
    if not temp == NoSport:
        $Stat.record(p, temp)
        "准备进行[temp.name]……"
        call Task_processing from _call_Task_processing_40
        $temp.executeTask(p)
        if Injured.has(p):
            $p.updateAfterTask(temp)
            $Notice.show()
            jump gym_injured
        else:
            $Notice.show()
            $temp = rd(1,5)
            if temp == 1:
                "呼，算是比较成功地做完了……"
            elif temp == 2:
                "幸好没受伤……看来我得稍微小心点。"
            elif temp == 3:
                "刚才坐在旁边的狼兽人穿着白袜哦，不会是男同吧……"
            elif temp == 4:
                "好想喝可乐啊……会不会一口下去，今天的锻炼成果就直接白费了……"
            else:
                "好累啊……好想休息……"

    jump GymTask_execute3

label GymTask_execute3:
    $temp = p.gymplan[2]
    if not temp == NoSport:
        $Stat.record(p, temp)
        "准备进行[temp.name]……"
        call Task_processing from _call_Task_processing_41
        $temp.executeTask(p)
        if Injured.has(p):
            $p.updateAfterTask(temp)
            $Notice.show()
            jump gym_injured
        else:
            $Notice.show()
            $temp = rd(1,5)
            if temp == 1:
                "呼，算是比较成功地做完了……"
            elif temp == 2:
                "幸好没受伤……看来我得稍微小心点。"
            elif temp == 3:
                "刚才坐在旁边的狼兽人穿着白袜哦，不会是男同吧……"
            elif temp == 4:
                "好想喝可乐啊……会不会一口下去，今天的锻炼成果就直接白费了……"
            else:
                "好累啊……好想休息……"

    jump gym_result