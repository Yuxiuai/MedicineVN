init python early:

    class Effect:
        id = None
        name = None
        kind = None
        maxDuration = None
        maxStacks = None
        info = None
        ad = None
        hide = False

        def __init__(self):
            self.duration = self.maxDuration
            self.stacks = 1

        def __eq__(self, other):
            if type(self) == type(other):
                return True
            return False

        def getPrefixInfo(self, player):
            if self.duration == -1:
                dur_info = _('持续时间：永久  ')
            elif self.duration == 1:
                dur_info = _('持续时间：本日  ')
            else:
                dur_info = _('持续时间：') + str(self.duration) + _('天  ')

            if self.stacks > 1:
                sta_info = _('层数：') + str(self.stacks)
            elif self.stacks < 1:
                sta_info = _('该效果将在第二天或之后自动消失')
            else:
                sta_info = ''

            return dur_info + sta_info + '\n'

        def getPrincipalInfo(self):
            showinfo = self.info

            feed = '\n' if showinfo != '' else ''
            return feed + showinfo

        def getSuffixInfo(self):
            feed = '\n\n'
            return feed + self.kind

        def timeUpdate(self, player, times=1):
            if self.duration == -1:
                return
            if self.duration > 0:
                self.duration -= times
            if self.duration <= 0:
                if self.maxDuration != 1:
                    Notice.add(self.name + _('的持续时间为0！效果清除！'))
                self.timeUpAction(player)
                self.clear(player)
            
        @classmethod
        def icon(cls):
            path = 'gui/effects/%s.png' % cls.id
            if not renpy.loadable(path):
                path = 'gui/effects/unknown.png'
            return path

        @classmethod
        def has(cls, player):
            return cls in [type(i) for i in player.effects]

        @classmethod
        def get(cls, player):  # 需要先用has检测
            return list(filter(lambda x: type(x) == cls, player.effects))[0]

        @classmethod
        def getstack(cls, player):
            if not cls.has(player):
                return 0
            return cls.get(player).stacks


        @classmethod
        def add(cls, player, times=1):  # 增加新效果或增加层数
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                Stat.record(player, cls)
                cls.defaultAddEffect(player)

        def clear(self, player):
            self.sub(player, self.stacks)

        @classmethod
        def clearByType(cls, player):
            if cls.has(player):
                cls.get(player).clear(player)

        def sub(self, player, times=1):  # 减少层数
            if times == 0 and not self.stacks == 0:
                return
            for i in range(min(times, self.stacks)):
                self.subStackAction(player)
                self.stacks -= 1
            if self.stacks <= 0:
                self.disableAction(player)
                if self in player.effects:
                    player.effects.remove(self)

        @classmethod
        def subByType(cls, player, times=1):  # 减少层数
            if times == 0:
                return
            if cls.has(player):
                cls.get(player).sub(player, times)

        def enableAction(self, player):  # 启用Buff时进行的操作，一般是提供某些数据
            pass

        def disableAction(self, player):  # Buff无效时的操作，无论是被删除还是被转化还是时间到都会调用，enableAction的反向操作，恢复其对数据的修改
            pass

        def addStackAction(self, player):  # 每次添加层数的操作，一般是某些根据层数给予效果的Effect需要设置
            pass

        def subStackAction(self, player):  # 减少层数的操作，前者的反向函数
            pass

        def timeUpAction(self, player):  # 时间结束的操作，不包括删除Effect的操作，一般是持续时间为0转化为其他Effect时调用
            pass

        def afterSleepAction(self, player):  # 睡眠之后的操作，玩家睡眠后触发的效果，也包括起床效果
            pass

        def afterTaskAction(self, player, task):  # 日程后
            pass

        @classmethod
        def defaultAddEffect(cls, player):  # 默认的add函数，禁止重写
            if not cls.has(player):
                if cls.maxDuration != 0:
                    if cls.kind == '天气' and cls.id not in (198, 199):
                        Notice.add(_('本日的天气为：%s。') % (cls.name))
                    else:
                        if not cls.hide:
                            Notice.add(_('获得新%s：%s！') % (cls.kind, cls.name))
                e = cls()
                player.effects.append(e)
                e.enableAction(player)
                e.addStackAction(player)
            else:
                e = cls.get(player)
                e.duration = cls.maxDuration

                if e.stacks != cls.maxStacks:
                    e.stacks += 1
                    e.addStackAction(player)
            sortByID(player.effects)

        @classmethod
        def notResetDurationAddEffect(cls, player):  # 默认的add函数，禁止重写
            if not cls.has(player):
                if cls.maxDuration != 0:
                    Notice.add(_('获得新%s：%s！') % (cls.kind, cls.name))
                e = cls()
                player.effects.append(e)
                e.enableAction(player)
                e.addStackAction(player)
            else:
                e = cls.get(player)
                temp = e.stacks
                e.stacks = min(e.stacks + 1, cls.maxStacks)
                if temp != e.stacks:
                    e.addStackAction(player)
            sortByID(player.effects)


    def effectKindInfo(kind, mode):
        d = {
            '天气i': _('天气\n\n随状态一同刷新，每天有且只有一个天气，在不同的天气下有不同的效果。'),
            '天气a': _('\n为什么没有可以让我休息的天气……'),
            '状态i': _('状态\n\n一般由各种日程获得，带有一定的持续时间，效果较为复杂，部分状态之间存在转化关系。'),
            '状态a': _('\n据说是0.3版本遗留下来的东西，但0.3版本到底是什么意思？'),
            '增益i': _('增益\n\n一般由各种日程获得，与状态不同的是，增益皆为正面效果且不会互相转化，作为完成某项事情后的奖励。'),
            '增益a': _('\n仪式感带来的安心，成就感带来的慰藉……'),
            '药物反应i': _('药物反应\n\n包含了所有与药物相关的效果，来源于早上刷新，旧药物反应的转化和使用药物后的具体效果。'),
            '药物反应a': _('\n是的，这些生命反抗自然而制取的智慧结晶最终变成了枷锁。'),
            '学识i': _('学识\n\n进行阅读日程后获得的效果，效果相对于增益更为优秀。'),
            '学识a': _('\n你以为我在学习？其实我在看小说哦？'),
            '伤痕i': _('伤痕\n\n永久存在的负面效果，出现此状态说明你经营不善，让主角的身体受到了永久性的创伤。'),
            '伤痕a': _('\n“更近一步走向日落，已看到夜晚的初星。”……'),
            '酒类作用i': _('酒类作用\n\n……'),
            '酒类作用a': _('\n……')
        }
        return d[kind + mode]

    def clearE(player):
        for i in range(len(player.effects) - 1, -1, -1):
            if type(player.effects[i]) != LifeIsColorless:
                player.effects[i].clear(player)
        p.newMorningWeather().add(player)

    def clearI(player):
        for i in range(len(player.items) - 1, -1, -1):
            player.items[i].remove(player)