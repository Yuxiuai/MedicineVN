init python early:

    class Player:
        def __init__(self, name='Solitus'):
            self.name = name
            self.seed = rd(-1000000, 1000000)
            self.safe = 0.0
            self.route = None
            self.p2 = None

            self.mental = 80.0
            self.severity = 1.0

            self.physical = 1.0
            self.working = 1.0
            self.writing = 1.0

            self.money = 2000.0
            self.price = 200.0
            self.priceIncrease = 10
            self.wages = 2000.0
            self.goal = 7.5
            self.achievedGoal = 0.0
            self.popularity = 1000

            self.mon = 4
            self.day = 29
            self.week = 0
            self.today = 5
            self.times = 2
            self.spec_hour = '15'
            self.spec_min = '54'

            self.hal_p = 0
            self.dep_p = 0
            self.aco_p = 0
            self.sol_p = 0

            self.s4 = False
            self.s5 = False
            self.s6 = False
            self.s7 = False
            self.s8 = False
            self.s9 = False

            self.onVacation = True
            self.onOutside = True

            self.cured = -1

            # basic- 基础提升，默认为1.0
            self.basicConsumption = 1.0
            self.basicRecovery = 1.0
            self.basicConcentration = 0  # 基础专注度

            self.physicalGain = 0
            self.workingGain = 0
            self.writingGain = 0

            self.physicalRegarded = 1.0
            self.workingRegarded = 1.0
            self.writingRegarded = 1.0
            self.severityRegarded = 1.0

            self.foodRecovery = 1.0  # 所有食物恢复效果
            self.drugRecovery = 1.0  # 所有药物恢复效果
            self.deteriorateConsumption = 1.0  # 睡眠消耗的

            self.outdoorSportRecovery = 1.0  # 外出跑步恢复率
            self.canOutdoorSport = 0  # 能否室外跑步 >1可以
            self.canWrite = 0  # 能否完成委托
            self.canRead = 0  # 能否读小说
            self.canSport = 0  # 能否运动类
            self.canExplore = 0  # 能否外出

            self.sportConsumption = 1.0 # 运动消耗率
            self.sportRecovery = 1.0  # 运动恢复率
            self.sportConcentration = 0  # 运动专注度

            self.writeConsumption = 1.0  # 写作消耗率
            self.writeRecovery = 1.0  # 写作恢复率
            self.writeConcentration = 0  # 写作专注度

            self.workConsumption = 1.0  # 写作消耗率
            self.workRecovery = 1.0  # 写作恢复率
            self.workConcentration = 0  # 写作专注度
            
            self.homeConsumption = 1.0  # 家中消耗率
            self.homeConcentration = 0  # 家中专注度

            self.sleepRecovery = 1.0  # 休息恢复率

            self.writeValuable = 1.0  # 写作价值率
            self.workSpeed = 1.0  # 工作进度提升
            self.foodPrice = 1.0  # 外卖价格修正

            self.fooduse = 0

            self.savetime = None

            self.effects = []
            self.items = []
            
            self.unlockedTasks = set()
            self.lockedTasks = set()
            self.starItems = []
            self.plan = [NoTask, NoTask, NoTask]
            self.plancheck = [False, False, False]
            self.gymplan = [NoSport, NoSport, NoSport]
            
            
            #self.medinfo = {MedicineA: MedInfo(MedicineA)}
            self.medinfo = {}

            self.itemcd = {}

            self.unacComm = []

            self.retval = None
            self.retval1 = None

            self.hadAskedForMoney = False
            self.hadAskedForLeave = False
            self.finalStageDays = -1
            self.color = 1.0

            self.aggra = 0
            self.messages = {'Pathos':[], 'Halluke':[], 'Acolas':[], 'Depline':[]}
            self.LocalStatistics = {}

            self.visitedStore = set()
            self.version = config.version

            self.difficultylocked = False

            self.nousemed = 0
            self.playtime = 0
            self.restart = 0
            self.note = None
            
            self.staylate = False
            self.cheat = False
            self.hatcolor = 0

        def __eq__(self, other):
            return id(other) == id(self)

        def rtn(self, retval):
            self.retval = retval
            
        def rtn1(self, retval):
            self.retval1 = retval
        

        def refreshUnacComm(self):
            self.unacComm = [Comm(self), Comm(self)]
            perc = self.popularity / 100
            for i in range(8):
                if rra(self, perc):
                    self.unacComm.append(Comm(self))

        def receiveComm(self, comm):
            unc = UnfinishedCommission(p)
            unc.comm = comm
            self.items.append(unc)
            showNotice([_('已接取新委托：%s') % comm.name])
            self.unacComm.remove(comm)


        def findNoTask(self):
            for i in range(3):
                if self.plan[i] == NoTask:
                    return i
            return 2

        def setTask(self, task):
            if self.findNoTask() != -1:
                self.plan[self.findNoTask()] = task
                    
        def removeTask(self, ind):
            self.plan[ind] = NoTask

        def morning_checkTask(self):
            self.plancheck = [False, False, False]
            self.checkTask()
            if AcolasItem4.has(self) and not config.developer and self.cured < 0:
                self.plan = [AcolasTask1, AcolasTask1, AcolasTask1]
            if p.hal_p == 50 and p.today == 6 and self.cured < 0:
                self.plan[1] = BadmintonClass

        def checkTask(self):
            for i in range(3):
                if self.plan[i] != NoTask:
                    if self.plan[i].checkAvailable(self, self.today, i)!=True and self.plancheck[i] == False:
                        if self.times != 2:
                            Notice.add(_('因为一些原因划去了计划上的日程：%s……') % self.plan[i].name)
                        self.plan[i] = NoTask
            if self.times != 2:
                Notice.show()

        def findNoSport(self):
            for i in range(3):
                if self.gymplan[i] == NoSport:
                    return i
            return 2

        def setgymtask(self, gymtask):
            if self.findNoSport() != -1:
                self.gymplan[self.findNoSport()] = gymtask
                    
        def removegymtask(self, ind):
            self.gymplan[ind] = NoSport

        def checkgymtask(self):
            for i in range(3):
                if self.gymplan[i].checkAvailable(self, self.today, i)!=True:
                    self.gymplan[i] = NoSport

            
            
        def afterUseSeed(self):
            self.safe += 0.001

        def newSeed(self):
            self.seed = rs(self, -1000000, 1000000)
            self.safe = 0.0

        def phy(self):
            return r2(self.physical * self.physicalRegarded)

        def wor(self):
            return r2(self.working * self.workingRegarded)

        def wri(self):
            return r2(self.writing * self.writingRegarded)

        def sev(self):  # 单调递减
            if self.cured >= 0:
                self.severity = max(self.severity, 0.0)
                return max(0.0001, r2(self.severity * self.severityRegarded))
            if self.severity < 0.65 + 0.05 * self.week:
                self.severity = 0.65 + 0.05 * self.week
            if self.severityRegarded <= 0.2:
                return r2(self.severity * 0.2)

            return r2(self.severity * self.severityRegarded)
        

        def phyCons(self):  # 单调递减
            if self.phy()<3:
                return 0.12 * self.phy() ** 2 - 0.72 * self.phy() + 1.7
            else:
                return 0.55

        def phyReco(self):  # 单调递增
            if self.phy()<3:
                return -0.19 * self.phy() ** 2 + 1.14 * self.phy() - 0.1
            else:
                return 1.7

        def wriConc(self):
            if self.wri()<3:
                return -4 * self.wri() ** 2 + 35 * self.wri() -40
            else:
                return 35
            

        def useFoodScale(self):
            if self.fooduse < 0:
                self.fooduse = 0
            scale = 1200 * self.foodRecovery / self.sev()
            scale *= 1-(self.fooduse* 0.005)
            scale *= (self.basicRecovery + 1) / 2
            scale *= 0.001
            scale = max(0.2, scale)
            return scale

        def useDrugScale(self):
            scale = 1000 * self.drugRecovery / self.sev()
            scale *= 0.001
            scale = max(0.2, scale)
            return scale
        
        def aggravationConsumption(self):
            consumption = 70
            consumption *= self.deteriorateConsumption  # 受睡眠消耗数值影响
            consumption *= max(self.sev(), 1.0) ** 1.5
            consumption *= self.phyCons()  # 受身体素质和严重度影响
            if consumption < self.mental * 0.5:
                consumption = self.mental * 0.5
            return r2(consumption)

        def aggravation(self):
            consumption = self.aggravationConsumption() * f()
            s = 0

            if self.week < 3:
                if rra(self, 50):
                    s = 0.01
                else:
                    s = 0.02
            elif self.week < 5:
                if rra(self, 50):
                    s = 0.02
                else:
                    s = 0.03
            elif self.week < 8:
                s = 0.03
            elif self.week >= 8:
                s = 0.04


            if self.cured > -1:
                self.cured += 1
                self.color -= 0.01

            self.severity += r2(s)

            if consumption > 0:
                Notice.add(_('睡眠消耗了')+r2s(consumption)+_('点精神状态！'))
                self.mental -= r2(consumption)
            else:
                Notice.add(_('睡眠没有消耗精神状态！'))

            if s > 0:
                Notice.add(_('严重度上升了')+r2s(s)+_('点！'))


        def dateChange(self):
            self.times = 0
            self.stime()
            if self.mon in (1, 3, 5, 7, 8, 10, 12):
                if self.day == 31:
                    self.mon += 1
                    self.day = 1
                else:
                    self.day += 1
            elif self.mon == 2:
                if self.day == 28:
                    self.mon += 1
                    self.day = 1
                else:
                    self.day += 1
            elif self.day == 30:
                self.mon += 1
                self.day = 1
            else:
                self.day += 1

            if self.today == 7:
                self.today = 1
                self.week += 1
            else:
                self.today += 1

            if self.mon == 13 and self.day == 1:
                self.mon = 1

        def rh(self, a=0, b=24):
            return rs(self, a, b)

        def rm(self, a=1, b=59):
            randMin = rs(self, a, b)
            return '0' + str(randMin) if randMin < 10 else str(randMin)
            # 返回一个范围内的随机min，默认1-59，若返回值小于10则补0

        def st(self):
            
            specTimeDict = {
                '0' : ['7', '00'],
                '1' : ['7', self.rm(21, 49)],
                '2' : ['7', '50'],
                '3' : ['8', '00'],
                '4' : [self.rh(8, 11), self.rm(21, 49)],
                '5' : ['12', '00'],
                '6' : ['12', self.rm(40)],
                '7' : ['13', '00'],
                '8' : [self.rh(13, 16), self.rm()],
                '9' : ['17', '00'],
                '10' : ['17', self.rm(1, 29)],
                '11' : ['18', '00'],
                '12' : [self.rh(18, 20), self.rm()],
                '13' : ['21', self.rm(0)],
                '14' : ['22', '00'],
                '15' : ['24', '00'],
                '666' : ['???', '???']
            }
            r = specTimeDict[str(self.times)]
            if self.spec_hour is not None:
                r[0] = self.spec_hour
            if self.spec_min is not None:
                r[1] = self.spec_min

            if len(r[1])<2:
                r[1]='0' + r[1]


            return r

        def stime(self, hour=-1, min=-1):
            
            if hour < 0 and min < 0:
                if self.staylate:
                    return
                self.spec_hour = None
                self.spec_min = None
            elif hour > 0 and min >0:
                self.spec_hour = str(hour)
                self.spec_min = str(min)
            else:
                self.spec_min = str(hour)

        def meds(self):
            meds = 0
            for i in (MedicineA, MedicineB, MedicineC, MedicineD):
                if i.has(self):
                    if not i.get(self).broken:
                        meds += i.get(self).amounts
            return meds

        def newMorningWeather(self, b=False):
            if self.cured > -1:
                return WeatherUnknown

            if self.week == 0:
                return WeatherSunny

            if Despair.has(self):
                return WeatherNone

            if WeatherTornado.has(self):
                if WeatherTornado.get(self).duration != 0:
                    return WeatherTornado
                
            weathers = [WeatherSunny, WeatherRainy, WeatherCloudy]

            if 4 < self.week <= 10:
                if self.today not in (3, 4, 5) and rra(self, 3):
                    return WeatherTornado

                weathers += [WeatherWet, WeatherHot, WeatherThunder, WeatherWindy]
        
            if b:
                import random
                       
                seed = rs(self, -1000000, 1000000)
                random.seed(seed)
                
                return random.choice(weathers)

            return rcs(self, weathers)

            

            

        def newMorningEffects(self):  # 每天早上调用以添加随机状态及反应
            if not list(filter(lambda x: x.kind=='天气', self.effects)):
                self.newMorningWeather().add(self)

            if self.week == 0 or Despair.has(self) or self.cured > -1:
                return

            states2 = {
                Erection: 30,
                Restlessness: 5,
                Contentment: 5,
                Desire: 5,
                Sadness: 5,
                Agony: 5,
                Dread: 5,
                Relaxation: 5
            }


            if self.today in (1, 2):
                states2[Restlessness] += 20
            if self.today in (3, 4):
                states2[Restlessness] += 40

            if self.today in (6, 7):
                states2[Contentment] += 40
            if MeetingReward7.has(self):
                states2[Restlessness] += 100

            if PhysProb.has(self):
                states2[Contentment] += 40
            if MentProb.has(self):
                states2[Sadness] += 40

            if self.severity > 1 + 0.075 * self.week:
                states2[Agony] += 15
                states2[Dread] += 15

            if self.mental > 50:
                states2[Dread] += 30

            if Novice.has(self):
                states2[Dread] = 0

            pool = (0,0,0,0,0,0,0,0,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,5) # 0:33.3%  1:12.5%  2:20.8%  3:16.6%  4:12.5%  5:4.6%

            if rra(self, 55):
                ConsInc.add(self, rca(self, pool))
            else:
                ConsDec.add(self, rca(self, pool))

            if rra(self, 60):
                ConcDec.add(self, rca(self, pool))
            else:
                ConcInc.add(self, rca(self, pool))


            for i in states2:
                if rra(self, states2[i]):
                    i.add(self)


        def updateAfterSleep(self):  # 夜晚进行的更新工作
            for i in range(len(self.effects) - 1, -1, -1):
                self.effects[i].afterSleepAction(self)
            for i in range(len(self.effects) - 1, -1, -1):
                self.effects[i].timeUpdate(self)
            for i in range(len(self.items) - 1, -1, -1):
                self.items[i].afterSleepAction(self)
            for i in range(len(self.items) - 1, -1, -1):
                if self.items[i].kind == _('文稿'):
                    self.items[i].comm.timeUpdate(self)
                else:
                    self.items[i].timeUpdate(self)

            if persistent.AutoQuitBrokenItem and self.finalStageDays == -1:
                for i in range(len(self.items) - 1, -1, -1):
                    if self.items[i].broken: 
                        del self.items[i]

            for k in list(self.itemcd.keys()):
                if self.itemcd[k] > 0:
                    self.itemcd[k] -= 1
                if self.itemcd[k] == 0:
                    del self.itemcd[k]
                    
        def updateMedicine(self):
            for i in self.medinfo:
                self.medinfo[i].afterSleepAction(self)
            
        def updateAfterTask(self, task):
            for i in range(len(self.effects) - 1, -1, -1):
                self.effects[i].afterTaskAction(self, task)
            for i in range(len(self.items) - 1, -1, -1):
                self.items[i].afterTaskAction(self, task)

        def calPlatformReward(self):
            money = 0
            reader = 0
            for i in range(int(self.popularity/1000)):
                if rra(self, 20):
                    money += ra(self, 20 * self.wri(), 100 * self.wri())
                    reader += 1
            
            if money != 0:
                if money > self.price*0.75:
                    money = int(self.price *0.75* f())
                Notice.add(_('昨日收到由%s位读者打赏给您的共%s元。') % (reader, money))
                self.money += money

        def calWorkPaid(self): 
            completedPercent = int(self.achievedGoal*100/self.goal)
            
            if completedPercent > 120:
                paid = r2(self.wages * 1.2 * 1.05)
                wages = r2(self.working * 2000 * 1.05 ** self.week)

            elif completedPercent >= 100:
                paid = r2(self.wages)
                wages = r2(self.working * 2000 * 1.035 ** self.week)

            elif completedPercent >= 80:
                paid = r2(self.wages * completedPercent * 0.01 * 0.8)
                wages = r2(self.working * 2000 * 1.015 ** self.week)

            elif completedPercent >= 50:
                paid = r2(self.wages *completedPercent * 0.01 * 0.6)
                wages = r2(self.working * 2000 * 0.9 ** self.week)

            else:
                paid = r2(self.wages *completedPercent * 0.01 * 0.55)
                wages = r2(self.working * 2000 * 0.8 ** self.week)

            if wages > self.price * 8 and self.wages<self.price * 8:
                wages = r2(self.price * 8)

            if wages < self.price * 5 and completedPercent >= 80:
                wages = r2(self.price * 5)

            return paid, wages

        def getWorkPaid(self):  # 在script里判定
            completedPercent = int(self.achievedGoal*100/self.goal)

            paid, wages = self.calWorkPaid()

            if completedPercent > 120:
                if self.cured < 0:
                    WorkReward.add(self)
                paid += ra(self, 50, 200)
                
            elif completedPercent >= 100:
                if rra(self, 75) and self.cured < 0:
                    WorkReward.add(self)
                paid += ra(self, 0, 50)
            
            #else:
                #Anxiety.add(self)

            self.wages = wages
            self.achievedGoal = 0.0
            self.goal = (1.08 ** self.week) * 0.3 + self.working * 0.7
            self.goal = r2(self.goal * ra(self, 800, 1100) * 0.01 * f())
            if GameModule1.has(self):
                self.goal = r2(self.goal * (1 + (0.05 * self.week)))
            self.money += paid
            if self.cured < 0 and not Despair.has(self):
                Notice.add(_('Boss：“第%s周工资已发放。”') % self.week)
                Notice.add(_('X付宝到账：%s元！') % r2(paid))
                Notice.add(_('Boss：“本周的工作指标系数为%s。”') % self.goal)

        def plotUpdate(self):
            #if self.sol_p %2 == 0:
            #    self.sol_p += 1

            #if self.hal_p %2 == 0:
            #    self.hal_p += 1
                
            #if self.aco_p %2 == 0:
            #    self.aco_p += 1
            pass
            

        def newDay(self, times=1):
            global _history_list
            _history_list = []


            if self.p2:
                self.p2.newDay()

            t = r2(renpy.get_game_runtime())
            persistent.runtime += t
            self.playtime += t
            renpy.clear_game_runtime()


            if not persistent.nomedicine:
                self.aggravation()
                
            self.updateAfterSleep()
            self.updateMedicine()
            if self.cured < 0 and not Despair.has(self):
                if not Achievement603.has():
                    self.nousemed += 1
                    if self.nousemed >= 7:
                        Achievement603.achieve()
                self.refreshUnacComm()
            self.newSeed()
            
            
            #  起床后
            #  熬夜的情况
            if not self.staylate:
                self.dateChange()
                
            else:
                Achievement305.achieve()
                self.staylate = False
                self.times = 0
                self.stime()
            
            self.newMorningEffects()
            if self.cured == -1 and not Despair.has(self):
                if rra(self, 10):
                    PhysRezA.add(self)
            
            sortByID(self.effects)
            sortByID(self.items)
            if times > 1:
                self.newDay(times-1)

        def beforeSchedule(self):
            if self.cured < 0 and not Despair.has(self):
                self.calPlatformReward()
            self.morning_checkTask()
            if self.today == 5:
                if not Despair.has(self):
                    self.getWorkPaid()
                self.plotUpdate()
                self.hadAskedForLeave = False
                if self.sol_p == 1:
                    self.sol_p = 2
                if self.sol_p == 3:
                    self.sol_p = 4

                self.price = r2(self.price *(100 + self.priceIncrease) * 0.01)

                
                if self.money <= self.price * 10:
                    self.priceIncrease = ra(self, 10, 25)
                    if GameModule1.has(self):
                        self.priceIncrease *= 1.5
                
                else:
                    self.priceIncrease = (self.money * 0.1 / self.price) - 1
                    self.priceIncrease *= 10

                    self.priceIncrease = int(self.priceIncrease * f())
                

            if self.hal_p == 10 and self.today == 1:
                Message.new(self, 'Halluke', 'Halluke', _('那个，我想说一些事，如果我说错了的话，请不要生气。\n第一次上课的时候老师有清点人数，我对来上课的人也大概有了一点印象，但是你是后来才出现的，最初我把你当成第一节课就没来的学生，但是老师当时点名也没人缺席的样子。后来发现老师点名的时候也没看到你过产生回应。我也调查了一段时间，在年级大群，甚至校园墙上都没有查到和你有关的信息。\n你并不是我们学校的人，对吧？\n不过我主要是想提醒你，下周的周六就是考试了，虽然你并不需要考试，如果你想的话，可以来帮我发球。'), '6', '42')
                self.hal_p = 11
    
            Notice.show()
            Achievement.show()

        def cheat_times(self):
            self.times = 2

        def cheat_ment(self, value):
            self.mental += value
        
        def cheat_sev(self, value):
            self.severity += value
        
        def cheat_wor(self, value):
            self.working += value
        
        def cheat_phy(self, value):
            self.physical += value
        
        def cheat_wri(self, value):
            self.writing += value

        def cheat_route(self, value):
            self.route = value

        def when_cheat(self):
            self.cheat = True

        
        def get_task_time(self):
            if all(p.plancheck):
                return -1
            for i, done in enumerate(p.plancheck):
                if not done:
                    return i
            