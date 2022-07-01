init python early:

    class MedicineBase(Item):
        id = None
        name = None
        kind = '实验药物'
        maxCd = 0
        maxDu = 8
        isUnique = False
        info = None
        reuse = False
        d_ = None
        w_ = None
        e_ = None

        def __init__(self, player):
            super(MedicineBase, self).__init__(player)
            self.takeTime_ = -4

        @classmethod
        def getFormatOperableTime(cls, player):  # 起床时：0->1，早上规划日程时：2->2，午休时：6->3，睡觉前：10->4
            dictTakeMedTime = {0: 1, 2: 2, 6: 3, 10: 4,
                            101: 1, 102: 2, 103: 3, 104: 4}
            if player.times not in dictTakeMedTime:
                if player.times < 2:
                    return dictTakeMedTime[0]
                if player.times < 6:
                    return dictTakeMedTime[2]
                if player.times < 10:
                    return dictTakeMedTime[6]
                if player.times >= 10:
                    return dictTakeMedTime[10]
            else:
                return dictTakeMedTime[player.times]

        @classmethod
        def getInterval(cls, player, takeTime):  # 获得间隔
            r = []
            for i in player.usedMedicines:
                if i is not None:
                    if i.hasByType(player):
                        r.append(takeTime - i.getByType(player).takeTime_)
                    else:
                        r.append(takeTime - cls.getFormatOperableTime(player))
            return r

        @classmethod
        def getBenefit(cls, player):
            if player.times == 0 and cls==MedicineA:
                s = int(cls.getMedicineScale(player, True) * 140)
            elif cls==MedicineB:
                s = int(cls.getMedicineScale(player, True) * (MedicineB.recovery(player, prev=True) * 100 / 60))
            elif cls==MedicineC:
                s = int(cls.getMedicineScale(player, True) * Task.getConsScale(player) * 100)
            else:
                s = int(cls.getMedicineScale(player, True) * 100)

            return '\n\n使用效率：' + str(s) + '%\n'

        @classmethod
        def getResInfo(cls, player):
            infor = cls.getBenefit(player)
            scale0 = (100 - player.resistance[cls.__name__]) * 0.01
            scale1 = 1
            scale2 = 1
            scale3 = 1
            intervals = cls.getInterval(player, cls.getFormatOperableTime(player))
            for i in range(len(intervals)):
                if player.usedMedicines[i] == cls:  # 本药物情况：需要隔一个时间段吃
                    if intervals[i] == 0:
                        scale1 *= 0.33
                    if intervals[i] == 1:
                        scale2 *= 0.66
                else:
                    if intervals[i] == 0:
                        scale3 *= 0.5
            info = '\n其中：\n' if s != 100 else ''
            info0 = '    抗药性：-' + str(int(player.resistance[cls.__name__])) + '%\n' if player.resistance[cls.__name__] != 0 else ''
            info1 = '    刚刚使用过本实验药物：*' + str(int(scale1*100)) + '%\n' if scale1 != 1 else ''
            info2 = '    近期使用过本实验药物：*' + str(int(scale2*100)) + '%\n' if scale2 != 1 else ''
            info3 = '    刚刚使用过其他实验药物：*' + str(int(scale3*100)) + '%\n' if scale3 != 1 else ''
            infoa = '{color=#fe6363}    早上服用：*140%\n{/color}' if player.times == 0 and cls==MedicineA else ''
            infob = '{color=#7881e8}    该精神状态下服用：*'+str(int(MedicineB.recovery(player, prev=True) * 100 / 60))+'%{/color}\n' if cls==MedicineB else ''
            infoc = '{color=#e4f06f}    基础精神消耗加成效果：*'+str(int(100*Task.getConsScale(player)))+'%{/color}\n' if cls==MedicineC else ''
            infoitem = '    空的安慰剂药瓶：+20%' if PlaceboBottle.hasByType(player) else ''
            infogm1 = '    偏头痛：+15%' if GameMode1.has(player) else ''

            return infor+info+info0+info1+info2+info3+infoa+infob+infoc+infoitem+infogm1+'\n'

        @classmethod
        def getMedicineScale(cls, player, prev=False):
            scale = 1.0
            scale *= player.drugRecovery  # 所有药物恢复效果
            if prev == False:
                scale *= f()

            scale *= (100 - player.resistance[cls.__name__]) * 0.01  # 药物自身抗药性
            intervals = cls.getInterval(player, cls.getFormatOperableTime(player))  # 间隔列表
            for i in range(len(intervals)):
                if player.usedMedicines[i] == cls:  # 本药物情况：需要隔一个时间段吃
                    if intervals[i] == 0:
                        scale *= 0.33
                        if prev == False:
                            player.resistance[cls.__name__] += min(player.resistance[cls.__name__] + ra(player, 3, 5), 80)
                            Notice.add('升高了3点严重程度！')
                            player.severity += 0.03
                    if intervals[i] == 1:
                        scale *= 0.66
                        if prev == False:
                            player.resistance[cls.__name__] += min(player.resistance[cls.__name__] + ra(player, 1, 3), 80)
                            Notice.add('升高了1点严重程度！')
                            player.severity += 0.01
                else:  # 非本药物情况：只要不一个时间段同时吃就可以
                    if intervals[i] == 0:
                        scale *= 0.5
                        if prev == False:
                            player.resistance[cls.__name__] += min(player.resistance[cls.__name__] + ra(player, 1, 3), 80)
                            Notice.add('升高了2点严重程度！')
                            player.severity += 0.02
            return r4(scale)

        def afterSleepAction(self, player):  # 睡眠后将使用时间提前
            self.takeTime_ = -4

        def useItemAction(self, player):
            if type(self) not in player.usedMedicines:  # 使用后将自身填进已经使用过的药物中
                player.usedMedicines.append(type(self))
            if type(self).d_.has(player):  # 移除对应的药物依赖
                type(self).d_.subByType(player)
            if type(self).w_.has(player):  # 处理对应的戒断反应
                type(self).w_.get(player).afterDrug(player)

            rec = type(self).recovery(player) * type(self).getMedicineScale(player)
            self.takeTime_ = type(self).getFormatOperableTime(player)  # 更新药物使用时间
            Notice.add('使用了%s，恢复了%s点精神状态。' % (type(self).name, r2s(rec)))
            player.mental += r2(rec)

            if player.resistance[type(self).__name__] > 40:
                Notice.add('由于使用的药物抗药性过高，升高了2点严重程度！')
                player.severity += 0.02
            
            if player.week < 3:
                resi = ra(player, 1, 2)
            elif player.week < 8:
                resi = ra(player, 1, 3)
            elif player.week < 12:
                resi = ra(player, 2, 4)
            elif player.week >= 12:
                resi = ra(player, 3, 5)

            player.resistance[type(self).__name__] = min(player.resistance[type(self).__name__] + resi, 80)
            type(self).e_.add(player)  # 添加药物作用
            player.druguse += 1

        @classmethod
        def recovery(cls, player, prev=False):  # 独特的药物机制，返回具体恢复值 需重写
            if prev == False:
                rec = 100
                return rec

        @classmethod
        def expectedReco(cls, player):
            return r2(cls.recovery(player, prev=True) * cls.getMedicineScale(player, prev=True))

    class MedicineA(MedicineBase):
        id = 100
        name = '药物{font=arial.ttf}α{/font}'
        kind = '实验药物'
        info = '移除药物依赖{font=arial.ttf}α{/font}以及戒断反应{font=arial.ttf}α{/font}，获得药物作用{font=arial.ttf}α{/font}。\n' \
            '在起床时使用该药物时，恢复额外的精神状态。'
        d_ = DrugDA
        w_ = DrugWA
        e_ = DrugEA
        ad = '“一日1-2次，使用频率依你的头疼剧烈程度而定，最好早上吃……另外一周后就不要再用上一周旧的药物了……”\n我的主治医师Pathos在我每次买药之前都会和我念叨一遍，我都听腻了，难道他真以为我是那种什么都记不住的三岁小孩吗？'

        @classmethod
        def recovery(cls, player, prev=False):
            rec = 60
            if player.times == 0 or player.times == 101:
                rec *= 1.4
                #Notice.add('在起床时使用，恢复了额外30%的精神状态。')
            return rec


    class MedicineB(MedicineBase):
        id = 101
        name = '药物{font=arial.ttf}β{/font}'
        kind = '实验药物'
        info = '移除药物依赖{font=arial.ttf}β{/font}以及戒断反应{font=arial.ttf}β{/font}，获得药物作用{font=arial.ttf}β{/font}。\n' \
            '当前的精神状态越少，恢复的精神状态越多，低于阈值时恢复效果将大幅度下降。'
        d_ = DrugDB
        w_ = DrugWB
        e_ = DrugEB
        ad = '“这种药只有在非常紧急的时候才能服用！因为服用之后会产生幻觉，以及各种尚不明确原因的效果……就算你喜欢这种幻觉，这药也不是为了让你当合法LSD用的！”\n为什么不能？写东西之前来份这个魔法药片，灵感就会像泉水似的往外喷！'

        @classmethod
        def resistance(cls, player):
            return player.resists[1]

        @classmethod
        def recovery(cls, player, prev=False):
            
            if player.mental < -50:
                rec = 100
            elif player.mental > 120:
                rec = 5
                if prev==False:
                    Notice.add('升高了2点严重程度！')
                    player.severity += 0.02
            else:
                rec = -0.65 * player.mental + 67
            #Notice.add('恢复了相当于药物基础恢复量的' + r2s(s) + '%的精神状态。')
            return rec


    class MedicineC(MedicineBase):
        id = 102
        name = '药物{font=arial.ttf}γ{/font}'
        kind = '实验药物'
        info = '移除药物依赖{font=arial.ttf}γ{/font}以及戒断反应{font=arial.ttf}γ{/font}，获得药物作用{font=arial.ttf}γ{/font}。\n' \
            '单次服用恢复较少精神状态，但每次完成日程后都会恢复较多精神状态，基础精神状态消耗越多，恢复的越多。'
        d_ = DrugDC
        w_ = DrugWC
        e_ = DrugEC
        ad = '“这种药物对肠胃影响很大，也会影响你的味觉，虽然恢复效果一般，但是长远来看对你的头疼恢复效果还是要比前面几种药好一点的。”\n真不喜欢吃这药，如果吃美食都没有了快乐，那我活着还有什么乐趣……'

        @classmethod
        def resistance(cls, player):
            return player.resists[2]

        @classmethod
        def recovery(cls, player, prev=False):
            rec = 30
            return rec

        @classmethod
        def expectedReco(cls, player):
            times = 3
            if player.times >= 4:
                times -= 1
            if player.times >= 8:
                times -= 1
            if player.times >= 12:
                times -= 1
            return r2(cls.recovery(player, prev=True) * cls.getMedicineScale(player, prev=True) +2000 * 0.01 * (100 - player.resistance['MedicineC']) * 0.01 * Task.getConsScale(player) * times)

    class MedicineD(Item):
        id = 103
        name = '药物{font=arial.ttf}δ{/font}'
        kind = '实验药物'
        maxCd = 0
        maxDu = 8
        isUnique = False
        info = '移除所有其他药物相关的药物反应，获得药物作用{font=arial.ttf}δ{/font}。\n' \
            '恢复精神状态。'
        ad = '“你已经不需要其他的药了。”'

        def useItemAction(self, player):
            r = rd(50000, 200000) * 0.01
            Notice.add('恢复了%s点精神状态！' % str(r))
            player.mental += r
            DrugED.add(player)
            for i in [DrugDA, DrugDB, DrugDC, DrugWA, DrugWB, DrugWC, DrugEA, DrugEB, DrugEC]:
                if i.has(player):
                    i.clearByType(player)

        @classmethod
        def getResInfo(cls, player):

            infor = '\n\n使用效率：' + glitchtext(5) + ' %\n'

            info = '\n其中：\n'
            info0 = '    ' + glitchtext(rd(5,25))
            info1 = '\n    ' + glitchtext(rd(5,25))
            infoa = '\n{color=#ff60cd}    ' + glitchtext(rd(5,25)) + '{/color}'
            infob = '\n{color=#ff60cd}    ' + glitchtext(rd(5,25)) + '{/color}\n'

            return infor+info+info0+info1+infoa+infob


    class DrugHypnotic(Item):
        id = 300
        name = '安眠药'
        kind = '普通药物'
        maxCd = 0
        maxDu = 280
        reuse = False
        isUnique = False
        info = '服用后随层数降低睡眠消耗的精神状态，本日还没有服用过该药物时额外降低更多的精神状态。\n建议服用次数为每日一次，多次使用的效果未知。'
        p=0.08

        def useItemAction(self, player):
            DrugHypnoticEffect.add(player)
            player.druguse += 1
            player.severity += 0.01



    class DrugColdrex(Item):
        id = 301
        name = '感冒药'
        kind = '普通药物'
        maxCd = 0
        maxDu = 280
        reuse = False
        isUnique = False
        info = '服用后降低少量专注度，若没有生病则获得大量严重度。\n' \
            '使用后会延长1天生病的持续时间并根据层数提升休息时恢复的效果，但本效果结束时则会减少生病的持续时间。\n' \
            '建议服用次数为每日一次，多次使用的效果未知。'
        p=0.15

        def useItemAction(self, player):
            if DrugColdrexEffect.has(player):
                effect = DrugColdrexEffect.get(player)
                if effect.duration == 1 and effect.stacks >1:
                    player.severity += 0.05
                elif effect.duration == 1 and effect.stacks >2:
                    player.severity += 0.1
                elif effect.duration == 1 and effect.stacks >3:
                    player.severity += 1000

            if PhysPun.has(player):
                DrugColdrexEffect.add(player)
            else:
                player.severity += 0.05
            player.druguse += 1
            player.severity += 0.02


    class DrugIbuprofen(Item):
        id = 302
        name = '头疼药'
        kind = '普通药物'
        maxCd = 0
        maxDu = 280
        reuse = False
        isUnique = False
        info = '服用后每完成一个日程随层数百分比恢复微量精神状态。\n建议服用次数为每日一次，多次使用的效果未知。'
        p=0.05

        def useItemAction(self, player):
            if DrugIbuprofenEffect.has(player):
                effect = DrugIbuprofenEffect.get(player)
                if effect.duration == 1 and effect.stacks >1:
                    player.severity += 0.1
                elif effect.duration == 1 and effect.stacks >2:
                    player.severity += 1000
            DrugIbuprofenEffect.add(player)
            player.druguse += 1

    class DrugVitamin(Item):
        id = 303
        name = '维生素片'
        kind = '普通药物'
        maxCd = 7
        maxDu = 280
        reuse = False
        isUnique = False
        info = '降低所有曾使用过的药物的抗药性。'
        p=0.25

        def useItemAction(self, player):
            for i in player.usedMedicines:
                player.resistance[i.__name__] -= 3
                if player.resistance[i.__name__] < 0:
                    player.resistance[i.__name__] = 0
            player.druguse += 1
            player.severity += 0.01

    class DrugStomach(Item):
        id = 305
        name = '胃药'
        kind = '普通药物'
        maxCd = 1
        maxDu = 280
        reuse = False
        isUnique = False
        info = '移除1~2层饱腹，并提升食物的回复效果，当恢复效果无法再提升时没有效果。'
        p=0.2

        def useItemAction(self, player):
            r = 6 + int(player.fooduse / 10)
            if player.fooduse <= r:
                r = player.fooduse
            player.fooduse -= r
            player.druguse += 2
            if r > 0:
                Notice.add('恢复了%s%s食物的恢复效果！' % (r * 0.3, '%'))
            else:
                Notice.add('没有恢复食物的恢复效果。')
            player.severity += 0.01
            if Satiety.has(player):
                Satiety.subByType(player)
            if Satiety.has(player) and rra(player, 50):
                Satiety.subByType(player)


    class DrugAntibiotic(Item):
        id = 397
        name = '抗生素'
        kind = '普通药物'
        maxCd = 7
        maxDu = 280
        reuse = False
        isUnique = False
        info = '将生病转化为6层持续时间为1的过劳，未生病则提升严重程度。'
        p=0.3

        def useItemAction(self, player):
            if PhysPun.has:
                PhysPun.clearByType(player)
                PhysProb.add(player, 6)
                PhysProb.get(player).duration = 1
                player.severity += 0.02
            else:
                player.severity += 0.05
            player.druguse += 1


    class DrugAntidepressant(Item):
        id = 398
        name = '抗抑郁药'
        kind = '普通药物'
        maxCd = 7
        maxDu = 280
        reuse = False
        isUnique = False
        info = '将偏执转化为6层持续时间为1的焦虑，未生病则提升严重程度。'
        p=0.3

        def useItemAction(self, player):
            if MentPun.has:
                MentPun.clearByType(player)
                MentProb.add(player, 6)
                MentProb.get(player).duration = 1
                player.severity += 0.02
            else:
                player.severity += 0.05
            player.druguse += 1


    class DrugFake(Item):
        id = 399
        name = '安慰剂'
        kind = '普通药物'
        maxCd = 0
        maxDu = 280
        reuse = False
        isUnique = False
        info = '本身没有任何治疗作用。' 
        ad = '因患者对医生信任、患者叫自我暗示以及对某种药物疗效的期望等而起到镇痛、镇蘸或缓解症状的作用。'
        p=0.01
        
        def useItemAction(self, player):
            showNotice(['什么也没有发生。'])

    ####################################################################################################

    class BookBase(Item):

        def __init__(self, player):
            super(BookBase, self).__init__(player)
            self.progress = 0

        def checkAvailable(self, player):
            if not BookQuickReadEffect.has(player):
                return '书本只能在进行阅读日程时才可阅读！'
            if type(self).__name__ in player.itemcd:
                return '书本仍在冷却时间中！'
            return True

        def use(self, player):
            if self.checkAvailable(player) != True:
                Notice.add(self.checkAvailable(player))
            else:
                Notice.add('已速读书本：'+ type(self).name)
                player.itemcd[type(self).__name__] = type(self).maxCd 
                BookQuickReadEffect.subByType(player)
                self.readBook(player, 2)
            Notice.show()


        def getPrefixInfo(self, player):
            if not type(self).reuse:
                reuse_info = '使用后消耗  '
            else:
                reuse_info = ''

            if type(self).__name__ not in player.itemcd and self.progress == 0:
                cd_info = '未阅读  '
            elif type(self).__name__ not in player.itemcd and self.progress == 1:
                cd_info = '已阅读：50%  '
            else:
                cd_info = '下次可阅读时间：'+str(player.itemcd[type(self).__name__])+'天后  '

            return '数量：'+str(self.amounts)+ '\n' +reuse_info+'\n'+ cd_info

        def readBook(self, player, e=1):
            if rra(player, 50):
                ReadReward.add(player)
            self.progress += e
            if self.progress >= 2:
                self.progress = 0
                player.itemcd[type(self).__name__] = type(self).maxCd
                self.useItemAction(player)
                if type(self).reuse == False:
                    self.sub(player)


    class BookDefault(BookBase):
        id = 400
        name = '《泽尼的森林》'
        kind = '书本'
        maxCd = 14
        maxDu = -1
        isUnique = True
        info = '阅读本书籍将获得2~3层的良好的睡眠和精神的平复。\n当没有过劳时，额外获得1层良好的睡眠；当没有焦虑时，额外获得1层精神的平复。'
        ad = '“我想起自己在过去的人生旅途中失去的许多东西——蹉跎的岁月，死去或离去的人们，无可追回的懊悔。”'

        def useItemAction(self, player):
            PhysRezA.add(player, ra(player,2,3))
            MentRezB.add(player, ra(player,2,3))
            if not PhysProb.has(p):
                PhysRezA.add(player)
            if not MentProb.has(p):
                MentRezB.add(player)

    class BookWri(BookBase):
        id = 401
        name = '《于老师教我的写作技巧》'
        kind = '书本'
        maxCd = 14
        maxDu = -1
        isUnique = True
        info = '当写作素材层数不低于25层时，阅读本书籍获得额外10层写作素材，并使写作技巧大幅提升。\n\n获得长门的手稿。'
        ad = '“在写作之前，最好先花些时间在笔记本上设计人物，搜集情节，或者记下脑海中曾涌现过的东西，直到动笔的那一刻到来。”'
        bookEffect_ = BookWriEffect

        def useItemAction(self, player):
            if FixedInspiration.getstack(player) >= 25:
                type(self).bookEffect_.add(player)
                FixedInspiration.add(player, 10)
                ManuscriptChangmen.add(p)


    class BookConc(BookBase):
        id = 402
        name = '《海边的于秀爱》'
        kind = '书本'
        maxCd = 14
        maxDu = -1
        isUnique = True
        info = '阅读本书籍后，持续时间内过劳和焦虑不会因为层数过多而转化成生病和偏执。\n持续时间结束时，每有一层过劳和焦虑都会提升2点随机属性。'
        ad = '“于是我们领教了世界是何等凶顽，同时又得知世界也可以变得温存和美好。”'
        bookEffect_ = BookConcEffect

        def useItemAction(self, player):
            type(self).bookEffect_.add(player)

        def timeUpAction(self, player):
            s = 0

            for i in (PhysProb, MentProb):
                if i.has(player):
                    s += i.get(player).stacks
            if s != 0:
                for i in range(2*s):
                    temp = ra(player, 1, 3)
                    if temp==1:
                        player.working += 0.01
                    elif temp ==2:
                        player.writing += 0.01
                    else:
                        player.physical += 0.01
                


    class BookPhysPun(BookBase):
        id = 403
        name = '《呼吸训练》'
        kind = '书本'
        maxCd = 14
        maxDu = -1
        isUnique = True
        info = '拥有生病或受伤时，阅读本书籍随机延长对应状态的持续时间。\n提升对应状态的休息恢复效果，在此期间通过休息治愈生病或受伤时，降低5%的严重程度。'
        ad = '“保证呼吸道通畅，提升呼吸肌功能，促进排痰和痰液引流，以及加强气体交换效率……”'
        bookEffect_ = BookPhysPunEffect

        def useItemAction(self, player):
            for i in [PhysPun, Injured]:
                if i.has(player):
                    i.get(player).duration += rca(player, (1, 1, 1, 1, 1, 2, 2, 3))
                    type(self).bookEffect_.add(player)

    
    class BookQuickRead(BookBase):
        id = 404
        name = '《量子波动速读》'
        kind = '书本'
        maxCd = 14
        maxDu = -1
        isUnique = True
        info = '阅读本书籍后获得2层速读次数，拥有速读次数时阅读书籍不需要消耗回合，每速读一次消耗1次速读次数。'
        ad = '“1分钟可以看完10万字的书！”\n“闭着眼睛就能和书发生感应！”\n“不需要翻开书本就能理解书中内容！”'
        bookEffect_ = BookQuickReadEffect

        def useItemAction(self, player):
            type(self).bookEffect_.add(player, 2)



    class BookWor(BookBase):
        id = 405
        name = '《保持清醒的秘诀》'
        kind = '书本'
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = '阅读本书籍将根据已完成的工作量提升工作速度，已完成的工作量越多，获得的层数越多，持续时间2天。\n\n获得架构师的手稿。'
        ad = '“有效的思考是可以随着时间的推移而练习和发展的一个技能。当然，一切都始于心与脑的联系。”'
        bookEffect_ = BookWorEffect

        def useItemAction(self, player):
            completion = r2(player.achievedGoal / player.goal)
            type(self).bookEffect_.add(player, int(completion * 10))
            ManuscriptConstructor.add(player)


    class BookIns(BookBase):
        id = 406
        name = '《2001年的弹珠机》'
        kind = '书本'
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = '阅读本书籍后效果持续时间内每天起床时获得灵感，有小几率结束该效果。'
        ad = '“迟早要失去的东西并没有太多意义. 必失之物的荣光并非真正的荣光。”'
        bookEffect_ = BookInsEffect

        def useItemAction(self, player):
            type(self).bookEffect_.add(player)

    class BookLevi(BookBase):
        id = 407
        name = '《海神记》'
        kind = '书本'
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = '立刻刷新所有物品的冷却时间。\n\n获得利维坦的手稿。'
        ad = '“他曾经有很多名字：始源，深寂，永黑之蓝，涅柔斯，无名之游兽………但现在他只有一个名字，利维坦……”'

        def useItemAction(self, player):
            player.itemcd.clear()
            player.itemcd[type(self).__name__] = 14
            ManuscriptLevi.add(player)

    class BookSport(BookBase):
        id = 409
        name = '《阿斯卡隆之春》'
        kind = '书本'
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = '阅读本书籍后效果持续时间内进行运动类日程有几率提升身体素质，触发5次后结束效果。'
        ad = '“我正伫立于现实的边缘。你会想念我吗，如果我轻轻一跃？”'
        bookEffect_ = BookSportEffect

        def useItemAction(self, player):
            type(self).bookEffect_.add(player, 5)


    class BookWrite(BookBase):
        id = 410
        name = '《亚斯塔禄之冬》'
        kind = '书本'
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = '阅读本书籍后效果持续时间内进行写作类日程有几率提升写作技巧，触发5次后结束效果。'
        ad = '“呼吸吧，趁你还能呼吸的时候。”'
        bookEffect_ = BookWriteEffect

        def useItemAction(self, player):
            type(self).bookEffect_.add(player, 5)


    class BookCM(BookBase):
        id = 411
        name = '《城堡与莫梭提斯》'
        kind = '书本'
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = '阅读本书籍后效果持续时间内每天起床时减少严重度，同时有小几率结束该效果。\n\n获得帕索斯的手稿。'
        ad = '“永生从来就不是什么馈赠。”'
        bookEffect_ = BookCMEffect

        def useItemAction(self, player):
            type(self).bookEffect_.add(player)
            ManuscriptPathos.add(player)


    class BookMED(BookBase):
        id = 412
        name = '《药：绝望的解决手段》'
        kind = '书本'
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = '阅读本书籍后效果持续时间内进行工作类日程时有几率额外提升随机属性，提升5次后结束效果。\n\n获得'
        ad = '“我看向蔚蓝的天空，仿佛现在还是四五年前，我正趴在大学教室的最后一排桌子上，歪头看着窗户，对着和现在一样蓝的天空做着永远不会实现的白日梦。”'
        bookEffect_ = BookMEDEffect

        def useItemAction(self, player):
            type(self).bookEffect_.add(player, 5)


    class AMaverickLion(BookBase):
        id = 413
        name = '《一只特立独行的狮子》'
        kind = '书本'
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = '阅读本书籍后随机移除1~2个负面状态。\n\n负面状态包括：过劳，焦虑，生病，受伤，偏执，酸痛'
        ad = '“它们会自由自在地闲逛，饥则进行捕食渴则饮，春天来临时还要谈谈爱情。”'

        def useItemAction(self, player):
            l = list(filter(lambda x: type(x) in (PhysProb, PhysPun, MentProb, MentPun, Injured, Soreness), player.effects))
            if len(l)>0:
                rca(player, l).clearByType(player)
            if len(l)>1:
                l = list(filter(lambda x: type(x) in (PhysProb, PhysPun, MentProb, MentPun, Injured, Soreness), player.effects))
                if rra(player, 50):
                    rca(player, l).clearByType(player)

    class BookHeal(BookBase):
        id = 414
        name = '《神，我们，或所有的士兵》'
        kind = '书本'
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = '阅读本书籍后移除当前所有非永久的学识和增益，每个被移除的学识和增益都能恢复10点精神状态。'
        ad = '“明天王子就会来见他，守卫这样说。他知道这其实是什么意思，被圈养的生活将迎来终结，但他好像对此没有什么特别的情绪。”'

        def useItemAction(self, player):
            s = 0
            for i in list(filter(lambda x: x.duration>=0 and type(x).kind in ('学识','增益'), player.effects)):
                i.clearByType(player)
                s += 1
            if s>0:
                rec = r2(s * 10)
                player.mental += rec
                Notice.add('恢复了%s点精神状态！' % rec)

    class Bookdont(BookBase):
        id = 415
        name = '《不要读这本书》'
        kind = '书本'
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = '不要看这本书的简介不要看这本书的简介不要看这本书的简介不要看这本书的简介不要看这本书的简介不要看这本书的简介'
        ad = '不要看这本书的内容不要看这本书的内容不要看这本书的内容不要看这本书的内容不要看这本书的内容不要看这本书的内容不要看这本书的内容'

        def useItemAction(self, player):
            renpy.quit()

    class BookRisk(BookBase):
        id = 416
        name = '《失而复得》'
        kind = '书本'
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = '阅读本书籍后效果期间内消耗的精力越多，效果结束时降低的严重度越多，同时提升的工作能力越多。\n若消耗的精神状态低于100则获得2层焦虑。'
        ad = '我觉得，即使能够重新开始自己的人生，恐怕也还是走回老路。\n因为那便是我自身。\n我除了成为我自身别无选择。哪怕有更多的人弃我而去，或我弃更多的人而去，哪怕五彩缤纷的感情，出类拔萃的素质和对未来的企盼受到限制以至消失，我也只能成为我自身，还有别的可能吗？'
        bookEffect_ = BookRiskEffect

        def useItemAction(self, player):
            type(self).bookEffect_.add(player)

    class BookRisk(BookBase):
        id = 417
        name = '《世界之终与冷漠之城》'
        kind = '书本'
        maxCd = 21
        maxDu = -1  # 数字
        isUnique = True
        info = '阅读本书籍后获得状态：存在感。'
        ad = '“我要坐在有阳光的地方，像猫舔奶碗那样一字不漏地把报纸上下看遍左右看遍，然后把世人在阳光下开展的各种生之片段吸入体内，滋润每一个细胞。”'
        bookEffect_ = Novice

        def useItemAction(self, player):
            Novice.add(player)
            Novice.get(player).duration = 2


    class ManuscriptLevi(Item):
        id = 450
        name = '利维坦的手稿'
        kind = '手稿'
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = False
        reuse = False
        info = '阅读本手稿后延长所有学识和增益的持续时间1天。'
        ad = '“……然而，尽管利维坦已然离去，但当海啸摧毁城池，淹没陆地，在人们的恐惧和敬畏中总会诞生新的海神。”'

        def useItemAction(self, player):
            for i in list(filter(lambda x: type(x).kind in ('学识', '增益'), player.effects)):
                if i.get(player).duration >= 0:
                    i.get(player).duration += 1

    
    class ManuscriptConstructor(Item):
        id = 451
        name = '架构师的手稿'
        kind = '手稿'
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = False
        reuse = False
        info = '阅读本手稿后立刻完成20%的当前已完成工作。'
        ad = '{color=#ff0000}Exception in thread "main" java.lang.StackOverflowError{/color}'

        def useItemAction(self, player):
            player.achievedGoal += r2(player.achievedGoal * 0.2)


    class ManuscriptChangmen(Item):
        id = 452
        name = '长门的手稿'
        kind = '手稿'
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = False
        reuse = False
        info = '阅读本手稿后将灵感的持续时间延长3天，如果没有灵感则没有效果。'
        ad = '“人生是旷野，不是轨道，我有权拒绝一种生活。”'

        def useItemAction(self, player):
            if Inspiration.has(p):
                Inspiration.get(p).duration += 3


    class ManuscriptPathos(Item):
        id = 453
        name = '帕索斯的手稿'
        kind = '手稿'
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = False
        reuse = False
        info = '阅读本手稿后延长当前所有种类的药物依赖状态的持续时间1~2天，并降低5%已经使用过的药物的抗药性。'
        ad = '至少他的字写得很漂亮……想在上面射精……'

        def useItemAction(self, player):
            for i in player.usedMedicines:
                if i.d_.has(player):
                    i.d_.get(player).duration += ra(player, 1, 2)
                player.resistance[i.__name__] -= 5



    class ProfessionalBookWorking(BookBase):
        id = 497
        name = '计算机科学专业书籍'
        kind = '书本'
        maxCd = 7
        maxDu = -1  # 数字
        reuse = False
        isUnique = False
        info = '阅读本书籍后随机提升工作能力并消耗该书，永久提升2%的工作速度，并获得状态：专注度提升。'
        ad = '数据结构、设计模式，软件架构，程序测试，操作系统，计算机组成原理……'

        def useItemAction(self, player):
            g = rca(player, (1,2,2, 3, 3, 4))
            player.working += g * 0.01
            Notice.add('提升了%s点工作能力。' % g)
            FocusAttention.add(player,2)
            player.workSpeed += 0.02

    class ProfessionalBookWriting(BookBase):
        id = 498
        name = '文字运用专业书籍'
        kind = '书本'
        maxCd = 7
        maxDu = -1  # 数字
        reuse = False
        isUnique = False
        info = '阅读本书籍后随机提升写作技巧并消耗该书，永久提升2%的专注度，并获得3层灵感。'
        ad = '虽然都是些老掉牙的写法，看这些还不如去读点别人写的小说。'

        def useItemAction(self, player):
            g = rca(player, (1,2,2, 3, 3,4))
            player.writing += g * 0.01
            Notice.add('提升了%s点写作技巧。' % g)
            Inspiration.add(player, 3)
            player.workConcentration += 2

    class ProfessionalBookSeverity(BookBase):
        id = 499
        name = '心理学专业书籍'
        kind = '书本'
        maxCd = 7
        maxDu = -1  # 数字
        reuse = False
        isUnique = False
        info = '阅读本书籍后随机降低严重程度并消耗该书，永久降低2%的严重度倍率，并大概率获得数层精神的释放和精神的平复。'
        ad = '测测你是哪种人格？是NTXL！'

        def useItemAction(self, player):
            g = rca(player, (1,2,2, 3, 3,4))
            player.severity -= g * 0.01
            Notice.add('降低了%s点严重程度。' % g)
            if rra(player, 75):
                MentRezA.add(player, rca(player,(1, 1, 2)))
            if rra(player, 75):
                MentRezB.add(player, rca(player,(1, 1, 2)))
            player.severityRegarded -= 0.02

    


    ##################################################################################################################

    class AppleJuice(Item):
        id = 200
        name = '苹果汽水'
        kind = '食物'
        maxCd = 0
        maxDu = 28
        reuse = False
        isUnique = False
        info = '使用后恢复少量精神状态并获得增益：苹果口味'
        ad = '“亚斯塔禄牌苹果汽水，比同类品牌产品多添加20%纯果汁！”'

        def useItemAction(self, player):
            rec = r2(10 * player.useFoodScale())
            Notice.add('恢复了%s点精神状态！' % rec)
            player.mental += rec
            AppleFlavor.add(player)
            player.fooduse += 1


    class CitrusJuice(Item):
        id = 201
        name = '橘子汽水'
        kind = '食物'
        maxCd = 0
        maxDu = 28
        reuse = False
        isUnique = False
        info = '使用后恢复少量精神状态并获得增益：柑橘口味'
        ad = '“阿斯卡隆牌橘子汽水，喝到就是赚到！”'

        def useItemAction(self, player):
            rec = r2(10 * player.useFoodScale())
            Notice.add('恢复了%s点精神状态！' % rec)
            player.mental += rec
            CitrusFlavor.add(player)
            player.fooduse += 1


    class Cola(Item):
        id = 202
        name = '罐装可乐'
        kind = '食物'
        maxCd = 1
        maxDu = 28
        reuse = False
        isUnique = False
        info = '使用后获得状态：集中注意力，并刷新本日的随机状态。\n（睡意，兴奋，紧张，放松）'
        ad = '“The choice of a new generation.”'

        def useItemAction(self, player):
            for i in list(filter(lambda x: type(x) in (ConsDec, ConsInc, ConcDec, ConcInc), player.effects)):
                i.clearByType(player)

            pool = (0,0,0,0,0,0,0,0,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,5) # 0:33.3%  1:12.5%  2:20.8%  3:16.6%  4:12.5%  5:4.6%

            if rra(player, 45):
                ConsInc.add(player, rca(player, pool))
            else:
                ConsDec.add(player, rca(player, pool))

            if rra(player, 45):
                ConcDec.add(player, rca(player, pool))
            else:
                ConcInc.add(player, rca(player, pool))

            player.fooduse += 1
            FocusAttention.add(player)


    class ToastFood(Item):
        id = 203
        name = '厚蛋吐司'
        kind = '食物'
        maxCd = 1
        maxDu = 1
        reuse = False
        isUnique = False
        info = '使用后恢复精神状态，移除2层紧张，但会降低食物的恢复效果。'
        ad = '外脆里嫩，鲜香不腻，不过高筋面粉一定要过筛。'

        def useItemAction(self, player):
            rec = r2(6 * player.useFoodScale())
            Notice.add('恢复了%s点精神状态！' % rec)
            player.mental += rec
            player.fooduse += 3
            Notice.add('降低了0.9%食物的恢复效果！')
            if ConsInc.has(player):
                ConsInc.subByType(p, 2)

    class CoffeeFood(Item):
        id = 204
        name = '咖啡'
        kind = '食物'
        maxCd = 0
        maxDu = 2
        reuse = False
        isUnique = False
        info = '获得1~2层兴奋，2层失眠。'
        ad = '又苦又难喝，但是能让人打起精神。'

        def useItemAction(self, player):
            Caffeine.add(player, 2)
            ConcInc.add(player, ra(player, 1,2))

    class SaladFood(Item):
        id = 205
        name = '时蔬沙拉'
        kind = '食物'
        maxCd = 1
        maxDu = 1
        reuse = False
        isUnique = False
        info = '使用后恢复精神状态，有概率提升身体素质，有概率提升食物的恢复效果。'
        ad = '膳食指南推荐一般建议每天摄入300-500g、至少5种以上的蔬菜……'

        def useItemAction(self, player):
            rec = r2(5 * player.useFoodScale())
            Notice.add('恢复了%s点精神状态！' % rec)
            player.mental += rec
            player.fooduse += 1
            if rra(player, 30):
                Notice.add('提升了1点身体素质！')
                player.physical += 0.01
            if rra(player, 40):
                Notice.add('提升了0.6%食物的恢复效果！')
                player.fooduse -= 2

    class PizzaFood(Item):
        id = 206
        name = '香肠披萨'
        kind = '食物'
        maxCd = 1
        maxDu = 1
        reuse = False
        isUnique = False
        info = '使用后恢复精神状态，获得状态：专注度提升，但会降低食物的恢复效果。'
        ad = '上等的披萨必须具备四个特质：新鲜饼皮、上等芝士、奶酪、顶级比萨酱和新鲜的馅料……'

        def useItemAction(self, player):
            rec = r2(8 * player.useFoodScale())
            Notice.add('恢复了%s点精神状态！' % rec)
            player.mental += rec
            player.fooduse += 3
            Notice.add('降低了0.9%食物的恢复效果！')
            if rra(player, 50):
                Satiety.add(player)
            FocusAttention.add(p)
                

    class BurgerFood(Item):
        id = 207
        name = '牛肉汉堡'
        kind = '食物'
        maxCd = 1
        maxDu = 1
        reuse = False
        isUnique = False
        info = '使用后恢复较多的精神状态。'
        ad = '热熔芝士yyds！芝士与牛肉饼完美融合，浓香四溢的完美升级！'

        def useItemAction(self, player):
            rec = r2(17 * player.useFoodScale())
            Notice.add('恢复了%s点精神状态！' % rec)
            player.mental += rec
            player.fooduse += 1
            if rra(player, 60):
                Satiety.add(player)

    class BreadFood(Item):
        id = 208
        name = '凯撒面包'
        kind = '食物'
        maxCd = 1
        maxDu = 1
        reuse = False
        isUnique = False
        info = '使用后恢复精神状态，并降低严重程度。'
        ad = '规定斜切必须要有5道裂口才算标准的长条面包！'

        def useItemAction(self, player):
            rec = r2(10 * player.useFoodScale())
            Notice.add('恢复了%s点精神状态！' % rec)
            player.mental += rec
            player.fooduse += 1
            Notice.add('降低了1点严重程度！')
            player.severity -= 0.01
            if rra(player, 25):
                Satiety.add(player)

    class PastaFood(Item):
        id = 209
        name = '黑椒意面'
        kind = '食物'
        maxCd = 1
        maxDu = 1
        reuse = False
        isUnique = False
        info = '使用后恢复精神状态，提升全部属性或移除1层过劳。'
        ad = '非常的新鲜，非常的美味。'

        def useItemAction(self, player):
            rec = r2(17 * player.useFoodScale())
            Notice.add('恢复了%s点精神状态！' % rec)
            player.mental += rec
            player.fooduse += 1
            if rra(player, 40):
                Satiety.add(player)
            if rra(player, 30):
                player.physical += 0.01
                player.writing += 0.01
                player.working += 0.01
                Notice.add('全部属性提升了1点！')

    class SoupFood(Item):
        id = 210
        name = '鲑鱼靓汤'
        kind = '食物'
        maxCd = 1
        maxDu = 1
        reuse = False
        isUnique = False
        info = '使用后恢复精神状态，提升写作技巧或获得1层精神的平复。'
        ad = '“现在，它早已死了，只是眼里还闪着一丝诡异的光。”'

        def useItemAction(self, player):
            rec = r2(17 * player.useFoodScale())
            Notice.add('恢复了%s点精神状态！' % rec)
            player.mental += rec
            player.fooduse += 1
            if rra(player, 60):
                Satiety.add(player)
            if rra(player, 85):
                if rra(player, 70):
                    player.writing += 0.01
                    Notice.add('写作技巧提升了1点！')
                else:
                    player.writing += 0.02
                    Notice.add('写作技巧提升了2点！')
            else:
                MentRezB.add(p)

    class SteakFood(Item):
        id = 211
        name = '战斧牛排'
        kind = '食物'
        maxCd = 1
        maxDu = 1
        reuse = False
        isUnique = False
        info = '使用后恢复巨量精神状态并获得状态：饱腹。'
        ad = '家庭聚会一定要点这道菜，比惠灵顿还哇塞。一个人吃？咋不撑死你呢？'

        def useItemAction(self, player):
            rec = r2(40 * player.useFoodScale())
            Notice.add('恢复了%s点精神状态！' % rec)
            player.mental += rec
            player.fooduse += 1
            Satiety.add(player, 3)
            Satiety.get(player).duration = 1

    class StreetFood1(Item):
        id = 212
        name = '一袋糖炒板栗'
        kind = '食物'
        maxCd = 1
        maxDu = 1
        reuse = False
        isUnique = False
        info = '使用后恢复精神状态，永久大幅度提升食物效果。'
        ad = '大多数人都喜欢购买的餐后小零食，也可以当做一顿不怎么管饱的午饭，香味飘散在空气中极易引发食欲。\n不过吃多了可不太妙，你不准备再花更多的钱去看牙齿。'

        def useItemAction(self, player):
            rec = r2(5 * player.useFoodScale())
            Notice.add('恢复了%s点精神状态！' % rec)
            player.mental += rec
            player.fooduse -= 10
            Notice.add('提升了3%食物的恢复效果！')

    class StreetFood2(Item):
        id = 213
        name = '油炸小酥肉'
        kind = '食物'
        maxCd = 0
        maxDu = 2
        reuse = False
        isUnique = False
        info = '使用后恢复精神状态。'
        ad = '似乎是一家网红小吃店的招牌，手机里到处是它的广告，同样在各种测评里时常出现它的身影。\n看上去金黄酥脆，但是谁知道是不是地沟油做的呢？'

        def useItemAction(self, player):
            rec = r2(7 * player.useFoodScale())
            Notice.add('恢复了%s点精神状态！' % rec)
            if rra(player, 25):
                Satiety.add(p)
            player.mental += rec
            player.fooduse +=1

    class StreetFood3(Item):
        id = 214
        name = '冰雪蜜城'
        kind = '食物'
        maxCd = 1
        maxDu = 1
        reuse = False
        isUnique = False
        info = '使用后恢复精神状态，降低严重性，永久提升食物效果。'
        ad = '谁不喜欢价格亲民又冰爽解渴的柠檬水呢？正值酷暑的大街上极其需要一倍冰冰凉的柠檬水帮你消消暑。\n冰冰凉凉还好喝，但是冷热交加容易胃疼。'

        def useItemAction(self, player):
            rec = r2(3 * player.useFoodScale())
            Notice.add('恢复了%s点精神状态！' % rec)
            player.mental += rec
            player.severity -= 0.02
            Notice.add('降低了2点严重程度！')
            player.fooduse -= 3
            Notice.add('提升了0.9%食物的恢复效果！')

    class StreetFood4(Item):
        id = 215
        name = '插着木签的菠萝片'
        kind = '食物'
        maxCd = 0
        maxDu = 1
        reuse = False
        isUnique = False
        info = '使用后随机提升或降低严重度，概率提升食物的恢复效果。'
        ad = '新鲜的小菠萝，店家特地用盐水洗过一遍的削皮新鲜水果，酸中带甜，可是总会有汁水溅在衣服上。\n当然，最难过的是菠萝会塞牙，祝你好运。'

        def useItemAction(self, player):
            if rra(player, 60):
                player.severity -= 0.01
                Notice.add('降低了1点严重程度！')
            else:
                player.severity += 0.01
                Notice.add('提升了1点严重程度！')
            if rra(player, 60):
                player.fooduse -= 2
                Notice.add('提升了0.6%食物的恢复效果！')

    class StreetFood5(Item):
        id = 216
        name = '冰美式'
        kind = '食物'
        maxCd = 1
        maxDu = 3
        reuse = False
        isUnique = False
        info = '使用后获得2~3层兴奋，0~1层失眠，永久提升食物恢复的效果。'
        ad = 'A市的人喝咖啡，像进行一场不需要规则的游戏，随性放任，百无禁忌。'

        def useItemAction(self, player):
            player.fooduse -= 3
            ConcInc.add(player)
            ConcInc.add(player, ra(player, 2, 3))
            if rra(player, 40):
                Caffeine.add(player)

    class StreetFood6(Item):
        id = 217
        name = '生椰拿铁'
        kind = '食物'
        maxCd = 1
        maxDu = 3
        reuse = False
        isUnique = False
        info = '使用后获得1层兴奋和2层紧张，降低2点严重程度，0~1层失眠。'
        ad = '“我不在咖啡馆，就在去咖啡馆的路上。”'

        def useItemAction(self, player):
            ConcInc.add(player, 2)
            ConsInc.add(player, ra(player, 1, 2))
            player.severity -= 0.02
            Notice.add('降低了2点严重程度！')
            if rra(player, 40):
                Caffeine.add(player)

    class StreetFood7(Item):
        id = 218
        name = '摩卡咖啡'
        kind = '食物'
        maxCd = 1
        maxDu = 3
        reuse = False
        isUnique = False
        info = '使用后获得2层放松，降低2点严重程度，3层失眠。'
        ad = '让爱恋中的人们了解爱情的甜美和波折，为了告诉我们幸福的简单。'

        def useItemAction(self, player):
            player.severity -= 0.02
            Caffeine.add(player, 3)
            Notice.add('降低了2点严重程度！')
            ConsDec.add(player, 2)

    class StreetFood8(Item):
        id = 219
        name = '奇怪的红茶'
        kind = '食物'
        maxCd = 1
        maxDu = 2
        reuse = False
        isUnique = False
        info = '使用后获得2层睡意。'
        ad = '在你拜访你最喜欢的朋友的家时，可以分享给他品尝，不过要提前问好几分钟后会不会有人敲门。'

        def useItemAction(self, player):
            ConcDec.add(player, 2)

    class StreetFood9(Item):
        id = 220
        name = '天然矿泉水'
        kind = '食物'
        maxCd = 1
        maxDu = 7
        reuse = False
        isUnique = False
        info = '使用后提升1点随机属性。'
        ad = '“添加了一整个元素周期表的微量元素，纯天然矿物质水就选于秀爱牌天然矿泉水。”'

        def useItemAction(self, player):
            temp = rd(1,3)
            if temp == 1:
                player.working += 0.01
            elif temp == 2:
                player.physical += 0.01
            else:
                player.writing += 0.01

    
    class StreetFood10(Item):
        id = 221
        name = '泡面'
        kind = '食物'
        maxCd = 0
        maxDu = 90
        reuse = False
        isUnique = False
        info = '使用后恢复精神状态，有概率获得饱腹同时降低食物的恢复效果。'
        ad = '某种意义上的硬通货。'

        def useItemAction(self, player):
            rec = r2(10 * player.useFoodScale())
            Notice.add('恢复了%s点精神状态！' % rec)
            player.mental += rec
            if rra(player, 60):
                Satiety.add(player)
                player.fooduse += 4
                Notice.add('降低了1.2%食物的恢复效果！')

    class Alcohol(Item):
        id = 222
        name = '梅子酒'
        kind = '食物'
        maxCd = 1
        maxDu = 90
        reuse = False
        isUnique = False
        info = '使用后消耗50%的精神状态，低于0时固定降低100点。\n获得2层睡意，2层放松和3层灵感，并提升严重程度。'
        ad = '“吾身为火，烧尽那些敢于眷恋我的勇者。”'

        def useItemAction(self, player):
            if player.mental < 0:
                player.mental -= 100 * f()
            else:
                player.mental = r2(0.5 * player.mental)
            player.severity += 0.02
            ConcDec.add(player, 2)
            ConsDec.add(player, 2)
            Inspiration.add(player, 3)

    class Cigarette(Item):
        id = 223
        name = '香烟'
        kind = '食物'
        maxCd = 0
        maxDu = 280
        reuse = False
        isUnique = False
        info = '使用后消耗20%的精神状态，低于0时固定降低100点。\n获得1层灵感，30%的专注度提升和20%~30%+难耐层数*10%的严重程度降低，进行日程有大概率消耗该增益。\n近期抽过烟使用将不会获得更多效果，同时还会提升严重度。'
        ad = '抽烟的人通常短命，它和我算是绝配。'

        def useItemAction(self, player):
            if player.mental < 0:
                player.mental -= 100 * f()
            else:
                player.mental = r2(0.8 * player.mental)
            if Entrance.has(player):
                player.severity += 0.02
            else:
                Inspiration.add(player)
                s = 0
                if Smoking.has(player):
                    s += Smoking.get(player).stacks
                Entrance.add(player, ra(player, 2, 3)+s)
    

    ########################################################################################

    class HallukeItem1(Item):
        id = 500
        name = '{color=#FFD700}Halluke的旧护膝{/color}'
        kind = '收藏品'
        maxCd = -1
        maxDu = -1  # 数字
        isUnique = True
        info = '身体素质+15%。\n获得身体素质时额外获得1点。\n体魄恢复的精神状态+20%。\n体魄消失的概率-50%。'
        ad = '对他来说正好的护膝在你腿上就有些稍紧了，不过无论如何，都是从他身上换下来的装备，这种膝部的包裹感使你在在运动时回忆起他运动时的身影。'

        def enableAction(self, player):
            player.physicalRegarded += 0.15
            player.physicalGain += 0.01

        def disableAction(self, player):
            player.physicalRegarded -= 0.15
            player.physicalGain -= 0.01


    class Sticker59(Item):
        id = 600
        name = '59号贴纸'
        kind = '收藏品'
        maxCd = -1
        maxDu = -1
        isUnique = True
        info = '全部属性提升了。'  # 普通结局获得 持有本收藏品可进入真结局
        ad = '白色的方形贴纸，中央打印着黑色的数字59，你似乎十分熟悉这个数字，但又完全回忆不起来。'

        def enableAction(self, player):
            player.workingRegarded += 0.05
            player.writingRegarded += 0.05
            player.physicalRegarded += 0.05

        def disableAction(self, player):
            player.workingRegarded -= 0.05
            player.writingRegarded -= 0.05
            player.physicalRegarded -= 0.05


    class AppleJuiceSticker(Item):
        id = 601
        name = '苹果汽水标签'
        kind = '收藏品'
        maxCd = -1
        maxDu = -1
        isUnique = True
        info = '在商店中解锁可购买道具：苹果汽水。'  # 真结局获得
        ad = '红色的标签上打印着夸张的字体，是？？？喜欢喝的汽水品牌。'

    class AppleJuiceSticker(Item):
        id = 602
        name = '橘子汽水标签'
        kind = '收藏品'
        maxCd = -1
        maxDu = -1
        isUnique = True
        info = '在商店中解锁可购买道具：橘子汽水。'  # 真结局获得
        ad = '橙色的标签上打印着夸张的字体，是？？？喜欢喝的汽水品牌。'


    class ExaminationReport(Item):
        id = 603
        name = 'A市医院体检报告单'
        kind = '收藏品'
        maxCd = -1
        maxDu = -1
        isUnique = True
        info = '购买药物的消费降低10%。'  # 治愈结局获得 不写效果了到时候直接用has查
        ad = '上面记录着你所有的标准体检报告内容，医师结语为一切正常，但你仍被痛苦困扰着。'

    class PlaceboBottle(Item):
        id = 604
        name = '空的安慰剂药瓶'
        kind = '收藏品'
        maxCd = -1
        maxDu = -1
        isUnique = True
        info = '大幅提升药物的治疗效果，因为你相信。'  # 安慰剂结局获得
        ad = '骗子不仅需要具备欺骗他人的能力，更要懂得欺骗自己的内心。'

        def enableAction(self, player):
            player.drugRecovery += 0.2

        def disableAction(self, player):
            player.drugRecovery -= 0.2

    
    class PathosDoll(Item):
        id = 605
        name = '黑色狮子玩偶'
        kind = '收藏品'
        maxCd = -1
        maxDu = -1
        isUnique = False
        info = '物品仅有收藏价值。'
        ad = '这东西太几把难夹到了。'


    class BadmintonRacket(Item):
        id = 610
        name = '羽毛球拍'
        kind = '收藏品'
        maxCd = -1
        maxDu = 28  # 数字
        isUnique = True
        info = '身体素质百分比提升。'
        ad = '普通的球拍，对你来说使用起来十分顺手。'

        def enableAction(self, player):
            player.physicalRegarded += 0.05

        def disableAction(self, player):
            player.physicalRegarded -= 0.05


    class Humidifier(Item):
        id = 611
        name = '小型加湿器'
        kind = '收藏品'
        maxCd = -1
        maxDu = 44  # 数字
        isUnique = True
        info = '降低睡眠消耗的精神状态。'
        ad = '桶面造型的加湿器，让你在干燥的夜晚入眠。'

        def enableAction(self, player):
            player.deteriorateConsumption += 0.15

        def disableAction(self, player):
            player.deteriorateConsumption -= 0.15


    class MusicBox(Item):
        id = 612
        name = '八音盒'
        kind = '收藏品'
        maxCd = -1
        maxDu = 28  # 数字
        isUnique = True
        info = '每日有概率降低严重程度。'
        ad = '转动发条便可以周而复始地播放一首十分经典的名为《Myosotis》的曲目。'

        def afterSleepAction(self, player):
            if not self.broken:
                if rra(player, 45):
                    player.severity -= 0.01
                    Notice.add('由于八音盒，降低了1点严重程度。')


    class ClockTower(Item):
        id = 613
        name = '钟塔摆件'
        kind = '收藏品'
        maxCd = -1
        maxDu = 28  # 数字
        isUnique = True
        info = '起床后随机恢复少量精神状态。'
        ad = '小巧精致的钟塔模型，据说是还原了已经失落的国家“阿斯卡隆”的建筑风格制成的。'

        def afterSleepAction(self, player):
            if not self.broken:
                r = ra(player, 5, 10)
                Notice.add('由于钟塔摆件，恢复了%s点精神状态。' % r)
                player.mental += r



    class GymTicket(Item):
        id = 614
        name = '健身房的有效会员卡'
        kind = '收藏品'
        maxCd = -1
        maxDu = 1
        isUnique = True
        info = '持有有效的会员卡可以进入健身房，仅本日有效。'
        ad = 'Topaz健身房的会员卡，上面印有琥珀色的logo。'

        def timeUpAction(self, player):
            GymBrokenTicket.add(player)
            self.remove(p)

    class GymBrokenTicket(Item):
        id = 615
        name = '健身房的无效会员卡'
        kind = '收藏品'
        maxCd = -1
        maxDu = -1
        isUnique = False
        info = '物品仅有收藏价值。'
        ad = 'Topaz健身房的会员卡，上面印有琥珀色的logo。'

    class WriterProof(Item):
        id = 616
        name = '金牌作者证明'
        kind = '收藏品'
        maxCd = -1
        maxDu = -1
        isUnique = True
        info = '严重度百分比降低，收到的委托更容易出现更高的价格修正。'
        ad = '写作平台的作者证明，你的粉丝已经破万了，这是你不曾想过的。'

        def enableAction(self, player):
            player.severityRegarded -= 0.1

        def disableAction(self, player):
            player.severityRegarded += 0.1

    class VipCard(Item):
        id = 617
        name = '夜店Vip卡'
        kind = '收藏品'
        maxCd = -1
        maxDu = -1
        isUnique = False
        info = '物品仅有收藏价值。'
        ad = '上面写着一家名为“Endorphins”的男同酒吧地址以及详细信息，联系方式是……\n谁会想去这种地方啊！而且我为什么要收集这东西啊！'

    class SexyPic(Item):
        id = 618
        name = '色情照片'
        kind = '收藏品'
        maxCd = 1
        maxDu = -1
        isUnique = False
        reuse = False
        info = '使用后获得状态：勃起'
        ad = '知名男演员于秀爱的色情写真，照片里的他裸体坐在白色的大床中央，双手向后支撑身体，而身边则围绕一群肌肉雄兽……\n我焯太烧辣，我不行了，兄弟们我先冲啦！'

        def useItemAction(self, player):
            Erection.add(player)

    class TomatoBrooch(Item):
        id = 620
        name = '番茄胸针'
        kind = '收藏品'
        maxCd = -1
        maxDu = -1
        isUnique = True
        info = '获取时降低3%的严重性，丢弃时增加6%的严重性。'
        ad = '十分漂亮，但胸针如果放在衣服上又太张扬，放在包上又很容易被蹭掉或者偷走……总之还是放在抽屉里最安全……'

        def enableAction(self, player):
            player.severity = r2(player.severity * 0.97)

        def disableAction(self, player):
            player.severity = r2(player.severity * 1.06)
        

    class PaperStar(Item):
        id = 621
        name = '千纸鹤'
        kind = '收藏品'
        maxCd = 1
        maxDu = -1
        isUnique = False
        reuse = False
        info = '使用后有概率获得灵感，未获得则恢复少量精神状态。'
        ad = '真的有人会折这东西折几千个吗？'

        def enableAction(self, player):
            if rra(player, 30):
                Inspiration.add(player)
            else:
                r = ra(player, 2, 7)
                Notice.add('由于千纸鹤，恢复了%s点精神状态。' % r)
                player.mental += r

    
    class Flower1(Item):
        id = 622
        name = '一束木兰'
        kind = '收藏品'
        maxCd = -1
        maxDu = 5
        isUnique = True
        info = '持有时，百分比降低严重程度。'
        ad = '花语：高尚的灵魂。'

        def enableAction(self, player):
            player.severityRegarded -= 0.1
        
        def disableAction(self, player):
            player.severityRegarded += 0.1

    
    class Flower2(Item):
        id = 623
        name = '一把勿忘我'
        kind = '收藏品'
        maxCd = -1
        maxDu = 5
        isUnique = True
        info = '持有时，每天结束后有概率获得1层灵感。'
        ad = '花语：请不要忘记我真诚的爱。'

        def afterSleepAction(self, player):
            if not self.broken:
                if rra(player, 60):
                    Inspiration.add(player)

    
    class Flower3(Item):
        id = 624
        name = '一捧万寿菊'
        kind = '收藏品'
        maxCd = -1
        maxDu = 5
        isUnique = True
        info = '持有时，每天结束后有概率移除一层焦虑。'
        ad = '花语：健康长寿。'

        def afterSleepAction(self, player):
            if not self.broken:
                if rra(player, 70):
                    PhysProb.subByType(player)
                    MentProb.subByType(player)

    
    class Sneakers(Item):
        id = 625
        name = '运动鞋'
        kind = '收藏品'
        maxCd = -1
        maxDu = 14  # 数字
        isUnique = True
        info = '身体素质百分比提升。'
        ad = '普通的运动鞋，至少你不用穿休闲鞋去打羽毛球了。'

        def enableAction(self, player):
            player.physicalRegarded += 0.05

        def disableAction(self, player):
            player.physicalRegarded -= 0.05

    class FileFolder(Item):
        id = 626
        name = '档案夹套装'
        kind = '收藏品'
        maxCd = -1
        maxDu = 14  # 数字
        isUnique = True
        info = '工作能力百分比提升。'
        ad = '一大堆五颜六色的档案夹，可以分类各种各样的纸质数据。'

        def enableAction(self, player):
            player.workingRegarded += 0.05

        def disableAction(self, player):
            player.workingRegarded -= 0.05

    
    class NotePad(Item):
        id = 627
        name = '记事本'
        kind = '收藏品'
        maxCd = -1
        maxDu = 14  # 数字
        isUnique = True
        info = '工作能力百分比提升。'
        ad = '包装精美的记事本，可以用来记录会议内容。'

        def enableAction(self, player):
            player.workingRegarded += 0.05

        def disableAction(self, player):
            player.workingRegarded -= 0.05


    class TicketRoot(Item):
        id = 697
        name = '票根'
        kind = '收藏品'
        maxCd = -1
        maxDu = -1
        isUnique = False
        info = '物品仅有收藏价值。'
        ad = '一大堆花里胡哨的票根，火车票电影票游泳馆入场券展览馆入场券应有尽有。'


    '''
    class OldClothes(Item):
        id = 698
        name = '旧衣服'
        kind = '收藏品'
        maxCd = -1
        maxDu = -1
        isUnique = False
        info = '物品仅有收藏价值。'
        ad = '堆在一起的旧衣服，你并不是很想丢掉，毕竟很多件衣服你一次都没穿过。'
    '''

    class Trash(Item):
        id = 699
        name = '杂物'
        kind = '收藏品'
        maxCd = -1
        maxDu = -1
        isUnique = False
        info = '物品仅有收藏价值。'
        ad = '心血来潮买的乱七八糟的小摆件，至少它们曾经让你开心过，或者没有，但那已经不重要了，现在你已经对它们失去了兴趣。'


    class UnfinishedCommission(Item):
        id = 700
        name = '未完成的文稿'
        kind = '文稿'
        maxCd = -1
        maxDu = -1
        isUnique = False
        info = ''

        def __eq__(self, other):
            return False

        def __init__(self, player):
            super(UnfinishedCommission, self).__init__(player)
            self.comm = Comm(player)

        def getPrincipalInfo(self):
            cInfo = self.comm.contentInfo()
            info1 = self.comm.commInfo()
            info2 = '\n\n已完成字数：'+str(cInfo[0])+'\n文稿总价值：'+str(cInfo[1])+'\n共消耗灵感：'+str(cInfo[2])

            return info1 + info2

        def write(self, player):
            cms = self.comm.write(player)
            player.items.append(cms)
            self.remove(player)


    class FinishedCommission(Item):
        id = 701
        name = '已完成的文稿'
        kind = '文稿'
        maxCd = -1
        maxDu = -1
        isUnique = False
        info = ''

        def __eq__(self, other):
            return False

        def __init__(self, player):
            super(FinishedCommission, self).__init__(player)
            self.comm = Comm(player)

        def getPrincipalInfo(self):
            cInfo = self.comm.contentInfo()
            info1 = self.comm.commInfo()
            info2 = '\n\n已完成字数：'+str(cInfo[0])+'\n文稿总价值：'+str(cInfo[1])+'\n共消耗灵感：'+str(cInfo[2])

            return info1 + info2

        def getReward(self, player):
            money = r2(self.comm.contentInfo()[1])
            ins = int(0.2 * self.comm.contentInfo()[2])

            player.money += money
            
            Notice.add('完成委托！')

            if money>0:
                Notice.add('获得了%s元报酬。' % money)
            else:
                Notice.add('未获得报酬！')

            if ins > 0:
                FixedInspiration.add(player, ins)
                Notice.add('获得了%s层写作素材！' % ins)
            else:
                Notice.add('未获得新的写作素材！')

            if not WriterProof.hasByType(player) and player.popularity >= 10000:
                Notice.add('由于您的粉丝数已经超过一万，平台特颁发作家证明，以资鼓励。')
                WriterProof.add(player)

            Notice.show()
            self.remove(player)

        def uploadToSocial(self, player):
            di = self.comm.contentInfo()[2]

            np = player.popularity/1000
            r = 0.5 * (di - 7)
            up = int(r * (np-np*np/100) * 120)

            ins = int(0.5 * (di-5))
            if player.popularity + up <= 1000 or player.popularity >= 40000:
                Notice.add('已将文稿发布到写作平台！\n平台没有新增粉丝。')
            elif up < 0:
                player.popularity += up
                Notice.add('已将文稿发布到写作平台！\n流失了%s个新粉丝。' % up)
            else:
                if up+player.popularity > 40000:
                    up = 40000 - player.popularity
                player.popularity += up
                Notice.add('已将文稿发布到写作平台！\n涨了%s个新粉丝。' % up)

            if ins > 0:
                FixedInspiration.add(player, ins)
                Notice.add('恢复了%s层灵感！' % ins)

            if not WriterProof.hasByType(player) and player.popularity >= 10000:
                Notice.add('由于您的粉丝数已经超过一万，平台特颁发作家证明，以资鼓励。')
                WriterProof.add(player)
            
            Notice.show()
            self.remove(player)
            

    def wr(p):
        Inspiration.add(p, 10)
        FreewheelingWriting.executeTask(p)
        Notice.show()