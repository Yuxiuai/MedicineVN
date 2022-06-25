init python:

    class WeatherSunny(Effect):
        id = 100
        name = '{color=#FFD700}晴天{/color}'
        kind = '天气'
        maxDuration = 0
        maxStacks = 1
        info = '外出运动会{color=#7CFC00}恢复{/color}更多精神状态，并额外{color=#7CFC00}提升{/color}身体素质。'
        info_p = '进行外出散步、慢跑、速跑时会{color=#7CFC00}恢复{/color}额外25%的精神状态，并额外{color=#7CFC00}提升{/color}2点身体素质。'
        ad = '适合室外运动的好天气。'

        def enableAction(self, player):
            player.outdoorSportRecovery += 0.25

        def disableAction(self, player):
            player.outdoorSportRecovery -= 0.25

        def afterTaskAction(self, player, task):
            if task.name in ('外出散步', '慢跑', '速跑'):
                Notify.add('由于晴天，提升了2点身体素质！')
                player.physical += 0.01


    class WeatherRainy(Effect):
        id = 101
        name = '{color=#87CEFA}雨天{/color}'
        kind = '天气'
        maxDuration = 0
        maxStacks = 1
        info = '休息，写作类日程{color=#7CFC00}恢复{/color}更多的精神状态，且会额外{color=#7CFC00}降低{/color}严重程度。\n\n{color=FF0000}无法进行室外跑步。{/color}'
        info_p = '进行休息，写作类日程时会{color=#7CFC00}恢复{/color}额外25%的精神状态，且会额外{color=#7CFC00}降低{/color}2点严重程度。\n\n{color=FF0000}无法进行室外跑步。{/color}'
        ad = '适合宅家的好天气。'

        def enableAction(self, player):
            player.sleepRecovery += 0.25
            player.writeRecovery += 0.25
            player.canOutdoorSport -= 1

        def disableAction(self, player):
            player.sleepRecovery -= 0.25
            player.writeRecovery -= 0.25
            player.canOutdoorSport += 1

        def afterTaskAction(self, player, task):
            if task.kind in ('休息类', '写作类'):
                Notify.add('由于雨天，降低了2点严重程度！')
                player.severity -= 0.02


    class WeatherCloudy(Effect):
        id = 102
        name = '{color=#B0C4DE}多云{/color}'
        kind = '天气'
        maxDuration = 0
        maxStacks = 1
        info = '工作类日程的专注度{color=#FF4500}降低{/color}，进行休息时{color=#7CFC00}提升{/color}生病和受伤的恢复率。'
        info_p = '工作类日程的专注度{color=#FF4500}降低{/color}15%，进行休息时{color=#7CFC00}提升{/color}20%生病和受伤的恢复率。'
        ad = '阴沉的天气让你犯困，你总是忍不住打哈欠。'

        def enableAction(self, player):
            player.workConcentration -= 15

        def disableAction(self, player):
            player.workConcentration += 15


    class WeatherHot(Effect):
        id = 103
        name = '{color=#FF4500}酷热{/color}'
        kind = '天气'
        maxDuration = 0
        maxStacks = 1
        info = '身体素质暂时小幅度{color=#FF4500}降低{/color}，运动类日程恢复的精神状态和专注度{color=#FF4500}降低{/color}，且进行后将额外{color=#FF4500}提升{/color}严重程度。'
        info_p = '身体素质暂时{color=#FF4500}降低{/color}5%，运动类日程恢复的精神状态和专注度{color=#FF4500}降低{/color}20%，且进行后将额外{color=#FF4500}提升{/color}2点严重程度。'
        ad = '衣服都被汗打湿了啊，也太热了吧！'

        def enableAction(self, player):
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
        maxDuration = 0
        maxStacks = 1
        info = '完成日程后百分比{color=#7CFC00}恢复{/color}少量精神状态。'
        info_p = '完成日程后{color=#7CFC00}恢复{/color}当前精神状态的5% ~ 15%，最高恢复20点。'
        ad = '人都要被吹跑了！不过我喜欢这种感觉！'

        def afterTaskAction(self, player, task):
            rec = r2(player.mental * ra(player, 1050, 1150) * 0.0001)
            if rec > 20:
                rec = 20
            player.mental += rec


    class WeatherWet(Effect):
        id = 105
        name = '{color=#00FFFF}阴冷{/color}'
        kind = '天气'
        maxDuration = 0
        maxStacks = 1
        info = '完成日程后若没有良好的运动则有概率生病，若已经生病则不会再生病。'
        info_p = '完成日程后若没有良好的运动则有40%的概率生病，若已经生病则不会再生病。'
        ad = '……我真应该把我那件大衣带到公司……'

        def afterTaskAction(self, player, task):
            if not PhysRezB.has(player) and not PhysPun.has(player):
                if rra(player, 40):
                    PhysPun.add(player)


    class WeatherThunder(Effect):
        id = 106
        name = '{color=#FFFF00}打雷{/color}'
        kind = '天气'
        maxDuration = 0
        maxStacks = 1
        info = '睡眠消耗的精神状态{color=#FF4500}提升{/color}，同时第二日获得更多的睡意。'
        info_p = '睡眠消耗的精神状态{color=#FF4500}提升{/color}20%，同时第二日获得1 ~ 3层睡意。'
        ad = '我并非是怕打雷的小孩子，但即便是轻微的声响都让我难以入眠……'

        def enableAction(self, player):
            player.afterSleepEffects.append(ConcDec)
            if rra(player, 50):
                player.afterSleepEffects.append(ConcDec)
            if rra(player, 50):
                player.afterSleepEffects.append(ConcDec)
            player.deteriorateConsumption += 0.2

        def disableAction(self, player):
            player.deteriorateConsumption -= 0.2


    class WeatherNone(Effect):
        id = 107
        name = '？？？'
        kind = '天气'
        maxDuration = 0
        maxStacks = 1
        info = '？？？？？？？？？？？'
        info_p = '？？？？？？？？？？？'
        ad = '在废墟之下，你不知道外界的天气。'


    class Novice(Effect):
        id = 200
        name = '存在感'
        kind = '状态'
        maxDuration = 16
        maxStacks = 1
        info = '即将死亡时，{color=#7CFC00}恢复{/color}精神状态至一定值。\n如果没有触发效果，则持续时间结束时降低严重程度。'
        info_p = '当起床时，没有任何可用药物且精神状态低于0，或仅有数量为1的可使用的任意药物，但预计使用效果与当前精神状态相加后仍然低于0时：{color=#7CFC00}恢复{/color}精神状态至60。\n如果没有触发效果，则持续时间结束时降低3点严重程度。'
        ad = '“我很想看到渐次泛白的黎明时分的天宇，想喝热气蒸腾的牛奶，想闻树木的清香，想翻晨报的版面。”'

        def timeUpAction(self, player):
            Notify.add('存在感持续时间结束，降低了3点严重程度！')
            player.severity -= 0.03

        def afterSleepAction(self, player):
            flag = False
            if player.meds() <= 1:
                l = list(filter(lambda x: type(x).kind == '实验药物' and not x.broken, player.items))
                if len(l)==1:
                    if player.mental + type(l[0]).expectedReco(player) <= -5:
                        flag = True
                else:
                    if player.mental <= 0:
                        flag = True
            
            if flag:
                showNotify(['移除了状态：存在感，将精神状态恢复至60.0'])
                player.mental = 60.0
                self.clear(player)


    class Erection(Effect):
        id = 201
        name = '勃起'
        kind = '状态'
        maxDuration = 0
        maxStacks = 1
        info = '你的欲望让你的生殖器官充血膨胀。'
        info_p = '你的欲望让你的生殖器官充血膨胀。'
        ad = '我感觉我的内裤开始变紧了……'

        def afterTaskAction(self, player, task):
            if rra(player, 50):
                self.clear(player)

        def end(self, player):
            Pleasure.add(player)
            self.clear(player)


    class Pleasure(Effect):
        id = 202
        name = '快感'
        kind = '状态'
        maxDuration = 0
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
        maxDuration = 0
        maxStacks = 5
        info = '精神状态消耗随层数{color=#FF4500}提升{/color}，精神状态恢复随层数{color=#7CFC00}提升{/color}。'
        info_p = '精神状态消耗每层都会{color=#FF4500}提升{/color}10%，精神状态恢复每层都会{color=#7CFC00}提升{/color}15%。'
        ad = '做点什么，是的，尽可能多地做，尽可能完美地做，至少在死前做更多的事情，做世界上大多数人都没做过的事，不然怎么能算活着呢。'

        def enableAction(self, player):
            if ConsDec.has(player):
                ConsDec.subByType(player)
                self.sub(player)

        def addStackAction(self, player):
            player.basicConsumption += 0.1
            player.basicRecovery += 0.15

        def subStackAction(self, player):
            player.basicConsumption -= 0.1
            player.basicRecovery -= 0.15


    class ConsDec(Effect):
        id = 211
        name = '放松'
        kind = '状态'
        maxDuration = 0
        maxStacks = 5
        info = '精神状态消耗随层数{color=#7CFC00}降低{/color}，精神状态恢复随层数{color=#FF4500}降低{/color}。'
        info_p = '精神状态消耗每层都会{color=#7CFC00}降低{/color}7.5%，精神状态恢复每层都会{color=#FF4500}降低{/color}15%。'
        ad = '不，也许我没必要做那么多？我为什么要那样折磨自己？死亡之后一切都对我没有意义，及时行乐……我应该辞了这份工作。'

        def enableAction(self, player):
            if ConsInc.has(player):
                ConsInc.subByType(player)
                self.sub(player)

        def addStackAction(self, player):
            player.basicConsumption -= 0.075
            player.basicRecovery -= 0.15

        def subStackAction(self, player):
            player.basicConsumption += 0.075
            player.basicRecovery += 0.15


    class ConcDec(Effect):
        id = 212
        name = '睡意'
        kind = '状态'
        maxDuration = 0
        maxStacks = 5
        info = '专注度随层数{color=#FF4500}降低{/color}，睡眠消耗的精神状态随层数{color=#7CFC00}降低{/color}。'
        info_p = '专注度每层都会{color=#FF4500}降低{/color}10%，睡眠消耗的精神状态每层都会{color=#7CFC00}降低{/color}7.5%。'
        ad = '是的，让我睡觉，求你了，能让我躺在柔软的床上美美地睡一觉的话我什么都会做的。'

        def enableAction(self, player):
            if ConcInc.has(player):
                ConcInc.subByType(player)
                self.sub(player)

        def addStackAction(self, player):
            player.basicConcentration -= 10
            player.deteriorateConsumption -= 0.075

        def subStackAction(self, player):
            player.basicConcentration += 10
            player.deteriorateConsumption += 0.075


    class ConcInc(Effect):
        id = 213
        name = '兴奋'
        kind = '状态'
        maxDuration = 0
        maxStacks = 5
        info = '专注度随层数{color=#7CFC00}提升{/color}，睡眠消耗的精神状态随层数{color=#FF4500}提升{/color}。'
        info_p = '专注度每层都会{color=#7CFC00}提升{/color}7.5%，睡眠消耗的精神状态每层都会{color=#FF4500}提升{/color}10%。'
        ad = '我痛恨我需要睡眠，若是能有按钮迅速跳过夜晚瞬间恢复精神状态来到第二天，或是单纯将我的肉体与电线链接便可恢复能量就好了。'

        def enableAction(self, player):
            if ConcDec.has(player):
                ConcDec.subByType(player)
                self.sub(player)

        def addStackAction(self, player):
            player.basicConcentration += 7.5
            player.deteriorateConsumption += 0.1

        def subStackAction(self, player):
            player.basicConcentration -= 7.5
            player.deteriorateConsumption -= 0.1

    class Restlessness(Effect):
        id = 214
        name = '紧迫'
        kind = '状态'
        maxDuration = 0
        maxStacks = 1
        info = '{color=#7CFC00}提升{/color}工作速度和工作的专注度。'
        info_p = '工作速度{color=#7CFC00}提升{/color}10%，对工作的专注度{color=#7CFC00}提升{/color}20%。'
        ad = '我难以呼吸，总觉有何未知的存在正追赶着我，挤压着我将我向前推进。'

        def enableAction(self, player):
            player.workSpeed += 0.1
            player.workConcentration += 20

        def disableAction(self, player):
            player.workSpeed -= 0.1
            player.workConcentration -= 20


    class Contentment(Effect):
        id = 215
        name = '安逸'
        kind = '状态'
        maxDuration = 0
        maxStacks = 99
        info = '休息恢复的精神状态{color=#FF4500}提升{/color}，且必定移除全部的过劳。'
        info_p = '休息恢复的精神状态{color=#FF4500}提升{/color}20%，且必定移除全部的过劳。'
        ad = '我已经得到了部分存在而得的愉悦，较低的期望让我不再渴求之外的事物，无需追赶自己。'

        def enableAction(self, player):
            player.sleepRecovery += 0.2

        def disableAction(self, player):
            player.sleepRecovery -= 0.2

        def afterTaskAction(self, player, task):
            if task.name == '休息':
                if PhysProb.has(player):
                    PhysProb.clearByType(player)


    class Dread(Effect):
        id = 216
        name = '恐惧'
        kind = '状态'
        maxDuration = 0
        maxStacks = 99
        info = '{color=#FF4500}提升{/color}严重程度和精神状态消耗。\n状态结束后获得存在感。'
        info_p = '{color=#FF4500}提升{/color}5点严重程度，{color=#FF4500}提升{/color}20%精神状态消耗。\n状态结束后获得持续时间为2天的存在感。'
        ad = '当破除这份来源于存在本身的的恐惧后，迎来的则是存活的希望。'

        def enableAction(self, player):
            player.severity += 0.05
            player.basicConsumption += 0.2

        def disableAction(self, player):
            player.basicConsumption -= 0.2

        def timeUpAction(self, player):
            if not Novice.has(player):
                Novice.add(player)
                Novice.get(player).duration = 2
    

    class Desire(Effect):
        id = 217
        name = '渴求'
        kind = '状态'
        maxDuration = 0
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
        maxDuration = 0
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
        maxDuration = 0
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
        maxDuration = 6
        maxStacks = 2
        info = '获得该状态时{color=#FF4500}降低{/color}身体素质和工作能力。\n' \
            '日程结算专注度小幅度{color=#FF4500}降低{/color}，精神状态消耗小幅度{color=#FF4500}提升{/color}，精神状态恢复小幅度{color=#FF4500}降低{/color}；休息恢复的精神状态小幅度{color=#7CFC00}提升{/color}。\n\n' \
            '休息时有小概率治愈，每个“良好的运动”和“良好的睡眠”都能较高{color=#7CFC00}提升{/color}休息治愈的概率。\n' \
            '以此种方式恢复时，减轻大量严重程度并获得大量身体素质。\n' \
            '持续时间结束或层数超过1层时{color=#FF4500}转化{/color}为伤痕：体弱。'
        info_p = '获得该状态时{color=#FF4500}降低{/color}2点身体素质和2点工作能力。\n' \
            '日程结算专注度{color=#FF4500}降低{/color}10%，精神状态消耗{color=#FF4500}提升{/color}10%，精神状态恢复{color=#FF4500}降低{/color}10%；休息恢复的精神状态{color=#7CFC00}提升{/color}10%。\n\n' \
            '休息时有10%的概率治愈，每个“良好的运动”和“良好的睡眠”都能{color=#7CFC00}提升{/color}20%的治愈概率，每层感冒药都能{color=#7CFC00}提升{/color}10%的治愈概率。\n' \
            '以此种方式恢复时，减轻5点严重程度并获得5点身体素质。\n' \
            '持续时间结束或层数超过1层时{color=#FF4500}转化{/color}为伤痕：体弱。'
        ad = '病痛折磨着我，与脑中毫无频率的头疼一同。'

        @classmethod
        def add(cls, player, times=1):
            if times == 0:
                return
            for i in range(times):
                cls.defaultAddEffect(player)
                effect = cls.get(player)
                if effect.stacks == 2:
                    Notify.add('生病层数为2，{color=#FF4500}转化{/color}为伤痕:体弱！')
                    Debilitated.add(player)
                    effect.clearByType(player)

        def timeUpAction(self, player):
            Notify.add('生病持续时间结束！{color=#FF4500}转化{/color}为伤痕:体弱！')
            Debilitated.add(player)

        def enableAction(self, player):
            Notify.add('由于生病，{color=#FF4500}降低{/color}2点工作能力。')
            Notify.add('由于生病，{color=#FF4500}降低{/color}2点身体素质。')
            player.working -= 0.02
            player.physical -= 0.02
            player.basicConcentration -= 10
            player.basicConsumption += 0.1
            player.basicRecovery -= 0.1
            player.sleepRecovery += 0.3

        def disableAction(self, player):
            player.basicConcentration += 10
            player.basicConsumption -= 0.1
            player.basicRecovery += 0.1
            player.sleepRecovery -= 0.3

        def cureBySleep(self, player):
            curePercent = 10
            if WeatherCloudy.has(player):
                curePercent += 20
            if DrugColdrexEffect.has(player):
                curePercent += 10 * DrugColdrexEffect.get(player).stacks
            if BookPhysPunEffect.has(player):
                curePercent += 20
            if PhysRezA.has(player):
                curePercent += PhysRezA.get(player).stacks * 20
            if PhysRezB.has(player):
                curePercent += PhysRezB.get(player).stacks * 20
            if rra(player, curePercent):  # 判定成功时，消耗所有的rezA和rezB
                Notify.add('成功治愈！')
                PhysRezA.clearByType(player)
                PhysRezB.clearByType(player)
                DrugColdrexEffect.clearByType(player)
                Notify.add('降低了5点严重程度！')
                Notify.add('提升了5点身体素质！')
                if BookPhysPunEffect.has(player):
                    s = r2(player.severity * 0.1)
                    player.severity -= s
                    Notify.add('由于学习成果：《呼吸训练》，额外降低了%s点严重程度！' % s)
                player.severity -= 0.05
                player.physical += 0.05

                self.clear(player)



    class MentPun(Effect):
        id = 221
        name = '偏执'
        kind = '状态'
        maxDuration = 6
        maxStacks = 2
        info = '获得该状态时{color=#FF4500}降低{/color}写作技巧和工作能力。\n' \
            '精神状态消耗{color=#FF4500}提升{/color}，工作类日程的专注度大幅度{color=#7CFC00}提升{/color}，工作类日程消耗的精神状态大幅度{color=#FF4500}降低{/color}，运动类日程的专注度大幅度{color=#FF4500}降低{/color}。\n\n' \
            '无法完成委托，阅读小说。\n' \
            '持续时间结束时或层数超过1层{color=#FF4500}转化{/color}为伤痕：精神创伤。'
        info_p = '获得该状态时{color=#FF4500}降低{/color}2点写作技巧和2点工作能力。\n' \
            '精神状态消耗{color=#FF4500}提升{/color}25%，工作类日程的专注度{color=#7CFC00}提升{/color}50%，工作类日程消耗的精神状态{color=#FF4500}降低{/color}45%，运动类日程的专注度{color=#FF4500}降低{/color}50%。\n\n' \
            '无法完成委托，阅读小说。\n' \
            '持续时间结束时或层数超过1层{color=#FF4500}转化{/color}为伤痕：精神创伤。'
        ad = '是的，工作，加倍努力工作，其他的一切都不重要。'

        @classmethod
        def add(cls, player, times=1):
            if times == 0:
                return
            for i in range(times):
                cls.defaultAddEffect(player)
                effect = cls.get(player)
                if effect.stacks == 2:
                    Notify.add('偏执层数为2，{color=#FF4500}转化{/color}为伤痕:精神创伤！')
                    Decadent.add(player)
                    effect.clearByType(player)

        def timeUpAction(self, player):
            Notify.add('偏执持续时间结束！{color=#FF4500}转化{/color}为伤痕:精神创伤！')
            Decadent.add(player)

        def enableAction(self, player):
            Notify.add('由于偏执，{color=#FF4500}降低{/color}2点写作技巧。')
            Notify.add('由于偏执，{color=#FF4500}降低{/color}2点工作能力。')
            player.working -= 0.02
            player.writing -= 0.02
            player.canWrite -= 1
            player.canRead -= 1
            player.sportConcentration -= 50
            player.basicConsumption += 0.25
            player.workConcentration += 50
            player.workConsumption -= 0.45

        def disableAction(self, player):
            player.canWrite += 1
            player.canRead += 1
            player.sportConcentration += 50
            player.basicConsumption -= 0.25
            player.workConcentration -= 50
            player.workConsumption += 0.45


    class Injured(Effect):
        id = 222
        name = '受伤'
        kind = '状态'
        maxDuration = 6
        maxStacks = 2
        info = '日程结算专注度小幅度{color=#FF4500}降低{/color}，精神状态消耗{color=#FF4500}提升{/color}。\n\n' \
            '无法进行运动类日程。\n' \
            '休息时有大概率治愈，每个“良好的运动”和“良好的睡眠”都能较高{color=#7CFC00}提升{/color}休息治愈的概率。\n' \
            '以此种方式恢复时，获得身体素质。\n' \
            '持续时间结束时或层数超过1层{color=#FF4500}转化{/color}为伤痕：体弱。'
        info_p = '日程结算专注度{color=#FF4500}降低{/color}15%，精神状态消耗{color=#FF4500}提升{/color}25%。\n\n' \
            '无法进行运动类日程。\n' \
            '休息时有30%的概率治愈，每个“良好的运动”和“良好的睡眠”都能{color=#7CFC00}提升{/color}25%的治愈概率。\n' \
            '以此种方式恢复时，获得2点身体素质。\n' \
            '持续时间结束时或层数超过1层{color=#FF4500}转化{/color}为伤痕：体弱。'
        ad = '我已为力量做出了牺牲。'

        @classmethod
        def add(cls, player, times=1):
            if times == 0:
                return
            for i in range(times):
                if Physique.has(player):
                    s = Physique.get(player).stacks
                    if s>=2:
                        Notify.add('移除2层体魄以抵挡了受伤效果！')
                        Physique.subByType(player, 2)
                        return
                cls.defaultAddEffect(player)
                effect = cls.get(player)
                if effect.stacks == 2:
                    Notify.add('受伤层数为2，{color=#FF4500}转化{/color}为伤痕:体弱！')
                    Debilitated.add(player)
                    effect.clearByType(player)

        def timeUpAction(self, player):
            Notify.add('受伤持续时间结束！{color=#FF4500}转化{/color}为伤痕:体弱！')
            Debilitated.add(player)

        def enableAction(self, player):
            player.basicConcentration -= 15
            player.basicConsumption += 0.25
            player.canSport -= 1

        def disableAction(self, player):
            player.basicConcentration += 15
            player.basicConsumption -= 0.25
            player.canSport += 1

        def cureBySleep(self, player):
            curePercent = 30
            if WeatherCloudy.has(player):
                curePercent += 20
            if BookPhysPunEffect.has(player):
                curePercent += 20
            if PhysRezA.has(player):
                curePercent += PhysRezA.get(player).stacks * 25
            if PhysRezB.has(player):
                curePercent += PhysRezB.get(player).stacks * 25
            if rra(player, curePercent):  # 判定成功时，消耗所有的rezA和rezB
                Notify.add('成功治愈！')
                PhysRezA.clearByType(player)
                PhysRezB.clearByType(player)
                Notify.add('提升了5点身体素质！')
                Notify.add('降低了5点严重程度！')
                if BookPhysPunEffect.has(player):
                    s = r2(player.severity * 0.1)
                    player.severity -= s
                    Notify.add('由于学习成果：《呼吸训练》，额外降低了%s点严重程度！' % s)
                player.severity -= 0.05
                player.physical += 0.05
                self.clear(player)


    class PhysProb(Effect):
        id = 223
        name = '过劳'
        kind = '状态'
        maxDuration = 2
        maxStacks = 99
        info = '进行工作类日程时有一定概率获得。\n' \
            '获得该状态时有小概率{color=#FF4500}降低{/color}身体素质和工作能力。\n入睡前大于3层以上时将在第二日{color=#FF4500}转化{/color}为状态：生病。'
        info_p = '进行工作类日程时有一定概率获得。\n' \
            '获得该状态时各有20%的概率{color=#FF4500}降低{/color}2点身体素质和2点工作能力。\n入睡前大于3层以上时将在第二日{color=#FF4500}转化{/color}为状态：生病。'
        ad = '痛苦来自于无法衡量工作和身体健康。'

        def enableAction(self, player):
            if rra(player, 20):
                Notify.add('由于过劳，{color=#FF4500}降低{/color}2点身体素质。')
                player.physical -= 0.02
            if rra(player, 20):
                Notify.add('由于过劳，{color=#FF4500}降低{/color}2点工作能力。')
                player.working -= 0.02

        @classmethod
        def add(cls, player, times=1):
            if times == 0:
                return
            for i in range(times):
                if PhysRezA.has(player):
                    Notify.add('添加%s：%s！{color=#FF4500}抵消{/color}1层状态:良好的睡眠！' % (cls.kind, cls.name))
                    PhysRezA.subByType(player)
                elif PhysRezB.has(player):
                    Notify.add('添加%s：%s！{color=#FF4500}抵消{/color}1层状态:良好的运动！' % (cls.kind, cls.name))
                    PhysRezB.subByType(player)
                else:
                    cls.defaultAddEffect(player)

        def afterSleepAction(self, player):
            if self.stacks >= 4 and not BookConcEffect.has(player):
                Notify.add('过劳层数大于3，{color=#FF4500}转化{/color}为状态：生病！')
                PhysPun.add(player)
                self.clear(player)


    class MentProb(Effect):
        id = 224
        name = '焦虑'
        kind = '状态'
        maxDuration = 2
        maxStacks = 99
        info = '进行工作类日程时有一定概率获得。\n' \
            '获得该状态时有小概率{color=#FF4500}降低{/color}写作技巧和工作能力。\n入睡前大于3层以上时将在第二日{color=#FF4500}转化{/color}为状态：偏执。'
        info_p = '进行工作类日程时有一定概率获得。\n' \
            '获得该状态时各有20%的概率{color=#FF4500}降低{/color}2点写作技巧和2点工作能力。\n入睡前大于3层以上时将在第二日{color=#FF4500}转化{/color}为状态：偏执。'
        ad = '我难以呼吸，总觉有何未知的存在正追赶着我，挤压着我将我向前推进。'

        def enableAction(self, player):
            if rra(player, 20):
                Notify.add('由于焦虑，{color=#FF4500}降低{/color}2点写作技巧。')
                player.writing -= 0.01
            if rra(player, 20):
                Notify.add('由于焦虑，{color=#FF4500}降低{/color}2点工作能力。')
                player.working -= 0.01

        @classmethod
        def add(cls, player, times=1):
            if times == 0:
                return
            for i in range(times):
                if MentRezA.has(player):
                    Notify.add('添加%s：%s！{color=#FF4500}抵消{/color}1层状态:精神的释放!' % (cls.kind, cls.name))
                    MentRezA.subByType(player)
                elif MentRezB.has(player):
                    Notify.add('添加%s：%s！{color=#FF4500}抵消{/color}1层状态:精神的平复！' % (cls.kind, cls.name))
                    MentRezB.subByType(player)
                else:
                    cls.defaultAddEffect(player)

        def afterSleepAction(self, player):
            if self.stacks >= 4 and not BookConcEffect.has(player):
                Notify.add('焦虑层数大于3，{color=#FF4500}转化{/color}为状态：偏执！')
                MentPun.add(player)
                self.clear(player)


    class PhysRezA(Effect):
        id = 230
        name = '良好的睡眠'
        kind = '状态'
        maxDuration = 1
        maxStacks = 99
        info = '休息或过夜有概率获得。\n' \
            '{color=#7CFC00}抵消{/color}相同层数状态：过劳。'  # 66%
        info_p = '休息后随机获得1~3层，过夜有10%的概率获得1层。\n' \
            '{color=#7CFC00}抵消{/color}相同层数状态：过劳。'  # 66%
        ad = '“梦中的我穿梭在林地的高耸树木之间，又越过由刀刃制成的阶梯和源头是一幅画的宽广河流……”'

        @classmethod
        def defaultAddEffect(cls, player):  # 默认的add函数，禁止重写
            cls.notResetDurationAddEffect(player)

        @classmethod
        def add(cls, player, times=1):
            if times == 0:
                return
            for i in range(times):
                if PhysProb.has(player):
                    Notify.add('添加%s：%s！{color=#7CFC00}抵消{/color}1层状态:过劳！' % (cls.kind, cls.name))
                    PhysProb.subByType(player)
                else:
                    cls.defaultAddEffect(player)


    class PhysRezB(Effect):
        id = 231
        name = '良好的运动'
        kind = '状态'
        maxDuration = 1
        maxStacks = 99
        info = '进行运动类日程后或外出有概率获得。\n' \
            '{color=#7CFC00}抵消{/color}相同层数状态：过劳。'  # 33%
        info_p = '进行部分运动类日程后随机获得0~2层，外出探索有25%的概率获得1层。\n' \
            '{color=#7CFC00}抵消{/color}相同层数状态：过劳。'  # 33%
        ad = '“我的心脏以不同于以往的速度躁动跳跃，仿佛我的肋骨也无法阻拦，如若要挣脱这副残破躯壳的限制……”'

        @classmethod
        def defaultAddEffect(cls, player):  # 默认的add函数，禁止重写
            cls.notResetDurationAddEffect(player)

        @classmethod
        def add(cls, player, times=1):
            if times == 0:
                return
            for i in range(times):
                if PhysProb.has(player):
                    Notify.add('添加%s：%s！{color=#7CFC00}抵消{/color}1层状态:过劳！' % (cls.kind, cls.name))
                    PhysProb.subByType(player)
                else:
                    cls.defaultAddEffect(player)


    class MentRezA(Effect):
        id = 232
        name = '精神的释放'
        kind = '状态'
        maxDuration = 1
        maxStacks = 99
        info = '完成委托时根据消耗的灵感层数获得。\n' \
            '{color=#7CFC00}抵消{/color}相同层数状态：焦虑。'
        info_p = '完成委托时根据消耗的灵感及写作素材层数获得，每10层灵感及写作素材都可以获得1层。\n' \
            '{color=#7CFC00}抵消{/color}相同层数状态：焦虑。'
        ad = '“我掀开盖骨，将我的脑脊液倒进我前方的键盘，于是我的双手在键盘上如起舞的天鹅，我所理解的语言即以字符的形式在屏幕上显现，此时此刻的愉悦紧紧环绕着我的气管，似要将我缢杀。”'

        @classmethod
        def defaultAddEffect(cls, player):  # 默认的add函数，禁止重写
            cls.notResetDurationAddEffect(player)

        @classmethod
        def add(cls, player, times=1):
            if times == 0:
                return
            for i in range(times):
                if MentProb.has(player):
                    Notify.add('添加%s：%s！{color=#7CFC00}抵消{/color}1层状态:焦虑！' % (cls.kind, cls.name))
                    MentProb.subByType(player)
                else:
                    cls.defaultAddEffect(player)


    class MentRezB(Effect):
        id = 233
        name = '精神的平复'
        kind = '状态'
        maxDuration = 1
        maxStacks = 99
        info = '进行休息类日程时有概率获得，周末时每完成一项日程都有大概率获得1层。\n' \
            '{color=#7CFC00}抵消{/color}相同层数状态：焦虑。'  # 33%
        info_p = '进行部分休息类日程后随机获得0~2层，周末时每完成一项日程都有60%的概率获得1层。\n' \
            '{color=#7CFC00}抵消{/color}相同层数状态：焦虑。'  # 33%
        ad = '“我呼吸，尽可能地呼吸。也许下一刻我就失去了呼吸的权利。”'

        @classmethod
        def defaultAddEffect(cls, player):  # 默认的add函数，禁止重写
            cls.notResetDurationAddEffect(player)

        @classmethod
        def add(cls, player, times=1):
            if times == 0:
                return
            for i in range(times):
                if MentProb.has(player):
                    Notify.add('添加%s：%s！{color=#7CFC00}抵消{/color}1层状态:焦虑！' % (cls.kind, cls.name))
                    MentProb.subByType(player)
                else:
                    cls.defaultAddEffect(player)


    class Soreness(Effect):
        id = 240
        name = '酸痛'
        kind = '状态'
        maxDuration = 3
        maxStacks = 99
        info = '每次进行运动时获得4层，拥有该状态时进行任意日程都会获得1层。\n' \
            '每层酸痛都会使起床时额外{color=#FF4500}消耗{/color}少量精神状态。\n' \
            '再次获取不会刷新该状态的持续时间，持续时间结束时获得体弱。\n\n进行{color=#FFFF00}拉伸运动{/color}日程可转化该状态为{color=#FFFF00}体魄。{/color}'
        info_p = '每次进行运动时获得4层，拥有该状态时进行任意日程都会获得1层。\n' \
            '每层酸痛都会使起床时额外{color=#FF4500}消耗{/color}0.5点精神状态。\n' \
            '再次获取不会刷新该状态的持续时间，持续时间结束时获得1层体弱。\n\n进行{color=#FFFF00}拉伸运动{/color}日程可转化该状态为{color=#FFFF00}体魄。{/color}'
        ad = '要成为肌肉体育生……必先劳其心志苦其筋骨饿其体肤……'

        @classmethod
        def defaultAddEffect(cls, player):  # 默认的add函数，禁止重写
            cls.notResetDurationAddEffect(player)

        def afterSleepAction(self, player):
            m = r2(0.5 * self.stacks * f())
            player.mental -= m
            Notify.add('由于酸痛，额外消耗了%s点精神状态。' % m)

        def timeUpAction(self, player):
            Debilitated.add(player)

        def afterTaskAction(self, player, task):  # 日程后
            self.add(player)


    class Inspiration(Effect):
        id = 241
        name = '灵感'
        kind = '状态'
        maxDuration = 3
        maxStacks = 99
        info = '当进行的日程与上一个日程不同时获得。\n' \
            '完成委托将消耗该增益，每层都能{color=#7CFC00}提升{/color}获得的精神的释放层数和委托价值。\n' \
            '再次获取不会刷新该状态的持续时间，持续时间结束时获得偏执。\n\n进行{color=#FFFF00}记录想法{/color}日程可转化该状态为{color=#FFFF00}写作素材。{/color}'
        info_p = '当进行的日程与上一个日程不同时获得1层。\n' \
            '完成委托，随笔写作或集中写作将消耗该增益，每层都能{color=#7CFC00}提升{/color}获得的精神的释放层数和委托价值。\n' \
            '再次获取不会刷新该状态的持续时间，持续时间结束时获得1层偏执。\n\n进行{color=#FFFF00}记录想法{/color}日程可转化该状态为{color=#FFFF00}写作素材。{/color}'
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
        maxDuration = 0
        maxStacks = 99
        info = '使用部分食物获得。\n专注度小幅度{color=#FF4500}降低{/color}。\n食物恢复的精神状态随层数大幅{color=#FF4500}降低{/color}，层数较高时食用食物可能会{color=#FF4500}消耗{/color}精神状态。\n进行日程后有大概率移除状态的层数。'
        info_p = '使用部分食物获得。\n专注度{color=#FF4500}降低{/color}10%。\n食物恢复的精神状态每层都会{color=#FF4500}降低{/color}70%，层数较高时食用食物可能会{color=#FF4500}消耗{/color}精神状态。\n进行日程后有75%的概率移除1层该状态。'
        ad = '吃饱了就想睡觉了……'

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


    class Caffeine(Effect):
        id = 243
        name = '咖啡因刺激'
        kind = '状态'
        maxDuration = 0
        maxStacks = 99
        info = '睡眠消耗的精神状态随层数{color=#FF4500}提升{/color}。'
        info_p = '每层都会{color=#FF4500}提升{/color}7.5%睡眠消耗的精神状态。'
        ad = '试图干涉生物体生命活动的内在节律性的结果。'

        def addStackAction(self, player):  # 每次添加层数的操作，一般是某些根据层数给予效果的Effect需要设置
            player.deteriorateConsumption += 0.075

        def subStackAction(self, player):  # 减少层数的操作，前者的反向函数
            player.deteriorateConsumption -= 0.075

    class Anxiety(Effect):
        id = 244
        name = '忧虑'
        kind = '状态'
        maxDuration = 6
        maxStacks = 99
        info = '无法进行写作。'
        info_p = '无法进行随笔写作，完成委托，集中写作日程。'
        ad = '你对自己可能会丢掉工作这件事的担忧占据了大脑。'

        def enableAction(self, player):
            self.duration = ra(player, 4, 6)

    class SleepReward(Effect):
        id = 310
        name = '整备'
        kind = '增益'
        maxDuration = 0
        maxStacks = 99
        info = '进行休息和小睡转化睡意后获得。\n' \
            '随层数{color=#7CFC00}提升{/color}专注度和工作速度，并{color=#7CFC00}降低{/color}精神状态消耗。\n\n{color=#ffff00}存在此增益时，进行全力工作不会受到过劳惩罚。{/color}'
        info_p = '进行休息和小睡转化睡意后获得。\n移除全力工作施加的2层过劳。' \
            '每层都会{color=#7CFC00}提升{/color}8%的专注度和15%的工作速度，并{color=#7CFC00}降低{/color}10%的精神状态消耗。\n\n{color=#ffff00}存在此增益时，进行全力工作不会受到过劳惩罚。{/color}'
        ad = '可我还没有睡饱——'

        def addStackAction(self, player):
            player.basicConcentration += 8
            player.workSpeed += 0.15
            player.basicConsumption -= 0.1

        def subStackAction(self, player):
            player.basicConcentration -= 8
            player.workSpeed -= 0.15
            player.basicConsumption += 0.1

        def afterTaskAction(self, player, task):
            self.clear(player)


    class CommissionReward(Effect):
        id = 311
        name = '释然'
        kind = '增益'
        maxDuration = 2
        maxStacks = 1
        info = '结束委托后获得。\n' \
            '日程结算专注度{color=#7CFC00}提升{/color}，精神状态恢复{color=#7CFC00}提升{/color}。'
        info_p = '结束委托后获得。\n' \
            '日程结算专注度{color=#7CFC00}提升{/color}25%，精神状态恢复{color=#7CFC00}提升{/color}25%。'
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


    class MeetingReward(Effect):
        id = 313
        name = '会议指导'
        kind = '增益'
        maxDuration = 7
        maxStacks = 1
        info = '参加周会议后获得。\n' \
            '对工作类日程的专注度{color=#7CFC00}提升{/color}，工作能力暂时{color=#7CFC00}提升{/color}。'
        info_p = '参加周会议后获得。\n' \
            '对工作类日程的专注度{color=#7CFC00}提升{/color}20%，工作能力暂时{color=#7CFC00}提升{/color}5%。'
        ad = '“是的，当他将右手攥成指向的姿势，你便要随他的步伐朝那个目标进军。”'

        def enableAction(self, player):
            self.duration = ra(player, 4, 7)
            player.workConcentration += 20
            player.workingRegarded += 0.05

        def disableAction(self, player):
            player.workConcentration -= 20
            player.workingRegarded -= 0.05


    class CleanReward(Effect):
        id = 314
        name = '整洁的房间'
        kind = '增益'
        maxDuration = 4
        maxStacks = 1
        info = '进行整理房间日程后获得。\n' \
            '在家中进行日程时，精神状态消耗{color=#7CFC00}降低{/color}，日程的专注度{color=#7CFC00}提升{/color}。'
        info_p = '进行整理房间日程后获得。\n' \
            '在家中进行日程时，精神状态消耗{color=#7CFC00}降低{/color}25%，对家中进行的日程的专注度{color=#7CFC00}提升{/color}25%。'
        ad = '久违的大扫除让你从仪式感中获得些许慰藉。'

        def enableAction(self, player):
            self.duration = ra(player, 2, 4)
            player.homeConsumption -= 0.25  # 家中消耗率
            player.homeConcentration += 25  # 家中专注度

        def disableAction(self, player):
            player.homeConsumption += 0.25  # 家中消耗率
            player.homeConcentration -= 25  # 家中专注度


    class ReadReward(Effect):
        id = 315
        name = '领悟'
        kind = '增益'
        maxDuration = 1
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
        name = '专注度提升'
        kind = '增益'
        maxDuration = 0
        maxStacks = 2
        info = '仅一次对日程的专注度大幅度{color=#7CFC00}提升{/color}。'
        info_p = '仅一次对日程的专注度{color=#7CFC00}提升{/color}60%。'
        ad = '注意力……全集中！'

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
        maxDuration = 1
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
        maxDuration = 1
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
        maxDuration = 1
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
    
    class Smoking(Effect):
        id = 320
        name = '尼古丁刺激'
        kind = '增益'
        maxDuration = 0
        maxStacks = 20
        info = '随层数提升写作技巧，写作专注度，工作专注度和工作速度，暂时降低严重程度。'
        info_p = '每层都会{color=#7CFC00}提升{/color}2%写作技巧，4%写作专注度，4%工作专注度和3%工作速度，严重程度暂时{color=#7CFC00}降低{/color}3%。'
        ad = '身心渐渐放松，有种运动过后无法言语的感觉……'

        def addStackAction(self, player):
            player.writingRegarded += 0.02
            player.writeConcentration += 4
            player.workConcentration += 4
            player.workSpeed += 0.03
            player.severityRegarded -= 0.03

        def subStackAction(self, player):
            player.writingRegarded -= 0.02
            player.writeConcentration -= 4
            player.workConcentration -= 4
            player.workSpeed -= 0.03
            player.severityRegarded += 0.03


    class WarmupEffect(Effect):
        id = 321
        name = '准备运动'
        kind = '增益'
        maxDuration = 0
        maxStacks = 1
        info = '对运动类日程的专注度大幅度{color=#7CFC00}提升{/color}。'
        info_p = '对运动类日程的专注度{color=#7CFC00}提升{/color}30%。'
        ad = '“有备而无患。”'

        def enableAction(self, player):  # 每次添加层数的操作，一般是某些根据层数给予效果的Effect需要设置
            player.sportConcentration += 0.3

        def disableAction(self, player):  # 减少层数的操作，前者的反向函数
            player.sportConcentration -= 0.3


    class Physique(Effect):
        id = 300
        name = '体魄'
        kind = '增益'
        maxDuration = -1
        maxStacks = 99
        info = '由拉伸运动转化酸痛获得。\n' \
            '每层体魄使你起床时{color=#7CFC00}恢复{/color}精神状态并概率获得身体素质。\n每天有概率失去1层，层数越多概率越大。'
        info_p = '由拉伸运动转化酸痛获得。\n' \
            '每层体魄使你起床时{color=#7CFC00}恢复{/color}1.2的精神状态并获得0~0.5*体魄层数的身体素质。\n每天有5%*体魄层数的概率失去1层。'
        ad = '你终于可以说自己是有点肌肉的人了。'

        def afterSleepAction(self, player):
            m = r2(2 * self.stacks * f())

            if HallukeItem1.hasByType(player):
                m *= 1.2

            player.mental += m
            Notify.add('由于体魄，恢复了%s点精神状态。' % m)

            g = ra(player, 0, int(self.stacks/2))
                    
            if g!= 0:
                Notify.add('由于体魄，提升了%s点身体素质。' % g)
                player.physical += 0.01*g

            per = 2.5 * self.stacks
            if HallukeItem1.hasByType(player):
                per *= 0.5

            if rra(player, per):
                self.sub(player)
                Notify.add('体魄随时间失去了1层。')



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
                Notify.add('获得了%s层写作素材！' % newStacks)
            else:
                self.clear(player)


    # D: dependence
    # W: withdrawal
    # E: effect


    class DrugDA(Effect):
        id = 403
        name = '药物依赖{font=arial.ttf}α{/font}'
        kind = '药物反应'
        maxDuration = 1
        maxStacks = 99
        info = '使用药物{font=arial.ttf}α{/font}后解除。\n' \
            '持续时间结束后{color=#FF4500}转化{/color}为戒断反应{font=arial.ttf}α{/font}。'
        info_p = '使用药物{font=arial.ttf}α{/font}后解除。\n' \
            '持续时间结束后{color=#FF4500}转化{/color}为戒断反应{font=arial.ttf}α{/font}。'
        ad = '你偶尔会感到有些恶心。'

        def timeUpAction(self, player):
            DrugWA.add(player)

        @classmethod
        def defaultAddEffect(cls, player):  # 默认的add函数，禁止重写
            cls.notResetDurationAddEffect(player)


    class DrugDB(Effect):
        id = 404
        name = '药物依赖{font=arial.ttf}β{/font}'
        kind = '药物反应'
        maxDuration = 1
        maxStacks = 99
        info = '使用药物{font=arial.ttf}β{/font}后解除。\n' \
            '持续时间结束后{color=#FF4500}转化{/color}为戒断反应{font=arial.ttf}β{/font}。'
        info_p = '使用药物{font=arial.ttf}β{/font}后解除。\n' \
            '持续时间结束后{color=#FF4500}转化{/color}为戒断反应{font=arial.ttf}β{/font}。'
        ad = '你偶尔会感到有些头晕。'

        def timeUpAction(self, player):
            DrugWB.add(player)

        @classmethod
        def defaultAddEffect(cls, player):  # 默认的add函数，禁止重写
            cls.notResetDurationAddEffect(player)


    class DrugDC(Effect):
        id = 405
        name = '药物依赖{font=arial.ttf}γ{/font}'
        kind = '药物反应'
        maxDuration = 1
        maxStacks = 99
        info = '使用药物{font=arial.ttf}γ{/font}后解除。\n' \
            '持续时间结束后{color=#FF4500}转化{/color}为戒断反应{font=arial.ttf}γ{/font}。'
        info_p = '使用药物{font=arial.ttf}γ{/font}后解除。\n' \
            '持续时间结束后{color=#FF4500}转化{/color}为戒断反应{font=arial.ttf}γ{/font}。'
        ad = '你偶尔会眼前一黑。'

        def timeUpAction(self, player):
            DrugWC.add(player)

        @classmethod
        def defaultAddEffect(cls, player):  # 默认的add函数，禁止重写
            cls.notResetDurationAddEffect(player)


    class DrugWA(Effect):
        id = 400
        name = '戒断反应{font=arial.ttf}α{/font}'
        kind = '药物反应'
        maxDuration = 1
        maxStacks = 1
        info = '专注度大幅度{color=#FF4500}降低{/color}，精神状态消耗超大幅度{color=#FF4500}提升{/color}。\n'\
            '你需要尽快服用任意剂量的{font=arial.ttf}α{/font}药物，并且在第二天早上才会恢复。\n' \
            '持续时间结束{color=#FF4500}转化{/color}为衰退。'
        info_p = '专注度{color=#FF4500}降低{/color}100%，精神状态消耗{color=#FF4500}提升{/color}200%。\n'\
            '你需要尽快服用任意剂量的{font=arial.ttf}α{/font}药物，并且在第二天早上才会恢复。\n' \
            '持续时间结束{color=#FF4500}转化{/color}为衰退。'
        ad = '反胃感使你频繁跑去厕所呕吐。'

        def enableAction(self, player):
            player.basicConcentration -= 100
            player.basicConsumption += 2

        def disableAction(self, player):
            player.basicConcentration += 100
            player.basicConsumption -= 2

        def timeUpAction(self, player):
            Deterioration.add(player)

        def afterDrug(self, player):
            self.stacks = 0

        def afterSleepAction(self, player):
            if self.stacks == 0:
                self.clear(player)


    class DrugWB(Effect):
        id = 401
        name = '戒断反应{font=arial.ttf}β{/font}'
        kind = '药物反应'
        maxDuration = 1
        maxStacks = 1
        info = '专注度大幅度{color=#FF4500}降低{/color}，精神状态消耗超大幅度{color=#FF4500}提升{/color}。\n' \
            '你需要尽快服用任意剂量的{font=arial.ttf}β{/font}药物，并且在第二天早上才会恢复。\n' \
            '持续时间结束{color=#FF4500}转化{/color}为衰退。'
        info_p = '专注度{color=#FF4500}降低{/color}100%，精神状态消耗{color=#FF4500}提升{/color}200%。\n' \
            '你需要尽快服用任意剂量的{font=arial.ttf}β{/font}药物，并且在第二天早上才会恢复。\n' \
            '持续时间结束{color=#FF4500}转化{/color}为衰退。'
        ad = '重度胸闷让你难以专注工作。'

        def enableAction(self, player):
            player.basicConcentration -= 100
            player.basicConsumption += 2

        def disableAction(self, player):
            player.basicConcentration += 100
            player.basicConsumption -= 2

        def timeUpAction(self, player):
            Deterioration.add(player)

        def afterDrug(self, player):
            self.stacks = 0

        def afterSleepAction(self, player):
            if self.stacks == 0:
                self.clear(player)


    class DrugWC(Effect):
        id = 402
        name = '戒断反应{font=arial.ttf}γ{/font}'
        kind = '药物反应'
        maxDuration = 1
        maxStacks = 1
        info = '专注度大幅度{color=#FF4500}降低{/color}，精神状态消耗超大幅度{color=#FF4500}提升{/color}。\n' \
            '你需要尽快服用任意剂量的{font=arial.ttf}γ{/font}药物，并且在第二天早上才会恢复。\n' \
            '持续时间结束{color=#FF4500}转化{/color}为衰退。'
        info_p = '专注度{color=#FF4500}降低{/color}100%，精神状态消耗{color=#FF4500}提升{/color}200%。\n' \
            '你需要尽快服用任意剂量的{font=arial.ttf}γ{/font}药物，并且在第二天早上才会恢复。\n' \
            '持续时间结束{color=#FF4500}转化{/color}为衰退。'
        ad = '你难以呼吸。'

        def enableAction(self, player):
            player.basicConcentration -= 100
            player.basicConsumption += 2

        def disableAction(self, player):
            player.basicConcentration += 100
            player.basicConsumption -= 2

        def timeUpAction(self, player):
            Deterioration.add(player)

        def afterDrug(self, player):
            self.stacks = 0

        def afterSleepAction(self, player):
            if self.stacks == 0:
                self.clear(player)


    class DrugEA(Effect):
        id = 406
        name = '药物作用{font=arial.ttf}α{/font}'
        kind = '药物反应'
        maxDuration = 0
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


    class DrugEB(Effect):
        id = 407
        name = '药物作用{font=arial.ttf}β{/font}'
        kind = '药物反应'
        maxDuration = 0
        maxStacks = 1
        info = '精神状态恢复超大幅度{color=#FF4500}降低{/color}，但写作能力大幅度{color=#7CFC00}提升{/color}。'
        info_p = '精神状态恢复{color=#FF4500}降低{/color}80%，写作能力暂时{color=#7CFC00}提升{/color}30%。'
        ad = '你开始出现光怪陆离的幻觉。'

        def enableAction(self, player):
            player.basicRecovery -= 0.8
            player.writingRegarded += 0.3

        def disableAction(self, player):
            player.basicRecovery += 0.8
            player.writingRegarded -= 0.3


    class DrugEC(Effect):
        id = 408
        name = '药物作用{font=arial.ttf}γ{/font}'
        kind = '药物反应'
        maxDuration = 0
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
            t *= (100 - MedicineC.resistance_) * 0.01
            t *= Task.getConsScale(player)
            Notify.add('由于药物{font=arial.ttf}γ{/font}，恢复了' + r2s(t) + '点精神状态。')
            player.mental += r2(t)


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
        maxDuration = 0
        maxStacks = 5
        info = '随层数{color=#7CFC00}降低{/color}睡眠消耗的精神状态和专注度。'
        info_p = '{color=#7CFC00}降低{/color}5%睡眠消耗的精神状态，除此之外每层都会{color=#7CFC00}降低{/color}5%睡眠消耗的精神状态和20%专注度。'

        def enableAction(self, player):
            player.deteriorateConsumption -= 0.05

        def disableAction(self, player):
            player.deteriorateConsumption += 0.05

        def addStackAction(self, player):
            player.deteriorateConsumption -= 0.05
            player.basicConcentration -= 0.2
            if self.stacks >1:
                player.severity += 0.01
            elif self.stacks >2:
                player.severity += 0.03
            elif self.stacks >3:
                player.severity += 1000
            
        def subStackAction(self, player):
            player.deteriorateConsumption += 0.05
            player.basicConcentration += 0.2


    class DrugIbuprofenEffect(Effect):
        id = 411
        name = '药物作用：头疼药'
        kind = '药物反应'
        maxDuration = 1
        maxStacks = 3
        info = '每完成一个日程随层数{color=#7CFC00}恢复{/color}微量精神状态。'
        info_p = '完成日程后，每层都会{color=#7CFC00}恢复{/color}5%的当前精神状态。'

        def addStackAction(self, player):
            if self.duration == 1 and self.stacks >1:
                player.severity += 0.1
            elif self.duration == 1 and self.stacks >2:
                player.severity += 1000

        def afterTaskAction(self, player, task):
            t = r2(0.05 * player.mental * self.stacks)
            player.mental += t
            Notify.add('由于头疼药，恢复了' + str(t) + '点精神状态。')




    class DrugColdrexEffect(Effect):
        id = 412
        name = '药物作用：感冒药'
        kind = '药物反应'
        maxDuration = 1
        maxStacks = 5
        info = '{color=#FF4500}降低{/color}少量专注度，使用时若没有生病则结束该药物反应并获得大量严重度。\n' \
            '使用后会延长1天生病的持续时间并根据层数{color=#7CFC00}提升{/color}休息时的恢复概率，但本效果结束时若仍在生病则会{color=#FF4500}降低{/color}生病的持续时间。'
        info_p = '{color=#FF4500}降低{/color}10%专注度，使用时若没有生病则结束该药物反应并获得5点严重度。\n' \
            '使用后会延长1天生病的持续时间，每层都会{color=#7CFC00}提升{/color}10%休息时的恢复概率，但本效果结束时若仍在生病则会{color=#FF4500}降低{/color}2天生病的持续时间。'

        def enableAction(self, player):
            player.basicConcentration -= 10

        def addStackAction(self, player):
            if PhysPun.has(player):
                PhysPun.get(player).duration += 1
            if self.duration == 1 and self.stacks >1:
                player.severity += 0.05
            elif self.duration == 1 and self.stacks >2:
                player.severity += 0.1
            elif self.duration == 1 and self.stacks >3:
                player.severity += 1000

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
        maxDuration = 1
        maxStacks = 1
        info = '写作能力{color=#7CFC00}提升{/color}。'
        info_p = '写作能力暂时{color=#7CFC00}提升{/color}20%。'

        def enableAction(self, player):
            player.writingRegarded += 0.2

        def disableAction(self, player):
            player.writingRegarded -= 0.2

    class BookConcEffect(Effect):
        id = 501
        name = '学习成果：《海边的于秀爱》'
        kind = '学识'
        maxDuration = 1
        maxStacks = 1
        info = '持续时间内过劳和焦虑不会因为层数过多而转化成生病和偏执。持续时间结束时，每有一层过劳和焦虑都会{color=#7CFC00}提升{/color}1点随机属性。'
        info_p = '持续时间内过劳和焦虑不会因为层数过多而转化成生病和偏执。持续时间结束时，每有一层过劳和焦虑都会{color=#7CFC00}提升{/color}1点随机属性。'


    class BookPhysPunEffect(Effect):
        id = 502
        name = '学习成果：《呼吸训练》'
        kind = '学识'
        maxDuration = 1
        maxStacks = 1
        info = '小幅度{color=#7CFC00}提升{/color}生病和受伤的休息恢复率。\n在此期间通过休息治愈生病或受伤时，额外{color=#7CFC00}降低{/color}大量严重度。'
        info_p = '{color=#7CFC00}提升{/color}20%生病和受伤的休息恢复率。\n在此期间通过休息治愈生病或受伤时，额外{color=#7CFC00}降低{/color}10%的当前严重度。'


    class BookQuickReadEffect(Effect):
        id = 503
        name = '学习成果：《量子波动速读》'
        kind = '学识'
        maxDuration = 1
        maxStacks = 4
        info = '效果时间内可以直接在物品栏中使用书籍而不用消耗日程来阅读。'
        info_p = '效果时间内可以直接在物品栏中使用书籍而不用消耗日程来阅读。'



    class BookWorEffect(Effect):
        id = 504
        name = '学习成果：《保持清醒的秘诀》'
        kind = '学识'
        maxDuration = 1
        maxStacks = 10
        info = '按层数{color=#7CFC00}提升{/color}工作速度。'
        info_p = '每层都会{color=#7CFC00}提升{/color}5%的工作速度。'

        def addStackAction(self, player):
            player.workSpeed += 0.05

        def subStackAction(self, player):
            player.workSpeed -= 0.05


    class BookInsEffect(Effect):
        id = 505
        name = '感悟：《2001年的弹珠机》'
        kind = '学识'
        maxDuration = 14
        maxStacks = 1
        info = '每天起床时{color=#7CFC00}获得{/color}灵感，同时有小概率结束该效果。'
        info_p = '每天起床时{color=#7CFC00}获得{/color}灵感，同时有20%的概率结束该效果。'

        def afterSleepAction(self, player):
            Inspiration.add(player)
            if rra(player, 20):
                self.clear(player)


    class BookSportEffect(Effect):
        id = 507
        name = '感悟：《阿斯卡隆之春》'
        kind = '学识'
        maxDuration = 14
        maxStacks = 5
        info = '进行运动类日程有概率{color=#7CFC00}提升{/color}身体素质。'
        info_p = '进行运动类日程随机{color=#7CFC00}提升{/color}0~2点身体素质。'

        def afterTaskAction(self, player, task):  # 日程后
            if task.kind == '运动类':
                if rra(player, 45):

                    if rra(player, 80):
                        Notify.add('由于感悟：《阿斯卡隆之春》，{color=#7CFC00}提升{/color}了1点身体素质！')
                        player.physical += 0.01
                    else:
                        Notify.add('由于感悟：《阿斯卡隆之春》，{color=#7CFC00}提升{/color}了2点身体素质！')
                        player.physical += 0.02

                    self.sub(player)


    class BookWriteEffect(Effect):
        id = 508
        name = '感悟：《亚斯塔禄之冬》'
        kind = '学识'
        maxDuration = 14
        maxStacks = 5
        info = '进行写作类日程有概率{color=#7CFC00}提升{/color}写作技巧。'
        info_p = '进行写作类日程随机{color=#7CFC00}提升{/color}0~2点写作技巧。'

        def afterTaskAction(self, player, task):  # 日程后
            if task.kind == '写作类':
                if rra(player, 45):

                    if rra(player, 80):
                        Notify.add('由于感悟：《亚斯塔禄之冬》，{color=#7CFC00}提升{/color}了1点写作技巧！')
                        player.writing += 0.01
                    else:
                        Notify.add('由于感悟：《亚斯塔禄之冬》，{color=#7CFC00}提升{/color}了2点写作技巧！')
                        player.writing += 0.02
                    self.sub(player)


    class BookCMEffect(Effect):
        id = 509
        name = '感悟：《城堡与莫梭提斯》'
        kind = '学识'
        maxDuration = 7
        maxStacks = 1
        info = '每天起床时{color=#7CFC00}降低{/color}严重度，同时有小概率结束该效果。'
        info_p = '每天起床时{color=#7CFC00}降低{/color}1点严重度，同时有10%的概率结束该效果。'

        def afterSleepAction(self, player):
            Notify.add('由于感悟：《城堡与莫梭提斯》，{color=#7CFC00}降低{/color}1点严重度！')
            player.severity -= 0.01
            if rra(player, 10):
                self.clear(player)


    class BookMEDEffect(Effect):
        id = 510
        name = '感悟：《药：绝望的解决手段》'
        kind = '学识'
        maxDuration = 7
        maxStacks = 5
        info = '进行工作类日程时有概率额外{color=#7CFC00}提升{/color}随机属性。'
        info_p = '进行工作类日程时有概率额外{color=#7CFC00}提升{/color}随机属性。'

        def afterTaskAction(self, player, task):  # 日程后
            if task.kind == '工作类':
                used = False
                while rra(player, 50):
                    if rra(player, 20):
                        Notify.add('由于感悟：《药：绝望的解决手段》，{color=#7CFC00}提升{/color}了1点身体素质！')
                        player.physical += 0.01
                        used = True
                    if rra(player, 20):
                        Notify.add('由于感悟：《药：绝望的解决手段》，{color=#7CFC00}提升{/color}了1点写作技巧！')
                        player.writing += 0.01
                        used = True
                    if rra(player, 20):
                        Notify.add('由于感悟：《药：绝望的解决手段》，{color=#7CFC00}提升{/color}了1点工作能力！')
                        player.working += 0.01
                        used = True
                if used:
                    self.sub(player)

    class BookRiskEffect(Effect):
        id = 511
        name = '感悟：《失而复得》'
        kind = '学识'
        maxDuration = 1
        maxStacks = 1
        info = '效果期间内消耗的精神状态越多，效果结束时降低的严重程度越多，{color=#7CFC00}提升{/color}的工作能力越多。\n若消耗的精神状态低于150则只会获得2层焦虑。'
        info_p = '效果期间内消耗的精神状态越多，效果结束时降低的严重程度越多，{color=#7CFC00}提升{/color}的工作能力越多。\n若消耗的精神状态低于150则只会获得2层焦虑。'
        cons = 0

        def enableAction(self, player):
            type(self).cons = 0
            type(self).renewInfo()
        
        @classmethod
        def renewInfo(cls):
            cls.info = '效果期间内消耗的精神状态越多，效果结束时降低的严重程度越多，{color=#7CFC00}提升{/color}的工作能力越多。\n若消耗的精神状态低于150则只会获得2层焦虑。\n\n当前已消耗精神状态：'+str(cls.cons)

        def timeUpAction(self, player):
            g = r2(type(self).cons * 0.035 * 0.01)
            if type(self).cons>=150:
                player.working += g
                player.severity -= g
                Notify.add('由于感悟：《失而复得》，{color=#7CFC00}提升{/color}了%s点工作能力！' % (g*100))
                Notify.add('由于感悟：《失而复得》，{color=#7CFC00}降低{/color}了%s点严重程度！' % (g*100))
            else:
                MentProb.add(p, 2)
                Notify.add('由于感悟：《失而复得》，{color=#FF4500}获得{/color}了2层焦虑！')
            type(self).info = '效果期间内消耗的精神状态越多，效果结束时降低的严重程度越多，{color=#7CFC00}提升{/color}的工作能力越多。\n若消耗的精神状态低于150则只会获得2层偏执。'

    class ManuscriptPharmacistEffect(Effect):
        id = 512
        name = '学习成果：《药剂师的手稿》'
        kind = '学识'
        maxDuration = 1
        maxStacks = 1
        info = '药物的恢复效果{color=#7CFC00}提升{/color}，但过夜消耗的精神状态和工作消耗的精神状态也{color=#FF4500}提升{/color}。'
        info_p = '药物的恢复效果{color=#7CFC00}提升{/color}25%，但过夜消耗的精神状态和工作消耗的精神状态也{color=#FF4500}提升{/color}25%。'
        cons = 0

        def enableAction(self, player):
            player.workConsumption += 0.25
            player.drugRecovery += 0.25
            player.deteriorateConsumption += 0.25

        def disableAction(self, player):
            player.workConsumption -= 0.25
            player.drugRecovery -= 0.25
            player.deteriorateConsumption -= 0.25

    class GameDifficulty1(Effect):
        id = 600
        name = '病情好转'
        kind = '伤痕'
        maxDuration = -1
        maxStacks = 1
        info = '精神状态消耗大幅度{color=#7CFC00}降低{/color}。\n精神状态恢复大幅度{color=#7CFC00}提升{/color}。\n睡眠消耗的精神状态大幅度{color=#7CFC00}降低{/color}。'
        info_p = '精神状态消耗{color=#7CFC00}降低{/color}50%。\n精神状态恢复{color=#7CFC00}提升{/color}50%。\n睡眠消耗的精神状态{color=#7CFC00}降低{/color}50%。'
        ad = '“你的病情正在逐渐好转，虽然你还是会偶尔头疼，但也许用不了一阵子你就可以脱离药物的治疗。”'

        def enableAction(self, player):
            GameDifficulty2.clearByType(player)
            GameDifficulty3.clearByType(player)
            GameDifficulty4.clearByType(player)
            GameDifficulty5.clearByType(player)
            player.basicConsumption -= 0.5
            player.basicRecovery += 0.5
            player.deteriorateConsumption -= 0.5

        def disableAction(self, player):
            player.basicConsumption += 0.5
            player.basicRecovery -= 0.5
            player.deteriorateConsumption += 0.5

    class GameDifficulty2(Effect):
        id = 601
        name = '病情稳定'
        kind = '伤痕'
        maxDuration = -1
        maxStacks = 1
        info = '精神状态消耗{color=#7CFC00}降低{/color}。\n精神状态恢复{color=#7CFC00}提升{/color}。\n睡眠消耗的精神状态{color=#7CFC00}降低{/color}。'
        info_p = '精神状态消耗{color=#7CFC00}降低{/color}30%。\n精神状态恢复{color=#7CFC00}提升{/color}30%。\n睡眠消耗的精神状态{color=#7CFC00}降低{/color}30%。'
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

    class GameDifficulty3(Effect):
        id = 602
        name = '病情较重'
        kind = '伤痕'
        maxDuration = -1
        maxStacks = 1
        info = ''
        info_p = ''
        ad = '“你的病情相对严重，不要忘记按时吃药，多锻炼，不过相信你已经习惯这样的生活了吧。”'

        def enableAction(self, player):
            GameDifficulty1.clearByType(player)
            GameDifficulty2.clearByType(player)
            GameDifficulty4.clearByType(player)
            GameDifficulty5.clearByType(player)

    
    class GameDifficulty4(Effect):
        id = 603
        name = '病情严重'
        kind = '伤痕'
        maxDuration = -1
        maxStacks = 1
        info = '精神状态消耗小幅度{color=#FF4500}提升{/color}。\n睡眠消耗的精神状态小幅度{color=#FF4500}提升{/color}。'
        info_p = '精神状态消耗{color=#FF4500}提升{/color}20%。\n睡眠消耗的精神状态{color=#FF4500}提升{/color}20%。'
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

    class GameDifficulty5(Effect):
        id = 604
        name = '病情危急'
        kind = '伤痕'
        maxDuration = -1
        maxStacks = 1
        info = '精神状态消耗{color=#FF4500}提升{/color}。\n精神状态恢复{color=#FF4500}降低{/color}。\n睡眠消耗的精神状态{color=#FF4500}提升{/color}。'
        info_p = '精神状态消耗{color=#FF4500}提升{/color}40%。\n精神状态恢复{color=#FF4500}降低{/color}40%。\n睡眠消耗的精神状态{color=#FF4500}提升{/color}40%。'
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

    class GameMode1(Effect):
        id = 605
        name = '偏头痛'
        kind = '伤痕'
        maxDuration = -1
        maxStacks = 99
        info = '药物的恢复效果小幅度提升，但每完成一个日程后以百分比随机{color=#FF4500}消耗{/color}较大范围内的当前精神状态。'
        info_p = '药物的恢复效果提升15%，但每完成一个日程后以百分比随机{color=#FF4500}消耗{/color}0%~50%的当前精神状态。'
        ad = '也许把大脑切开能将痛苦缓解。'

        def enableAction(self, player):
            player.drugRecovery += 0.15

        def disableAction(self, player):
            player.drugRecovery -= 0.15

        def afterTaskAction(self, player, task):
            per = ra(player, 0, 20)
            if rra(player, 50):
                per += ra(player, 0, 20)
            if rra(player, 50):
                per += ra(player, 0, 10)
                
            t = r2(player.mental * per * 0.01)
            if player.mental <0:
                player.mental += t
                Notify.add('由于伤痕：偏头痛，消耗了%s点精神状态！' % -t)
            else:
                player.mental -= t
                Notify.add('由于伤痕：偏头痛，消耗了%s点精神状态！' % t)

    class GameMode2(Effect):
        id = 606
        name = '资源供给'
        kind = '伤痕'
        maxDuration = -1
        maxStacks = 99
        info = '药物的价格自然增长倍率{color=#FF4500}提升{/color}。'
        info_p = '药物的价格自然增长倍率{color=#FF4500}提升{/color}125%。'
        ad = '你的口袋里凭空多出来2000块，这到底是好事还是坏事？'

        def enableAction(self, player):
            player.money += 2000
            player.priceIncrease *= 2.25

    class GameMode3(Effect):
        id = 607
        name = '优越开局'
        kind = '伤痕'
        maxDuration = -1
        maxStacks = 99
        info = '过夜后有概率{color=#FF4500}失去{/color}随机基础属性。'
        info_p = '过夜后工作能力，身体素质，写作技巧各有50%的概率{color=#FF4500}失去{/color}1点。'
        ad = '也许你就不应该出生在这个世上。'

        def enableAction(self, player):
            player.physical += 0.15
            player.writing += 0.15
            player.working += 0.15

        def afterSleepAction(self, player):
            if rra(player, 30):
                player.physical -= 0.02
            if rra(player, 30):
                player.writing -= 0.02
            if rra(player, 30):
                player.working -= 0.02


    class Despair(Effect):
        id = 610
        name = '绝望'
        kind = '伤痕'
        maxDuration = -1
        maxStacks = 99
        info = '我还能活下去吗？'
        info_p = '我还能活下去吗？'

        def addStackAction(self, player):
            player.basicConsumption += 0.05

        def subStackAction(self, player):
            player.basicConsumption -= 0.05

        def afterTaskAction(self, player, task):
            type(self).add(player, ra(player, self.stacks, self.stacks*3))
            t = r2(self.stacks * 5 * f() * player.basicConsumption)
            player.mental -= t
            Notify.add('由于状态：绝望，消耗了%s点精神状态！' % t)

        def afterDrug(self, player):
            self.sub(player, self.stacks-1)


    class LifeIsColorless(Effect):
        id = 611
        name = '生命失去了色彩'
        kind = '伤痕'
        maxDuration = -1
        maxStacks = 1
        info = '活着。'
        info_p = '活着。'



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
        info = '严重程度{color=#FF4500}提升{/color}。\n' \
            '过夜将会{color=#FF4500}失去{/color}相当于该伤痕层数的灵感。\n' \
            '过夜将会{color=#FF4500}失去{/color}相当于该伤痕层数的体魄。'
        info_p = '每层都会{color=#FF4500}提升{/color}10%的严重程度。\n' \
            '每次过夜都会{color=#FF4500}失去{/color}相当于该伤痕层数的灵感。\n' \
            '每次过夜都会{color=#FF4500}失去{/color}相当于该伤痕层数的体魄。'
        ad = '“对你来说可能有毒，但你还是会喝下去。”'

        def addStackAction(self, player):
            player.severityRegarded += 0.1

        def afterSleepAction(self, player):
            if Inspiration.has(player):
                Inspiration.subByType(player, self.stacks)
            if Physique.has(player):
                Physique.subByType(player, self.stacks)

        def subStackAction(self, player):
            player.severityRegarded -= 0.1


    class SmokingAddiction(Effect):
        id = 623
        name = '烟瘾'
        kind = '伤痕'
        maxDuration = 7
        maxStacks = 99
        info = '吸烟后获得。\n层数大于1时，随层数{color=#FF4500}降低{/color}写作技巧，写作专注度，工作专注度和工作速度，{color=#FF4500}提升{/color}严重程度。\n吸烟会刷新该伤痕的持续时间，有概率会{color=#FF4500}叠加{/color}层数或{color=#FF4500}减少{/color}最大持续时间。\n持续时间结束时随层数{color=#FF4500}消耗{/color}精神状态和{color=#FF4500}提升{/color}严重程度，同时有小概率移除1层，但无法完全移除。'
        info_p = '吸烟后获得。\n层数大于1时，每层都会{color=#FF4500}降低{/color}2.5%写作技巧，4.5%写作专注度，4.5%工作专注度和3.5%工作速度，{color=#FF4500}提升{/color}3.5%严重程度。\n吸烟会刷新该伤痕的持续时间，有50%的概率会{color=#FF4500}叠加{/color}层数或{color=#FF4500}减少{/color}最大持续时间。\n持续时间结束时随层数{color=#FF4500}消耗{/color}精神状态和{color=#FF4500}提升{/color}严重程度，同时有25%的概率移除1层，但无法完全移除。'
        ad = '“贪婪从未饕足，自由却囿于一方。”'

        @classmethod
        def defaultClass(cls):
            cls.maxDuration = 7

        def timeUpdate(self, player):
            if self.duration == 0:
                if type(self).maxDuration != 0:
                    Notify.add(type(self).name + '的持续时间为0！')
                self.timeUpAction(player)
            elif self.duration > 0:
                self.duration -= 1

        def timeUpAction(self, player):
            self.duration = type(self).maxDuration
            if rra(player, 25):
                self.stacks = max(1, self.stacks-1)
                self.subStackAction(player)
                type(self).maxDuration += 1
            t = 10 * player.sev() * self.stacks
            Notify.add('由于烟瘾，精神状态降低了%s点！' % t)
            Notify.add('由于烟瘾，严重程度提升了5点！')
            player.mental -= t
            player.severity += 0.05

        def addStackAction(self, player):
            if self.stacks > 1:
                player.writingRegarded -= 0.025
                player.writeConcentration -= 4.5
                player.workConcentration -= 4.5
                player.workSpeed -= 0.035
                player.severityRegarded += 0.035

            if rra(player, 50):
                type(self).maxDuration = max(1, type(self).maxDuration-1)

        def subStackAction(self, player):
            if self.stacks > 1:
                player.writingRegarded += 0.025
                player.writeConcentration += 4.5
                player.workConcentration += 4.5
                player.workSpeed += 0.035
                player.severityRegarded -= 0.035
