init python early:
    def doplan(p, pos):
        Stat.record(p,p.plan[pos])
        p.plancheck[pos] = True
        labelname = p.plan[pos].__name__ + _('_beginning')
        renpy.jump(labelname)
    
    def donextplan(p):
        if all(p.plancheck):
            renpy.say(None, '1')
            renpy.jump('before_dayend')

        else:
            pos = 0
            for i, done in enumerate(p.plancheck):
                if not done:
                    pos = i
                    break
            doplan(p, pos)
        
        




    class NoTask(Task):
        id = 0
        name = _('未安排')
        kind = None
        unlocked = True
        info = _('该时间段尚未分配工作。')

        @classmethod
        def checkAvailable(cls, player, day, time):
            return _('该时间段尚未分配工作。')

    class SkipTask(Task):
        id = 0
        name = _('睡懒觉')
        kind = None
        unlocked = True
        info = _('你睡过头了……')

        @classmethod
        def checkAvailable(cls, player, day, time):
            return True

    class TestTask(Task):
        id = 1
        name = _('跳过')
        kind = None
        unlocked = True
        info = _('跳过日程。')
       

    class DefaultWork(WorkTask):
        id = 100
        name = _('完成工作')
        kind = _('工作类')
        unlocked = True
        info = _('基础消耗：35\n均衡提升工作能力，同时以标准水平完成工作进度。')
        ad = _('以你平常的状态和方法对待工作。')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if player.experience == 'wri':
                return _('你已经辞掉了工作。')
            if player.onVacation:
                return _('正在放假！')
            if time >= 2:
                return _('这个时候已经下班了！')
            return True

        @classmethod
        def excePerf(cls, player):
            cons = r2(35 * cls.getConsScale(player))
            a = r2(1.2 * player.workSpeed * player.wor() * f())
            if MeetingReward3.has(player):
                cons = r2(cons * 0.8)
                a = r2(a * 1.15)
            
            g = 0.02 + player.workingGain
            player.gain_mental(-cons)
            player.gain_abi(g, 'wor')
            player.gain_abi(-0.01, 'sev')
            player.achievedGoal += a
            Notice.add(_('完成了%s点工作进度。') % a)
            
            if player.des_score < 100 and player.des_p == 2:
                prog = r2(ra(p, 600, 800) * player.wor() * 0.01 * 0.5)
                player.des_score += prog
                Notice.add(_('实习生的能力值提升了%s，当前能力值为%s。') % (prog, player.des_score))


        @classmethod
        def goodPerf(cls, player):
            
            cons = r2(35 * cls.getConsScale(player))
            a = r2(0.95 * player.workSpeed * player.wor() * f())
            if MeetingReward3.has(player):
                cons = r2(cons * 0.8)
                a = r2(a * 1.15)
            g = 0.01 + player.workingGain
            player.gain_mental(-cons)
            player.gain_abi(g, 'wor')
            player.achievedGoal += a
            Notice.add(_('完成了%s点工作进度。') % a)
            if player.des_score < 100 and player.des_p == 2:
                prog = r2(ra(p, 550, 600) * player.wor() * 0.01 * 0.5)
                player.des_score += prog
                Notice.add(_('实习生的能力值提升了%s，当前能力值为%s。') % (prog, player.des_score))

        @classmethod
        def normPerf(cls, player):
            
            cons = r2(40 * cls.getConsScale(player))
            reco = r2(10 * cls.getRecoScale(player))
            a = r2(0.65 * player.workSpeed * player.wor() * f())
            g = 0
            if rra(player, 50):
                g = 0.01 + player.workingGain
            if MeetingReward3.has(player):
                cons = r2(cons * 0.8)
                a = r2(a * 1.15)
            player.gain_mental(-cons)
            player.gain_mental(reco)
            player.achievedGoal += a
            player.gain_abi(g, 'wor')
            Notice.add(_('完成了%s点工作进度。') % a)
            if player.des_score < 100 and player.des_p == 2:
                prog = r2(ra(p, 450, 550) * player.wor() * 0.01 * 0.5)
                player.des_score += prog
                Notice.add(_('实习生的能力值提升了%s，当前能力值为%s。') % (prog, player.des_score))

        @classmethod
        def badPerf(cls, player):
            
            cons = r2(40 * cls.getConsScale(player))
            a = r2(0.75 * player.workSpeed * player.wor() * f())
            if MeetingReward3.has(player):
                cons = r2(cons * 0.8)
                a = r2(a * 1.15)
            player.gain_mental(-cons)
            player.gain_abi(-0.02, 'sev')
            player.achievedGoal += a
            Notice.add(_('完成了%s点工作进度。') % a)
            
            if player.des_score < 100 and player.des_p == 2:
                prog = r2(ra(p, 250, 450) * player.wor() * 0.01 * 0.5)
                player.des_score += prog
                Notice.add(_('实习生的能力值提升了%s，当前能力值为%s。') % (prog, player.des_score))


    class LoafingWork(WorkTask):
        id = 101
        name = _('偷懒')
        kind = _('工作类')
        unlocked = True
        info = _('基础消耗：15\n进行偷懒日程时，还可以在日程的进行状态中进行其他的操作。')
        ad = _('伪装自己正在工作，同时可以做一些其他事情，比如看书，写点什么或者单纯趴在桌子上。')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if player.experience == 'wri':
                return _('你已经辞掉了工作。')
            if player.onVacation:
                return _('正在放假！')
            if time >= 2:
                return _('这个时候已经下班了！')
            return True

        @classmethod
        def executeTask(cls, player):
            if BookRandConcEffect.has(player):
                renpy.call_screen(_screen_name="screen_BookRandConcEffect", player=player, adj=cls.getConcScale(player))
            perf = ra(player, 1, 100)
            perf += cls.getConcScale(player)
            resultLabel = cls.getResultLabel(player, perf)
            cls.executeAnotherTask(player, player.retval, perf)

            player.updateAfterTask(cls)
            cls.afterTaskResult(player)
            
            renpy.jump(resultLabel)

        @classmethod
        def executeAnotherTask(cls, player, doWith, perf):
            p = 1 if perf < 50 else 2
            if doWith == 'sleep':
                rec = r2(15 * cls.getRecoScale(player) * player.sleepRecovery * p)
                player.gain_mental(rec)
                if ConcDec.has(player):
                    ConcDec.subByType(player, int(ConcDec.getstack(player)/2))
                    Notice.add(_('状态：%s的层数减少了一半！') % ConcDec.name)
                if rra(player, 35 * p):
                    PhysRezA.add(player, 1 if rra(player, 50) else 2)
            elif doWith == 'phy' and player.canSport >= 0:
                rec = r2(10 * cls.getRecoScale(player) * player.sleepRecovery * p)
                Notice.add('在工作的间隙中尝试做些杂活……')
                if p == 2:
                    player.gain_abi(0.01, 'phy')
                else:
                    PhysRezB.add(player)
            elif doWith == 'wri' and player.canRead >= 0:
                Notice.add('在工作的间隙中看了一会网络小说……')
                rec = r2(10 * cls.getRecoScale(player) * player.sleepRecovery * p)
                player.gain_mental(rec)
                Inspiration.add(player)
                if p == 2:
                    player.gain_abi(0.01, 'wri')
                else:
                    MentRezA.add(player)
            else:
                for book, allo in player.retval:
                    book.readBook(player, allo)

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
            player.gain_mental(-cons)
            player.gain_abi(g, 'wor')
            player.achievedGoal += a
            Notice.add(_('完成了%s点工作进度。') % a)

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
            player.gain_mental(-cons)
            player.achievedGoal += a
            player.gain_abi(g, 'wor')
            Notice.add(_('完成了%s点工作进度。') % a)

        @classmethod
        def normPerf(cls, player):
            cons = r2(20 * cls.getConsScale(player))
            if MeetingReward5.has(player):
                cons = r2(cons * 1.2)
            a = r2(0.15 * player.workSpeed * player.wor() * f())
            if MeetingReward6.has(player):
                a = r2(a * 1.3)
            player.gain_mental(-cons)
            player.achievedGoal += a
            Notice.add(_('完成了%s点工作进度。') % a)

        @classmethod
        def badPerf(cls, player):
            cons = r2(20 * cls.getConsScale(player))
            if MeetingReward5.has(player):
                cons = r2(cons * 1.2)
            a = r2(0.1 * player.workSpeed * player.wor() * f())
            if MeetingReward6.has(player):
                a = r2(a * 1.3)
            player.gain_mental(-cons)
            player.achievedGoal += a
            player.gain_abi(0.01, 'sev')
            player.gain_abi(-0.01, 'wor')
            Notice.add(_('完成了%s点工作进度。') % a)


    class OvertimeWork(WorkTask):
        id = 102
        name = _('在家工作')
        kind = _('工作类')
        unlocked = False
        info = _('基础消耗：40\n获得1层过劳。\n\n解锁条件 1.1工作能力解锁。')
        ad = _('我是自愿加班的，真的。')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return _('请先单击该日程解锁！')
            if player.experience == 'wri':
                return _('你已经辞掉了工作。')
            if not player.onVacation and time < 2:
                return _('现在是正常上班时间！')
            return True

        @classmethod
        def unlockCond(cls, player):
            if player.working < 1.1:
                return _('基础工作能力尚未达到要求，需要至少等于1.1')
            return True

        @classmethod
        def getConcScale(cls, player):
            scale = 0
            scale += player.basicConcentration
            scale += player.workConcentration
            scale += player.homeConcentration
            scale += 15 * player.wor() - 20
            scale += player.wriConc()
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
        def executeTask(cls, player):
            if BookRandConcEffect.has(player):
                renpy.call_screen(_screen_name="screen_BookRandConcEffect", player=player, adj=cls.getConcScale(player))
            perf = ra(player, 1, 100)
            perf += cls.getConcScale(player)
            #Notice.add('Perf: %s' % perf)
            
            resultLabel = cls.getResultLabel(player, perf)
            player.updateAfterTask(cls)
            cls.afterTaskResult(player)
            if player.week >= 2 and player.times >= 10 and PhysProb.has(player) and not player.s7 and not HotelBuff.has(player) and not CafeBuff.has(player) and not BookstoreBuff.has(player):
                renpy.jump("solitus_route_7")
            renpy.jump(resultLabel)

        @classmethod
        def excePerf(cls, player):
            cons = r2(40 * cls.getConsScale(player))
            a = r2(1.05 * player.workSpeed * player.wor() * f())
            if CleanReward.has(player) and not player.s7 and not HotelBuff.has(player) and not CafeBuff.has(player) and not BookstoreBuff.has(player):
                a = r2(a*1.5)
            
            g = 0.02 + player.workingGain
            player.gain_mental(-cons)
            player.gain_abi(g, 'wor')
            player.gain_abi(-0.01, 'sev')
            player.achievedGoal += a
            Notice.add(_('完成了%s点工作进度。') % a)
            

        @classmethod
        def goodPerf(cls, player):
            cons = r2(40 * cls.getConsScale(player))
            a = r2(0.95 * player.workSpeed * player.wor() * f())
            if CleanReward.has(player) and not HotelBuff.has(player) and not CafeBuff.has(player) and not BookstoreBuff.has(player):
                a = r2(a*1.5)
            g = 0.01 + player.workingGain
            player.gain_mental(-cons)
            player.gain_abi(g, 'wor')
            player.achievedGoal += a
            Notice.add(_('完成了%s点工作进度。') % a)

        @classmethod
        def normPerf(cls, player):
            cons = r2(45 * cls.getConsScale(player))
            reco = r2(10 * cls.getConsScale(player))
            a = r2(0.85 * player.workSpeed * player.wor() * f())
            if CleanReward.has(player) and not HotelBuff.has(player) and not CafeBuff.has(player) and not BookstoreBuff.has(player):
                a = r2(a*1.5)
            g = 0.01 + player.workingGain
            player.gain_mental(-cons)
            player.gain_mental(-reco)
            player.gain_abi(g, 'wor')
            player.achievedGoal += a
            Notice.add(_('完成了%s点工作进度。') % a)

        @classmethod
        def badPerf(cls, player):
            cons = r2(45 * cls.getConsScale(player))
            a = r2(0.6 * player.workSpeed * player.wor() * f())
            if CleanReward.has(player) and not HotelBuff.has(player) and not CafeBuff.has(player) and not BookstoreBuff.has(player):
                a = r2(a*1.5)
            player.gain_mental(-cons)
            player.gain_abi(0.01, 'sev')
            player.achievedGoal += a
            Notice.add(_('完成了%s点工作进度。') % a)

        @classmethod
        def afterTaskResult(cls, player):
            
            if CleanReward.has(player) and not CafeBuff.has(player):
                return
            if rra(player, 100/(1+int(bool(CafeBuff.has(player))))):
                PhysProb.add(player)
            if rra(player, 60):
                MentProb.add(player)
            if rra(player, 50/(1+int(bool(CafeBuff.has(player))))):
                PhysProb.add(player)


    class SnapWork(WorkTask):
        id = 103
        name = _('小睡')
        kind = _('工作类')
        unlocked = False
        info = _('基础消耗：0\n将睡意转化为精神专注。\n解锁条件 1.2工作能力解锁。')
        ad = _('偷偷睡一觉……不会被发现吧？')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return _('请先单击该日程解锁！')
            if player.experience == 'wri':
                return _('你已经辞掉了工作。')
            if player.onVacation:
                return _('正在放假！')
            if time >= 2:
                return _('这个时候已经下班了！')
            return True

        @classmethod
        def unlockCond(cls, player):
            if player.working < 1.2:
                return _('基础工作能力尚未达到要求，需要至少等于1.2')
            return True

        @classmethod
        def excePerf(cls, player):
            reco = r2(10 * cls.getRecoScale(player))
            a = r2(0.15 * player.workSpeed * player.wor() * f())
            player.gain_mental(reco)
            player.achievedGoal += a
            Notice.add(_('完成了%s点工作进度。') % a)
            Stomachache.clearByType(player)
            Headache.clearByType(player)

        @classmethod
        def goodPerf(cls, player):
            reco = r2(10 * cls.getRecoScale(player))
            a = r2(0.125 * player.workSpeed * player.wor() * f())
            PhysRezA.add(player)
            player.gain_mental(reco)
            player.achievedGoal += a
            Notice.add(_('完成了%s点工作进度。') % a)
            Stomachache.clearByType(player)
            Headache.clearByType(player)

        @classmethod
        def normPerf(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            a = r2(0.1 * player.workSpeed * player.wor() * f())
            PhysRezA.add(player)
            player.gain_abi(-0.01, 'sev')
            player.gain_mental(reco)
            player.achievedGoal += a
            Notice.add(_('完成了%s点工作进度。') % a)
            
            Stomachache.clearByType(player)
            Headache.clearByType(player)

        @classmethod
        def badPerf(cls, player):
            cons = r2(35 * cls.getConsScale(player))
            a = r2(0.75 * player.workSpeed * player.wor() * f())
            player.gain_mental(-cons)
            player.gain_abi(0.02, 'sev')
            player.achievedGoal += a
            Notice.add(_('完成了%s点工作进度。') % a)

        @classmethod
        def executeTask(cls, player):
            if BookRandConcEffect.has(player):
                renpy.call_screen(_screen_name="screen_BookRandConcEffect", player=player, adj=cls.getConcScale(player))
            perf = ra(player, 1, 100)
            perf += cls.getConcScale(player)
            #Notice.add('Perf: %s' % perf)
            resultLabel = cls.getResultLabel(player, perf)

            if rra(player, 35 * 1 if perf < 50 else 2):
                PhysRezA.add(player, 1 if rra(player, 50) else 2)

            stacks = 0

            if ConcDec.has(player):
                if MeetingReward4.has(player):
                    stacks = ConcDec.getstack(player) + 2
                    player.gain_mental(5 * stacks)
                else:
                    stacks = ConcDec.getstack(player)
                    player.gain_mental(2.5 * stacks)
            
            player.updateAfterTask(cls)

            if stacks != 0 and perf > 18:
                ConcDec.clearByType(player)
                SleepReward.add(player, stacks)
            else:
                ConcDec.clearByType(player)
                SleepReward.add(player, int(stacks*0.5))
            
            if WeatherRainy.has(player):
                player.gain_abi(-0.02, 'sev', due='雨天')

            

            renpy.jump(resultLabel)


    class FocusWork(WorkTask):
        id = 104
        name = _('全力工作')
        kind = _('工作类')
        unlocked = False
        info = _('基础消耗：70\n没有精神专注的情况进行该日程将额外获得2层过劳。\n\n解锁条件 1.3工作能力解锁。')
        ad = _('像牲畜一样工作。')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return _('请先单击该日程解锁！')
            if player.experience == 'wri':
                return _('你已经辞掉了工作。')
            if player.onVacation:
                return _('正在放假！')
            if time >= 2:
                return _('这个时候已经下班了！')
            return True

        @classmethod
        def unlockCond(cls, player):
            if player.working < 1.3:
                return _('基础工作能力尚未达到要求，需要至少等于1.3')
            return True


        @classmethod
        def executeTask(cls, player):
            if BookRandConcEffect.has(player):
                renpy.call_screen(_screen_name="screen_BookRandConcEffect", player=player, adj=cls.getConcScale(player))
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
            player.gain_mental(-cons)
            player.gain_abi(g, 'wor')
            player.gain_abi(-0.02, 'sev')
            player.achievedGoal += a
            Notice.add(_('完成了%s点工作进度。') % a)
            
            if player.des_score < 100 and player.des_p == 2:
                prog = r2(ra(p, 800, 1000) * player.wor() * 0.01 * 0.5)
                player.des_score += prog
                Notice.add(_('实习生的能力值提升了%s，当前能力值为%s。') % (prog, player.des_score))

        @classmethod
        def goodPerf(cls, player):
            cons = r2(70 * cls.getConsScale(player))
            a = r2(1.5 * player.workSpeed * player.wor() * f())
            g = 0.01 + player.workingGain
            player.gain_mental(-cons)
            player.gain_abi(g, 'wor')
            player.achievedGoal += a
            Notice.add(_('完成了%s点工作进度。') % a)
            if player.des_score < 100 and player.des_p == 2:
                prog = r2(ra(p, 700, 8000) * player.wor() * 0.01 * 0.5)
                player.des_score += prog
                Notice.add(_('实习生的能力值提升了%s，当前能力值为%s。') % (prog, player.des_score))

        @classmethod
        def normPerf(cls, player):
            cons = r2(80 * cls.getConsScale(player))
            a = r2(1.3 * player.workSpeed * player.wor() * f())
            player.gain_mental(-cons)
            player.achievedGoal += a
            player.gain_abi(0.02, 'sev')
            Notice.add(_('完成了%s点工作进度。') % a)
            if player.des_score < 100 and player.des_p == 2:
                prog = r2(ra(p, 600, 700) * player.wor() * 0.01 * 0.5)
                player.des_score += prog
                Notice.add(_('实习生的能力值提升了%s，当前能力值为%s。') % (prog, player.des_score))

        @classmethod
        def badPerf(cls, player):
            cons = r2(80 * cls.getConsScale(player))
            a = r2(0.6 * player.workSpeed * player.wor() * f())
            player.gain_mental(-cons)
            player.achievedGoal += a
            player.gain_abi(0.02, 'sev')
            Notice.add(_('完成了%s点工作进度。') % a)
            if player.des_score < 100 and player.des_p == 2:
                prog = r2(ra(p, 400, 600) * player.wor() * 0.01 * 0.5)
                player.des_score += prog
                Notice.add(_('实习生的能力值提升了%s，当前能力值为%s。') % (prog, player.des_score))

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
        name = _('参与周研讨会')
        kind = _('工作类')
        unlocked = True
        info = _('基础消耗：20\n随机获得一种会议指导。')
        ad = _('整理本周的工作，确定工作目标和下周要做的工作。')


        @classmethod
        def hasplot(cls, player):
            if player.aco_p not in (7, 8, 12, 99):
                return True
            return False

        @classmethod
        def checkAvailable(cls, player, day, time):
            if player.experience == 'wri':
                return _('你已经辞掉了工作。')
            if player.onVacation:
                return _('正在放假！')
            if day == 5 and time == 1:
                return True
            return _('非会议时间段。')
            

        @classmethod
        def excePerf(cls, player):
            cons = r2(20 * cls.getConsScale(player))
            g = 0.03 + player.workingGain
            player.gain_mental(-cons)
            player.gain_abi(g, 'wor')
            if player.des_score < 100 and player.des_p == 2:
                prog = r2(10 * player.wor())
                player.des_score += prog
                Notice.add(_('实习生的能力值提升了%s，当前能力值为%s。') % (prog, player.des_score))

        @classmethod
        def goodPerf(cls, player):
            cons = r2(20 * cls.getConsScale(player))
            g = 0.02 + player.workingGain
            player.gain_mental(-cons)
            player.gain_abi(g, 'wor')
            if player.des_score < 100 and player.des_p == 2:
                prog = r2(10 * player.wor())
                player.des_score += prog
                Notice.add(_('实习生的能力值提升了%s，当前能力值为%s。') % (prog, player.des_score))

        @classmethod
        def normPerf(cls, player):
            cons = r2(25 * cls.getConsScale(player))
            g = 0.01 + player.workingGain
            player.gain_mental(-cons)
            player.gain_abi(g, 'wor')
            if player.des_score < 100 and player.des_p == 2:
                prog = r2(10 * player.wor())
                player.des_score += prog
                Notice.add(_('实习生的能力值提升了%s，当前能力值为%s。') % (prog, player.des_score))

        @classmethod
        def badPerf(cls, player):
            cons = r2(25 * cls.getConsScale(player))
            g = 0.01 + player.workingGain
            player.gain_mental(-cons)
            player.gain_abi(g, 'wor')
            if player.des_score < 100 and player.des_p == 2:
                prog = r2(10 * player.wor())
                player.des_score += prog
                Notice.add(_('实习生的能力值提升了%s，当前能力值为%s。') % (prog, player.des_score))

        @classmethod
        def afterTaskResult(cls, player):

            mrs = (MeetingReward1, MeetingReward2, MeetingReward3, MeetingReward4, MeetingReward5, MeetingReward6, MeetingReward7, MeetingReward8)
            mrs = filter(lambda x: not x.has(player), mrs)
            if mrs:
                rca(player, mrs).add(player)
            # some code……  # 剧情

    class DestotWork(WorkTask):
        id = 106
        name = _('指导Destot完成工作')
        kind = _('工作类')
        unlocked = False
        info = _('基础消耗：70\n完成少量工作进度，提升工作能力同时大幅提升实习生的能力，该日程不受专注度影响。')
        ad = _('辉光是一个疑问。')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return _('日程将根据剧情解锁。')
            if player.experience == 'wri':
                return _('你已经辞掉了工作。')
            if player.onVacation:
                return _('正在放假！')
            if time >= 2:
                return _('这个时候已经下班了！')
            if player.des_score >= 100:
                return _('实习生的能力值已达上限。')
            return True

        @classmethod
        def unlockCond(cls, player):
            if player.des_p == 99:
                return _('{color=#ff0000}需要Destot在公司里。{/color}')
            return _('日程将根据剧情解锁。')

        @classmethod
        def executeTask(cls, player):
            renpy.jump('destot_route_workgame')

        @classmethod
        def excePerf(cls, player):
            cons = r2(60 * cls.getConsScale(player))
            a = r2(0.6 * player.workSpeed * player.wor() * f())
            if MeetingReward3.has(player):
                cons = r2(cons * 0.8)
                a = r2(a * 1.15)
            
            g = 0.03 + player.workingGain
            player.gain_mental(-cons)
            player.gain_abi(g, 'wor')
            player.gain_abi(-0.01, 'sev')
            player.achievedGoal += a
            prog = r2(ra(p, 1700, 2000) * player.wor() * 0.01 * 0.5)
            player.des_score += prog
            Notice.add(_('完成了%s点工作进度。') % a)
            
            Notice.add(_('实习生的能力值提升了%s，当前能力值为%s。') % (prog, player.des_score))

        @classmethod
        def goodPerf(cls, player):
            
            cons = r2(60 * cls.getConsScale(player))
            a = r2(0.425 * player.workSpeed * player.wor() * f())
            if MeetingReward3.has(player):
                cons = r2(cons * 0.8)
                a = r2(a * 1.15)
            g = 0.02 + player.workingGain
            player.gain_mental(-cons)
            player.gain_abi(g, 'wor')
            player.achievedGoal += a
            prog = r2(ra(p, 1200, 1700) * player.wor() * 0.01 * 0.5)
            player.des_score += prog
            Notice.add(_('完成了%s点工作进度。') % a)
            Notice.add(_('实习生的能力值提升了%s，当前能力值为%s。') % (prog, player.des_score))

        @classmethod
        def normPerf(cls, player):
            
            cons = r2(60 * cls.getConsScale(player))
            reco = r2(10 * cls.getRecoScale(player))
            a = r2(0.35 * player.workSpeed * player.wor() * f())
            g = 0
            g = 0.02 + player.workingGain
            if MeetingReward3.has(player):
                cons = r2(cons * 0.8)
                a = r2(a * 1.15)
            player.gain_mental(-cons)
            player.gain_mental(reco)
            player.achievedGoal += a
            player.gain_abi(g, 'wor')
            prog = r2(ra(p, 900, 1200) * player.wor() * 0.01 * 0.5)
            player.des_score += prog
            Notice.add(_('完成了%s点工作进度。') % a)
            Notice.add(_('实习生的能力值提升了%s，当前能力值为%s。') % (prog, player.des_score))

        @classmethod
        def badPerf(cls, player):
            cons = r2(70 * cls.getConsScale(player))
            a = r2(0.45 * player.workSpeed * player.wor() * f())
            if MeetingReward3.has(player):
                cons = r2(cons * 0.8)
                a = r2(a * 1.15)
            g = 0.03 + player.workingGain
            player.gain_mental(-cons)
            player.gain_abi(-0.02, 'sev')
            player.achievedGoal += a
            player.gain_abi(g, 'wor')
            prog = r2(ra(p, 550, 900) * player.wor() * 0.01 * 0.5)
            player.des_score += prog
            Notice.add(_('完成了%s点工作进度。') % a)
            
            Notice.add(_('实习生的能力值提升了%s，当前能力值为%s。') % (prog, player.des_score))

    class CafeWork(WorkTask):
        id = 107
        name = _('代码维护')
        kind = _('工作类')
        unlocked = False
        info = _('基础消耗：50\n日程成功则会提升少量本周工资，每周只能进行一次，不在咖啡馆办公时消耗的精神状态翻倍。\n不会增加工作进度，不会提升实习生进度。\n\n解锁条件 在咖啡馆办公解锁。')
        ad = _('这些屎山代码早该维护一下了，主管肯定会给我加薪的。')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return _('请先单击该日程解锁！')
            if player.experience == 'wri':
                return _('你已经辞掉了工作。')
            if CafeWork_.has(player):
                return _('这周已经进行过代码维护了。')
            return True

        @classmethod
        def valuefunc(cls, player):
            if player.week <= 3:
                return 1.0
            if player.week <= 6:
                return 0.75
            if player.week <= 9:
                return 0.5 
            if player.week <= 12:
                return 0.25 
            return 0.1

        @classmethod
        def unlockCond(cls, player):
            if not CafeBuff.has(player):
                return _('在咖啡馆办公解锁。')
            return True

        @classmethod
        def getConcScale(cls, player):
            scale = 0
            scale += player.basicConcentration
            scale += player.workConcentration
            if player.onVacation:
                scale += player.homeConcentration
            scale += 15 * player.wor() - 20
            scale += player.wriConc()
            scale /= player.sev()
            scale = max(0.2, scale)
            return scale

        @classmethod
        def getConsScale(cls, player):
            scale = 1.0
            scale *= player.basicConsumption
            if player.onVacation:
                scale *= player.homeConsumption
            scale *= player.phyCons()
            scale *= player.sev()
            scale = max(0.2, scale)
            return scale

        @classmethod
        def executeTask(cls, player):
            if BookRandConcEffect.has(player):
                renpy.call_screen(_screen_name="screen_BookRandConcEffect", player=player, adj=cls.getConcScale(player))
            perf = ra(player, 1, 100)
            perf += cls.getConcScale(player)
            #Notice.add('Perf: %s' % perf)
            
            resultLabel = cls.getResultLabel(player, perf)
            player.updateAfterTask(cls)
            cls.afterTaskResult(player)
            renpy.jump(resultLabel)

        @classmethod
        def excePerf(cls, player):
            cons = r2(50 * cls.getConsScale(player))
            if not CafeBuff.has(player):
                cons *= 2
            g = 0.03 + player.workingGain
            player.gain_mental(-cons)
            player.gain_abi(g, 'wor')
            player.gain_abi(0.01, 'sev')
            w = r2(player.wages*0.2*cls.valuefunc(player)*f())
            player.wages += w
            Notice.add(_('提升了%s点每周工资。') % w)

        @classmethod
        def goodPerf(cls, player):
            cons = r2(50 * cls.getConsScale(player))
            if not CafeBuff.has(player):
                cons *= 2
            g = 0.02 + player.workingGain
            player.gain_mental(-cons)
            player.gain_abi(g, 'wor')
            player.gain_abi(0.02, 'sev')
            w = r2(player.wages*0.1*cls.valuefunc(player)*f())
            player.wages += w
            Notice.add(_('提升了%s点每周工资。') % w)

        @classmethod
        def normPerf(cls, player):
            cons = r2(75 * cls.getConsScale(player))
            if not CafeBuff.has(player):
                cons *= 2
            g = 0.02 + player.workingGain
            player.gain_mental(-cons)
            player.gain_abi(g, 'wor')
            player.severity += 0.03
            w = r2(player.wages*0.05*cls.valuefunc(player)*f())
            player.wages += w
            Notice.add(_('提升了%s点每周工资。') % w)

        @classmethod
        def badPerf(cls, player):
            cons = r2(100 * cls.getConsScale(player))
            if not CafeBuff.has(player):
                cons *= 2
            g = 0.01 + player.workingGain
            player.gain_mental(-cons)
            player.gain_abi(g, 'wor')
            player.severity += 0.05
            Headache.add(player)
            w = r2(player.wages*0.025*player.week*f())
            ww = player.wages
            player.wages = max(ww-w, 10)
            Notice.add(_('降低了%s点每周工资。') % w)

        @classmethod
        def afterTaskResult(cls, player):
            CafeWork_.add(player)

    class DefaultSport(SportTask):
        id = 200
        name = _('外出散步')
        kind = _('运动类')
        unlocked = True
        info = _('基础恢复：20\n偏向于均衡发展的运动，不会在运动中受伤。')
        ad = _('走走长路舒活筋骨。')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if player.canOutdoorSport < 0:
                return _('外面正在下雨。')
            if player.canSport < 0:
                return _('你受伤了，不能做激烈的运动。')
            if not player.onVacation and time < 2:
                return _('现在是正常上班时间！')
            return True

        @classmethod
        def executeTask(cls, player):
            if BookRandConcEffect.has(player):
                renpy.call_screen(_screen_name="screen_BookRandConcEffect", player=player, adj=cls.getConcScale(player))
            perf = ra(player, 1, 100)
            perf += cls.getConcScale(player)
            while BookSportEffect.has(player) and perf <= 18:
                perf = ra(player, 1, 100)
            resultLabel = cls.getResultLabel(player, perf)
            player.updateAfterTask(cls)
            cls.afterTaskResult(player)
            renpy.jump(resultLabel)

        @classmethod
        def getRecoScale(cls, player):
            scale = 1.0
            scale *= player.basicRecovery
            scale *= player.phyReco()
            scale *= player.sportRecovery
            scale *= player.outdoorSportRecovery
            scale /= player.sev()
            scale = max(0.2, scale)
            return scale

        @classmethod
        def excePerf(cls, player):
            reco = r2(20 * cls.getRecoScale(player))
            exReco = r2(12.5 * cls.getRecoScale(player))
            g = 0.02 + player.physicalGain
            player.gain_mental(reco)
            player.gain_mental(exReco, extra=True)
            player.gain_abi(g, 'phy')
            return "DefaultSport_result_exce"

        @classmethod
        def goodPerf(cls, player):
            reco = r2(20 * cls.getRecoScale(player))
            exReco = r2(10 * cls.getRecoScale(player))
            g = 0.01 + player.physicalGain
            player.gain_mental(reco)
            player.gain_mental(exReco, extra=True)
            player.gain_abi(-0.01, 'sev')
            player.gain_abi(g, 'phy')
            
            return "DefaultSport_result_good"

        @classmethod
        def normPerf(cls, player):
            reco = r2(20 * cls.getRecoScale(player))
            g = 0.01 + player.physicalGain
            player.gain_mental(reco)
            player.gain_abi(g, 'phy')
            return "DefaultSport_result_norm"

        @classmethod
        def badPerf(cls, player):
            reco = r2(20 * cls.getRecoScale(player))
            exReco = r2(15 * cls.getRecoScale(player))
            player.gain_mental(reco)
            player.gain_mental(exReco, extra=True)
            return "DefaultSport_result_bad"

        @classmethod
        def afterTaskResult(cls, player):
            if rra(player, 50):
                PhysicalLimited.add(player)
            Soreness.add(player, 4)
            if rra(player, 75):
                PhysRezB.add(player)
            if rra(player, 25):
                PhysRezB.add(player)
            if WeatherSmog.has(player):
                WeatherSmog.get(player).check(player)


    class JoggingSport(SportTask):
        id = 201
        name = _('慢跑')
        kind = _('运动类')
        unlocked = False
        info = _('基础恢复：30\n偏向于减轻严重程度的运动，小概率额外获得1层良好的运动，极少会在运动中受伤。\n\n解锁条件 1.1身体素质解锁。')
        ad = _('“我洋溢着活力。”')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return _('请先单击该日程解锁！')
            if player.canOutdoorSport < 0:
                return _('外面正在下雨。')
            if player.canSport < 0:
                return _('你受伤了，不能做激烈的运动。')
            if not player.onVacation and time < 2:
                return _('现在是正常上班时间！')
            return True

        @classmethod
        def executeTask(cls, player):
            if BookRandConcEffect.has(player):
                renpy.call_screen(_screen_name="screen_BookRandConcEffect", player=player, adj=cls.getConcScale(player))
            perf = ra(player, 1, 100)
            perf += cls.getConcScale(player)
            while BookSportEffect.has(player) and perf <= 25:
                perf = ra(player, 1, 100)
            resultLabel = cls.getResultLabel(player, perf, c=25)
            player.updateAfterTask(cls)
            cls.afterTaskResult(player)
            renpy.jump(resultLabel)

        @classmethod
        def unlockCond(cls, player):
            if player.physical < 1.1:
                return _('基础身体素质尚未达到要求，需要至少等于1.1')
            return True

        
        @classmethod
        def getRecoScale(cls, player):
            scale = 1.0
            scale *= player.basicRecovery
            scale *= player.phyReco()
            scale *= player.sportRecovery
            scale *= player.outdoorSportRecovery
            scale /= player.sev()
            scale = max(0.2, scale)
            return scale

        @classmethod
        def excePerf(cls, player):
            reco = r2(30 * cls.getRecoScale(player))
            g = 0.02 + player.physicalGain
            player.gain_mental(reco)
            player.gain_abi(g, 'phy')
            player.gain_abi(-0.02, 'sev')
            

        @classmethod
        def goodPerf(cls, player):
            reco = r2(30 * cls.getRecoScale(player))
            exReco = r2(5 * cls.getRecoScale(player))
            player.gain_mental(reco)
            player.gain_mental(exReco, extra=True)
            player.gain_abi(-0.01, 'sev')
            

        @classmethod
        def normPerf(cls, player):
            reco = r2(30 * cls.getRecoScale(player))
            player.gain_mental(reco)
            player.gain_abi(-0.02, 'sev')
            

        @classmethod
        def badPerf(cls, player):
            player.gain_abi(0.01, 'sev')
            Injured.add(player)
            Notice.add(_('你在运动中受伤了，没有恢复精神状态。'))

        @classmethod
        def afterTaskResult(cls, player):
            if not Injured.has(player):
                if rra(player, 70):
                    PhysicalLimited.add(player)
                Soreness.add(player, 4)

                if rra(player, 75):
                    PhysRezB.add(player)
                if rra(player, 25):
                    PhysRezB.add(player)

                if rra(player, 33):
                    PhysRezB.add(player)
            if WeatherSmog.has(player):
                WeatherSmog.get(player).check(player)


    class FastrunSport(SportTask):
        id = 202
        name = _('速跑')
        kind = _('运动类')
        unlocked = False
        info = _('基础恢复：25\n偏向于提升身体素质的运动，小概率额外获得1层良好的运动，偶尔会在运动中受伤。\n\n解锁条件 1.1身体素质解锁。')
        ad = _('“我的心跳平稳又充满力量，汗水从我的皮肤上渗出。”')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return _('请先单击该日程解锁！')
            if player.canOutdoorSport < 0:
                return _('外面正在下雨。')
            if player.canSport < 0:
                return _('你受伤了，不能做激烈的运动。')
            if not player.onVacation and time < 2:
                return _('现在是正常上班时间！')
            return True

        @classmethod
        def unlockCond(cls, player):
            if player.physical < 1.1:
                return _('基础身体素质尚未达到要求，需要至少等于1.1')
            return True

        @classmethod
        def getRecoScale(cls, player):
            scale = 1.0
            scale *= player.basicRecovery
            scale *= player.phyReco()
            scale *= player.sportRecovery
            scale *= player.outdoorSportRecovery
            scale /= player.sev()
            scale = max(0.2, scale)
            return scale

        @classmethod
        def executeTask(cls, player):
            if BookRandConcEffect.has(player):
                renpy.call_screen(_screen_name="screen_BookRandConcEffect", player=player, adj=cls.getConcScale(player))
            perf = ra(player, 1, 100)
            perf += cls.getConcScale(player)
            #Notice.add('Perf: %s' % perf)
            while BookSportEffect.has(player) and perf <= 35:
                perf = ra(player, 1, 100)
            resultLabel = cls.getResultLabel(player, perf, c=35)
            player.updateAfterTask(cls)
            cls.afterTaskResult(player)
            renpy.jump(resultLabel)

        @classmethod
        def excePerf(cls, player):
            reco = r2(25 * cls.getRecoScale(player))
            g = 0.02 + player.physicalGain
            if rra(player, 50):
                g+= 0.01
            player.gain_mental(reco)
            player.gain_abi(g, 'phy')
            PhysRezB.add(player)

        @classmethod
        def goodPerf(cls, player):
            reco = r2(25 * cls.getRecoScale(player))
            g = 0.01 + player.physicalGain
            player.gain_mental(reco)
            player.gain_abi(g, 'phy')
            player.gain_abi(-0.01, 'sev')
            

        @classmethod
        def normPerf(cls, player):
            reco = r2(25 * cls.getRecoScale(player))
            exReco = r2(10 * cls.getRecoScale(player))
            g = 0.01 + player.physicalGain
            player.gain_abi(g, 'phy')
            player.gain_mental(reco)
            player.gain_mental(exReco, extra=True)

        @classmethod
        def badPerf(cls, player):
            player.gain_abi(0.01, 'sev')
            Injured.add(player)
            Notice.add(_('你在运动中受伤了，没有恢复精神状态。'))

        @classmethod
        def afterTaskResult(cls, player):

            if not Injured.has(player):
                if rra(player, 70):
                    PhysicalLimited.add(player)
                Soreness.add(player, 4)

                if rra(player, 75):
                    PhysRezB.add(player)
                if rra(player, 25):
                    PhysRezB.add(player)

                if rra(player, 33):
                    PhysRezB.add(player)
            if WeatherSmog.has(player):
                WeatherSmog.get(player).check(player)


    class GymSport(SportTask):
        id = 203
        name = _('去健身房健身')
        kind = _('运动类')
        unlocked = False
        info = _('基础恢复：15\n定制独特的健身日程自定义健身内容，基础专注度在健身日程中仅能发挥33%的作用。\n单日购卡需40元。\n\n解锁条件 1.2身体素质解锁。')
        ad = _('“这部机器，即我的身体，涌动着力量。”')

        @classmethod
        def checkAvailable(cls, player, day, time):
            cls.info = _('基础恢复：15\n定制健身日程自定义健身内容。\n单日购卡需%s元。\n\n解锁条件 1.2身体素质解锁。') % r2(0.4*player.price)
            if not cls.isUnlocked(player):
                return _('请先单击该日程解锁！')
            if player.canSport < 0:
                return _('你受伤了，不能做激烈的运动。')
            if not player.onVacation and time < 2:
                return _('现在是正常上班时间！')
            if Stayuplate.has(player):
                return _('非健身房营业时间。')
            if player.money < r2(0.4*player.price) and not GymTicket.has(player):
                return _('你的钱不够单日消费。')
            return True

        @classmethod
        def unlockCond(cls, player):
            if player.physical < 1.2:
                return _('基础身体素质尚未达到要求，需要至少等于1.2')
            return True

        @classmethod
        def executeTask(cls, player):
            if BookRandConcEffect.has(player):
                renpy.call_screen(_screen_name="screen_BookRandConcEffect", player=player, adj=cls.getConcScale(player))
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
            player.updateAfterTask(cls)

        @classmethod
        def excePerf(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            if GymLimited.has(player):
                g = 0.02
            else:
                g = 0.02 + player.physicalGain
            player.gain_mental(reco)
            player.gain_abi(g, 'phy')
            Soreness.add(player)
            PhysRezB.add(player)

        @classmethod
        def goodPerf(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            player.gain_mental(reco)
            player.gain_abi(-0.02, 'sev')
            Soreness.add(player)
            

        @classmethod
        def normPerf(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            exReco = r2(7.5 * cls.getRecoScale(player))
            player.gain_mental(reco)
            player.gain_mental(exReco, extra=True)
            PhysRezB.add(player)

        @classmethod
        def badPerf(cls, player):
            player.gain_abi(0.02, 'sev')

        @classmethod
        def afterTaskResult(cls, player):
            
            if not Injured.has(player):
                PhysicalLimited.add(player)
                Soreness.add(player, 2)
                PhysRezB.add(player, 2)
            if WeatherSmog.has(player):
                WeatherSmog.get(player).check(player)


    class BadmintonClass(SportTask):
        id = 204
        name = _('羽毛球课程')
        kind = _('运动类')
        unlocked = True
        info = _('基础恢复：15\n该日程不受专注度影响，不会在运动中受伤。')
        ad = _('上课是次要的……主要是为了……')

        @classmethod
        def hasplot(cls, player):
            if player.hal_p == 50:
                return True
            if player.hal_p == 11:
                return True
            if player.hal_p < 7:
                return True
            return False

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return _('请先单击该日程解锁！')
            if not player.onVacation and time < 2:
                return _('现在是正常上班时间！')
            if day == 6 and time == 1 and player.hal_p == 11:
                return True
            if player.canSport < 0:
                return _('你受伤了，不能做激烈的运动。')
            if not BadmintonRacket.has(player):
                return _('你还没有羽毛球拍，外出去商店街的文体商店里买一个！')
            if day == 6 and time == 1:
                return True
            return _('非课程时间段。')

        @classmethod
        def unlockCond(cls, player):
            return _('课程已结束！')

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
            player.gain_mental(reco)
            player.gain_abi(g, 'phy')
            player.gain_abi(-0.02, 'sev')
            PhysRezB.add(player)
            

        @classmethod
        def goodPerf(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            g = 0.02 + player.physicalGain
            player.gain_mental(reco)
            player.gain_abi(g, 'phy')
            player.gain_abi(-0.02, 'sev')
            

        @classmethod
        def normPerf(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            g = 0.01 + player.physicalGain
            player.gain_mental(reco)
            player.gain_abi(g, 'phy')
            player.gain_abi(-0.01, 'sev')
            

        @classmethod
        def badPerf(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            exReco = r2(5 * cls.getRecoScale(player))
            g = 0.02 + player.physicalGain
            player.gain_mental(reco)
            player.gain_mental(exReco, extra=True)
            player.gain_abi(g, 'phy')

        @classmethod
        def afterTaskResult(cls, player):
            PhysicalLimited.add(player)
            Soreness.add(player, 4)
            if rra(player, 75):
                PhysRezB.add(player)
            if rra(player, 25):
                PhysRezB.add(player)
            if WeatherSmog.has(player):
                WeatherSmog.get(player).check(player)


    class StretchingSport(SportTask):
        id = 205
        name = _('拉伸运动')
        kind = _('运动类')
        unlocked = True
        info = _('恢复根据酸痛层数的精神状态，将酸痛转化为体魄。')
        ad = _('扭动你的手腕和关节直到它们脱臼断裂。')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not player.onVacation and time < 2:
                return _('现在是正常上班时间！')
            if player.canSport < 0:
                return _('你受伤了，不能做激烈的运动。')
            return True

        @classmethod
        def executeTask(cls, player):
            Soreness.add(player)
            if BookRandConcEffect.has(player):
                renpy.call_screen(_screen_name="screen_BookRandConcEffect", player=player, adj=cls.getConcScale(player))
            perf = ra(player, 1, 100)
            perf += cls.getConcScale(player)
            #Notice.add('Perf: %s' % perf)
            resultLabel = cls.getResultLabel(player, perf)
            player.updateAfterTask(cls)
            cls.afterTaskResult(player)
            renpy.jump(resultLabel)

        @classmethod
        def excePerf(cls, player):
            stacks = Soreness.getstack(player)
            g = stacks * 0.15
            Physique.add(player, int(g))
            if rra(player, 100 * (g-int(g))):
                Physique.add(player)
            Soreness.clearByType(player)
            reco = r2(1 * stacks)
            player.gain_mental(reco)

        @classmethod
        def goodPerf(cls, player):
            stacks = Soreness.getstack(player)
            g = stacks * 0.13
            Physique.add(player, int(g))
            if rra(player, 100 * (g - int(g))):
                Physique.add(player)
            Soreness.clearByType(player)
            reco = r2(0.8 * stacks)
            player.gain_mental(reco)

        @classmethod
        def normPerf(cls, player):
            stacks = Soreness.getstack(player)
            g = stacks * 0.11
            Physique.add(player, int(g))
            if rra(player, 100 * (g - int(g))):
                Physique.add(player)
            Soreness.clearByType(player)
            reco = r2(0.7 * stacks)
            player.gain_mental(reco)

        @classmethod
        def badPerf(cls, player):
            stacks = Soreness.getstack(player)
            g = stacks * 0.1
            Physique.add(player, int(g))
            if rra(player, 100 * (g - int(g))):
                Physique.add(player)
            Soreness.clearByType(player)
            reco = r2(0.6 * stacks)
            player.gain_mental(reco)

        @classmethod
        def afterTaskResult(cls, player):
            PhysicalLimited.add(player)
            if rra(player, 50):
                PhysRezB.add(player)


    class DefaultRead(WriteTask):
        id = 300
        name = _('读流行小说')
        kind = _('写作类')
        unlocked = True
        info = _('基础恢复：12.5\n偏向于均衡发展的阅读。')
        ad = _('俗话说文人相轻，但偶尔我也是会看点当下流行的小说的……虽然我觉得大多都没我写的好，哼哼。')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not player.onVacation and time < 2:
                return _('现在是正常上班时间！')
            if Anxiety.has(player):
                return _('你由于十分担心自己能否有稳定经济来源而没有阅读的欲望。')
            if player.canRead < 0:
                return _('因为某种原因无法专心阅读。')
            return True

        @classmethod
        def excePerf(cls, player):
            reco = r2(12.5 * cls.getRecoScale(player))
            exReco = r2(12.5 * cls.getRecoScale(player))
            g = 0.03 + player.writingGain
            player.gain_mental(reco)
            player.gain_mental(exReco, extra=True)
            player.gain_abi(g, 'wri')
            ReadReward.add(player)
            Inspiration.add(player)

        @classmethod
        def goodPerf(cls, player):
            reco = r2(12.5 * cls.getRecoScale(player))
            exReco = r2(5 * cls.getRecoScale(player))
            player.gain_mental(reco)
            player.gain_mental(exReco, extra=True)
            player.gain_abi(-0.02, 'sev')
            Inspiration.add(player)
            Notice.add(_('降低了2点严重度。'))

        @classmethod
        def normPerf(cls, player):
            reco = r2(12.5 * cls.getRecoScale(player))
            exReco = r2(7.5 * cls.getRecoScale(player))
            g = 0.02 + player.writingGain
            player.gain_mental(reco)
            player.gain_mental(exReco, extra=True)
            player.gain_abi(g, 'wri')

        @classmethod
        def badPerf(cls, player):
            reco = r2(10 * cls.getRecoScale(player))
            exReco = r2(15 * cls.getRecoScale(player))
            player.gain_mental(reco)
            player.gain_mental(exReco, extra=True)
            player.gain_abi(-0.01, 'sev')
        
        @classmethod
        def afterTaskResult(cls, player):
            if rra(player, 50):
                ReadingLimited.add(player)
            Inspiration.add(player, 1)


    class SentimentalRead(WriteTask):
        id = 301
        name = _('读感伤文学')
        kind = _('写作类')
        unlocked = False
        info = _('基础恢复：15\n偏向获得灵感的阅读。\n\n解锁条件 1.1写作技巧解锁。')
        ad = _('“我的情绪远比平常更为高昂或低沉，但我也仍然无法完全理解这些文字。”')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return _('请先单击该日程解锁！')
            if not player.onVacation and time < 2:
                return _('现在是正常上班时间！')
            if Anxiety.has(player):
                return _('你由于十分担心自己能否有稳定经济来源而没有阅读的欲望。')
            if player.canRead < 0:
                return _('因为某种原因无法专心阅读。')
            return True

        @classmethod
        def unlockCond(cls, player):
            if player.writing < 1.1:
                return _('基础写作技巧尚未达到要求，需要至少等于1.1')
            return True

        @classmethod
        def excePerf(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            player.gain_mental(reco)
            player.gain_abi(-0.02, 'wri')
            ReadReward.add(player)
            Inspiration.add(player, 3)

        @classmethod
        def goodPerf(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            exReco = r2(5 * cls.getRecoScale(player))
            player.gain_mental(reco)
            player.gain_mental(exReco, extra=True)
            player.gain_abi(-0.01, 'sev')
            ReadReward.add(player)
            Inspiration.add(player, 1)
            Notice.add(_('降低了1点严重度。'))

        @classmethod
        def normPerf(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            player.gain_mental(reco)
            Inspiration.add(player, 1)

        @classmethod
        def badPerf(cls, player):
            cons = r2(20 * cls.getConsScale(player))
            player.gain_mental(-cons)
            player.gain_abi(-0.01, 'wri')

        @classmethod
        def afterTaskResult(cls, player):
            if rra(player, 70):
                ReadingLimited.add(player)
            Inspiration.add(player, 1)

    class TraditionalRead(WriteTask):
        id = 302
        name = _('读传统文学')
        kind = _('写作类')
        unlocked = False
        info = _('基础恢复：10\n偏向于提升写作技巧的阅读。\n\n解锁条件 1.1写作技巧解锁。')
        ad = _('“我的双眼如饥似渴地吸收着文字，仿佛影子吸收光线。”')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return _('请先单击该日程解锁！')
            if not player.onVacation and time < 2:
                return _('现在是正常上班时间！')
            if Anxiety.has(player):
                return _('你由于十分担心自己能否有稳定经济来源而没有阅读的欲望。')
            if player.canRead < 0:
                return _('因为某种原因无法专心阅读。')
            return True

        @classmethod
        def unlockCond(cls, player):
            if player.writing < 1.1:
                return _('基础写作技巧尚未达到要求，需要至少等于1.1')
            return True


        @classmethod
        def excePerf(cls, player):
            reco = r2(10 * cls.getRecoScale(player))
            g = 0.05 + player.writingGain
            player.gain_mental(reco)
            player.gain_abi(g, 'wri')
            player.gain_abi(-0.01, 'sev')
            ReadReward.add(player)
            Inspiration.add(player, 1)

        @classmethod
        def goodPerf(cls, player):
            reco = r2(10 * cls.getRecoScale(player))
            exReco = r2(5 * cls.getRecoScale(player))
            g = 0.03 + player.writingGain
            player.gain_mental(reco)
            player.gain_mental(exReco)
            player.gain_abi(g, 'wri')
            ReadReward.add(player)

        @classmethod
        def normPerf(cls, player):
            reco = r2(10 * cls.getRecoScale(player))
            g = 0.02 + player.writingGain
            player.gain_mental(reco)
            player.gain_abi(-0.02, 'sev')
            player.gain_abi(g, 'wri')
            Notice.add(_('降低了2点严重度。'))

        @classmethod
        def badPerf(cls, player):
            cons = r2(15 * cls.getConsScale(player))
            player.gain_mental(-cons)
            g = 0.01 + player.writingGain
            player.gain_abi(0.01, 'sev')
            Notice.add(_('升高了1点严重度。'))
            Notice.add(_('升高了%s点写作技巧。') % int(g * 100))
        
        @classmethod
        def afterTaskResult(cls, player):
            if rra(player, 70):
                ReadingLimited.add(player)


    class FreewheelingWriting(WriteTask):
        id = 303
        name = _('随笔写作')
        kind = _('写作类')
        unlocked = True
        info = _('基础恢复：25\n进行一次仅能用于获取粉丝的写作，消耗所有灵感和可转化的状态进行写作，根据状态的层数和种类获得额外的灵感。\n\n无需接取委托。\n\n{color=#fde827}可转化的状态：\n0层灵感：焦虑，勃起，写作欲\n1层灵感：紧迫，安逸，渴求，澎湃\n2层灵感：悲伤，恐惧，偏执{/color}')
        ad = _('发泄想法与灵感，积累人气，偶尔还能获得打赏，但我并非为金钱才踏上写作之路。')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not player.onVacation and time < 2:
                return _('现在是正常上班时间！')
            if time < 2:
                return _('你只有在晚上才会想写随笔。')
            if Anxiety.has(player):
                return _('你由于十分担心自己能否有稳定经济来源而没有写随笔的欲望。')
            if list(filter(lambda x: type(x) in (MentProb,MentPun,Erection,Sadness,Pleasure,Restlessness,Contentment,Dread,Desire,Agony), player.effects))==[]:
                return _('没有可以用于随笔的状态。')
            return True

        @classmethod
        def executeTask(cls, player):
            s = 0
            for i in (MentProb,Erection,Pleasure):
                if i.has(player):
                    i.get(player).clear(player)

            for i in (Restlessness,Contentment,Desire,Agony):
                if i.has(player):
                    s += i.get(player).stacks * 1
                    i.get(player).clear(player)
            
            for i in (Dread,Sadness,MentPun):
                if i.has(player):
                    s += i.get(player).stacks * 2
                    i.get(player).clear(player)
            
                    
            Inspiration.add(player, s)

            if BookRandConcEffect.has(player):
                renpy.call_screen(_screen_name="screen_BookRandConcEffect", player=player, adj=cls.getConcScale(player))

            perf = ra(player, 1, 100)
            perf += cls.getConcScale(player)
            #Notice.add('Perf: %s' % perf)
            resultLabel = cls.getResultLabel(player, perf)
            informalEssay = Comm(player)
            informalEssay.name = rca(player, comm_informal_names)
            if len(comm_informal_names) != 1:
                comm_informal_names.remove(informalEssay.name)
            informalEssay.freewheeling = True
            informalEssay.needWord = -1
            informalEssay.needInspiration = -1
            informalEssay.du = -1
            informalEssay.require = player.wri()
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
            s = 0.008 * player.week if player.week <= 7 else 0.064
            
            if SleepReward_.has(player):
                s *= 0.15 * SleepReward_.getstack(player)
            reco = r2(25 * cls.getRecoScale(player))
            player.gain_mental(reco)
            player.severity += r2(s)
            Notice.add(_('提升了%s点严重度。') % int(s*100))

        @classmethod
        def goodPerf(cls, player):
            reco = r2(25 * cls.getRecoScale(player))
            s = 0.01 * player.week if player.week <= 7 else 0.08
            if SleepReward_.has(player):
                s *= 0.15 * SleepReward_.getstack(player)
            player.gain_mental(reco)
            player.severity += r2(s)
            Notice.add(_('提升了%s点严重度。') % int(s*100))

        @classmethod
        def normPerf(cls, player):
            reco = r2(25 * cls.getRecoScale(player))
            exReco = r2(5 * cls.getRecoScale(player))
            s = 0.012 * player.week if player.week <= 7 else 0.096
            if SleepReward_.has(player):
                s *= 0.15 * SleepReward_.getstack(player)
            player.gain_mental(reco)
            player.gain_mental(exReco, extra=True)
            player.severity += r2(s)
            Notice.add(_('提升了%s点严重度。') % int(s*100))

        @classmethod
        def badPerf(cls, player):
            reco = r2(25 * cls.getRecoScale(player))
            player.gain_mental(reco)
            s = 0.02
            if SleepReward_.has(player):
                s *= 0.01
            player.severity += s
            Notice.add(_('提升了%s点严重度。' % int(s*100)))
        
    
        @classmethod
        def afterTaskResult(cls, player):
            if rra(player, 50):
                ReadingLimited.add(player)

    class NormalWriting(WriteTask):
        id = 304
        name = _('完成委托')
        kind = _('写作类')
        unlocked = True
        info = _('基础恢复：20\n消耗所有灵感完成写作委托。\n\n需要在手机上接取委托。')
        ad = _('赚点外快罢了，现在谁还没个两份工——')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not player.onVacation and time < 2:
                return _('现在是正常上班时间！')
            if player.canWrite < 0:
                return _('因为某种原因无法专心写作。')
            if Anxiety.has(player):
                return _('你由于十分担心自己能否有稳定经济来源而没有写委托的欲望。')
            if not UnfinishedCommission.has(player):
                return _('并没有接委托，请先接个委托吧。')
            return True

        @classmethod
        def executeTask(cls, player):
            if BookRandConcEffect.has(player):
                renpy.call_screen(_screen_name="screen_BookRandConcEffect", player=player, adj=cls.getConcScale(player))
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
            s = 0.01 * player.week if player.week <= 7 else 0.08
            
            if SleepReward_.has(player):
                s *= 0.15 * SleepReward_.getstack(player)
            reco = r2(20 * cls.getRecoScale(player))
            player.gain_mental(reco)
            player.severity += r2(s)
            Notice.add(_('提升了%s点严重度。') % r2(s))

        @classmethod
        def goodPerf(cls, player):
            reco = r2(20 * cls.getRecoScale(player))
            s = 0.012 * player.week if player.week <= 7 else 0.1
            if SleepReward_.has(player):
                s *= 0.15 * SleepReward_.getstack(player)
            player.gain_mental(reco)
            player.severity += r2(s)
            Notice.add(_('提升了%s点严重度。') % r2(s))

        @classmethod
        def normPerf(cls, player):
            reco = r2(20 * cls.getRecoScale(player))
            exReco = r2(5 * cls.getRecoScale(player))
            s = 0.015 * player.week if player.week <= 7 else 0.12
            if SleepReward_.has(player):
                s *= 0.15 * SleepReward_.getstack(player)
            player.gain_mental(reco)
            player.gain_mental(exReco, extra=True)
            player.severity += r2(s)
            Notice.add(_('提升了%s点严重度。') % r2(s))

        @classmethod
        def badPerf(cls, player):
            reco = r2(25 * cls.getRecoScale(player))
            player.gain_mental(reco)
            s = 0.02
            if SleepReward_.has(player):
                s *= 0.01
            player.severity += s
            Notice.add(_('提升了%s点严重度。' % int(s*100)))

        @classmethod
        def afterTaskResult(cls, player):
            if rra(player, 50):
                ReadingLimited.add(player)

    class ExactWriting(WriteTask):
        id = 305
        name = _('精准写作')
        kind = _('写作类')
        unlocked = False
        info = _('基础恢复：10\n只消耗委托要求的灵感和字数完成写作委托，如果完成委托的字数低于需求，至多提升额外50%的字数并消耗精神状态。\n\n需要在手机上接取委托。\n\n解锁条件 1.1写作技巧解锁。')
        ad = _('赚点外快罢了，现在谁还没个两份工——')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return _('请先单击该日程解锁！')
            if not player.onVacation and time < 2:
                return _('现在是正常上班时间！')
            if player.canWrite < 0:
                return _('因为某种原因无法专心写作。')
            if Stayuplate.has(player):
                return _('你无法在熬夜时集中太多的精力。')
            if Anxiety.has(player):
                return _('你由于十分担心自己能否有稳定经济来源而没有写委托的欲望。')
            if not UnfinishedCommission.has(player):
                return _('并没有接委托，请先接个委托吧。')
            return True

        @classmethod
        def unlockCond(cls, player):
            if player.writing < 1.1:
                return _('基础写作技巧尚未达到要求，需要至少等于1.1')
            return True

        @classmethod
        def executeTask(cls, player):
            if BookRandConcEffect.has(player):
                renpy.call_screen(_screen_name="screen_BookRandConcEffect", player=player, adj=cls.getConcScale(player))
            perf = ra(player, 1, 100)
            perf += cls.getConcScale(player)
            #Notice.add('Perf: %s' % perf)
            resultLabel = cls.getResultLabel(player, perf)
            unf = player.retval
            unf.write(player, True)

            cls.afterTaskResult(player)
            player.updateAfterTask(cls)
            renpy.jump(resultLabel)

        @classmethod
        def excePerf(cls, player):
            s = 0.01 * player.week if player.week <= 7 else 0.08
            
            if SleepReward_.has(player):
                s *= 0.15 * SleepReward_.getstack(player)
            reco = r2(20 * cls.getRecoScale(player))
            player.gain_mental(reco)
            player.severity += r2(s)
            Notice.add(_('提升了%s点严重度。') % r2(s))

        @classmethod
        def goodPerf(cls, player):
            reco = r2(20 * cls.getRecoScale(player))
            s = 0.012 * player.week if player.week <= 7 else 0.1
            if SleepReward_.has(player):
                s *= 0.15 * SleepReward_.getstack(player)
            player.gain_mental(reco)
            player.severity += r2(s)
            Notice.add(_('提升了%s点严重度。') % r2(s))

        @classmethod
        def normPerf(cls, player):
            reco = r2(20 * cls.getRecoScale(player))
            exReco = r2(5 * cls.getRecoScale(player))
            s = 0.015 * player.week if player.week <= 7 else 0.12
            if SleepReward_.has(player):
                s *= 0.15 * SleepReward_.getstack(player)
            player.gain_mental(reco)
            player.gain_mental(exReco, extra=True)
            player.severity += r2(s)
            Notice.add(_('提升了%s点严重度。') % r2(s))

        @classmethod
        def badPerf(cls, player):
            reco = r2(25 * cls.getRecoScale(player))
            player.gain_mental(reco)
            s = 0.02
            if SleepReward_.has(player):
                s *= 0.01
            player.severity += s
            Notice.add(_('提升了%s点严重度。' % int(s*100)))

        @classmethod
        def afterTaskResult(cls, player):
            if rra(player, 50):
                ReadingLimited.add(player)

    class FocusWriting(WriteTask):
        id = 306
        name = _('集中写作')
        kind = _('写作类')
        unlocked = False
        info = _('基础消耗：20\n使这次写作中的写作技巧暂时提升。\n\n需要在手机上接取委托。\n\n解锁条件 1.2写作技巧解锁。')
        ad = _('也许我不该把写作看作放松行为，而应该是一种严肃的脑力工作。')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return _('请先单击该日程解锁！')
            if not player.onVacation and time < 2:
                return _('现在是正常上班时间！')
            if Stayuplate.has(player):
                return _('你无法在熬夜时集中太多的精力。')
            if player.canWrite < 0:
                return _('因为某种原因无法专心写作。')
            if not UnfinishedCommission.has(player):
                return _('并没有接委托，请先接个委托吧。')
            return True

        @classmethod
        def unlockCond(cls, player):
            if player.writing < 1.2:
                return _('基础写作技巧尚未达到要求，需要至少等于1.2')
            return True


        @classmethod
        def executeTask(cls, player):
            if BookRandConcEffect.has(player):
                renpy.call_screen(_screen_name="screen_BookRandConcEffect", player=player, adj=cls.getConcScale(player))
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
            player.gain_abi(0.01, 'wri', extra=True)
            renpy.jump(resultLabel)

        @classmethod
        def excePerf(cls, player):
            
            s = 0.012 * player.week if player.week <= 7 else 0.096
            if SleepReward_.has(player):
                s *= 0.15 * SleepReward_.getstack(player)
            reco = r2(15 * cls.getRecoScale(player))
            player.gain_mental(reco)
            player.severity += r2(s)
            Notice.add(_('提升了%s点严重度。') % r2(s))

        @classmethod
        def goodPerf(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            s = 0.014 * player.week if player.week <= 7 else 0.112
            if SleepReward_.has(player):
                s *= 0.15 * SleepReward_.getstack(player)
            player.gain_mental(reco)
            player.severity += r2(s)
            Notice.add(_('提升了%s点严重度。') % r2(s))

        @classmethod
        def normPerf(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            exReco = r2(5 * cls.getRecoScale(player))
            s = 0.018 * player.week if player.week <= 7 else 0.146
            if SleepReward_.has(player):
                s *= 0.15 * SleepReward_.getstack(player)
            player.gain_mental(reco)
            player.gain_mental(exReco, extra=True)
            player.severity += r2(s)
            Notice.add(_('提升了%s点严重度。') % r2(s))

        @classmethod
        def badPerf(cls, player):
            reco = r2(25 * cls.getRecoScale(player))
            player.gain_mental(reco)
            s = 0.02
            if SleepReward_.has(player):
                s *= 0.01
            player.severity += s
            Notice.add(_('提升了%s点严重度。' % int(s*100)))

        @classmethod
        def afterTaskResult(cls, player):
            if rra(player, 80):
                ReadingLimited.add(player)

    class ReadingBook(WriteTask):
        id = 397
        name = _('阅读书籍')
        kind = _('写作类')
        unlocked = True
        info = _('基础恢复：15\n选择书籍进行完整的阅读，或选择两本书籍各阅读一半的进度，没有书籍无法进行该日程。')
        ad = _('“书籍是不死的记忆。”')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not player.onVacation and time < 2:
                return _('现在是正常上班时间！')
            if list(filter(lambda x: x.kind in ('书籍', '专业类书籍') and type(x).__name__ not in player.itemcd, player.items)) == []:
                return _('你暂时并没有可以读的书籍。')
            if player.canRead < 0:
                return _('因为某种原因无法专心阅读。')
            return True
        
        @classmethod
        def executeTask(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            player.gain_mental(reco)
            resultLabel = cls.getResultLabel(player, rd(1,100))
            player.updateAfterTask(cls)
            cls.afterTaskResult(player)
            for book, allo in player.retval:
                book.readBook(player, allo)

            renpy.jump(resultLabel)

        @classmethod
        def afterTaskResult(cls, player):
            ReadingLimited.add(player)

    class WriteDownInspiration(WriteTask):
        id = 398
        name = _('记录想法')
        kind = _('写作类')
        unlocked = True
        info = _('将灵感转化为写作素材，基于转化的灵感获得少量精神状态。')
        ad = _('“回首某个瞬间。下个瞬间即告消逝。”')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not player.onVacation and time < 2:
                return _('现在是正常上班时间！')
            if player.canWrite < 0:
                return _('因为某种原因无法专心写作。')
            return True

        @classmethod
        def executeTask(cls, player):
            Inspiration.add(player)
            if BookRandConcEffect.has(player):
                renpy.call_screen(_screen_name="screen_BookRandConcEffect", player=player, adj=cls.getConcScale(player))
            perf = ra(player, 1, 100)
            perf += cls.getConcScale(player)
            #Notice.add('Perf: %s' % perf)
            resultLabel = cls.getResultLabel(player, perf)
            player.updateAfterTask(cls)
            renpy.jump(resultLabel)

        @classmethod
        def excePerf(cls, player):
            stacks = Inspiration.getstack(player)
            g = stacks * 0.9
            FixedInspiration.add(player, int(g))
            if rra(player, 100 * (g-int(g))):
                FixedInspiration.add(player)
            Inspiration.clearByType(player)
            reco = r2(1.8 * stacks)
            player.gain_mental(reco)

        @classmethod
        def goodPerf(cls, player):
            stacks = Inspiration.getstack(player)
            g = stacks * 0.85
            FixedInspiration.add(player, int(g))
            if rra(player, 100 * (g - int(g))):
                FixedInspiration.add(player)
            Inspiration.clearByType(player)
            reco = r2(1.7 * stacks)
            player.gain_mental(reco)

        @classmethod
        def normPerf(cls, player):
            stacks = Inspiration.getstack(player)
            g = stacks * 0.8
            FixedInspiration.add(player, int(g))
            if rra(player, 100 * (g - int(g))):
                FixedInspiration.add(player)
            Inspiration.clearByType(player)
            reco = r2(1.6 * stacks)
            player.gain_mental(reco)

        @classmethod
        def badPerf(cls, player):
            stacks = Inspiration.getstack(player)
            g = stacks * 0.65
            FixedInspiration.add(player, int(g))
            if rra(player, 100 * (g - int(g))):
                FixedInspiration.add(player)
            Inspiration.clearByType(player)
            reco = r2(1.3 * stacks)
            player.gain_mental(reco)

        @classmethod
        def afterTaskResult(cls, player):
            ReadingLimited.add(player)

    class SpecialWriting(WriteTask):
        id = 399
        name = _('撰写小说')
        kind = _('写作类')
        unlocked = True
        info = _('基础消耗：40\n消耗回忆片段来提升小说的进度，只能记录一个人的故事。\n该日程不受专注度影响。')
        ad = _('在这个世界上留下一点东西……')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if player.experience!='wri':
                return _('出身必须为全职小说家。')
            if not WriterItem1.has(player):
                return _('没有可以写的小说原稿。')
            if not WriterItem3.has(player) and WriterItem1.get(player).route == 'Halluke':
                return _('没有可用的回忆片段。')
            if not WriterItem4.has(player) and WriterItem1.get(player).route == 'Depline':
                return _('没有可用的回忆片段。')
            if not WriterItem3.has(player) and not WriterItem4.has(player) and not WriterItem1.get(player).route:
                return _('没有可用的回忆片段。')
            if player.canWrite < 0:
                return _('因为某种原因无法专心写作。')
            return True

        @classmethod
        def afterTaskResult(cls, player):
            ReadingLimited.add(player)

        @classmethod
        def executeTask(cls, player):
            WriterItem1.get(player).work(player)
            cls.afterTaskResult(player)
            player.updateAfterTask(cls)
            WriterBuff.add(player)
            renpy.jump("SpecialWriting_result")



    class Sleep(RestTask):
        id = 400
        name = _('在床上休息')
        kind = _('休息类')
        unlocked = True
        info = _('基础恢复：30\n转化睡意为精神专注，有一定概率治疗受伤和生病，获得良好的睡眠。')
        ad = _('床是最小单位的诺亚方舟。')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not player.onVacation and time < 2:
                return _('现在是正常上班时间！')
            if Stayuplate.has(player):
                return _('你不能熬夜睡觉。')
            if CafeBuff.has(player) or BookstoreBuff.has(player):
                return '你需要在一个有床的地方睡觉。'
            return True

        @classmethod
        def getRecoScale(cls, player):
            scale = 1.0
            scale *= player.basicRecovery
            scale *= player.sleepRecovery
            scale *= player.phyReco()
            scale /= player.sev()
            scale = max(0.2, scale)
            return scale

        @classmethod
        def executeTask(cls, player):
            if Tired.has(player):
                Tired.clearByType(player)
            if BookRandConcEffect.has(player):
                renpy.call_screen(_screen_name="screen_BookRandConcEffect", player=player, adj=cls.getConcScale(player))
            perf = ra(player, 1, 100)
            perf += cls.getConcScale(player)
            #Notice.add('Perf: %s' % perf)
            resultLabel = cls.getResultLabel(player, perf)

            PhysRezA.add(player)
            if rra(player, 50 * 1 if perf < 50 else 2):
                PhysRezA.add(player, 1 if rra(player, 50) else 2)

            stacks = 0

            if ConcDec.has(player):
                stacks = ConcDec.getstack(player)
                player.gain_mental(2.5 * stacks)
                ConcDec.clearByType(player)

            

            if PhysPun.has(player):
                PhysPun.get(player).cureBySleep(player)
            elif Injured.has(player):
                Injured.get(player).cureBySleep(player)

            player.updateAfterTask(cls)
            cls.afterTaskResult(player)

            if stacks != 0:
                if player.experience == 'wri' and not SleepReward_.has(player):
                    SleepReward_.add(player, stacks)
                else:
                    SleepReward.add(player, stacks)

            if rra(player, 33):  
                Relaxation.add(player)

            Stomachache.clearByType(player)
            Headache.clearByType(player)

            if not p.acosexdream and HotelBuff.has(player) and p.aco_p >= 2:
                renpy.jump("dream_acolas")
            if not player.s6 and player.today in (6, 7) and player.week >= 2 and not HotelBuff.has(player):
                if Inspiration.has(player):
                    if Inspiration.getstack(player) >= 5:
                        renpy.jump("solitus_route_6")
            if not player.s9 and Erection.has(player) and player.week >= 2 and not HotelBuff.has(player):
                renpy.jump("solitus_route_9")
            renpy.jump(resultLabel)


        @classmethod
        def excePerf(cls, player):
            reco = r2(30 * cls.getRecoScale(player))
            exReco = r2(5 * cls.getRecoScale(player))
            g = 0.01 + player.physicalGain
            player.gain_mental(reco)
            player.gain_mental(exReco, extra=True)
            player.gain_abi(g, 'phy')

        @classmethod
        def goodPerf(cls, player):
            reco = r2(30 * cls.getRecoScale(player))
            exReco = r2(10 * cls.getRecoScale(player))
            player.gain_mental(reco)
            player.gain_mental(exReco, extra=True)
            player.gain_abi(-0.01, 'sev')
            

        @classmethod
        def normPerf(cls, player):
            reco = r2(25 * cls.getRecoScale(player))
            player.gain_mental(reco)
            player.gain_abi(-0.01, 'sev')
            

        @classmethod
        def badPerf(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            exReco = r2(15 * cls.getRecoScale(player))
            player.gain_mental(reco)
            player.gain_mental(exReco, extra=True)


    class ComputerGaming(RestTask):
        id = 401
        name = _('打游戏')
        kind = _('休息类')
        unlocked = True
        info = _('基础消耗：10\n减少1~4天过劳或焦虑的持续时间，有大概率恢复精神状态。')
        ad = _('玩玩单机或者网络游戏解压。')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not player.onVacation and time < 2:
                return _('现在是正常上班时间！')
            if HotelBuff.has(player) or CafeBuff.has(player) or BookstoreBuff.has(player):
                return _('你现在并不在家。')
            return True

        @classmethod
        def excePerf(cls, player):
            reco = r2(10 * cls.getConsScale(player))
            exReco = r2(20 * cls.getRecoScale(player))
            player.gain_mental(-reco)
            player.gain_mental(exReco, extra=True)

        @classmethod
        def goodPerf(cls, player):
            reco = r2(10 * cls.getConsScale(player))
            exReco = r2(7.5 * cls.getRecoScale(player))
            player.gain_mental(-reco)
            player.gain_mental(exReco, extra=True)
            player.gain_abi(0.01, 'sev')

        @classmethod
        def normPerf(cls, player):
            reco = r2(10 * cls.getConsScale(player))
            exReco = r2(5 * cls.getRecoScale(player))
            player.gain_mental(-reco)
            player.gain_mental(exReco, extra=True)
            player.gain_abi(0.02, 'sev')
            

        @classmethod
        def badPerf(cls, player):
            cons = r2(10 * cls.getConsScale(player))
            player.gain_mental(-cons)

        @classmethod
        def afterTaskResult(cls, player):

            if PhysProb.has(player):
                PhysProb.get(player).timeUpdate(player, ra(player, 1, 4))
            
            if MentProb.has(player):
                MentProb.get(player).timeUpdate(player, ra(player, 1, 4))


    class CleanRoom(RestTask):
        id = 402
        name = _('打扫房间')
        kind = _('休息类')
        unlocked = True
        info = _('基础恢复：15\n获得整洁的房间。如果未过劳还会移除焦虑，如果过劳则增加恢复的精神状态。')
        ad = _('收拾收拾屋子吧，瞅你那房间乱得像猪窝一样。')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if HotelBuff.has(player) or CafeBuff.has(player) or BookstoreBuff.has(player):
                return _('你现在并不在家。')
            if CleanReward.has(player):
                return _('你的房间很干净，无需打扫。')
            if not player.onVacation and time < 2:
                return _('现在是正常上班时间！')
            return True

        @classmethod
        def executeTask(cls, player):
            if PhysProb.has(player):
                reco = r2(25 * cls.getRecoScale(player))
            else:
                reco = r2(15 * cls.getRecoScale(player))
            player.gain_mental(reco)
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
        name = _('上莓博')
        kind = _('休息类')
        unlocked = False
        info = _('基础恢复：15\n该日程不受专注度影响。')
        ad = _('刷刷莓博看看有什么有趣的东西。')
       
        @classmethod
        def unlockCond(cls, player):
            return _('日程将根据剧情解锁。')

        @classmethod
        def hasplot(cls, player):
            if p.dep_p == 0:
                return True
            return False

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return _('请先单击该日程解锁！')
            if not player.onVacation and time < 2:
                return _('现在是正常上班时间！')
            return True

        @classmethod
        def executeTask(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            player.gain_mental(reco)
            player.updateAfterTask(cls)
            cls.afterTaskResult(player)
            

        @classmethod
        def afterTaskResult(cls, player):
            pass


    class DoNothing(RestTask):
        id = 404
        name = _('发呆')
        kind = _('休息类')
        unlocked = True
        info = _('基础恢复：0\n什么也不做，跳过一回合。')
        ad = _('要问这个日程意义何在，那就要去问问名为额叶损管的人了。')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not player.onVacation and time < 2:
                return _('现在是正常上班时间！')
            return True

        @classmethod
        def executeTask(cls, player):
            player.updateAfterTask(cls)
            cls.afterTaskResult(player)
            renpy.jump("DoNothing_result")

        @classmethod
        def afterTaskResult(cls, player):
            pass


    class GoOutside(Task):
        id = 598
        name = _('外出')
        kind = _('特殊类')
        unlocked = True
        info = _('去医院购买药物或者去一些其他的地方。')
        ad = _('“一切事物皆有其所在之处，如此物位于此处。”')

        @classmethod
        def hasplot(cls, player):
            if p.sol_p == 0 and p.week >=4 and p.today == 5:
                return True
            elif p.sol_p == 2 and p.week >=8 and p.today == 5:
                return True
            elif p.sol_p == 4 and p.week >=12 and p.today == 5:
                return True
            elif player.aco_p == 7 and p.today in (6, 7):
                return True
            elif player.dep_p in (3, 4, 5, 6, 7) and p.today == 7:
                return True
            return False

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not player.onVacation and time < 2:
                return _('现在是正常上班时间！')
            if Tired.has(player):
                return _('你太累了。')
            if player.canExplore < 0:
                return _('外面正在刮台风。')
            if Stayuplate.has(player):
                return _('在深夜出门并不明智……')
            return True

        @classmethod
        def executeTask(cls, player):
            pass

        @classmethod
        def afterTaskResult(cls, player):
            pass

    class GoFishing(Task):
        id = 599
        name = _('去森林公园钓鱼')
        kind = _('特殊类')
        unlocked = False
        info = _('去森林公园钓鱼。\n\n该版本开放此日程以供测试，可以在工具店购买鱼竿后进行日程。')
        ad = _('每个游戏的经典标配。')

        @classmethod
        def unlockCond(cls, player):
            return _('日程将根据剧情解锁。')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not any([x.has(player) for x in (FishingRod1,FishingRod2, FishingRod3, FishingRod4,FishingRod99)]):
                return _('你需要有一个鱼竿才能去钓鱼，商店街的工具店会出售鱼竿。')
            if not player.onVacation and time < 2:
                return _('现在是正常上班时间！')
            if time >= 2:
                return _('现在已经没有去那边的公交车了。')
            if Tired.has(player):
                return _('你太累了。')
            if player.canExplore < 0:
                return _('外面正在刮台风。')
            return True

        @classmethod
        def executeTask(cls, player):
            pass

        @classmethod
        def afterTaskResult(cls, player):
            pass

    class HallukeTask1(Task):
        id = 500
        name = _('和Halluke打羽毛球')
        kind = _('特殊类')
        unlocked = False
        info = _('基础恢复：15\n获得1层良好的运动和精神的平复。\n该日程不受专注度影响。')
        ad = _('某种意义上的约会。')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return _('日程将根据剧情解锁。')
            if player.canSport < 0:
                return _('你受伤了，不能做激烈的运动。')
            if not BadmintonRacket.has(player):
                return _('你还没有羽毛球拍，外出去商店街的文体商店里买一个！')
            if player.hal_p in (12, 13) and time >= 2:
                return True
            if day == 7 and time == 1:
                return True
            return _('非约定时间')

        @classmethod
        def hasplot(cls, player):
            if player.hal_p in (7, 8, 9):
                return True
            return False

        @classmethod
        def unlockCond(cls, player):
            if player.hal_p == 99:
                return _('{color=#ff0000}需要Halluke活着。{/color}')
            return _('日程将根据剧情解锁。')

        @classmethod
        def executeTask(cls, player):
            reco = r2(15 * cls.getRecoScale(player))
            player.gain_mental(reco)
            PhysRezB.add(player)
            MentRezB.add(player)
            player.updateAfterTask(cls)
            renpy.jump("HallukeTask1_result")

    class HallukeTask2(Task):
        id = 501
        name = _('去Halluke家')
        kind = _('特殊类')
        unlocked = False
        info = _('该日程不受专注度影响。')
        ad = _('你们已经是恋人关系了，找他聊聊天？或者做些什么？')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return _('日程将根据剧情解锁。')
            if day == 6 and time == 1:
                return True
            return _('非约定时间')

        @classmethod
        def hasplot(cls, player):
            if player.hal_p == 12:
                return True
            return False

        @classmethod
        def unlockCond(cls, player):
            if player.hal_p == 99:
                return _('{color=#ff0000}需要Halluke活着。{/color}')
            return _('日程将根据剧情解锁。')

        @classmethod
        def executeTask(cls, player):
            player.updateAfterTask(cls)
            player.hal_noreply = 0
            renpy.jump("HallukeTask2_result")


    class AcolasTask1(Task):
        id = 510
        name = _('完成Acolas的项目')
        kind = _('特殊类')
        unlocked = False
        info = _('基础消耗：100\n完成进度，获得3层过劳，提升5点严重程度。\n该日程不受专注度影响。')
        ad = _('这应该不是什么难事……对吧？')
        
        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return _('日程将根据剧情解锁。')
            if not player.onVacation and time < 2:
                return _('现在是正常上班时间！')
            if not any([x.has(player) for x in (AcolasItem2, AcolasItem3, AcolasItem4)]):
                return _('你没有可以完成的项目')
            if HotelBuff.has(player) or CafeBuff.has(player) or BookstoreBuff.has(player):
                return _('你没有带项目……它在家里。')
            return True

        @classmethod
        def hasplot(cls, player):
            if player.aco_p == 8 and player.today == 4:
                return True
            return False

        @classmethod
        def unlockCond(cls, player):
            if player.aco_p == 99:
                return _('{color=#ff0000}需要Acolas活着。{/color}')
            return _('日程将根据剧情解锁。')

        @classmethod
        def executeTask(cls, player):
            for i in (AcolasItem2, AcolasItem3, AcolasItem4):
                if i.has(player):
                    script = i.get(player)
            script.work(player)

            

    class AcolasTask2(Task):
        id = 511
        name = _('去Acolas家')
        kind = _('特殊类')
        unlocked = False
        info = _('该日程不受专注度影响。')
        ad = _('听说他生病了，去探望他一下吧？\n切记，不要做蠢事。')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return _('日程将根据剧情解锁。')
            if day == 6 and time == 1:
                return True
            return _('非约定时间')

        @classmethod
        def hasplot(cls, player):
            if player.aco_p == 8:
                return True
            return False

        @classmethod
        def unlockCond(cls, player):
            if player.aco_p == 99:
                return _('{color=#ff0000}需要Acolas活着。{/color}')
            return _('日程将根据剧情解锁。')

        @classmethod
        def executeTask(cls, player):
            reco = r2(20 * cls.getRecoScale(player))
            player.gain_mental(reco)
            player.updateAfterTask(cls)
            renpy.jump("AcolasTask2_result")
    
    class DeplineTask1(Task):
        id = 511
        name = _('和赤松面基')
        kind = _('特殊类')
        unlocked = False
        info = _('该日程不受专注度影响。')
        ad = _('赤松把地点定在了商场，我真的要去参加么……')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return _('日程将根据剧情解锁。')
            if day == 7 and time == 0:
                return True
            return _('非约定时间')

        @classmethod
        def hasplot(cls, player):
            if player.dep_p == 2:
                return True
            return False

        @classmethod
        def unlockCond(cls, player):
            if player.dep_p == 99:
                return _('{color=#ff0000}需要Depline活着。{/color}')
            return _('日程将根据剧情解锁。')

        @classmethod
        def executeTask(cls, player):
            reco = r2(20 * cls.getRecoScale(player))
            player.gain_mental(reco)
            player.updateAfterTask(cls)

    class DestotTask1(Task):
        id = 630
        name = _('和Destot外出')
        kind = _('特殊类')
        unlocked = False
        info = _('该日程不受专注度影响。')
        ad = _('不知道他想带我吃什么，不过我最好留着肚子吃东西。')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return _('日程将根据剧情解锁。')
            if day == 7 and time == 2:
                return True
            return _('非约定时间')

        @classmethod
        def hasplot(cls, player):
            if player.des_p==2:
                return True
            return False

        @classmethod
        def unlockCond(cls, player):
            return _('日程将根据剧情解锁。')

        @classmethod
        def executeTask(cls, player):
            reco = r2(20 * cls.getRecoScale(player))
            player.gain_mental(reco)
            player.updateAfterTask(cls)
            renpy.jump("DestotTask1_result")

    class DestotTask2(Task):
        id = 631
        name = _('去Destot家')
        kind = _('特殊类')
        unlocked = False
        info = _('该日程不受专注度影响。')
        ad = _('不知道为什么，我总觉得不应该去。')

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not cls.isUnlocked(player):
                return _('日程将根据剧情解锁。')
            if day == 7 and time == 1:
                return True
            return _('非约定时间')

        @classmethod
        def hasplot(cls, player):
            if player.des_p==4:
                return True
            return False

        @classmethod
        def unlockCond(cls, player):
            return _('日程将根据剧情解锁。')

        @classmethod
        def executeTask(cls, player):
            reco = r2(10 * cls.getRecoScale(player))
            player.gain_mental(reco)
            player.updateAfterTask(cls)
            renpy.jump("DestotTask2_result")