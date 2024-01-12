init python early:

    class Task:
        id = None
        name = None
        kind = None
        unlocked = True
        info = None
        ad = None
        
        @classmethod
        def hasplot(cls, player):
            return False
        
        @classmethod
        def unlock(cls, player):
            player.unlockedTasks.add(cls)
            if cls in player.lockedTasks:
                player.lockedTasks.remove(cls)
            showNotice([_('已解锁新日程：%s！') % cls.name])
        
        @classmethod
        def lock(cls, player):
            player.lockedTasks.add(cls)
            if cls in player.unlockedTasks:
                player.unlockedTasks.remove(cls)

        @classmethod
        def unlockClass(cls, player):
            if not cls.isUnlocked(player):
                if cls.unlockCond(player) == True:
                    cls.unlock(player)
                else:
                    showNotice([_('未达到日程？？？的解锁条件：\n%s') % (cls.unlockCond(player))])
            else:
                showNotice([_('该日程：%s已解锁！') % cls.name])

        @classmethod
        def isUnlocked(cls, player):
            if cls in player.lockedTasks:
                return False
            if cls in player.unlockedTasks:
                return True
            return cls.unlocked
            
        @classmethod
        def unlockCond(cls, player):
            return True

        @classmethod
        def getRecoScale(cls, player):
            scale = 1.0
            scale *= player.basicRecovery
            scale *= player.phyReco()
            scale /= player.sev()
            scale = max(0.2, scale)
            return scale

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
            scale += player.basicConcentration
            scale += player.wriConc()
            scale /= player.sev()
            return scale

        @classmethod
        def getperf(cls, player):
            perf = ra(player, 1, 100)
            if BookRandConcEffect.has(player):
                perf = max(perf, ra(player, 1, 100))
            return perf

        @classmethod
        def getResultLabel(cls, player, perf, a=85, b=58, c=18):
            if perf > a:
                cls.excePerf(player)
                if BookRandConcEffect.has(player):
                    player.gain_abi(-0.01, 'sev', due=BookRandConcEffect.name)
                resultLabel = cls.__name__ + _('_result_exce')
            elif perf > b:
                cls.goodPerf(player)
                resultLabel = cls.__name__ + _('_result_good')
            elif perf > c:
                cls.normPerf(player)
                resultLabel = cls.__name__ + _('_result_norm')
            else:
                cls.badPerf(player)
                resultLabel = cls.__name__ + _('_result_bad')
            return resultLabel

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return _('日程未解锁！')
            return True

        @classmethod
        def executeTask(cls, player):
            perf = cls.getperf(player)
            perf += cls.getConcScale(player)            
            resultLabel = cls.getResultLabel(player, perf)
            player.updateAfterTask(cls)
            cls.afterTaskResult(player)
            renpy.jump(resultLabel)

        @classmethod
        def excePerf(cls, player):
            pass

        @classmethod
        def goodPerf(cls, player):
            pass

        @classmethod
        def normPerf(cls, player):
            pass

        @classmethod
        def badPerf(cls, player):
            pass

        @classmethod
        def afterTaskResult(cls, player):
            pass


    class WorkTask(Task):
        id = None
        name = None
        kind = _('工作类')
        unlocked = False
        info = None

        @classmethod
        def getConcScale(cls, player):
            scale = 0
            scale += player.basicConcentration
            scale += player.workConcentration
            scale += 15 * player.wor() - 20
            scale += player.wriConc()
            scale /= player.sev()
            return scale

        @classmethod
        def getConsScale(cls, player):
            scale = 1.0
            scale *= player.basicConsumption
            scale *= player.phyCons()
            scale *= player.sev()
            if AcolasItem1.has(player):
                scale *= 0.7
            scale = max(0.2, scale)
            return scale

        @classmethod
        def afterTaskResult(cls, player):
            if rra(player, 60):
                PhysProb.add(player)
            if rra(player, 60):
                MentProb.add(player)


    class SportTask(Task):
        id = None
        name = None
        kind = _('运动类')
        unlocked = False
        info = None

        @classmethod
        def getConcScale(cls, player):
            scale = 0
            scale += player.basicConcentration
            scale += player.sportConcentration
            scale += 20 * player.phy() - 30
            scale += player.wriConc()
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
        def afterTaskResult(cls, player):
            Soreness.add(player, 4)
            if rra(player, 75):
                PhysRezB.add(player)
            if rra(player, 25):
                PhysRezB.add(player)


    class WriteTask(Task):
        id = None
        name = None
        kind = _('写作类')
        unlocked = False
        info = None

        @classmethod
        def getConcScale(cls, player):
            scale = 0
            scale += player.basicConcentration
            scale += player.homeConcentration
            scale += 7 * player.wri() - 10
            scale += player.wriConc()
            scale /= player.sev()
            return scale

        @classmethod
        def getRecoScale(cls, player):
            scale = 1.0
            scale *= player.basicRecovery
            scale *= player.writeRecovery
            scale *= player.phyReco()
            scale /= player.sev()
            scale = max(0.2, scale)
            return scale

        @classmethod
        def getConsScale(cls, player):
            scale = 1.0
            scale *= player.basicConsumption
            scale *= player.homeConsumption
            scale *= player.phyCons()
            scale *= player.sev()
            scale = max(0.2, scale)
            return scale

        @classmethod
        def afterTaskResult(cls, player):
            Inspiration.add(player)


    class RestTask(Task):
        id = None
        name = None
        kind = _('休息类')
        unlocked = False
        info = None

        @classmethod
        def getConcScale(cls, player):
            scale = 0
            scale += player.basicConcentration
            scale += player.homeConcentration
            scale += player.wriConc()
            scale /= player.sev()
            return scale

        @classmethod
        def getConsScale(cls, player):
            scale = 1.0
            scale *= player.basicConsumption
            scale *= player.homeConsumption
            scale *= player.phyCons()
            scale *= player.sev()
            scale = max(0.2, scale)
            return scale

        @classmethod
        def getRecoScale(cls, player):
            scale = 1.0
            scale *= player.basicRecovery
            scale *= player.phyReco()
            scale /= player.sev()
            scale = max(0.2, scale)
            return scale

        @classmethod
        def afterTaskResult(cls, player):
            MentRezB.add(player, ra(player, 0, 2))







    def taskKindInfo(kind, mode):
            d = {
                '工作类i': _('工作类\n\n获取工作能力的基本来源，完成工作进度以赚取金钱。\n如果在周五早上之前没有完成足够的工作量将无法获得全额报酬。'),
                '工作类a': _('我热爱我的工作吗？也许对编程的喜好让我在进行这份工作的时候不会产生太多的抵触心理……\n但除了这份工作，我还能做什么赚钱养活自己呢？'),
                '运动类i': _('运动类\n\n获取身体素质的基本来源，以及恢复精神状态，降低严重程度。\n部分运动有几率受伤，受伤期间无法运动。'),
                '运动类a': _('等我满身肌肉就可以去……泡男人……\n呵呵呵……'),
                '写作类i': _('写作类\n\n获取写作技巧的基本来源，以及恢复精神状态，降低严重程度。\n写作可以获得大量精神的释放和金钱，将随笔发布到社交平台还会获取粉丝。'),
                '写作类a': _('小时候很喜欢在网络上和别人玩文字角色扮演的游戏，但我没想到仅仅是这种消遣的行为也能让我现在的文笔要超出普通人一点……'),
                '休息类i': _('休息类\n\n恢复大量精神状态和降低严重程度。\n在床上休息会有一定几率恢复过劳和受伤。'),
                '休息类a': _('除了晚上，我都能随时随地睡得很香……'),
                '特殊类i': _('特殊类\n\n特殊的日程，外出日程包括去医院购买药物。'),
                '特殊类a': _('虽然我对出门不感兴趣，但如果突发一场大瘟疫，整个城市都被封住的话，一直被关在家里也能难受的。\n我是说，如果。')
            }
            if kind+mode not in d:
                return glitchtext(rd(15,45))
            return d[kind+mode]