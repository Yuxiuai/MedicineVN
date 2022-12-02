init python early:
    class NoSport(GymTask):
        id = 0
        name = '未安排健身日程'
        kind = '无难度'
        unlocked = True
        info = '该时间段尚未安排健身日程。'

        @classmethod
        def checkAvailable(cls, player, day, time):
            return '该时间段尚未安排健身日程。'

        @classmethod
        def executeTask(cls, player):
            pass


    class WarmUpSport(GymTask):
        id = 100
        name = '准备运动'
        kind = '无难度'
        unlocked = True
        info = '基础恢复：5\n获得状态：准备运动。\n大幅提升运动专注度。\n\n不会受伤。'
        ad = '“有备而无患。”'

        @classmethod
        def executeTask(cls, player):
            reco = r2(5 * cls.getRecoScale(player))
            player.mental += reco
            Notice.add('恢复了%s点精神状态。' % reco)
            WarmupEffect.add(player)


    class TreadmillSport(GymTask):
        id = 101
        name = '跑步机'
        kind = '低难度'
        unlocked = True
        info = '基础恢复：5.5\n有概率提升身体素质，获得2层酸痛和1层良好的运动。\n\n偶尔会在运动中受伤。'
        ad = '墨丘利说：“黑夜是多么的美丽，令人昏昏欲睡，我给你讲个故事吧。”'


        @classmethod
        def executeTask(cls, player):
            reco = r2(5.5 * cls.getRecoScale(player))
            player.mental += reco
            g = ra(player, 0, 1) * 0.01
            player.physical += g
            Notice.add('恢复了%s点精神状态。' % reco)
            if g>0:
                Notice.add('升高了%s点身体素质。' % int(g * 100))
            Soreness.add(player, 2)
            PhysRezB.add(player)
            cls.setInjured(player, 20)
            


    class SpinningSport(GymTask):
        id = 102
        name = '动感单车'
        kind = '低难度'
        unlocked = True
        info = '基础恢复：4\n降低0~2点严重程度，获得2层酸痛。\n\n偶尔会在运动中受伤。'
        ad = '“他是来自外太空的人，我们要带他去他的宇宙飞船。”'

        @classmethod
        def executeTask(cls, player):
            reco = r2(5.5 * cls.getRecoScale(player))
            player.mental += reco
            g = ra(player, 0, 2) * 0.01
            player.severity -= g
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('降低了%s点严重程度。' % int(g * 100))
            Soreness.add(player, 2)
            cls.setInjured(player, 20)


    class DumbbellSport(GymTask):
        id = 103
        name = '哑铃训练'
        kind = '中难度'
        unlocked = False
        info = '基础恢复：3\n获得1点身体素质，获得2层酸痛。\n\n有概率会在运动中受伤。\n\n解锁条件 1.3身体素质解锁。'
        ad = '其实这枚哑铃的材质是木棍和棉花糖。'

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return '日程未解锁！'
            return True

        @classmethod
        def unlockCond(cls, player):
            if player.physical < 1.3:
                return '基础身体素质尚未达到要求，需要至少等于1.3'
            return True


        @classmethod
        def executeTask(cls, player):
            reco = r2(3 * cls.getRecoScale(player))
            player.mental += reco
            g = 0.01 + player.physicalGain
            player.physical += g
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('升高了%s点身体素质。' % int(g * 100))
            Soreness.add(player, 2)
            cls.setInjured(player, 50)


    class QuickStretchSport(GymTask):
        id = 104
        name = '快速拉伸'
        kind = '中难度'
        unlocked = False
        info = '将15层酸痛转化为2层体魄。\n\n有概率会在运动中受伤。\n\n解锁条件 1.3身体素质解锁。'
        ad = '再多拉伸几次就可以口到自己了。'

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return '日程未解锁！'
            return True

        @classmethod
        def unlockCond(cls, player):
            if player.physical < 1.3:
                return '基础身体素质尚未达到要求，需要至少等于1.3'
            return True


        @classmethod
        def executeTask(cls, player):
            if Soreness.has(player):
                if Soreness.get(player).stacks >= 15:
                    Soreness.subByType(player, 15)
                    Physique.add(player, 2)
            cls.setInjured(player, 50)

    
    class ArmStrengthSport(GymTask):
        id = 105
        name = '臂力训练'
        kind = '高难度'
        unlocked = False
        info = '基础恢复：3.5\n获得2~3点身体素质，获得3层酸痛，获得1层良好的运动。\n\n大概率会在运动中受伤。\n\n解锁条件 1.4身体素质解锁。'
        ad = '“火麒麟犹如千斤热油的血喷洒到他的左臂上，就像要将他的手臂炸熟一样。”'

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return '日程未解锁！'
            return True

        @classmethod
        def unlockCond(cls, player):
            if player.physical < 1.4:
                return '基础身体素质尚未达到要求，需要至少等于1.4'
            return True


        @classmethod
        def executeTask(cls, player):
            reco = r2(3.5 * cls.getRecoScale(player))
            player.mental += reco
            g = ra(player, 2, 3) * 0.01 + player.physicalGain
            player.physical += g
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('升高了%s点身体素质。' % int(g * 100))
            Soreness.add(player, 3)
            PhysRezB.add(player)
            cls.setInjured(player, 80)

    
    class SquattingSport(GymTask):
        id = 106
        name = '深蹲训练'
        kind = '高难度'
        unlocked = False
        info = '基础恢复：3\n获得4层酸痛，获得1层良好的运动。\n\n大概率会在运动中受伤。\n\n解锁条件 1.4身体素质解锁。'
        ad = '“世间泰坦仅允我喘息，深陷其足下泥泞。”'

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return '日程未解锁！'
            return True

        @classmethod
        def unlockCond(cls, player):
            if player.physical < 1.4:
                return '基础身体素质尚未达到要求，需要至少等于1.4'
            return True


        @classmethod
        def executeTask(cls, player):
            reco = r2(3 * cls.getRecoScale(player))
            player.mental += reco
            Notice.add('恢复了%s点精神状态。' % reco)
            Soreness.add(player, 4)
            PhysRezB.add(player)
            cls.setInjured(player, 80)


    class AbdominalSport(GymTask):
        id = 107
        name = '腹肌撕裂'
        kind = '高难度'
        unlocked = False
        info = '基础恢复：2.5\n获得1层体魄，获得3层酸痛，获得1层良好的运动。\n\n大概率会在运动中受伤。\n\n解锁条件 1.5身体素质解锁。'
        ad = '再卷腹一百次，我就能打过——奥特曼。'

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return '日程未解锁！'
            return True

        @classmethod
        def unlockCond(cls, player):
            if player.physical < 1.5:
                return '基础身体素质尚未达到要求，需要至少等于1.5'
            return True


        @classmethod
        def executeTask(cls, player):
            reco = r2(3 * cls.getRecoScale(player))
            player.mental += reco
            Notice.add('恢复了%s点精神状态。' % reco)
            Physique.add(player)
            Soreness.add(player, 6)
            PhysRezB.add(player)
            cls.setInjured(player, 80)


    class ExRelation(GymTask):
        id = 108
        name = '超高速跑步机'
        kind = '高难度'
        unlocked = False
        info = '基础恢复：5\n降低2~4严重程度，获得1层体魄。\n\n大概率会在运动中受伤。\n\n解锁条件 1.6身体素质解锁。'
        ad = '后面就是玻璃窗，跟不上速度的就会直接被这台跑步机甩出窗外。'

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return '日程未解锁！'
            return True

        @classmethod
        def unlockCond(cls, player):
            if player.physical < 1.6:
                return '基础身体素质尚未达到要求，需要至少等于1.6'
            return True


        @classmethod
        def executeTask(cls, player):
            
            reco = r2(5 * cls.getRecoScale(player))
            player.mental += reco
            g = ra(player, 2, 4) * 0.01
            player.severity -= g
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('降低了%s点严重程度。' % int(g * 100))
            Physique.add(player)
            cls.setInjured(player, 90)
            

            