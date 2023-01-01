init python early:

    class WeatherSunny(Effect):
        id = 100
        name = '{color=#FFD700}晴天{/color}'
        kind = '天气'
        maxDuration = 1
        maxStacks = 1
        info = '户外运动会{color=#7CFC00}恢复{/color}更多精神状态，并额外{color=#7CFC00}提升{/color}身体素质。'
        info_p = '进行外出散步、慢跑、速跑时会{color=#7CFC00}恢复{/color}额外25%的精神状态，并额外{color=#7CFC00}提升{/color}2点身体素质。'
        ad = '适合室外运动的好天气。'

        def enableAction(self, player):
            for i in (WeatherRainy, WeatherCloudy, WeatherWet, WeatherHot, WeatherThunder, WeatherWindy, WeatherUnknown, WeatherNone, WeatherTornado):
                i.clearByType(player)

            player.outdoorSportRecovery += 0.25

        def disableAction(self, player):
            player.outdoorSportRecovery -= 0.25

        def afterTaskAction(self, player, task):
            if task.name in ('外出散步', '慢跑', '速跑'):
                Notice.add('由于晴天，提升了2点身体素质！')
                player.physical += 0.01


    class WeatherRainy(Effect):
        id = 101
        name = '{color=#87CEFA}雨天{/color}'
        kind = '天气'
        maxDuration = 1
        maxStacks = 1
        info = '进行写作类日程或在床上休息会{color=#7CFC00}恢复{/color}更多的精神状态，且会额外{color=#7CFC00}降低{/color}严重程度。\n外卖价格会小幅度提升。\n\n{color=FF0000}无法进行室外跑步。{/color}'
        info_p = '进行写作类日程或在床上休息会{color=#7CFC00}恢复{/color}额外25%的精神状态，且会额外{color=#7CFC00}降低{/color}2点严重程度。\n外卖价格提升20%。\n\n{color=FF0000}无法进行室外跑步。{/color}'
        ad = '适合宅家的好天气。'

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
                Notice.add('由于雨天，降低了2点严重程度！')
                player.severity -= 0.02


    class WeatherCloudy(Effect):
        id = 102
        name = '{color=#B0C4DE}多云{/color}'
        kind = '天气'
        maxDuration = 1
        maxStacks = 1
        info = '工作类日程的专注度{color=#FF4500}降低{/color}，{color=#7CFC00}提升{/color}生病和受伤的恢复率。'
        info_p = '工作类日程的专注度{color=#FF4500}降低{/color}15%，{color=#7CFC00}提升{/color}20%生病和受伤的恢复率。'
        ad = '阴沉的天气让你犯困，你总是忍不住打哈欠。'

        def enableAction(self, player):
            for i in (WeatherSunny, WeatherRainy, WeatherWet, WeatherHot, WeatherThunder, WeatherWindy, WeatherUnknown, WeatherNone, WeatherTornado):
                i.clearByType(player)

            player.workConcentration -= 15

        def disableAction(self, player):
            player.workConcentration += 15


    class WeatherHot(Effect):
        id = 103
        name = '{color=#FF4500}酷热{/color}'
        kind = '天气'
        maxDuration = 1
        maxStacks = 1
        info = '身体素质暂时小幅度{color=#FF4500}降低{/color}，运动类日程恢复的精神状态和专注度{color=#FF4500}降低{/color}，且进行后将额外{color=#FF4500}提升{/color}严重程度。'
        info_p = '身体素质暂时{color=#FF4500}降低{/color}5%，运动类日程恢复的精神状态和专注度{color=#FF4500}降低{/color}20%，且进行后将额外{color=#FF4500}提升{/color}2点严重程度。'
        ad = '衣服都被汗打湿了啊，也太热了吧！'

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
            if task.kind == '运动类':
                player.severity += 0.02


    class WeatherWindy(Effect):
        id = 104
        name = '{color=#98FB98}刮风{/color}'
        kind = '天气'
        maxDuration = 1
        maxStacks = 1
        info = '完成日程后百分比{color=#7CFC00}恢复{/color}少量精神状态。'
        info_p = '完成日程后{color=#7CFC00}恢复{/color}当前精神状态的5% ~ 15%，最高恢复20点。'
        ad = '人都要被吹跑了！不过我喜欢这种感觉！'

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
        name = '{color=#00FFFF}阴冷{/color}'
        kind = '天气'
        maxDuration = 1
        maxStacks = 1
        info = '完成日程后若没有良好的运动则有概率生病，若已经生病则不会再生病。'
        info_p = '完成日程后若没有良好的运动则有40%的概率生病，若已经生病则不会再生病。'
        ad = '……我真应该把我那件大衣带到公司……'

        def enableAction(self, player):
            for i in (WeatherSunny, WeatherRainy, WeatherCloudy, WeatherHot, WeatherThunder, WeatherWindy, WeatherUnknown, WeatherNone, WeatherTornado):
                i.clearByType(player)

        def afterTaskAction(self, player, task):
            if not PhysRezB.has(player) and not PhysPun.has(player):
                if rra(player, 40):
                    PhysPun.add(player)


    class WeatherThunder(Effect):
        id = 106
        name = '{color=#FFFF00}打雷{/color}'
        kind = '天气'
        maxDuration = 1
        maxStacks = 1
        info = '睡眠消耗的精神状态{color=#FF4500}提升{/color}。'
        info_p = '睡眠消耗的精神状态{color=#FF4500}提升{/color}20%。'
        ad = '我并非是怕打雷的小孩子，但即便是轻微的声响都让我难以入眠……'

        def enableAction(self, player):
            for i in (WeatherSunny, WeatherRainy, WeatherCloudy, WeatherWet, WeatherHot, WeatherWindy, WeatherUnknown, WeatherNone, WeatherTornado):
                i.clearByType(player)

            player.deteriorateConsumption += 0.15

        def disableAction(self, player):
            player.deteriorateConsumption -= 0.15

    class WeatherTornado(Effect):
        id = 107
        name = '{color=#4682B4}台风{/color}'
        kind = '天气'
        maxDuration = 2
        maxStacks = 1
        info = '该天气持续时无需上班，但也无法进行户外运动，也不能外出。\n外卖价格会大幅度提升。'
        info_p = '该天气持续时无需上班，但也无法进行户外运动，也不能外出。\n外卖价格提升50%。'
        ad = '以此天气纪念于秀爱两次阳光明媚时出门被突发的大暴雨浇成落汤鸡。'

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
        name = '？？？'
        kind = '天气'
        maxDuration = 1
        maxStacks = 1
        info = '？？？？？？？？？？？'
        info_p = '？？？？？？？？？？？'
        ad = '在废墟之下，你不知道外界的天气。'

        def enableAction(self, player):
            for i in (WeatherSunny, WeatherRainy, WeatherCloudy, WeatherWet, WeatherHot, WeatherThunder, WeatherWindy, WeatherUnknown, WeatherTornado):
                i.clearByType(player)

    class WeatherUnknown(Effect):
        id = 110
        name = '未知'
        kind = '天气'
        maxDuration = 1
        maxStacks = 1
        info = '你并不关心今天是什么天气。'
        info_p = '你并不关心今天是什么天气。'

        def enableAction(self, player):
            for i in (WeatherSunny, WeatherRainy, WeatherCloudy, WeatherWet, WeatherHot, WeatherThunder, WeatherWindy, WeatherNone, WeatherTornado):
                i.clearByType(player)


    class Novice(Effect):
        id = 200
        name = '存在感'
        kind = '状态'
        maxDuration = 14
        maxStacks = 1
        info = '持续时间内{color=#7CFC00}降低{/color}严重程度和睡眠消耗的精神状态。\n即将死亡时，{color=#7CFC00}恢复{/color}精神状态至一定值。\n如果没有触发效果，则持续时间结束时{color=#7CFC00}降低{/color}严重程度倍率。'
        info_p = '持续时间内{color=#7CFC00}降低{/color}10%的严重程度和睡眠消耗的精神状态。\n当起床时精神状态低于单个药物能够恢复至大于0的数值，或已经没有药物且精神状态低于0，则消耗该效果{color=#7CFC00}恢复{/color}精神状态至80。\n如果没有触发效果，则持续时间结束时{color=#7CFC00}降低{/color}2%的严重程度倍率。'
        ad = '“很想看到渐次泛白的黎明时分的天宇，想喝热气蒸腾的牛奶，想闻树木的清香，想翻晨报的版面。”'

        def timeUpAction(self, player):
            Notice.add('存在感持续时间结束，降低了2%的严重程度倍率！')
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
                Notice.add('移除了状态：存在感，将精神状态恢复至80.0')
                player.mental = 80.0
                self.clear(player)


    class Erection(Effect):
        id = 201
        name = '勃起'
        kind = '状态'
        maxDuration = 1
        maxStacks = 1
        info = '你的欲望让你的生殖器官充血膨胀。'
        info_p = '你的欲望让你的生殖器官充血膨胀。'
        ad = '我感觉我的内裤开始变紧了……'

        def afterTaskAction(self, player, task):
            if rra(player, 50):
                self.clear(player)

        def end(self, player):
            Pleasure.add(player)
            player.mental += r2(player.mental * 0.5)
            self.clear(player)


    class Pleasure(Effect):
        id = 202
        name = '快感'
        kind = '状态'
        maxDuration = 1
        maxStacks = 1
        info = '你刚刚射过精。'
        info_p = '你刚刚射过精。'
        ad = '啊……这种感觉……爽到……'

        def afterTaskAction(self, player, task):
            self.clear(player)


    class ConsInc(Effect):
        id = 210
        name = '紧张'
        kind = '状态'
        maxDuration = 1
        maxStacks = 5
        info = '精神状态消耗随层数{color=#FF4500}提升{/color}，精神状态恢复随层数{color=#7CFC00}提升{/color}。'
        info_p = '精神状态消耗每层都会{color=#FF4500}提升{/color}10%，精神状态恢复每层都会{color=#7CFC00}提升{/color}10%。'
        ad = '做点什么，是的，尽可能多地做，尽可能完美地做，至少在死前做更多的事情，做世界上大多数人都没做过的事，不然怎么能算活着呢。'

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
        name = '放松'
        kind = '状态'
        maxDuration = 1
        maxStacks = 5
        info = '精神状态消耗随层数{color=#7CFC00}降低{/color}，精神状态恢复随层数{color=#FF4500}降低{/color}。'
        info_p = '精神状态消耗每层都会{color=#7CFC00}降低{/color}10%，精神状态恢复每层都会{color=#FF4500}降低{/color}10%。'
        ad = '不，也许我没必要做那么多？我为什么要那样折磨自己？死亡之后一切都对我没有意义，及时行乐……我应该辞了这份工作。'

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
        name = '睡意'
        kind = '状态'
        maxDuration = 1
        maxStacks = 5
        info = '专注度随层数{color=#FF4500}降低{/color}，睡眠消耗的精神状态随层数{color=#7CFC00}降低{/color}。'
        info_p = '专注度每层都会{color=#FF4500}降低{/color}10%，睡眠消耗的精神状态每层都会{color=#7CFC00}降低{/color}10%。'
        ad = '是的，让我睡觉，求你了，能让我躺在柔软的床上美美地睡一觉的话我什么都会做的。'

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
        name = '兴奋'
        kind = '状态'
        maxDuration = 1
        maxStacks = 5
        info = '专注度随层数{color=#7CFC00}提升{/color}，睡眠消耗的精神状态随层数{color=#FF4500}提升{/color}。'
        info_p = '专注度每层都会{color=#7CFC00}提升{/color}10%，睡眠消耗的精神状态每层都会{color=#FF4500}提升{/color}10%。'
        ad = '我痛恨我需要睡眠，若是能有按钮迅速跳过夜晚瞬间恢复精神状态来到第二天，或是单纯将我的肉体与电线链接便可恢复能量就好了。'

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
        name = '紧迫'
        kind = '状态'
        maxDuration = 1
        maxStacks = 1
        info = '大幅{color=#7CFC00}提升{/color}工作速度和工作的专注度。'
        info_p = '工作速度{color=#7CFC00}提升{/color}30%，对工作的专注度{color=#7CFC00}提升{/color}30%。'
        ad = '我难以呼吸，总觉有何未知的存在正追赶着我，挤压着我将我向前推进。'

        def enableAction(self, player):
            player.workSpeed += 0.3
            player.workConcentration += 30

        def disableAction(self, player):
            player.workSpeed -= 0.3
            player.workConcentration -= 30


    class Contentment(Effect):
        id = 215
        name = '安逸'
        kind = '状态'
        maxDuration = 1
        maxStacks = 99
        info = '在床上休息恢复的精神状态大幅{color=#7CFC00}提升{/color}，且必定移除全部的过劳。'
        info_p = '在床上休息恢复的精神状态{color=#7CFC00}提升{/color}30%，且必定移除全部的过劳。'
        ad = '我已经得到了部分存在而得的愉悦，较低的期望让我不再渴求之外的事物，无需追赶自己。'

        def enableAction(self, player):
            player.sleepRecovery += 0.3

        def disableAction(self, player):
            player.sleepRecovery -= 0.3

        def afterTaskAction(self, player, task):
            if task.name == '在床上休息':
                if PhysProb.has(player):
                    PhysProb.clearByType(player)


    class Dread(Effect):
        id = 216
        name = '恐惧'
        kind = '状态'
        maxDuration = 1
        maxStacks = 99
        info = '暂时{color=#FF4500}提升{/color}严重程度。\n状态结束后降低大量严重程度。'
        info_p = '暂时{color=#FF4500}提升{/color}15%的严重程度。\n状态结束后降低5点严重程度。'
        ad = '当破除这份来源于存在本身的的恐惧后，迎来的则是存活的希望。'

        def enableAction(self, player):
            player.severityRegarded += 0.15

        def disableAction(self, player):
            player.severityRegarded -= 0.15
            player.severity -= 0.05
            
    

    class Desire(Effect):
        id = 217
        name = '渴求'
        kind = '状态'
        maxDuration = 1
        maxStacks = 99
        info = '精神状态消耗{color=#7CFC00}提升{/color}，但通过日程提升的属性额外{color=#7CFC00}提升{/color}。'
        info_p = '精神状态消耗{color=#7CFC00}提升{/color}15%，但通过日程提升的属性额外{color=#7CFC00}提升{/color}1点。'
        ad = '对美好的未来之憧憬让我更加渴望努力获得我应得之物，但这份躁动让我难以忍受。'

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
        name = '悲伤'
        kind = '状态'
        maxDuration = 1
        maxStacks = 99
        info = '可以进行随笔写作，写作的价值度{color=#7CFC00}提升{/color}，通过日程提升的写作技巧额外{color=#7CFC00}提升{/color}。'
        info_p = '可以进行随笔写作，写作的价值度提升15%，通过日程{color=#7CFC00}提升{/color}的写作技巧额外{color=#7CFC00}提升{/color}2点。'
        ad = '一双无形的手挤压着我的心脏，它渴望看到我的眼泪。'

        def enableAction(self, player):
            player.writeValuable += 0.15
            player.writingGain += 0.02

        def disableAction(self, player):
            player.writeValuable -= 0.15
            player.writingGain -= 0.02


    class Agony(Effect):
        id = 219
        name = '澎湃'
        kind = '状态'
        maxDuration = 1
        maxStacks = 99
        info = '每个日程结束后都会获得良好的运动，运动恢复的精神状态大幅度{color=#7CFC00}提升{/color}，运动类日程的专注度{color=#7CFC00}提升{/color}，通过日程提升的身体素质额外{color=#7CFC00}提升{/color}。'
        info_p = '每个日程结束后都会获得良好的运动，运动恢复的精神状态{color=#7CFC00}提升{/color}30%，对运动类日程的专注度{color=#7CFC00}提升{/color}20%，通过日程提升的身体素质额外{color=#7CFC00}提升{/color}2点。'
        ad = '即便世间还要如此折磨我，但我仍要努力反抗。'

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
        name = '生病'
        kind = '状态'
        maxDuration = 7
        maxStacks = 2
        info = '获得该状态时{color=#FF4500}降低{/color}身体素质和工作能力。\n' \
            '专注度小幅度{color=#FF4500}降低{/color}，精神状态消耗小幅度{color=#FF4500}提升{/color}，精神状态恢复小幅度{color=#FF4500}降低{/color}；在床上休息恢复的精神状态大幅度{color=#7CFC00}提升{/color}。\n' \
            '持续时间结束或层数超过1层时{color=#FF4500}转化{/color}为体弱。'
        info_p = '获得该状态时{color=#FF4500}降低{/color}2点身体素质和2点工作能力。\n' \
            '专注度{color=#FF4500}降低{/color}10%，精神状态消耗{color=#FF4500}提升{/color}10%，精神状态恢复{color=#FF4500}降低{/color}10%；在床上休息恢复的精神状态{color=#7CFC00}提升{/color}40%。\n' \
            '持续时间结束或层数超过1层时{color=#FF4500}转化{/color}为体弱。'
        ad = '病痛折磨着我，与脑中毫无频率的头疼一同。'

        @classmethod
        def add(cls, player, times=1):
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                if cls.has(p):
                    Notice.add('生病层数为2，{color=#FF4500}转化{/color}为伤痕:体弱！')
                    Debilitated.add(player)
                    cls.clearByType(player)
                    return
                Stat.record(player, cls)
                cls.defaultAddEffect(player)

        def timeUpAction(self, player):
            Notice.add('生病持续时间结束！{color=#FF4500}转化{/color}为伤痕:体弱！')
            Debilitated.add(player)

        def getPrincipalInfo(self):
            if persistent.PreciseDisplay:
                showinfo = self.info_p
            else:
                showinfo = self.info

            feed = '\n' if showinfo != '' else ''

            if BookPhysPunEffect.has(p):
                return feed + showinfo + '\n\n当前治愈率：'+green(self.getCurePer(p))+'%'
            return feed + showinfo + '\n\n当前治愈率：'+str(self.getCurePer(p))+'%'

        def getCurePer(self, player):
            curePercent = 10.0
            if WeatherCloudy.has(player):
                curePercent += 20
            if DrugColdrexEffect.has(player):
                curePercent += 3 ** DrugColdrexEffect.get(player).stacks
            if PhysRezA.has(player):
                curePercent += PhysRezA.get(player).stacks * 15
            if PhysRezB.has(player):
                curePercent += PhysRezB.get(player).stacks * 15
            if Physique.has(player):
                curePercent += Physique.get(player).stacks * 5
            if BookPhysPunEffect.has(player):
                curePercent += 30
            return curePercent

        def enableAction(self, player):
            Notice.add('由于生病，{color=#FF4500}降低{/color}2点工作能力。')
            Notice.add('由于生病，{color=#FF4500}降低{/color}2点身体素质。')
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
                Notice.add('成功治愈！')
                PhysRezA.clearByType(player)
                PhysRezB.clearByType(player)
                DrugColdrexEffect.clearByType(player)
                BookPhysPunEffect.clearByType(player)
                bonus = 2 + Physique.getS(player)/2
                Notice.add('降低了%s点严重程度！'%bonus)
                Notice.add('提升了%s点身体素质！'%bonus)
                if BookPhysPunEffect.has(player):
                    s = r2(player.severity * 0.05)
                    player.severity -= s
                    Notice.add('由于学习成果：《呼吸训练》，额外降低了%s点严重程度！' % s)
                player.severity -= 0.01 * bonus
                player.physical += 0.01 * bonus

                self.clear(player)



    class MentPun(Effect):
        id = 221
        name = '偏执'
        kind = '状态'
        maxDuration = 7
        maxStacks = 2
        info = '获得该状态时{color=#FF4500}降低{/color}写作技巧和工作能力。\n' \
            '精神状态消耗{color=#FF4500}提升{/color}，工作类日程的专注度大幅度{color=#7CFC00}提升{/color}，工作类日程消耗的精神状态大幅度{color=#FF4500}降低{/color}，运动类日程的专注度大幅度{color=#FF4500}降低{/color}。\n\n' \
            '无法完成委托，阅读小说。\n' \
            '持续时间结束时或层数超过1层{color=#FF4500}转化{/color}为精神创伤。'
        info_p = '获得该状态时{color=#FF4500}降低{/color}2点写作技巧和2点工作能力。\n' \
            '精神状态消耗{color=#FF4500}提升{/color}25%，工作类日程的专注度{color=#7CFC00}提升{/color}60%，工作类日程消耗的精神状态{color=#FF4500}降低{/color}60%，运动类日程的专注度{color=#FF4500}降低{/color}50%。\n\n' \
            '无法完成委托，阅读小说。\n' \
            '持续时间结束时或层数超过1层{color=#FF4500}转化{/color}为精神创伤。'
        ad = '是的，工作，加倍努力工作，其他的一切都不重要。'

        @classmethod
        def add(cls, player, times=1):
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                if cls.has(p):
                    Notice.add('偏执层数为2，{color=#FF4500}转化{/color}为伤痕:精神创伤！')
                    Decadent.add(player)
                    cls.clearByType(player)
                    return
                Stat.record(player, cls)
                cls.defaultAddEffect(player)

        def timeUpAction(self, player):
            Notice.add('偏执持续时间结束！{color=#FF4500}转化{/color}为伤痕:精神创伤！')
            Decadent.add(player)

        def enableAction(self, player):
            Notice.add('由于偏执，{color=#FF4500}降低{/color}2点写作技巧。')
            Notice.add('由于偏执，{color=#FF4500}降低{/color}2点工作能力。')
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
        name = '受伤'
        kind = '状态'
        maxDuration = 7
        maxStacks = 2
        info = '专注度小幅度{color=#FF4500}降低{/color}，精神状态消耗{color=#FF4500}提升{/color}。\n' \
            '无法进行运动类日程。\n' \
            '持续时间结束时或层数超过1层{color=#FF4500}转化{/color}为体弱。'
        info_p = '专注度{color=#FF4500}降低{/color}15%，精神状态消耗{color=#FF4500}提升{/color}25%。\n' \
            '无法进行运动类日程。\n' \
            '持续时间结束时或层数超过1层{color=#FF4500}转化{/color}为体弱。'
        ad = '我已为力量做出了牺牲。'

        @classmethod
        def add(cls, player, times=1):
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                if cls.has(p):
                    Notice.add('受伤层数为2，{color=#FF4500}转化{/color}为：体弱！')
                    Debilitated.add(player)
                    cls.clearByType(player)
                    return
                Stat.record(player, cls)
                cls.defaultAddEffect(player)

        def timeUpAction(self, player):
            Notice.add('受伤持续时间结束！{color=#FF4500}转化{/color}为：体弱！')
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
                return feed + showinfo + '\n\n当前治愈率：'+green(self.getCurePer(p))+'%'
            return feed + showinfo + '\n\n当前治愈率：'+str(self.getCurePer(p))+'%'

        def getCurePer(self, player):
            curePercent = 30.0
            if WeatherCloudy.has(player):
                curePercent += 20
            if PhysRezA.has(player):
                curePercent += PhysRezA.get(player).stacks * 15
            if PhysRezB.has(player):
                curePercent += PhysRezB.get(player).stacks * 15
            if Physique.has(player):
                curePercent += Physique.get(player).stacks * 5
            if Pain.has(player):
                curePercent -= Pain.get(player).stacks * 50
            if BookPhysPunEffect.has(player):
                curePercent += 30
            return curePercent


        def cureBySleep(self, player):
            
            if rra(player, self.getCurePer(player)):  # 判定成功时，消耗所有的rezA和rezB
                Notice.add('成功治愈！')
                PhysRezA.clearByType(player)
                PhysRezB.clearByType(player)
                BookPhysPunEffect.clearByType(player)
                bonus = 2 + Physique.getS(player)/2
                Notice.add('降低了%s点严重程度！'%bonus)
                Notice.add('提升了%s点身体素质！'%bonus)
                if BookPhysPunEffect.has(player):
                    BookPhysPunEffect.clearByType(player)
                    s = r2(player.severity * 0.05)
                    player.severity -= s
                    Notice.add('由于学习成果：《呼吸训练》，额外降低了%s点严重程度！' % s)
                player.severity -= 0.01 * bonus
                player.physical += 0.01 * bonus

                self.clear(player)

        def afterSleepAction(self, player):
            if self.stacks == 0 and rra(player, self.getCurePer(player)/4):
                Notice.add('一觉醒来，你的受伤已经治愈！')
                PhysRezA.clearByType(player)
                PhysRezB.clearByType(player)
                BookPhysPunEffect.clearByType(player)
                bonus = 2 + Physique.getS(player)/2
                bonus = int(bonus*0.5)
                Notice.add('降低了%s点严重程度！'%bonus)
                Notice.add('提升了%s点身体素质！'%bonus)
                if BookPhysPunEffect.has(player):
                    BookPhysPunEffect.clearByType(player)
                    s = r2(player.severity * 0.05)
                    player.severity -= s
                    Notice.add('由于学习成果：《呼吸训练》，额外降低了%s点严重程度！' % s)
                player.severity -= 0.01 * bonus
                player.physical += 0.01 * bonus

                self.clear(player)


    class PhysProb(Effect):
        id = 223
        name = '过劳'
        kind = '状态'
        maxDuration = 3
        maxStacks = 99
        info = '进行工作类日程时有一定概率获得。\n' \
            '获得该状态时有小概率{color=#FF4500}降低{/color}身体素质和工作能力。\n入睡前大于3层以上时将在第二日{color=#FF4500}转化{/color}为生病。'
        info_p = '进行工作类日程时有一定概率获得。\n' \
            '获得该状态时各有20%的概率{color=#FF4500}降低{/color}2点身体素质和2点工作能力。\n入睡前大于3层以上时将在第二日{color=#FF4500}转化{/color}为生病。'
        ad = '痛苦来自于无法衡量工作和身体健康。'

        def enableAction(self, player):
            if rra(player, 20):
                Notice.add('由于过劳，{color=#FF4500}降低{/color}2点身体素质。')
                player.physical -= 0.02
            if rra(player, 20):
                Notice.add('由于过劳，{color=#FF4500}降低{/color}2点工作能力。')
                player.working -= 0.02

        @classmethod
        def add(cls, player, times=1):
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                Stat.record(player, cls)
                if PhysRezA.has(player):
                    Notice.add('添加%s：%s！{color=#FF4500}抵消{/color}1层状态：良好的睡眠！' % (cls.kind, cls.name))
                    PhysRezA.subByType(player)
                elif PhysRezB.has(player):
                    Notice.add('添加%s：%s！{color=#FF4500}抵消{/color}1层状态：良好的运动！' % (cls.kind, cls.name))
                    PhysRezB.subByType(player)
                else:
                    cls.defaultAddEffect(player)

        def afterSleepAction(self, player):
            if self.stacks >= 4:
                if not BookConcEffect.has(player):
                    Notice.add('过劳层数大于3，{color=#FF4500}转化{/color}为状态：生病！')
                    PhysPun.add(player)
                    self.clear(player)
                elif self.duration == 0:
                    self.duration += 1


    class MentProb(Effect):
        id = 224
        name = '焦虑'
        kind = '状态'
        maxDuration = 3
        maxStacks = 99
        info = '进行工作类日程时有一定概率获得。\n' \
            '获得该状态时有小概率{color=#FF4500}降低{/color}写作技巧和工作能力。\n入睡前大于3层以上时将在第二日{color=#FF4500}转化{/color}为偏执。'
        info_p = '进行工作类日程时有一定概率获得。\n' \
            '获得该状态时各有20%的概率{color=#FF4500}降低{/color}2点写作技巧和2点工作能力。\n入睡前大于3层以上时将在第二日{color=#FF4500}转化{/color}为偏执。'
        ad = '我难以呼吸，总觉有何未知的存在正追赶着我，挤压着我将我向前推进。'

        def enableAction(self, player):
            if rra(player, 20):
                Notice.add('由于焦虑，{color=#FF4500}降低{/color}2点写作技巧。')
                player.writing -= 0.01
            if rra(player, 20):
                Notice.add('由于焦虑，{color=#FF4500}降低{/color}2点工作能力。')
                player.working -= 0.01

        @classmethod
        def add(cls, player, times=1):
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                Stat.record(player, cls)
                if MentRezA.has(player):
                    Notice.add('添加%s：%s！{color=#FF4500}抵消{/color}1层状态：精神的释放!' % (cls.kind, cls.name))
                    MentRezA.subByType(player)
                elif MentRezB.has(player):
                    Notice.add('添加%s：%s！{color=#FF4500}抵消{/color}1层状态：精神的平复！' % (cls.kind, cls.name))
                    MentRezB.subByType(player)
                else:
                    cls.defaultAddEffect(player)

        def afterSleepAction(self, player):
            if self.stacks >= 4:
                if not BookConcEffect.has(player):
                    Notice.add('焦虑层数大于3，{color=#FF4500}转化{/color}为偏执！')
                    MentPun.add(player)
                    self.clear(player)
                elif self.duration == 0:
                    self.duration += 1



    class PhysRezA(Effect):
        id = 230
        name = '良好的睡眠'
        kind = '状态'
        maxDuration = 2
        maxStacks = 99
        info = '在床上休息或过夜有概率获得。\n' \
            '{color=#7CFC00}抵消{/color}相同层数的过劳。\n' \
            '每层都能提升较多的治愈生病和受伤的恢复率。'
        info_p = '在床上休息后随机获得1~3层，过夜有10%的概率获得1层。\n' \
            '{color=#7CFC00}抵消{/color}相同层数的过劳。\n' \
            '每层都能提升15%治愈生病和受伤的恢复率。'
        ad = '“梦中的我穿梭在林地的高耸树木之间，又越过由刀刃制成的阶梯和源头是一幅画的宽广河流……”'

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
                    Notice.add('添加%s：%s！{color=#7CFC00}抵消{/color}1层状态：过劳！' % (cls.kind, cls.name))
                    PhysProb.subByType(player)
                else:
                    cls.defaultAddEffect(player)


    class PhysRezB(Effect):
        id = 231
        name = '良好的运动'
        kind = '状态'
        maxDuration = 2
        maxStacks = 99
        info = '进行运动类日程后或外出有概率获得。\n' \
            '{color=#7CFC00}抵消{/color}相同层数过劳。\n' \
            '每层都能提升较多的治愈生病和受伤的恢复率。'
        info_p = '进行部分运动类日程后随机获得0~2层，外出探索有25%的概率获得1层。\n' \
            '{color=#7CFC00}抵消{/color}相同层数过劳。\n' \
            '每层都能提升15%治愈生病和受伤的恢复率。'
        ad = '“我的心脏以不同于以往的速度躁动跳跃，仿佛我的肋骨也无法阻拦，如若要挣脱这副残破躯壳的限制……”'

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
                    Notice.add('添加%s：%s！{color=#7CFC00}抵消{/color}1层状态：过劳！' % (cls.kind, cls.name))
                    PhysProb.subByType(player)
                else:
                    cls.defaultAddEffect(player)


    class MentRezA(Effect):
        id = 232
        name = '精神的释放'
        kind = '状态'
        maxDuration = 2
        maxStacks = 99
        info = '完成委托时根据消耗的灵感层数获得。\n' \
            '{color=#7CFC00}抵消{/color}相同层数焦虑。'
        info_p = '完成委托时根据消耗的灵感及写作素材层数获得，每10层灵感及写作素材都可以获得1层。\n' \
            '{color=#7CFC00}抵消{/color}相同层数焦虑。'
        ad = '“我掀开盖骨，将我的脑脊液倒进我前方的键盘，于是我的双手在键盘上如起舞的天鹅，我所理解的语言即以字符的形式在屏幕上显现，此时此刻的愉悦紧紧环绕着我的气管，似要将我缢杀。”'

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
                    Notice.add('添加%s：%s！{color=#7CFC00}抵消{/color}1层状态：焦虑！' % (cls.kind, cls.name))
                    MentProb.subByType(player)
                else:
                    cls.defaultAddEffect(player)


    class MentRezB(Effect):
        id = 233
        name = '精神的平复'
        kind = '状态'
        maxDuration = 2
        maxStacks = 99
        info = '进行休息类日程时有概率获得，周末时每完成一项日程都有大概率获得1层。\n' \
            '{color=#7CFC00}抵消{/color}相同层数焦虑。'  # 33%
        info_p = '进行部分休息类日程后随机获得0~2层，周末时每完成一项日程都有60%的概率获得1层。\n' \
            '{color=#7CFC00}抵消{/color}相同层数焦虑。'  # 33%
        ad = '“我呼吸，尽可能地呼吸。也许下一刻我就失去了呼吸的权利。”'

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
                    Notice.add('添加%s：%s！{color=#7CFC00}抵消{/color}1层状态：焦虑！' % (cls.kind, cls.name))
                    MentProb.subByType(player)
                else:
                    cls.defaultAddEffect(player)


    class Soreness(Effect):
        id = 240
        name = '酸痛'
        kind = '状态'
        maxDuration = 4
        maxStacks = 99
        info = '每次进行运动时获得4层，拥有该状态时进行任意日程都会获得1层。\n' \
            '每层酸痛都会使起床时额外{color=#FF4500}消耗{/color}少量精神状态。\n' \
            '再次获取不会刷新该状态的持续时间，持续时间结束时获得体弱。\n\n进行拉伸运动可{color=#7CFC00}转化{/color}该状态为体魄。'
        info_p = '每次进行运动时获得4层，拥有该状态时进行任意日程都会获得1层。\n' \
            '每层酸痛都会使起床时额外{color=#FF4500}消耗{/color}0.5点精神状态。\n' \
            '再次获取不会刷新该状态的持续时间，持续时间结束时获得1层体弱。\n\n进行拉伸运动可{color=#7CFC00}转化{/color}该状态为体魄。'
        ad = '“我感觉每根骨头中间的接缝处都积满了淤泥，肌肉与肌肉之间的连接变得干枯易碎。”'

        @classmethod
        def defaultAddEffect(cls, player):  # 默认的add函数，禁止重写
            cls.notResetDurationAddEffect(player)

        def afterSleepAction(self, player):
            m = r2(0.5 * self.stacks * f())
            player.mental -= m
            Notice.add('由于酸痛，额外消耗了%s点精神状态。' % m)

        def timeUpAction(self, player):
            Debilitated.add(player)

        def afterTaskAction(self, player, task):  # 日程后
            self.add(player)


    class Inspiration(Effect):
        id = 241
        name = '灵感'
        kind = '状态'
        maxDuration = 4
        maxStacks = 99
        info = '当进行的日程与上一个日程不同时获得。\n' \
            '完成委托将消耗该增益，每层都能{color=#7CFC00}提升{/color}获得的精神的释放层数和委托价值。\n' \
            '再次获取不会刷新该状态的持续时间，持续时间结束时获得偏执。\n\n进行记录想法可{color=#7CFC00}转化{/color}该状态为写作素材。'
        info_p = '当进行的日程与上一个日程不同时获得1层。\n' \
            '完成委托，随笔写作或集中写作将消耗该增益，每层都能{color=#7CFC00}提升{/color}获得的精神的释放层数和委托价值。\n' \
            '再次获取不会刷新该状态的持续时间，持续时间结束时获得1层偏执。\n\n进行记录想法可{color=#7CFC00}转化{/color}该状态为写作素材。'
        ad = '用所爱之人的头颅做成的飞机杯……这个点子似乎很有趣啊……'
 
        @classmethod
        def defaultAddEffect(cls, player):  # 默认的add函数，禁止重写
            cls.notResetDurationAddEffect(player)

        def afterTaskAction(self, player, task):  # 日程后
            if task.name == '记录想法':
                FixedInspiration.add(player, int(self.stacks * 0.8))
                self.clear(player)

        def timeUpAction(self, player):
            MentPun.add(player)


    class Satiety(Effect):
        id = 242
        name = '饱腹'
        kind = '状态'
        maxDuration = 1
        maxStacks = 99
        info = '使用部分食物获得。\n专注度小幅度{color=#FF4500}降低{/color}。\n食物恢复的精神状态随层数大幅{color=#FF4500}降低{/color}，层数较高时食用食物可能会{color=#FF4500}消耗{/color}精神状态。\n进行日程后有大概率移除状态的层数。'
        info_p = '使用部分食物获得。\n专注度{color=#FF4500}降低{/color}10%。\n食物恢复的精神状态每层都会{color=#FF4500}降低{/color}70%，层数较高时食用食物可能会{color=#FF4500}消耗{/color}精神状态。\n进行日程后有75%的概率移除1层该状态。'
        ad = '你腹痛难耐，悔恨自己暴食的行为。'

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
        name = '忧虑'
        kind = '状态'
        maxDuration = 7
        maxStacks = 99
        info = '无法进行写作。'
        info_p = '无法进行随笔写作，完成委托，集中写作日程。'
        ad = '你对自己可能会丢掉工作这件事的担忧占据了大脑。'

        def enableAction(self, player):
            self.duration = ra(player, 4, 6)


    class Caffeine(Effect):
        id = 244
        name = '失眠'
        kind = '状态'
        maxDuration = 1
        maxStacks = 99
        info = '睡眠消耗的精神状态随层数{color=#FF4500}提升{/color}。'
        info_p = '每层都会{color=#FF4500}提升{/color}10%睡眠消耗的精神状态。'
        ad = '试图干涉生物体生命活动的内在节律性的结果。'

        def addStackAction(self, player):  # 每次添加层数的操作，一般是某些根据层数给予效果的Effect需要设置
            player.deteriorateConsumption += 0.1

        def subStackAction(self, player):  # 减少层数的操作，前者的反向函数
            player.deteriorateConsumption -= 0.1

    class Smoking(Effect):
        id = 245
        name = '难耐'
        kind = '状态'
        maxDuration = 7
        maxStacks = 99
        info = '严重程度随层数百分比{color=#FF4500}提升{/color}。'
        info_p = '每层都会{color=#FF4500}提升{/color}12%的严重程度。'
        ad = '也许我不该抽烟的。'

        def addStackAction(self, player):
            player.severityRegarded += 0.12

        def subStackAction(self, player):
            player.severityRegarded -= 0.12

    class Pain(Effect):
        id = 246
        name = '痛苦'
        kind = '状态'
        maxDuration = 7
        maxStacks = 99
        info = '严重程度，睡眠消耗的精神状态和受伤的治愈难度随层数百分比{color=#FF4500}提升{/color}。'
        info_p = '每层都会{color=#FF4500}提升{/color}15%的严重程度和睡眠消耗的精神状态，并降低50%受伤的治愈率。'
        ad = '“终于有活着的感觉了……\n不过放着不管的话手会变得像烤乌贼那样的。”'

        def addStackAction(self, player):
            player.severityRegarded += 0.15
            player.deteriorateConsumption += 0.15

        def subStackAction(self, player):
            player.severityRegarded -= 0.15
            player.deteriorateConsumption -= 0.15

    class EffectGameModule2(Effect):
        id = 247
        name = '失语'
        kind = '状态'
        maxDuration = 2
        maxStacks = 1
        info = '无法进行写作类日程，超大幅度{color=#FF4500}降低{/color}工作能力。'
        info_p = '无法进行写作类日程，{color=#FF4500}降低{/color}99%的工作能力。'
        ad = '现在我醒来了，我仍能看到那些颜色……'

        def addStackAction(self, player):
            player.workingRegarded -= 0.99
            player.canWrite -= 1

        def subStackAction(self, player):
            player.workingRegarded += 0.99
            player.canWrite += 1

    class EffectGameModule2_1(Effect):
        id = 248
        name = '死亡-五晶的怜悯'
        kind = '状态'
        maxDuration = 3
        maxStacks = 1
        info = '精神状态消耗{color=#FF4500}提升{/color}了，精神状态恢复{color=#FF4500}提升{/color}了。'
        info_p = '精神状态消耗{color=#FF4500}降低{/color}20%，精神状态恢复{color=#FF4500}降低{/color}20%。'
        ad = '*这里只有沉默。*'

        def addStackAction(self, player):
            player.basicConsumption += 0.2
            player.basicRecovery -= 0.2

        def subStackAction(self, player):
            player.basicConsumption -= 0.2
            player.basicRecovery += 0.2
    
    class EffectGameModule2_2(Effect):
        id = 248
        name = '梦境-白影的幻想'
        kind = '状态'
        maxDuration = 1
        maxStacks = 6
        info = '写作能力暂时{color=#7CFC00}提升{/color}了。'
        info_p = '写作能力暂时{color=#7CFC00}提升{/color}了10%，效果可叠加。'
        ad = '“来梦里吧，我会让你得到无限的幸福。”'

        def addStackAction(self, player):
            player.writingRegarded += 0.05

        def subStackAction(self, player):
            player.writingRegarded -= 0.05
    
    class EffectGameModule2_3(Effect):
        id = 248
        name = '欲望-徵羽微凉的贪婪'
        kind = '状态'
        maxDuration = 1
        maxStacks = 6
        info = '下次写作时价值大幅度{color=#7CFC00}提升{/color}。'
        info_p = '下次写作时价值{color=#7CFC00}提升{/color}30%。'
        ad = '“即使是在这片钢筋丛林里，我们也要做最危险的野兽。”'


    class SleepReward(Effect):
        id = 310
        name = '整备'
        kind = '增益'
        maxDuration = 1
        maxStacks = 99
        info = '在床上休息或小睡转化睡意后获得。\n' \
            '随层数{color=#7CFC00}提升{/color}专注度和工作速度，并{color=#7CFC00}降低{/color}精神状态消耗。\n\n{color=#ffff00}存在此增益时，全力工作不会受到过劳惩罚。{/color}'
        info_p = '在床上休息或小睡转化睡意后获得。\n移除全力工作施加的2层过劳。' \
            '每层都会{color=#7CFC00}提升{/color}5%的专注度和10%的工作速度，并{color=#7CFC00}降低{/color}5%的精神状态消耗。\n\n{color=#ffff00}存在此增益时，全力工作不会受到过劳惩罚。{/color}'
        ad = '看来你已经学会如何利用自己的身体了。'

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
        name = '释然'
        kind = '增益'
        maxDuration = 3
        maxStacks = 1
        info = '结束委托后获得。\n' \
            '专注度{color=#7CFC00}提升{/color}，精神状态恢复{color=#7CFC00}提升{/color}。'
        info_p = '结束委托后获得。\n' \
            '专注度{color=#7CFC00}提升{/color}25%，精神状态恢复{color=#7CFC00}提升{/color}25%。'
        ad = '我写爽了。'

        def enableAction(self, player):
            player.basicConcentration += 25
            player.basicRecovery += 0.25

        def disableAction(self, player):
            player.basicConcentration -= 25
            player.basicRecovery -= 0.25


    class WorkReward(Effect):
        id = 312
        name = '成就感'
        kind = '增益'
        maxDuration = 7
        maxStacks = 1
        info = '完成本周全部工作时有概率获得。\n' \
            '工作速度{color=#7CFC00}提升{/color}。'
        info_p = '完成本周全部工作时有75%的概率获得，超额完成工作时（>120%）必定获得。\n' \
            '工作速度{color=#7CFC00}提升{/color}20%。'
        ad = '从虚幻的数据中获得虚假的感动。'

        def enableAction(self, player):
            self.duration = ra(player, 4, 7)
            player.workSpeed += 0.2

        def disableAction(self, player):
            player.workSpeed -= 0.2


    


    class CleanReward(Effect):
        id = 314
        name = '整洁的房间'
        kind = '增益'
        maxDuration = 4
        maxStacks = 1
        info = '进行整理房间日程后获得。\n' \
            '在家中进行日程时，精神状态消耗大幅度{color=#7CFC00}降低{/color}，日程的专注度大幅度{color=#7CFC00}提升{/color}。'
        info_p = '进行整理房间日程后获得。\n' \
            '在家中进行日程时，精神状态消耗{color=#7CFC00}降低{/color}40%，对家中进行的日程的专注度{color=#7CFC00}提升{/color}40%。'
        ad = '久违的大扫除让你从仪式感中获得些许慰藉。'

        def enableAction(self, player):
            self.duration = ra(player, 2, 4)
            player.homeConsumption -= 0.4  # 家中消耗率
            player.homeConcentration += 40  # 家中专注度

        def disableAction(self, player):
            player.homeConsumption += 0.4  # 家中消耗率
            player.homeConcentration -= 40  # 家中专注度


    class ReadReward(Effect):
        id = 315
        name = '领悟'
        kind = '增益'
        maxDuration = 2
        maxStacks = 1
        info = '阅读部分书籍或进行除完成委托外的写作类日程后获得。\n' \
            '写作技巧暂时{color=#7CFC00}提升{/color}，进行写作时，{color=#7CFC00}提升{/color}写作价值度。'
        info_p = '阅读部分书籍或进行除完成委托外的写作类日程后获得。\n' \
            '写作技巧暂时{color=#7CFC00}提升{/color}10%，进行写作时，{color=#7CFC00}提升{/color}20%的写作价值度。'
        ad = '如此如此……这般这般……这写法用进我的下一篇随笔里绝对出色……！'

        def enableAction(self, player):
            player.writeValuable += 0.2
            player.writingRegarded += 0.1

        def disableAction(self, player):
            player.writeValuable -= 0.2
            player.writingRegarded -= 0.1


    class FocusAttention(Effect):
        id = 316
        name = '心流'
        kind = '增益'
        maxDuration = 1
        maxStacks = 2
        info = '进行日程将消耗1层本状态，使本次日程的判定结果大幅度{color=#7CFC00}提升{/color}。'
        info_p = '进行日程将消耗1层本状态，使本次日程的专注度{color=#7CFC00}提升{/color}60%。'
        ad = '你从未像如此一样渴望做好一件事。'

        def enableAction(self, player):
            player.basicConcentration += 60

        def disableAction(self, player):
            player.basicConcentration -= 60

        def afterTaskAction(self, player, task):
            self.sub(player)


    class Novelty(Effect):
        id = 317
        name = '见闻'
        kind = '增益'
        maxDuration = 2
        maxStacks = 1
        info = '外出探索后有概率获得。\n写作技巧暂时{color=#7CFC00}提升{/color}。'
        info_p = '外出探索后有50%的概率获得。\n写作技巧暂时{color=#7CFC00}提升{/color}10%。'
        ad = '才不是出去玩呢！这叫采风！'

        def enableAction(self, player):
            player.writingRegarded += 0.1

        def disableAction(self, player):
            player.writingRegarded -= 0.1


    class AppleFlavor(Effect):
        id = 318
        name = '苹果口味'
        kind = '增益'
        maxDuration = 2
        maxStacks = 1
        info = '工作速度和工作能力各小幅度{color=#7CFC00}提升{/color}。'
        info_p = '工作速度和工作能力各{color=#7CFC00}提升{/color}10%。'
        ad = '这个味道让你想起了在你病床边为你削苹果的人。'

        def enableAction(self, player):
            player.workSpeed += 0.1
            player.workingRegarded += 0.1

        def disableAction(self, player):
            player.workSpeed -= 0.1
            player.workingRegarded -= 0.1


    class CitrusFlavor(Effect):
        id = 319
        name = '柑橘口味'
        kind = '增益'
        maxDuration = 2
        maxStacks = 1
        info = '身体素质，写作技巧和工作能力暂时{color=#7CFC00}提升{/color}。'
        info_p = '身体素质，写作技巧和工作能力暂时{color=#7CFC00}提升{/color}10%。'
        ad = '这个味道让你想起了血液和胆汁的气味。'

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
        name = '准备运动'
        kind = '增益'
        maxDuration = 1
        maxStacks = 1
        info = '对运动类日程的专注度大幅度{color=#7CFC00}提升{/color}。'
        info_p = '对运动类日程的专注度{color=#7CFC00}提升{/color}30%。'
        ad = '“有备而无患。”'

        def enableAction(self, player):  # 每次添加层数的操作，一般是某些根据层数给予效果的Effect需要设置
            player.sportConcentration += 30

        def disableAction(self, player):  # 减少层数的操作，前者的反向函数
            player.sportConcentration -= 30

    class Entrance(Effect):
        id = 322
        name = '清醒'
        kind = '增益'
        maxDuration = 1
        maxStacks = 99
        info = '获得大量专注度{color=#7CFC00}提升{/color}，同时严重程度随层数百分比{color=#7CFC00}降低{/color}。\n进行任意日程后有大概率消耗该增益，结束时获得难耐。'
        info_p = '{color=#7CFC00}提升{/color}30%的专注度，同时每层都会{color=#7CFC00}降低{/color}10%的严重程度。\n进行任意日程后有50%的概率消耗该增益，结束时获得难耐。'
        ad = '烟草让能让痛苦消弭。'

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
        name = '松弛'
        kind = '增益'
        maxDuration = 1
        maxStacks = 1
        info = '在床上休息或外出获得。\n在物品栏中可以快速阅读一本专业类书籍并消耗1层本状态，获得书籍效果并使书籍进入冷却时间。'
        info_p = '在床上休息或外出获得。\n在物品栏中可以快速阅读一本专业类书籍并消耗1层本状态，获得书籍效果并使书籍进入冷却时间。'
        ad = '“你突然想学习，这倒是很稀有。”'

    
    class MeetingReward1(Effect):
        id = 324
        name = '指导：专注'
        kind = '增益'
        maxDuration = 7
        maxStacks = 1
        info = '参与周研讨会后获得。\n' \
            '对工作类日程的专注度{color=#7CFC00}提升{/color}。'
        info_p = '参与周研讨会后获得。\n' \
            '对工作类日程的专注度{color=#7CFC00}提升{/color}40%。'
        ad = '“把你的注意力聚焦于工作上。”'

        def enableAction(self, player):
            self.duration = ra(player, 5, 7)
            player.workConcentration += 40

        def disableAction(self, player):
            player.workConcentration -= 40
    

    class MeetingReward2(Effect):
        id = 325
        name = '指导：激励'
        kind = '增益'
        maxDuration = 7
        maxStacks = 1
        info = '参与周研讨会后获得。\n' \
            '工作能力{color=#7CFC00}提升{/color}。'
        info_p = '参与周研讨会后获得。\n' \
            '工作能力{color=#7CFC00}提升{/color}30%。'
        ad = '“努力！努力！在这个时代不卷的人已经被淘汰了！”'

        def enableAction(self, player):
            self.duration = ra(player, 5, 7)
            player.workingRegarded += 0.3

        def disableAction(self, player):
            player.workingRegarded -= 0.3
    
    class MeetingReward3(Effect):
        id = 326
        name = '指导：坚实'
        kind = '增益'
        maxDuration = 7
        maxStacks = 1
        info = '参与周研讨会后获得。\n' \
            '进行完成工作日程时，精神状态消耗{color=#7CFC00}降低{/color}，同时{color=#7CFC00}提升{/color}完成的进度。'
        info_p = '参与周研讨会后获得。\n' \
            '进行完成工作日程时，精神状态消耗{color=#7CFC00}降低{/color}30%，同时{color=#7CFC00}提升{/color}15%完成的进度。'
        ad = '“有些人总在工位睡觉，这是不好的……你们应该……”'

        def enableAction(self, player):
            self.duration = ra(player, 5, 7)
    
    class MeetingReward4(Effect):
        id = 327
        name = '指导：技巧'
        kind = '增益'
        maxDuration = 7
        maxStacks = 1
        info = '参与周研讨会后获得。\n' \
            '进行小睡日程时，额外{color=#7CFC00}获得{/color}2层整备，转化睡意时{color=#7CFC00}恢复{/color}的精神状态翻倍。'
        info_p = '参与周研讨会后获得。\n' \
            '进行小睡日程时，额外{color=#7CFC00}获得{/color}2层整备，转化睡意时{color=#7CFC00}恢复{/color}的精神状态翻倍。'
        ad = '“在工作中你们要学会技巧……”'

        def enableAction(self, player):
            self.duration = ra(player, 5, 7)
    

    class MeetingReward5(Effect):
        id = 328
        name = '指导：分心'
        kind = '增益'
        maxDuration = 7
        maxStacks = 1
        info = '参与周研讨会后获得。\n' \
            '进行偷懒日程时，消耗的精神状态{color=#FF4500}提升{/color}，但是在偷懒中选择读书时将立刻读完整本书。'
        info_p = '参与周研讨会后获得。\n' \
            '进行偷懒日程时，消耗的精神状态{color=#FF4500}提升{/color}20%，但是在偷懒中选择读书时将立刻读完整本书。'
        ad = '“一心二用还不够，你们必须一心三用！……”'

        def enableAction(self, player):
            self.duration = ra(player, 5, 7)
    
    class MeetingReward6(Effect):
        id = 329
        name = '指导：积累'
        kind = '增益'
        maxDuration = 7
        maxStacks = 1
        info = '参与周研讨会后获得。\n' \
            '立刻完成20%的工作进度，同时进行偷懒日程时，完成的工作进度{color=#7CFC00}提升{/color}。'
        info_p = '参与周研讨会后获得。\n' \
            '立刻完成20%的工作进度，同时进行偷懒日程时，完成的工作进度{color=#7CFC00}提升{/color}30%。'
        ad = '“回想起以往的工作内容，来对待新的内容……”'

        def enableAction(self, player):
            self.duration = ra(player, 5, 7)
            player.achievedGoal += r2(player.goal * 0.2)
    
    class MeetingReward7(Effect):
        id = 330
        name = '指导：压力'
        kind = '增益'
        maxDuration = 7
        maxStacks = 1
        info = '参与周研讨会后获得。\n' \
            '起床时必定获得紧迫。'
        info_p = '参与周研讨会后获得。\n' \
            '起床时必定{color=#7CFC00}获得{/color}紧迫。'
        ad = '“这周的工作再完成不了……你们就都给我扫地出门！”'

        def enableAction(self, player):
            self.duration = ra(player, 5, 7)

    class MeetingReward8(Effect):
        id = 330
        name = '指导：放松'
        kind = '增益'
        maxDuration = 7
        maxStacks = 1
        info = '参与周研讨会后获得。\n' \
            '工作消耗的精神状态大幅{color=#7CFC00}降低{/color}。'
        info_p = '参与周研讨会后获得。\n' \
            '工作消耗的精神状态{color=#7CFC00}降低{/color}50%。'
        ad = '“上周的工作完成的还不错，值得表扬……”'

        def enableAction(self, player):
            self.duration = ra(player, 5, 7)
            player.workConsumption -= 0.5

        def disableAction(self, player):
            player.workConsumption += 0.5
            
  

    class Physique(Effect):
        id = 300
        name = '体魄'
        kind = '增益'
        maxDuration = -1
        maxStacks = 99
        info = '由拉伸运动转化酸痛获得。\n' \
            '起床时根据层数{color=#7CFC00}恢复{/color}精神状态并获得身体素质。\n每层体魄都能{color=#7CFC00}提升{/color}受伤和生病的治愈恢复率，以及以及治愈成功后获得的奖励。\n\n每天有概率失去一半，层数越多概率越大。'
        info_p = '由拉伸运动转化酸痛获得。\n' \
            '起床时{color=#7CFC00}恢复{/color}3*层数的精神状态，每拥有4层体魄，都能在起床时获得1点身体素质。\n每层体魄都能{color=#7CFC00}提升{/color}5%受伤和生病的治愈恢复率，以及治愈成功后获得的奖励。\n\n每天有2%*体魄层数的概率失去一半。'
        ad = '你终于可以说自己是有点肌肉的人了。'

        def afterSleepAction(self, player):
            m = r2(3 * self.stacks * f())

            if HallukeItem1.has(player):
                m *= 1.5

            player.mental += m
            Notice.add('由于体魄，恢复了%s点精神状态。' % m)

            g = int(self.stacks/4)
                    
            if g > 0:
                Notice.add('由于体魄，提升了%s点身体素质。' % g)
                player.physical += 0.01*g

            per = 2 * self.stacks
            if HallukeItem1.has(player):
                per *= 0.5

            if rra(player, per):
                s = int(self.stacks/2)
                self.sub(player, s)
                Notice.add('体魄随时间失去了%s层。'%s)



    class FixedInspiration(Effect):
        id = 301
        name = '写作素材'
        kind = '增益'
        maxDuration = -1
        maxStacks = 99
        info = '由记录想法{color=#7CFC00}转化{/color}灵感获得。\n' \
            '可作为灵感在写作中被消耗。'
        info_p = '由记录想法{color=#7CFC00}转化{/color}灵感获得。\n' \
            '可作为灵感在写作中被消耗。'
        ad = '不离手的照片、老人开的地铁站、离开、蚂蚁吃掉了骨柄、重新回到地铁站、我也是懦弱的人、亲吻、挣扎。'

        def afterWriting(self, player, scale):
            if scale != 0:  # 当本次写作会返回写作素材时
                self.stacks = int(self.stacks * scale)
                Notice.add('获得了%s层写作素材！' % newStacks)
            else:
                self.clear(player)


    # D: dependence
    # W: withdrawal
    # E: effect


    class DrugDA(Effect):
        id = 403
        name = '药物依赖{font=arial.ttf}α{/font}'
        kind = '药物反应'
        maxDuration = 2
        maxStacks = 99
        info = '过夜时提升等同于层数的对应药物抗药性。\n使用药物{font=arial.ttf}α{/font}后解除。\n' \
            '持续时间结束后{color=#FF4500}转化{/color}为戒断反应{font=arial.ttf}α{/font}。'
        info_p = '过夜时提升等同于层数的对应药物抗药性。\n使用药物{font=arial.ttf}α{/font}后解除。\n' \
            '持续时间结束后{color=#FF4500}转化{/color}为戒断反应{font=arial.ttf}α{/font}。'
        ad = '你偶尔会感到有些恶心。'

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
        name = '药物依赖{font=arial.ttf}β{/font}'
        kind = '药物反应'
        maxDuration = 2
        maxStacks = 99
        info = '过夜时提升等同于层数的对应药物抗药性。\n使用药物{font=arial.ttf}β{/font}后解除。\n' \
            '持续时间结束后{color=#FF4500}转化{/color}为戒断反应{font=arial.ttf}β{/font}。'
        info_p = '过夜时提升等同于层数的对应药物抗药性。\n使用药物{font=arial.ttf}β{/font}后解除。\n' \
            '持续时间结束后{color=#FF4500}转化{/color}为戒断反应{font=arial.ttf}β{/font}。'
        ad = '你偶尔会感到有些头晕。'

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
        name = '药物依赖{font=arial.ttf}γ{/font}'
        kind = '药物反应'
        maxDuration = 2
        maxStacks = 99
        info = '过夜时提升等同于层数的对应药物抗药性。\n使用药物{font=arial.ttf}γ{/font}后解除。\n' \
            '持续时间结束后{color=#FF4500}转化{/color}为戒断反应{font=arial.ttf}γ{/font}。'
        info_p = '过夜时提升等同于层数的对应药物抗药性。\n使用药物{font=arial.ttf}γ{/font}后解除。\n' \
            '持续时间结束后{color=#FF4500}转化{/color}为戒断反应{font=arial.ttf}γ{/font}。'
        ad = '你偶尔会眼前一黑。'

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
        name = '戒断反应{font=arial.ttf}α{/font}'
        kind = '药物反应'
        maxDuration = 2
        maxStacks = 1
        info = '专注度大幅度{color=#FF4500}降低{/color}，精神状态消耗大幅度{color=#FF4500}提升{/color}。\n'\
            '你需要尽快服用任意剂量的{font=arial.ttf}α{/font}药物，并且在第二天早上才会恢复。\n' \
            '持续时间结束{color=#FF4500}转化{/color}为衰退。'
        info_p = '专注度{color=#FF4500}降低{/color}100%，精神状态消耗{color=#FF4500}提升{/color}100%。\n'\
            '你需要尽快服用任意剂量的{font=arial.ttf}α{/font}药物，并且在第二天早上才会恢复。\n' \
            '持续时间结束{color=#FF4500}转化{/color}为衰退。'
        ad = '反胃感使你频繁跑去厕所呕吐。'

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
        name = '戒断反应{font=arial.ttf}β{/font}'
        kind = '药物反应'
        maxDuration = 2
        maxStacks = 1
        info = '专注度大幅度{color=#FF4500}降低{/color}，精神状态消耗大幅度{color=#FF4500}提升{/color}。\n' \
            '你需要尽快服用任意剂量的{font=arial.ttf}β{/font}药物，并且在第二天早上才会恢复。\n' \
            '持续时间结束{color=#FF4500}转化{/color}为衰退。'
        info_p = '专注度{color=#FF4500}降低{/color}100%，精神状态消耗{color=#FF4500}提升{/color}100%。\n' \
            '你需要尽快服用任意剂量的{font=arial.ttf}β{/font}药物，并且在第二天早上才会恢复。\n' \
            '持续时间结束{color=#FF4500}转化{/color}为衰退。'
        ad = '重度胸闷让你难以专注工作。'

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
        name = '戒断反应{font=arial.ttf}γ{/font}'
        kind = '药物反应'
        maxDuration = 2
        maxStacks = 1
        info = '专注度大幅度{color=#FF4500}降低{/color}，精神状态消耗大幅度{color=#FF4500}提升{/color}。\n' \
            '你需要尽快服用任意剂量的{font=arial.ttf}γ{/font}药物，并且在第二天早上才会恢复。\n' \
            '持续时间结束{color=#FF4500}转化{/color}为衰退。'
        info_p = '专注度{color=#FF4500}降低{/color}100%，精神状态消耗{color=#FF4500}提升{/color}100%。\n' \
            '你需要尽快服用任意剂量的{font=arial.ttf}γ{/font}药物，并且在第二天早上才会恢复。\n' \
            '持续时间结束{color=#FF4500}转化{/color}为衰退。'
        ad = '你难以呼吸。'

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
        name = '药物作用{font=arial.ttf}α{/font}'
        kind = '药物反应'
        maxDuration = 1
        maxStacks = 1
        info = '工作类日程专注度小幅度{color=#7CFC00}提升{/color}，但精神状态消耗也会小幅度{color=#FF4500}提升{/color}。'
        info_p = '工作类日程专注度{color=#7CFC00}提升{/color}10%，精神状态消耗{color=#FF4500}提升{/color}10%。'
        ad = '你看不清太远的东西。'

        def enableAction(self, player):
            player.workConcentration += 10
            player.basicConsumption += 0.1

        def disableAction(self, player):
            player.workConcentration -= 10
            player.basicConsumption -= 0.1
        
        @classmethod
        def add(cls, player, times=1):  # 增加新效果或增加层数
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                if not BookBanDepEffect.has(player):
                    Stat.record(player, cls)
                    cls.defaultAddEffect(player)


    class DrugEB(Effect):
        id = 407
        name = '药物作用{font=arial.ttf}β{/font}'
        kind = '药物反应'
        maxDuration = 1
        maxStacks = 1
        info = '工作速度{color=#FF4500}降低{/color}，写作技巧幅度{color=#7CFC00}提升{/color}。'
        info_p = '工作速度{color=#FF4500}降低{/color}30%，写作技巧暂时{color=#7CFC00}提升{/color}30%。'
        ad = '你开始出现光怪陆离的幻觉。'

        def enableAction(self, player):
            player.workSpeed -= 0.3
            player.writingRegarded += 0.3

        def disableAction(self, player):
            player.workSpeed += 0.3
            player.writingRegarded -= 0.3

        @classmethod
        def add(cls, player, times=1):  # 增加新效果或增加层数
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                if not BookBanDepEffect.has(player):
                    Stat.record(player, cls)
                    cls.defaultAddEffect(player)


    class DrugEC(Effect):
        id = 408
        name = '药物作用{font=arial.ttf}γ{/font}'
        kind = '药物反应'
        maxDuration = 1
        maxStacks = 1
        info = '食物恢复的精神状态超大幅度{color=#FF4500}降低{/color}，服用药物的精神状态恢复效果{color=#FF4500}降低{/color}，但运动类日程恢复的精神状态{color=#7CFC00}提升{/color}。\n且每个日程结束后{color=#7CFC00}恢复{/color}一定的精神状态。'
        info_p = '食物恢复的精神状态{color=#FF4500}降低{/color}80%，服用药物的精神状态恢复效果{color=#FF4500}降低{/color}40%，运动类日程恢复的精神状态{color=#7CFC00}提升{/color}40%。\n且每个日程结束后{color=#7CFC00}恢复{/color}15~25*基础精神状态消耗的精神状态。'
        ad = '你的味觉突然消失了。'

        def enableAction(self, player):
            player.foodRecovery -= 0.8
            player.sportRecovery += 0.4
            player.drugRecovery -= 0.4

        def disableAction(self, player):
            player.foodRecovery += 0.8
            player.sportRecovery -= 0.4
            player.drugRecovery += 0.4

        def afterTaskAction(self, player, task):
            t = ra(player, 1500, 2500) * 0.01
            t *= MedicineC.getResScale(player)
            t *= Task.getConsScale(player)
            Notice.add('由于药物{font=arial.ttf}γ{/font}，恢复了' + r2s(t) + '点精神状态。')
            player.mental += r2(t)

        @classmethod
        def add(cls, player, times=1):  # 增加新效果或增加层数
            if times == 0:
                return
            GuideE.unlock(cls)
            for i in range(times):
                if not BookBanDepEffect.has(player):
                    Stat.record(player, cls)
                    cls.defaultAddEffect(player)


    class DrugED(Effect):
        id = 409
        name = '药物作用{font=arial.ttf}δ{/font}'
        kind = '药物反应'
        maxDuration = 7
        maxStacks = 1
        info = '不会出现其他药物的依赖反应。'
        info_p = '不会出现其他药物的依赖反应。'
        ad = '似乎没有任何头疼的感觉了，未知的躁动和其他药物的微弱反应也消失了。'


    class DrugHypnoticEffect(Effect):
        id = 410
        name = '药物作用：安眠药'
        kind = '药物反应'
        maxDuration = 1
        maxStacks = 5
        info = '随层数{color=#7CFC00}降低{/color}睡眠消耗的精神状态和专注度。'
        info_p = '{color=#7CFC00}降低{/color}10%睡眠消耗的精神状态，除此之外每层都会{color=#7CFC00}降低{/color}5%睡眠消耗的精神状态和20%专注度。'
        ad = '昏昏欲睡？也许吧。'

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
            elif self.stacks >2:
                player.severity += 1.0
            elif self.stacks >1:
                player.severity += 0.02
            
        def subStackAction(self, player):
            player.deteriorateConsumption += 0.05
            player.basicConcentration += 0.2


    class DrugIbuprofenEffect(Effect):
        id = 411
        name = '药物作用：头疼药'
        kind = '药物反应'
        maxDuration = 2
        maxStacks = 5
        info = '每完成一个日程随层数{color=#7CFC00}恢复{/color}微量精神状态。'
        info_p = '完成日程后，每层都会{color=#7CFC00}恢复{/color}2%的当前精神状态，最大每层恢复5点。\n精神状态低于0时无效。'
        ad = '食之无味，弃之可惜。\n有没有人算过到底是维持这东西的药物浓度更加划算还是用等量的钱去买正经的药来吃更划算？'

        def afterTaskAction(self, player, task):
            t = r2(0.02 * player.mental)
            if t > 5:
                t = 5.0
            elif t<0:
                t = 0
            if t>0:
                player.mental += t* self.stacks
                Notice.add('由于头疼药，恢复了' + str(t * self.stacks) + '点精神状态。')




    class DrugColdrexEffect(Effect):
        id = 412
        name = '药物作用：感冒药'
        kind = '药物反应'
        maxDuration = 2
        maxStacks = 5
        info = '{color=#FF4500}降低{/color}少量专注度，使用时若没有生病则结束该药物反应并提升大量严重程度。\n' \
            '使用后会延长生病的持续时间并根据层数{color=#7CFC00}提升{/color}生病的恢复率，但本效果结束时若仍在生病则会{color=#FF4500}降低{/color}生病的持续时间。'
        info_p = '{color=#FF4500}降低{/color}10%专注度，使用时若没有生病则结束该药物反应并提升5点严重程度。\n' \
            '使用后会延长1天生病的持续时间，每层都会{color=#7CFC00}提升{/color}10%生病的恢复率，但本效果结束时若仍在生病则会{color=#FF4500}降低{/color}2天生病的持续时间。'
        ad = '其实持续时间延长的越久代表状态越好，而持续时间即将结束代表着病情将恶化至下一个阶段。'

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


    class BookWriEffect(Effect):
        id = 500
        name = '学习成果：《于老师教我的写作技巧》'
        kind = '学识'
        maxDuration = 2
        maxStacks = 1
        info = '写作技巧{color=#7CFC00}提升{/color}。'
        info_p = '写作技巧暂时{color=#7CFC00}提升{/color}20%。'
        ad = '于老师到底是谁？写作、摄影、拍电影、做游戏……几乎各个领域都有他出现？'

        def enableAction(self, player):
            player.writingRegarded += 0.2

        def disableAction(self, player):
            player.writingRegarded -= 0.2

    class BookConcEffect(Effect):
        id = 501
        name = '学习成果：《海边的于秀爱》'
        kind = '学识'
        maxDuration = 2
        maxStacks = 1
        info = '持续时间内过劳和焦虑不会因为层数过多而转化成生病和偏执。\n持续时间结束时，每有一层过劳和焦虑都会{color=#7CFC00}降低{/color}0.5点严重程度。\n降低的严重程度之和大于10点时，额外{color=#7CFC00}降低{/color}大量严重程度。'
        info_p = '持续时间内过劳和焦虑不会因为层数过多而转化成生病和偏执。\n持续时间结束时，每有一层过劳和焦虑都会{color=#7CFC00}降低{/color}0.5点严重程度。\n降低的严重程度之和大于10点时，额外{color=#7CFC00}降低{/color}3%的严重程度。'

        def timeUpAction(self, player):
            s = PhysProb.getS(player) + MentProb.getS(player)

            if s != 0:
                e = r2(s*0.005)
                player.severity -= e
                Notice.add('由于学习成果：《海边的于秀爱》，降低了%s点严重程度！' % e)
                if s >= 10:
                    e = r2(player.severity * 0.03)
                    player.severity -= e
                    Notice.add('由于降低的严重程度之和大于10点，额外降低了%s点严重程度！' % e)

    class BookPhysPunEffect(Effect):
        id = 502
        name = '学习成果：《呼吸训练》'
        kind = '学识'
        maxDuration = 2
        maxStacks = 1
        info = '小幅度百分比{color=#7CFC00}提升{/color}生病和受伤的恢复率。\n百分比{color=#7CFC00}提升{/color}对应状态的恢复率，如果成功治愈，结束效果并{color=#7CFC00}降低{/color}大量严重程度。'
        info_p = '百分比{color=#7CFC00}提升{/color}30%生病和受伤的恢复率。\n百分比{color=#7CFC00}提升{/color}对应状态的恢复率，如果成功治愈，结束效果并{color=#7CFC00}降低{/color}3%的严重程度。'

    class BookQuickReadEffect(Effect):
        id = 503
        name = '学习成果：《量子波动速读》'
        kind = '学识'
        maxDuration = 2
        maxStacks = 4
        info = '在物品栏中可以快速阅读一本任意书籍并消耗1层本状态，获得书籍效果并使书籍进入冷却时间。'
        info_p = '在物品栏中可以快速阅读一本任意书籍并消耗1层本状态，获得书籍效果并使书籍进入冷却时间。'



    class BookWorEffect(Effect):
        id = 504
        name = '学习成果：《保持清醒的秘诀》'
        kind = '学识'
        maxDuration = 3
        maxStacks = 5
        info = '按层数{color=#7CFC00}提升{/color}工作速度，{color=#7CFC00}降低{/color}工作消耗的精神状态。'
        info_p = '每层都会{color=#7CFC00}提升{/color}10%的工作速度，{color=#7CFC00}降低{/color}5%工作消耗的精神状态。'

        def addStackAction(self, player):
            player.workSpeed += 0.1
            player.workConsumption -= 0.05

        def subStackAction(self, player):
            player.workSpeed -= 0.1
            player.workConsumption += 0.05


    class BookInsEffect(Effect):
        id = 505
        name = '感悟：《2001年的弹珠机》'
        kind = '学识'
        maxDuration = 24
        maxStacks = 1
        info = '每天起床时{color=#7CFC00}获得{/color}灵感，同时有小概率结束该效果。'
        info_p = '每天起床时{color=#7CFC00}获得{/color}灵感，同时有10%的概率结束该效果。'

        def afterSleepAction(self, player):
            Inspiration.add(player)
            if rra(player, 10):
                self.clear(player)


    class BookCMEffect(Effect):
        id = 509
        name = '感悟：《城堡与莫梭提斯》'
        kind = '学识'
        maxDuration = 7
        maxStacks = 1
        info = '每天起床时{color=#7CFC00}降低{/color}严重程度，同时有小概率结束该效果。'
        info_p = '每天起床时{color=#7CFC00}降低{/color}1点严重程度，同时有10%的概率结束该效果。'

        def afterSleepAction(self, player):
            Notice.add('由于感悟：《城堡与莫梭提斯》，{color=#7CFC00}降低{/color}1点严重程度！')
            player.severity -= 0.01
            if rra(player, 10):
                self.clear(player)


    class BookMEDEffect(Effect):
        id = 510
        name = '感悟：《药：绝望的解决手段》'
        kind = '学识'
        maxDuration = 7
        maxStacks = 5
        info = '进行工作类日程时有概率{color=#7CFC00}提升{/color}随机属性。'
        info_p = '进行工作类日程时有概率{color=#7CFC00}提升{/color}随机属性。'

        def afterTaskAction(self, player, task):  # 日程后
            if task.kind == '工作类':
                used = False
                phy = 0
                wri = 0
                wor = 0
                while rra(player, 60):
                    if rra(player, 25):
                        phy += 1
                        used = True
                    if rra(player, 25):
                        wri += 1
                        used = True
                    if rra(player, 25):
                        wor += 1
                        used = True
                if used:
                    if phy > 0:
                        player.physical += 0.01 * phy
                        Notice.add('由于感悟：《药：绝望的解决手段》，{color=#7CFC00}提升{/color}了%s点身体素质！' % phy)
                    if wri > 0:
                        player.writing += 0.01 * wri
                        Notice.add('由于感悟：《药：绝望的解决手段》，{color=#7CFC00}提升{/color}了%s点写作技巧！' % wri)
                    if wor > 0:
                        player.working += 0.01 * wor
                        Notice.add('由于感悟：《药：绝望的解决手段》，{color=#7CFC00}提升{/color}了%s点工作能力！' % wor)
                    self.sub(player)

    class BookRiskEffect(Effect):
        id = 511
        name = '感悟：《失而复得》'
        kind = '学识'
        maxDuration = 2
        maxStacks = 1
        info = '效果期间内消耗的精神状态越多，效果结束时{color=#7CFC00}降低{/color}的严重程度越多，{color=#7CFC00}提升{/color}的工作能力和{color=#7CFC00}降低{/color}的严重程度越多。\n若消耗的精神状态低于150则只会获得2层焦虑，有效上限为500点。'
        info_p = '效果期间内消耗的精神状态越多，效果结束时{color=#7CFC00}降低{/color}的严重程度越多，{color=#7CFC00}提升{/color}的工作能力和{color=#7CFC00}降低{/color}的严重程度越多。\n若消耗的精神状态低于150则只会获得2层焦虑，有效上限为500点。'

        def __init__(self):
            Effect.__init__(self)
            self.cons=0

        def getPrincipalInfo(self):
            if persistent.PreciseDisplay:
                showinfo = self.info_p
            else:
                showinfo = self.info

            feed = '\n' if showinfo != '' else ''
            return feed + showinfo + '\n\n当前已消耗精神状态：'+str(self.cons)
        
        def timeUpAction(self, player):
            g = min(r2(self.cons * 0.04 * 0.01), 0.2)

            if self.cons>=150:
                player.working += g
                player.severity -= g
                Notice.add('由于感悟：《失而复得》，{color=#7CFC00}提升{/color}了%s点工作能力！' % (g*100))
                Notice.add('由于感悟：《失而复得》，{color=#7CFC00}降低{/color}了%s点严重程度！' % (g*100))
            else:
                MentProb.add(p, 2)
                Notice.add('由于感悟：《失而复得》，{color=#FF4500}获得{/color}了2层焦虑！')

    class BookSevUpEffect(Effect):
        id = 512
        name = '感悟：《热病》'
        kind = '学识'
        maxDuration = 4
        maxStacks = 1
        info = '暂时{color=#FF4500}提升{/color}严重程度。'
        info_p = '暂时{color=#FF4500}提升{/color}10%的严重程度。'

        def enableAction(self, player):
            player.severityRegarded += 0.1

        def disableAction(self, player):
            player.severityRegarded -= 0.1


    class BookUndeadEffect(Effect):
        id = 512
        name = '感悟：《国境以北星空以南》'
        kind = '学识'
        maxDuration = 2
        maxStacks = 1
        info = '暂时{color=#FF4500}提升{/color}严重程度，使精神状态不会低于0。'
        info_p = '暂时{color=#FF4500}提升{/color}10%的严重程度，使精神状态不会低于0。'

        def enableAction(self, player):
            player.severityRegarded += 0.1

        def disableAction(self, player):
            player.severityRegarded -= 0.1
        
    class BookRandConcEffect(Effect):
        id = 512
        name = '感悟：《寻羊历险记》'
        kind = '学识'
        maxDuration = 3
        maxStacks = 1
        info = '完成日程后{color=#7CFC00}获得{/color}随机专注度加成，仅对下一个日程有效。'
        info_p = '完成日程后{color=#7CFC00}获得{/color}随机0%~50%的专注度加成，仅对下一个日程有效。'

        def afterTaskAction(self, player, task):
            s = ra(player, 0, 20) # 10
            if rra(player, 50): #3.75
                s += ra(player, 0, 15)
            if rra(player, 25): #1.25
                s += ra(player, 0, 10)
            if rra(player, 10): #0.25
                s += ra(player, 0, 5)

            BookRandConcEffect_1.add(player, s)


    class BookRandConcEffect_1(Effect):
        id = 512
        name = '提升：《寻羊历险记》'
        kind = '学识'
        maxDuration = 1
        maxStacks = 50
        info = '进行日程将消耗所有本状态，使本次日程的专注度{color=#7CFC00}提升{/color}等同于层数的专注度。'
        info_p = '进行日程将消耗所有本状态，使本次日程的专注度{color=#7CFC00}提升{/color}等同于层数的专注度。'

        def addStackAction(self, player):
            player.basicConcentration += 1

        def subStackAction(self, player):
            player.basicConcentration -= 1

        def afterTaskAction(self, player, task):
            self.clear(player)

    class BookBanDepEffect(Effect):
        id = 513
        name = '学识：《常用药理学知识》'
        kind = '学识'
        maxDuration = 3
        maxStacks = 1
        info = '持续时间内使用药物{color=#7CFC00}提升{/color}10%恢复的精神状态，同时不会获得药物效果。获得新的药物依赖时，取而代之获得其对应药物的1点抗药性。'
        info_p = '持续时间内使用药物{color=#7CFC00}提升{/color}10%恢复的精神状态，同时不会获得药物效果。获得新的药物依赖时，取而代之获得其对应药物的1点抗药性。'

        def enableAction(self, player):
            player.drugRecovery += 0.1

        def disableAction(self, player):
            player.drugRecovery -= 0.1


    class GameDifficulty1(Effect):
        id = 600
        name = '病情好转'
        kind = '伤痕'
        maxDuration = -1
        maxStacks = 1
        info = '精神状态消耗大幅度{color=#7CFC00}降低{/color}。\n精神状态恢复大幅度{color=#7CFC00}提升{/color}。\n睡眠消耗的精神状态大幅度{color=#7CFC00}降低{/color}。\n\n{color=#7FFF00}游戏难度：简单{/color}\n\n{color=#ffff00}可以随时更改已制定好的日程。\n书籍可以在道具栏中直接使用。\n药店中解锁了新的药物。{/color}\n严重程度提升概率：低'
        info_p = '精神状态消耗{color=#7CFC00}降低{/color}60%。\n精神状态恢复{color=#7CFC00}提升{/color}60%。\n睡眠消耗的精神状态{color=#7CFC00}降低{/color}60%。\n\n{color=#7FFF00}游戏难度：简单{/color}\n\n{color=#ffff00}可以随时更改已制定好的日程。\n书籍可以在道具栏中直接使用。\n药店中解锁了新的药物。{/color}\n严重程度提升概率：30%'
        ad = '“你的病情正在逐渐好转，虽然你还是会偶尔头疼，但也许用不了一阵子你就可以脱离药物的治疗。”'

        def enableAction(self, player):
            GameDifficulty2.clearByType(player)
            GameDifficulty3.clearByType(player)
            GameDifficulty4.clearByType(player)
            GameDifficulty5.clearByType(player)
            player.basicConsumption -= 0.6
            player.basicRecovery += 0.6
            player.deteriorateConsumption -= 0.6

        def disableAction(self, player):
            player.basicConsumption += 0.6
            player.basicRecovery -= 0.6
            player.deteriorateConsumption += 0.6

        def getPrincipalInfo(self):
            if persistent.PreciseDisplay:
                showinfo = self.info_p
            else:
                showinfo = self.info

            feed = '\n' if showinfo != '' else ''
            return feed + showinfo + '\n已提升的严重程度倍率：+%s%s'%(p.aggra, '%')

        def afterSleepAction(self, player):
            if rra(player, 30) and player.cured < 0:
                player.severityRegarded += 0.01
                player.aggra += 1

    class GameDifficulty2(Effect):
        id = 601
        name = '病情稳定'
        kind = '伤痕'
        maxDuration = -1
        maxStacks = 1
        info = '精神状态消耗{color=#7CFC00}降低{/color}。\n精神状态恢复{color=#7CFC00}提升{/color}。\n睡眠消耗的精神状态{color=#7CFC00}降低{/color}。\n\n{color=#FFE4C4}游戏难度：较易{/color}\n\n严重程度提升概率：较低'
        info_p = '{color=#7CFC00}降低{/color}30%。\n精神状态恢复{color=#7CFC00}提升{/color}30%。\n睡眠消耗的精神状态{color=#7CFC00}降低{/color}30%。\n\n{color=#FFE4C4}游戏难度：较易{/color}\n\n严重程度提升概率：30%'
        ad = '“你的病情趋向于稳定，这段时间里你仍然要忍耐头疼的折磨，但过段时间，应该就可以脱离药物的治疗。”'

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
            return feed + showinfo + '\n已提升的严重程度倍率：+%s%s'%(p.aggra, '%')

        def afterSleepAction(self, player):
            if rra(player, 30) and player.cured < 0:
                player.severityRegarded += 0.01
                player.aggra += 1

    class GameDifficulty3(Effect):
        id = 602
        name = '病情较重'
        kind = '伤痕'
        maxDuration = -1
        maxStacks = 1
        info = '{color=#87CEEB}游戏难度：一般{/color}\n\n严重程度提升概率：一般'
        info_p = '{color=#87CEEB}游戏难度：一般{/color}\n\n严重程度提升概率：50%'
        ad = '“你的病情相对严重，不要忘记按时吃药，多锻炼，不过相信你已经习惯这样的生活了吧。”'

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
            return feed + showinfo + '\n已提升的严重程度倍率：+%s%s'%(p.aggra, '%')
        
        def afterSleepAction(self, player):
            if rra(player, 50) and player.cured < 0:
                player.severityRegarded += 0.01
                player.aggra += 1

    
    class GameDifficulty4(Effect):
        id = 603
        name = '病情严重'
        kind = '伤痕'
        maxDuration = -1
        maxStacks = 1
        info = '精神状态消耗小幅度{color=#FF4500}提升{/color}。\n睡眠消耗的精神状态小幅度{color=#FF4500}提升{/color}。\n\n{color=#DA70D6}游戏难度：较难{/color}\n\n严重程度提升概率：较高'
        info_p = '精神状态消耗{color=#FF4500}提升{/color}20%。\n睡眠消耗的精神状态{color=#FF4500}提升{/color}20%。\n\n{color=#DA70D6}游戏难度：较难{/color}\n\n严重程度提升概率：65%'
        ad = '“你的病情比较严重，你必须更加谨慎地对待生存这件事，不要妄想有一天你能不用吃药了。”'

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
            return feed + showinfo + '\n已提升的严重程度倍率：+%s%s'%(p.aggra, '%')

        def afterSleepAction(self, player):
            if rra(player, 65) and player.cured < 0:
                player.severityRegarded += 0.01
                player.aggra += 1

    class GameDifficulty5(Effect):
        id = 604
        name = '病情危急'
        kind = '伤痕'
        maxDuration = -1
        maxStacks = 1
        info = '精神状态消耗{color=#FF4500}提升{/color}。\n精神状态恢复{color=#FF4500}降低{/color}。\n睡眠消耗的精神状态{color=#FF4500}提升{/color}。\n{color=#FF0000}游戏难度：硬核{/color}\n\n严重程度提升概率：高'
        info_p = '精神状态消耗{color=#FF4500}提升{/color}40%。\n精神状态恢复{color=#FF4500}降低{/color}40%。\n睡眠消耗的精神状态{color=#FF4500}提升{/color}40%。\n{color=#FF0000}游戏难度：硬核{/color}\n\n严重程度提升概率：80%'
        ad = '“你是怎么在ICU外还能活到现在的？”'

        def enableAction(self, player):
            GameDifficulty1.clearByType(player)
            GameDifficulty2.clearByType(player)
            GameDifficulty3.clearByType(player)
            GameDifficulty4.clearByType(player)
            player.basicConsumption += 0.4
            player.basicRecovery -= 0.4
            player.deteriorateConsumption += 0.4

        def disableAction(self, player):
            player.basicConsumption -= 0.4
            player.basicRecovery += 0.4
            player.deteriorateConsumption -= 0.4

        def getPrincipalInfo(self):
            if persistent.PreciseDisplay:
                showinfo = self.info_p
            else:
                showinfo = self.info

            feed = '\n' if showinfo != '' else ''
            return feed + showinfo + '\n已提升的严重程度倍率：+%s%s'%(p.aggra, '%')

        def afterSleepAction(self, player):
            if rra(player, 80) and player.cured < 0:
                player.severityRegarded += 0.01
                player.aggra += 1


    class GameModule1(Effect):
        id = 650
        name = '挑战模式'
        kind = '伤痕'
        maxDuration = -1
        maxStacks = 1
        info = '游戏进入了挑战模式，在该模组下，游戏发生以下改变：\n偏头痛：每完成一个日程后随机{color=#FF4500}消耗{/color}精神状态。\n资源供给：{color=#7CFC00}获得{/color}1000元，但药物的价格自然增长倍率{color=#FF4500}提升{/color}。\n自卑感：过夜后每个能力属性都有概率{color=#FF4500}失去{/color}少量，有概率{color=#FF4500}提升{/color}严重程度倍率。\n理财不善：过夜后百分比{color=#FF4500}失去{/color}少量金钱。\n效率低下：每周需要完成的工作目标随周数{color=#FF4500}提升{/color}。\n药物过敏：药物恢复效果小幅度{color=#7CFC00}提升{/color}，过夜后有概率{color=#FF4500}提升{/color}随机一种已经使用过的药物的抗药性。'
        info_p = '游戏进入了挑战模式，在该模组下，游戏发生以下改变：\n偏头痛：每完成一个日程后{color=#FF4500}消耗{/color}1%~20%的当前精神状态。\n资源供给：{color=#7CFC00}获得{/color}1000元，但药物的价格自然增长倍率{color=#FF4500}提升{/color}至1.5倍。\n自卑感：过夜后工作能力，身体素质，写作技巧各有50%的概率{color=#FF4500}失去{/color}1%，严重程度有25%的概率永久{color=#FF4500}提升{/color}1%。\n理财不善：所持金钱大于500元时，过夜后{color=#FF4500}失去{/color}10%的当前金钱。\n效率低下：每周需要完成的工作目标{color=#FF4500}提升{/color}3%*周数。\n药物过敏：药物的恢复效果{color=#7CFC00}提升{/color}15%，过夜后有33%的概率{color=#FF4500}提升{/color}随机一种已经使用过的药物的抗药性。'
        ad = '也许把大脑切开能将痛苦缓解。'

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

        def getPrincipalInfo(self):
            if persistent.PreciseDisplay:
                showinfo = self.info_p
            else:
                showinfo = self.info

            feed = '\n' if showinfo != '' else ''
            extra = '\n\n【偏头痛】总消耗的精神状态：%s\n【自卑感】提升的严重程度：+%s%s\n失去的工作能力：%s 失去的身体素质：%s 失去的写作技巧：%s\n【理财不善】花掉的金钱：%s\n【药物过敏】%s提升的抗药性：%s %s提升的抗药性：%s %s提升的抗药性：%s'%(self.ment, self.se, '%', self.wo, self.ph, self.wr, self.mo, MedicineA.name, self.ra, MedicineB.name, self.rb, MedicineC.name, self.rc)
            return feed + showinfo + extra


        def enableAction(self, player):
            GameDifficulty1.clearByType(player)
            GameDifficulty2.clearByType(player)
            GameDifficulty3.clearByType(player)
            GameDifficulty4.clearByType(player)
            GameDifficulty5.clearByType(player)

            GameDifficulty5.add(player)

            player.drugRecovery += 0.15

            player.priceIncrease *= 1.5
            player.money += 1000

            player.physical += 0.2
            player.writing += 0.2
            player.working += 0.2

            player.goal = r2(player.goal * (1 + (0.03 * player.week)))



        def afterTaskAction(self, player, task):
            per = ra(player, 1, 8)
            if rra(player, 50):
                per += ra(player, 0, 8)
            if rra(player, 50):
                per += ra(player, 0, 4)
            if player.mental > 150:
                per = ra(player, 15, 20)
            t = r2(player.mental * per * 0.01)
            self.ment += t
            player.mental -= t
            Notice.add('由于偏头痛，消耗了%s点精神状态！' % t)

        def afterSleepAction(self, player):
            if rra(player, 50):
                player.physical -= r2(0.01 * player.physical)
                self.ph += 1
                Notice.add('由于自卑，降低了1%的身体素质！')
            if rra(player, 50):
                player.writing -= r2(0.01 * player.writing)
                self.wr += 1
                Notice.add('由于自卑，降低了1%的写作技巧！')
            if rra(player, 50):
                player.working -= r2(0.01 * player.working)
                self.wo += 1
                Notice.add('由于自卑，降低了1%的工作能力！')
            if rra(player, 25):
                self.se += 1
                player.severityRegarded += 0.01
                Notice.add('由于自卑，提升了1%的严重程度！')
            
            if player.money >= 500:
                t = r2(player.money*0.1*f())
                self.mo += t
                player.money -= t
                Notice.add('由于理财不善，不受控制地花掉了%s元！' % t)
            
            if rra(player, 33) and player.medinfo:
                med = rca(player, player.medinfo.keys())
                if med == MedicineA:
                    self.ra += 1
                elif med == MedicineB:
                    self.rb += 1
                elif med == MedicineC:
                    self.rc += 1
                player.medinfo[med].res += 1
                Notice.add('由于药物过敏，%s的药物抗性上升了1%s！' % (med.name, '%'))



    class GameModule2(Effect):
        id = 650
        name = '无尽之旅'
        kind = '伤痕'
        maxDuration = -1
        maxStacks = 1
        info = '{color=#97e41b}你正行走于无尽之旅的道路之上。{/color}\n每次阅读无尽之旅都会{color=#7CFC00}获得{/color}3点{color=#97e41b}足迹{/color}，而使用阅读后获得的手稿也会{color=#7CFC00}获得{/color}2点{color=#97e41b}足迹{/color}。\n每层{color=#97e41b}足迹{/color}都能在起床时提供2%的概率来{color=#7CFC00}减少{/color}1天无尽之旅书籍的冷却时间，2%起床时{color=#7CFC00}获得{/color}灵感的概率，以及0.5%{color=#7CFC00}获得{/color}存在感的概率。'
        info_p = '{color=#97e41b}你正行走于无尽之旅的道路之上。{/color}\n每次阅读无尽之旅都会{color=#7CFC00}获得{/color}3点{color=#97e41b}足迹{/color}，而使用阅读后获得的手稿也会{color=#7CFC00}获得{/color}2点{color=#97e41b}足迹{/color}。\n每层{color=#97e41b}足迹{/color}都能在起床时提供2%的概率来{color=#7CFC00}减少{/color}1天无尽之旅书籍的冷却时间，2%起床时{color=#7CFC00}获得{/color}灵感的概率，以及0.5%{color=#7CFC00}获得{/color}存在感的概率。'
        ad = '当旅人来到无尽家族，看着无尽们的“忙碌”，让旅人得到灵感——如果不同的我拿到这种能力会发生什么呢？'

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
            extra = '\n\n足迹：%s\n已减少的书本冷却时间：%s\n已获得的灵感层数：%s\n已获得的存在感层数：%s' %(self.pace, self.cddown, self.insp, self.getrevive)
            return feed + showinfo + extra
        
        def afterSleepAction(self, player):
            if BookGameModule2 in player.itemcd:
                if rra(player, self.pace*2):
                    player.itemcd[BookGameModule2] -= 1
                    self.cddown += 1

                    for k in list(player.itemcd.keys()):
                        if player.itemcd[k] == 0:
                            del player.itemcd[k]
                    Notice.add('由于无尽之旅，无尽之旅的冷却时间降低了！')
                            
            if rra(player, self.pace*2):
                Inspiration.add(player)
                Notice.add('由于无尽之旅，获得了1层灵感！')
                self.insp += 1
            if self.pace*2 > 100:
                if rra(player, self.pace*2-100):
                    Inspiration.add(player)
                    self.insp += 1
                    Notice.add('由于无尽之旅，获得了1层灵感！')

            if rra(player, self.pace*0.5) and not Novice.has(player):
                Novice.add(player)
                Novice.get(player).duration = 4
                Notice.add('由于无尽之旅，获得了存在感！')
                self.getrevive += 1
        
        def readbook(self):
            self.pace += 3
        
        def readmanu(self):
            self.pace += 2

    class Despair(Effect):
        id = 610
        name = '绝望'
        kind = '伤痕'
        maxDuration = -1
        maxStacks = 99
        info = '我还能活下去吗？'
        info_p = '我还能活下去吗？'

        def addStackAction(self, player):
            player.basicConsumption += 0.015

        def subStackAction(self, player):
            player.basicConsumption -= 0.015

        def afterTaskAction(self, player, task):
            t = r2(3 * self.stacks  * f() * player.basicConsumption)
            self.add(player, ra(player, 1, self.stacks))
            player.mental -= t
            Notice.add('%s由于绝望，消耗了%s点精神状态！' % (player.name, t))

        def afterDrug(self, player):
            self.sub(player, self.stacks-1)


    class LifeIsColorless(Effect):
        id = 611
        name = '生命失去了色彩'
        kind = '伤痕'
        maxDuration = -1
        maxStacks = 99
        info = '活着。'
        info_p = '活着。'

        def afterSleepAction(self, player):
            self.stacks += 1



    class Debilitated(Effect):
        id = 620
        name = '体弱'
        kind = '伤痕'
        maxDuration = -1
        maxStacks = 99
        info = '按层数{color=#FF4500}降低{/color}身体素质。\n' \
            '药物效果按层数{color=#FF4500}降低{/color}。\n' \
            '睡眠{color=#FF4500}消耗{/color}的精神状态按层数{color=#FF4500}提升{/color}。'
        info_p = '每层都会{color=#FF4500}降低{/color}10%的身体素质。\n' \
            '每层都会{color=#FF4500}降低{/color}10%的药物效果。\n' \
            '每层都会{color=#FF4500}提升{/color}10%睡眠消耗的精神状态。'
        ad = '“有些伤口永远不会完全愈合。”'

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
        name = '精神创伤'
        kind = '伤痕'
        maxDuration = -1
        maxStacks = 99
        info = '按层数{color=#FF4500}降低{/color}写作技巧。\n' \
            '过夜将会{color=#FF4500}失去{/color}相当于该伤痕层数的灵感。\n' \
            '完成委托时，委托的价值按层数{color=#FF4500}降低{/color}。'
        info_p = '每层都会{color=#FF4500}降低{/color}10%的写作技巧。\n' \
            '每次过夜都会{color=#FF4500}失去{/color}相当于该伤痕层数的灵感。\n' \
            '完成委托时，委托的价值每层都会{color=#FF4500}降低{/color}10%。'
        ad = '“我已经悖离了我自己的心。”'

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
        name = '衰退'
        kind = '伤痕'
        maxDuration = -1
        maxStacks = 99
        info = '严重程度{color=#FF4500}提升{/color}，过夜有概率失去灵感和体魄。\n'
        info_p = '每层都会{color=#FF4500}提升{/color}10%的严重程度，过夜有33%的概率失去等于衰退层数的灵感和体魄。\n'
        ad = '“对你来说可能有毒，但你还是会喝下去。”'

        def addStackAction(self, player):
            player.severityRegarded += 0.1

        def subStackAction(self, player):
            player.severityRegarded -= 0.1

        def afterSleepAction(self, player):
            if Inspiration.has(player) and rra(player, 33):
                Inspiration.subByType(player, self.stacks)
            if Physique.has(player) and rra(player, 33):
                Physique.subByType(player, self.stacks)

