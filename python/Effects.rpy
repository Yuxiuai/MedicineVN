init python early:

    class WeatherSunny(Effect):
        id = 100
        name = _('{color=#FFD700}晴天{/color}')
        kind = _('天气')
        maxDuration = 1
        maxStacks = 1
        info = _('户外运动会{color=#7CFC00}恢复{/color}更多精神状态，并额外{color=#7CFC00}提升{/color}身体素质。')
        info_p = _('进行外出散步、慢跑、速跑时会{color=#7CFC00}恢复{/color}额外25%的精神状态，并额外{color=#7CFC00}提升{/color}2点身体素质。')
        ad = _('适合室外运动的好天气。')

        def enableAction(self, player):
            for i in (WeatherRainy, WeatherCloudy, WeatherWet, WeatherHot, WeatherThunder, WeatherWindy, WeatherUnknown, WeatherNone, WeatherTornado):
                i.clearByType(player)

            player.outdoorSportRecovery += 0.25

        def disableAction(self, player):
            player.outdoorSportRecovery -= 0.25

        def afterTaskAction(self, player, task):
            if task in (DefaultSport, JoggingSport, FastrunSport):
                Notice.add(_('由于晴天，提升了2点身体素质！'))
                player.physical += 0.02


    class WeatherRainy(Effect):
        id = 101
        name = _('{color=#87CEFA}雨天{/color}')
        kind = _('天气')
        maxDuration = 1
        maxStacks = 1
        info = _('进行写作类日程或在床上休息会{color=#7CFC00}恢复{/color}更多的精神状态，且会额外{color=#7CFC00}降低{/color}严重程度。\n外卖价格会小幅度提升。\n\n{color=FF0000}无法进行室外跑步。{/color}')
        info_p = _('进行写作类日程或在床上休息会{color=#7CFC00}恢复{/color}额外25%的精神状态，且会额外{color=#7CFC00}降低{/color}2点严重程度。\n外卖价格提升20%。\n\n{color=FF0000}无法进行室外跑步。{/color}')
        ad = _('适合宅家的好天气。')

        def enableAction(self, player):
            for i in (WeatherSunny, WeatherCloudy, WeatherWet, WeatherHot, WeatherThunder, WeatherWindy, WeatherUnknown, WeatherNone, WeatherTornado):
                i.clearByType(player)

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
                Notice.add(_('由于雨天，降低了2点严重程度！'))
                player.severity -= 0.02


    class WeatherCloudy(Effect):
        id = 102
        name = _('{color=#B0C4DE}多云{/color}')
        kind = _('天气')
        maxDuration = 1
        maxStacks = 1
        info = _('工作类日程的专注度{color=#FF4500}降低{/color}，{color=#7CFC00}提升{/color}生病和受伤的恢复率。')
        info_p = _('工作类日程的专注度{color=#FF4500}降低{/color}15%，{color=#7CFC00}提升{/color}20%生病和受伤的恢复率。')
        ad = _('阴沉的天气让你犯困，你总是忍不住打哈欠。')

        def enableAction(self, player):
            for i in (WeatherSunny, WeatherRainy, WeatherWet, WeatherHot, WeatherThunder, WeatherWindy, WeatherUnknown, WeatherNone, WeatherTornado):
                i.clearByType(player)

            player.workConcentration -= 15

        def disableAction(self, player):
            player.workConcentration += 15


    class WeatherHot(Effect):
        id = 103
        name = _('{color=#FF4500}酷热{/color}')
        kind = _('天气')
        maxDuration = 1
        maxStacks = 1
        info = _('身体素质暂时小幅度{color=#FF4500}降低{/color}，运动类日程恢复的精神状态和专注度{color=#FF4500}降低{/color}，且进行后将额外{color=#FF4500}提升{/color}严重程度。')
        info_p = _('身体素质暂时{color=#FF4500}降低{/color}5%，运动类日程恢复的精神状态和专注度{color=#FF4500}降低{/color}20%，且进行后将额外{color=#FF4500}提升{/color}2点严重程度。')
        ad = _('衣服都被汗打湿了啊，也太热了吧！')

        def enableAction(self, player):
            for i in (WeatherSunny, WeatherRainy, WeatherCloudy, WeatherWet, WeatherThunder, WeatherWindy, WeatherUnknown, WeatherNone, WeatherTornado):
                i.clearByType(player)

            player.physicalRegarded -= 0.05
            player.sportConcentration -= 20
            player.sportRecovery -= 0.2

        def disableAction(self, player):
            player.physicalRegarded += 0.05
            player.sportConcentration += 20
            player.sportRecovery += 0.2

        def afterTaskAction(self, player, task):
            if task in (DefaultSport, JoggingSport, FastrunSport):
                player.severity += 0.02


    class WeatherWindy(Effect):
        id = 104
        name = _('{color=#98FB98}刮风{/color}')
        kind = _('天气')
        maxDuration = 1
        maxStacks = 1
        info = _('完成日程后百分比{color=#7CFC00}恢复{/color}少量精神状态。')
        info_p = _('完成日程后{color=#7CFC00}恢复{/color}当前精神状态的5% ~ 15%，最高恢复20点。')
        ad = _('人都要被吹跑了！不过我喜欢这种感觉！')

        def enableAction(self, player):
            for i in (WeatherSunny, WeatherRainy, WeatherCloudy, WeatherWet, WeatherHot, WeatherThunder, WeatherUnknown, WeatherNone, WeatherTornado):
                i.clearByType(player)

        def afterTaskAction(self, player, task):
            rec = r2(player.mental * ra(player, 1050, 1150) * 0.0001)
            if rec > 20:
                rec = 20
            player.mental += rec


    class WeatherWet(Effect):
        id = 105
        name = _('{color=#00FFFF}阴冷{/color}')
        kind = _('天气')
        maxDuration = 1
        maxStacks = 1
        info = _('完成日程后若没有良好的运动则有概率生病，若已经生病则不会再生病。')
        info_p = _('完成日程后若没有良好的运动则有40%的概率生病，若已经生病则不会再生病。')
        ad = _('……我真应该把我那件大衣带到公司……')

        def enableAction(self, player):
            for i in (WeatherSunny, WeatherRainy, WeatherCloudy, WeatherHot, WeatherThunder, WeatherWindy, WeatherUnknown, WeatherNone, WeatherTornado):
                i.clearByType(player)

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
        info = _('睡眠消耗的精神状态{color=#FF4500}提升{/color}。')
        info_p = _('睡眠消耗的精神状态{color=#FF4500}提升{/color}20%。')
        ad = _('我并非是怕打雷的小孩子，但即便是轻微的声响都让我难以入眠……')

        def enableAction(self, player):
            for i in (WeatherSunny, WeatherRainy, WeatherCloudy, WeatherWet, WeatherHot, WeatherWindy, WeatherUnknown, WeatherNone, WeatherTornado):
                i.clearByType(player)

            player.deteriorateConsumption += 0.15

        def disableAction(self, player):
            player.deteriorateConsumption -= 0.15

    class WeatherTornado(Effect):
        id = 107
        name = _('{color=#4682B4}台风{/color}')
        kind = _('天气')
        maxDuration = 2
        maxStacks = 1
        info = _('该天气持续时无需上班，但也无法进行户外运动，也不能外出。\n外卖价格会大幅度提升。')
        info_p = _('该天气持续时无需上班，但也无法进行户外运动，也不能外出。\n外卖价格提升50%。')
        ad = _('以此天气纪念于秀爱两次阳光明媚时出门被突发的大暴雨浇成落汤鸡。')

        def enableAction(self, player):
            for i in (WeatherSunny, WeatherRainy, WeatherCloudy, WeatherWet, WeatherHot, WeatherThunder, WeatherWindy, WeatherUnknown, WeatherNone):
                i.clearByType(player)

            player.canOutdoorSport -= 1
            player.canExplore -= 1
            player.foodPrice += 1

        def disableAction(self, player):
            player.canOutdoorSport += 1
            player.canExplore += 1
            player.foodPrice -= 1


    class WeatherNone(Effect):
        id = 109
        name = _('？？？')
        kind = _('天气')
        maxDuration = 1
        maxStacks = 1
        info = _('？？？？？？？？？？？')
        info_p = _('？？？？？？？？？？？')
        ad = _('在废墟之下，你不知道外界的天气。')

        def enableAction(self, player):
            for i in (WeatherSunny, WeatherRainy, WeatherCloudy, WeatherWet, WeatherHot, WeatherThunder, WeatherWindy, WeatherUnknown, WeatherTornado):
                i.clearByType(player)

    class WeatherUnknown(Effect):
        id = 110
        name = _('未知')
        kind = _('天气')
        maxDuration = 1
        maxStacks = 1
        info = _('你并不关心今天是什么天气。')
        info_p = _('你并不关心今天是什么天气。')

        def enableAction(self, player):
            for i in (WeatherSunny, WeatherRainy, WeatherCloudy, WeatherWet, WeatherHot, WeatherThunder, WeatherWindy, WeatherNone, WeatherTornado):
                i.clearByType(player)


    class Novice(Effect):
        id = 299
        name = _('存在感')
        kind = _('增益')
        maxDuration = 14
        maxStacks = 1
        info = _('持续时间内{color=#7CFC00}降低{/color}严重程度和睡眠消耗的精神状态。\n即将死亡时，{color=#7CFC00}恢复{/color}精神状态至一定值。\n如果没有触发效果，则持续时间结束时{color=#7CFC00}降低{/color}严重程度倍率。')
        info_p = _('持续时间内{color=#7CFC00}降低{/color}10%的严重程度和睡眠消耗的精神状态。\n当起床时精神状态低于单个药物能够恢复至大于0的数值，或已经没有药物且精神状态低于0，则消耗该效果{color=#7CFC00}恢复{/color}精神状态至80。\n如果没有触发效果，则持续时间结束时{color=#7CFC00}降低{/color}2%的严重程度倍率。')
        ad = _('“很想看到渐次泛白的黎明时分的天宇，想喝热气蒸腾的牛奶，想闻树木的清香，想翻晨报的版面。”')

        def timeUpAction(self, player):
            Notice.add(_('存在感持续时间结束，降低了2%的严重程度倍率！'))
            player.severityRegarded -= 0.02

        def enableAction(self, player):
            player.severityRegarded -= 0.1
            player.deteriorateConsumption -= 0.1

        def disableAction(self, player):
            player.severityRegarded += 0.1
            player.deteriorateConsumption += 0.1

        def afterSleepAction(self, player):
            m = 0
            if MedicineA.has(player):
                m = max(MedicineA.expectedReco(player)-5, m)
            if MedicineB.has(player):
                m = max(MedicineB.expectedReco(player)-5, m)
            if MedicineC.has(player):
                m = max(30 * MedicineC.getMedicineScale(player, prev=True)-5, m)
            if player.mental + m <= 0:
                Notice.add(_('移除了状态：存在感，将精神状态恢复至80.0'))
                player.mental = 80.0
                self.clear(player)


    class Erection(Effect):
        id = 201
        name = _('勃起')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 1
        info = _('你的欲望让你的生殖器官充血膨胀。')
        info_p = _('你的欲望让你的生殖器官充血膨胀。')
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
        info_p = _('可以进行随笔写作。')
        ad = _('好想写点什么……')


    class ConsInc(Effect):
        id = 210
        name = _('紧张')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 5
        info = _('精神状态消耗随层数{color=#FF4500}提升{/color}，精神状态恢复随层数{color=#7CFC00}提升{/color}。')
        info_p = _('精神状态消耗每层都会{color=#FF4500}提升{/color}10%，精神状态恢复每层都会{color=#7CFC00}提升{/color}10%。')
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
        info = _('精神状态消耗随层数{color=#7CFC00}降低{/color}，精神状态恢复随层数{color=#FF4500}降低{/color}。')
        info_p = _('精神状态消耗每层都会{color=#7CFC00}降低{/color}10%，精神状态恢复每层都会{color=#FF4500}降低{/color}10%。')
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
        info = _('专注度随层数{color=#FF4500}降低{/color}，睡眠消耗的精神状态随层数{color=#7CFC00}降低{/color}。')
        info_p = _('专注度每层都会{color=#FF4500}降低{/color}10%，睡眠消耗的精神状态每层都会{color=#7CFC00}降低{/color}10%。')
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
        info = _('专注度随层数{color=#7CFC00}提升{/color}，睡眠消耗的精神状态随层数{color=#FF4500}提升{/color}。')
        info_p = _('专注度每层都会{color=#7CFC00}提升{/color}10%，睡眠消耗的精神状态每层都会{color=#FF4500}提升{/color}10%。')
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
        info = _('大幅{color=#7CFC00}提升{/color}工作速度和工作的专注度。')
        info_p = _('工作速度{color=#7CFC00}提升{/color}30%，对工作的专注度{color=#7CFC00}提升{/color}30%。')
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
        maxStacks = 99
        info = _('在床上休息恢复的精神状态大幅{color=#7CFC00}提升{/color}，且必定移除全部的过劳。')
        info_p = _('在床上休息恢复的精神状态{color=#7CFC00}提升{/color}30%，且必定移除全部的过劳。')
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
        maxStacks = 99
        info = _('暂时{color=#FF4500}提升{/color}严重程度。\n状态结束后降低大量严重程度。')
        info_p = _('暂时{color=#FF4500}提升{/color}15%的严重程度。\n状态结束后降低5点严重程度。')
        ad = _('当破除这份来源于存在本身的的恐惧后，迎来的则是存活的希望。')

        def enableAction(self, player):
            player.severityRegarded += 0.15

        def disableAction(self, player):
            player.severityRegarded -= 0.15
            player.severity -= 0.05
            
    

    class Desire(Effect):
        id = 217
        name = _('渴求')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 99
        info = _('精神状态消耗{color=#FF4500}提升{/color}，但所有基础能力属性的获取加成{color=#7CFC00}提升{/color}。')
        info_p = _('精神状态消耗{color=#FF4500}提升{/color}15%，但所有基础能力属性的获取加成{color=#7CFC00}提升{/color}1点。')
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
        maxStacks = 99
        info = _('可以进行随笔写作，写作的价值度{color=#7CFC00}提升{/color}，写作技巧获取加成{color=#7CFC00}提升{/color}。')
        info_p = _('可以进行随笔写作，写作的价值度提升15%，写作技巧获取加成{color=#7CFC00}提升{/color}2点。')
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
        maxStacks = 99
        info = _('每个日程结束后都会获得良好的运动，运动恢复的精神状态大幅度{color=#7CFC00}提升{/color}，运动类日程的专注度{color=#7CFC00}提升{/color}，身体素质获取加成{color=#7CFC00}提升{/color}。')
        info_p = _('每个日程结束后都会获得良好的运动，运动恢复的精神状态{color=#7CFC00}提升{/color}30%，对运动类日程的专注度{color=#7CFC00}提升{/color}20%，身体素质获取加成{color=#7CFC00}提升{/color}2点。')
        ad = _('即便世间还要如此折磨我，但我仍要努力反抗。')

        def enableAction(self, player):
            player.sportRecovery += 0.3
            player.sportConcentration += 20
            player.physicalGain += 0.02

        def disableAction(self, player):
            player.sportRecovery -= 0.3
            player.sportConcentration -= 20
            player.physicalGain -= 0.02

        def afterTaskAction(self, player, task):
            PhysRezB.add(player)


    class PhysPun(Effect):
        id = 220
        name = _('生病')
        kind = _('状态')
        maxDuration = 7
        maxStacks = 2
        info = _('获得该状态时{color=#FF4500}降低{/color}身体素质和工作能力。\n专注度小幅度{color=#FF4500}降低{/color}，精神状态消耗小幅度{color=#FF4500}提升{/color}，精神状态恢复小幅度{color=#FF4500}降低{/color}；在床上休息恢复的精神状态大幅度{color=#7CFC00}提升{/color}。\n持续时间结束或层数超过1层时{color=#FF4500}转化{/color}为体弱。')
        info_p = _('获得该状态时{color=#FF4500}降低{/color}2点身体素质和2点工作能力。\n专注度{color=#FF4500}降低{/color}10%，精神状态消耗{color=#FF4500}提升{/color}10%，精神状态恢复{color=#FF4500}降低{/color}10%；在床上休息恢复的精神状态{color=#7CFC00}提升{/color}40%。\n持续时间结束或层数超过1层时{color=#FF4500}转化{/color}为体弱。')
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

        def timeUpAction(self, player):
            Notice.add(_('生病持续时间结束！{color=#FF4500}转化{/color}为伤痕:体弱！'))
            Debilitated.add(player)

        def getPrincipalInfo(self):
            if persistent.PreciseDisplay:
                showinfo = self.info_p
            else:
                showinfo = self.info

            feed = '\n' if showinfo != '' else ''

            if BookPhysPunEffect.has(p):
                return feed + showinfo + _('\n\n当前治愈率：')+green(self.getCurePer(p))+'%'
            return feed + showinfo + _('\n\n当前治愈率：')+str(self.getCurePer(p))+'%'

        def getCurePer(self, player):
            curePercent = 10.0
            if WeatherCloudy.has(player):
                curePercent += 20
            if DrugColdrexEffect.has(player):
                curePercent += 3 ** DrugColdrexEffect.getstack(player)
            if PhysRezA.has(player):
                curePercent += PhysRezA.getstack(player) * 15
            if PhysRezB.has(player):
                curePercent += PhysRezB.getstack(player) * 15
            if Physique.has(player):
                curePercent += Physique.getstack(player) * 5
            if BookPhysPunEffect.has(player):
                curePercent += 30
            return curePercent

        def enableAction(self, player):
            Notice.add(_('由于生病，{color=#FF4500}降低{/color}2点工作能力。'))
            Notice.add(_('由于生病，{color=#FF4500}降低{/color}2点身体素质。'))
            player.working -= 0.02
            player.physical -= 0.02
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
                BookPhysPunEffect.clearByType(player)
                bonus = 2 + Physique.getstack(player)/2
                Notice.add(_('降低了%s点严重程度！')%bonus)
                Notice.add(_('提升了%s点身体素质！')%bonus)
                if BookPhysPunEffect.has(player):
                    s = r2(player.severity * 0.03)
                    player.severity -= s
                    Notice.add(_('由于学习成果：《呼吸训练》，额外降低了%s点严重程度！') % s)
                player.severity -= 0.01 * bonus
                player.physical += 0.01 * bonus

                self.clear(player)



    class MentPun(Effect):
        id = 221
        name = _('偏执')
        kind = _('状态')
        maxDuration = 7
        maxStacks = 2
        info = _('获得该状态时{color=#FF4500}降低{/color}写作技巧和工作能力。\n精神状态消耗{color=#FF4500}提升{/color}，工作类日程的专注度大幅度{color=#7CFC00}提升{/color}，工作类日程消耗的精神状态大幅度{color=#7CFC00}降低{/color}，运动类日程的专注度大幅度{color=#FF4500}降低{/color}。\n\n无法完成委托，阅读小说。\n持续时间结束时或层数超过1层{color=#FF4500}转化{/color}为精神创伤。')
        info_p = _('获得该状态时{color=#FF4500}降低{/color}2点写作技巧和2点工作能力。\n精神状态消耗{color=#FF4500}提升{/color}25%，工作类日程的专注度{color=#7CFC00}提升{/color}60%，工作类日程消耗的精神状态{color=#7CFC00}降低{/color}60%，运动类日程的专注度{color=#FF4500}降低{/color}50%。\n\n无法完成委托，阅读小说。\n持续时间结束时或层数超过1层{color=#FF4500}转化{/color}为精神创伤。')
        ad = _('是的，工作，加倍努力工作，其他的一切都不重要。')

        @classmethod
        def add(cls, player, times=1):
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                if cls.has(p):
                    Notice.add(_('偏执层数为2，{color=#FF4500}转化{/color}为伤痕:精神创伤！'))
                    Decadent.add(player)
                    cls.clearByType(player)
                    return
                Stat.record(player, cls)
                cls.defaultAddEffect(player)

        def timeUpAction(self, player):
            Notice.add(_('偏执持续时间结束！{color=#FF4500}转化{/color}为伤痕:精神创伤！'))
            Decadent.add(player)

        def enableAction(self, player):
            Notice.add(_('由于偏执，{color=#FF4500}降低{/color}2点写作技巧。'))
            Notice.add(_('由于偏执，{color=#FF4500}降低{/color}2点工作能力。'))
            player.working -= 0.02
            player.writing -= 0.02
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
        info = _('专注度小幅度{color=#FF4500}降低{/color}，精神状态消耗{color=#FF4500}提升{/color}。\n无法进行运动类日程。\n持续时间结束时或层数超过1层{color=#FF4500}转化{/color}为体弱。')
        info_p = _('专注度{color=#FF4500}降低{/color}15%，精神状态消耗{color=#FF4500}提升{/color}25%。\n无法进行运动类日程。\n持续时间结束时或层数超过1层{color=#FF4500}转化{/color}为体弱。')
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

        def enableAction(self, player):
            player.basicConcentration -= 15
            player.basicConsumption += 0.25
            player.canSport -= 1

        def disableAction(self, player):
            player.basicConcentration += 15
            player.basicConsumption -= 0.25
            player.canSport += 1

        def getPrincipalInfo(self):
            if persistent.PreciseDisplay:
                showinfo = self.info_p
            else:
                showinfo = self.info

            feed = '\n' if showinfo != '' else ''

            if BookPhysPunEffect.has(p):
                return feed + showinfo + _('\n\n当前治愈率：')+green(self.getCurePer(p))+'%'
            return feed + showinfo + _('\n\n当前治愈率：')+str(self.getCurePer(p))+'%'

        def getCurePer(self, player):
            curePercent = 30.0
            if WeatherCloudy.has(player):
                curePercent += 20
            if PhysRezA.has(player):
                curePercent += PhysRezA.getstack(player) * 15
            if PhysRezB.has(player):
                curePercent += PhysRezB.getstack(player) * 15
            if Physique.has(player):
                curePercent += Physique.getstack(player) * 5
            if Pain.has(player):
                curePercent -= Pain.getstack(player) * 50
            if BookPhysPunEffect.has(player):
                curePercent += 30
            return curePercent


        def cureBySleep(self, player):
            
            if rra(player, self.getCurePer(player)):  # 判定成功时，消耗所有的rezA和rezB
                Notice.add(_('成功治愈！'))
                PhysRezA.clearByType(player)
                PhysRezB.clearByType(player)
                BookPhysPunEffect.clearByType(player)
                bonus = 2 + Physique.getstack(player)/2
                Notice.add(_('降低了%s点严重程度！')%bonus)
                Notice.add(_('提升了%s点身体素质！')%bonus)
                if BookPhysPunEffect.has(player):
                    BookPhysPunEffect.clearByType(player)
                    s = r2(player.severity * 0.03)
                    player.severity -= s
                    Notice.add(_('由于学习成果：《呼吸训练》，额外降低了%s点严重程度！') % s)
                player.severity -= 0.01 * bonus
                player.physical += 0.01 * bonus

                self.clear(player)

        def afterSleepAction(self, player):
            if self.stacks == 0 and rra(player, self.getCurePer(player)):
                Notice.add(_('一觉醒来，你的受伤已经治愈！'))
                PhysRezA.clearByType(player)
                PhysRezB.clearByType(player)
                BookPhysPunEffect.clearByType(player)
                bonus = 2 + Physique.getstack(player)/2
                bonus = int(bonus*0.5)
                Notice.add(_('降低了%s点严重程度！')%bonus)
                Notice.add(_('提升了%s点身体素质！')%bonus)
                if BookPhysPunEffect.has(player):
                    BookPhysPunEffect.clearByType(player)
                    s = r2(player.severity * 0.03)
                    player.severity -= s
                    Notice.add(_('由于学习成果：《呼吸训练》，额外降低了%s点严重程度！') % s)
                player.severity -= 0.01 * bonus
                player.physical += 0.01 * bonus

                self.clear(player)


    class PhysProb(Effect):
        id = 223
        name = _('过劳')
        kind = _('状态')
        maxDuration = 3
        maxStacks = 99
        info = _('进行工作类日程时有一定概率获得。\n获得该状态时有小概率{color=#FF4500}降低{/color}身体素质和工作能力。\n入睡前如果大于3层，状态将在第二日{color=#FF4500}转化{/color}为生病。')
        info_p = _('进行工作类日程时有一定概率获得。\n获得该状态时各有20%的概率{color=#FF4500}降低{/color}2点身体素质和2点工作能力。\n入睡前如果大于3层，状态将在第二日{color=#FF4500}转化{/color}为生病。')
        ad = _('痛苦来自于无法衡量工作和身体健康。')

        def enableAction(self, player):
            if rra(player, 20):
                Notice.add(_('由于过劳，{color=#FF4500}降低{/color}2点身体素质。'))
                player.physical -= 0.02
            if rra(player, 20):
                Notice.add(_('由于过劳，{color=#FF4500}降低{/color}2点工作能力。'))
                player.working -= 0.02

        @classmethod
        def add(cls, player, times=1):
            if times == 0:
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
                if not BookConcEffect.has(player):
                    Notice.add(_('过劳层数大于3，{color=#FF4500}转化{/color}为状态：生病！'))
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
                if BookConcEffect.has(player):
                    self.duration = 1
                    return
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
        info = _('进行工作类日程时有一定概率获得。\n获得该状态时有小概率{color=#FF4500}降低{/color}写作技巧和工作能力。\n入睡前如果大于3层，状态将在第二日{color=#FF4500}转化{/color}为偏执。')
        info_p = _('进行工作类日程时有一定概率获得。\n获得该状态时各有20%的概率{color=#FF4500}降低{/color}2点写作技巧和2点工作能力。\n入睡前如果大于3层，状态将在第二日{color=#FF4500}转化{/color}为偏执。')
        ad = _('我难以呼吸，总觉有何未知的存在正追赶着我，挤压着我将我向前推进。')

        def enableAction(self, player):
            if rra(player, 20):
                Notice.add(_('由于焦虑，{color=#FF4500}降低{/color}2点写作技巧。'))
                player.writing -= 0.01
            if rra(player, 20):
                Notice.add(_('由于焦虑，{color=#FF4500}降低{/color}2点工作能力。'))
                player.working -= 0.01

        @classmethod
        def add(cls, player, times=1):
            if times == 0:
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
                if not BookConcEffect.has(player):
                    Notice.add(_('焦虑层数大于3，{color=#FF4500}转化{/color}为偏执！'))
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
                if BookConcEffect.has(player):
                    self.duration = 1
                    return
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
        info = _('在床上休息或过夜有概率获得。\n{color=#7CFC00}抵消{/color}相同层数的过劳。\n每层都能提升较多的治愈生病和受伤的恢复率。')
        info_p = _('在床上休息后随机获得1~3层，过夜有10%的概率获得1层。\n{color=#7CFC00}抵消{/color}相同层数的过劳。\n每层都能提升15%治愈生病和受伤的恢复率。')
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
        info = _('进行运动类日程后或外出有概率获得。\n{color=#7CFC00}抵消{/color}相同层数过劳。\n每层都能提升较多的治愈生病和受伤的恢复率。')
        info_p = _('进行部分运动类日程后随机获得0~2层，外出探索有25%的概率获得1层。\n{color=#7CFC00}抵消{/color}相同层数过劳。\n每层都能提升15%治愈生病和受伤的恢复率。')
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
        info = _('完成委托时根据消耗的灵感层数获得。\n{color=#7CFC00}抵消{/color}相同层数焦虑。')
        info_p = _('完成委托时根据消耗的灵感及写作素材层数获得，每10层灵感及写作素材都可以获得1层。\n{color=#7CFC00}抵消{/color}相同层数焦虑。')
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
        info = _('进行休息类日程时有概率获得，周末时每完成一项日程都有大概率获得1层。\n{color=#7CFC00}抵消{/color}相同层数焦虑。')  # 33%
        info_p = _('进行部分休息类日程后随机获得0~2层，周末时每完成一项日程都有60%的概率获得1层。\n{color=#7CFC00}抵消{/color}相同层数焦虑。')  # 33%
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
        info = _('每次进行运动时获得4层，拥有该状态时进行任意日程都会获得1层。\n每层酸痛都会使起床时额外{color=#FF4500}消耗{/color}少量精神状态。\n再次获取不会刷新该状态的持续时间，持续时间结束时获得体弱。\n\n进行拉伸运动可{color=#7CFC00}转化{/color}该状态为体魄。')
        info_p = _('每次进行运动时获得4层，拥有该状态时进行任意日程都会获得1层。\n每层酸痛都会使起床时额外{color=#FF4500}消耗{/color}0.5点精神状态。\n再次获取不会刷新该状态的持续时间，持续时间结束时获得1层体弱。\n\n进行拉伸运动可{color=#7CFC00}转化{/color}该状态为体魄。')
        ad = _('“我感觉每根骨头中间的接缝处都积满了淤泥，肌肉与肌肉之间的连接变得干枯易碎。”')

        @classmethod
        def defaultAddEffect(cls, player):  # 默认的add函数，禁止重写
            cls.notResetDurationAddEffect(player)

        def afterSleepAction(self, player):
            m = r2(0.5 * self.stacks * f())
            player.mental -= m
            Notice.add(_('由于酸痛，额外消耗了%s点精神状态。') % m)

        def timeUpAction(self, player):
            Debilitated.add(player)

        def afterTaskAction(self, player, task):  # 日程后
            self.add(player)

        @classmethod
        def add(cls, player, times=1):  # 增加新效果或增加层数
            if GameDifficulty1.has(player):
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
        info = _('当进行的日程与上一个日程不同时获得。\n完成委托将消耗该增益，每层都能{color=#7CFC00}提升{/color}获得的精神的释放层数和委托价值。\n再次获取不会刷新该状态的持续时间，持续时间结束时获得偏执。\n\n进行记录想法可{color=#7CFC00}转化{/color}该状态为写作素材。')
        info_p = _('当进行的日程与上一个日程不同时获得1层。\n完成委托，随笔写作或集中写作将消耗该增益，每层都能{color=#7CFC00}提升{/color}获得的精神的释放层数和委托价值。\n再次获取不会刷新该状态的持续时间，持续时间结束时获得1层偏执。\n\n进行记录想法可{color=#7CFC00}转化{/color}该状态为写作素材。')
        ad = _('用所爱之人的头颅做成的飞机杯……这个点子似乎很有趣啊……')
 
        @classmethod
        def defaultAddEffect(cls, player):  # 默认的add函数，禁止重写
            cls.notResetDurationAddEffect(player)

        def afterTaskAction(self, player, task):  # 日程后
            if task.name == _('记录想法'):
                FixedInspiration.add(player, int(self.stacks * 0.8 + 1))
                self.clear(player)

        def afterSleepAction(self, player):
            if GameDifficulty1.has(player):
                FixedInspiration.add(player, int(self.stacks * 0.8))
                self.clear(player)

        def timeUpAction(self, player):
            MentPun.add(player)


    class Satiety(Effect):
        id = 242
        name = _('饱腹')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 99
        info = _('使用部分食物获得。\n专注度小幅度{color=#FF4500}降低{/color}。\n食物恢复的精神状态随层数大幅{color=#FF4500}降低{/color}，层数较高时食用食物可能会{color=#FF4500}消耗{/color}精神状态。\n进行日程后有大概率移除状态的层数。')
        info_p = _('使用部分食物获得。\n专注度{color=#FF4500}降低{/color}10%。\n食物恢复的精神状态每层都会{color=#FF4500}降低{/color}70%，层数较高时食用食物可能会{color=#FF4500}消耗{/color}精神状态。\n进行日程后有75%的概率移除1层该状态。')
        ad = _('你腹痛难耐，悔恨自己暴食的行为。')

        def enableAction(self, player):
            player.basicConcentration -= 10

        def addStackAction(self, player):
            player.foodRecovery -= 0.7

        def subStackAction(self, player):
            player.foodRecovery += 0.7

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
        info = _('无法进行写作。')
        info_p = _('无法进行随笔写作，完成委托，集中写作日程。')
        ad = _('你对自己可能会丢掉工作这件事的担忧占据了大脑。')

        def enableAction(self, player):
            self.duration = ra(player, 4, 6)


    class Caffeine(Effect):
        id = 244
        name = _('失眠')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 99
        info = _('睡眠消耗的精神状态随层数{color=#FF4500}提升{/color}。')
        info_p = _('每层都会{color=#FF4500}提升{/color}10%睡眠消耗的精神状态。')
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
        maxStacks = 99
        info = _('严重程度随层数百分比{color=#FF4500}提升{/color}。')
        info_p = _('每层都会{color=#FF4500}提升{/color}12%的严重程度。')
        ad = _('也许我不该抽烟的。')

        def addStackAction(self, player):
            player.severityRegarded += 0.12

        def subStackAction(self, player):
            player.severityRegarded -= 0.12

    class Pain(Effect):
        id = 246
        name = _('痛苦')
        kind = _('状态')
        maxDuration = 7
        maxStacks = 99
        info = _('严重程度，睡眠消耗的精神状态和受伤的治愈难度随层数百分比{color=#FF4500}提升{/color}。')
        info_p = _('每层都会{color=#FF4500}提升{/color}15%的严重程度和睡眠消耗的精神状态，并降低50%受伤的治愈率。')
        ad = _('“终于有活着的感觉了……\n不过放着不管的话手会变得像烤乌贼那样的。”')

        def addStackAction(self, player):
            player.severityRegarded += 0.15
            player.deteriorateConsumption += 0.15

        def subStackAction(self, player):
            player.severityRegarded -= 0.15
            player.deteriorateConsumption -= 0.15

    class MuscleFatigue(Effect):
        id = 249
        name = _('肌肉疲劳')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 1
        info = _('获取身体素质时，身体素质获取加成暂时无效。\n健身日程结束后结束该状态。')
        info_p = _('获取身体素质时，身体素质获取加成暂时无效。\n健身日程结束后结束该状态。')
        ad = _('曾经这个疏忽让每个主角都变成了身体素质超过10.0的白袜寸头体育生。')

        def afterTaskAction(self, player, task):
            self.sub(player)


    class EffectGameModule2(Effect):
        id = 296
        name = _('失语')
        kind = _('状态')
        maxDuration = 2
        maxStacks = 1
        info = _('无法进行写作类日程，超大幅度{color=#FF4500}降低{/color}工作能力。')
        info_p = _('无法进行写作类日程，{color=#FF4500}降低{/color}99%的工作能力。')
        ad = _('现在我醒来了，我仍能看到那些颜色……')

        def addStackAction(self, player):
            player.workingRegarded -= 0.99
            player.canWrite -= 1

        def subStackAction(self, player):
            player.workingRegarded += 0.99
            player.canWrite += 1

    class EffectGameModule2_1(Effect):
        id = 297
        name = _('死亡-五晶的怜悯')
        kind = _('状态')
        maxDuration = 3
        maxStacks = 1
        info = _('精神状态消耗{color=#FF4500}提升{/color}了，精神状态恢复{color=#FF4500}提升{/color}了。')
        info_p = _('精神状态消耗{color=#FF4500}降低{/color}20%，精神状态恢复{color=#FF4500}降低{/color}20%。')
        ad = _('*这里只有沉默。*')

        def addStackAction(self, player):
            player.basicConsumption += 0.2
            player.basicRecovery -= 0.2

        def subStackAction(self, player):
            player.basicConsumption -= 0.2
            player.basicRecovery += 0.2
    
    class EffectGameModule2_2(Effect):
        id = 298
        name = _('梦境-白影的幻想')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 6
        info = _('写作能力暂时{color=#7CFC00}提升{/color}了。')
        info_p = _('写作能力暂时{color=#7CFC00}提升{/color}了10%，效果可叠加。')
        ad = _('“来梦里吧，我会让你得到无限的幸福。”')

        def addStackAction(self, player):
            player.writingRegarded += 0.05

        def subStackAction(self, player):
            player.writingRegarded -= 0.05
    
    class EffectGameModule2_3(Effect):
        id = 299
        name = _('欲望-徵羽微凉的贪婪')
        kind = _('状态')
        maxDuration = 1
        maxStacks = 6
        info = _('下次写作时价值大幅度{color=#7CFC00}提升{/color}。')
        info_p = _('下次写作时价值{color=#7CFC00}提升{/color}30%。')
        ad = _('“即使是在这片钢筋丛林里，我们也要做最危险的野兽。”')

    

    class SleepReward(Effect):
        id = 310
        name = _('整备')
        kind = _('增益')
        maxDuration = 1
        maxStacks = 99
        info = _('在床上休息或小睡转化睡意后获得。\n随层数{color=#7CFC00}提升{/color}专注度和工作速度，并{color=#7CFC00}降低{/color}精神状态消耗。\n\n{color=#ffff00}存在此增益时，全力工作不会受到过劳惩罚。{/color}')
        info_p = _('在床上休息或小睡转化睡意后获得。\n移除全力工作施加的2层过劳。每层都会{color=#7CFC00}提升{/color}5%的专注度和10%的工作速度，并{color=#7CFC00}降低{/color}5%的精神状态消耗。\n\n{color=#ffff00}存在此增益时，全力工作不会受到过劳惩罚。{/color}')
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


    class CommissionReward(Effect):
        id = 311
        name = _('释然')
        kind = _('增益')
        maxDuration = 3
        maxStacks = 1
        info = _('结束委托后获得。\n专注度{color=#7CFC00}提升{/color}，精神状态恢复{color=#7CFC00}提升{/color}。')
        info_p = _('结束委托后获得。\n专注度{color=#7CFC00}提升{/color}25%，精神状态恢复{color=#7CFC00}提升{/color}25%。')
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
        info = _('完成本周全部工作时有概率获得。\n工作速度{color=#7CFC00}提升{/color}。')
        info_p = _('完成本周全部工作时有75%的概率获得，超额完成工作时（>120%）必定获得。\n工作速度{color=#7CFC00}提升{/color}20%。')
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
        maxDuration = 14
        maxStacks = 1
        info = _('进行整理房间日程后获得。\n{color=#7CFC00}降低{/color}睡眠消耗的精神状态，进行阅读相关日程时{color=#7CFC00}获得{/color}额外灵感，进行写作相关日程时{color=#7CFC00}降低{/color}严重程度，进行在家工作日程时，不会获得过劳和焦虑，同时完成的工作进度大幅{color=#7CFC00}提升{/color}。\n进行以上日程时，减少1天状态的持续时间。')
        info_p = _('进行整理房间日程后获得。\n{color=#7CFC00}降低{/color}10%睡眠消耗的精神状态，进行阅读相关日程时额外{color=#7CFC00}获得{/color}1层灵感，进行写作相关日程时{color=#7CFC00}降低{/color}2点严重程度，进行在家工作日程时，不会获得过劳和焦虑，同时完成的工作进度{color=#7CFC00}提升{/color}50%。\n进行以上日程时，减少1天状态的持续时间。')
        ad = _('久违的大扫除让你从仪式感中获得些许慰藉，同时也为你在家中的行动带来了便利。')

        def afterTaskAction(self, player, task):  # 日程后
            if task in (DefaultRead, SentimentalRead, TraditionalRead, ReadingBook):
                Inspiration.add(player, 1)
                self.duration = max(self.duration-1, 1)
            elif task in (FreewheelingWriting, NormalWriting, FocusWriting, WriteDownInspiration):
                player.severity -= 0.02
                Notice.add('降低了2点严重度。')
                self.duration = max(self.duration-1, 1)
            elif task == OvertimeWork:
                self.duration = max(self.duration-1, 1)

        def enableAction(self, player):
            self.duration = ra(player, 10, 14)
            player.deteriorateConsumption -= 0.1

        def disableAction(self, player):
            player.deteriorateConsumption += 0.1


    class ReadReward(Effect):
        id = 315
        name = _('领悟')
        kind = _('增益')
        maxDuration = 3
        maxStacks = 1
        info = _('阅读部分书籍或进行除完成委托外的写作类日程后获得。\n写作技巧暂时{color=#7CFC00}提升{/color}，进行写作时，{color=#7CFC00}提升{/color}写作价值度。')
        info_p = _('阅读部分书籍或进行除完成委托外的写作类日程后获得。\n写作技巧暂时{color=#7CFC00}提升{/color}10%，进行写作时，{color=#7CFC00}提升{/color}20%的写作价值度。')
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
        info = _('进行日程将消耗1层本状态，使本次日程的判定结果大幅度{color=#7CFC00}提升{/color}。')
        info_p = _('进行日程将消耗1层本状态，使本次日程的专注度{color=#7CFC00}提升{/color}60%。')
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
        info = _('外出探索后有概率获得。\n写作技巧暂时{color=#7CFC00}提升{/color}。')
        info_p = _('外出探索后有50%的概率获得。\n写作技巧暂时{color=#7CFC00}提升{/color}10%。')
        ad = _('才不是出去玩呢！这叫采风！')

        def enableAction(self, player):
            player.writingRegarded += 0.1

        def disableAction(self, player):
            player.writingRegarded -= 0.1


    class AppleFlavor(Effect):
        id = 318
        name = _('苹果口味')
        kind = _('增益')
        maxDuration = 1
        maxStacks = 1
        info = _('工作速度和工作能力各小幅度{color=#7CFC00}提升{/color}。')
        info_p = _('工作速度和工作能力各{color=#7CFC00}提升{/color}10%。')
        ad = _('这个味道让你想起了在你病床边为你削苹果的人。')

        def enableAction(self, player):
            player.workSpeed += 0.1
            player.workingRegarded += 0.1

        def disableAction(self, player):
            player.workSpeed -= 0.1
            player.workingRegarded -= 0.1


    class CitrusFlavor(Effect):
        id = 319
        name = _('柑橘口味')
        kind = _('增益')
        maxDuration = 1
        maxStacks = 1
        info = _('身体素质，写作技巧和工作能力暂时{color=#7CFC00}提升{/color}。')
        info_p = _('身体素质，写作技巧和工作能力暂时{color=#7CFC00}提升{/color}10%。')
        ad = _('这个味道让你想起了血液和胆汁的气味。')

        def enableAction(self, player):
            player.workingRegarded += 0.1
            player.physicalRegarded += 0.1
            player.writingRegarded += 0.1

        def disableAction(self, player):
            player.basicRecovery -= 0.1
            player.physicalRegarded -= 0.1
            player.writingRegarded -= 0.1
    
    class WarmupEffect(Effect):
        id = 321
        name = _('准备运动')
        kind = _('增益')
        maxDuration = 1
        maxStacks = 1
        info = _('对运动类日程的专注度大幅度{color=#7CFC00}提升{/color}。\n健身日程结束后结束该状态。')
        info_p = _('对运动类日程的专注度{color=#7CFC00}提升{/color}40%。\n健身日程结束后结束该状态。')
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
        maxStacks = 99
        info = _('获得大量专注度{color=#7CFC00}提升{/color}，同时严重程度随层数百分比{color=#7CFC00}降低{/color}。\n进行任意日程后有大概率消耗该增益，结束时获得难耐。')
        info_p = _('{color=#7CFC00}提升{/color}30%的专注度，同时每层都会{color=#7CFC00}降低{/color}10%的严重程度。\n进行任意日程后有50%的概率消耗该增益，结束时获得难耐。')
        ad = _('烟草让能让痛苦消弭。')

        def enableAction(self, player):
            player.basicConcentration += 30

        def disableAction(self, player):
            player.basicConcentration -= 30
            Smoking.add(player)

        def addStackAction(self, player):
            player.severityRegarded -= 0.1

        def subStackAction(self, player):
            player.severityRegarded += 0.1

        def afterTaskAction(self, player, task):
            if rra(player, 50):
                self.clear(player)

    class Relaxation(Effect):
        id = 323
        name = _('松弛')
        kind = _('增益')
        maxDuration = 1
        maxStacks = 1
        info = _('在床上休息或外出获得。\n在物品栏中可以快速阅读一本专业类书籍并消耗1层本状态，获得书籍效果并使书籍进入冷却时间。')
        info_p = _('在床上休息或外出获得。\n在物品栏中可以快速阅读一本专业类书籍并消耗1层本状态，获得书籍效果并使书籍进入冷却时间。')
        ad = _('“你突然想学习，这倒是很稀有。”')

    
    class MeetingReward1(Effect):
        id = 324
        name = _('指导：专注')
        kind = _('增益')
        maxDuration = 7
        maxStacks = 1
        info = _('参与周研讨会后获得。\n对工作类日程的专注度{color=#7CFC00}提升{/color}。')
        info_p = _('参与周研讨会后获得。\n对工作类日程的专注度{color=#7CFC00}提升{/color}40%。')
        ad = _('“把你的注意力聚焦于工作上。”')

        def enableAction(self, player):
            self.duration = ra(player, 5, 7)
            player.workConcentration += 40

        def disableAction(self, player):
            player.workConcentration -= 40
    

    class MeetingReward2(Effect):
        id = 325
        name = _('指导：激励')
        kind = _('增益')
        maxDuration = 7
        maxStacks = 1
        info = _('参与周研讨会后获得。\n工作能力{color=#7CFC00}提升{/color}。')
        info_p = _('参与周研讨会后获得。\n工作能力{color=#7CFC00}提升{/color}30%。')
        ad = _('“努力！努力！在这个时代不卷的人已经被淘汰了！”')

        def enableAction(self, player):
            self.duration = ra(player, 5, 7)
            player.workingRegarded += 0.3

        def disableAction(self, player):
            player.workingRegarded -= 0.3
    
    class MeetingReward3(Effect):
        id = 326
        name = _('指导：坚实')
        kind = _('增益')
        maxDuration = 7
        maxStacks = 1
        info = _('参与周研讨会后获得。\n进行完成工作日程时，精神状态消耗{color=#7CFC00}降低{/color}，同时{color=#7CFC00}提升{/color}完成的进度。')
        info_p = _('参与周研讨会后获得。\n进行完成工作日程时，精神状态消耗{color=#7CFC00}降低{/color}30%，同时{color=#7CFC00}提升{/color}15%完成的进度。')
        ad = _('“有些人总在工位睡觉，这是不好的……你们应该……”')

        def enableAction(self, player):
            self.duration = ra(player, 5, 7)
    
    class MeetingReward4(Effect):
        id = 327
        name = _('指导：技巧')
        kind = _('增益')
        maxDuration = 7
        maxStacks = 1
        info = _('参与周研讨会后获得。\n进行小睡日程时，额外{color=#7CFC00}获得{/color}2层整备，转化睡意时{color=#7CFC00}恢复{/color}的精神状态翻倍。')
        info_p = _('参与周研讨会后获得。\n进行小睡日程时，额外{color=#7CFC00}获得{/color}2层整备，转化睡意时{color=#7CFC00}恢复{/color}的精神状态翻倍。')
        ad = _('“在工作中你们要学会技巧……”')

        def enableAction(self, player):
            self.duration = ra(player, 5, 7)
    

    class MeetingReward5(Effect):
        id = 328
        name = _('指导：分心')
        kind = _('增益')
        maxDuration = 7
        maxStacks = 1
        info = _('参与周研讨会后获得。\n进行偷懒日程时，消耗的精神状态{color=#FF4500}提升{/color}，但是在偷懒中选择读书时将立刻读完整本书。')
        info_p = _('参与周研讨会后获得。\n进行偷懒日程时，消耗的精神状态{color=#FF4500}提升{/color}20%，但是在偷懒中选择读书时将立刻读完整本书。')
        ad = _('“一心二用还不够，你们必须一心三用！……”')

        def enableAction(self, player):
            self.duration = ra(player, 5, 7)
    
    class MeetingReward6(Effect):
        id = 329
        name = _('指导：积累')
        kind = _('增益')
        maxDuration = 7
        maxStacks = 1
        info = _('参与周研讨会后获得。\n立刻完成20%的工作进度，同时进行偷懒日程时，完成的工作进度{color=#7CFC00}提升{/color}。')
        info_p = _('参与周研讨会后获得。\n立刻完成20%的工作进度，同时进行偷懒日程时，完成的工作进度{color=#7CFC00}提升{/color}30%。')
        ad = _('“回想起以往的工作内容，来对待新的内容……”')

        def enableAction(self, player):
            self.duration = ra(player, 5, 7)
            player.achievedGoal += r2(player.goal * 0.2)
    
    class MeetingReward7(Effect):
        id = 330
        name = _('指导：压力')
        kind = _('增益')
        maxDuration = 7
        maxStacks = 1
        info = _('参与周研讨会后获得。\n起床时必定获得紧迫。')
        info_p = _('参与周研讨会后获得。\n起床时必定{color=#7CFC00}获得{/color}紧迫。')
        ad = _('“这周的工作再完成不了……你们就都给我扫地出门！”')

        def enableAction(self, player):
            self.duration = ra(player, 5, 7)

    class MeetingReward8(Effect):
        id = 330
        name = _('指导：放松')
        kind = _('增益')
        maxDuration = 7
        maxStacks = 1
        info = _('参与周研讨会后获得。\n工作消耗的精神状态大幅{color=#7CFC00}降低{/color}。')
        info_p = _('参与周研讨会后获得。\n工作消耗的精神状态{color=#7CFC00}降低{/color}50%。')
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
        info = _('由拉伸运动转化酸痛获得。\n起床时根据层数{color=#7CFC00}恢复{/color}精神状态并获得身体素质。\n每层体魄都能{color=#7CFC00}提升{/color}受伤和生病的治愈恢复率，以及以及治愈成功后获得的奖励。\n\n每天有概率失去一半，层数越多概率越大。')
        info_p = _('由拉伸运动转化酸痛获得。\n起床时{color=#7CFC00}恢复{/color}2.5*层数的精神状态，每层体魄都能提升过夜提升身体素质的概率。\n每层体魄都能{color=#7CFC00}提升{/color}5%受伤和生病的治愈恢复率，以及治愈成功后获得的奖励。\n\n每天有2%*体魄层数的概率失去一半。')
        ad = _('你终于可以说自己是有点肌肉的人了。')

        def afterSleepAction(self, player):
            m = r2(2.50* self.stacks * f())

            if HallukeItem1.has(player):
                m *= 1.5

            player.mental += m
            Notice.add(_('由于体魄，恢复了%s点精神状态。') % m)

            if rra(player, int(self.stacks*10)):
                Notice.add(_('由于体魄，提升了1点身体素质。'))
                player.physical += 0.01

            per = 2 * self.stacks
            if HallukeItem1.has(player):
                per *= 0.5

            if rra(player, per):
                s = int(self.stacks/2)
                self.sub(player, s)
                Notice.add(_('体魄随时间失去了%s层。')%s)



    class FixedInspiration(Effect):
        id = 301
        name = _('写作素材')
        kind = _('增益')
        maxDuration = -1
        maxStacks = 99
        info = _('由记录想法{color=#7CFC00}转化{/color}灵感获得。\n可作为灵感在写作中被消耗。')
        info_p = _('由记录想法{color=#7CFC00}转化{/color}灵感获得。\n可作为灵感在写作中被消耗。')
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


    class DrugDA(Effect):
        id = 403
        name = _('药物依赖{font=arial.ttf}α{/font}')
        kind = _('药物反应')
        maxDuration = 2
        maxStacks = 99
        info = _('过夜时提升等同于层数的对应药物抗药性。\n使用药物{font=arial.ttf}α{/font}后解除。\n持续时间结束后{color=#FF4500}转化{/color}为戒断反应{font=arial.ttf}α{/font}。')
        info_p = _('过夜时提升等同于层数的对应药物抗药性。\n使用药物{font=arial.ttf}α{/font}后解除。\n持续时间结束后{color=#FF4500}转化{/color}为戒断反应{font=arial.ttf}α{/font}。')
        ad = _('你偶尔会感到有些恶心。')

        def timeUpAction(self, player):
            DrugWA.add(player)

        @classmethod
        def defaultAddEffect(cls, player):  # 默认的add函数，禁止重写
            cls.notResetDurationAddEffect(player)
        
        def afterSleepAction(self, player):
            if MedicineA in player.medinfo:
                player.medinfo[MedicineA].res = min(player.medinfo[MedicineA].res + 1 * self.stacks, 80)

        @classmethod
        def add(cls, player, times=1):  # 增加新效果或增加层数
            if GameDifficulty1.has(player):
                return
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                if not BookBanDepEffect.has(player):
                    Stat.record(player, cls)
                    cls.defaultAddEffect(player)
                else:
                    if MedicineA in player.medinfo:
                        player.medinfo[MedicineA].res = min(player.medinfo[MedicineA].res + 1, 80)


    class DrugDB(Effect):
        id = 404
        name = _('药物依赖{font=arial.ttf}β{/font}')
        kind = _('药物反应')
        maxDuration = 2
        maxStacks = 99
        info = _('过夜时提升等同于层数的对应药物抗药性。\n使用药物{font=arial.ttf}β{/font}后解除。\n持续时间结束后{color=#FF4500}转化{/color}为戒断反应{font=arial.ttf}β{/font}。')
        info_p = _('过夜时提升等同于层数的对应药物抗药性。\n使用药物{font=arial.ttf}β{/font}后解除。\n持续时间结束后{color=#FF4500}转化{/color}为戒断反应{font=arial.ttf}β{/font}。')
        ad = _('你偶尔会感到有些头晕。')

        def timeUpAction(self, player):
            DrugWB.add(player)

        @classmethod
        def defaultAddEffect(cls, player):  # 默认的add函数，禁止重写
            cls.notResetDurationAddEffect(player)
        
        def afterSleepAction(self, player):
            if MedicineB in player.medinfo:
                player.medinfo[MedicineB].res = min(player.medinfo[MedicineB].res + 1 * self.stacks, 80)

        @classmethod
        def add(cls, player, times=1):  # 增加新效果或增加层数
            if GameDifficulty1.has(player):
                return
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                if not BookBanDepEffect.has(player):
                    Stat.record(player, cls)
                    cls.defaultAddEffect(player)
                else:
                    if MedicineB in player.medinfo:
                        player.medinfo[MedicineB].res = min(player.medinfo[MedicineB].res + 1, 80)


    class DrugDC(Effect):
        id = 405
        name = _('药物依赖{font=arial.ttf}γ{/font}')
        kind = _('药物反应')
        maxDuration = 2
        maxStacks = 99
        info = _('过夜时提升等同于层数的对应药物抗药性。\n使用药物{font=arial.ttf}γ{/font}后解除。\n持续时间结束后{color=#FF4500}转化{/color}为戒断反应{font=arial.ttf}γ{/font}。')
        info_p = _('过夜时提升等同于层数的对应药物抗药性。\n使用药物{font=arial.ttf}γ{/font}后解除。\n持续时间结束后{color=#FF4500}转化{/color}为戒断反应{font=arial.ttf}γ{/font}。')
        ad = _('你偶尔会眼前一黑。')

        def timeUpAction(self, player):
            DrugWC.add(player)

        @classmethod
        def defaultAddEffect(cls, player):  # 默认的add函数，禁止重写
            cls.notResetDurationAddEffect(player)
        
        def afterSleepAction(self, player):
            if MedicineC in player.medinfo:
                player.medinfo[MedicineC].res = min(player.medinfo[MedicineC].res + 1 * self.stacks, 80)
        
        @classmethod
        def add(cls, player, times=1):  # 增加新效果或增加层数
            if GameDifficulty1.has(player):
                return
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                if not BookBanDepEffect.has(player):
                    Stat.record(player, cls)
                    cls.defaultAddEffect(player)
                else:
                    if MedicineC in player.medinfo:
                        player.medinfo[MedicineC].res = min(player.medinfo[MedicineC].res + 1, 80)


    class DrugWA(Effect):
        id = 400
        name = _('戒断反应{font=arial.ttf}α{/font}')
        kind = _('药物反应')
        maxDuration = 2
        maxStacks = 1
        info = _('专注度大幅度{color=#FF4500}降低{/color}，精神状态消耗大幅度{color=#FF4500}提升{/color}。\n你需要尽快服用任意剂量的{font=arial.ttf}α{/font}药物，并且在第二天早上才会恢复。\n持续时间结束{color=#FF4500}转化{/color}为衰退。')
        info_p = _('专注度{color=#FF4500}降低{/color}100%，精神状态消耗{color=#FF4500}提升{/color}100%。\n你需要尽快服用任意剂量的{font=arial.ttf}α{/font}药物，并且在第二天早上才会恢复。\n持续时间结束{color=#FF4500}转化{/color}为衰退。')
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
            if MedicineA in player.medinfo:
                player.medinfo[MedicineA].res = min(player.medinfo[MedicineA].res + 5, 80)
            if self.stacks == 0:
                self.clear(player)


    class DrugWB(Effect):
        id = 401
        name = _('戒断反应{font=arial.ttf}β{/font}')
        kind = _('药物反应')
        maxDuration = 2
        maxStacks = 1
        info = _('专注度大幅度{color=#FF4500}降低{/color}，精神状态消耗大幅度{color=#FF4500}提升{/color}。\n你需要尽快服用任意剂量的{font=arial.ttf}β{/font}药物，并且在第二天早上才会恢复。\n持续时间结束{color=#FF4500}转化{/color}为衰退。')
        info_p = _('专注度{color=#FF4500}降低{/color}100%，精神状态消耗{color=#FF4500}提升{/color}100%。\n你需要尽快服用任意剂量的{font=arial.ttf}β{/font}药物，并且在第二天早上才会恢复。\n持续时间结束{color=#FF4500}转化{/color}为衰退。')
        ad = _('重度胸闷让你难以专注工作。')

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
            if MedicineB in player.medinfo:
                player.medinfo[MedicineB].res = min(player.medinfo[MedicineB].res + 5, 80)
            if self.stacks == 0:
                self.clear(player)


    class DrugWC(Effect):
        id = 402
        name = _('戒断反应{font=arial.ttf}γ{/font}')
        kind = _('药物反应')
        maxDuration = 2
        maxStacks = 1
        info = _('专注度大幅度{color=#FF4500}降低{/color}，精神状态消耗大幅度{color=#FF4500}提升{/color}。\n你需要尽快服用任意剂量的{font=arial.ttf}γ{/font}药物，并且在第二天早上才会恢复。\n持续时间结束{color=#FF4500}转化{/color}为衰退。')
        info_p = _('专注度{color=#FF4500}降低{/color}100%，精神状态消耗{color=#FF4500}提升{/color}100%。\n你需要尽快服用任意剂量的{font=arial.ttf}γ{/font}药物，并且在第二天早上才会恢复。\n持续时间结束{color=#FF4500}转化{/color}为衰退。')
        ad = _('你难以呼吸。')

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
            if MedicineC in player.medinfo:
                player.medinfo[MedicineC].res = min(player.medinfo[MedicineC].res + 5, 80)
            if self.stacks == 0:
                self.clear(player)


    class DrugEA(Effect):
        id = 406
        name = _('药物作用{font=arial.ttf}α{/font}')
        kind = _('药物反应')
        maxDuration = 1
        maxStacks = 1
        info = _('基础专注度{color=#FF4500}降低{/color}。')
        info_p = _('基础专注度{color=#FF4500}降低{/color}？%。')
        ad = _('你看不清太远的东西。')

        def __init__(self):
            Effect.__init__(self)
            self.useweek = 1

        def getPrincipalInfo(self):
            
            if persistent.PreciseDisplay:
                return _('\n基础专注度{color=#FF4500}降低{/color}%s%s。') % (self.useweek*5, '%')
            return self.info

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

        @classmethod
        def add(cls, player, times=1):  # 增加新效果或增加层数
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                if not BookBanDepEffect.has(player):
                    Stat.record(player, cls)
                    cls.drugEffectAdd(player)


    class DrugEB(Effect):
        id = 407
        name = _('药物作用{font=arial.ttf}β{/font}')
        kind = _('药物反应')
        maxDuration = 1
        maxStacks = 1
        info = _('睡眠消耗的精神状态{color=#FF4500}提升{/color}，写作技巧{color=#7CFC00}提升{/color}。')
        info_p = _('睡眠消耗的精神状态{color=#FF4500}提升{/color}？%，写作技巧{color=#7CFC00}提升{/color}？%。')
        ad = _('你开始出现光怪陆离的幻觉。')

        def __init__(self):
            Effect.__init__(self)
            self.useweek = 1
            
        def getPrincipalInfo(self):
            if persistent.PreciseDisplay:
                return _('\n睡眠消耗的精神状态{color=#FF4500}提升{/color}%s%s，写作技巧{color=#7CFC00}提升{/color}%s%s。') % (self.useweek*5, '%', self.useweek*5, '%')
            return self.info

        def enableAction(self, player):
            player.deteriorateConsumption += 0.05 * self.useweek
            player.writingRegarded += 0.05 * self.useweek

        def disableAction(self, player):
            player.deteriorateConsumption -= 0.05 * self.useweek
            player.writingRegarded -= 0.05 * self.useweek

        @classmethod
        def drugEffectAdd(cls, player):  # 默认的add函数，禁止重写
            if not cls.has(player):
                Notice.add(_('获得新%s：%s！') % (cls.kind, cls.name))
                e = cls()
                e.useweek = player.week
                player.effects.append(e)
                e.enableAction(player)

            sortByID(player.effects)

        @classmethod
        def add(cls, player, times=1):  # 增加新效果或增加层数
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                if not BookBanDepEffect.has(player):
                    Stat.record(player, cls)
                    cls.drugEffectAdd(player)


    class DrugEC(Effect):
        id = 408
        name = _('药物作用{font=arial.ttf}γ{/font}')
        kind = _('药物反应')
        maxDuration = 1
        maxStacks = 1
        info = _('每个日程结束后{color=#7CFC00}恢复{/color}一定的精神状态，但食物恢复的精神状态超大幅度{color=#FF4500}降低{/color}，服用药物的精神状态恢复效果{color=#FF4500}降低{/color}。')
        info_p = _('每个日程结束后{color=#7CFC00}恢复{/color}？~？*基础精神状态消耗的精神状态，但食物恢复的精神状态{color=#FF4500}降低{/color}？%，服用药物的精神状态恢复效果{color=#FF4500}降低{/color}？%。')
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
            if persistent.PreciseDisplay:
                return _('\n每个日程结束后{color=#7CFC00}恢复{/color}%s~%s*基础精神状态消耗的精神状态，但食物恢复的精神状态{color=#FF4500}降低{/color}%s%s，服用药物的精神状态恢复效果{color=#FF4500}降低{/color}%s%s。') % (3*self.useweek, 5*self.useweek, self.useweek*10, '%', self.useweek*5, '%')
            return self.info

        def afterTaskAction(self, player, task):
            t = ra(player, 300, 500) * 0.01 * self.useweek
            t *= MedicineC.getResScale(player)
            t *= Task.getConsScale(player)
            Notice.add(_('由于药物{font=arial.ttf}γ{/font}，恢复了%s点精神状态。') % r2(t))
            player.mental += r2(t)

        @classmethod
        def drugEffectAdd(cls, player):  # 默认的add函数，禁止重写
            if not cls.has(player):
                Notice.add(_('获得新%s：%s！') % (cls.kind, cls.name))
                e = cls()
                e.useweek = player.week
                player.effects.append(e)
                e.enableAction(player)

            sortByID(player.effects)

        @classmethod
        def add(cls, player, times=1):  # 增加新效果或增加层数
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                if not BookBanDepEffect.has(player):
                    Stat.record(player, cls)
                    cls.drugEffectAdd(player)


    class DrugED(Effect):
        id = 409
        name = _('药物作用{font=arial.ttf}δ{/font}')
        kind = _('药物反应')
        maxDuration = 7
        maxStacks = 1
        info = _('不会出现其他药物的依赖反应。')
        info_p = _('不会出现其他药物的依赖反应。')
        ad = _('似乎没有任何头疼的感觉了，未知的躁动和其他药物的微弱反应也消失了。')


    class DrugHypnoticEffect(Effect):
        id = 410
        name = _('药物作用：安眠药')
        kind = _('药物反应')
        maxDuration = 1
        maxStacks = 5
        info = _('随层数{color=#7CFC00}降低{/color}睡眠消耗的精神状态和专注度。')
        info_p = _('{color=#7CFC00}降低{/color}10%睡眠消耗的精神状态，除此之外每层都会{color=#7CFC00}降低{/color}5%睡眠消耗的精神状态和20%专注度。')
        ad = _('昏昏欲睡？也许吧。')

        def enableAction(self, player):
            player.deteriorateConsumption -= 0.1

        def disableAction(self, player):
            player.deteriorateConsumption += 0.1

        def addStackAction(self, player):
            player.deteriorateConsumption -= 0.05
            player.basicConcentration -= 0.2
            if self.stacks >3:
                player.severity += 1000
                Achievement304.achieve()
                Achievement.show()
            elif self.stacks >2:
                player.severity += 1.0
            elif self.stacks >1:
                player.severity += 0.02
            
        def subStackAction(self, player):
            player.deteriorateConsumption += 0.05
            player.basicConcentration += 0.2


    class DrugIbuprofenEffect(Effect):
        id = 411
        name = _('药物作用：头疼药')
        kind = _('药物反应')
        maxDuration = 2
        maxStacks = 5
        info = _('每完成一个日程随层数{color=#7CFC00}恢复{/color}微量精神状态。')
        info_p = _('完成日程后，每层都会{color=#7CFC00}恢复{/color}2%的当前精神状态，最大每层恢复5点。\n精神状态低于0时无效。')
        ad = _('食之无味，弃之可惜。\n有没有人算过到底是维持这东西的药物浓度更加划算还是用等量的钱去买正经的药来吃更划算？')

        def afterTaskAction(self, player, task):
            t = r2(0.02 * player.mental)
            if t > 5:
                t = 5.0
            elif t<0:
                t = 0
            if t>0:
                player.mental += t* self.stacks
                Notice.add(_('由于头疼药，恢复了') + str(t * self.stacks) + _('点精神状态。'))




    class DrugColdrexEffect(Effect):
        id = 412
        name = _('药物作用：感冒药')
        kind = _('药物反应')
        maxDuration = 2
        maxStacks = 5
        info = _('{color=#FF4500}降低{/color}少量专注度，使用时若没有生病则结束该药物反应并提升大量严重程度。\n使用后会延长生病的持续时间并根据层数{color=#7CFC00}提升{/color}生病的恢复率，但本效果结束时若仍在生病则会{color=#FF4500}降低{/color}生病的持续时间。')
        info_p = _('{color=#FF4500}降低{/color}10%专注度，使用时若没有生病则结束该药物反应并提升5点严重程度。\n使用后会延长1天生病的持续时间，每层都会{color=#7CFC00}提升{/color}10%生病的恢复率，但本效果结束时若仍在生病则会{color=#FF4500}降低{/color}2天生病的持续时间。')
        ad = _('其实持续时间延长的越久代表状态越好，而持续时间即将结束代表着病情将恶化至下一个阶段。')

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
        info = _('在硬核模式下，使用后使下一个日程消耗的精神状态大幅度{color=#7CFC00}减少{/color}。') 
        info_p = _('在硬核模式下，使用后使下一个日程消耗的精神状态{color=#7CFC00}减少{/color}60%。') 

        def enableAction(self, player):
            player.basicConsumption -= 0.6

        def disableAction(self, player):
            player.basicConsumption += 0.6

        def afterTaskAction(self, player, task):
            self.sub(player)

    class DrugMethylphenidateEffect(Effect):
        id = 414
        name = _('药物作用：利他林')
        kind = _('药物反应')
        maxDuration = 1
        maxStacks = 1
        info = _('在硬核模式下，所有基础能力{color=#7CFC00}提升{/color}10%，所有基础能力属性的获取加成{color=#7CFC00}提升{/color}1点。效果结束时，大幅{color=#FF4500}降低{/color}专注度。') 
        info_p = _('在硬核模式下，工作能力、身体素质和写作技巧{color=#7CFC00}提升{/color}10%，所有基础能力属性的获取加成{color=#7CFC00}提升{/color}1点。效果结束时，{color=#FF4500}降低{/color}30%的专注度。') 

        def enableAction(self, player):
            player.workingRegarded += 0.1
            player.physicalRegarded += 0.1
            player.writingRegarded += 0.1

            player.workingGain += 0.01
            player.physicalGain += 0.01
            player.writingGain += 0.01


        def disableAction(self, player):
            player.workingRegarded -= 0.1
            player.physicalRegarded -= 0.1
            player.writingRegarded -= 0.1

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
        info = _('专注度大幅度{color=#FF4500}降低{/color}。') 
        info_p = _('专注度{color=#FF4500}降低{/color}30%。') 

        def addStackAction(self, player):
            player.basicConcentration -= 30
            
        def subStackAction(self, player):
            player.basicConcentration += 30

    class DrugdextropropoxypheneEffect(Effect):
        id = 416
        name = _('药物作用：右丙氧芬')
        kind = _('药物反应')
        maxDuration = 1
        maxStacks = 1
        info = _('进行去床上休息日程后时，{color=#FF4500}移除{/color}持续时间等于1的药物依赖。') 
        info_p = _('进行去床上休息日程后时，{color=#FF4500}移除{/color}持续时间等于1的药物依赖。') 

        def afterTaskAction(self, player, task):
            if task.name == _('在床上休息'):
                for i in player.effects:
                    if type(i) not in (DrugDA, DrugDB, DrugDC):
                        continue
                    if i.duration == 1:
                        i.clear(player)


    class BookWriEffect(Effect):
        id = 500
        name = _('学习成果：《于老师教我的写作技巧》')
        kind = _('学识')
        maxDuration = 2
        maxStacks = 1
        info = _('写作技巧{color=#7CFC00}提升{/color}。')
        info_p = _('写作技巧暂时{color=#7CFC00}提升{/color}20%。')
        ad = _('于老师到底是谁？写作、摄影、拍电影、做游戏……几乎各个领域都有他出现？')

        def enableAction(self, player):
            player.writingRegarded += 0.2

        def disableAction(self, player):
            player.writingRegarded -= 0.2

    class BookConcEffect(Effect):
        id = 501
        name = _('学习成果：《海边的于秀爱》')
        kind = _('学识')
        maxDuration = 2
        maxStacks = 1
        info = _('持续时间内过劳和焦虑不会因为层数过多而转化成生病和偏执。\n持续时间结束时，每有一层过劳和焦虑都会{color=#7CFC00}降低{/color}2点严重程度。\n降低的严重程度之和大于10点时，额外{color=#7CFC00}降低{/color}大量严重程度。')
        info_p = _('持续时间内过劳和焦虑不会因为层数过多而转化成生病和偏执。\n持续时间结束时，每有一层过劳和焦虑都会{color=#7CFC00}降低{/color}2点严重程度。\n降低的严重程度之和大于10点时，额外{color=#7CFC00}降低{/color}3%的严重程度。')

        def timeUpAction(self, player):
            s = PhysProb.getstack(player) + MentProb.getstack(player)

            if s != 0:
                e = r2(s*0.02)
                player.severity -= e
                Notice.add(_('由于学习成果：《海边的于秀爱》，降低了%s点严重程度！') % e)
                if s >= 10:
                    e = r2(player.severity * 0.03)
                    player.severity -= e
                    Notice.add(_('由于降低的严重程度之和大于10点，额外降低了%s点严重程度！') % e)

    class BookPhysPunEffect(Effect):
        id = 502
        name = _('学习成果：《呼吸训练》')
        kind = _('学识')
        maxDuration = 2
        maxStacks = 1
        info = _('小幅度百分比{color=#7CFC00}提升{/color}生病和受伤的恢复率。\n百分比{color=#7CFC00}提升{/color}对应状态的恢复率，如果成功治愈，结束效果并{color=#7CFC00}降低{/color}大量严重程度。')
        info_p = _('百分比{color=#7CFC00}提升{/color}30%生病和受伤的恢复率。\n百分比{color=#7CFC00}提升{/color}对应状态的恢复率，如果成功治愈，结束效果并{color=#7CFC00}降低{/color}3%的严重程度。')

    class BookQuickReadEffect(Effect):
        id = 503
        name = _('学习成果：《量子波动速读》')
        kind = _('学识')
        maxDuration = 2
        maxStacks = 4
        info = _('在物品栏中可以快速阅读一本任意书籍并消耗1层本状态，获得书籍效果并使书籍进入冷却时间。')
        info_p = _('在物品栏中可以快速阅读一本任意书籍并消耗1层本状态，获得书籍效果并使书籍进入冷却时间。')



    class BookWorEffect(Effect):
        id = 504
        name = _('学习成果：《保持清醒的秘诀》')
        kind = _('学识')
        maxDuration = 3
        maxStacks = 5
        info = _('按层数{color=#7CFC00}提升{/color}工作速度，{color=#7CFC00}降低{/color}工作消耗的精神状态。')
        info_p = _('每层都会{color=#7CFC00}提升{/color}10%的工作速度，{color=#7CFC00}降低{/color}5%工作消耗的精神状态。')

        def addStackAction(self, player):
            player.workSpeed += 0.1
            player.workConsumption -= 0.05

        def subStackAction(self, player):
            player.workSpeed -= 0.1
            player.workConsumption += 0.05


    class BookInsEffect(Effect):
        id = 505
        name = _('感悟：《2001年的弹珠机》')
        kind = _('学识')
        maxDuration = 14
        maxStacks = 1
        info = _('每天起床时{color=#7CFC00}获得{/color}灵感，同时有小概率结束该效果。')
        info_p = _('每天起床时{color=#7CFC00}获得{/color}1~2层灵感，同时有10%的概率结束该效果。')

        def afterSleepAction(self, player):
            if not Inspiration.has(player):
                Inspiration.add(player, ra(player, 1, 2))
                Inspiration.get(player).duration += 1
            else:
                Inspiration.add(player, ra(player, 1, 2))
            if rra(player, 10) and self.duration <=7:
                self.clear(player)


    class BookSportEffect(Effect):
        id = 506
        name = _('感悟：《阿斯卡隆之春》')
        kind = _('学识')
        maxDuration = 7
        maxStacks = 1
        info = _('阅读本书籍后，一段时间内运动类日程的专注度{color=#7CFC00}提升{/color}，身体素质获取加成{color=#7CFC00}提升{/color}，效果结束后，身体素质永久{color=#7CFC00}提升{/color}。')
        info_p = _('阅读本书籍后，一段时间内运动类日程的专注度{color=#7CFC00}提升{/color}20%，身体素质获取加成{color=#7CFC00}提升{/color}2点，效果结束后，身体素质永久{color=#7CFC00}提升{/color}2%。')

        def enableAction(self, player):
            player.physicalGain += 0.02
            player.sportConcentration += 20

        def disableAction(self, player):
            player.physical += r2(player.physical * 0.02)
            player.sportConcentration -= 20
            player.physicalGain -= 0.02
        

    class BookWriteEffect(Effect):
        id = 507
        name = _('感悟：《亚斯塔禄之冬》')
        kind = _('学识')
        maxDuration = 7
        maxStacks = 1
        info = _('阅读本书籍后，一段时间内写作类日程的专注度{color=#7CFC00}提升{/color}，写作技巧获取加成{color=#7CFC00}提升{/color}，效果结束后，写作技巧永久{color=#7CFC00}提升{/color}。')
        info_p = _('阅读本书籍后，一段时间内写作类日程的专注度{color=#7CFC00}提升{/color}20%，写作技巧获取加成{color=#7CFC00}提升{/color}2点，效果结束后，写作技巧永久{color=#7CFC00}提升{/color}2%。')

        def enableAction(self, player):
            player.writingGain += 0.02
            player.writeConcentration += 20

        def disableAction(self, player):
            player.writing += r2(player.writing * 0.02)
            player.writeConcentration += 20
            player.writingGain -= 0.02
        

    class BookCMEffect(Effect):
        id = 509
        name = _('感悟：《城堡与莫梭提斯》')
        kind = _('学识')
        maxDuration = 14
        maxStacks = 1
        info = _('每天起床时{color=#7CFC00}降低{/color}严重程度，同时有小概率结束该效果。')
        info_p = _('每天起床时{color=#7CFC00}降低{/color}1点严重程度，同时有10%的概率结束该效果。')

        def afterSleepAction(self, player):
            Notice.add(_('由于感悟：《城堡与莫梭提斯》，{color=#7CFC00}降低{/color}1点严重程度！'))
            player.severity -= 0.01
            if rra(player, 10) and self.duration <=7:
                self.clear(player)


    class BookMEDEffect(Effect):
        id = 510
        name = _('感悟：《药：绝望的解决手段》')
        kind = _('学识')
        maxDuration = 7
        maxStacks = 5
        info = _('进行工作类日程时有概率{color=#7CFC00}提升{/color}随机属性。')
        info_p = _('进行工作类日程时有概率{color=#7CFC00}提升{/color}随机属性。')

        def afterTaskAction(self, player, task):  # 日程后
            if task.kind == _('工作类'):
                used = False
                phy = 0
                wri = 0
                wor = 0
                while rra(player, 70):
                    if rra(player, 30):
                        phy += 1
                        used = True
                    if rra(player, 30):
                        wri += 1
                        used = True
                    if rra(player, 30):
                        wor += 1
                        used = True
                if used:
                    if phy > 0:
                        player.physical += 0.01 * phy
                        Notice.add(_('由于感悟：《药：绝望的解决手段》，{color=#7CFC00}提升{/color}了%s点身体素质！') % phy)
                    if wri > 0:
                        player.writing += 0.01 * wri
                        Notice.add(_('由于感悟：《药：绝望的解决手段》，{color=#7CFC00}提升{/color}了%s点写作技巧！') % wri)
                    if wor > 0:
                        player.working += 0.01 * wor
                        Notice.add(_('由于感悟：《药：绝望的解决手段》，{color=#7CFC00}提升{/color}了%s点工作能力！') % wor)
                    self.sub(player)

    class BookRiskEffect(Effect):
        id = 511
        name = _('感悟：《失而复得》')
        kind = _('学识')
        maxDuration = 2
        maxStacks = 1
        info = _('效果期间内消耗的精神状态越多，效果结束时{color=#7CFC00}降低{/color}的严重程度越多，{color=#7CFC00}提升{/color}的工作能力和{color=#7CFC00}降低{/color}的严重程度越多。\n若消耗的精神状态低于150则只会获得2层焦虑，有效上限为500点。')
        info_p = _('效果期间内消耗的精神状态越多，效果结束时{color=#7CFC00}降低{/color}的严重程度越多，{color=#7CFC00}提升{/color}的工作能力和{color=#7CFC00}降低{/color}的严重程度越多。\n若消耗的精神状态低于150则只会获得2层焦虑，有效上限为500点。')

        def __init__(self):
            Effect.__init__(self)
            self.cons=0

        def getPrincipalInfo(self):
            if persistent.PreciseDisplay:
                showinfo = self.info_p
            else:
                showinfo = self.info

            feed = '\n' if showinfo != '' else ''
            return feed + showinfo + _('\n\n当前已消耗精神状态：')+str(self.cons)
        
        def timeUpAction(self, player):
            g = min(r2(self.cons * 0.04 * 0.01), 0.2)

            if self.cons>=150:
                player.working += g
                player.severity -= g
                Notice.add(_('由于感悟：《失而复得》，{color=#7CFC00}提升{/color}了%s点工作能力！') % (g*100))
                Notice.add(_('由于感悟：《失而复得》，{color=#7CFC00}降低{/color}了%s点严重程度！') % (g*100))
            else:
                MentProb.add(p, 2)
                Notice.add(_('由于感悟：《失而复得》，{color=#FF4500}获得{/color}了2层焦虑！'))

    class BookSevUpEffect(Effect):
        id = 512
        name = _('感悟：《热病》')
        kind = _('学识')
        maxDuration = 4
        maxStacks = 1
        info = _('暂时{color=#FF4500}提升{/color}严重程度。')
        info_p = _('暂时{color=#FF4500}提升{/color}10%的严重程度。')

        def enableAction(self, player):
            player.severityRegarded += 0.1

        def disableAction(self, player):
            player.severityRegarded -= 0.1


    class BookUndeadEffect(Effect):
        id = 512
        name = _('感悟：《国境以北星空以南》')
        kind = _('学识')
        maxDuration = 2
        maxStacks = 1
        info = _('暂时{color=#FF4500}提升{/color}严重程度，使精神状态不会低于0。')
        info_p = _('暂时{color=#FF4500}提升{/color}10%的严重程度，使精神状态不会低于0。')

        def enableAction(self, player):
            player.severityRegarded += 0.1

        def disableAction(self, player):
            player.severityRegarded -= 0.1
        
    class BookRandConcEffect(Effect):
        id = 512
        name = _('感悟：《寻羊历险记》')
        kind = _('学识')
        maxDuration = 3
        maxStacks = 1
        info = _('完成日程后{color=#7CFC00}获得{/color}随机专注度加成，仅对下一个日程有效。')
        info_p = _('完成日程后{color=#7CFC00}获得{/color}随机专注度加成，仅对下一个日程有效。')

        def afterTaskAction(self, player, task):
            s = 10
            if rra(player, 50): #10
                s += ra(player, 0, 20)
            if rra(player, 25): #3.25
                s += ra(player, 0, 15)
            if rra(player, 10): #0.5
                s += ra(player, 0, 5)

            BookRandConcEffect_1.add(player, s)


    class BookRandConcEffect_1(Effect):
        id = 512
        name = _('提升：《寻羊历险记》')
        kind = _('学识')
        maxDuration = 1
        maxStacks = 50
        info = _('进行日程将消耗所有本状态，使本次日程的专注度{color=#7CFC00}提升{/color}等同于层数的专注度。')
        info_p = _('进行日程将消耗所有本状态，使本次日程的专注度{color=#7CFC00}提升{/color}等同于层数的专注度。')

        def addStackAction(self, player):
            player.basicConcentration += 1

        def subStackAction(self, player):
            player.basicConcentration -= 1

        def afterTaskAction(self, player, task):
            self.clear(player)

    class BookBanDepEffect(Effect):
        id = 513
        name = _('学识：《常用药理学知识》')
        kind = _('学识')
        maxDuration = 3
        maxStacks = 1
        info = _('持续时间内使用药物{color=#7CFC00}提升{/color}10%恢复的精神状态，同时不会获得药物效果。获得新的药物依赖时，取而代之获得其对应药物的1点抗药性。')
        info_p = _('持续时间内使用药物{color=#7CFC00}提升{/color}10%恢复的精神状态，同时不会获得药物效果。获得新的药物依赖时，取而代之获得其对应药物的1点抗药性。')

        def enableAction(self, player):
            player.drugRecovery += 0.1

        def disableAction(self, player):
            player.drugRecovery -= 0.1


    class GameDifficulty1(Effect):
        id = 600
        name = _('病情好转')
        kind = _('伤痕')
        maxDuration = -1
        maxStacks = 1
        info = _('精神状态消耗大幅度{color=#7CFC00}降低{/color}。\n精神状态恢复大幅度{color=#7CFC00}提升{/color}。\n\n{color=#7FFF00}游戏难度：简单{/color}\n\n{color=#ffff00}可以随时更改已制定好的日程。\n书籍可以在道具栏中直接使用。\n不会获得酸痛和药物依赖效果。\n灵感将在一天结束后自动转化为写作素材。{/color}\n\n严重程度提升概率：低')
        info_p = _('精神状态消耗{color=#7CFC00}降低{/color}40%。\n精神状态恢复{color=#7CFC00}提升{/color}40%。\n\n{color=#7FFF00}游戏难度：简单{/color}\n\n{color=#ffff00}可以随时更改已制定好的日程。\n书籍可以在道具栏中直接使用。\n不会获得酸痛和药物依赖效果。\n灵感将在一天结束后自动转化为写作素材。{/color}\n\n严重程度提升概率：30%')
        ad = _('“你的病情正在逐渐好转，虽然你还是会偶尔头疼，但也许用不了一阵子你就可以脱离药物的治疗。”')

        def enableAction(self, player):
            GameDifficulty2.clearByType(player)
            GameDifficulty3.clearByType(player)
            GameDifficulty4.clearByType(player)
            GameDifficulty5.clearByType(player)
            player.basicConsumption -= 0.4
            player.basicRecovery += 0.4

        def disableAction(self, player):
            player.basicConsumption += 0.4
            player.basicRecovery -= 0.4

        def getPrincipalInfo(self):
            if persistent.PreciseDisplay:
                showinfo = self.info_p
            else:
                showinfo = self.info

            feed = '\n' if showinfo != '' else ''
            return feed + showinfo + _('\n已提升的严重程度倍率：+%s%s')%(p.aggra, '%')

        def afterSleepAction(self, player):
            if rra(player, 30) and player.cured < 0:
                player.severityRegarded += 0.01
                player.aggra += 1

    class GameDifficulty2(Effect):
        id = 601
        name = _('病情稳定')
        kind = _('伤痕')
        maxDuration = -1
        maxStacks = 1
        info = _('精神状态消耗{color=#7CFC00}降低{/color}。\n精神状态恢复{color=#7CFC00}提升{/color}。\n睡眠消耗的精神状态{color=#7CFC00}降低{/color}。\n\n{color=#FFE4C4}游戏难度：较易{/color}\n\n严重程度提升概率：较低')
        info_p = _('{color=#7CFC00}降低{/color}30%。\n精神状态恢复{color=#7CFC00}提升{/color}30%。\n睡眠消耗的精神状态{color=#7CFC00}降低{/color}30%。\n\n{color=#FFE4C4}游戏难度：较易{/color}\n\n严重程度提升概率：30%')
        ad = _('“你的病情趋向于稳定，这段时间里你仍然要忍耐头疼的折磨，但过段时间，应该就可以脱离药物的治疗。”')

        def enableAction(self, player):
            GameDifficulty1.clearByType(player)
            GameDifficulty3.clearByType(player)
            GameDifficulty4.clearByType(player)
            GameDifficulty5.clearByType(player)
            player.basicConsumption -= 0.3
            player.basicRecovery += 0.3
            player.deteriorateConsumption -= 0.3

        def disableAction(self, player):
            player.basicConsumption += 0.3
            player.basicRecovery -= 0.3
            player.deteriorateConsumption += 0.3

        def getPrincipalInfo(self):
            if persistent.PreciseDisplay:
                showinfo = self.info_p
            else:
                showinfo = self.info

            feed = '\n' if showinfo != '' else ''
            return feed + showinfo + _('\n已提升的严重程度倍率：+%s%s')%(p.aggra, '%')

        def afterSleepAction(self, player):
            if rra(player, 30) and player.cured < 0:
                player.severityRegarded += 0.01
                player.aggra += 1

    class GameDifficulty3(Effect):
        id = 602
        name = _('病情较重')
        kind = _('伤痕')
        maxDuration = -1
        maxStacks = 1
        info = _('{color=#87CEEB}游戏难度：一般{/color}\n\n严重程度提升概率：一般')
        info_p = _('{color=#87CEEB}游戏难度：一般{/color}\n\n严重程度提升概率：50%')
        ad = _('“你的病情相对严重，不要忘记按时吃药，多锻炼，不过相信你已经习惯这样的生活了吧。”')

        def enableAction(self, player):
            GameDifficulty1.clearByType(player)
            GameDifficulty2.clearByType(player)
            GameDifficulty4.clearByType(player)
            GameDifficulty5.clearByType(player)

        def getPrincipalInfo(self):
            if persistent.PreciseDisplay:
                showinfo = self.info_p
            else:
                showinfo = self.info

            feed = '\n' if showinfo != '' else ''
            return feed + showinfo + _('\n已提升的严重程度倍率：+%s%s')%(p.aggra, '%')
        
        def afterSleepAction(self, player):
            if rra(player, 50) and player.cured < 0:
                player.severityRegarded += 0.01
                player.aggra += 1

    
    class GameDifficulty4(Effect):
        id = 603
        name = _('病情严重')
        kind = _('伤痕')
        maxDuration = -1
        maxStacks = 1
        info = _('精神状态消耗小幅度{color=#FF4500}提升{/color}。\n睡眠消耗的精神状态小幅度{color=#FF4500}提升{/color}。\n\n{color=#DA70D6}游戏难度：较难{/color}\n\n严重程度提升概率：较高')
        info_p = _('精神状态消耗{color=#FF4500}提升{/color}20%。\n睡眠消耗的精神状态{color=#FF4500}提升{/color}20%。\n\n{color=#DA70D6}游戏难度：较难{/color}\n\n严重程度提升概率：65%')
        ad = _('“你的病情比较严重，你必须更加谨慎地对待生存这件事，不要妄想有一天你能不用吃药了。”')

        def enableAction(self, player):
            GameDifficulty1.clearByType(player)
            GameDifficulty2.clearByType(player)
            GameDifficulty3.clearByType(player)
            GameDifficulty5.clearByType(player)
            player.basicConsumption += 0.2
            player.deteriorateConsumption += 0.2

        def disableAction(self, player):
            player.basicConsumption -= 0.2
            player.deteriorateConsumption -= 0.2

        def getPrincipalInfo(self):
            if persistent.PreciseDisplay:
                showinfo = self.info_p
            else:
                showinfo = self.info

            feed = '\n' if showinfo != '' else ''
            return feed + showinfo + _('\n已提升的严重程度倍率：+%s%s')%(p.aggra, '%')

        def afterSleepAction(self, player):
            if rra(player, 65) and player.cured < 0:
                player.severityRegarded += 0.01
                player.aggra += 1

    class GameDifficulty5(Effect):
        id = 604
        name = _('病情危急')
        kind = _('伤痕')
        maxDuration = -1
        maxStacks = 1
        info = _('精神状态消耗{color=#FF4500}提升{/color}。\n精神状态恢复{color=#FF4500}降低{/color}。\n睡眠消耗的精神状态{color=#FF4500}提升{/color}。\n{color=#FF0000}游戏难度：硬核{/color}\n\n严重程度提升概率：高')
        info_p = _('精神状态消耗{color=#FF4500}提升{/color}60%。\n精神状态恢复{color=#FF4500}降低{/color}60%。\n睡眠消耗的精神状态{color=#FF4500}提升{/color}60%。\n{color=#FF0000}游戏难度：硬核{/color}\n\n严重程度提升概率：80%')
        ad = _('“你是怎么在ICU外还能活到现在的？”')

        def enableAction(self, player):
            GameDifficulty1.clearByType(player)
            GameDifficulty2.clearByType(player)
            GameDifficulty3.clearByType(player)
            GameDifficulty4.clearByType(player)
            player.basicConsumption += 0.6
            player.basicRecovery -= 0.6
            player.deteriorateConsumption += 0.6

        def disableAction(self, player):
            player.basicConsumption -= 0.6
            player.basicRecovery += 0.6
            player.deteriorateConsumption -= 0.6

        def getPrincipalInfo(self):
            if persistent.PreciseDisplay:
                showinfo = self.info_p
            else:
                showinfo = self.info

            feed = '\n' if showinfo != '' else ''
            return feed + showinfo + _('\n已提升的严重程度倍率：+%s%s')%(p.aggra, '%')

        def afterSleepAction(self, player):
            if rra(player, 80) and player.cured < 0:
                player.severityRegarded += 0.01
                player.aggra += 1


    class GameModule1(Effect):
        id = 650
        name = _('挑战模式')
        kind = _('伤痕')
        maxDuration = -1
        maxStacks = 1
        info = _('游戏进入了挑战模式，在该模组下，游戏新增了以下新机制：\n偏头痛：每完成一个日程后随机{color=#FF4500}消耗{/color}精神状态。\n资源供给：{color=#7CFC00}获得{/color}1000元，但药物的价格自然增长倍率{color=#FF4500}提升{/color}。\n自卑感：过夜后每个能力属性都有概率{color=#FF4500}失去{/color}少量，有概率{color=#FF4500}提升{/color}严重程度倍率。\n理财不善：过夜后百分比{color=#FF4500}失去{/color}少量金钱。\n效率低下：每周需要完成的工作目标随周数{color=#FF4500}提升{/color}。\n药物过敏：药物恢复效果小幅度{color=#7CFC00}提升{/color}，过夜后有概率{color=#FF4500}提升{/color}随机一种已经使用过的药物的抗药性。\n知识厌倦：每天有概率使冷却中的书本{color=#FF4500}提升{/color}1点冷却时间。')
        info_p = _('游戏进入了挑战模式，在该模组下，游戏新增了以下新机制：\n偏头痛：每完成一个日程后{color=#FF4500}消耗{/color}1%~20%的当前精神状态。\n资源供给：{color=#7CFC00}获得{/color}1000元，但药物的价格自然增长倍率{color=#FF4500}提升{/color}至1.5倍。\n自卑感：过夜后工作能力，身体素质，写作技巧各有50%的概率{color=#FF4500}失去{/color}1%，严重程度有25%的概率永久{color=#FF4500}提升{/color}1%。\n理财不善：所持金钱大于500元时，过夜后{color=#FF4500}失去{/color}10%的当前金钱。\n效率低下：每周需要完成的工作目标{color=#FF4500}提升{/color}5%*周数。\n药物过敏：药物的恢复效果{color=#7CFC00}提升{/color}15%，过夜后有33%的概率{color=#FF4500}提升{/color}随机一种已经使用过的药物的抗药性。\n知识厌倦：每天有33%的概率使冷却中的书本{color=#FF4500}提升{/color}1点冷却时间。')
        ad = _('也许把大脑切开能将痛苦缓解。')

        def __init__(self):
            Effect.__init__(self)
            self.ment = 0
            self.ph=0
            self.wo=0
            self.wr=0
            self.se=0
            self.mo=0
            self.ra=0
            self.rb=0
            self.rc=0
            self.k=0

        def getPrincipalInfo(self):
            if persistent.PreciseDisplay:
                showinfo = self.info_p
            else:
                showinfo = self.info

            feed = '\n' if showinfo != '' else ''
            extra = _('\n\n【偏头痛】总消耗的精神状态：%s\n【自卑感】提升的严重程度：+%s%s\n失去的工作能力：%s 失去的身体素质：%s 失去的写作技巧：%s\n【理财不善】花掉的金钱：%s\n【药物过敏】%s提升的抗药性：%s %s提升的抗药性：%s %s提升的抗药性：%s\n【知识厌倦】提升的冷却时间：%s') % (self.ment, self.se, '%', self.wo, self.ph, self.wr, self.mo, MedicineA.name, self.ra, MedicineB.name, self.rb, MedicineC.name, self.rc, self.k)
            return feed + showinfo + extra


        def enableAction(self, player):
            player.difficultylocked = True
            player.drugRecovery += 0.15

            player.priceIncrease *= 1.5
            player.money += 1000

            player.physical += 0.2
            player.writing += 0.2
            player.working += 0.2

            player.goal = r2(player.goal * (1 + (0.05 * player.week)))



        def afterTaskAction(self, player, task):
            per = ra(player, 1, 8)
            if rra(player, 50):
                per += ra(player, 0, 8)
            if rra(player, 50):
                per += ra(player, 0, 4)
            if player.mental > 150:
                per = ra(player, 15, 20)
            t = abs(r2(player.mental * per * 0.01))
            self.ment += t
            player.mental -= t
            Notice.add(_('由于偏头痛，消耗了%s点精神状态！') % t)

        def afterSleepAction(self, player):
            if rra(player, 50):
                player.physical -= r2(0.01 * player.physical)
                self.ph += 1
                Notice.add(_('由于自卑，降低了1%的身体素质！'))
            if rra(player, 50):
                player.writing -= r2(0.01 * player.writing)
                self.wr += 1
                Notice.add(_('由于自卑，降低了1%的写作技巧！'))
            if rra(player, 50):
                player.working -= r2(0.01 * player.working)
                self.wo += 1
                Notice.add(_('由于自卑，降低了1%的工作能力！'))
            if rra(player, 25):
                self.se += 1
                player.severityRegarded += 0.01
                Notice.add(_('由于自卑，提升了1%的严重程度！'))
            
            if player.money >= 500:
                t = r2(player.money*0.1*f())
                self.mo += t
                player.money -= t
                Notice.add(_('由于理财不善，不受控制地花掉了%s元！') % t)
            
            if rra(player, 33) and player.medinfo:
                med = rca(player, player.medinfo.keys())
                if med == MedicineA:
                    self.ra += 1
                elif med == MedicineB:
                    self.rb += 1
                elif med == MedicineC:
                    self.rc += 1
                player.medinfo[med].res += 1
                Notice.add(_('由于药物过敏，%s的药物抗性上升了1%s！') % (med.name, '%'))
            
            for i in player.itemcd:
                if i.kind == '书本':
                    if rra(player, 33):
                        Notice.add(_('由于知识厌恶，%s的冷却时间上升了1天！') % (i.name))
                        player.itemcd[i]+=1
                        self.k += 1



    class GameModule2(Effect):
        id = 650
        name = _('无尽之旅')
        kind = _('伤痕')
        maxDuration = -1
        maxStacks = 1
        info = _('{color=#97e41b}你正行走于无尽之旅的道路之上。{/color}\n每次阅读无尽之旅都会{color=#7CFC00}获得{/color}3点{color=#97e41b}足迹{/color}，而使用阅读后获得的手稿也会{color=#7CFC00}获得{/color}2点{color=#97e41b}足迹{/color}。\n每层{color=#97e41b}足迹{/color}都能在起床时提供2%的概率来{color=#7CFC00}减少{/color}1天无尽之旅书籍的冷却时间，2%起床时{color=#7CFC00}获得{/color}灵感的概率，以及0.5%{color=#7CFC00}获得{/color}存在感的概率。')
        info_p = _('{color=#97e41b}你正行走于无尽之旅的道路之上。{/color}\n每次阅读无尽之旅都会{color=#7CFC00}获得{/color}3点{color=#97e41b}足迹{/color}，而使用阅读后获得的手稿也会{color=#7CFC00}获得{/color}2点{color=#97e41b}足迹{/color}。\n每层{color=#97e41b}足迹{/color}都能在起床时提供2%的概率来{color=#7CFC00}减少{/color}1天无尽之旅书籍的冷却时间，2%起床时{color=#7CFC00}获得{/color}灵感的概率，以及0.5%{color=#7CFC00}获得{/color}存在感的概率。')
        ad = _('当旅人来到无尽家族，看着无尽们的“忙碌”，让旅人得到灵感——如果不同的我拿到这种能力会发生什么呢？')

        def __init__(self):
            Effect.__init__(self)
            self.pace = 0
            self.cddown = 0
            self.insp = 0
            self.getrevive = 0

        def enableAction(self, player):
            BookGameModule2.add(player)

        def getPrincipalInfo(self):
            if persistent.PreciseDisplay:
                showinfo = self.info_p
            else:
                showinfo = self.info

            feed = '\n' if showinfo != '' else ''
            extra = _('\n\n足迹：%s\n已减少的书本冷却时间：%s\n已获得的灵感层数：%s\n已获得的存在感层数：%s') %(self.pace, self.cddown, self.insp, self.getrevive)
            return feed + showinfo + extra
        
        def afterSleepAction(self, player):
            if BookGameModule2 in player.itemcd:
                if rra(player, self.pace*2):
                    player.itemcd[BookGameModule2] -= 1
                    self.cddown += 1

                    for k in list(player.itemcd.keys()):
                        if player.itemcd[k] <= 0:
                            del player.itemcd[k]
                    Notice.add(_('由于无尽之旅，无尽之旅的冷却时间降低了！'))
                            
            if rra(player, self.pace*2):
                if not Inspiration.has(player):
                    Inspiration.add(player, 1)
                    Inspiration.get(player).duration += 1
                else:
                    Inspiration.add(player, 1)
                Notice.add(_('由于无尽之旅，获得了1层灵感！'))
                self.insp += 1
            if self.pace*2 > 100:
                if rra(player, self.pace*2-100):
                    if not Inspiration.has(player):
                        Inspiration.add(player, 1)
                        Inspiration.get(player).duration += 1
                    else:
                        Inspiration.add(player, 1)
                    self.insp += 1
                    Notice.add(_('由于无尽之旅，获得了1层灵感！'))

            if rra(player, self.pace*0.5) and not Novice.has(player):
                Novice.add(player)
                Novice.get(player).duration = 4
                Notice.add(_('由于无尽之旅，获得了存在感！'))
                self.getrevive += 1
        
        def readbook(self):
            self.pace += 3
        
        def readmanu(self):
            self.pace += 2

    class Despair(Effect):
        id = 610
        name = _('绝望')
        kind = _('伤痕')
        maxDuration = -1
        maxStacks = 99
        info = _('我还能活下去吗？')
        info_p = _('我还能活下去吗？')

        def addStackAction(self, player):
            player.basicConsumption += 0.015

        def subStackAction(self, player):
            player.basicConsumption -= 0.015

        def afterTaskAction(self, player, task):
            t = r2(3 * self.stacks  * f() * player.basicConsumption)
            self.add(player, ra(player, 1, self.stacks))
            player.mental -= t
            Notice.add(_('%s由于绝望，消耗了%s点精神状态！') % (player.name, t))

        def afterDrug(self, player):
            self.sub(player, self.stacks-1)


    class LifeIsColorless(Effect):
        id = 611
        name = _('生命失去了色彩')
        kind = _('伤痕')
        maxDuration = -1
        maxStacks = 99
        info = _('活着。')
        info_p = _('活着。')

        def afterSleepAction(self, player):
            self.stacks += 1



    class Debilitated(Effect):
        id = 620
        name = _('体弱')
        kind = _('伤痕')
        maxDuration = -1
        maxStacks = 99
        info = _('按层数{color=#FF4500}降低{/color}身体素质。\n药物效果按层数{color=#FF4500}降低{/color}。\n睡眠{color=#FF4500}消耗{/color}的精神状态按层数{color=#FF4500}提升{/color}。')
        info_p = _('每层都会{color=#FF4500}降低{/color}10%的身体素质。\n每层都会{color=#FF4500}降低{/color}10%的药物效果。\n每层都会{color=#FF4500}提升{/color}10%睡眠消耗的精神状态。')
        ad = _('“有些伤口永远不会完全愈合。”')

        def addStackAction(self, player):
            player.physicalRegarded -= 0.1
            player.drugRecovery -= 0.1
            player.deteriorateConsumption += 0.1

        def subStackAction(self, player):
            player.physicalRegarded += 0.1
            player.drugRecovery += 0.1
            player.deteriorateConsumption -= 0.1


    class Decadent(Effect):
        id = 621
        name = _('精神创伤')
        kind = _('伤痕')
        maxDuration = -1
        maxStacks = 99
        info = _('按层数{color=#FF4500}降低{/color}写作技巧。\n过夜将会{color=#FF4500}失去{/color}相当于该伤痕层数的灵感。\n完成委托时，委托的价值按层数{color=#FF4500}降低{/color}。')
        info_p = _('每层都会{color=#FF4500}降低{/color}10%的写作技巧。\n每次过夜都会{color=#FF4500}失去{/color}相当于该伤痕层数的灵感。\n完成委托时，委托的价值每层都会{color=#FF4500}降低{/color}10%。')
        ad = _('“我已经悖离了我自己的心。”')

        def addStackAction(self, player):
            player.writingRegarded -= 0.1
            player.writeValuable -= 0.1

        def afterSleepAction(self, player):
            if Inspiration.has(player):
                Inspiration.subByType(player, self.stacks)

        def subStackAction(self, player):
            player.writingRegarded += 0.1
            player.writeValuable += 0.1

    class Deterioration(Effect):
        id = 622
        name = _('衰退')
        kind = _('伤痕')
        maxDuration = -1
        maxStacks = 99
        info = _('严重程度{color=#FF4500}提升{/color}，过夜有概率失去灵感和体魄。\n')
        info_p = _('每层都会{color=#FF4500}提升{/color}10%的严重程度，过夜有33%的概率失去等于衰退层数的灵感和体魄。\n')
        ad = _('“对你来说可能有毒，但你还是会喝下去。”')

        def addStackAction(self, player):
            player.severityRegarded += 0.1

        def subStackAction(self, player):
            player.severityRegarded -= 0.1

        def afterSleepAction(self, player):
            if Inspiration.has(player) and rra(player, 33):
                Inspiration.subByType(player, self.stacks)
            if Physique.has(player) and rra(player, 33):
                Physique.subByType(player, self.stacks)

