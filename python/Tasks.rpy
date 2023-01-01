init python early:
    def doplan(p, pos):
        Stat.record(p,p.plan[pos])
        labelname = p.plan[pos].__name__ + '_beginning'
        renpy.jump(labelname)
        
        




    class NoTask(Task):
        id = 0
        name = '未安排'
        kind = None
        unlocked = True
        info = '该时间段尚未分配工作。'

        @classmethod
        def checkAvailable(cls, player, day, time):
            return '该时间段尚未分配工作。'

    class TestTask(Task):
        id = 1
        name = '测试日程'
        kind = None
        unlocked = True
        info = '跳过日程。'
       

    class DefaultWork(WorkTask):
        id = 100
        name = '完成工作'
        kind = '工作类'
        unlocked = True
        info = '基础消耗：35\n均衡提升工作能力，同时以标准水平完成工作进度。'
        ad = '以你平常的状态和方法对待工作。'

        @classmethod
        def checkAvailable(cls, player, day, time):
            if player.onVacation:
                return '正在放假！'
            if time == 2:
                return '这个时候已经下班了！'
            return True

        @classmethod
        def excePerf(cls, player):
            cons = r2(35 * cls.getConsScale(player))
            a = r2(1.2 * player.workSpeed * player.wor() * f())
            if MeetingReward3.has(player):
                cons = r2(cons * 0.8)
                a = r2(a * 1.15)
            
            g = 0.02 + player.workingGain
            player.mental -= cons
            player.working += g
            player.severity -= 0.01
            player.achievedGoal += a
            Notice.add('消耗了%s点精神状态。' % cons)
            Notice.add('完成了%s点工作进度。' % a)
            Notice.add('降低了1点严重程度。')
            Notice.add('升高了%s点工作能力。' % (int(g * 100)))

        @classmethod
        def goodPerf(cls, player):
            
            cons = r2(35 * cls.getConsScale(player))
            a = r2(1.05 * player.workSpeed * player.wor() * f())
            if MeetingReward3.has(player):
                cons = r2(cons * 0.8)
                a = r2(a * 1.15)
            g = 0.01 + player.workingGain
            player.mental -= cons
            player.working += g
            player.achievedGoal += a
            Notice.add('消耗了%s点精神状态。' % cons)
            Notice.add('完成了%s点工作进度。' % a)
            Notice.add('升高了%s点工作能力。' % (int(g * 100)))

        @classmethod
        def normPerf(cls, player):
            
            cons = r2(40 * cls.getConsScale(player))
            reco = r2(10 * cls.getRecoScale(player))
            a = r2(0.95 * player.workSpeed * player.wor() * f())
            g = 0
            if rra(player, 50):
                g = 0.01 + player.workingGain
            if MeetingReward3.has(player):
                cons = r2(cons * 0.8)
                a = r2(a * 1.15)
            player.mental -= cons
            player.mental -= reco
            player.achievedGoal += a
            player.working += g
            Notice.add('消耗了%s点精神状态。' % cons)
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('完成了%s点工作进度。' % a)
            if g >0:
                Notice.add('升高了%s点工作能力。' % (int(g * 100)))

        @classmethod
        def badPerf(cls, player):
            
            cons = r2(40 * cls.getConsScale(player))
            a = r2(0.75 * player.workSpeed * player.wor() * f())
            if MeetingReward3.has(player):
                cons = r2(cons * 0.8)
                a = r2(a * 1.15)
            player.mental -= cons
            player.severity -= 0.02
            player.achievedGoal += a
            Notice.add('消耗了%s点精神状态。' % cons)
            Notice.add('完成了%s点工作进度。' % a)
            Notice.add('降低了2点严重程度。')


    class LoafingWork(WorkTask):
        id = 101
        name = '偷懒'
        kind = '工作类'
        unlocked = True
        info = '基础消耗：15\n进行偷懒日程时，还可以在日程的进行状态中进行其他的操作。'
        ad = '伪装自己正在工作，同时可以做一些其他事情，比如看书，写点什么或者单纯趴在桌子上。'

        @classmethod
        def checkAvailable(cls, player, day, time):
            if player.onVacation:
                return '正在放假！'
            if time == 2:
                return '这个时候已经下班了！'
            return True

        @classmethod
        def executeTask(cls, player):
            perf = ra(player, 1, 100)
            perf += cls.getConcScale(player)
            #Notice.add('Perf: %s' % perf)
            resultLabel = cls.getResultLabel(player, perf)
            player.updateAfterTask(cls)
            cls.afterTaskResult(player)
            cls.executeAnotherTask(player, player.retval, perf)
            renpy.jump(resultLabel)

        @classmethod
        def executeAnotherTask(cls, player, doWith, perf):
            p = 1 if perf < 50 else 2
            if doWith == 'sleep':
                rec = r2(15 * cls.getRecoScale(player) * player.sleepRecovery * p)
                Notice.add('在工作的间隙中尝试小睡，恢复了%s点精神状态。' % rec)
                player.mental += rec
                if ConcDec.has(player):
                    ConcDec.subByType(player, int(ConcDec.get(player).stacks/2))
                    Notice.add('状态：%s的层数减少了一半！' % ConcDec.name)
                if rra(player, 35 * p):
                    PhysRezA.add(player, 1 if rra(player, 50) else 2)
            elif doWith == 'phy' and player.canSport >= 0:
                rec = r2(10 * cls.getRecoScale(player) * player.sleepRecovery * p)
                Notice.add('在工作的间隙中尝试做些杂活，恢复了%s点精神状态。' % rec)
                if p == 2:
                    player.physical += 0.01
                    Notice.add('流了些汗，提升了1点身体素质。')
                else:
                    PhysRezB.add(player)
                    Notice.add('流了些汗，获得了状态：良好的运动。')
            elif doWith == 'wri' and player.canRead >= 0:
                rec = r2(10 * cls.getRecoScale(player) * player.sleepRecovery * p)
                Notice.add('在工作的间隙中看了一会网络小说，恢复了%s点精神状态，获得了1层灵感。' % rec)
                Inspiration.add(player)
                if p == 2:
                    player.writing += 0.01
                    Notice.add('对写作有了更多的想法，提升了1点写作技巧。')
                else:
                    Notice.add('对写作有了更多的想法，获得了状态：精神的释放。')
                    MentRezA.add(player)
            elif doWith == 'read' and player.canRead >= 0:
                renpy.call_screen(_screen_name="screen_tr_readingbook", player=player)
                book = player.retval
                if book is not None:
                    pro = 1
                    if MeetingReward5.has(player):
                        pro = 2
                    if book.progress == 0:
                        Notice.add('从头开始阅读书本：%s……' % type(book).name)
                        book.readBook(player, pro)
                        
                    elif book.progress == 1:
                        Notice.add('从上次看过的位置继续阅读书本：%s……' % type(book).name)
                        book.readBook(player, pro)
                        
                    if book.progress == 1:
                        Notice.add('完成了一半的进度！')
                    elif book.progress == 2:
                        Notice.add('完成了整本书的阅读！')
            else:
                renpy.say(None, '任务参数错误！')
                renpy.jump("to_the_title")

            if rra(player, 35 * p):
                MentRezB.add(player, 1 if rra(player, 50) else 2)

        @classmethod
        def excePerf(cls, player):
            cons = r2(15 * cls.getConsScale(player))
            if MeetingReward5.has(player):
                cons = r2(cons * 1.2)
            a = r2(0.4 * player.workSpeed * player.wor() * f())
            if MeetingReward6.has(player):
                a = r2(a * 1.3)
            g = 0.01 + player.workingGain
            player.mental -= cons
            player.working += g
            player.achievedGoal += a
            Notice.add('消耗了%s点精神状态。' % cons)
            Notice.add('完成了%s点工作进度。' % a)
            Notice.add('升高了%s点工作能力。' % int(g * 100))

        @classmethod
        def goodPerf(cls, player):
            cons = r2(15 * cls.getConsScale(player))
            a = r2(0.3 * player.workSpeed * player.wor() * f())
            if MeetingReward5.has(player):
                cons = r2(cons * 1.2)
            if MeetingReward6.has(player):
                a = r2(a * 1.3)
            g=0
            if rra(player, 50):
                g = 0.01 + player.workingGain
            player.mental -= cons
            player.achievedGoal += a
            player.working += g
            Notice.add('消耗了%s点精神状态。' % cons)
            Notice.add('完成了%s点工作进度。' % a)
            if g>0:
                Notice.add('升高了%s点工作能力。' % int(g * 100))

        @classmethod
        def normPerf(cls, player):
            cons = r2(20 * cls.getConsScale(player))
            if MeetingReward5.has(player):
                cons = r2(cons * 1.2)
            a = r2(0.15 * player.workSpeed * player.wor() * f())
            if MeetingReward6.has(player):
                a = r2(a * 1.3)
            player.mental -= cons
            player.achievedGoal += a
            Notice.add('消耗了%s点精神状态。' % cons)
            Notice.add('完成了%s点工作进度。' % a)

        @classmethod
        def badPerf(cls, player):
            cons = r2(20 * cls.getConsScale(player))
            if MeetingReward5.has(player):
                cons = r2(cons * 1.2)
            a = r2(0.1 * player.workSpeed * player.wor() * f())
            if MeetingReward6.has(player):
                a = r2(a * 1.3)
            player.mental -= cons
            player.achievedGoal += a
            player.severity += 0.01
            player.working -= 0.01
            Notice.add('消耗了%s点精神状态。' % cons)
            Notice.add('完成了%s点工作进度。' % a)
            Notice.add('升高了1点严重程度。')
            Notice.add('降低了1点工作能力。')


    class OvertimeWork(WorkTask):
        id = 102
        name = '在家工作'
        kind = '工作类'
        unlocked = False
        info = '基础消耗：40\n小概率获得1层过劳。\n\n解锁条件 1.1工作能力解锁。'
        ad = '我是自愿加班的，真的。'

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return '请先单击该日程解锁！'
            if not player.onVacation and time != 2:
                return '现在是正常上班时间！'
            return True

        @classmethod
        def unlockCond(cls, player):
            if player.working < 1.1:
                return '基础工作能力尚未达到要求，需要至少等于1.1'
            return True

        @classmethod
        def getConcScale(cls, player):
            scale = 0
            scale += player.basicConcentration
            scale += player.workConcentration
            scale += player.homeConcentration
            scale += 15 * player.wor() - 20
            scale /= player.sevscale()
            scale = max(0.2, scale)
            return scale

        @classmethod
        def getConsScale(cls, player):
            scale = 1.0
            scale *= player.basicConsumption
            scale *= player.homeConsumption
            scale *= player.phyCons()
            scale *= player.sevscale()
            scale = max(0.2, scale)
            return scale

        @classmethod
        def executeTask(cls, player):
            perf = ra(player, 1, 100)
            perf += cls.getConcScale(player)
            #Notice.add('Perf: %s' % perf)
            resultLabel = cls.getResultLabel(player, perf)
            player.updateAfterTask(cls)
            cls.afterTaskResult(player)
            if player.week >= 2 and player.times >= 10 and PhysProb.has(player) and not player.s7:
                renpy.jump("solitus_route_7")
            renpy.jump(resultLabel)

        @classmethod
        def excePerf(cls, player):
            cons = r2(40 * cls.getConsScale(player))
            a = r2(1.3 * player.workSpeed * player.wor() * f())
            g = 0.02 + player.workingGain
            player.mental -= cons
            player.working += g
            player.severity -= 0.01
            player.achievedGoal += a
            Notice.add('消耗了%s点精神状态。' % cons)
            Notice.add('完成了%s点工作进度。' % a)
            Notice.add('降低了1点严重程度。')
            Notice.add('升高了%s点工作能力。' % int(g * 100))

        @classmethod
        def goodPerf(cls, player):
            cons = r2(40 * cls.getConsScale(player))
            a = r2(1.15 * player.workSpeed * player.wor() * f())
            g = 0.01 + player.workingGain
            player.mental -= cons
            player.working += g
            player.achievedGoal += a
            Notice.add('消耗了%s点精神状态。' % cons)
            Notice.add('完成了%s点工作进度。' % a)
            Notice.add('升高了%s点工作能力。' % int(g * 100))

        @classmethod
        def normPerf(cls, player):
            cons = r2(45 * cls.getConsScale(player))
            reco = r2(10 * cls.getRecoScale(player))
            a = r2(1.05 * player.workSpeed * player.wor() * f())
            g = 0.01 + player.workingGain
            player.mental -= cons
            player.mental -= reco
            player.working += g
            player.achievedGoal += a
            Notice.add('消耗了%s点精神状态。' % cons)
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('完成了%s点工作进度。' % a)
            Notice.add('升高了%s点工作能力。' % int(g * 100))

        @classmethod
        def badPerf(cls, player):
            cons = r2(45 * cls.getConsScale(player))
            a = r2(0.7 * player.workSpeed * player.wor() * f())
            player.mental -= cons
            player.severity += 0.01
            player.achievedGoal += a
            Notice.add('消耗了%s点精神状态。' % cons)
            Notice.add('完成了%s点工作进度。' % a)
            Notice.add('升高了1点严重程度。')

        @classmethod
        def afterTaskResult(cls, player):
            if rra(player, 60):
                PhysProb.add(player)
            if rra(player, 60):
                MentProb.add(player)
            if rra(player, 33):
                PhysProb.add(player)


    class SnapWork(WorkTask):
        id = 103
        name = '小睡'
        kind = '工作类'
        unlocked = False
        info = '基础消耗：0\n' \
            '将睡意转化为整备。\n' \
            '解锁条件 1.2工作能力解锁。'
        ad = '偷偷睡一觉……不会被发现吧？'

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return '请先单击该日程解锁！'
            if player.onVacation:
                return '正在放假！'
            if time == 2:
                return '这个时候已经下班了！'
            return True

        @classmethod
        def unlockCond(cls, player):
            if player.working < 1.2:
                return '基础工作能力尚未达到要求，需要至少等于1.2'
            return True

        @classmethod
        def excePerf(cls, player):
            reco = r2(10 * cls.getRecoScale(player))
            a = r2(0.15 * player.workSpeed * player.wor() * f())
            player.mental += reco
            player.achievedGoal += a
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('完成了%s点工作进度。' % a)

        @classmethod
        def goodPerf(cls, player):
            reco = r2(10 * cls.getRecoScale(player))
            a = r2(0.125 * player.workSpeed * player.wor() * f())
            PhysRezA.add(player)
            player.mental += reco
            player.achievedGoal += a
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('完成了%s点工作进度。' % a)

        @classmethod
        def normPerf(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            a = r2(0.1 * player.workSpeed * player.wor() * f())
            PhysRezA.add(player)
            player.severity -= 0.01
            player.mental += reco
            player.achievedGoal += a
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('完成了%s点工作进度。' % a)
            Notice.add('降低了1点严重程度。')

        @classmethod
        def badPerf(cls, player):
            cons = r2(35 * cls.getConsScale(player))
            a = r2(0.75 * player.workSpeed * player.wor() * f())
            player.mental -= cons
            player.severity += 0.02
            player.achievedGoal += a
            Notice.add('消耗了%s点精神状态。' % cons)
            Notice.add('完成了%s点工作进度。' % a)
            Notice.add('提升了2点严重程度。')  # 被叫醒了

        @classmethod
        def executeTask(cls, player):
            perf = ra(player, 1, 100)
            perf += cls.getConcScale(player)
            #Notice.add('Perf: %s' % perf)
            resultLabel = cls.getResultLabel(player, perf)

            if rra(player, 35 * 1 if perf < 50 else 2):
                PhysRezA.add(player, 1 if rra(player, 50) else 2)

            stacks = 0

            if ConcDec.has(player):
                if MeetingReward4.has(player):
                    stacks = ConcDec.get(player).stacks + 2
                    player.mental += 5 * stacks
                else:
                    stacks = ConcDec.get(player).stacks
                    player.mental += 2.5 * stacks
            
            player.updateAfterTask(cls)

            if stacks != 0 and perf > 18:
                ConcDec.clearByType(player)
                SleepReward.add(player, stacks)
            else:
                ConcDec.clearByType(player)
                SleepReward.add(player, int(stacks*0.5))
            
            if WeatherRainy.has(player):
                Notice.add('由于雨天，降低了2点严重程度！')
                player.severity -= 0.02

            

            renpy.jump(resultLabel)


    class FocusWork(WorkTask):
        id = 104
        name = '全力工作'
        kind = '工作类'
        unlocked = False
        info = '基础消耗：70\n没有整备的情况进行该日程将额外获得2层过劳。\n\n解锁条件 1.3工作能力解锁。'
        ad = '像牲畜一样工作。'

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return '请先单击该日程解锁！'
            if player.onVacation:
                return '正在放假！'
            if time == 2:
                return '这个时候已经下班了！'
            return True

        @classmethod
        def unlockCond(cls, player):
            if player.working < 1.3:
                return '基础工作能力尚未达到要求，需要至少等于1.3'
            return True


        @classmethod
        def executeTask(cls, player):
            perf = ra(player, 1, 100)
            perf += cls.getConcScale(player)
            #Notice.add('Perf: %s' % perf)
            resultLabel = cls.getResultLabel(player, perf)
            cls.afterTaskResult(player)
            player.updateAfterTask(cls)
            renpy.jump(resultLabel)

        @classmethod
        def excePerf(cls, player):
            cons = r2(70 * cls.getConsScale(player))
            a = r2(1.7 * player.workSpeed * player.wor() * f())
            g = 0.03 + player.workingGain
            player.mental -= cons
            player.working += g
            player.severity -= 0.02
            player.achievedGoal += a
            Notice.add('消耗了%s点精神状态。' % cons)
            Notice.add('完成了%s点工作进度。' % a)
            Notice.add('降低了2点严重程度。')
            Notice.add('升高了%s点工作能力。' % int(g * 100))

        @classmethod
        def goodPerf(cls, player):
            cons = r2(70 * cls.getConsScale(player))
            a = r2(1.5 * player.workSpeed * player.wor() * f())
            g = 0.01 + player.workingGain
            player.mental -= cons
            player.working += g
            player.achievedGoal += a
            Notice.add('消耗了%s点精神状态。' % cons)
            Notice.add('完成了%s点工作进度。' % a)
            Notice.add('升高了%s点工作能力。' % int(g * 100))

        @classmethod
        def normPerf(cls, player):
            cons = r2(80 * cls.getConsScale(player))
            a = r2(1.3 * player.workSpeed * player.wor() * f())
            player.mental -= cons
            player.achievedGoal += a
            player.severity += 0.02
            Notice.add('消耗了%s点精神状态。' % cons)
            Notice.add('完成了%s点工作进度。' % a)
            Notice.add('升高了2点严重程度。')

        @classmethod
        def badPerf(cls, player):
            cons = r2(80 * cls.getConsScale(player))
            a = r2(0.6 * player.workSpeed * player.wor() * f())
            player.mental -= cons
            player.achievedGoal += a
            player.severity += 0.02
            Notice.add('消耗了%s点精神状态。' % cons)
            Notice.add('完成了%s点工作进度。' % a)
            Notice.add('升高了2点严重程度。')

        @classmethod
        def afterTaskResult(cls, player):
            if rra(player, 60):
                PhysProb.add(player)
            if rra(player, 60):
                MentProb.add(player)
            if not SleepReward.has(player):
                PhysProb.add(player, 2)


    class MeetingWork(WorkTask):
        id = 105
        name = '参与周研讨会'
        kind = '工作类'
        unlocked = True
        info = '基础消耗：20\n随机获得一种会议指导，结果为优时，再获得一种。'
        ad = '整理本周的工作，确定工作目标和下周要做的工作。'


        @classmethod
        def hasplot(cls, player):
            if player.aco_p in (0, 1, 2, 3, 4, 5, 6, 9, 10, 11, 98):
                return True
            return False

        @classmethod
        def checkAvailable(cls, player, day, time):
            if player.onVacation:
                return '正在放假！'
            if day == 5 and time == 1:
                return True
            return '非会议时间段。'
            

        @classmethod
        def excePerf(cls, player):
            cons = r2(20 * cls.getConsScale(player))
            g = 0.03 + player.workingGain
            player.mental -= cons
            player.working += g
            Notice.add('消耗了%s点精神状态。' % cons)
            Notice.add('升高了%s点工作能力。' % int(g * 100))
            cls.afterTaskResult(player)

        @classmethod
        def goodPerf(cls, player):
            cons = r2(20 * cls.getConsScale(player))
            g = 0.02 + player.workingGain
            player.mental -= cons
            player.working += g
            Notice.add('消耗了%s点精神状态。' % cons)
            Notice.add('升高了%s点工作能力。' % int(g * 100))

        @classmethod
        def normPerf(cls, player):
            cons = r2(25 * cls.getConsScale(player))
            g = 0.01 + player.workingGain
            player.mental -= cons
            player.working += g
            Notice.add('消耗了%s点精神状态。' % cons)
            Notice.add('升高了%s点工作能力。' % int(g * 100))

        @classmethod
        def badPerf(cls, player):
            cons = r2(25 * cls.getConsScale(player))
            g = 0.01 + player.workingGain
            player.mental -= cons
            player.working += g
            Notice.add('消耗了%s点精神状态。' % cons)
            Notice.add('升高了%s点工作能力。' % int(g * 100))

        @classmethod
        def afterTaskResult(cls, player):
            mrs = (MeetingReward1, MeetingReward2, MeetingReward3, MeetingReward4, MeetingReward5, MeetingReward6, MeetingReward7, MeetingReward8)
            mrs = filter(lambda x: not x.has(player), mrs)
            if mrs:
                rca(player, mrs).add(player)
            # some code……  # 剧情


    class DefaultSport(SportTask):
        id = 200
        name = '外出散步'
        kind = '运动类'
        unlocked = True
        info = '基础恢复：20\n偏向于均衡发展的运动，不会在运动中受伤。'
        ad = '走走长路舒活筋骨。'

        @classmethod
        def checkAvailable(cls, player, day, time):
            if player.canOutdoorSport < 0:
                return '外面正在下雨。'
            if player.canSport < 0:
                return '你受伤了，不能做激烈的运动。'
            if not player.onVacation and time != 2:
                return '现在是正常上班时间！'
            return True

        @classmethod
        def getRecoScale(cls, player):
            scale = 1.0
            scale *= player.basicRecovery
            scale *= player.phyReco()
            scale *= player.sportRecovery
            scale *= player.outdoorSportRecovery
            scale /= player.sevscale()
            scale = max(0.2, scale)
            return scale

        @classmethod
        def excePerf(cls, player):
            reco = r2(20 * cls.getRecoScale(player))
            exReco = r2(12.5 * cls.getRecoScale(player))
            g = 0.02 + player.physicalGain
            player.mental += reco + exReco
            player.physical += g
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('额外恢复了%s点精神状态。' % exReco)
            Notice.add('升高了%s点身体素质。' % int(g * 100))
            return "DefaultSport_result_exce"

        @classmethod
        def goodPerf(cls, player):
            reco = r2(20 * cls.getRecoScale(player))
            exReco = r2(10 * cls.getRecoScale(player))
            g = 0.01 + player.physicalGain
            player.mental += reco + exReco
            player.severity -= 0.01
            player.physical += g
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('额外恢复了%s点精神状态。' % exReco)
            Notice.add('降低了1点严重程度。')
            Notice.add('升高了%s点身体素质。' % int(g * 100))
            return "DefaultSport_result_good"

        @classmethod
        def normPerf(cls, player):
            reco = r2(20 * cls.getRecoScale(player))
            g = 0.01 + player.physicalGain
            player.mental += reco
            player.physical += g
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('升高了%s点身体素质。' % int(g * 100))
            return "DefaultSport_result_norm"

        @classmethod
        def badPerf(cls, player):
            reco = r2(20 * cls.getRecoScale(player))
            exReco = r2(15 * cls.getRecoScale(player))
            player.mental += reco + exReco
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('额外恢复了%s点精神状态。' % exReco)
            return "DefaultSport_result_bad"

        @classmethod
        def afterTaskResult(cls, player):
            Soreness.add(player, 4)
            if rra(player, 75):
                PhysRezB.add(player)
            if rra(player, 25):
                PhysRezB.add(player)


    class JoggingSport(SportTask):
        id = 201
        name = '慢跑'
        kind = '运动类'
        unlocked = False
        info = '基础恢复：30\n偏向于减轻严重程度的运动，小概率额外获得1层良好的运动，极少会在运动中受伤。\n\n解锁条件 1.1身体素质解锁。'
        ad = '“我洋溢着活力。”'

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return '请先单击该日程解锁！'
            if player.canOutdoorSport < 0:
                return '外面正在下雨。'
            if player.canSport < 0:
                return '你受伤了，不能做激烈的运动。'
            if not player.onVacation and time != 2:
                return '现在是正常上班时间！'
            return True

        @classmethod
        def unlockCond(cls, player):
            if player.physical < 1.1:
                return '基础身体素质尚未达到要求，需要至少等于1.1'
            return True

        @classmethod
        def getRecoScale(cls, player):
            scale = 1.0
            scale *= player.basicRecovery
            scale *= player.phyReco()
            scale *= player.sportRecovery
            scale *= player.outdoorSportRecovery
            scale /= player.sevscale()
            scale = max(0.2, scale)
            return scale

        @classmethod
        def excePerf(cls, player):
            reco = r2(30 * cls.getRecoScale(player))
            g = 0.02 + player.physicalGain
            player.mental += reco
            player.physical += g
            player.severity -= 0.02
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('升高了%s点身体素质。' % int(g * 100))
            Notice.add('降低了2点严重程度。')

        @classmethod
        def goodPerf(cls, player):
            reco = r2(30 * cls.getRecoScale(player))
            exReco = r2(5 * cls.getRecoScale(player))
            player.mental += reco + exReco
            player.severity -= 0.01
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('额外恢复了%s点精神状态。' % exReco)
            Notice.add('降低了1点严重程度。')

        @classmethod
        def normPerf(cls, player):
            reco = r2(30 * cls.getRecoScale(player))
            player.mental += reco
            player.severity -= 0.02
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('降低了2点严重程度。')

        @classmethod
        def badPerf(cls, player):
            player.severity += 0.01
            Injured.add(player)
            Notice.add('你在运动中受伤了，没有恢复精神状态。')
            Notice.add('升高了1点严重程度。')

        @classmethod
        def afterTaskResult(cls, player):
            if not Injured.has(player):
                Soreness.add(player, 4)

                if rra(player, 75):
                    PhysRezB.add(player)
                if rra(player, 25):
                    PhysRezB.add(player)

                if rra(player, 33):
                    PhysRezB.add(player)


    class FastrunSport(SportTask):
        id = 202
        name = '速跑'
        kind = '运动类'
        unlocked = False
        info = '基础恢复：25\n偏向于提升身体素质的运动，小概率额外获得1层良好的运动，偶尔会在运动中受伤。\n\n解锁条件 1.1身体素质解锁。'
        ad = '“我的心跳平稳又充满力量，汗水从我的皮肤上渗出。”'

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return '请先单击该日程解锁！'
            if player.canOutdoorSport < 0:
                return '外面正在下雨。'
            if player.canSport < 0:
                return '你受伤了，不能做激烈的运动。'
            if not player.onVacation and time != 2:
                return '现在是正常上班时间！'
            return True

        @classmethod
        def unlockCond(cls, player):
            if player.physical < 1.1:
                return '基础身体素质尚未达到要求，需要至少等于1.1'
            return True

        @classmethod
        def getRecoScale(cls, player):
            scale = 1.0
            scale *= player.basicRecovery
            scale *= player.phyReco()
            scale *= player.sportRecovery
            scale *= player.outdoorSportRecovery
            scale /= player.sevscale()
            scale = max(0.2, scale)
            return scale

        @classmethod
        def executeTask(cls, player):
            perf = ra(player, 1, 100)
            perf += cls.getConcScale(player)
            #Notice.add('Perf: %s' % perf)
            resultLabel = cls.getResultLabel(player, perf, c=30)
            player.updateAfterTask(cls)
            cls.afterTaskResult(player)
            renpy.jump(resultLabel)

        @classmethod
        def excePerf(cls, player):
            reco = r2(25 * cls.getRecoScale(player))
            g = 0.02 + player.physicalGain
            if rra(player, 50):
                g+= 0.01
            player.mental += reco
            player.physical += g
            PhysRezB.add(player)
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('升高了%s点身体素质。' % int(g * 100))

        @classmethod
        def goodPerf(cls, player):
            reco = r2(25 * cls.getRecoScale(player))
            g = 0.01 + player.physicalGain
            player.mental += reco
            player.physical += g
            player.severity -= 0.01
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('升高了%s点身体素质。' % int(g * 100))
            Notice.add('降低了1点严重程度。')

        @classmethod
        def normPerf(cls, player):
            reco = r2(25 * cls.getRecoScale(player))
            exReco = r2(10 * cls.getRecoScale(player))
            g = 0.01 + player.physicalGain
            player.physical += g
            player.mental += reco + exReco
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('额外恢复了%s点精神状态。' % exReco)
            Notice.add('升高了%s点身体素质。' % int(g * 100))

        @classmethod
        def badPerf(cls, player):
            player.severity += 0.01
            Injured.add(player)
            Notice.add('你在运动中受伤了，没有恢复精神状态。')
            Notice.add('升高了1点严重程度。')

        @classmethod
        def afterTaskResult(cls, player):
            if not Injured.has(player):
                Soreness.add(player, 4)

                if rra(player, 75):
                    PhysRezB.add(player)
                if rra(player, 25):
                    PhysRezB.add(player)

                if rra(player, 33):
                    PhysRezB.add(player)


    class GymSport(SportTask):
        id = 203
        name = '去健身房健身'
        kind = '运动类'
        unlocked = False
        info = '基础恢复：15\n定制健身日程自定义健身内容。\n单日购卡需40元。\n\n解锁条件 1.2身体素质解锁。'
        ad = '“这部机器，即我的身体，涌动着力量。”'

        @classmethod
        def checkAvailable(cls, player, day, time):
            cls.info = '基础恢复：15\n定制健身日程自定义健身内容。\n单日购卡需%s元。\n\n解锁条件 1.2身体素质解锁。' % r2(0.2*player.price)
            if not cls.isUnlocked(player):
                return '请先单击该日程解锁！'
            if player.canSport < 0:
                return '你受伤了，不能做激烈的运动。'
            if not player.onVacation and time != 2:
                return '现在是正常上班时间！'
            if player.money < r2(0.4*player.price):
                return '你的钱不够单日消费。'
            return True

        @classmethod
        def unlockCond(cls, player):
            if player.physical < 1.2:
                return '基础身体素质尚未达到要求，需要至少等于1.2'
            return True

        @classmethod
        def executeTask(cls, player):
            perf = ra(player, 1, 100)
            perf += cls.getConcScale(player)
            if Injured.has(player):
                cls.badPerf(player)
            elif perf > 85:
                cls.excePerf(player)
            elif perf > 58:
                cls.goodPerf(player)
            else:
                cls.normPerf(player)

            cls.afterTaskResult(player)

        @classmethod
        def excePerf(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            g = 0.02 + player.physicalGain
            player.mental += reco
            player.physical += g
            Soreness.add(player)
            PhysRezB.add(player)
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('升高了%s点身体素质。' % int(g * 100))

        @classmethod
        def goodPerf(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            player.mental += reco
            player.severity -= 0.02
            Soreness.add(player)
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('降低了2点严重程度。')

        @classmethod
        def normPerf(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            exReco = r2(7.5 * cls.getRecoScale(player))
            player.mental += reco + exReco
            PhysRezB.add(player)
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('额外恢复了%s点精神状态。' % exReco)

        @classmethod
        def badPerf(cls, player):
            player.severity += 0.02
            Notice.add('升高了2点严重程度。')

        @classmethod
        def afterTaskResult(cls, player):
            if not Injured.has(player):
                Soreness.add(player, 2)
                PhysRezB.add(player)
                while rra(player, 50):
                    PhysRezB.add(player)


    class BadmintonClass(SportTask):
        id = 204
        name = '羽毛球课程'
        kind = '运动类'
        unlocked = True
        info = '基础恢复：15\n该日程不受专注度状态，不会在运动中受伤。'
        ad = '上课是次要的……主要是为了……'

        @classmethod
        def hasplot(cls, player):
            if player.hal_p == 50:
                return True
            if player.hal_p < 7:
                return True
            return False

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return '请先单击该日程解锁！'
            if not player.onVacation and time != 2:
                return '现在是正常上班时间！'
            if player.canSport < 0:
                return '你受伤了，不能做激烈的运动。'
            if day == 6 and time == 1:
                return True
            return '非课程时间段'

        @classmethod
        def unlockCond(cls, player):
            return '课程已结束！'

        @classmethod
        def executeTask(cls, player):
            perf = ra(player, 1, 100)
            #Notice.add('Perf: %s' % perf)
            resultLabel = cls.getResultLabel(player, perf, 75, 50, 25)
            player.updateAfterTask(cls)
            cls.afterTaskResult(player)
            renpy.jump(resultLabel)

        @classmethod
        def excePerf(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            g = 0.02 + player.physicalGain
            player.mental += reco
            player.physical += g
            player.severity -= 0.02
            PhysRezB.add(player)
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('升高了%s点身体素质。' % int(g * 100))
            Notice.add('降低了2点严重程度。')

        @classmethod
        def goodPerf(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            g = 0.02 + player.physicalGain
            player.mental += reco
            player.physical += g
            player.severity -= 0.02
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('升高了%s点身体素质。' % int(g * 100))
            Notice.add('降低了2点严重程度。')

        @classmethod
        def normPerf(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            g = 0.01 + player.physicalGain
            player.mental += reco
            player.physical += g
            player.severity -= 0.01
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('升高了%s点身体素质。' % int(g * 100))
            Notice.add('降低了1点严重程度。')

        @classmethod
        def badPerf(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            exReco = r2(5 * cls.getRecoScale(player))
            g = 0.02 + player.physicalGain
            player.mental += reco + exReco
            player.physical += g
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('额外恢复了%s点精神状态。' % exReco)
            Notice.add('升高了%s点身体素质。' % int(g * 100))

        @classmethod
        def afterTaskResult(cls, player):
            Soreness.add(player, 4)
            if rra(player, 75):
                PhysRezB.add(player)
            if rra(player, 25):
                PhysRezB.add(player)
            #some code……  # 剧情


    class StretchingSport(SportTask):
        id = 205
        name = '拉伸运动'
        kind = '运动类'
        unlocked = True
        info = '恢复根据酸痛层数的精神状态，将酸痛转化为体魄。'
        ad = '扭动你的手腕和关节直到它们脱臼断裂。'

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not player.onVacation and time != 2:
                return '现在是正常上班时间！'
            if player.canSport < 0:
                return '你受伤了，不能做激烈的运动。'
            return True

        @classmethod
        def executeTask(cls, player):
            Soreness.add(player)
            perf = ra(player, 1, 100)
            perf += cls.getConcScale(player)
            #Notice.add('Perf: %s' % perf)
            resultLabel = cls.getResultLabel(player, perf)
            player.updateAfterTask(cls)
            cls.afterTaskResult(player)
            renpy.jump(resultLabel)

        @classmethod
        def excePerf(cls, player):
            stacks = Soreness.get(player).stacks
            g = stacks * 0.15
            Physique.add(player, int(g))
            if rra(player, 100 * (g-int(g))):
                Physique.add(player)
            Soreness.clearByType(player)
            reco = r2(1 * stacks)
            player.mental += reco
            Notice.add('恢复了%s点精神状态。' % reco)

        @classmethod
        def goodPerf(cls, player):
            stacks = Soreness.get(player).stacks
            g = stacks * 0.13
            Physique.add(player, int(g))
            if rra(player, 100 * (g - int(g))):
                Physique.add(player)
            Soreness.clearByType(player)
            reco = r2(0.8 * stacks)
            player.mental += reco
            Notice.add('恢复了%s点精神状态。' % reco)

        @classmethod
        def normPerf(cls, player):
            stacks = Soreness.get(player).stacks
            g = stacks * 0.11
            Physique.add(player, int(g))
            if rra(player, 100 * (g - int(g))):
                Physique.add(player)
            Soreness.clearByType(player)
            reco = r2(0.7 * stacks)
            player.mental += reco
            Notice.add('恢复了%s点精神状态。' % reco)

        @classmethod
        def badPerf(cls, player):
            stacks = Soreness.get(player).stacks
            g = stacks * 0.1
            Physique.add(player, int(g))
            if rra(player, 100 * (g - int(g))):
                Physique.add(player)
            Soreness.clearByType(player)
            reco = r2(0.6 * stacks)
            player.mental += reco
            Notice.add('恢复了%s点精神状态。' % reco)

        @classmethod
        def afterTaskResult(cls, player):
            if rra(player, 50):
                PhysRezB.add(player)


    class DefaultRead(WriteTask):
        id = 300
        name = '读流行小说'
        kind = '写作类'
        unlocked = True
        info = '基础恢复：12.5\n偏向于均衡发展的阅读，偶尔可以额外多获得1层灵感。'
        ad = '俗话说文人相轻，但偶尔我也是会看点当下流行的小说的……虽然我觉得大多都没我写的好，哼哼。'

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not player.onVacation and time != 2:
                return '现在是正常上班时间！'
            if Anxiety.has(player):
                return '你由于十分担心自己能否有稳定经济来源而没有阅读的欲望。'
            if player.canRead < 0:
                return '情绪过于低落无法专心阅读。'
            return True

        @classmethod
        def excePerf(cls, player):
            reco = r2(12.5 * cls.getRecoScale(player))
            exReco = r2(12.5 * cls.getRecoScale(player))
            g = 0.02 + player.writingGain
            player.mental += reco + exReco
            player.writing += g
            ReadReward.add(player)
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('额外恢复了%s点精神状态。' % exReco)
            Notice.add('升高了%s点写作技巧。' % int(g * 100))

        @classmethod
        def goodPerf(cls, player):
            reco = r2(12.5 * cls.getRecoScale(player))
            exReco = r2(5 * cls.getRecoScale(player))
            player.mental += reco + exReco
            player.severity -= 0.02
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('额外恢复了%s点精神状态。' % exReco)
            Notice.add('降低了2点严重度。')

        @classmethod
        def normPerf(cls, player):
            reco = r2(12.5 * cls.getRecoScale(player))
            exReco = r2(7.5 * cls.getRecoScale(player))
            g = 0.01 + player.writingGain
            player.mental += reco + exReco
            player.writing += g
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('额外恢复了%s点精神状态。' % exReco)
            Notice.add('升高了%s点写作技巧。' % int(g * 100))

        @classmethod
        def badPerf(cls, player):
            reco = r2(10 * cls.getRecoScale(player))
            exReco = r2(15 * cls.getRecoScale(player))
            player.mental += reco + exReco
            player.severity -= 0.01
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('额外恢复了%s点精神状态。' % exReco)


    class SentimentalRead(WriteTask):
        id = 301
        name = '读感伤文学'
        kind = '写作类'
        unlocked = False
        info = '基础恢复：15\n偏向获得灵感的阅读。\n\n解锁条件 1.1写作技巧解锁。'
        ad = '“我的情绪远比平常更为高昂或低沉，但我也仍然无法完全理解这些文字。”'

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return '请先单击该日程解锁！'
            if not player.onVacation and time != 2:
                return '现在是正常上班时间！'
            if Anxiety.has(player):
                return '你由于十分担心自己能否有稳定经济来源而没有阅读的欲望。'
            if player.canRead < 0:
                return '情绪过于低落无法专心阅读。'
            return True

        @classmethod
        def unlockCond(cls, player):
            if player.writing < 1.1:
                return '基础写作技巧尚未达到要求，需要至少等于1.1'
            return True

        @classmethod
        def excePerf(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            player.mental += reco
            player.writing -= 0.02
            ReadReward.add(player)
            Inspiration.add(player, 2)
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('降低了2点写作技巧。')

        @classmethod
        def goodPerf(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            exReco = r2(5 * cls.getRecoScale(player))
            player.mental += reco + exReco
            player.severity -= 0.01
            ReadReward.add(player)
            Inspiration.add(player, 1)
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('额外恢复了%s点精神状态。' % exReco)
            Notice.add('降低了1点严重度。')

        @classmethod
        def normPerf(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            player.mental += reco
            Inspiration.add(player, 1)
            Notice.add('恢复了%s点精神状态。' % reco)

        @classmethod
        def badPerf(cls, player):
            cons = r2(20 * cls.getConsScale(player))
            player.mental -= cons
            player.writing -= 0.01
            Notice.add('消耗了%s点精神状态。' % cons)
            Notice.add('降低了1点写作技巧。')


    class TraditionalRead(WriteTask):
        id = 302
        name = '读传统文学'
        kind = '写作类'
        unlocked = False
        info = '基础恢复：10\n偏向于提升写作技巧的阅读。\n\n解锁条件 1.1写作技巧解锁。'
        ad = '“我的双眼如饥似渴地吸收着文字，仿佛影子吸收光线。”'

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return '请先单击该日程解锁！'
            if not player.onVacation and time != 2:
                return '现在是正常上班时间！'
            if Anxiety.has(player):
                return '你由于十分担心自己能否有稳定经济来源而没有阅读的欲望。'
            if player.canRead < 0:
                return '情绪过于低落无法专心阅读。'
            return True

        @classmethod
        def unlockCond(cls, player):
            if player.writing < 1.1:
                return '基础写作技巧尚未达到要求，需要至少等于1.1'
            return True


        @classmethod
        def excePerf(cls, player):
            reco = r2(10 * cls.getRecoScale(player))
            g = 0.03 + player.writingGain
            player.mental += reco
            player.writing += g
            player.severity += 0.01
            ReadReward.add(player)
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('升高了1点严重度。')
            Notice.add('升高了%s点写作技巧。' % int(g * 100))

        @classmethod
        def goodPerf(cls, player):
            reco = r2(10 * cls.getRecoScale(player))
            exReco = r2(5 * cls.getRecoScale(player))
            g = 0.02 + player.writingGain
            player.mental += reco + exReco
            player.writing += g
            ReadReward.add(player)
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('额外恢复了%s点精神状态。' % exReco)
            Notice.add('升高了%s点写作技巧。' % int(g * 100))

        @classmethod
        def normPerf(cls, player):
            reco = r2(10 * cls.getRecoScale(player))
            g = 0.01 + player.writingGain
            player.mental += reco
            player.severity -= 0.02
            player.writing += g
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('降低了2点严重度。')
            Notice.add('升高了%s点写作技巧。' % int(g * 100))

        @classmethod
        def badPerf(cls, player):
            cons = r2(15 * cls.getConsScale(player))
            player.mental -= cons
            player.severity += 0.01
            Notice.add('消耗了%s点精神状态。' % cons)
            Notice.add('升高了1点严重度。')


    class FreewheelingWriting(WriteTask):
        id = 303
        name = '随笔写作'
        kind = '写作类'
        unlocked = True
        info = '基础恢复：25\n消耗所有状态转化为额外的灵感并作为写作题材进行写作，并消耗所有灵感进行写作，无需接取委托。\n可转化的状态：（焦虑，偏执，悲伤，勃起）'
        ad = '发泄想法与灵感，积累人气，偶尔还能获得打赏，但我并非为金钱才踏上写作。'

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not player.onVacation and time != 2:
                return '现在是正常上班时间！'
            if time != 2:
                return '你只有在晚上才会想写随笔。'
            if Anxiety.has(player):
                return '你由于十分担心自己能否有稳定经济来源而没有写随笔的欲望。'
            if list(filter(lambda x: type(x).name in ('焦虑','偏执','勃起','悲伤'), player.effects))==[]:
                return '你不知道写什么。'
            return True

        @classmethod
        def executeTask(cls, player):
            l = list(filter(lambda x: type(x).name in ('焦虑','偏执','勃起','悲伤'), player.effects))
            s = 0
            for i in (MentProb,MentPun,Erection,Sadness):
                if i.has(player):
                    s += i.get(player).stacks
                    i.clearByType(player)
                    
            Inspiration.add(player, s)
            perf = ra(player, 1, 100)
            perf += cls.getConcScale(player)
            #Notice.add('Perf: %s' % perf)
            resultLabel = cls.getResultLabel(player, perf)
            informalEssay = Comm(player)
            informalEssay.name = rca(player, comm_informal_names)
            if len(comm_informal_names) != 1:
                comm_informal_names.remove(informalEssay.name)
            informalEssay.freewheeling = True
            informalEssay.needWora = -1
            informalEssay.needInspiration = -1
            informalEssay.du = -1
            informalEssay.require = 0.0
            informalEssay.priceFluctuation = 1.0
            informalEssay.write(player)
            c = FinishedCommission(player)
            c.comm = informalEssay
            player.items.append(c)

            cls.afterTaskResult(player)
            player.updateAfterTask(cls)
            renpy.jump(resultLabel)
    
        @classmethod
        def excePerf(cls, player):
            s = 0.015 * player.week if player.week <= 7 else 0.12
            reco = r2(25 * cls.getRecoScale(player))
            player.mental += reco
            player.severity += r2(s)
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('提升了%s点严重度。' % r2(s))

        @classmethod
        def goodPerf(cls, player):
            reco = r2(25 * cls.getRecoScale(player))
            s = 0.012 * player.week if player.week <= 7 else 0.1
            player.mental += reco
            player.severity += r2(s)
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('提升了%s点严重度。' % r2(s))

        @classmethod
        def normPerf(cls, player):
            reco = r2(25 * cls.getRecoScale(player))
            exReco = r2(5 * cls.getRecoScale(player))
            s = 0.01 * player.week if player.week <= 7 else 0.08
            player.mental += reco + exReco
            player.severity += r2(s)
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('额外恢复了%s点精神状态。' % exReco)
            Notice.add('提升了%s点严重度。' % r2(s))

        @classmethod
        def badPerf(cls, player):
            reco = r2(25 * cls.getRecoScale(player))
            player.mental += reco
            player.severity += 0.02
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('提升了2点严重度。')


    class NormalWriting(WriteTask):
        id = 304
        name = '完成委托'
        kind = '写作类'
        unlocked = True
        info = '基础恢复：20\n消耗灵感进行写作，需要在手机上接取委托。'
        ad = '赚点外快罢了，现在谁还没个两份工——'

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not player.onVacation and time != 2:
                return '现在是正常上班时间！'
            if player.canWrite < 0:
                return '情绪过于低落无法专心写作。'
            if Anxiety.has(player):
                return '你由于十分担心自己能否有稳定经济来源而没有写委托的欲望。'
            if not UnfinishedCommission.has(player):
                return '并没有接委托，请先接个委托吧。'
            return True

        @classmethod
        def executeTask(cls, player):
            perf = ra(player, 1, 100)
            perf += cls.getConcScale(player)
            #Notice.add('Perf: %s' % perf)
            resultLabel = cls.getResultLabel(player, perf)
            unf = player.retval
            unf.write(player)

            cls.afterTaskResult(player)
            player.updateAfterTask(cls)
            renpy.jump(resultLabel)

        @classmethod
        def excePerf(cls, player):
            s = 0.015 * player.week if player.week <= 7 else 0.12
            reco = r2(20 * cls.getRecoScale(player))
            player.mental += reco
            player.severity += r2(s)
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('提升了%s点严重度。' % r2(s))

        @classmethod
        def goodPerf(cls, player):
            reco = r2(20 * cls.getRecoScale(player))
            s = 0.012 * player.week if player.week <= 7 else 0.1
            player.mental += reco
            player.severity += r2(s)
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('提升了%s点严重度。' % r2(s))

        @classmethod
        def normPerf(cls, player):
            reco = r2(20 * cls.getRecoScale(player))
            exReco = r2(5 * cls.getRecoScale(player))
            s = 0.01 * player.week if player.week <= 7 else 0.08
            player.mental += reco + exReco
            player.severity += r2(s)
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('额外恢复了%s点精神状态。' % exReco)
            Notice.add('提升了%s点严重度。' % r2(s))

        @classmethod
        def badPerf(cls, player):
            reco = r2(20 * cls.getRecoScale(player))
            player.mental += reco
            player.severity += 0.02
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('提升了2点严重度。')


    class FocusWriting(WriteTask):
        id = 306
        name = '集中写作'
        kind = '写作类'
        unlocked = False
        info = '基础消耗：20\n短暂提升大量写作技巧。\n\n解锁条件 1.2写作技巧解锁。'
        ad = '也许我不该把写作看作放松行为，而应该是一种严肃的脑力工作。'

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return '请先单击该日程解锁！'
            if not player.onVacation and time != 2:
                return '现在是正常上班时间！'
            if Anxiety.has(player):
                return '你由于十分担心自己能否有稳定经济来源而没有写委托的欲望。'
            if player.canWrite < 0:
                return '情绪过于低落无法专心写作。'
            if not UnfinishedCommission.has(player):
                return '并没有接委托，请先接个委托吧。'
            return True

        @classmethod
        def unlockCond(cls, player):
            if player.writing < 1.2:
                return '基础写作技巧尚未达到要求，需要至少等于1.2'
            return True


        @classmethod
        def executeTask(cls, player):
            perf = ra(player, 1, 100)
            perf += cls.getConcScale(player)
            #Notice.add('Perf: %s' % perf)
            resultLabel = cls.getResultLabel(player, perf)

            player.writingRegarded += 0.25

            unf = player.retval
            unf.write(player)
            

            cls.afterTaskResult(player)
            player.writingRegarded -= 0.25
            player.updateAfterTask(cls)
            player.writing += 0.01
            Notice.add('额外提升了1点写作技巧。')
            renpy.jump(resultLabel)

        @classmethod
        def excePerf(cls, player):
            s = 0.015 * player.week if player.week <= 7 else 0.12
            reco = r2(15 * cls.getRecoScale(player))
            player.mental += reco
            player.severity += r2(s)
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('提升了%s点严重度。' % r2(s))

        @classmethod
        def goodPerf(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            s = 0.012 * player.week if player.week <= 7 else 0.1
            player.mental += reco
            player.severity += r2(s)
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('提升了%s点严重度。' % r2(s))

        @classmethod
        def normPerf(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            exReco = r2(5 * cls.getRecoScale(player))
            s = 0.01 * player.week if player.week <= 7 else 0.08
            player.mental += reco + exReco
            player.severity += r2(s)
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('额外恢复了%s点精神状态。' % exReco)
            Notice.add('提升了%s点严重度。' % r2(s))

        @classmethod
        def badPerf(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            player.mental += reco
            player.severity += 0.02
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('提升了2点严重度。')


    class ReadingBook(WriteTask):
        id = 307
        name = '阅读书籍'
        kind = '写作类'
        unlocked = True
        info = '基础恢复：15\n降低严重度并获得1层灵感。\n选择一本物品中的书籍进行完整的阅读，没有书籍无法进行该日程。'
        ad = '“书籍是不死的记忆。”'

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not player.onVacation and time != 2:
                return '现在是正常上班时间！'
            if list(filter(lambda x: type(x).kind == '书本' and type(x).__name__ not in player.itemcd, player.items)) == []:
                return '你暂时并没有可以读的书籍。'
            if Anxiety.has(player):
                return '你由于十分担心自己能否有稳定经济来源而没有阅读的欲望。'
            if player.canRead < 0:
                return '情绪过于低落无法专心阅读。'
            return True
        
        @classmethod
        def executeTask(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            player.mental += reco
            Notice.add('恢复了%s点精神状态。' % reco)
            Inspiration.add(p)
            player.severity -= 0.01
            player.retval.readBook(player, 2)
            player.updateAfterTask(cls)
            resultLabel = cls.getResultLabel(player, rd(1,100))
            cls.afterTaskResult(player)
            renpy.jump(resultLabel)

    class WriteDownInspiration(WriteTask):
        id = 308
        name = '记录想法'
        kind = '写作类'
        unlocked = True
        info = '将灵感转化为写作素材，基于转化的灵感获得少量精神状态。'
        ad = '“回首某个瞬间。下个瞬间即告消逝。”'

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not player.onVacation and time != 2:
                return '现在是正常上班时间！'
            if player.canWrite < 0:
                return '情绪过于低落无法专心写作。'
            return True

        @classmethod
        def executeTask(cls, player):
            Inspiration.add(player)
            perf = ra(player, 1, 100)
            perf += cls.getConcScale(player)
            #Notice.add('Perf: %s' % perf)
            resultLabel = cls.getResultLabel(player, perf)
            player.updateAfterTask(cls)
            renpy.jump(resultLabel)

        @classmethod
        def excePerf(cls, player):
            stacks = Inspiration.get(player).stacks
            g = stacks * 0.9
            FixedInspiration.add(player, int(g))
            if rra(player, 100 * (g-int(g))):
                FixedInspiration.add(player)
            Inspiration.clearByType(player)
            reco = r2(1.8 * stacks)
            player.mental += reco
            Notice.add('恢复了%s点精神状态。' % reco)

        @classmethod
        def goodPerf(cls, player):
            stacks = Inspiration.get(player).stacks
            g = stacks * 0.85
            FixedInspiration.add(player, int(g))
            if rra(player, 100 * (g - int(g))):
                FixedInspiration.add(player)
            Inspiration.clearByType(player)
            reco = r2(1.7 * stacks)
            player.mental += reco
            Notice.add('恢复了%s点精神状态。' % reco)

        @classmethod
        def normPerf(cls, player):
            stacks = Inspiration.get(player).stacks
            g = stacks * 0.8
            FixedInspiration.add(player, int(g))
            if rra(player, 100 * (g - int(g))):
                FixedInspiration.add(player)
            Inspiration.clearByType(player)
            reco = r2(1.6 * stacks)
            player.mental += reco
            Notice.add('恢复了%s点精神状态。' % reco)

        @classmethod
        def badPerf(cls, player):
            stacks = Inspiration.get(player).stacks
            g = stacks * 0.65
            FixedInspiration.add(player, int(g))
            if rra(player, 100 * (g - int(g))):
                FixedInspiration.add(player)
            Inspiration.clearByType(player)
            reco = r2(1.3 * stacks)
            player.mental += reco
            Notice.add('恢复了%s点精神状态。' % reco)


    class Sleep(RestTask):
        id = 400
        name = '在床上休息'
        kind = '休息类'
        unlocked = True
        info = '基础恢复：40\n移除睡意，概率治疗受伤和生病，获得良好的睡眠。'
        ad = '少说话，多睡觉。'

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not player.onVacation and time != 2:
                return '现在是正常上班时间！'
            return True

        @classmethod
        def getRecoScale(cls, player):
            scale = 1.0
            scale *= player.basicRecovery
            scale *= player.sleepRecovery
            scale *= player.phyReco()
            scale /= player.sevscale()
            scale = max(0.2, scale)
            return scale

        @classmethod
        def executeTask(cls, player):
            perf = ra(player, 1, 100)
            perf += cls.getConcScale(player)
            #Notice.add('Perf: %s' % perf)
            resultLabel = cls.getResultLabel(player, perf)

            PhysRezA.add(player)
            if rra(player, 50 * 1 if perf < 50 else 2):
                PhysRezA.add(player, 1 if rra(player, 50) else 2)

            stacks = 0

            if ConcDec.has(player):
                stacks = ConcDec.get(player).stacks
                player.mental += 2.5 * stacks
                ConcDec.clearByType(player)

            

            if PhysPun.has(player):
                PhysPun.get(player).cureBySleep(player)
            elif Injured.has(player):
                Injured.get(player).cureBySleep(player)

            player.updateAfterTask(cls)
            cls.afterTaskResult(player)

            if stacks != 0:
                SleepReward.add(player, stacks)

            if rra(player, 25):  
                Relaxation.add(player)

            if not player.s6 and player.today in (6, 7):
                if Inspiration.has(player):
                    if Inspiration.get(player).stacks >= 5:
                        renpy.jump("solitus_route_6")
            renpy.jump(resultLabel)


        @classmethod
        def excePerf(cls, player):
            reco = r2(40 * cls.getRecoScale(player))
            exReco = r2(10 * cls.getRecoScale(player))
            g = 0.01 + player.physicalGain
            player.mental += reco + exReco
            player.physical += g
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('额外恢复了%s点精神状态。' % exReco)
            Notice.add('升高了%s点身体素质。' % int(g * 100))

        @classmethod
        def goodPerf(cls, player):
            reco = r2(40 * cls.getRecoScale(player))
            exReco = r2(15 * cls.getRecoScale(player))
            player.mental += reco + exReco
            player.severity -= 0.01
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('额外恢复了%s点精神状态。' % exReco)
            Notice.add('降低了1点严重程度。')

        @classmethod
        def normPerf(cls, player):
            reco = r2(35 * cls.getRecoScale(player))
            player.mental += reco
            player.severity -= 0.01
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('降低了1点严重程度。')

        @classmethod
        def badPerf(cls, player):
            reco = r2(25 * cls.getRecoScale(player))
            exReco = r2(15 * cls.getRecoScale(player))
            player.mental += reco + exReco
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.add('额外恢复了%s点精神状态。' % exReco)


    class ComputerGaming(RestTask):
        id = 401
        name = '打游戏'
        kind = '休息类'
        unlocked = True
        info = '基础消耗：10\n有大概率减少过劳或焦虑的持续时间，偶尔能恢复少量精神状态。'
        ad = '玩玩单机或者网络游戏解压。'

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not player.onVacation and time != 2:
                return '现在是正常上班时间！'
            return True

        @classmethod
        def excePerf(cls, player):
            reco = r2(10 * cls.getConsScale(player))
            exReco = r2(15 * cls.getRecoScale(player))
            player.mental += -reco + exReco
            Notice.add('消耗了%s点精神状态。' % reco)
            Notice.add('额外恢复了%s点精神状态。' % exReco)

        @classmethod
        def goodPerf(cls, player):
            reco = r2(10 * cls.getConsScale(player))
            exReco = r2(7.5 * cls.getRecoScale(player))
            player.mental += -reco + exReco
            player.severity += 0.01
            Notice.add('消耗了%s点精神状态。' % reco)
            Notice.add('额外恢复了%s点精神状态。' % exReco)
            Notice.add('升高了1点严重程度。')

        @classmethod
        def normPerf(cls, player):
            reco = r2(10 * cls.getConsScale(player))
            exReco = r2(5 * cls.getRecoScale(player))
            player.mental += -reco + exReco
            player.severity += 0.02
            Notice.add('消耗了%s点精神状态。' % reco)
            Notice.add('额外恢复了%s点精神状态。' % exReco)
            Notice.add('升高了2点严重程度。')
            

        @classmethod
        def badPerf(cls, player):
            reco = r2(10 * cls.getConsScale(player))
            player.mental -= reco
            Notice.add('消耗了%s点精神状态。' % reco)

        @classmethod
        def afterTaskResult(cls, player):
            if PhysProb.has(player):
                if rra(player, 75):
                    PhysProb.get(player).timeUpdate(player)
            
            if MentProb.has(player):
                if rra(player, 75):
                    MentProb.get(player).timeUpdate(player)


    class CleanRoom(RestTask):
        id = 402
        name = '打扫房间'
        kind = '休息类'
        unlocked = True
        info = '基础恢复：15\n获得整洁的房间。如果未过劳还会移除焦虑，如果过劳则增加恢复的精神状态。'
        ad = '收拾收拾屋子吧，瞅你那房间乱得像猪窝一样。'

        @classmethod
        def checkAvailable(cls, player, day, time):
            if CleanReward.has(player):
                return '你的房间很干净，无需打扫。'
            if not player.onVacation and time != 2:
                return '现在是正常上班时间！'
            return True

        @classmethod
        def executeTask(cls, player):
            if PhysProb.has(player):
                reco = r2(25 * cls.getRecoScale(player))
            else:
                reco = r2(15 * cls.getRecoScale(player))
            player.mental += reco
            Notice.add('恢复了%s点精神状态。' % reco)
            player.updateAfterTask(cls)
            cls.afterTaskResult(player)
            renpy.jump("CleanRoom_result")

        @classmethod
        def afterTaskResult(cls, player):
            if not PhysProb.has(player) and MentProb.has(player):
                MentProb.clearByType(player)
            MentRezB.add(player, ra(player, 0, 2))
            CleanReward.add(player)


    class SocialMedia(RestTask):
        id = 403
        name = '上网冲浪'
        kind = '休息类'
        unlocked = False
        info = '基础恢复：15\n该日程不受专注度影响。'
        ad = '和网上的怪胎们聊聊天，或者在莓博上翻翻有没有好看的画作。'
       
        @classmethod
        def unlockCond(cls, player):
            return '当前版本尚未开放此日程。'

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return '请先单击该日程解锁！'
            if not player.onVacation and time != 2:
                return '现在是正常上班时间！'
            return True

        @classmethod
        def executeTask(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            player.mental += reco
            Notice.add('恢复了%s点精神状态。' % reco)
            resultLabel = cls.getResultLabel(player, rd(1,100))
            player.updateAfterTask(cls)
            cls.afterTaskResult(player)
            renpy.jump(resultLabel)

        @classmethod
        def afterTaskResult(cls, player):
            pass  # some codes

    class DoNothing(RestTask):
        id = 404
        name = '发呆'
        kind = '休息类'
        unlocked = True
        info = '基础恢复：0\n什么也不做，跳过一回合。'
        ad = '要问这个日程意义何在，那就要去问问名为额叶损管的人了。'

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not player.onVacation and time != 2:
                return '现在是正常上班时间！'
            return True

        @classmethod
        def executeTask(cls, player):
            player.updateAfterTask(cls)
            cls.afterTaskResult(player)
            renpy.jump("DoNothing_result")

        @classmethod
        def afterTaskResult(cls, player):
            pass  # some codes


    class GoOutside(Task):
        id = 599
        name = '外出'
        kind = '特殊类'
        unlocked = True
        info = '去医院购买药物或者去一些其他的地方。'
        ad = '“一切事物皆有其所在之处，如此物位于此处。”'

        @classmethod
        def hasplot(cls, player):
            if p.sol_p == 0 and p.week >=4 and p.today == 5:
                return True
            elif p.sol_p == 2 and p.week >=8 and p.today == 5:
                return True
            elif player.aco_p == 7:
                return True
            return False

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not player.onVacation and time != 2:
                return '现在是正常上班时间！'
            if player.canExplore < 0:
                return '外面正在刮台风。'
            return True

        @classmethod
        def executeTask(cls, player):
            pass

        @classmethod
        def afterTaskResult(cls, player):
            pass  # some codes

    class HallukeTask1(Task):
        id = 500
        name = '和Halluke打羽毛球'
        kind = '特殊类'
        unlocked = False
        info = '基础恢复：15\n获得1层良好的运动和精神的平复。\n该日程不受专注度影响。'
        ad = '某种意义上的约会。'

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return '日程将根据剧情解锁'
            if player.canSport < 0:
                return '你受伤了，不能做激烈的运动。'
            if day == 7 and time == 1:
                return True
            return '非约定时间'

        @classmethod
        def hasplot(cls, player):
            if player.hal_p in (8, 9, 10):
                return True
            return False

        @classmethod
        def unlockCond(cls, player):
            if player.hal_p == 99:
                return '{color=#ff0000}需要Halluke活着。{/color}'
            return '日程将根据剧情解锁'

        @classmethod
        def executeTask(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            player.mental += reco
            Notice.add('恢复了%s点精神状态。' % reco)
            PhysRezB.add(player)
            MentRezB.add(player)
            player.updateAfterTask(cls)
            renpy.jump("HallukeTask1_result")

    class HallukeTask2(Task):
        id = 501
        name = '去Halluke家'
        kind = '特殊类'
        unlocked = False
        info = '该日程不受专注度影响。'
        ad = '你们已经是恋人关系了，找他聊聊天？或者做些什么？'

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return '日程将根据剧情解锁'
            if day == 6 and time == 1:
                return True
            return '非约定时间'

        @classmethod
        def hasplot(cls, player):
            if player.hal_p == 12:
                return True
            return False

        @classmethod
        def unlockCond(cls, player):
            if player.hal_p == 99:
                return '{color=#ff0000}需要Halluke活着。{/color}'
            return '日程将根据剧情解锁'

        @classmethod
        def executeTask(cls, player):
            player.updateAfterTask(cls)
            renpy.jump("HallukeTask2_result")


    class AcolasTask1(Task):
        id = 600
        name = '完成Acolas的项目'
        kind = '特殊类'
        unlocked = False
        info = '基础消耗：100\n完成进度，获得3层过劳，提升5点严重程度。\n该日程不受专注度影响。'
        ad = '这应该不是什么难事……对吧？。'
        
        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return '日程将根据剧情解锁'
            if day == 5 and time == 2:
                return '你不想在这个时候完成项目。'
            if not player.onVacation and time != 2:
                return '现在是正常上班时间！'
            if not any([x.has(player) for x in (AcolasItem2, AcolasItem3, AcolasItem4)]):
                return '你没有可以完成的设计稿'
            for i in (AcolasItem2, AcolasItem3, AcolasItem4):
                if i.has(p):
                    if i.get(p).progress >= 100:
                        return '你已经完成了项目，没有必要再做那种事了。'
            return True

        @classmethod
        def unlockCond(cls, player):
            if player.aco_p == 99:
                return '{color=#ff0000}需要Acolas活着。{/color}'
            return '日程将根据剧情解锁'

        @classmethod
        def executeTask(cls, player):
            cons = r2(100 * cls.getConsScale(player))
            a = r2(10 * player.workSpeed * f())
            
            player.severity += 0.05

            if AcolasItem2.has(player):
                item = AcolasItem2.get(player)
                if item.progress <= 33:
                    a *= ra(player, 30, 60) * 0.01
                elif item.progress <= 66:
                    a *= ra(player, 15, 30) * 0.01
                else:
                    a *= ra(player, 1, 5) * 0.01
                item.progress += r2(a)
            
            elif AcolasItem3.has(player):
                item = AcolasItem3.get(player)
                if item.progress <= 33:
                    a *= ra(player, 80, 120) * 0.01
                elif item.progress <= 66:
                    a *= ra(player, 65, 85) * 0.01
                else:
                    a *= ra(player, 35, 55) * 0.01
                item.progress += r2(a)

            elif AcolasItem4.has(player):
                item = AcolasItem4.get(player)
                if item.progress < 1:
                    a = item.progress * (1 + item.progress)
                elif item.progress < 10:
                    a = item.progress * (1 + item.progress * 0.01)
                else:
                    a = item.progress * (item.progress * 0.01) + 5
                if a == 0:
                    a = 0.01
                cons += player.mental * 0.5
                item.progress += r2(a)

            player.mental -= cons
            Notice.add('消耗了%s点精神状态。' % cons)
            Notice.add('完成了%s%s的进度。' % (r2(a), '%'))
            if 100 > item.progress:
                Notice.add('还差%s%s。' % (r2(100-item.progress), '%'))
            if item.progress > 100:
                item.progress = 100.0
            Notice.add('提升了5点严重程度。')
            PhysProb.add(player, 3)

            
            player.updateAfterTask(cls)
            if AcolasItem3.has(p) and player.times == 12 and player.today == 4 and player.aco_p == 8:
                renpy.jump("AcolasTask1_loop")
            elif AcolasItem4.has(p) and player.times == 12:
                aa = 0.01 * int(a)
                if aa > 0:
                    player.severity += aa
                    Notice.add('提升了%s点严重程度。' % int(a))
                p.color = (100 - item.progress)* 0.01
                if p.color < 0:
                    p.color = 0.0
                renpy.jump("AcolasTask2_loop")
            else:
                renpy.jump("AcolasTask1_result")

    class AcolasTask2(Task):
        id = 601
        name = '去Acolas家'
        kind = '特殊类'
        unlocked = False
        info = '该日程不受专注度影响。'
        ad = '听说他生病了，去探望他一下吧？切记，不要做蠢事。'

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return '日程将根据剧情解锁'
            if day == 6 and time == 1:
                return True
            return '非约定时间'

        @classmethod
        def hasplot(cls, player):
            if player.hal_p == 8:
                return True
            return False

        @classmethod
        def unlockCond(cls, player):
            if player.aco_p == 99:
                return '{color=#ff0000}需要Acolas活着。{/color}'
            return '日程将根据剧情解锁'

        @classmethod
        def executeTask(cls, player):
            reco = r2(20 * cls.getRecoScale(player))
            player.mental += reco
            Notice.add('恢复了%s点精神状态。' % reco)
            player.updateAfterTask(cls)
            renpy.jump("AcolasTask2_result")