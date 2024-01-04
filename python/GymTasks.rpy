init python early:
    class NoSport(GymTask):
        id = 0
        name = _('未安排健身日程')
        kind = _('无难度')
        unlocked = True
        info = _('该时间段尚未安排健身日程。')

        @classmethod
        def checkAvailable(cls, player, day, time):
            return _('该时间段尚未安排健身日程。')

        @classmethod
        def executeTask(cls, player):
            pass


    class WarmUpSport(GymTask):
        id = 100
        name = _('准备运动')
        kind = _('无难度')
        unlocked = True
        info = _('基础恢复：5\n获得状态：准备运动。\n大幅提升运动专注度。\n\n不会受伤。')
        ad = _('“有备而无患。”')

        @classmethod
        def executeTask(cls, player):
            reco = r2(5 * cls.getRecoScale(player))
            player.gain_mental(reco)
            WarmupEffect.add(player)


    class TreadmillSport(GymTask):
        id = 101
        name = _('跑步机')
        kind = _('低难度')
        unlocked = True
        info = _('基础恢复：5.5\n有概率提升身体素质，获得2层酸痛和1层良好的运动。\n\n偶尔会在运动中受伤。')
        ad = _('墨丘利说：“黑夜是多么的美丽，令人昏昏欲睡，我给你讲个故事吧。”')


        @classmethod
        def executeTask(cls, player):
            reco = r2(5.5 * cls.getRecoScale(player))
            player.gain_mental(reco)
            g = ra(player, 0, 1) * 0.01
            player.gain_abi(g, 'phy')
            Soreness.add(player, 2)
            PhysRezB.add(player)
            cls.setInjured(player, 20)
            


    class SpinningSport(GymTask):
        id = 102
        name = _('动感单车')
        kind = _('低难度')
        unlocked = True
        info = _('基础恢复：4\n降低0~2点严重程度，获得2层酸痛。\n\n偶尔会在运动中受伤。')
        ad = _('“他是来自外太空的人，我们要带他去他的宇宙飞船。”')

        @classmethod
        def executeTask(cls, player):
            reco = r2(5.5 * cls.getRecoScale(player))
            player.gain_mental(reco)
            g = ra(player, 0, 2) * 0.01
            player.gain_abi(g, 'sev')
            Soreness.add(player, 2)
            cls.setInjured(player, 20)


    class DumbbellSport(GymTask):
        id = 103
        name = _('哑铃训练')
        kind = _('中难度')
        unlocked = False
        info = _('基础恢复：3\n获得1~2点身体素质，获得2~3层酸痛。\n\n有概率会在运动中受伤。\n\n解锁条件 1.3身体素质解锁。')
        ad = _('其实这枚哑铃的材质是木棍和棉花糖。')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return _('日程未解锁！')
            return True

        @classmethod
        def unlockCond(cls, player):
            if player.physical < 1.3:
                return _('基础身体素质尚未达到要求，需要至少等于1.3')
            return True


        @classmethod
        def executeTask(cls, player):
            reco = r2(3 * cls.getRecoScale(player))
            player.gain_mental(reco)
            if GymLimited.has(player):
                g = 0.01 * ra(player, 1, 2)
            else:
                g = 0.01 * ra(player, 1, 2) + player.physicalGain
                GymLimited.add(player)
            player.gain_abi(g, 'phy')
            Soreness.add(player, 2)
            cls.setInjured(player, 50)


    class QuickStretchSport(GymTask):
        id = 104
        name = _('快速拉伸')
        kind = _('中难度')
        unlocked = False
        info = _('将15层酸痛转化为2层体魄。\n\n有概率会在运动中受伤。\n\n解锁条件 1.3身体素质解锁。')
        ad = _('再多拉伸几次就可以口到自己了。')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return _('日程未解锁！')
            return True

        @classmethod
        def unlockCond(cls, player):
            if player.physical < 1.3:
                return _('基础身体素质尚未达到要求，需要至少等于1.3')
            return True


        @classmethod
        def executeTask(cls, player):
            if Soreness.getstack(player) >= 15:
                Soreness.subByType(player, 15)
                Physique.add(player, 2)
            cls.setInjured(player, 50)

    
    class ArmStrengthSport(GymTask):
        id = 105
        name = _('臂力训练')
        kind = _('高难度')
        unlocked = False
        info = _('基础恢复：3.5\n获得2~3点身体素质，获得3层酸痛，获得1层良好的运动。\n\n大概率会在运动中受伤。\n\n解锁条件 1.4身体素质解锁。')
        ad = _('“火麒麟犹如千斤热油的血喷洒到他的左臂上，就像要将他的手臂炸熟一样。”')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return _('日程未解锁！')
            return True

        @classmethod
        def unlockCond(cls, player):
            if player.physical < 1.4:
                return _('基础身体素质尚未达到要求，需要至少等于1.4')
            return True


        @classmethod
        def executeTask(cls, player):
            reco = r2(3.5 * cls.getRecoScale(player))
            player.gain_mental(reco)
            if GymLimited.has(player):
                g = 0.01 * ra(player, 2, 3)
            else:
                g = 0.01 * ra(player, 2, 3) + player.physicalGain
                GymLimited.add(player)
            player.gain_abi(g, 'phy')
            Soreness.add(player, 3)
            PhysRezB.add(player)
            cls.setInjured(player, 80)

    
    class SquattingSport(GymTask):
        id = 106
        name = _('深蹲训练')
        kind = _('高难度')
        unlocked = False
        info = _('基础恢复：3\n获得3~5层酸痛，获得1层良好的运动。\n\n大概率会在运动中受伤。\n\n解锁条件 1.4身体素质解锁。')
        ad = _('“痛苦总是折磨着那些停滞不前的人。”')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return _('日程未解锁！')
            return True

        @classmethod
        def unlockCond(cls, player):
            if player.physical < 1.4:
                return _('基础身体素质尚未达到要求，需要至少等于1.4')
            return True


        @classmethod
        def executeTask(cls, player):
            reco = r2(3 * cls.getRecoScale(player))
            player.gain_mental(reco)
            Soreness.add(player, ra(player, 3, 5))
            PhysRezB.add(player)
            cls.setInjured(player, 80)


    class AbdominalSport(GymTask):
        id = 107
        name = _('腹肌撕裂')
        kind = _('高难度')
        unlocked = False
        info = _('基础恢复：2.5\n获得1~2层体魄。\n\n大概率会在运动中受伤。\n\n解锁条件 1.5身体素质解锁。')
        ad = _('再卷腹一百次，我就能打过——奥特曼。')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return _('日程未解锁！')
            return True

        @classmethod
        def unlockCond(cls, player):
            if player.physical < 1.5:
                return _('基础身体素质尚未达到要求，需要至少等于1.5')
            return True


        @classmethod
        def executeTask(cls, player):
            reco = r2(3 * cls.getRecoScale(player))
            player.gain_mental(reco)
            Physique.add(player, rca(player, (1,1,1,2)))
            cls.setInjured(player, 120)


    class ExRelation(GymTask):
        id = 108
        name = _('超高速跑步机')
        kind = _('高难度')
        unlocked = False
        info = _('基础恢复：5\n降低2~4严重程度。\n\n大概率会在运动中受伤。\n\n解锁条件 1.6身体素质解锁。')
        ad = _('后面就是玻璃窗，跟不上速度的就会直接被这台跑步机甩出窗外。')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return _('日程未解锁！')
            return True

        @classmethod
        def unlockCond(cls, player):
            if player.physical < 1.6:
                return _('基础身体素质尚未达到要求，需要至少等于1.6')
            return True


        @classmethod
        def executeTask(cls, player):
            
            reco = r2(5 * cls.getRecoScale(player))
            player.gain_mental(reco)
            g = ra(player, 2, 4) * 0.01
            player.gain_abi(-g, 'sev')
            cls.setInjured(player, 120)
            

            