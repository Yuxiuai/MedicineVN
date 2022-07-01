init python early:

    class Player:
        def __init__(self, name='Solitus'):
            self.name = name
            self.seed = rd(-1000000, 1000000)
            self.safe = 0.0

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

            self.onVacation = True
            self.onOutside = True

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

            self.fooduse = 0
            self.druguse = 0

            self.effects = []
            self.afterSleepEffects = []
            self.items = []
            self.usedMedicines = [MedicineA]
            self.unlockedTasks = []
            self.lockedTasks = []
            self.starItems = []
            self.plan = [NoTask, NoTask, NoTask]
            self.gymplan = [NoSport, NoSport, NoSport]

            self.resistance = {'MedicineA':0, 'MedicineB':0, 'MedicineC':0}
            self.itemcd = {}

            self.unacComm = []

            self.retval = None
            self.retval1 = None

            self.hadAskedForMoney = False
            self.hadAskedForLeave = False
            self.finalStageDays = 1
            self.aggra = 0
            self.messages = {'Pathos':[], 'Halluke':[], 'Acolas':[], 'Depline':[]}

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
            self.items.append(UnfinishedCommission(p))
            self.items[-1].comm = comm
            showNotice(['已接取新委托：%s' % self.items[-1].name])
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

        def checkTask(self):
            for i in range(3):
                if self.plan[i].checkAvailable(self, self.today, i)!=True:
                    self.plan[i] = NoTask

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
            return r2(self.severity ** 1.5 * self.severityRegarded)

        def phyCons(self):  # 单调递减
            if self.phy()<4:
                return 0.127 * self.phy() ** 2 - 0.87 * self.phy() + 1.85
            else:
                return 0.4

        def phyReco(self):  # 单调递增
            if self.phy()<4:
                return -0.177 * self.phy() ** 2 + 1.621 * self.phy() - 0.54
            else:
                return 2

        def wriConc(self):
            if self.wri()<4:
                return -3.333 * self.wri() ** 2 + 34.381 * self.wri() -39.071
            else:
                return 45
            

        def useFoodScale(self):
            scale = 1200 * self.foodRecovery / self.sev()
            scale *= 1-(self.fooduse* 0.003)
            scale *= (self.basicRecovery + 1) / 2
            scale *= 0.001
            scale = max(0.2, scale)
            return scale

        def useDrugScale(self):
            scale = 1200 * self.drugRecovery / self.sev()
            scale *= 1-(self.druguse* 0.002)
            scale *= (self.basicRecovery + 1) / 2
            scale *= 0.001
            if scale < 0.3:
                return 0.3
            scale = max(0.2, scale)
            return scale

        def aggravationConsumption(self):
            consumption = 50
            consumption *= self.deteriorateConsumption  # 受睡眠消耗数值影响
            consumption *= self.sev()
            consumption *= self.phyCons() ** 1.5  # 受身体素质和严重度影响
            if consumption < self.mental * 0.75:
                consumption = self.mental * 0.75
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

            if self.severity-s < 0.85 + 0.075 * self.week:
                s = 0.85 + 0.075 * self.week - self.severity

            self.severity += r2(s)

            if consumption > 0:
                Notice.add('睡眠消耗了'+r2s(consumption)+'点精神状态！')
                self.mental -= r2(consumption)
            else:
                Notice.add('睡眠没有消耗精神状态！')

            if s > 0:
                Notice.add('严重度上升了'+r2s(s)+'点！')


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
                self.spec_hour = None
                self.spec_min = None
            elif hour > 0 and min >0:
                self.spec_hour = str(hour)
                self.spec_min = str(min)
            else:
                self.spec_min = str(hour)

        def meds(self):
            meds = 0
            if MedicineA.hasByType(self):
                meds += MedicineA.getByType(self).amounts
            if MedicineB.hasByType(self):
                meds += MedicineB.getByType(self).amounts
            if MedicineC.hasByType(self):
                meds += MedicineC.getByType(self).amounts
            return meds

        def addAfterSleep(self):
            for i in self.afterSleepEffects:
                i.add(self)
            self.afterSleepEffects = []

        def newMorningWeather(self, b=False):
            if self.week == 0:
                return WeatherSunny
                
            weathers = [WeatherSunny, WeatherRainy, WeatherCloudy]

            if self.week >4:
                weathers += [WeatherWet, WeatherHot, WeatherThunder, WeatherWindy]

            if Despair.has(self):
                return WeatherNone

            if b:
                import random
                seed = rs(self, -1000000, 1000000)
                random.seed(seed)
                return random.choice(weathers)

            return rcs(self, weathers)

            

            

        def newMorningEffects(self):  # 每天早上调用以添加随机状态及反应
            self.newMorningWeather().add(self)

            if self.week == 0 or Despair.has(self):
                return

            states2 = {
                Erection: 30,
                Restlessness: 5,
                Contentment: 5,
                Desire: 5,
                Sadness: 5,
                Agony: 5,
                Dread: 5
            }


            if self.today in (1, 2):
                states2[Restlessness] += 10
            if self.today in (3, 4):
                states2[Restlessness] += 15
            if PhysProb.has(self):
                states2[Contentment] += 15
            if MentProb.has(self):
                states2[Sadness] += 15
            if MentPun.has(self):
                states2[Sadness] += 15
            if self.severity > 1 + 0.075 * self.week:
                states2[Agony] += 10
                states2[Dread] += 10
            if self.mental > 50:
                states2[Dread] += 20
            if GameMode3.has(self):
                states2[Dread] += 10
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

            for i in self.usedMedicines:
                if rra(self, 20+2*self.week):
                    i.d_.add(self)

            self.addAfterSleep()  # 添加第二日必定获得的状态

        def updateAfterSleep(self):  # 夜晚进行的更新工作
            for i in range(len(self.effects) - 1, -1, -1):
                self.effects[i].afterSleepAction(self)
            for i in range(len(self.effects) - 1, -1, -1):
                self.effects[i].timeUpdate(self)
            for i in range(len(self.items) - 1, -1, -1):
                self.items[i].afterSleepAction(self)
            for i in range(len(self.items) - 1, -1, -1):
                self.items[i].timeUpdate(self)
                if self.items[i].kind == '文稿':
                    self.items[i].comm.timeUpdate(self)

            for k in list(self.itemcd.keys()):
                if self.itemcd[k] > 0:
                    self.itemcd[k] -= 1
                if self.itemcd[k] == 0:
                    del self.itemcd[k]
                    

            
        
        def updateMedicine(self):
            for i in self.usedMedicines:
                r = 0
                if self.week < 5:
                    if rra(self, 50):
                        r = 1
                else:
                    if len(self.usedMedicines) == 1:
                        if rra(self, 25):
                            r = 1
                    else:
                        if rra(self, 50):
                            r = 1
                self.resistance[i.__name__] = max(self.resistance[i.__name__] - r, 0)
            
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
                Notice.add('昨日收到由%s位读者打赏给您的共%s元。' % (reader, money))
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
                WorkReward.add(self)
                paid += ra(self, 50, 200)
                
            elif completedPercent >= 100:
                if rra(self, 75):
                    WorkReward.add(self)
                paid += ra(self, 0, 50)
            
            else:
                Anxiety.add(self)

            self.wages = wages
            self.achievedGoal = 0.0
            self.goal = (1.08 ** self.week) * 0.3 + self.working * 0.7
            self.goal = r2(self.goal * ra(self, 750, 1100) * 0.01 * f())
            if GameMode5.has(self):
                self.goal = r2(self.goal * 1.15)
            self.money += paid

            Notice.add('Boss：“第%s周工资已发放。”' % self.week)
            Notice.add('X付宝到账：%s元！' % r2(paid))
            Notice.add('Boss：“本周的工作指标系数为%s。”' % self.goal)

        def plotUpdate(self):
            #if self.sol_p %2 == 0:
            #    self.sol_p += 1

            #if self.hal_p %2 == 0:
            #    self.hal_p += 1
                
            #if self.aco_p %2 == 0:
            #    self.aco_p += 1
            pass
            

        def newDay(self):
            # 睡觉后
            global _history_list
            self.aggravation()
            self.updateAfterSleep()
            self.updateMedicine()
            self.refreshUnacComm()
            self.newSeed()
            _history_list = []
            
            # 起床后
            self.dateChange()
            self.newMorningEffects()
            if rra(self, 10):
                PhysRezA.add(self)
            
            sortArr(self.effects)
            sortArr(self.items)

        def beforeSchedule(self):
            self.calPlatformReward()
            self.checkTask()
            if self.today == 5:
                self.getWorkPaid()
                self.plotUpdate()
                self.hadAskedForLeave = False
                if self.sol_p == 1:
                    self.sol_p = 2
                if self.sol_p == 3:
                    self.sol_p = 4

                self.price = r2(self.price *(100 + self.priceIncrease) * 0.01)

                
                if self.money <= self.price * 8:
                    self.priceIncrease = ra(self, 5, 15)
                    if GameMode3.has(self):
                        self.priceIncrease *= 2.25
                
                else:
                    self.priceIncrease = (self.money * 0.125 / self.price) - 1
                    self.priceIncrease *= 10

                    self.priceIncrease = int(self.priceIncrease * f())
                

            if self.hal_p == 10 and self.today == 1:
                Message.new(self, 'Halluke', 'Halluke', '那个，我想说一些事，如果我说错了的话，请不要生气。\n第一次上课的时候老师有清点人数，我对来上课的人也大概有了一点印象，但是你是后来才出现的，最初我把你当成第一节课就没来的学生，但是老师当时点名也没人缺席的样子。后来发现老师点名的时候也没看到你过产生回应。你并不是我们班的对吧？我也调查了一段时间，在年级大群，甚至校园墙上都没有查到和你有关的信息。\n你并不是我们学校的人，对吧？\n不过我主要是想提醒你，下周的周六就是考试了，虽然你并不需要考试，如果你想的话，可以来帮我发球。', '6', '42')
                self.hal_p == 11
    
            Notice.show()