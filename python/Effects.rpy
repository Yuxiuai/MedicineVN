init -11 python early:

    class WeatherSunny(Effect):
        id = 100
        name = _('{color=#FFD700}晴天{/color}')
        kind = _('天气')
        maxDuration = 1
        maxStacks = 1
        info = _('进行外出散步、慢跑、速跑时会{color=#7CFC00}恢复{/color}额外25%的精神状态，并额外{color=#7CFC00}提升{/color}2点身体素质。')
        ad = _('适合室外运动的好天气。')

        def enableAction(self, player):
            if player.effects[0].kind == '天气' and player.effects[0] != self:
                player.effects[0].clear(player)

            player.outdoorSportRecovery += 0.25

        def disableAction(self, player):
            player.outdoorSportRecovery -= 0.25

        def afterTaskAction(self, player, task):
            if task in (DefaultSport, JoggingSport, FastrunSport):
                player.gain_abi(0.02, 'phy', due='晴天')


    class WeatherRainy(Effect):
        id = 101
        name = _('{color=#87CEFA}雨天{/color}')
        kind = _('天气')
        maxDuration = 1
        maxStacks = 1
        info = _('进行写作类日程或在床上休息会{color=#7CFC00}恢复{/color}额外25%的精神状态，且会额外{color=#7CFC00}降低{/color}1点严重程度。\n外卖价格提升50%。\n\n{color=FF0000}无法进行室外运动。{/color}')
        ad = _('适合宅家的好天气。')

        def enableAction(self, player):
            if player.effects[0].kind == '天气' and player.effects[0] != self:
                player.effects[0].clear(player)

            player.sleepRecovery += 0.25
            player.writeRecovery += 0.25
            player.canOutdoorSport -= 1
            player.foodPrice += 0.5

        def disableAction(self, player):
            player.sleepRecovery -= 0.25
            player.writeRecovery -= 0.25
            player.canOutdoorSport += 1
            player.foodPrice -= 0.5

        def afterTaskAction(self, player, task):
            if task.kind in ('休息类', '写作类'):
                player.gain_abi(-0.01, 'sev', due='雨天')


    class WeatherCloudy(Effect):
        id = 102
        name = _('{color=#B0C4DE}多云{/color}')
        kind = _('天气')
        maxDuration = 1
        maxStacks = 1
        info = _('专注度{color=#FF4500}降低{/color}20%，{color=#7CFC00}提升{/color}5%生病和受伤的恢复率。')
        ad = _('阴沉的天气让你犯困，你总是忍不住打哈欠。')

        def enableAction(self, player):
            if player.effects[0].kind == '天气' and player.effects[0] != self:
                player.effects[0].clear(player)

            player.basicConcentration -= 20

        def disableAction(self, player):
            player.basicConcentration += 20


    class WeatherHot(Effect):
        id = 103
        name = _('{color=#FF4500}酷热{/color}')
        kind = _('天气')
        maxDuration = 1
        maxStacks = 1
        info = _('身体素质暂时{color=#FF4500}降低{/color}10%，室外运动恢复的精神状态和专注度{color=#FF4500}降低{/color}20%，且进行后将额外{color=#FF4500}提升{/color}2点严重程度。')
        ad = _('衣服都被汗打湿了啊，也太热了吧！')

        def enableAction(self, player):
            if player.effects[0].kind == '天气' and player.effects[0] != self:
                player.effects[0].clear(player)

            player.physicalRegarded -= 0.1
            player.sportConcentration -= 20
            player.sportRecovery -= 0.2

        def disableAction(self, player):
            player.physicalRegarded += 0.1
            player.sportConcentration += 20
            player.sportRecovery += 0.2

        def afterTaskAction(self, player, task):
            if task in (DefaultSport, JoggingSport, FastrunSport):
                player.severity += 0.02


    class WeatherWindy(Effect):
        id = 104
        name = _('{color=#98FB98}大风{/color}')
        kind = _('天气')
        maxDuration = 1
        maxStacks = 1
        info = _('完成日程后{color=#7CFC00}恢复{/color}当前精神状态的5% ~ 15%，最高恢复20点。')
        ad = _('人都要被吹跑了！不过我喜欢这种感觉！')

        def enableAction(self, player):
            if player.effects[0].kind == '天气' and player.effects[0] != self:
                player.effects[0].clear(player)

        def afterTaskAction(self, player, task):
            rec = r2(player.mental * ra(player, 1050, 1150) * 0.0001)
            if rec > 20:
                rec = 20
            player.gain_mental(rec)


    class WeatherWet(Effect):
        id = 105
        name = _('{color=#00FFFF}阴冷{/color}')
        kind = _('天气')
        maxDuration = 1
        maxStacks = 1
        info = _('完成日程后若没有良好的运动则有40%的概率生病，若已经生病则不会再生病。')
        ad = _('……我真应该把我那件大衣带到公司……')

        def enableAction(self, player):
            if player.effects[0].kind == '天气' and player.effects[0] != self:
                player.effects[0].clear(player)

        def afterTaskAction(self, player, task):
            if not PhysRezB.has(player) and not PhysPun.has(player):
                if rra(player, 40):
                    PhysPun.add(player)


    class WeatherThunder(Effect):
        id = 106
        name = _('{color=#FFFF00}打雷{/color}')
        kind = _('天气')
        maxDuration = 1
        maxStacks = 1
        info = _('睡眠消耗的精神状态{color=#FF4500}提升{/color}20%。')
        ad = _('我并非是怕打雷的小孩子，但即便是轻微的声响都让我难以入眠……')

        def enableAction(self, player):
            if player.effects[0].kind == '天气' and player.effects[0] != self:
                player.effects[0].clear(player)

            player.deteriorateConsumption += 0.2

        def disableAction(self, player):
            player.deteriorateConsumption -= 0.2

    class WeatherSmog(Effect):
        id = 107
        name = _('{color=#837350}雾霾{/color}')
        kind = _('天气')
        maxDuration = 1
        maxStacks = 1
        info = _('精神状态消耗{color=#FF4500}提升{/color}20%，如果没有戴上口罩，切换场地时会{color=#FF4500}消耗{/color}50%当前的精神状态并有60%的概率{color=#FF4500}获得{/color}生病。')
        ad = _('在这种天气下，呼吸都是一种罪过。')

        def enableAction(self, player):
            if player.effects[0].kind == '天气' and player.effects[0] != self:
                player.effects[0].clear(player)

            player.basicConsumption += 0.2

        def disableAction(self, player):
            player.basicConsumption -= 0.2

        def check(self, player):
            if not MaskEffect.has(player):
                cons = r2(player.mental * 0.5)
                player.gain_mental(-cons)
                if rra(player, 60):
                    PhysPun.add(player)

    class WeatherThunderRain(Effect):
        id = 108
        name = _('{color=#dddd00}雷雨{/color}')
        kind = _('天气')
        maxDuration = 1
        maxStacks = 1
        info = _('睡眠消耗的精神状态{color=#FF4500}提升{/color}20%。\n外卖价格提升80%。\n\n{color=FF0000}无法进行室外运动。{/color}')
        ad = _('雷声如同爆炸一般……')

        def enableAction(self, player):
            if player.effects[0].kind == '天气' and player.effects[0] != self:
                player.effects[0].clear(player)

            player.deteriorateConsumption += 0.2
            player.canOutdoorSport -= 1
            player.foodPrice += 0.8

        def disableAction(self, player):
            player.deteriorateConsumption -= 0.2
            player.canOutdoorSport += 1
            player.foodPrice -= 0.8

    class WeatherTornado(Effect):
        id = 197
        name = _('{color=#4682B4}台风{/color}')
        kind = _('天气')
        maxDuration = 1
        maxStacks = 1
        info = _('该天气持续时无需上班，但也无法进行室外运动，也不能外出。\n外卖价格提升100%。')
        ad = _('以此天气纪念作者两次阳光明媚时出门被突发的大暴雨浇成落汤鸡。')

        def enableAction(self, player):
            if player.effects[0].kind == '天气' and player.effects[0] != self:
                player.effects[0].clear(player)

            player.canOutdoorSport -= 1
            player.canExplore -= 1
            player.foodPrice += 1

        def disableAction(self, player):
            player.canOutdoorSport += 1
            player.canExplore += 1
            player.foodPrice -= 1


    class WeatherNone(Effect):
        id = 198
        name = _('？？？')
        kind = _('天气')
        maxDuration = 1
        maxStacks = 1
        info = _('？？？？？？？？？？？')
        ad = _('在废墟之下，你不知道外界的天气。')

        def enableAction(self, player):
            if player.effects[0].kind == '天气' and player.effects[0] != self:
                player.effects[0].clear(player)

    class WeatherUnknown(Effect):
        id = 199
        name = _('未知')
        kind = _('天气')
        maxDuration = 1
        maxStacks = 1
        info = _('你并不关心今天是什么天气。')

        def enableAction(self, player):
            if player.effects[0].kind == '天气' and player.effects[0] != self:
                player.effects[0].clear(player)


    class Novice(Effect):
        id = 299
        name = _('存在感')
        kind = _('增益')
        maxDuration = 14
        maxStacks = 1
        info = _('持续时间内{color=#7CFC00}降低{/color}10%的严重程度和睡眠消耗的精神状态。\n当你因精神状态过低即将崩溃时可以选择消耗该效果{color=#7CFC00}恢复{/color}精神状态至80。')
        ad = _('“很想看到渐次泛白的黎明时分的天宇，想喝热气蒸腾的牛奶，想闻树木的清香，想翻晨报的版面。”')

        def enableAction(self, player):
            player.severityRegarded -= 0.1
            player.deteriorateConsumption -= 0.1

        def disableAction(self, player):
            player.severityRegarded += 0.1
            player.deteriorateConsumption += 0.1


    class Erection(Effect):
        id = 201
        name = _('勃起')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 1
        info = _('你的欲望让你的生殖器官充血膨胀。')
        ad = _('我感觉我的内裤开始变紧了……')

        def afterTaskAction(self, player, task):
            if rra(player, 50):
                self.clear(player)

        def disableAction(self, player):
            Pleasure.add(player)

    class Pleasure(Effect):
        id = 202
        name = _('写作欲')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 1
        info = _('可以进行随笔写作。')
        ad = _('好想写点什么……')


    class ConsInc(Effect):
        id = 210
        name = _('紧张')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 5
        info = _('精神状态消耗每层都会{color=#FF4500}提升{/color}10%，精神状态恢复每层都会{color=#7CFC00}提升{/color}10%。')
        ad = _('做点什么，是的，尽可能多地做，尽可能完美地做，至少在死前做更多的事情，做世界上大多数人都没做过的事，不然怎么能算活着呢。')

        def enableAction(self, player):
            if ConsDec.has(player):
                ConsDec.subByType(player)
                self.sub(player)

        def addStackAction(self, player):
            player.basicConsumption += 0.1
            player.basicRecovery += 0.1

        def subStackAction(self, player):
            player.basicConsumption -= 0.1
            player.basicRecovery -= 0.1


    class ConsDec(Effect):
        id = 211
        name = _('放松')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 5
        info = _('精神状态消耗每层都会{color=#7CFC00}降低{/color}10%，精神状态恢复每层都会{color=#FF4500}降低{/color}10%。')
        ad = _('不，也许我没必要做那么多？我为什么要那样折磨自己？死亡之后一切都对我没有意义，及时行乐……我应该辞了这份工作。')

        def enableAction(self, player):
            if ConsInc.has(player):
                ConsInc.subByType(player)
                self.sub(player)

        def addStackAction(self, player):
            player.basicConsumption -= 0.1
            player.basicRecovery -= 0.1

        def subStackAction(self, player):
            player.basicConsumption += 0.1
            player.basicRecovery += 0.1


    class ConcDec(Effect):
        id = 212
        name = _('睡意')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 5
        info = _('专注度每层都会{color=#FF4500}降低{/color}10%，睡眠消耗的精神状态每层都会{color=#7CFC00}降低{/color}10%。')
        ad = _('是的，让我睡觉，求你了，能让我躺在柔软的床上美美地睡一觉的话我什么都会做的。')

        def enableAction(self, player):
            if ConcInc.has(player):
                ConcInc.subByType(player)
                self.sub(player)

        def addStackAction(self, player):
            player.basicConcentration -= 10
            player.deteriorateConsumption -= 0.1

        def subStackAction(self, player):
            player.basicConcentration += 10
            player.deteriorateConsumption += 0.1


    class ConcInc(Effect):
        id = 213
        name = _('兴奋')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 5
        info = _('专注度每层都会{color=#7CFC00}提升{/color}10%，睡眠消耗的精神状态每层都会{color=#FF4500}提升{/color}10%。')
        ad = _('我痛恨我需要睡眠，若是能有按钮迅速跳过夜晚瞬间恢复精神状态来到第二天，或是单纯将我的肉体与电线链接便可恢复能量就好了。')

        def enableAction(self, player):
            if ConcDec.has(player):
                ConcDec.subByType(player)
                self.sub(player)

        def addStackAction(self, player):
            player.basicConcentration += 10
            player.deteriorateConsumption += 0.1

        def subStackAction(self, player):
            player.basicConcentration -= 10
            player.deteriorateConsumption -= 0.1

    class Restlessness(Effect):
        id = 214
        name = _('紧迫')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 1
        info = _('工作速度{color=#7CFC00}提升{/color}30%，对工作的专注度{color=#7CFC00}提升{/color}30%。')
        ad = _('我难以呼吸，总觉有何未知的存在正追赶着我，挤压着我将我向前推进。')

        def enableAction(self, player):
            player.workSpeed += 0.3
            player.workConcentration += 30

        def disableAction(self, player):
            player.workSpeed -= 0.3
            player.workConcentration -= 30


    class Contentment(Effect):
        id = 215
        name = _('安逸')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 1
        info = _('在床上休息恢复的精神状态{color=#7CFC00}提升{/color}30%，且必定移除全部的过劳。')
        ad = _('我已经得到了部分存在而得的愉悦，较低的期望让我不再渴求之外的事物，无需追赶自己。')

        def enableAction(self, player):
            player.sleepRecovery += 0.3

        def disableAction(self, player):
            player.sleepRecovery -= 0.3

        def afterTaskAction(self, player, task):
            if task.name == _('在床上休息'):
                if PhysProb.has(player):
                    PhysProb.clearByType(player)


    class Dread(Effect):
        id = 216
        name = _('恐惧')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 1
        info = _('暂时{color=#FF4500}提升{/color}15%的严重程度。\n状态结束后降低5点严重程度。')
        ad = _('当破除这份来源于存在本身的的恐惧后，迎来的则是存活的希望。')

        def enableAction(self, player):
            player.severityRegarded += 0.15

        def disableAction(self, player):
            player.severityRegarded -= 0.15
            player.gain_abi(-0.05, 'sev', due='恐惧消散')
            
    

    class Desire(Effect):
        id = 217
        name = _('渴求')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 1
        info = _('精神状态消耗{color=#FF4500}提升{/color}15%，但所有基础能力属性的获取加成{color=#7CFC00}提升{/color}1点。')
        ad = _('对美好的未来之憧憬让我更加渴望努力获得我应得之物，但这份躁动让我难以忍受。')

        def enableAction(self, player):
            player.basicConsumption += 0.15
            player.physicalGain += 0.01
            player.workingGain += 0.01
            player.writingGain += 0.01

        def disableAction(self, player):
            player.basicConsumption -= 0.15
            player.physicalGain -= 0.01
            player.workingGain -= 0.01
            player.writingGain -= 0.01


    class Sadness(Effect):
        id = 218
        name = _('悲伤')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 1
        info = _('可以进行随笔写作，写作的价值度提升15%，写作技巧获取加成{color=#7CFC00}提升{/color}2点。')
        ad = _('一双无形的手挤压着我的心脏，它渴望看到我的眼泪。')

        def enableAction(self, player):
            player.writeValuable += 0.15
            player.writingGain += 0.02

        def disableAction(self, player):
            player.writeValuable -= 0.15
            player.writingGain -= 0.02


    class Agony(Effect):
        id = 219
        name = _('澎湃')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 1
        info = _('每个日程结束后都会获得良好的运动，运动恢复的精神状态{color=#7CFC00}提升{/color}30%，对运动类日程的专注度{color=#7CFC00}提升{/color}20%，身体素质获取加成{color=#7CFC00}提升{/color}1点。')
        ad = _('即便世间还要如此折磨我，但我仍要努力反抗。')

        def enableAction(self, player):
            player.sportRecovery += 0.3
            player.sportConcentration += 20
            player.physicalGain += 0.01

        def disableAction(self, player):
            player.sportRecovery -= 0.3
            player.sportConcentration -= 20
            player.physicalGain -= 0.01

        def afterTaskAction(self, player, task):
            PhysRezB.add(player)


    class PhysPun(Effect):
        id = 220
        name = _('生病')
        kind = _('状态')
        maxDuration = 7
        maxStacks = 2
        info = _('获得该状态时{color=#FF4500}降低{/color}2点身体素质和2点工作能力。\n专注度{color=#FF4500}降低{/color}10%，精神状态消耗{color=#FF4500}提升{/color}10%，精神状态恢复{color=#FF4500}降低{/color}10%；在床上休息恢复的精神状态{color=#7CFC00}提升{/color}40%。\n进行非在床上休息的日程时会{color=#FF4500}降低{/color}10%的当前精神状态，精神状态为负时{color=#FF4500}降低{/color}10点精神状态并提升1点严重程度。\n持续时间结束或层数超过1层时{color=#FF4500}转化{/color}为体弱。')
        ad = _('病痛折磨着我，与脑中毫无频率的头疼一同。')

        @classmethod
        def add(cls, player, times=1):
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                if cls.has(p):
                    Notice.add(_('生病层数为2，{color=#FF4500}转化{/color}为伤痕:体弱！'))
                    Debilitated.add(player)
                    cls.clearByType(player)
                    return
                Stat.record(player, cls)
                cls.defaultAddEffect(player)

        def afterTaskAction(self, player, task):
            if task.name != Sleep.name:
                dmg = r2(player.mental * 0.1)
                if dmg <= 0:
                    dmg = r2(10 * player.basicConsumption * f())
                    player.severity += 0.01
                    Notice.add(_('由于生病，提升了1点严重程度！'))
                player.gain_mental(-dmg, self.name)


        def timeUpAction(self, player):
            Notice.add(_('生病持续时间结束！{color=#FF4500}转化{/color}为伤痕:体弱！'))
            Debilitated.add(player)

        def getPrincipalInfo(self):
            showinfo = self.info

            feed = '\n' if showinfo != '' else ''

            if BookPhysPunEffect.has(p):
                return feed + showinfo + _('\n\n当前治愈率：')+green(self.getCurePer(p))+'%'
            return feed + showinfo + _('\n\n当前治愈率：')+str(self.getCurePer(p))+'%'

        def getCurePer(self, player):
            curePercent = 10.0
            if WeatherCloudy.has(player):
                curePercent += 5
            if DrugColdrexEffect.has(player):
                curePercent += 2 ** DrugColdrexEffect.getstack(player)
            if PhysRezA.has(player):
                curePercent += PhysRezA.getstack(player) * 2.5
            if PhysRezB.has(player):
                curePercent += PhysRezB.getstack(player) * 2.5
            if Physique.has(player):
                curePercent += Physique.getstack(player) * 1
            if BookPhysPunEffect.has(player):
                curePercent += 15
            return curePercent

        def enableAction(self, player):
            player.gain_abi(-0.02, 'wor', due='生病')
            player.gain_abi(-0.02, 'phy', due='生病')
            player.basicConcentration -= 10
            player.basicConsumption += 0.1
            player.basicRecovery -= 0.1
            player.sleepRecovery += 0.4

        def disableAction(self, player):
            player.basicConcentration += 10
            player.basicConsumption -= 0.1
            player.basicRecovery += 0.1
            player.sleepRecovery -= 0.4

        def cureBySleep(self, player):
            
            if rra(player, self.getCurePer(player)):  # 判定成功时，消耗所有的rezA和rezB
                Notice.add(_('成功治愈！'))
                PhysRezA.clearByType(player)
                PhysRezB.clearByType(player)
                DrugColdrexEffect.clearByType(player)
                
                bonus = int(2 + Physique.getstack(player)/3)
                if BookPhysPunEffect.has(player):
                    BookPhysPunEffect.clearByType(player)
                    s = r2(player.severity * 0.02)
                    player.gain_abi(-s, 'sev', due='学习成果：《呼吸训练》',extra=True)
                player.gain_abi(0.01 * bonus, 'phy')
                player.gain_abi(-0.01 * bonus, 'sev')

                self.clear(player)



    class MentPun(Effect):
        id = 221
        name = _('偏执')
        kind = _('状态')
        maxDuration = 7
        maxStacks = 2
        info = _('获得该状态时{color=#FF4500}降低{/color}2点写作技巧和2点工作能力。\n精神状态消耗{color=#FF4500}提升{/color}25%，工作类日程的专注度{color=#7CFC00}提升{/color}60%，工作类日程消耗的精神状态{color=#7CFC00}降低{/color}60%，运动类日程的专注度{color=#FF4500}降低{/color}50%。\n\n无法完成委托，阅读小说。\n持续时间结束时或层数超过1层{color=#FF4500}转化{/color}为谵妄。')
        ad = _('是的，工作，加倍努力工作，其他的一切都不重要。')

        @classmethod
        def add(cls, player, times=1):
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                if cls.has(p):
                    Notice.add(_('偏执层数为2，{color=#FF4500}转化{/color}为伤痕:谵妄！'))
                    Decadent.add(player)
                    cls.clearByType(player)
                    return
                Stat.record(player, cls)
                cls.defaultAddEffect(player)

        def timeUpAction(self, player):
            Notice.add(_('偏执持续时间结束！{color=#FF4500}转化{/color}为伤痕:谵妄！'))
            Decadent.add(player)

        def enableAction(self, player):
            player.gain_abi(-0.02, 'wor', due='偏执')
            player.gain_abi(-0.02, 'wri', due='偏执')
            player.canWrite -= 1
            player.canRead -= 1
            player.sportConcentration -= 50
            player.basicConsumption += 0.25
            player.workConcentration += 60
            player.workConsumption -= 0.6

        def disableAction(self, player):
            player.canWrite += 1
            player.canRead += 1
            player.sportConcentration += 50
            player.basicConsumption -= 0.25
            player.workConcentration -= 60
            player.workConsumption += 0.6


    class Injured(Effect):
        id = 222
        name = _('受伤')
        kind = _('状态')
        maxDuration = 7
        maxStacks = 2
        info = _('专注度{color=#FF4500}降低{/color}15%，精神状态消耗{color=#FF4500}提升{/color}25%。\n无法进行运动类日程。\n进行非在床上休息的日程时会{color=#FF4500}降低{/color}10%的当前精神状态，精神状态为负时{color=#FF4500}降低{/color}10点精神状态并提升1点严重程度。\n持续时间结束时或层数超过1层{color=#FF4500}转化{/color}为体弱。')
        ad = _('我已为力量做出了牺牲。')

        @classmethod
        def add(cls, player, times=1):
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                if cls.has(p):
                    Notice.add(_('受伤层数为2，{color=#FF4500}转化{/color}为：体弱！'))
                    Debilitated.add(player)
                    cls.clearByType(player)
                    return
                Stat.record(player, cls)
                cls.defaultAddEffect(player)

        def timeUpAction(self, player):
            Notice.add(_('受伤持续时间结束！{color=#FF4500}转化{/color}为：体弱！'))
            Debilitated.add(player)

        def afterTaskAction(self, player, task):
            if task.name != Sleep.name:
                dmg = r2(player.mental * 0.1)
                if dmg <= 0:
                    dmg = r2(10 * player.basicConsumption * f())
                    player.severity += 0.01
                    Notice.add(_('由于受伤，提升了1点严重程度！'))
                player.gain_mental(-dmg, self.name)

        def enableAction(self, player):
            player.basicConcentration -= 15
            player.basicConsumption += 0.25
            player.canSport -= 1

        def disableAction(self, player):
            player.basicConcentration += 15
            player.basicConsumption -= 0.25
            player.canSport += 1

        def getPrincipalInfo(self):
            showinfo = self.info

            feed = '\n' if showinfo != '' else ''

            if BookPhysPunEffect.has(p):
                return feed + showinfo + _('\n\n当前治愈率：')+green(self.getCurePer(p))+'%'
            return feed + showinfo + _('\n\n当前治愈率：')+str(self.getCurePer(p))+'%'

        def getCurePer(self, player):
            curePercent = 10.0
            if WeatherCloudy.has(player):
                curePercent += 5
            if PhysRezA.has(player):
                curePercent += PhysRezA.getstack(player) * 2.5
            if PhysRezB.has(player):
                curePercent += PhysRezB.getstack(player) * 2.5
            if Physique.has(player):
                curePercent += Physique.getstack(player) * 1
            if Pain.has(player):
                curePercent -= Pain.getstack(player) * 50
            if BookPhysPunEffect.has(player):
                curePercent += 15
            return curePercent


        def cureBySleep(self, player):
            
            if rra(player, self.getCurePer(player)):  # 判定成功时，消耗所有的rezA和rezB
                Notice.add(_('成功治愈！'))
                PhysRezA.clearByType(player)
                PhysRezB.clearByType(player)
                bonus = 2 + int(Physique.getstack(player)/3)
                if BookPhysPunEffect.has(player):
                    BookPhysPunEffect.clearByType(player)
                    s = r2(player.severity * 0.02)
                    player.gain_abi(-s, 'sev', due='学习成果：《呼吸训练》',extra=True)
                player.gain_abi(0.01 * bonus, 'phy')
                player.gain_abi(-0.01 * bonus, 'sev')

                self.clear(player)

        def afterSleepAction(self, player):


            if self.stacks == 0 and rra(player, self.getCurePer(player)):
                Notice.add(_('一觉醒来，你的受伤已经治愈！'))
                PhysRezA.clearByType(player)
                PhysRezB.clearByType(player)
                bonus = 2 + Physique.getstack(player)/2
                bonus = int(bonus*0.5)
                if BookPhysPunEffect.has(player):
                    BookPhysPunEffect.clearByType(player)
                    s = r2(player.severity * 0.02)
                    player.gain_abi(-s, 'sev', due='学习成果：《呼吸训练》',extra=True)
                player.gain_abi(0.01 * bonus, 'phy')
                player.gain_abi(-0.01 * bonus, 'sev')

                self.clear(player)


    class PhysProb(Effect):
        id = 223
        name = _('过劳')
        kind = _('状态')
        maxDuration = 3
        maxStacks = 99
        info = _('进行工作类日程时有一定概率获得。\n获得该状态时各有20%的概率{color=#FF4500}降低{/color}2点身体素质和2点工作能力。\n入睡前如果大于3层，状态将在第二日{color=#FF4500}转化{/color}为生病。')
        ad = _('痛苦来自于无法衡量工作和身体健康。')

        def enableAction(self, player):
            if rra(player, 4 * player.week):
                player.gain_abi(-0.01, 'phy', due='过劳')
            if rra(player, 4 * player.week):
                player.gain_abi(-0.01, 'wor', due='过劳')

        @classmethod
        def add(cls, player, times=1):
            if times == 0:
                return
            if BookConcEffect.has(player):
                return
            GuideE.unlock(cls)
            for i in range(times):
                Stat.record(player, cls)
                if PhysRezA.has(player):
                    Notice.add(_('添加%s：%s！{color=#FF4500}抵消{/color}1层状态：良好的睡眠！') % (cls.kind, cls.name))
                    PhysRezA.subByType(player)
                elif PhysRezB.has(player):
                    Notice.add(_('添加%s：%s！{color=#FF4500}抵消{/color}1层状态：良好的运动！') % (cls.kind, cls.name))
                    PhysRezB.subByType(player)
                else:
                    cls.defaultAddEffect(player)

        def afterSleepAction(self, player):
            if self.stacks >= 4:
                Notice.add(_('过劳层数大于3，{color=#FF4500}转化{/color}为生病！'))
                PhysPun.add(player)
                if PhysPun.has(player):
                    PhysPun.get(player).duration += 1
                self.clear(player)
            elif GameDifficulty4.has(player) or GameDifficulty5.has(player):
                if PhysPun.has(player):
                    return
                perc = [0, 5, 10, 25]
                if rra(player, perc[self.stacks]):
                    Notice.add(_('因层数过高，过劳{color=#FF4500}转化{/color}为生病！'))
                    PhysPun.add(player)
                    if PhysPun.has(player):
                        PhysPun.get(player).duration += 1
                    self.clear(player)
                
        
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


    class MentProb(Effect):
        id = 224
        name = _('焦虑')
        kind = _('状态')
        maxDuration = 3
        maxStacks = 99
        info = _('进行工作类日程时有一定概率获得。\n获得该状态时各有20%的概率{color=#FF4500}降低{/color}2点写作技巧和2点工作能力。\n入睡前如果大于3层，状态将在第二日{color=#FF4500}转化{/color}为偏执。')
        ad = _('我难以呼吸，总觉有何未知的存在正追赶着我，挤压着我将我向前推进。')

        def enableAction(self, player):
            if rra(player, 4 * player.week):
                player.gain_abi(-0.01, 'wri', due='焦虑')
            if rra(player, 4 * player.week):
                player.gain_abi(-0.01, 'wor', due='焦虑')

        @classmethod
        def add(cls, player, times=1):
            if times == 0:
                return
            if BookConcEffect.has(player):
                return
            GuideE.unlock(cls)
            for i in range(times):
                Stat.record(player, cls)
                if MentRezA.has(player):
                    Notice.add(_('添加%s：%s！{color=#FF4500}抵消{/color}1层状态：精神的释放!') % (cls.kind, cls.name))
                    MentRezA.subByType(player)
                elif MentRezB.has(player):
                    Notice.add(_('添加%s：%s！{color=#FF4500}抵消{/color}1层状态：精神的平复！') % (cls.kind, cls.name))
                    MentRezB.subByType(player)
                else:
                    cls.defaultAddEffect(player)

        def afterSleepAction(self, player):
            if self.stacks >= 4:
                Notice.add(_('焦虑层数大于3，{color=#FF4500}转化{/color}为偏执！'))
                MentPun.add(player)
                if MentPun.has(player):
                    MentPun.get(player).duration += 1
                self.clear(player)
            elif GameDifficulty4.has(player) or GameDifficulty5.has(player):
                perc = [0, 5, 10, 25]
                if MentPun.has(player):
                    return
                if rra(player, perc[self.stacks]):
                    Notice.add(_('因层数过高，焦虑{color=#FF4500}转化{/color}为偏执！'))
                    MentPun.add(player)
                    if MentPun.has(player):
                        MentPun.get(player).duration += 1
                    self.clear(player)
            
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



    class PhysRezA(Effect):
        id = 230
        name = _('良好的睡眠')
        kind = _('状态')
        maxDuration = 2
        maxStacks = 99
        info = _('在床上休息后随机获得1~3层，过夜有10%的概率获得1层。\n{color=#7CFC00}抵消{/color}相同层数的过劳。\n每层都能提升2.5%治愈生病和受伤的恢复率。')
        ad = _('“梦中的我穿梭在林地的高耸树木之间，又越过由刀刃制成的阶梯和源头是一幅画的宽广河流……”')

        @classmethod
        def defaultAddEffect(cls, player):  # 默认的add函数，禁止重写
            cls.notResetDurationAddEffect(player)

        @classmethod
        def add(cls, player, times=1):
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                Stat.record(player, cls)
                if PhysProb.has(player):
                    Notice.add(_('添加%s：%s！{color=#7CFC00}抵消{/color}1层状态：过劳！') % (cls.kind, cls.name))
                    PhysProb.subByType(player)
                else:
                    cls.defaultAddEffect(player)


    class PhysRezB(Effect):
        id = 231
        name = _('良好的运动')
        kind = _('状态')
        maxDuration = 2
        maxStacks = 99
        info = _('进行部分运动类日程后随机获得0~2层，外出探索有25%的概率获得1层。\n{color=#7CFC00}抵消{/color}相同层数的过劳。\n每层都能提升2.5%治愈生病和受伤的恢复率。')
        ad = _('“我的心脏以不同于以往的速度躁动跳跃，仿佛我的肋骨也无法阻拦，如若要挣脱这副残破躯壳的限制……”')

        @classmethod
        def defaultAddEffect(cls, player):  # 默认的add函数，禁止重写
            cls.notResetDurationAddEffect(player)

        @classmethod
        def add(cls, player, times=1):
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                Stat.record(player, cls)
                if PhysProb.has(player):
                    Notice.add(_('添加%s：%s！{color=#7CFC00}抵消{/color}1层状态：过劳！') % (cls.kind, cls.name))
                    PhysProb.subByType(player)
                else:
                    cls.defaultAddEffect(player)


    class MentRezA(Effect):
        id = 232
        name = _('精神的释放')
        kind = _('状态')
        maxDuration = 2
        maxStacks = 99
        info = _('完成委托时根据消耗的灵感及写作素材层数获得，每10层灵感及写作素材都可以获得1层。\n{color=#7CFC00}抵消{/color}相同层数的焦虑。')
        ad = _('“我掀开盖骨，将我的脑脊液倒进我前方的键盘，于是我的双手在键盘上如起舞的天鹅，我所理解的语言即以字符的形式在屏幕上显现，此时此刻的愉悦紧紧环绕着我的气管，似要将我缢杀。”')

        @classmethod
        def defaultAddEffect(cls, player):  # 默认的add函数，禁止重写
            cls.notResetDurationAddEffect(player)

        @classmethod
        def add(cls, player, times=1):
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                Stat.record(player, cls)
                if MentProb.has(player):
                    Notice.add(_('添加%s：%s！{color=#7CFC00}抵消{/color}1层状态：焦虑！') % (cls.kind, cls.name))
                    MentProb.subByType(player)
                else:
                    cls.defaultAddEffect(player)


    class MentRezB(Effect):
        id = 233
        name = _('精神的平复')
        kind = _('状态')
        maxDuration = 2
        maxStacks = 99
        info = _('进行部分休息类日程后随机获得0~2层，周末时每完成一项日程都有60%的概率获得1层。\n{color=#7CFC00}抵消{/color}相同层数的焦虑。')  # 33%
        ad = _('“我呼吸，尽可能地呼吸。也许下一刻我就失去了呼吸的权利。”')

        @classmethod
        def defaultAddEffect(cls, player):  # 默认的add函数，禁止重写
            cls.notResetDurationAddEffect(player)

        @classmethod
        def add(cls, player, times=1):
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                Stat.record(player, cls)
                if MentProb.has(player):
                    Notice.add(_('添加%s：%s！{color=#7CFC00}抵消{/color}1层状态：焦虑！') % (cls.kind, cls.name))
                    MentProb.subByType(player)
                else:
                    cls.defaultAddEffect(player)


    class Soreness(Effect):
        id = 240
        name = _('酸痛')
        kind = _('状态')
        maxDuration = 4
        maxStacks = 99
        info = _('每次进行运动时获得4层，拥有该状态时进行任意日程都会获得1层。\n每层酸痛都会使起床时和进行运动类日程时额外{color=#FF4500}消耗{/color}0.5点精神状态。\n再次获取不会刷新该状态的持续时间，持续时间结束时获得1层体弱。\n\n进行拉伸运动可{color=#7CFC00}转化{/color}该状态为体魄。')
        ad = _('“我感觉每根骨头中间的接缝处都积满了淤泥，肌肉与肌肉之间的连接变得干枯易碎。”')

        @classmethod
        def defaultAddEffect(cls, player):  # 默认的add函数，禁止重写
            cls.notResetDurationAddEffect(player)

        def afterSleepAction(self, player):
            m = r2(0.5 * self.stacks * f())
            player.gain_mental(-m, self.name, True)

        def timeUpAction(self, player):
            Debilitated.add(player)

        def afterTaskAction(self, player, task):  # 日程后
            self.add(player)
            if task.kind == "运动类":
                self.afterSleepAction(player)

        @classmethod
        def add(cls, player, times=1):  # 增加新效果或增加层数
            if GameDifficulty1.has(player) or GameDifficulty2.has(player):
                return
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                Stat.record(player, cls)
                cls.defaultAddEffect(player)


    class Inspiration(Effect):
        id = 241
        name = _('灵感')
        kind = _('状态')
        maxDuration = 4
        maxStacks = 99
        info = _('当进行的日程与上一个日程不同时获得1层。\n完成委托，随笔写作或集中写作将消耗该增益，每层都能{color=#7CFC00}提升{/color}获得的精神的释放层数和委托价值。\n再次获取不会刷新该状态的持续时间，持续时间结束时获得1层偏执。\n\n进行记录想法可{color=#7CFC00}转化{/color}该状态为写作素材。')
        ad = _('“我的情绪比平常更为高昂。有些事物我永远也不会理解，因而永远都那么珍贵，而如今我离它们更近了一点。”')

        @classmethod
        def add(cls, player, times=1):  # 增加新效果或增加层数
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                Stat.record(player, cls)
                cls.defaultAddEffect(player)

        @classmethod
        def defaultAddEffect(cls, player):  # 默认的add函数，禁止重写
            cls.notResetDurationAddEffect(player)
            if player.experience == 'wri':
                
                if not GameDifficulty5.has(player):
                    rec = Task.getRecoScale(player)*ra(player,1,50)*0.1*f()
                    rec *= (100 - Inspiration.getstack(player)*3) * 0.01
                    if rec > 0:
                        player.gain_mental(rec, due=cls.name)
                else:
                    rec = Task.getConsScale(player)*ra(player,1,50)*0.05*f()
                    if player.mental > 50:
                        rec *= 2
                    player.gain_mental(-rec, due=cls.name)

            if BookInsEffect.has(player):
                Inspiration.get(player).stacks += 1

        def afterTaskAction(self, player, task):  # 日程后
            if task.name == _('记录想法'):
                FixedInspiration.add(player, int(self.stacks * 0.8 + 1))
                self.clear(player)

        def afterSleepAction(self, player):
            if GameDifficulty1.has(player) or GameDifficulty2.has(player):
                FixedInspiration.add(player, int(self.stacks * 0.8))
                self.clear(player)

        def timeUpAction(self, player):
            if player.experience != 'phy':
                MentPun.add(player)


    class Satiety(Effect):
        id = 242
        name = _('饱腹')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 99
        info = _('食用食物获得。\n专注度{color=#FF4500}降低{/color}10%。\n食物恢复的精神状态每层都会{color=#FF4500}降低{/color}200%，且使用食物时每层会提升2点严重程度。\n进行日程后有75%的概率移除1层该状态。')
        ad = _('你腹痛难耐，悔恨自己暴食的行为。')

        @classmethod
        def add(cls, player, times=1):
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                Stat.record(player, cls)
                cls.defaultAddEffect(player)

        def enableAction(self, player):
            player.basicConcentration -= 10

        def addStackAction(self, player):
            player.foodRecovery -= 2.0
            

        def subStackAction(self, player):
            player.foodRecovery += 2.0

        def disableAction(self, player):
            player.basicConcentration += 10

        def afterTaskAction(self, player, task):
            if rra(player, 75):
                self.sub(player)

    class Anxiety(Effect):
        id = 243
        name = _('忧虑')
        kind = _('状态')
        maxDuration = 7
        maxStacks = 99
        info = _('无法进行随笔写作，完成委托，集中写作日程。')
        ad = _('你对自己可能会丢掉工作这件事的担忧占据了大脑。')

        def enableAction(self, player):
            self.duration = ra(player, 4, 6)


    class Caffeine(Effect):
        id = 244
        name = _('失眠')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 99
        info = _('每层都会{color=#FF4500}提升{/color}10%睡眠消耗的精神状态。')
        ad = _('试图干涉生物体生命活动的内在节律性的结果。')

        def addStackAction(self, player):  # 每次添加层数的操作，一般是某些根据层数给予效果的Effect需要设置
            player.deteriorateConsumption += 0.1

        def subStackAction(self, player):  # 减少层数的操作，前者的反向函数
            player.deteriorateConsumption -= 0.1

    class Smoking(Effect):
        id = 245
        name = _('难耐')
        kind = _('状态')
        maxDuration = 7
        maxStacks = 5
        info = _('未拥有清醒状态时，每层都会{color=#FF4500}提升{/color}10%的严重程度。\n每完成一个日程都有66%的概率{color=#7CFC00}减少{/color}持续时间。')
        ad = _('也许我不该抽烟的。')

        def addStackAction(self, player):
            player.severityRegarded += 0.1

        def subStackAction(self, player):
            player.severityRegarded -= 0.1

        def afterTaskAction(self, player, task):
            if self.duration > 1 and rra(player, 66):
                self.duration -= 1

    class Pain(Effect):
        id = 246
        name = _('痛苦')
        kind = _('状态')
        maxDuration = 7
        maxStacks = 99
        info = _('每层都会{color=#FF4500}提升{/color}15%的严重程度和睡眠消耗的精神状态，并降低50%受伤的治愈率。')
        ad = _('“终于有活着的感觉了……\n不过放着不管的话手会变得像烤乌贼那样的。”')

        def addStackAction(self, player):
            player.severityRegarded += 0.15
            player.deteriorateConsumption += 0.15

        def subStackAction(self, player):
            player.severityRegarded -= 0.15
            player.deteriorateConsumption -= 0.15
    
    class Headache(Effect):
        id = 247
        name = _('突发头疼')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 1
        info = _('精神状态消耗{color=#FF4500}提升{/color}100%，精神状态恢复{color=#FF4500}降低{/color}50%。\n进行在床上休息，小睡的非差结果可结束该状态。')
        ad = _('血管随着心跳的节奏快速地鼓动着，痛苦从大脑辐射至全身。')

        def addStackAction(self, player):
            player.basicConsumption += 1.0
            player.basicRecovery -= 0.5

        def subStackAction(self, player):
            player.basicConsumption -= 1.0
            player.basicRecovery += 0.5

        def afterTaskAction(self, player, task):
            if task == Sleep:
                self.clear(player)

    class Headache_(Effect):
        id = 248
        name = _('不会获得突发头疼')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 1
        info = _("今天不会再获得突发头疼了。")
        hide = True

    class CafeWork_(Effect):
        id = 248
        name = _('已做过代码维护')
        kind = _('状态')
        maxDuration = 14
        maxStacks = 1
        info = _("本周已经进行过一次代码维护了。")
        hide = True
    
        def afterSleepAction(self, player):
            if player.today == 7:
                self.clear(player)

    class Stomachache(Effect):
        id = 249
        name = _('腹痛')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 1
        info = _('严重度{color=#FF4500}提升{/color}10%，专注度{color=#FF4500}降低{/color}10%，食用道具恢复的精神状态{color=#FF4500}降低{/color}200%。\n进行在床上休息，小睡的非差结果可结束该状态。')
        ad = _('所有的脏器一同扭曲痉挛。')

        def addStackAction(self, player):
            player.severityRegarded += 0.1
            player.basicConcentration -= 10
            player.foodRecovery -= 2.0

        def subStackAction(self, player):
            player.severityRegarded -= 0.1
            player.basicConcentration += 10
            player.foodRecovery += 2.0

        
        
    
    class Stomachache_(Effect):
        id = 250
        name = _('不会获得腹痛')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 1
        info = _("今天不会再获得腹痛了。")
        hide = True


    class Tired(Effect):
        id = 251
        name = _('疲倦')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 1
        info = _('无法进行外出，下一个日程专注度{color=#FF4500}降低{/color}60%，但在床上休息日程不受影响。')
        ad = _('不应该这样的……')

        def addStackAction(self, player):
            player.basicConcentration -= 60

        def subStackAction(self, player):
            player.basicConcentration += 60

        def afterTaskAction(self, player, task):
            if task != GoOutside:
                self.clear(player)

    class Malnutrition_(Effect):
        id = 252
        name = _('未使用有营养的食物')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 99
        info = _('消失时变为营养不良。')
        ad = _('')
        hide = True

        def timeUpAction(self, player):
            Malnutrition.add(player)

    class Malnutrition(Effect):
        id = 252
        name = _('营养不良')
        kind = _('状态')
        maxDuration = -1
        maxStacks = 99
        info = _('每层使专注度{color=#FF4500}降低{/color}10%，且完成日程后根据层数{color=#FF4500}降低{/color}精神状态。\n食用部分食物时移除所有层数。\n进行日程后有50%的概率{color=#FF4500}提升{/color}1层。\n过夜、进行运动类日程和外出后固定{color=#FF4500}提升{/color}1层。')
        ad = _('我需要有营养的食物来保持生存，就像花朵需要土壤。')

        def addStackAction(self, player):
            player.basicConcentration -= 10

        def subStackAction(self, player):
            player.basicConcentration += 10

        def afterTaskAction(self, player, task):
            con = 5*self.stacks + 0.15*self.stacks*player.mental
            if con < 5:
                con = 5
            player.gain_mental(-con*player.severity*f(), due='营养不良')
            if task == GoOutside or task.kind == '运动类':
                Malnutrition.add(player)
            elif rra(player, 50):
                Malnutrition.add(player)
            

        def afterSleepAction(self, player):
            Malnutrition.add(player)

    class ReadingLimited(Effect):
        id = 297
        name = _('文字疲劳')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 99
        info = _('每层使进行写作类日程时灵感-2，进行非写作类日程时移除该状态。')
        ad = _('如果你不想发霉的话。')

        def afterTaskAction(self, player, task):
            if task.kind != '写作类':
                self.clear(player)
            else:
                Inspiration.subByType(player, self.stacks*2)
                ReadingLimited.add(player)

        @classmethod
        def add(cls, player, times=1):
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                Stat.record(player, cls)
                if CoffeeHQ2.has(player):
                    Notice.add(_('添加%s：%s！{color=#7CFC00}抵消{/color}1层状态：优质咖啡！') % (cls.kind, cls.name))
                    CoffeeHQ2.subByType(player)
                else:
                    cls.defaultAddEffect(player)

    class PhysicalLimited(Effect):
        id = 298
        name = _('肌肉疲劳')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 99
        info = _('每层使运动类日程的专注度降低10%，进行非运动类日程时移除该状态。')
        ad = _('熟悉的肌肉拉伤……')

        def addStackAction(self, player):
            player.sportConcentration -= 10

        def subStackAction(self, player):
            player.sportConcentration += 10

        def afterTaskAction(self, player, task):
            if task.kind != '运动类':
                self.clear(player)
            else:
                PhysicalLimited.add(player)

        @classmethod
        def add(cls, player, times=1):
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                Stat.record(player, cls)
                if BookSportEffect.has(player) and rra(player, 30):
                    return
                else:
                    cls.defaultAddEffect(player)



    class GymLimited(Effect):
        id = 298
        name = _('身体素质获取加成暂时无效')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 1
        info = _('获取身体素质时，身体素质获取加成暂时无效。\n健身日程结束后结束该状态。')
        ad = _('曾经这个疏忽让每个主角都变成了身体素质超过10.0的白袜寸头体育生。')
        hide = True

        def afterTaskAction(self, player, task):
            self.sub(player)
    



    class Stayuplate(Effect):
        id = 299
        name = _('熬夜')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 1
        info = _('专注度{color=#FF4500}降低{/color}40%，精神状态消耗{color=#FF4500}提升{/color}60%，精神状态恢复{color=#FF4500}降低{/color}60%，进行写作时写作进度{color=#FF4500}降低{/color}50%，状态结束时{color=#FF4500}提升{/color}3点严重程度。')
        ad = _('这真的值得么？')

        def enableAction(self, player):
            player.basicConcentration -= 40
            player.basicConsumption += 0.6
            player.basicRecovery -= 0.6

        def disableAction(self, player):
            player.basicConcentration += 40
            player.basicConsumption -= 0.6
            player.basicRecovery += 0.6
            player.severity += 0.03

        def afterTaskAction(self, player, task):
            self.sub(player)
    


    class SleepReward(Effect):
        id = 310
        name = _('精神专注')
        kind = _('增益')
        maxDuration = 1
        maxStacks = 99
        info = _('在床上休息或小睡转化睡意后获得。\n每层都会{color=#7CFC00}提升{/color}下一个日程5%的专注度和10%的工作速度，并{color=#7CFC00}降低{/color}5%的精神状态消耗。\n\n{color=#ffff00}存在此增益时，全力工作不会受到过劳惩罚。{/color}')
        ad = _('看来你已经学会如何利用自己的身体了。')

        def addStackAction(self, player):
            player.basicConcentration += 5
            player.workSpeed += 0.1
            player.basicConsumption -= 0.05

        def subStackAction(self, player):
            player.basicConcentration -= 5
            player.workSpeed -= 0.1
            player.basicConsumption += 0.05

        def afterTaskAction(self, player, task):
            self.clear(player)

    class SleepReward_(Effect):
        id = 310
        name = _('精神专注')
        kind = _('增益')
        maxDuration = 1
        maxStacks = 99
        info = _('在床上休息转化睡意后获得。\n每层使完成委托，随笔写作和集中写作提升的严重程度减少15%，进行一次以上日程后移除该效果。')
        ad = _('"痛饮思绪的脓液。"')


    class CommissionReward(Effect):
        id = 311
        name = _('释然')
        kind = _('增益')
        maxDuration = 3
        maxStacks = 1
        info = _('结束委托后获得。\n专注度{color=#7CFC00}提升{/color}25%，精神状态恢复{color=#7CFC00}提升{/color}25%。')
        ad = _('我写爽了。')

        def enableAction(self, player):
            player.basicConcentration += 25
            player.basicRecovery += 0.25

        def disableAction(self, player):
            player.basicConcentration -= 25
            player.basicRecovery -= 0.25


    class WorkReward(Effect):
        id = 312
        name = _('成就感')
        kind = _('增益')
        maxDuration = 7
        maxStacks = 1
        info = _('完成本周全部工作时有75%的概率获得，超额完成工作时（>120%）必定获得。\n工作速度{color=#7CFC00}提升{/color}20%。')
        ad = _('从虚幻的数据中获得虚假的感动。')

        def enableAction(self, player):
            self.duration = ra(player, 4, 7)
            player.workSpeed += 0.2

        def disableAction(self, player):
            player.workSpeed -= 0.2


    


    class CleanReward(Effect):
        id = 314
        name = _('整洁的房间')
        kind = _('增益')
        maxDuration = 18
        maxStacks = 1
        info = _('进行整理房间日程后获得。\n{color=#7CFC00}降低{/color}10%睡眠消耗的精神状态，进行阅读相关日程时额外{color=#7CFC00}获得{/color}1层灵感，进行写作相关日程时{color=#7CFC00}降低{/color}2点严重程度，进行在家工作日程时，不会获得过劳和焦虑，同时完成的工作进度{color=#7CFC00}提升{/color}50%。\n进行以上日程时，有50%的概率减少1天状态的持续时间。')
        ad = _('久违的大扫除让你从仪式感中获得些许慰藉，同时也为你在家中的行动带来了便利。')

        def afterTaskAction(self, player, task):  # 日程后
            if HotelBuff.has(player):
                return
            if CafeBuff.has(player):
                return
            if BookstoreBuff.has(player):
                return
            if task in (DefaultRead, SentimentalRead, TraditionalRead, ReadingBook):
                Inspiration.add(player, 1)
                if rra(player, 50):
                    self.duration = max(self.duration-1, 1)
            elif task in (FreewheelingWriting, NormalWriting, FocusWriting, WriteDownInspiration):
                player.gain_abi(-0.02, 'sev')
                if rra(player, 50):
                    self.duration = max(self.duration-1, 1)
            elif task == OvertimeWork:
                if rra(player, 50):
                    self.duration = max(self.duration-1, 1)

        def enableAction(self, player):
            self.duration = ra(player, 10, 18)
            player.deteriorateConsumption -= 0.1

        def disableAction(self, player):
            player.deteriorateConsumption += 0.1


    class ReadReward(Effect):
        id = 315
        name = _('领悟')
        kind = _('增益')
        maxDuration = 3
        maxStacks = 1
        info = _('阅读部分书籍或进行除完成委托外的写作类日程后获得。\n写作技巧暂时{color=#7CFC00}提升{/color}10%，进行写作时，{color=#7CFC00}提升{/color}20%的写作价值度。')
        ad = _('如此如此……这般这般……这写法用进我的下一篇随笔里绝对出色……！')

        def enableAction(self, player):
            player.writeValuable += 0.2
            player.writingRegarded += 0.1

        def disableAction(self, player):
            player.writeValuable -= 0.2
            player.writingRegarded -= 0.1


    class FocusAttention(Effect):
        id = 316
        name = _('心流')
        kind = _('增益')
        maxDuration = 1
        maxStacks = 2
        info = _('进行日程将消耗1层本状态，使本次日程的专注度{color=#7CFC00}提升{/color}60%。')
        ad = _('你从未像如此一样渴望做好一件事。')

        def enableAction(self, player):
            player.basicConcentration += 60

        def disableAction(self, player):
            player.basicConcentration -= 60

        def afterTaskAction(self, player, task):
            self.sub(player)


    class Novelty(Effect):
        id = 317
        name = _('见闻')
        kind = _('增益')
        maxDuration = 3
        maxStacks = 1
        info = _('外出探索后有50%的概率获得。\n写作技巧暂时{color=#7CFC00}提升{/color}10%。')
        ad = _('才不是出去玩呢！这叫采风！')

        def enableAction(self, player):
            player.writingRegarded += 0.1

        def disableAction(self, player):
            player.writingRegarded -= 0.1


    class CoffeeHQ(Effect):
        id = 318
        name = _('优质咖啡')
        kind = _('增益')
        maxDuration = 1
        maxStacks = 1
        info = _('工作速度和工作能力各{color=#7CFC00}提升{/color}10%。')
        ad = _('打工人自费提升自己的工作能力……')

        def enableAction(self, player):
            player.workSpeed += 0.1
            player.workingRegarded += 0.1

        def disableAction(self, player):
            player.workSpeed -= 0.1
            player.workingRegarded -= 0.1

    class CoffeeHQ2(Effect):
        id = 318
        name = _('优质咖啡')
        kind = _('增益')
        maxDuration = 1
        maxStacks = 1
        info = _('专注度提升{color=#7CFC00}提升{/color}10%，能够{color=#7CFC00}抵消{/color}1层文字疲劳。')
        ad = _('饮用咖啡应是品尝它的风味，不应该只是为了提神……')

        def enableAction(self, player):
            player.basicConcentration += 0.1

        def disableAction(self, player):
            player.basicConcentration -= 0.1

        @classmethod
        def add(cls, player, times=1):
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                Stat.record(player, cls)
                if ReadingLimited.has(player):
                    Notice.add(_('添加%s：%s！{color=#7CFC00}抵消{/color}1层状态：文字疲劳！') % (cls.kind, cls.name))
                    ReadingLimited.subByType(player)
                else:
                    cls.defaultAddEffect(player)
                    
    
    class ChewingGumEffect(Effect):
        id = 320
        name = _('清新口气')
        kind = _('增益')
        maxDuration = 1
        maxStacks = 1
        info = ''
        ad = '然而并不会有人和你接吻，甚至没人关心你嘴里有什么味道。'
        flavors = ['薄荷味','柑橘味','青柠味','桃子味','草莓味','葡萄味']

        def __init__(self):
            Effect.__init__(self)
            self.flavor = '薄荷味'

        def getPrincipalInfo(self):


            if self.flavor == '薄荷味':
                return '\n当前口味：{color=#b9ffa3}薄荷味{/color}\n工作类日程专注度+10%'
            if self.flavor == '柑橘味':
                return '\n当前口味：{color=#ffdd1f}柑橘味{/color}\n运动类日程专注度+10%'
            if self.flavor == '青柠味':
                return '\n当前口味：{color=#00ff62}青柠味{/color}\n写作类日程专注度+10%'
            if self.flavor == '桃子味':
                return '\n当前口味：{color=#ff79b7}桃子味{/color}\n精神状态恢复+10%'
            if self.flavor == '草莓味':
                return '\n当前口味：{color=#ff0000}草莓味{/color}\n精神状态消耗-10%'
            if self.flavor == '葡萄味':
                return '\n当前口味：{color=#9900ff}葡萄味{/color}\n睡眠消耗-10%'


        def enableAction(self, player):
            self.flavor = rcs(player, self.flavors)

            if self.flavor == '薄荷味':
                player.workConcentration += 10
            elif self.flavor == '柑橘味':
                player.sportConcentration += 10
            elif self.flavor == '青柠味':
                player.writeConcentration += 10
            elif self.flavor == '桃子味':
                player.basicRecovery += 0.1
            elif self.flavor == '草莓味':
                player.basicConsumption -= 0.1
            elif self.flavor == '葡萄味':
                player.deteriorateConsumption -= 0.1

        def disableAction(self, player):

            if self.flavor == '薄荷味':
                player.workConcentration -= 10
            elif self.flavor == '柑橘味':
                player.sportConcentration -= 10
            elif self.flavor == '青柠味':
                player.writeConcentration -= 10
            elif self.flavor == '桃子味':
                player.basicRecovery -= 0.1
            elif self.flavor == '草莓味':
                player.basicConsumption += 0.1
            elif self.flavor == '葡萄味':
                player.deteriorateConsumption += 0.1
    
    class WarmupEffect(Effect):
        id = 321
        name = _('准备运动')
        kind = _('增益')
        maxDuration = 1
        maxStacks = 1
        info = _('对运动类日程的专注度{color=#7CFC00}提升{/color}40%。\n健身日程结束后结束该状态。')
        ad = _('“有备而无患。”')

        def enableAction(self, player):  # 每次添加层数的操作，一般是某些根据层数给予效果的Effect需要设置
            player.sportConcentration += 40

        def disableAction(self, player):  # 减少层数的操作，前者的反向函数
            player.sportConcentration -= 40

        def afterTaskAction(self, player, task):
            self.sub(player)

    class Entrance(Effect):
        id = 322
        name = _('清醒')
        kind = _('增益')
        maxDuration = 1
        maxStacks = 4
        info = _('{color=#7CFC00}提升{/color}40%的专注度，同时每层都会{color=#7CFC00}降低{/color}10%的严重程度。\n进行任意日程后有33%的概率消耗该增益，结束时获得难耐。')
        ad = _('烟草让能让痛苦消弭。')

        def enableAction(self, player):
            player.basicConcentration += 40
            Entrance_1.add(player, Smoking.getstack(player))

        def disableAction(self, player):
            player.basicConcentration -= 40
            Smoking.add(player)
            Entrance_1.clearByType(player)

        def addStackAction(self, player):
            player.severityRegarded -= 0.1

        def subStackAction(self, player):
            player.severityRegarded += 0.1

        def afterTaskAction(self, player, task):
            if rra(player, 33):
                self.clear(player)

    class Entrance_1(Effect):
        id = 322
        name = _('Entrance_1')
        kind = _('增益')
        maxDuration = 1
        maxStacks = 5
        info = _('')
        ad = _('')
        hide = True

        def addStackAction(self, player):
            player.severityRegarded -= 0.1

        def subStackAction(self, player):
            player.severityRegarded += 0.1

    class Relaxation(Effect):
        id = 323
        name = _('松弛')
        kind = _('增益')
        maxDuration = 2
        maxStacks = 1
        info = _('在床上休息或外出获得。\n拥有此状态时，你可以{color=#fde827}速读{/color}一本专业类书籍。\n持续时间结束时，降低2点严重程度。\n\n{color=#fde827}速读：可以在道具栏中直接阅读书籍而不需要进行阅读书籍的日程。{/color}')
        ad = _('“你突然想学习，这倒是很稀有。”')

        def timeUpAction(self, player):
            player.gain_abi(-0.02, 'sev', due='松弛')

    class Freshness(Effect):
        id = 324
        name = _('新鲜感')
        kind = _('增益')
        maxDuration = 2
        maxStacks = 1
        info = _('购买新的书籍时获得。\n拥有此状态时，你可以{color=#fde827}速读{/color}一本非专业类的书籍。\n持续时间结束时，降低2点严重程度。\n\n{color=#fde827}速读：可以在道具栏中直接阅读书籍而不需要进行阅读书籍的日程。{/color}')
        ad = _('“你想看看有什么新的有趣的东西。”')
        
        def timeUpAction(self, player):
            player.gain_abi(-0.02, 'sev', due='新鲜感')

    class SwimEffect(Effect):
        id = 325
        name = _('活力')
        kind = _('增益')
        maxDuration = 7
        maxStacks = 1
        info = _('对运动类日程的专注度{color=#7CFC00}提升{/color}15%。状态结束时，永久{color=#7CFC00}获得{/color}5%的运动类日程专注度和2%的身体素质倍率。\n\n{color=#fde827}无法与其他文体中心给予的效果共存。\n（活力、沉静、触动）{/color}')
        ad = _('“我学到的第一件事便是呼吸。”')

        def enableAction(self, player):  # 每次添加层数的操作，一般是某些根据层数给予效果的Effect需要设置
            MuseumEffect.clearByType(player)
            MovieEffect.clearByType(player)
            player.sportConcentration += 15

        def disableAction(self, player):  # 减少层数的操作，前者的反向函数
            player.sportConcentration -= 15

        def timeUpAction(self, player):
            player.sportConcentration += 5
            player.physicalRegarded += 0.02
    
    class MuseumEffect(Effect):
        id = 326
        name = _('沉静')
        kind = _('增益')
        maxDuration = 7
        maxStacks = 1
        info = _('对工作类日程的专注度{color=#7CFC00}提升{/color}15%。状态结束时，永久{color=#7CFC00}获得{/color}5%的工作类日程专注度和2%的工作能力倍率。\n\n{color=#fde827}无法与其他文体中心给予的效果共存。\n（活力、沉静、触动）{/color}')
        ad = _('“我就在这里，同无所不知的你。”')

        def enableAction(self, player):  # 每次添加层数的操作，一般是某些根据层数给予效果的Effect需要设置
            SwimEffect.clearByType(player)
            MovieEffect.clearByType(player)
            player.workConcentration += 15

        def disableAction(self, player):  # 减少层数的操作，前者的反向函数
            player.workConcentration -= 15

        def timeUpAction(self, player):
            player.workConcentration += 5
            player.workingRegarded += 0.02


    class MovieEffect(Effect):
        id = 327
        name = _('触动')
        kind = _('增益')
        maxDuration = 7
        maxStacks = 1
        info = _('对写作类日程的专注度{color=#7CFC00}提升{/color}15%。状态结束时，永久{color=#7CFC00}获得{/color}5%的写作类日程专注度和2%的写作技巧倍率。\n\n{color=#fde827}无法与其他文体中心给予的效果共存。\n（活力、沉静、触动）{/color}')
        ad = _('“我知道尸体都会腐烂，但你的灵魂与精神将去往何处？”')

        def enableAction(self, player):  # 每次添加层数的操作，一般是某些根据层数给予效果的Effect需要设置
            MuseumEffect.clearByType(player)
            SwimEffect.clearByType(player)
            player.writeConcentration += 15

        def disableAction(self, player):  # 减少层数的操作，前者的反向函数
            player.writeConcentration -= 15

        def timeUpAction(self, player):
            player.writeConcentration += 5
            player.writingRegarded += 0.02



    class SpecialInspiration(Effect):
        id = 328
        name = _('独特灵感')
        kind = _('增益')
        maxDuration = -1
        maxStacks = 99
        info = _('每层在获得时提供少量精神状态并降低严重程度，并在下一次委托写作时{color=#7CFC00}提高{/color}5%这次写作的写作技巧，或是{color=#7CFC00}提高{/color}5%随笔写作获得的粉丝量。')
        ad = _('“如此你的心绪也能存活千年……”')

        def addStackAction(self, player):
            player.gain_mental(r2(10*Task.getRecoScale(player)*f()), due=self.name)
            player.gain_abi(-0.02, 'sev', due='独特灵感')

    class WriterBuff(Effect):
        id = 329
        name = _('舒缓')
        kind = _('增益')
        maxDuration = 3
        maxStacks = 1
        info = _('严重程度和睡眠消耗的精神状态{color=#7CFC00}降低{/color}10%。')
        ad = _('“醒醒，我们还没完呢。”')

        def enableAction(self, player):
            player.severityRegarded -= 0.1
            player.deteriorateConsumption -= 0.1

        def disableAction(self, player):
            player.severityRegarded += 0.1
            player.deteriorateConsumption += 0.1

    
    class WriterBuff2(Effect):
        id = 330
        name = _('新回忆')
        kind = _('增益')
        maxDuration = 3
        maxStacks = 1
        info = _('进行撰写小说日程时，移除该增益并使消耗的精神状态变为恢复。')
        ad = _('“我注视着你的脸庞。”')


    class HotelBuff(Effect):
        id = 331
        name = _('位置：宾馆')  # 可以睡觉
        kind = _('增益')
        maxDuration = 2
        maxStacks = 1
        info = _('在宾馆休息获得，视为在家。\n{color=#7CFC00}降低{/color}50%睡眠消耗的精神状态，{color=#7CFC00}提升{/color}50%在床上休息的恢复效果。\n\n“整洁的房间”在该增益存在时不会生效。')
        ad = _('一副柔软的床，细腻的床单和厚实的被子，我还能奢求什么呢。')

        def enableAction(self, player):
            player.deteriorateConsumption -= 0.5
            player.sleepRecovery += 0.5

        def disableAction(self, player):
            player.deteriorateConsumption += 0.5
            player.sleepRecovery -= 0.5

    class HotelBuff_(Effect):
        id = 331
        name = _('暂离：宾馆')  # 可以睡觉
        kind = _('增益')
        maxDuration = 1
        maxStacks = 1
        info = _('去往其他位置后获得，暂时无法享受宾馆带来的效果，结束其他效果后重新获得。')
        ad = _('我应该躺在宾馆的大床上……')


    class CafeBuff(Effect):
        id = 332
        name = _('位置：咖啡馆')
        kind = _('增益')
        maxDuration = 1
        maxStacks = 1
        info = _('在咖啡馆办公获得，视为在家。\n{color=#7CFC00}降低{/color}20%工作消耗的精神状态，{color=#7CFC00}提升{/color}20%工作速度，{color=#7CFC00}降低{/color}50%工作获得过劳和焦虑的概率。\n\n“整洁的房间”在该增益存在时不会生效。')
        ad = _('点一杯咖啡，然后抱着笔记本电脑在这里坐一下午。')

        def enableAction(self, player):
            if HotelBuff.has(player):
                HotelBuff_.add(player)
                HotelBuff.clearByType(player)
            player.workConsumption -= 0.2
            player.workSpeed += 0.2

        def disableAction(self, player):
            if HotelBuff_.has(player):
                HotelBuff.add(player)
                HotelBuff_.clearByType(player)
            player.workConsumption += 0.2
            player.workSpeed -= 0.2

    class BookstoreBuff(Effect):
        id = 333
        name = _('位置：书店')
        kind = _('增益')
        maxDuration = 1
        maxStacks = 1
        info = _('在书店阅读区获得，视为在家。\n{color=#7CFC00}提升{/color}20%写作技巧，进行阅读类日程时额外{color=#7CFC00}获得{/color}1~3层灵感，{color=#7CFC00}提升{/color}20%基础恢复效果。阅读书籍的效果{color=#7CFC00}提升{/color}100%。\n\n“整洁的房间”在该增益存在时不会生效。\n\n新鲜感在书店不会起作用。')
        ad = _('那是一条照明不佳的街巷，位于一个景貌不佳的小河弯处。')

        def afterTaskAction(self, player, task):  # 日程后
            if task in (DefaultRead, SentimentalRead, TraditionalRead, ReadingBook):
                Inspiration.add(player, ra(player, 1,3))

        def enableAction(self, player):
            if HotelBuff.has(player):
                HotelBuff_.add(player)
                HotelBuff.clearByType(player)
            player.writingRegarded += 0.2
            player.basicRecovery += 0.2

        def disableAction(self, player):
            if HotelBuff_.has(player):
                HotelBuff.add(player)
                HotelBuff_.clearByType(player)
            player.writingRegarded -= 0.2
            player.basicRecovery -= 0.2

    class ParkBuff(Effect):
        id = 334
        name = _('位置：森林公园')
        kind = _('增益')
        maxDuration = 1
        maxStacks = 1
        info = _('。')
        ad = _('')
        hide = True







    class MaskEffect(Effect):
        id = 390
        name = _('一次性口罩')
        kind = _('增益')
        maxDuration = 1
        maxStacks = 1
        info = _('使用一次性口罩后获得。\n在雾霾天气中抵消雾霾天气的部分负面状态')
        ad = _('这样别人就看不到我的抿起来的嘴了。')

    
    class MeetingReward1(Effect):
        id = 392
        name = _('指导：专注')
        kind = _('增益')
        maxDuration = 7
        maxStacks = 1
        info = _('参与周研讨会后获得。\n对工作类日程的专注度{color=#7CFC00}提升{/color}40%。')
        ad = _('“把你的注意力聚焦于工作上。”')

        def enableAction(self, player):
            self.duration = ra(player, 5, 7)
            player.workConcentration += 40

        def disableAction(self, player):
            player.workConcentration -= 40
    

    class MeetingReward2(Effect):
        id = 393
        name = _('指导：激励')
        kind = _('增益')
        maxDuration = 7
        maxStacks = 1
        info = _('参与周研讨会后获得。\n工作能力{color=#7CFC00}提升{/color}30%。')
        ad = _('“努力！努力！在这个时代不卷的人已经被淘汰了！”')

        def enableAction(self, player):
            self.duration = ra(player, 5, 7)
            player.workingRegarded += 0.3

        def disableAction(self, player):
            player.workingRegarded -= 0.3
    
    class MeetingReward3(Effect):
        id = 394
        name = _('指导：坚实')
        kind = _('增益')
        maxDuration = 7
        maxStacks = 1
        info = _('参与周研讨会后获得。\n进行完成工作日程时，精神状态消耗{color=#7CFC00}降低{/color}30%，同时{color=#7CFC00}提升{/color}15%完成的进度。')
        ad = _('“有些人总在工位睡觉，这是不好的……你们应该……”')

        def enableAction(self, player):
            self.duration = ra(player, 5, 7)
    
    class MeetingReward4(Effect):
        id = 395
        name = _('指导：技巧')
        kind = _('增益')
        maxDuration = 7
        maxStacks = 1
        info = _('参与周研讨会后获得。\n进行小睡日程时，额外{color=#7CFC00}获得{/color}2层精神专注，转化睡意时{color=#7CFC00}恢复{/color}的精神状态翻倍。')
        ad = _('“在工作中你们要学会技巧……”')

        def enableAction(self, player):
            self.duration = ra(player, 5, 7)
    

    class MeetingReward5(Effect):
        id = 396
        name = _('指导：分心')
        kind = _('增益')
        maxDuration = 7
        maxStacks = 1
        info = _('参与周研讨会后获得。\n进行偷懒日程时，消耗的精神状态{color=#FF4500}提升{/color}20%，但是偷懒时的阅读效果提升100%。')
        ad = _('“一心二用还不够，你们必须一心三用！……”')

        def enableAction(self, player):
            self.duration = ra(player, 5, 7)
    
    class MeetingReward6(Effect):
        id = 397
        name = _('指导：积累')
        kind = _('增益')
        maxDuration = 7
        maxStacks = 1
        info = _('参与周研讨会后获得。\n立刻完成20%的工作进度，同时进行偷懒日程时，完成的工作进度{color=#7CFC00}提升{/color}30%。')
        ad = _('“回想起以往的工作内容，来对待新的内容……”')

        def enableAction(self, player):
            self.duration = ra(player, 5, 7)
            player.achievedGoal += r2(player.goal * 0.2)
    
    class MeetingReward7(Effect):
        id = 398
        name = _('指导：压力')
        kind = _('增益')
        maxDuration = 7
        maxStacks = 1
        info = _('参与周研讨会后获得。\n起床时必定{color=#7CFC00}获得{/color}紧迫。')
        ad = _('“这周的工作再完成不了……你们就都给我扫地出门！”')

        def enableAction(self, player):
            self.duration = ra(player, 5, 7)

    class MeetingReward8(Effect):
        id = 399
        name = _('指导：放松')
        kind = _('增益')
        maxDuration = 7
        maxStacks = 1
        info = _('参与周研讨会后获得。\n工作消耗的精神状态{color=#7CFC00}降低{/color}50%。')
        ad = _('“上周的工作完成的还不错，值得表扬……”')

        def enableAction(self, player):
            self.duration = ra(player, 5, 7)
            player.workConsumption -= 0.5

        def disableAction(self, player):
            player.workConsumption += 0.5
            
  

    class Physique(Effect):
        id = 300
        name = _('体魄')
        kind = _('增益')
        maxDuration = -1
        maxStacks = 99
        info = _('由拉伸运动转化酸痛获得。\n起床时{color=#7CFC00}恢复{/color}2.5*层数的精神状态，每层体魄都能提升过夜提升身体素质的概率。\n每层体魄{color=#7CFC00}提升{/color}1%受伤和生病的治愈恢复率，治愈生病或受伤成功时，每3层体魄额外{color=#7CFC00}获得{/color}1点身体素质和{color=#7CFC00}降低{/color}1点严重程度。\n\n每天有2%*体魄层数的概率失去一半。')
        ad = _('你终于可以说自己是有点肌肉的人了。')

        def afterSleepAction(self, player):
            m = r2(2.50* self.stacks * f())

            if HallukeItem1.has(player):
                m *= 1.5

            
            player.gain_mental(m, self.name)

            if rra(player, int(self.stacks*10)):
                player.gain_abi(0.01, 'phy', due='体魄')

            per = 2 * self.stacks
            if HallukeItem1.has(player):
                per *= 0.5

            if rra(player, per):
                s = int(self.stacks/2)
                Notice.add(_('体魄随时间失去了%s层。')%s)
                self.sub(player, s)
                
            


    class FixedInspiration(Effect):
        id = 301
        name = _('写作素材')
        kind = _('增益')
        maxDuration = -1
        maxStacks = 99
        info = _('由记录想法{color=#7CFC00}转化{/color}灵感获得。\n可作为灵感在写作中被消耗。')
        ad = _('不离手的照片、老人开的地铁站、离开、蚂蚁吃掉了骨柄、重新回到地铁站、我也是懦弱的人、亲吻、挣扎。')

        def afterWriting(self, player, scale):
            if scale != 0:  # 当本次写作会返回写作素材时
                self.stacks = int(self.stacks * scale)
                Notice.add(_('获得了%s层写作素材！') % newStacks)
            else:
                self.clear(player)


    # D: dependence
    # W: withdrawal
    # E: effect


    class DrugD(Effect):
        id = 403
        name = _('药物依赖')
        kind = _('药物反应')
        maxDuration = 2
        maxStacks = 99
        info = _('使用任意实验药物后解除。\n持续时间结束后{color=#FF4500}转化{/color}为戒断反应。')
        ad = _('你偶尔会感到有些恶心。')

        def timeUpAction(self, player):
            DrugW.add(player)

        @classmethod
        def defaultAddEffect(cls, player):  # 默认的add函数，禁止重写
            cls.notResetDurationAddEffect(player)
        
        @classmethod
        def add(cls, player, times=1):  # 增加新效果或增加层数
            if GameDifficulty1.has(player) or GameDifficulty2.has(player):
                return
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                Stat.record(player, cls)
                cls.defaultAddEffect(player)




    class DrugW(Effect):
        id = 400
        name = _('戒断反应')
        kind = _('药物反应')
        maxDuration = 2
        maxStacks = 1
        info = _('专注度{color=#FF4500}降低{/color}100%，精神状态消耗{color=#FF4500}提升{/color}100%。\n你需要尽快服用任意实验药物，并且在第二天早上才会恢复。\n持续时间结束{color=#FF4500}转化{/color}为衰退。')
        ad = _('反胃感使你频繁跑去厕所呕吐。')

        def enableAction(self, player):
            player.basicConcentration -= 100
            player.basicConsumption += 1

        def disableAction(self, player):
            player.basicConcentration += 100
            player.basicConsumption -= 1

        def timeUpAction(self, player):
            Deterioration.add(player)

        def afterDrug(self, player):
            self.stacks = 0

        def afterSleepAction(self, player):
            if self.stacks == 0:
                self.clear(player)


    class DrugEA(Effect):
        id = 406
        name = _('药物作用{font=arial.ttf}α{/font}')
        kind = _('药物反应')
        maxDuration = 1
        maxStacks = 1
        info = _('基础专注度{color=#FF4500}降低{/color}？%。')
        ad = _('你看不清太远的东西。')

        def __init__(self):
            Effect.__init__(self)
            self.useweek = 1

        def getPrincipalInfo(self):
            return _('\n基础专注度{color=#FF4500}降低{/color}%s%s。') % (self.useweek*5, '%')

        def enableAction(self, player):
            player.basicConcentration -= 5 * self.useweek

        def disableAction(self, player):
            player.basicConcentration += 5 * self.useweek
        
        @classmethod
        def drugEffectAdd(cls, player):  # 默认的add函数，禁止重写
            if not cls.has(player):
                Notice.add(_('获得新%s：%s！') % (cls.kind, cls.name))
                e = cls()
                e.useweek = player.week
                player.effects.append(e)
                e.enableAction(player)

            sortByID(player.effects)
            if all((DrugEA.has(player),DrugEB.has(player),DrugEC.has(player))):
                Achievement304.achieve()
                Achievement.show()

        @classmethod
        def add(cls, player, times=1):  # 增加新效果或增加层数
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                Stat.record(player, cls)
                cls.drugEffectAdd(player)


    class DrugEB(Effect):
        id = 407
        name = _('药物作用{font=arial.ttf}β{/font}')
        kind = _('药物反应')
        maxDuration = 1
        maxStacks = 1
        info = _('睡眠消耗的精神状态{color=#FF4500}提升{/color}？%，写作技巧{color=#7CFC00}提升{/color}？%。')
        ad = _('你开始出现光怪陆离的幻觉。')

        def __init__(self):
            Effect.__init__(self)
            self.useweek = 1
            
        def getPrincipalInfo(self):
            return _('\n睡眠消耗的精神状态{color=#FF4500}提升{/color}%s%s，写作技巧{color=#7CFC00}提升{/color}%s%s。') % (self.useweek*2, '%', self.useweek*2, '%')

        def enableAction(self, player):
            player.deteriorateConsumption += 0.02 * self.useweek
            player.writingRegarded += 0.02 * self.useweek

        def disableAction(self, player):
            player.deteriorateConsumption -= 0.02 * self.useweek
            player.writingRegarded -= 0.02 * self.useweek

        @classmethod
        def drugEffectAdd(cls, player):  # 默认的add函数，禁止重写
            if not cls.has(player):
                Notice.add(_('获得新%s：%s！') % (cls.kind, cls.name))
                e = cls()
                e.useweek = player.week
                player.effects.append(e)
                e.enableAction(player)

            sortByID(player.effects)
            if all((DrugEA.has(player),DrugEB.has(player),DrugEC.has(player))):
                Achievement304.achieve()
                Achievement.show()

        @classmethod
        def add(cls, player, times=1):  # 增加新效果或增加层数
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                Stat.record(player, cls)
                cls.drugEffectAdd(player)


    class DrugEC(Effect):
        id = 408
        name = _('药物作用{font=arial.ttf}γ{/font}')
        kind = _('药物反应')
        maxDuration = 1
        maxStacks = 1
        info = _('每个日程结束后{color=#7CFC00}恢复{/color}？~？*基础精神状态消耗的精神状态，但食物恢复的精神状态{color=#FF4500}降低{/color}？%，服用药物的精神状态恢复效果{color=#FF4500}降低{/color}？%。')
        ad = _('你的味觉突然消失了。')

        def __init__(self):
            Effect.__init__(self)
            self.useweek = 1

        def enableAction(self, player):
            player.foodRecovery -= 0.1 * self.useweek
            player.drugRecovery -= 0.05 * self.useweek

        def disableAction(self, player):
            player.foodRecovery += 0.1 * self.useweek
            player.drugRecovery += 0.05 * self.useweek

        def getPrincipalInfo(self):
            return _('\n每个日程结束后{color=#7CFC00}恢复{/color}%s~%s*基础精神状态消耗的精神状态，但食物恢复的精神状态{color=#FF4500}降低{/color}%s%s，服用药物的精神状态恢复效果{color=#FF4500}降低{/color}%s%s。') % (4*self.useweek, 5*self.useweek, self.useweek*10, '%', self.useweek*5, '%')
            

        def afterTaskAction(self, player, task):
            t = ra(player, 400, 500) * 0.01 * self.useweek
            t *= MedicineC.getResScale(player)
            t *= Task.getConsScale(player)
            player.gain_mental(r2(t), self.name)

        @classmethod
        def drugEffectAdd(cls, player):  # 默认的add函数，禁止重写
            if not cls.has(player):
                Notice.add(_('获得新%s：%s！') % (cls.kind, cls.name))
                e = cls()
                e.useweek = player.week
                player.effects.append(e)
                e.enableAction(player)

            sortByID(player.effects)
            if all((DrugEA.has(player),DrugEB.has(player),DrugEC.has(player))):
                Achievement304.achieve()
                Achievement.show()

        @classmethod
        def add(cls, player, times=1):  # 增加新效果或增加层数
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                Stat.record(player, cls)
                cls.drugEffectAdd(player)


    class DrugED(Effect):
        id = 409
        name = _('药物作用{font=arial.ttf}δ{/font}')
        kind = _('药物反应')
        maxDuration = 7
        maxStacks = 1
        info = _('不会出现其他药物的依赖反应。')
        ad = _('似乎没有任何头疼的感觉了，未知的躁动和其他药物的微弱反应也消失了。')


    class DrugHypnoticEffect(Effect):
        id = 410
        name = _('药物作用：安眠药')
        kind = _('药物反应')
        maxDuration = 1
        maxStacks = 5
        info = _('{color=#7CFC00}降低{/color}20%睡眠消耗的精神状态，{color=#FF4500}降低{/color}50%的专注度。')
        ad = _('昏昏欲睡？也许吧。')

        def enableAction(self, player):
            player.deteriorateConsumption -= 0.2
            player.basicConcentration -= 50

        def disableAction(self, player):
            player.deteriorateConsumption += 0.2
            player.basicConcentration += 50

            


    class DrugIbuprofenEffect(Effect):
        id = 411
        name = _('药物作用：头疼药')
        kind = _('药物反应')
        maxDuration = 2
        maxStacks = 5
        info = _('完成日程后，每层都会{color=#7CFC00}恢复{/color}2%的当前精神状态，最大每层恢复5点。\n精神状态低于0时无效。')
        ad = _('食之无味，弃之可惜。\n有没有人算过到底是维持这东西的药物浓度更加划算还是用等量的钱去买正经的药来吃更划算？')

        def afterTaskAction(self, player, task):
            t = r2(0.02 * player.mental)
            if t > 5:
                t = 5.0
            elif t<0:
                t = 0
            if t>0:
                player.gain_mental(t* self.stacks, '头疼药')

    class DrugIbuprofenBEffect(Effect):
        id = 411
        name = _('药物作用：镇痛药')
        kind = _('药物反应')
        maxDuration = 1
        maxStacks = 1
        info = _('过夜不会消耗精神状态。')
        ad = _('我得到了满足，我再也不会奢求他物。')

        def getPrincipalInfo(self):
            showinfo = self.info
            showinfo += '\n\n下次使用时提升严重倍率：{color=#f00}%s%s{/color}' % (2**DrugIbuprofenBEffect_.getstack(p),'%')

            feed = '\n' if showinfo != '' else ''
            return feed + showinfo


    class DrugColdrexEffect(Effect):
        id = 412
        name = _('药物作用：感冒药')
        kind = _('药物反应')
        maxDuration = 2
        maxStacks = 5
        info = _('{color=#FF4500}降低{/color}10%的专注度，但每层都会{color=#7CFC00}提高{/color}生病的治疗率，效果结束时若仍在生病则会{color=#FF4500}缩减{/color}2天生病的持续时间。')
        ad = _('持续时间越久代表状态越好，而持续时间即将结束代表着病情将恶化至下一个阶段。')

        def enableAction(self, player):
            player.basicConcentration -= 10

        def addStackAction(self, player):
            if PhysPun.has(player):
                PhysPun.get(player).duration += 1

        def disableAction(self, player):
            player.basicConcentration += 10

        def timeUpAction(self, player):
            if PhysPun.has(player):
                existing = PhysPun.get(player)
                existing.duration = max(existing.duration - 2, 0)

    class DrugAspirinEffect(Effect):
        id = 413
        name = _('药物作用：阿司匹林')
        kind = _('药物反应')
        maxDuration = 1
        maxStacks = 1
        info = _('在硬核模式下，使用后使下一个日程消耗的精神状态{color=#7CFC00}减少{/color}75%。') 

        def enableAction(self, player):
            player.basicConsumption -= 0.75

        def disableAction(self, player):
            player.basicConsumption += 0.75

        def afterTaskAction(self, player, task):
            self.sub(player)

    class DrugMethylphenidateEffect(Effect):
        id = 414
        name = _('药物作用：利他林')
        kind = _('药物反应')
        maxDuration = 1
        maxStacks = 1
        info = _('在硬核模式下，工作能力、身体素质和写作技巧{color=#7CFC00}提升{/color}15%，所有基础能力属性的获取加成{color=#7CFC00}提升{/color}1点。效果结束时，{color=#FF4500}降低{/color}30%的专注度。') 

        def enableAction(self, player):
            player.workingRegarded += 0.15
            player.physicalRegarded += 0.15
            player.writingRegarded += 0.15

            player.workingGain += 0.01
            player.physicalGain += 0.01
            player.writingGain += 0.01


        def disableAction(self, player):
            player.workingRegarded -= 0.15
            player.physicalRegarded -= 0.15
            player.writingRegarded -= 0.15

            player.workingGain -= 0.01
            player.physicalGain -= 0.01
            player.writingGain -= 0.01

            DrugMethylphenidateEffect_1.add(player)
    
    class DrugMethylphenidateEffect_1(Effect):
        id = 415
        name = _('副作用：利他林')
        kind = _('药物反应')
        maxDuration = 3
        maxStacks = 5
        info = _('专注度{color=#FF4500}降低{/color}30%。') 

        def addStackAction(self, player):
            player.basicConcentration -= 30
            
        def subStackAction(self, player):
            player.basicConcentration += 30

    


    class BookWriEffect(Effect):
        id = 500
        name = _('学习成果：《于老师教我的写作技巧》')
        kind = _('学识')
        maxDuration = 2
        maxStacks = 1
        info = _('写作技巧暂时{color=#7CFC00}提升{/color}30%。')
        ad = _('于老师到底是谁？写作、摄影、拍电影、做游戏……几乎各个领域都有他出现？')

        def enableAction(self, player):
            player.writingRegarded += 0.3

        def disableAction(self, player):
            player.writingRegarded -= 0.3

    class BookConcEffect(Effect):
        id = 501
        name = _('学习成果：《海边的于秀爱》')
        kind = _('学识')
        maxDuration = 2
        maxStacks = 1
        info = _('生效时，不会获得焦虑和过劳。')

        def enableAction(self, player):
            PhysProb.clearByType(player)
            MentProb.clearByType(player)

    class BookPhysPunEffect(Effect):
        id = 502
        name = _('学习成果：《呼吸训练》')
        kind = _('学识')
        maxDuration = 2
        maxStacks = 1
        info = _('{color=#7CFC00}提升{/color}15%生病和受伤的恢复率。\n如果成功治愈生病或受伤，则结束效果并{color=#7CFC00}降低{/color}2%的严重程度。')

    class BookQuickReadEffect(Effect):
        id = 503
        name = _('学习成果：《量子波动速读》')
        kind = _('学识')
        maxDuration = 2
        maxStacks = 4
        info = _('你可以消耗1层此状态来{color=#fde827}速读{/color}一本任意书籍。\n\n{color=#fde827}速读：可以在道具栏中直接阅读书籍而不需要进行阅读书籍的日程。{/color}')



    class BookWorEffect(Effect):
        id = 504
        name = _('学习成果：《保持清醒的秘诀》')
        kind = _('学识')
        maxDuration = 3
        maxStacks = 1
        info = _('{color=#7CFC00}提升{/color}20%的工作速度，{color=#7CFC00}降低{/color}20%工作类日程消耗的精神状态，进行工作类日程时，额外{color=#7CFC00}完成{/color}5%的当周工作量。')

        def enableAction(self, player):
            player.workSpeed += 0.2
            player.workConsumption -= 0.2

        def subStackAction(self, player):
            player.workSpeed -= 0.2
            player.workConsumption -= 0.2

        def afterTaskAction(self, player, task):  # 日程后
            if task.kind == _('工作类'):
                player.achievedGoal += r2(player.goal * 0.05)


    class BookInsEffect(Effect):
        id = 505
        name = _('感悟：《2001年的弹珠机》')
        kind = _('学识')
        maxDuration = 1
        maxStacks = 1
        info = _('阅读本书籍后效果持续时间内获得灵感时{color=#7CFC00}翻倍{/color}。')


    class BookSportEffect(Effect):
        id = 506
        name = _('感悟：《阿斯卡隆之春》')
        kind = _('学识')
        maxDuration = 3
        maxStacks = 1
        info = _('进行室外运动时不会获得坏结果，且额外{color=#7CFC00}获得{/color}2层酸痛，并还有25%的概率{color=#7CFC00}获得{/color}1层体魄。')

        def afterTaskAction(self, player, task):  # 日程后
            if task in (DefaultSport, JoggingSport, FastrunSport) and rra(player, 25):
                Physique.add(player)
        

    class BookWriteEffect(Effect):
        id = 507
        name = _('感悟：《亚斯塔禄之冬》')
        kind = _('学识')
        maxDuration = 7
        maxStacks = 1
        info = _('进行读流行小说，读感伤文学或读传统文学日程时会给予你独特灵感，在获得时{color=#7CFC00}恢复{/color}少量精神状态并{color=#7CFC00}降低{/color}严重程度，并在下一次委托写作时{color=#7CFC00}提高{/color}这次写作的写作技巧，或是{color=#7CFC00}提高{/color}随笔写作获得的粉丝量。')

        def afterTaskAction(self, player, task):  # 日程后
            if task in (DefaultRead, SentimentalRead, TraditionalRead):
                SpecialInspiration.add(player)
        

    class AMaverickLionEffect(Effect):
        id = 508
        name = _('感悟：《一只特立独行的狮子》')
        kind = _('学识')
        maxDuration = 7
        maxStacks = 1
        info = _('效果消失时使精神状态变为记录的数值，当效果消失时或因精神状态过低即将崩溃时，使精神状态{color=#7CFC00}提升{/color}至记录的数值。')

        def __init__(self):
            Effect.__init__(self)
            self.m = 100

        def getPrincipalInfo(self):
            showinfo = self.info
            showinfo += '\n\n记录的精神状态：%s' % self.m

            feed = '\n' if showinfo != '' else ''
            return feed + showinfo

        def timeUpAction(self, player):
            player.mental = self.m

        def enableAction(self, player):
            self.m = player.mental


    class BookCMEffect(Effect):
        id = 509
        name = _('学识：《快速入睡秘籍》')
        kind = _('学识')
        maxDuration = 14
        maxStacks = 1
        info = _('{color=#7CFC00}降低{/color}20%过夜消耗的精神状态，并在起床时{color=#7CFC00}降低{/color}1点严重程度，同时有10%的概率结束该效果。')
        
        def enableAction(self, player):
            player.deteriorateConsumption -= 0.2

        def disableAction(self, player):
            player.deteriorateConsumption += 0.2

        def afterSleepAction(self, player):
            player.gain_abi(-0.01, 'sev', due=self.name)
            if rra(player, 10) and self.duration <=7:
                self.clear(player)
                Notice.add(self.name + _('的效果结束了。'))


    class BookMEDEffect(Effect):
        id = 510
        name = _('学识：《实用百科全书》')
        kind = _('学识')
        maxDuration = 4
        maxStacks = 1
        info = _('进行日程时{color=#7CFC00}提升{/color}随机属性，同时有10%的概率结束该效果。')

        def __init__(self):
            Effect.__init__(self)
            self.times = 0

        def afterTaskAction(self, player, task):  # 日程后
            used = False
            phy = 0
            wri = 0
            wor = 0
            while rra(player, 60) or not used:
                if rra(player, 33):
                    phy += 1
                    used = True
                if rra(player, 33):
                    wri += 1
                    used = True
                if rra(player, 33):
                    wor += 1
                    used = True
            if phy > 0:
                player.gain_abi(phy * 0.01, 'phy', due='学识：《实用百科全书》', extra=True)
            if wri > 0:
                player.gain_abi(wri * 0.01, 'wri', due='学识：《实用百科全书》', extra=True)
            if wor > 0 and not player.experience == 'wri':
                player.gain_abi(wor * 0.01, 'wor', due='学识：《实用百科全书》', extra=True)
            if rra(player, 20) and self.times>3:
                self.clear(player)
                Notice.add(self.name + _('的效果结束了。'))


    class BookSevUpEffect(Effect):
        id = 511
        name = _('感悟：《热病》')
        kind = _('学识')
        maxDuration = 2
        maxStacks = 1
        info = _('暂时{color=#FF4500}提升{/color}10%的严重程度。')

        def enableAction(self, player):
            player.severityRegarded += 0.1

        def disableAction(self, player):
            player.severityRegarded -= 0.1


    class BookUndeadEffect(Effect):
        id = 512
        name = _('感悟：《国境以北星空以南》')
        kind = _('学识')
        maxDuration = 3
        maxStacks = 1
        info = _('精神状态不会低于10，但专注度{color=#FF4500}降低{/color}20%。')

        def enableAction(self, player):
            player.basicConcentration -= 20

        def disableAction(self, player):
            player.basicConcentration += 20
        
    class BookRandConcEffect(Effect):
        id = 513
        name = _('感悟：《寻羊历险记》')
        kind = _('学识')
        maxDuration = 7
        maxStacks = 99
        info = _('在完成日程前会显示日程的完成结果，你可以消耗1层该效果以优势重新投掷完成结果。\n\n{color=#fde827}（优势：进行两次判定取最高值。）{/color}')


    class BookRandConcEffect_1(Effect):
        id = 9999
        name = _('已移除的状态')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 1
        info = _('该状态已被移除。')

    
    class BookHealEffect_1(Effect):
        id = 515
        name = _('感悟：《神，我们，或所有的士兵》')
        kind = _('学识')
        maxDuration = 2
        maxStacks = 1
        info = _('工作能力，身体素质，写作能力{color=#FF4500}降低{/color}30%。')

        def enableAction(self, player):
            player.workingRegarded -= 0.3
            player.physicalRegarded -= 0.3
            player.writingRegarded -= 0.3

        def disableAction(self, player):
            player.workingRegarded += 0.3
            player.physicalRegarded += 0.3
            player.writingRegarded += 0.3

            BookHealEffect_2.add(player)

    class BookHealEffect_2(Effect):
        id = 516
        name = _('提升：《神，我们，或所有的士兵》')
        kind = _('学识')
        maxDuration = 2
        maxStacks = 1
        info = _('工作能力，身体素质，写作能力{color=#7CFC00}提升{/color}30%。')

        def enableAction(self, player):
            player.workingRegarded += 0.3
            player.physicalRegarded += 0.3
            player.writingRegarded += 0.3

        def disableAction(self, player):
            player.workingRegarded -= 0.3
            player.physicalRegarded -= 0.3
            player.writingRegarded -= 0.3



    class GameDifficulty1(Effect):
        id = 600
        name = _('病情良好')
        kind = _('伤痕')
        maxDuration = -1
        maxStacks = 1
        info = _('{color=#ff9900}游戏难度：旅途{/color}')
        ad = _('“……你到底是真的头疼，还是只是在一直装病？”')

        def enableAction(self, player):
            GameDifficulty2.clearByType(player)
            GameDifficulty3.clearByType(player)
            GameDifficulty4.clearByType(player)
            GameDifficulty5.clearByType(player)



    class GameDifficulty2(Effect):
        id = 600
        name = _('病情好转')
        kind = _('伤痕')
        maxDuration = -1
        maxStacks = 1
        info = _('精神状态消耗{color=#7CFC00}降低{/color}40%。\n精神状态恢复{color=#7CFC00}提升{/color}40%。\n\n{color=#7FFF00}游戏难度：简单{/color}')
        ad = _('“你的病情正在逐渐好转，虽然你还是会偶尔头疼，但也许用不了一阵子你就可以脱离药物的治疗。”')

        def enableAction(self, player):
            GameDifficulty1.clearByType(player)
            GameDifficulty3.clearByType(player)
            GameDifficulty4.clearByType(player)
            GameDifficulty5.clearByType(player)
            player.basicConsumption -= 0.4
            player.basicRecovery += 0.4
            player.workingGain += 0.02
            player.physicalGain += 0.02
            player.writingGain += 0.02

        def disableAction(self, player):
            player.basicConsumption += 0.4
            player.basicRecovery -= 0.4
            player.workingGain -= 0.02
            player.physicalGain -= 0.02
            player.writingGain -= 0.02

        def getPrincipalInfo(self):
            showinfo = self.info
            feed = '\n' if showinfo != '' else ''
            return feed + showinfo + _('\n随时间提升的严重程度倍率：+%s%s')%(p.aggra, '%')

        def afterSleepAction(self, player):
            if rra(player, 30) and player.cured < 0:
                player.severityRegarded += 0.01
                player.aggra += 1

    class GameDifficulty3(Effect):
        id = 601
        name = _('病情较重')
        kind = _('伤痕')
        maxDuration = -1
        maxStacks = 1
        info = _('{color=#87CEEB}游戏难度：一般{/color}')
        ad = _('“你的病情相对严重，不要忘记按时吃药，多锻炼，不过相信你已经习惯这样的生活了吧。”')

        def enableAction(self, player):
            GameDifficulty1.clearByType(player)
            GameDifficulty2.clearByType(player)
            GameDifficulty4.clearByType(player)
            GameDifficulty5.clearByType(player)

        def getPrincipalInfo(self):
            showinfo = self.info

            feed = '\n' if showinfo != '' else ''
            return feed + showinfo + _('\n随时间提升的严重程度倍率：+%s%s')%(p.aggra, '%')
        
        def afterSleepAction(self, player):
            if rra(player, 50) and player.cured < 0:
                player.severityRegarded += 0.01
                player.aggra += 1

    

    class GameDifficulty4(Effect):
        id = 602
        name = _('病情危急')
        kind = _('伤痕')
        maxDuration = -1
        maxStacks = 1
        info = _('精神状态消耗{color=#FF4500}提升{/color}60%。\n精神状态恢复{color=#FF4500}降低{/color}60%。\n睡眠消耗的精神状态{color=#FF4500}提升{/color}60%。\n\n{color=#FF0000}游戏难度：硬核{/color}')
        ad = _('“你是怎么在ICU外还能活到现在的？”')

        def enableAction(self, player):
            GameDifficulty1.clearByType(player)
            GameDifficulty2.clearByType(player)
            GameDifficulty3.clearByType(player)
            GameDifficulty5.clearByType(player)
            player.basicConsumption += 0.6
            player.basicRecovery -= 0.6
            player.deteriorateConsumption += 0.6

        def disableAction(self, player):
            player.basicConsumption -= 0.6
            player.basicRecovery += 0.6
            player.deteriorateConsumption -= 0.6

        def afterTaskAction(self, player, task):
            if not Headache_.has(player) and rra(player, 5) and task not in (Sleep, SnapWork):
                Headache.add(player)

        def getPrincipalInfo(self):
            showinfo = self.info

            feed = '\n' if showinfo != '' else ''
            return feed + showinfo + _('\n随时间提升的严重程度倍率：+%s%s')%(p.aggra, '%')

        def afterSleepAction(self, player):
            if rra(player, 70) and player.cured < 0:
                player.severityRegarded += 0.01
                player.aggra += 1
            


    class GameDifficulty5(Effect):
        id = 603
        name = _('病情急迫')
        kind = _('伤痕')
        maxDuration = -1
        maxStacks = 1
        info = _('精神状态消耗{color=#FF4500}提升{/color}70%。\n精神状态恢复{color=#FF4500}降低{/color}70%。\n睡眠消耗的精神状态{color=#FF4500}提升{/color}70%。\n专注度{color=#FF4500}降低{/color}30%。\n\n{color=#c000da}游戏难度：地狱{/color}')
        ad = _('“你能独自存活便是医学界的悖论。”')

        def enableAction(self, player):
            GameDifficulty1.clearByType(player)
            GameDifficulty2.clearByType(player)
            GameDifficulty3.clearByType(player)
            GameDifficulty4.clearByType(player)            
            player.basicConsumption += 0.7
            player.basicRecovery -= 0.7
            player.deteriorateConsumption += 0.7
            player.basicConcentration -= 30

        def disableAction(self, player):
            player.basicConsumption -= 0.7
            player.basicRecovery += 0.7
            player.deteriorateConsumption -= 0.7
            player.basicConcentration -= 30

        def getPrincipalInfo(self):
            showinfo = self.info

            feed = '\n' if showinfo != '' else ''
            return feed + showinfo + _('\n随时间提升的严重程度倍率：+%s%s')%(p.aggra, '%')


        def afterTaskAction(self, player, task):
            per = ra(player, 1, 8)
            if rra(player, 50):
                per += ra(player, 0, 8)
            if rra(player, 50):
                per += ra(player, 0, 4)
            if player.mental > 150:
                per = ra(player, 15, 20)
            t = abs(r2(player.mental * per * 0.01))
            player.gain_mental(-t)
            if not Headache_.has(player) and rra(player, 10):
                Headache.add(player)

        def afterSleepAction(self, player):
            if rra(player, 33):
                player.gain_abi(-0.01, 'wor', due='病情急迫')
            if rra(player, 33):
                player.gain_abi(-0.01, 'phy', due='病情急迫')
            if rra(player, 33):
                player.gain_abi(-0.01, 'wri', due='病情急迫')
            
            if rra(player, 50) and player.money > 0:
                t = r2(player.money*0.01*f()*ra(player, 1, 10))
                if t > player.money:
                    t = player.money
                player.money -= t
                Notice.add(_('不受控制地花掉了%s元！') % t)
            
            if rra(player, 33) and player.medinfo:
                med = rca(player, player.medinfo.keys())
                player.medinfo[med].res += 1
                Notice.add(_('%s的药物抗性上升了1%s！') % (med.name, '%'))
            
            if rra(player, 90) and player.cured < 0:
                player.severityRegarded += 0.01
                player.aggra += 1

            if Inspiration.has(player):
                Inspiration.subByType(player)

            if Physique.has(player):
                Physique.subByType(player)
            
            

    
    class Despair(Effect):
        id = 610
        name = _('绝望')
        kind = _('伤痕')
        maxDuration = -1
        maxStacks = 99
        info = _('我还能活下去吗？')

        def addStackAction(self, player):
            player.basicConsumption += 0.015

        def subStackAction(self, player):
            player.basicConsumption -= 0.015

        def afterTaskAction(self, player, task):
            t = r2(3 * self.stacks  * f() * player.basicConsumption)
            self.add(player, ra(player, 1, self.stacks))
            player.gain_mental(-t, self.name)

        def afterDrug(self, player):
            self.sub(player, self.stacks-1)


    class LifeIsColorless(Effect):
        id = 611
        name = _('生命失去了色彩')
        kind = _('伤痕')
        maxDuration = -1
        maxStacks = 99
        info = _('活着。')

        def afterSleepAction(self, player):
            self.stacks += 1

    class Debilitated(Effect):
        id = 620
        name = _('体弱')
        kind = _('伤痕')
        maxDuration = -1
        maxStacks = 99
        info = _('每层都会{color=#FF4500}降低{/color}15%的身体素质。\n每层都会{color=#FF4500}降低{/color}10%的药物效果。\n每层都会{color=#FF4500}提升{/color}10%睡眠消耗的精神状态。')
        ad = _('“有些伤口永远不会完全愈合。”')

        def addStackAction(self, player):
            if GameDifficulty1.has(player) or GameDifficulty2.has(player):
                self.duration = 14
            player.physicalRegarded -= 0.15
            player.drugRecovery -= 0.1
            player.deteriorateConsumption += 0.1

        def subStackAction(self, player):
            player.physicalRegarded += 0.15
            player.drugRecovery += 0.1
            player.deteriorateConsumption -= 0.1


    class Decadent(Effect):
        id = 621
        name = _('谵妄')
        kind = _('伤痕')
        maxDuration = -1
        maxStacks = 99
        info = _('每层都会{color=#FF4500}降低{/color}15%的写作技巧。\n每次过夜都会{color=#FF4500}失去{/color}相当于该伤痕层数的灵感。\n完成委托时，委托的价值每层都会{color=#FF4500}降低{/color}10%。')
        ad = _('“我已经悖离了我自己的心。”')

        def addStackAction(self, player):
            if GameDifficulty1.has(player) or GameDifficulty2.has(player):
                self.duration = 14
            player.writingRegarded -= 0.15
            player.writeValuable -= 0.1

        def afterSleepAction(self, player):
            if Inspiration.has(player):
                Inspiration.subByType(player, self.stacks)

        def subStackAction(self, player):
            player.writingRegarded += 0.15
            player.writeValuable += 0.1

    class Deterioration(Effect):
        id = 622
        name = _('衰退')
        kind = _('伤痕')
        maxDuration = -1
        maxStacks = 99
        info = _('每层都会{color=#FF4500}提升{/color}15%的严重程度。')
        ad = _('“对你来说可能有毒，但你还是会喝下去。”')

        def addStackAction(self, player):
            if GameDifficulty1.has(player) or GameDifficulty2.has(player):
                self.duration = 14
            player.severityRegarded += 0.15

        def subStackAction(self, player):
            player.severityRegarded -= 0.15

    class DrugIbuprofenBEffect_(Effect):
        id = 623
        name = _('镇痛药使用次数')
        kind = _('伤痕')
        maxDuration = -1
        maxStacks = 99
        info = _('每层都会{color=#FF4500}提升{/color}镇痛药提升严重倍率的效果。')
        ad = _('如今我已尝过了忤逆的果实，这种饥饿便时常来烦扰我。闻见腐败的芳香我的嘴就流涎水，肚肠像狗一样嚎叫。')
        hide = True
