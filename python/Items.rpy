init -10 python early:

    class MedicineBase(Item):
        id = None
        name = None
        kind = _('实验药物')
        maxCd = 0
        maxDu = 8
        isUnique = False
        info = None
        reuse = False
        d_ = None
        w_ = None
        e_ = None

        @classmethod
        def getEffects(cls, player):
            return int(cls.getMedicineScale(player, True) * (cls.expectedReco(player) * 100 / 70))
        
        @classmethod
        def getMedicineEffects(cls, player):
            return int((cls.expectedReco(player) * 100 / 70))

        @classmethod
        def getlastuseinfo(cls, player):
            if cls in player.medinfo:
                return _('\n{color=#fde827}\n上次使用：%s（%s）\n过夜降低抗药性概率：%s%s\n过夜获得药物依赖概率：%s%s{/color}\n') % (player.medinfo[cls].time(), player.medinfo[cls].lastuse, r2(player.medinfo[cls].updateResistenceChance(player)), '%', r2(player.medinfo[cls].giveDependenceChance(player)), '%')
            return '\n'

        @classmethod
        def getBenefit(cls, player):
            ge = cls.getEffects(player)
            cl = '{color=#ffae00}'
            if ge < 67:
                cl = '{color=#FF4500}'
            if ge > 100:
                cl = '{color=#7CFC00}'
            return _('\n{font=DejaVuSans.ttf}• {/font}使用效率：%s%s%s{/color}') % (cl, ge, '%')

        @classmethod
        def getScale(cls, player, prev=True):
            scales = [1.0, 1.0, 1.0]
            for i in player.medinfo:
                if i == cls:
                    if player.medinfo[i].getInterval(player) == 0:
                        scales[0] *= 0.33
                        if not prev:
                            player.medinfo[cls].res += min(player.medinfo[cls].res + ra(player, 3, 5), 80)
                            Notice.add(_('升高了3点严重程度！'))
                            player.severity += 0.03
                    if player.medinfo[i].getInterval(player) == 1:
                        scales[1] *= 0.66
                        if not prev:
                            player.medinfo[cls].res += min(player.medinfo[cls].res + ra(player, 1, 3), 80)
                            Notice.add(_('升高了1点严重程度！'))
                            player.severity += 0.01
                else:
                    if player.medinfo[i].getInterval(player) == 0:
                        scales[2] *= 0.5
                        if not prev:
                            player.medinfo[cls].res += min(player.medinfo[cls].res + ra(player, 1, 3), 80)
                            Notice.add(_('升高了2点严重程度！'))
                            player.severity += 0.02
            return scales

        @classmethod
        def getResScale(cls, player):
            return (100 - cls.res(player)) * 0.01

        @classmethod
        def res(cls, player):
            if cls not in player.medinfo:
                return 0
            return player.medinfo[cls].res

        @classmethod
        def getinfo(cls, player):
            if not persistent.PreciseMedDisplay:
                return cls.getrecoveryinfo(player) + cls.getlastuseinfo(player)
            return _('预计恢复%s点精神状态。%s') % (cls.expectedReco(player), cls.getResInfo(player))

        @classmethod
        def getrecoveryinfo(cls, player):
            ge = cls.getEffects(player)
            cl = '{color=#ffae00}'
            if ge < 67:
                cl = '{color=#FF4500}'
            if ge > 100:
                cl = '{color=#7CFC00}'
            return _('预计恢复%s（%s%s%s{/color}）点精神状态。') % (cls.expectedReco(player), cl, ge, '%')

        @classmethod
        def getResInfo(cls, player):
            if not persistent.PreciseMedDisplay:
                return '\n'+cls.getBenefit(player)

            info = cls.getBenefit(player) + '\n'
            s = cls.getEffects(player)
            scales = cls.getScale(player)
            
            if cls.res(player) != 0:
                info += _('—抗药性：-%s%s\n') % (int(cls.res(player)), '%') 

            if scales[0] != 1:
                info += _('—刚刚使用过本实验药物：*%s%s\n') % (int(scales[0]*100), '%') 

            if scales[1] != 1:
                info += _('—近期使用过本实验药物：*%s%s\n') % (int(scales[1]*100), '%')  

            if scales[2] != 1:
                info += _('—刚刚使用过其他实验药物：*%s%s\n') % (int(scales[2]*100), '%') 

            if player.times == 0 and cls==MedicineA:
                info += _('{color=#fe6363}—早上服用：*%s%s{/color}\n') % (MedicineA.getMedicineEffects(player) ,'%') 

            if cls==MedicineB:
                info += _('{color=#7881e8}—该精神状态下服用：*%s%s{/color}\n') % (MedicineB.getMedicineEffects(player) ,'%') 

            if cls==MedicineC:
                info += _('{color=#e4f06f}—基础精神消耗加成效果：*%s%s{/color}\n') % (MedicineC.getMedicineEffects(player) ,'%') 

            if PlaceboBottle.has(player):
                info += _('—空的安慰剂药瓶：+20%\n') 

            if BookBanDepEffect.has(player):
                info += _('—常用药理学知识：+10%\n') 

            if GameModule1.has(player):
                info += _('—药物过敏：+15%\n') 

            return ('\n'+info).rstrip() + cls.getlastuseinfo(player)

        @classmethod
        def getMedicineScale(cls, player, prev=False):
            scale = 1.0
            scale *= cls.getResScale(player)
            scale *= player.drugRecovery  # 所有药物恢复效果
            
            scales = cls.getScale(player, prev)
            scale *= scales[0] * scales[1] * scales[2]

            if not prev:
                scale *= f()

            return r4(scale)

        def useItemAction(self, player):
            player.nousemed = 0

            if type(self) not in player.medinfo:  # 使用后将自身填进已经使用过的药物中
                player.medinfo[type(self)] = MedInfo(type(self))
            if self.d_.has(player):  # 移除对应的药物依赖
                self.d_.clearByType(player)
            if self.w_.has(player):  # 处理对应的戒断反应
                self.w_.get(player).afterDrug(player)

            if Despair.has(player):
                Despair.get(player).afterDrug(player)

            rec = self.recovery(player) * self.getMedicineScale(player)

            player.medinfo[type(self)].updateTime(player) # 更新药物使用时间

            Notice.add(_('使用了%s，恢复了%s点精神状态。') % (self.name, r2s(rec)))
            player.mental += r2(rec)

            if self.res(player) > 50:
                Notice.add(_('由于使用的药物抗药性过高，升高了2点严重程度！'))
                player.severity += 0.02
            
            if player.week < 3:
                resi = ra(player, 1, 2)
            elif player.week < 8:
                resi = ra(player, 2, 3)
            elif player.week < 12:
                resi = ra(player, 2, 4)
            elif player.week >= 12:
                resi = ra(player, 3, 4)

            player.medinfo[type(self)].res = min(player.medinfo[type(self)].res + resi, 80)
            self.e_.add(player)  # 添加药物作用

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
        name = _('药物{font=arial.ttf}α{/font}')
        kind = _('实验药物')
        info = _('移除药物依赖{font=arial.ttf}α{/font}以及戒断反应{font=arial.ttf}α{/font}，获得药物作用{font=arial.ttf}α{/font}。\n在起床时使用该药物时，恢复额外的精神状态。')
        d_ = DrugDA
        w_ = DrugWA
        e_ = DrugEA
        ad = _('“目前还不明确具体的使用频率，药物使用频率依你的头疼剧烈程度而定。我的建议是早上吃，等你头再疼的时候继续吃……另外一周后就不要再用上一周的过期药物了……”\n我的主治医师Pathos在我每次买药之前都会和我念叨一遍，我都听腻了，难道他真以为我是那种什么都记不住的三岁小孩吗？')

        @classmethod
        def recovery(cls, player, prev=False):
            rec = 70
            if player.times == 0 or player.times == 101:
                rec *= 1 + (0.4 + 0.02 * player.week)
                #Notice.add(_('在起床时使用，恢复了额外30%的精神状态。'))
            return rec


    class MedicineB(MedicineBase):
        id = 101
        name = _('药物{font=arial.ttf}β{/font}')
        kind = _('实验药物')
        info = _('移除药物依赖{font=arial.ttf}β{/font}以及戒断反应{font=arial.ttf}β{/font}，获得药物作用{font=arial.ttf}β{/font}。\n当前的精神状态越少，恢复的精神状态越多，低于阈值时恢复效果将大幅度下降。')
        d_ = DrugDB
        w_ = DrugWB
        e_ = DrugEB
        ad = _('“这种药只有在非常紧急的时候才能服用！因为目前了解的是这种药物服用之后会产生大量虚构的幻觉，以及各种尚不明确原因的效果……就算你喜欢这种幻觉，这药也不是为了让你当合法致幻剂用的！”\n为什么不能？写东西之前把这个丢进嘴里，灵感就会像泉水似的往外喷！')

        @classmethod
        def recovery(cls, player, prev=False):
  
            rec = (-0.6 - 0.04 * player.week) * max(-120*(1+0.1 * player.week), player.mental) + 70
            
            if rec < 20:
                rec = 20
                if prev==False:
                    Notice.add(_('因为使用该药物时精神状态过高，升高了2点严重程度！'))
                    player.severity += 0.02
            
            #Notice.add(_('恢复了相当于药物基础恢复量的') + r2s(s) + _('%的精神状态。'))
            return rec


    class MedicineC(MedicineBase):
        id = 102
        name = _('药物{font=arial.ttf}γ{/font}')
        kind = _('实验药物')
        info = _('移除药物依赖{font=arial.ttf}γ{/font}以及戒断反应{font=arial.ttf}γ{/font}，获得药物作用{font=arial.ttf}γ{/font}。\n单次服用恢复较少精神状态，但每次完成日程后都会恢复较多精神状态。\n基础精神状态消耗越多，恢复的越多。')
        d_ = DrugDC
        w_ = DrugWC
        e_ = DrugEC
        ad = _('“这种药物对肠胃影响很大，也会影响你的味觉，虽然瞬间的恢复效果一般，但是长远来看对你的头疼恢复效果还是要比前面几种药好一点的。”\n真不喜欢吃这药，如果吃美食都没有了快乐，那我活着还有什么乐趣……')

        @classmethod
        def recovery(cls, player, prev=False):
            return 30

        @classmethod
        def expectedReco(cls, player):
            times = 3
            if player.times >= 4:
                times -= 1
            if player.times >= 8:
                times -= 1
            if player.times >= 12:
                times -= 1

            t = 4 * player.week
            t *= Task.getConsScale(player)


            return r2(t * times + cls.recovery(player, prev=True))

    class MedicineD(Item):
        id = 103
        name = _('药物{font=arial.ttf}δ{/font}')
        kind = _('实验药物')
        maxCd = 0
        maxDu = 8
        reuse = False
        isUnique = False
        info = _('移除所有其他药物相关的药物反应和衰退，获得药物作用{font=arial.ttf}δ{/font}。\n恢复大量精神状态。')
        ad = _('“你已经不需要其他的药了。”')

        def useItemAction(self, player):
            r = rd(200000, 400000) * 0.01
            if player.mental < 0:
                r += -player.mental
            Notice.add(_('恢复了%s点精神状态！') % r)
            player.mental += r
            DrugED.add(player)
            for i in [DrugDA, DrugDB, DrugDC, DrugWA, DrugWB, DrugWC, DrugEA, DrugEB, DrugEC, Deterioration]:
                if i.has(player):
                    i.clearByType(player)

        @classmethod
        def getrecoveryinfo(cls, player):
            return _('预计恢复%s（%s）点精神状态。') % (glitchtext(rd(3, 5)), random_color(glitchtext(rd(2, 4))+' %'))

        @classmethod
        def getResInfo(cls, player):
            info= '\n'+cls.getBenefit(player)+'\n'
            for i in range(rd(3, 10)):
                info += random_color('—' + glitchtext(rd(5,25))+'\n')

            return info.rstrip()

        @classmethod
        def getBenefit(cls, player):
            return _('\n{font=DejaVuSans.ttf}• {/font}使用效率：%s') % random_color(glitchtext(rd(2, 4))+' %')

        @classmethod
        def getinfo(cls, player):
            if not persistent.PreciseMedDisplay:
                return cls.getrecoveryinfo(player)
            return _('预计恢复%s点精神状态。%s') % (glitchtext(5), MedicineD.getResInfo(player))


    class DrugHypnotic(Item):
        id = 300
        name = _('安眠药')
        kind = _('普通药物')
        maxCd = 0
        maxDu = 28
        reuse = False
        isUnique = False
        info = _('移除所有兴奋，服用后随层数降低睡眠消耗的精神状态，本日还没有服用过该药物时额外降低更多的精神状态。\n建议服用次数为每日一次，多次使用的效果未知。')
        ad = _('多咽下几片就能让一切痛苦消失。')
        p=0.1

        def useItemAction(self, player):
            DrugHypnoticEffect.add(player)
            ConcInc.clearByType(player)
            player.severity += 0.01



    class DrugColdrex(Item):
        id = 301
        name = _('感冒药')
        kind = _('普通药物')
        maxCd = 0
        maxDu = 28
        reuse = False
        isUnique = False
        info = _('服用后降低少量专注度，若没有生病则获得大量严重程度。\n使用后会延长1天生病的持续时间并根据层数提升恢复率，但本效果结束时则会减少生病的持续时间。\n建议服用次数为每日一次，多次使用的效果未知。')
        ad = _('建议用水送服，没有水的话那么用酒应该也可以？')
        p=0.15

        def useItemAction(self, player):
            if DrugColdrexEffect.has(player):
                effect = DrugColdrexEffect.get(player)
                if effect.duration == effect.maxDuration:
                    if effect.stacks >3:
                        player.severity += 1000
                        Achievement304.achieve()
                        Achievement.show()
                    elif effect.stacks >2:
                        player.severity += 0.5
                    elif effect.stacks >1:
                        player.severity += 0.1

            if PhysPun.has(player):
                DrugColdrexEffect.add(player)
            else:
                player.severity += 0.05
            player.severity += 0.02


    class DrugIbuprofen(Item):
        id = 302
        name = _('头疼药')
        kind = _('普通药物')
        maxCd = 0
        maxDu = 28
        reuse = False
        isUnique = False
        info = _('服用后每完成一个日程随层数百分比恢复微量精神状态。\n建议服用次数为每日一次，多次使用的效果未知。')
        ad = _('也许你单纯买来当糖豆吃。')
        p=0.05

        def useItemAction(self, player):
            if DrugIbuprofenEffect.has(player):
                effect = DrugIbuprofenEffect.get(player)
                if effect.duration == effect.maxDuration and effect.stacks >2:
                    player.severity += 1000
                    Achievement304.achieve()
                    Achievement.show()
                elif effect.duration == effect.maxDuration and effect.stacks >1:
                    player.severity += 0.1
            DrugIbuprofenEffect.add(player)

    class DrugVitamin(Item):
        id = 303
        name = _('维生素片')
        kind = _('普通药物')
        maxCd = 7
        maxDu = 28
        reuse = False
        isUnique = False
        info = _('在简单模式下，使用后可减少全部药物6点抗药性。')
        ad = 'So many sacrifices keep me alive,\nYet I don\'t even bother to survive.'
        p=1.5

        def useItemAction(self, player):
            if GameDifficulty1.has(player):
                for i in player.medinfo:
                    exa = player.medinfo[i].res-6
                    player.medinfo[i].res = max(exa, 0)
                    if exa <= 0:
                        Notice.add(_('降低了%s%s%s的抗药性！') % (6 + exa, '%', player.medinfo[i].med.name))
                    else:
                        Notice.add(_('降低了6%s%s的抗药性！') % ('%', player.medinfo[i].med.name))


    class DrugStomach(Item):
        id = 305
        name = _('胃药')
        kind = _('普通药物')
        maxCd = 7
        maxDu = 28
        reuse = False
        isUnique = False
        info = _('在简单模式下，使用后可提升5%食物的恢复效果。')
        ad = _('“为乳糖不耐受者献上痛苦死亡！”')
        p=1.5

        def useItemAction(self, player):
            if GameDifficulty1.has(player):
                exa = player.fooduse-10
                player.fooduse = max(exa, 0)
                if exa <= 0:
                    Notice.add(_('提升了%s%s食物的恢复效果！') % ((10 + exa)*0.5, '%'))
                else:
                    Notice.add(_('提升了5%食物的恢复效果！'))
    

    class DrugAmphetamine(Item):
        id = 306
        name = _('安非他命')
        kind = _('普通药物')
        maxCd = 2
        maxDu = 28
        reuse = False
        isUnique = False
        info = _('在简单模式下，使用后获得三层兴奋和心流。')
        ad = _('“不去思考也没有关系，马上就能给你解脱。”')
        p=1.5

        def useItemAction(self, player):
            if GameDifficulty1.has(player):
                ConcInc.add(player, 3)
                FocusAttention.add(player)
                
    
    class DrugEtizolam(Item):
        id = 307
        name = _('依替唑仑')
        kind = _('普通药物')
        maxCd = 2
        maxDu = 28
        reuse = False
        isUnique = False
        info = _('在简单模式下，使用后降低1%的当前严重度和1%的严重倍率。')
        ad = _('“比毒药更加甘甜。”')
        p=1.5

        def useItemAction(self, player):
            if GameDifficulty1.has(player):
                s = r2(player.severity * 0.01)
                player.severity -= s
                player.severityRegarded -= 0.01
                Notice.add(_('降低了1%的严重程度倍率！'))
                Notice.add(_('降低了%s点严重程度！') % s)

    
    class DrugUnknown(Item):
        id = 308
        name = _('魔法药片')
        kind = _('普通药物')
        maxCd = 14
        maxDu = 28
        reuse = False
        isUnique = False
        info = _('在简单模式下，使用后移除体弱，精神创伤和衰退中的一种效果。')
        ad = _('“PEACE PEACE PEACE PEACE PEACE PEACE PEACE PEACE PEACE PEACE PEACE PEACE PEACE PEACE PEACE PEACE PEACE PEACE PEACE PEACE PEACE PEACE”')
        p=3

        def useItemAction(self, player):
            if GameDifficulty1.has(player):
                for i in (Deterioration, Debilitated, Decadent):
                    if i.has(player):
                        i.clearByType(player)
                        return
    
    class DrugAspirin(Item):
        id = 309
        name = _('阿司匹林')
        kind = _('普通药物')
        maxCd = 2
        maxDu = 28
        reuse = False
        isUnique = False
        info = _('在硬核模式下，使用后使下一个日程消耗的精神状态减少60%。')
        ad = _('“倘若周围一团漆黑，那就只能静等眼睛习惯黑暗。”')
        p=0.25

        def useItemAction(self, player):
            if GameDifficulty5.has(player):
                DrugAspirinEffect.add(player)

    class Drugdextropropoxyphene(Item):
        id = 310
        name = _('右丙氧芬')
        kind = _('普通药物')
        maxCd = 2
        maxDu = 28
        reuse = False
        isUnique = False
        info = _('在硬核模式下，进行去床上休息日程后时，移除所有层数大于1的药物依赖。')
        ad = _('“我们的正常之处，就在于懂得自己的不正常。”')
        p=0.45

        def useItemAction(self, player):
            if GameDifficulty5.has(player):
                DrugdextropropoxypheneEffect.add(player)
                


    class DrugMethylphenidate(Item):
        id = 311
        name = _('利他林')
        kind = _('普通药物')
        maxCd = 2
        maxDu = 28
        reuse = False
        isUnique = False
        info = _('在硬核模式下，使用后使工作能力、身体素质和写作技巧提升10%，同时获得能力时额外获得1点。\n效果结束时，降低30%的专注度。')
        ad = _('“不要同情自己，同情自己是卑劣懦夫干的勾当。”')
        p=0.6

        def useItemAction(self, player):
            if GameDifficulty5.has(player):
                DrugMethylphenidateEffect.add(player)

    

    class DrugAntibiotic(Item):
        id = 397
        name = _('抗生素')
        kind = _('普通药物')
        maxCd = 7
        maxDu = 28
        reuse = False
        isUnique = False
        info = _('将生病转化为6层过劳，未生病则提升严重程度。')
        ad = _('如果我是一团青霉菌。\n那么我将献给你。\n我的盘尼西林。')
        p=0.25

        def useItemAction(self, player):
            if PhysPun.has(player):
                PhysPun.clearByType(player)
                PhysProb.add(player, 6)
                player.severity += 0.02
            else:
                player.severity += 0.05


    class DrugAntidepressant(Item):
        id = 398
        name = _('抗抑郁药')
        kind = _('普通药物')
        maxCd = 7
        maxDu = 28
        reuse = False
        isUnique = False
        info = _('将偏执转化为6层焦虑，未生病则提升严重程度。')
        ad = _('如果我是一株得病的小麦。\n那么我将献给你。\n我的麦角二乙酰胺。')
        p=0.25

        def useItemAction(self, player):
            if MentPun.has(player):
                MentPun.clearByType(player)
                MentProb.add(player, 6)
                player.severity += 0.02
            else:
                player.severity += 0.05


    class DrugFake(Item):
        id = 399
        name = _('安慰剂')
        kind = _('普通药物')
        maxCd = 0
        maxDu = 28
        reuse = False
        isUnique = False
        info = _('本身没有任何治疗作用。') 
        ad = _('因患者对医生信任、患者叫自我暗示以及对某种药物疗效的期望等而起到镇痛、镇蘸或缓解症状的作用。')
        p=0.01
        
        def useItemAction(self, player):
            Notice.add(_('什么也没有发生。'))

    ####################################################################################################

    class BookBase(Item):

        def __init__(self, player):
            super(BookBase, self).__init__(player)
            self.progress = 0
        
        def sound(self):
            pass

        def checkAvailable(self, player):
            if type(self) in player.itemcd:
                return _('书本仍在冷却时间中！')
            if GameDifficulty1.has(player):
                return True
            if not BookQuickReadEffect.has(player):
                return _('书本只能在进行阅读日程或存在特殊状态时才可阅读！')

            return True

        def use(self, player):
            if self.checkAvailable(player) != True:
                Notice.add(self.checkAvailable(player))
            else:
                self.sound()
                Stat.record(player, type(self))
                Notice.add(_('已阅读书本：')+ self.name)
                player.itemcd[type(self)] = self.maxCd
                if not GameDifficulty1.has(player):
                    BookQuickReadEffect.subByType(player)
                self.readBook(player, 2)
            Notice.show()


        def getPrefixInfo(self, player):
            if not self.reuse:
                reuse_info = _('\n使用后消耗  ')
            else:
                reuse_info = ''

            if type(self) not in player.itemcd and self.progress == 0:
                cd_info = _('未阅读  ')
            elif type(self) not in player.itemcd and self.progress == 1:
                cd_info = _('已阅读：50%  ')
            else:
                cd_info = _('下次可阅读时间：')+str(player.itemcd[type(self)])+_('天后  ')

            return _('数量：')+str(self.amounts) +reuse_info+'\n'+ cd_info+ '\n'

        def readBook(self, player, e=1):
            if rra(player, 50):
                ReadReward.add(player)
            self.progress += e
            if self.progress >= 2:
                Stat.record(player, type(self))
                self.progress = 0
                if self.maxCd != 0:
                    player.itemcd[type(self)] = self.maxCd
                self.useItemAction(player)
                if self.reuse == False:
                    self.sub(player)


    class BookDefault(BookBase):
        id = 400
        name = _('《泽尼的森林》')
        kind = _('书本')
        maxCd = 14
        maxDu = -1
        isUnique = True
        info = _('阅读本书籍将获得2~3层的良好的睡眠和精神的平复。\n当没有过劳时，额外获得1层良好的睡眠；当没有焦虑时，额外获得1层精神的平复。')
        ad = _('“迷失的人迷失了，相逢的人会再相逢。”')

        def useItemAction(self, player):
            if not PhysProb.has(p):
                PhysRezA.add(player)
            if not MentProb.has(p):
                MentRezB.add(player)
            PhysRezA.add(player, ra(player,2,3))
            MentRezB.add(player, ra(player,2,3))
            

    class BookWri(BookBase):
        id = 401
        name = _('《于老师教我的写作技巧》')
        kind = _('书本')
        maxCd = 14
        maxDu = -1
        isUnique = True
        info = _('当写作素材与灵感层数不低于25层时，阅读本书籍获得额外10层写作素材，并使写作技巧大幅提升。\n\n{color=#fbd26a}获得长门的手稿。{/color}')
        ad = _('“在写作之前，最好先花些时间在笔记本上设计人物，搜集情节，或者记下脑海中曾涌现过的东西，直到动笔的那一刻到来。”')
        bookEffect_ = BookWriEffect

        def useItemAction(self, player):
            if FixedInspiration.getstack(player) + Inspiration.getstack(player)>= 25:
                self.bookEffect_.add(player)
                FixedInspiration.add(player, 10)
                ManuscriptChangmen.add(p)


    class BookConc(BookBase):
        id = 402
        name = _('《海边的于秀爱》')
        kind = _('书本')
        maxCd = 14
        maxDu = -1
        isUnique = True
        info = _('阅读本书籍后，持续时间内过劳和焦虑不会因为层数过多而转化成生病和偏执。\n持续时间结束时，每有一层过劳和焦虑都会降低2点严重程度。\n降低的严重程度之和大于10点时，永久降低3%的严重程度。')
        ad = _('“于是我们领教了世界是何等凶顽，同时又得知世界也可以变得温存和美好。”')
        bookEffect_ = BookConcEffect

        def useItemAction(self, player):
            self.bookEffect_.add(player)


    class BookPhysPun(BookBase):
        id = 403
        name = _('《呼吸训练》')
        kind = _('书本')
        maxCd = 14
        maxDu = -1
        isUnique = True
        info = _('拥有生病或受伤时，阅读本书籍随机延长对应状态的持续时间。\n百分比提升恢复率，如果成功治愈，结束效果并降低3%的严重程度。')
        ad = _('“保证呼吸道通畅，提升呼吸肌功能，促进排痰和痰液引流，以及加强气体交换效率……”')
        bookEffect_ = BookPhysPunEffect

        def useItemAction(self, player):
            for i in [PhysPun, Injured]:
                if i.has(player):
                    i.get(player).duration += rca(player, (1, 1, 1, 1, 1, 2, 2, 3))
                    self.bookEffect_.add(player)

    
    class BookQuickRead(BookBase):
        id = 404
        name = _('《量子波动速读》')
        kind = _('书本')
        maxCd = 14
        maxDu = -1
        isUnique = True
        info = _('阅读本书籍后获得2层速读次数，拥有速读次数时阅读书籍不需要消耗回合，每速读一次消耗1次速读次数。')
        ad = _('“1分钟可以看完10万字的书！”\n“闭着眼睛就能和书发生感应！”\n“不需要翻开书本就能理解书中内容！”')
        bookEffect_ = BookQuickReadEffect

        def useItemAction(self, player):
            self.bookEffect_.add(player, 2)



    class BookWor(BookBase):
        id = 405
        name = _('《保持清醒的秘诀》')
        kind = _('书本')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('阅读本书籍将根据已完成的工作量提升工作速度，并降低工作消耗的精神状态。已完成的工作量越多，获得的层数越多，至多5层。\n\n{color=#fbd26a}获得架构师的手稿。{/color}')
        ad = _('“有效的思考是可以随着时间的推移而练习和发展的一个技能。当然，一切都始于心与脑的联系。”')
        bookEffect_ = BookWorEffect

        def useItemAction(self, player):
            completion = r2(player.achievedGoal / player.goal)
            self.bookEffect_.add(player, int(completion * 10))
            ManuscriptConstructor.add(player)


    class BookIns(BookBase):
        id = 406
        name = _('《2001年的弹珠机》')
        kind = _('书本')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('阅读本书籍后效果持续时间内每天起床时获得1~2层灵感，有小几率结束该效果。')
        ad = _('“迟早要失去的东西并没有太多意义. 必失之物的荣光并非真正的荣光。”')
        bookEffect_ = BookInsEffect

        def useItemAction(self, player):
            self.bookEffect_.add(player)

    class BookLevi(BookBase):
        id = 407
        name = _('《海神记》')
        kind = _('书本')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('立刻刷新所有书本的冷却时间。\n\n{color=#fbd26a}获得利维坦的手稿。{/color}')
        ad = _('“他曾经有很多名字：始源，深寂，永黑之蓝，涅柔斯，无名之游兽………但现在他只有一个名字，利维坦……”')

        def useItemAction(self, player):
            for i in player.itemcd:
                if i in ALLBOOKS:
                    player.itemcd[i] = 0

            for k in list(player.itemcd.keys()):
                if player.itemcd[k] == 0:
                    del player.itemcd[k]

            player.itemcd[type(self)] = 14
            ManuscriptLevi.add(player)

    class BookSport(BookBase):
        id = 409
        name = _('《阿斯卡隆之春》')
        kind = _('书本')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('阅读本书籍后，一段时间内提升20%运动类日程的专注度，同时获取身体素质时额外获得2点。效果结束后，身体素质永久提升2%。')
        ad = _('“我正伫立于现实的边缘。你会想念我吗，如果我轻轻一跃？”')

        def useItemAction(self, player):
            BookSportEffect.add(player)
            


    class BookWrite(BookBase):
        id = 410
        name = _('《亚斯塔禄之冬》')
        kind = _('书本')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('阅读本书籍后，一段时间内提升20%写作类日程的专注度，同时获取写作能力时额外获得2点。效果结束后，写作能力永久提升2%。')
        ad = _('“呼吸吧，趁你还能呼吸的时候。”')

        def useItemAction(self, player):
            BookWriteEffect.add(player)


    class BookCM(BookBase):
        id = 411
        name = _('《城堡与莫梭提斯》')
        kind = _('书本')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('阅读本书籍后效果持续时间内每天起床时减少严重程度，同时有小几率结束该效果。\n\n{color=#fbd26a}获得帕索斯的手稿。{/color}')
        ad = _('“永生从来就不是什么馈赠。”')
        bookEffect_ = BookCMEffect

        def useItemAction(self, player):
            self.bookEffect_.add(player)
            ManuscriptPathos.add(player)


    class BookMED(BookBase):
        id = 412
        name = _('《药：绝望的解决手段》')
        kind = _('书本')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('阅读本书籍后效果持续时间内进行工作类日程时有几率额外提升随机属性，提升5次后结束效果。')
        ad = _('“我看向蔚蓝的天空，仿佛现在还是四五年前，我正趴在大学教室的最后一排桌子上，歪头看着窗户，对着和现在一样蓝的天空做着永远不会实现的白日梦。”')
        bookEffect_ = BookMEDEffect

        def useItemAction(self, player):
            self.bookEffect_.add(player, 5)


    class AMaverickLion(BookBase):
        id = 413
        name = _('《一只特立独行的狮子》')
        kind = _('书本')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('阅读本书籍后随机移除2个负面状态。\n负面状态包括：过劳，焦虑，生病，受伤，偏执，酸痛')
        ad = _('“它们会自由自在地闲逛，饥则进行捕食渴则饮，春天来临时还要谈谈爱情。”')

        def useItemAction(self, player):
            l = list(filter(lambda x: type(x) in (PhysProb, PhysPun, MentProb, MentPun, Injured, Soreness), player.effects))
            if l:
                rca(player, l).clearByType(player)

            l = list(filter(lambda x: type(x) in (PhysProb, PhysPun, MentProb, MentPun, Injured, Soreness), player.effects))
            if l:
                rca(player, l).clearByType(player)

    class BookHeal(BookBase):
        id = 414
        name = _('《神，我们，或所有的士兵》')
        kind = _('书本')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('阅读本书籍后移除当前所有非永久的学识和增益，每个被移除的学识和增益都能降低0.5%的严重程度倍率。')
        ad = _('“明天王子就会来见他，守卫这样说。他知道这其实是什么意思，被圈养的生活将迎来终结，但他好像对此没有什么特别的情绪。”')

        def useItemAction(self, player):
            s = 0
            for i in list(filter(lambda x: x.duration>=0 and x.kind in ('学识','增益'), player.effects)):
                i.clearByType(player)
                s += 1
            if s>0:
                rec = r2(s * 0.005)
                player.severityRegarded -= rec
                Notice.add(_('降低了%s的严重程度倍率！') % rec)

    class Bookdont(BookBase):
        id = 415
        name = _('《不要读这本书》')
        kind = _('书本')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('不要看这本书的简介不要看这本书的简介不要看这本书的简介不要看这本书的简介不要看这本书的简介不要看这本书的简介')
        ad = _('不要看这本书的内容不要看这本书的内容不要看这本书的内容不要看这本书的内容不要看这本书的内容不要看这本书的内容不要看这本书的内容')

        def useItemAction(self, player):
            renpy.jump('bookdont')

    class BookRisk(BookBase):
        id = 416
        name = _('《失而复得》')
        kind = _('书本')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('阅读本书籍后效果期间内消耗的精力越多，效果结束时降低的严重程度越多，同时提升的工作能力越多。\n若消耗的精神状态低于150则获得2层焦虑，有效上限为500点。')
        ad = _('我觉得，即使能够重新开始自己的人生，恐怕也还是走回老路。\n因为那便是我自身。\n我除了成为我自身别无选择。哪怕有更多的人弃我而去，或我弃更多的人而去，哪怕五彩缤纷的感情，出类拔萃的素质和对未来的企盼受到限制以至消失，我也只能成为我自身，还有别的可能吗？')
        bookEffect_ = BookRiskEffect

        def useItemAction(self, player):
            self.bookEffect_.add(player)

    class BookRisk(BookBase):
        id = 417
        name = _('《世界之终与冷漠之城》')
        kind = _('书本')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('阅读本书籍后获得存在感。\n如果已存在存在感，则直接降低2%的严重倍率并将精神状态恢复至80。')
        ad = _('“我要坐在有阳光的地方，像猫舔奶碗那样一字不漏地把报纸上下看遍左右看遍，然后把世人在阳光下开展的各种生之片段吸入体内，滋润每一个细胞。”')
        bookEffect_ = Novice

        def useItemAction(self, player):
            if not Novice.has(player):
                Novice.add(player)
                Novice.get(player).duration = 4
            else:
                Notice.add(_('由于已存在存在感，降低了2%的严重倍率！'))
                player.severityRegarded -= 0.02
                if player.mental < 80:
                    player.mental = 80.0

    class BookSevUp(BookBase):
        id = 418
        name = _('《热病》')
        kind = _('书本')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('阅读本书籍后将精神状态提升至200，但持续时间内将暂时提升严重程度。')
        ad = _('“我知道，我只是觉得，今晚应该是我的终点了，这是我的预感。”\n我突然很想再吃一次那种名为凯撒面包的食物，我怀念那硬实的口感，它让我想起面前这只狼坚实的拥抱。')
        bookEffect_ = BookSevUpEffect

        def useItemAction(self, player):
            player.mental = 200.0
            self.bookEffect_.add(player)



    class ManuscriptLevi(Item):
        id = 450
        name = _('利维坦的手稿')
        kind = _('手稿')
        maxCd = 1
        maxDu = -1  # 数字
        isUnique = False
        reuse = False
        info = _('阅读本手稿后延长所有学识和增益的持续时间1天。')
        ad = _('“……然而，尽管利维坦已然离去，但当海啸摧毁城池，淹没陆地，在人们的恐惧和敬畏中总会诞生新的海神。”')

        def useItemAction(self, player):
            for i in list(filter(lambda x: x.kind in ('学识', '增益'), player.effects)):
                if i.get(player).duration >= 0:
                    i.get(player).duration += 1

    
    class ManuscriptConstructor(Item):
        id = 451
        name = _('架构师的手稿')
        kind = _('手稿')
        maxCd = 1
        maxDu = -1  # 数字
        isUnique = False
        reuse = False
        info = _('阅读本手稿后立刻完成30%的工作。')
        ad = _('{color=#ff0000}Exception in thread "main" java.lang.StackOverflowError{/color}')

        def useItemAction(self, player):
            player.achievedGoal += r2(player.goal * 0.3)


    class ManuscriptChangmen(Item):
        id = 452
        name = _('长门的手稿')
        kind = _('手稿')
        maxCd = 1
        maxDu = -1  # 数字
        isUnique = False
        reuse = False
        info = _('阅读本手稿后将灵感的持续时间延长3天，如果没有灵感则没有效果。')
        ad = _('“人生是旷野，不是轨道，我有权拒绝一种生活。”')

        def useItemAction(self, player):
            if Inspiration.has(p):
                Inspiration.get(p).duration += 3


    class ManuscriptPathos(Item):
        id = 453
        name = _('帕索斯的手稿')
        kind = _('手稿')
        maxCd = 1
        maxDu = -1  # 数字
        isUnique = False
        reuse = False
        info = _('阅读本手稿后随机移除一个药物依赖状态。')
        ad = _('至少他的字写得很漂亮……想在上面射精……')

        def useItemAction(self, player):
            l = list(filter(lambda x: type(x) in (DrugDA, DrugDB, DrugDC), player.effects))
            if l:
                rca(player, l).clearByType(player)



    class ProfessionalBookWorking(BookBase):
        id = 497
        name = _('计算机科学专业书籍')
        kind = _('书本')
        maxCd = 3
        maxDu = -1  # 数字
        reuse = False
        isUnique = False
        info = _('阅读本书籍后随机提升工作能力并消耗该书，永久提升2%的工作速度，并获得心流。')
        ad = _('数据结构、设计模式，软件架构，程序测试，操作系统，计算机组成原理……')

        def checkAvailable(self, player):
            if type(self) in player.itemcd:
                return _('书本仍在冷却时间中！')
            if GameDifficulty1.has(player):
                return True
            if not BookQuickReadEffect.has(player) and not Relaxation.has(player):
                return _('书本只能在进行阅读日程或存在特殊状态时才可阅读！')
            
            return True

        def use(self, player):
            if self.checkAvailable(player) != True:
                Notice.add(self.checkAvailable(player))
            else:
                Stat.record(player, type(self))
                Notice.add(_('已速读书本：')+ self.name)
                player.itemcd[type(self)] = self.maxCd 
                if not GameDifficulty1.has(player):
                    if Relaxation.has(player):
                        Relaxation.subByType(player)
                    else:
                        BookQuickReadEffect.subByType(player)
                self.readBook(player, 2)
            Notice.show()

        def useItemAction(self, player):
            g = rca(player, (1,2,2, 3, 3, 4))
            player.working += g * 0.01
            Notice.add(_('提升了%s点工作能力。') % g)
            FocusAttention.add(player)
            player.workSpeed += 0.02

    class ProfessionalBookWriting(BookBase):
        id = 498
        name = _('文字运用专业书籍')
        kind = _('书本')
        maxCd = 3
        maxDu = -1  # 数字
        reuse = False
        isUnique = False
        info = _('阅读本书籍后随机提升写作技巧并消耗该书，永久提升2%的专注度，并获得4层灵感。')
        ad = _('虽然都是些老掉牙的写法，看这些还不如去读点别人写的小说。')

        def checkAvailable(self, player):
            if type(self) in player.itemcd:
                return _('书本仍在冷却时间中！')
            if GameDifficulty1.has(player):
                return True
            if not BookQuickReadEffect.has(player) and not Relaxation.has(player):
                return _('书本只能在进行阅读日程或存在特殊状态时才可阅读！')
            return True

        def use(self, player):
            if self.checkAvailable(player) != True:
                Notice.add(self.checkAvailable(player))
            else:
                Stat.record(player, type(self))
                Notice.add(_('已速读书本：')+ self.name)
                player.itemcd[type(self)] = self.maxCd 
                if not GameDifficulty1.has(player):
                    if Relaxation.has(player):
                        Relaxation.subByType(player)
                    else:
                        BookQuickReadEffect.subByType(player)
                self.readBook(player, 2)
            Notice.show()

        def useItemAction(self, player):
            g = rca(player, (1,2,2, 3, 3,4))
            player.writing += g * 0.01
            Notice.add(_('提升了%s点写作技巧。') % g)
            Inspiration.add(player, 4)
            player.workConcentration += 2

    class ProfessionalBookSeverity(BookBase):
        id = 499
        name = _('心理学专业书籍')
        kind = _('书本')
        maxCd = 5
        maxDu = -1  # 数字
        reuse = False
        isUnique = False
        info = _('阅读本书籍后随机降低严重程度并消耗该书，永久降低1~2%的严重程度倍率，并随机获得数层精神的释放和精神的平复。')
        ad = _('测测你是哪种人格？是NTXL！')

        def checkAvailable(self, player):
            if type(self) in player.itemcd:
                return _('书本仍在冷却时间中！')
            if GameDifficulty1.has(player):
                return True
            if not BookQuickReadEffect.has(player) and not Relaxation.has(player):
                return _('书本只能在进行阅读日程或存在特殊状态时才可阅读！')
            return True

        def use(self, player):
            if self.checkAvailable(player) != True:
                Notice.add(self.checkAvailable(player))
            else:
                Stat.record(player, type(self))
                Notice.add(_('已速读书本：')+ self.name)
                player.itemcd[type(self)] = self.maxCd 
                if not GameDifficulty1.has(player):
                    if Relaxation.has(player):
                        Relaxation.subByType(player)
                    else:
                        BookQuickReadEffect.subByType(player)
                self.readBook(player, 2)
            Notice.show()

        def useItemAction(self, player):
            g = rca(player, (1, 2, 2, 3, 3))
            player.severity -= g * 0.01
            Notice.add(_('降低了%s点严重程度。') % g)
            MentRezA.add(player, rca(player,(0, 1, 1, 2)))
            MentRezB.add(player, rca(player,(0, 1, 1, 2)))
            g2 = rca(player, (1, 1, 1, 2))
            player.severityRegarded -= 0.01 * g2
            Notice.add(_('降低了%s%s的严重倍率。') % (g2, '%'))

    
    class BookGameModule2(BookBase):
        id = 419
        name = _('《无尽之旅》')
        kind = _('书本')
        maxCd = 14
        maxDu = -1  # 数字
        reuse = True
        isUnique = False
        info = _('完成阅读后获得失语，以及宿命、死亡、毁灭、梦境、欲望、绝望、狂热其一的手稿')
        ad = _('当旅人来到无尽家族，看着无尽们的“忙碌”，让旅人得到灵感——如果不同的我拿到这种能力会发生什么呢？')

        def useItemAction(self, player):
            EffectGameModule2.add(player)
            if GameModule2.has(player):
                GameModule2.get(player).readbook()
            else:
                renpy.jump("moduleerror")
            rca(player, (ManuscriptGameModule2_1, ManuscriptGameModule2_2, ManuscriptGameModule2_3, ManuscriptGameModule2_4, ManuscriptGameModule2_5, ManuscriptGameModule2_6, ManuscriptGameModule2_7)).add(player)
    
    class ManuscriptGameModule2_1(Item):
        id = 454
        name = _('宿命-糖迷白的祝福')
        kind = _('手稿')
        maxCd = 14
        maxDu = 14  # 数字
        isUnique = False
        reuse = False
        info = _('阅读本手稿后使用后减少3-6点严重程度。\n获得忧虑和2层睡意。')
        ad = _('“谁说我只做旁观者，我偶尔也是会干预一下的。”')

        def useItemAction(self, player):
            if GameModule2.has(player):
                GameModule2.get(player).readmanu()
            else:
                renpy.jump("moduleerror")
            temp = ra(player, 3, 6)
            Notice.add(_('降低了%s点严重程度！') % temp)
            player.severity -= 0.01 * temp
            Anxiety.add(player)
            Anxiety.get(player).duration = 1
            ConcDec.add(player, 2)
    
    class ManuscriptGameModule2_2(Item):
        id = 455
        name = _('死亡-五晶的怜悯')
        kind = _('手稿')
        maxCd = 14
        maxDu = 14  # 数字
        isUnique = False
        reuse = False
        info = _('使用后获得精神状态，随当前周数提升恢复的精神状态。\n提升20%精神状态的消耗，降低20%精神状态的恢复。')
        ad = _('*这里只有沉默。*')

        def useItemAction(self, player):
            if GameModule2.has(player):
                GameModule2.get(player).readmanu()
            else:
                renpy.jump("moduleerror")
            rec = ra(player, 3, 9) * player.week
            Notice.add(_('恢复了%s点精神状态！') % rec)
            player.mental += rec
            EffectGameModule2_1.add(player)

    class ManuscriptGameModule2_3(Item):
        id = 456
        name = _('毁灭-武言的低语')
        kind = _('手稿')
        maxCd = 14
        maxDu = 14  # 数字
        isUnique = False
        reuse = False
        info = _('阅读本手稿后降低2~6点身体素质，同时减少等量的严重程度，同时恢复当前精神状态的30%。')
        ad = _('“尘啊！埃啊！是时候尘埃落定了！”')

        def useItemAction(self, player):
            if GameModule2.has(player):
                GameModule2.get(player).readmanu()
            else:
                renpy.jump("moduleerror")
            temp = ra(player, 2, 6)
            Notice.add(_('降低了%s点身体素质！') % temp)
            Notice.add(_('降低了%s点严重程度！') % temp)
            player.severity -= 0.01 * temp
            player.physical -= 0.01 * temp
            rec = r2(player.mental * 0.3)
            Notice.add(_('恢复了%s点精神状态！') % rec)
            player.mental += rec

    class ManuscriptGameModule2_4(Item):
        id = 457
        name = _('梦境-白影的幻想')
        kind = _('手稿')
        maxCd = 14
        maxDu = 14  # 数字
        isUnique = False
        reuse = False
        info = _('阅读本手稿后降低3~6点工作能力，每降低1层暂时提升5%的写作能力，同时获得等量层数的灵感。')
        ad = _('“来梦里吧，我会让你得到无限的幸福。”')

        def useItemAction(self, player):
            if GameModule2.has(player):
                GameModule2.get(player).readmanu()
            else:
                renpy.jump("moduleerror")
            temp = ra(player, 3, 6)
            Notice.add(_('降低了%s点工作能力！') % temp)
            player.working -= 0.01 * temp
            EffectGameModule2_2.add(player, temp)
            Inspiration.add(player, temp)

    class ManuscriptGameModule2_5(Item):
        id = 458
        name = _('欲望-徵羽微凉的贪婪')
        kind = _('手稿')
        maxCd = 14
        maxDu = 14  # 数字
        isUnique = False
        reuse = False
        info = _('阅读本手稿后，增加0-4点严重程度，使下次写作时获得的价值提升30%。')
        ad = _('“即使是在这片钢筋丛林里，我们也要做最危险的野兽。”')

        def useItemAction(self, player):
            if GameModule2.has(player):
                GameModule2.get(player).readmanu()
            else:
                renpy.jump("moduleerror")
            temp = ra(player, 0, 4)
            Notice.add(_('提升了%s点严重程度！') % temp)
            player.severity += 0.01 * temp

    class ManuscriptGameModule2_6(Item):
        id = 459
        name = _('绝望-夏明雪狼的树荫')
        kind = _('手稿')
        maxCd = 14
        maxDu = 14  # 数字
        isUnique = False
        reuse = False
        info = _('使用后增加20-40点严重程度，立刻刷新除无尽之旅系列道具的所有带有冷却时间的道具冷却时间。')
        ad = _('“拥有你，就不需要魔法给的勇气。”')

        def useItemAction(self, player):
            if GameModule2.has(player):
                GameModule2.get(player).readmanu()
            else:
                renpy.jump("moduleerror")
            temp = ra(player, 20, 40)
            Notice.add(_('提升了%s点严重程度！') % temp)
            player.severity += 0.01 * temp

            for i in player.itemcd:
                if i.id not in (419, 454, 454, 456, 457, 458, 459, 460):
                    player.itemcd[i] = 0

            for k in list(player.itemcd.keys()):
                if player.itemcd[k] == 0:
                    del player.itemcd[k]
            
    class ManuscriptGameModule2_7(Item):
        id = 460
        name = _('狂热-空白的手稿')
        kind = _('手稿')
        maxCd = -1
        maxDu = -1  # 数字
        isUnique = False
        reuse = False
        info = _('无法阅读该手稿。')
        ad = _('看上去和无字天书一样，但……怎么这么厚啊。')

    class BookUndead(BookBase):
        id = 420
        name = _('《国境以北星空以南》')
        kind = _('书本')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('阅读本书籍时若精神状态低于0，则暂时提升严重程度，使精神状态不会低于0。')
        ad = _('“追求得到之日即其终止之时，寻觅的过程亦即失去的过程。”')
        bookEffect_ = BookUndeadEffect

        def useItemAction(self, player):
            if player.mental < 0:
                self.bookEffect_.add(player)

    class BookRandConc(BookBase):
        id = 421
        name = _('《寻羊历险记》')
        kind = _('书本')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('阅读本书籍后获得学识，每完成一个日程后获得对下一个日程0%~50%的专注度提升。')
        ad = _('“意志无法分割，或者百分之百继承，或者百分之百消失。”')
        bookEffect_ = BookRandConcEffect

        def useItemAction(self, player):
            self.bookEffect_.add(player)

    class BookBanDep(BookBase):
        id = 422
        name = _('《常用药理学知识》')
        kind = _('书本')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('阅读本书籍后获得学识，持续时间内使用药物提升10%恢复效果，同时不会获得药物效果。获得新的药物依赖时，取而代之获得其对应药物的1点抗药性。')
        ad = _('“吗啡适用于各种剧痛，但不包括颅脑外伤剧痛。”')
        bookEffect_ = BookBanDepEffect

        def useItemAction(self, player):
            self.bookEffect_.add(player)
            

    ##################################################################################################################

    class AppleJuice(Item):
        id = 200
        name = _('苹果汽水')
        kind = _('食物')
        maxCd = 1
        maxDu = 28
        reuse = False
        isUnique = False
        info = _('使用后恢复少量精神状态并获得增益：苹果口味，小概率降低严重程度倍率。')
        ad = _('“亚斯塔禄牌苹果汽水，比同类品牌产品多添加20%纯果汁！”')

        def useItemAction(self, player):
            rec = r2(5 * player.useFoodScale())
            Notice.add(_('恢复了%s点精神状态！') % rec)
            if rra(player, 10):
                player.severityRegarded -= 0.01
                Notice.add(_('严重程度的倍率下降了1%！'))
            player.mental += rec
            AppleFlavor.add(player)


    class CitrusJuice(Item):
        id = 201
        name = _('橘子汽水')
        kind = _('食物')
        maxCd = 1
        maxDu = 28
        reuse = False
        isUnique = False
        info = _('使用后恢复少量精神状态并获得增益：柑橘口味')
        ad = _('“阿斯卡隆牌橘子汽水，喝到就是赚到！”')

        def useItemAction(self, player):
            rec = r2(15 * player.useFoodScale())
            Notice.add(_('恢复了%s点精神状态！') % rec)
            player.mental += rec
            CitrusFlavor.add(player)


    class Cola(Item):
        id = 202
        name = _('罐装可乐')
        kind = _('食物')
        maxCd = 1
        maxDu = 28
        reuse = False
        isUnique = False
        info = _('使用后获得心流，并刷新本日的随机状态。\n（睡意，兴奋，紧张，放松）')
        ad = _('“The choice of a new generation.”')

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
            FocusAttention.add(player)


    class ToastFood(Item):
        id = 203
        name = _('厚蛋吐司')
        kind = _('食物')
        maxCd = 1
        maxDu = 1
        reuse = False
        isUnique = False
        info = _('使用后恢复精神状态，移除2层紧张。')
        ad = _('外脆里嫩，鲜香不腻，不过高筋面粉一定要过筛。')

        def useItemAction(self, player):
            rec = r2(10 * player.useFoodScale())
            Notice.add(_('恢复了%s点精神状态！') % rec)
            player.mental += rec
            player.fooduse += 2
            Notice.add(_('降低了1%食物的恢复效果！'))
            if ConsInc.has(player):
                ConsInc.subByType(p, 2)

    class CoffeeFood(Item):
        id = 204
        name = _('手冲咖啡')
        kind = _('食物')
        maxCd = 0
        maxDu = 2
        reuse = False
        isUnique = False
        info = _('获得2层兴奋和1层紧张。')
        ad = _('又苦又难喝，但是能让人打起精神。')

        def useItemAction(self, player):
            ConsInc.add(player)
            ConcInc.add(player, 2)
            player.fooduse += 2
            Notice.add(_('降低了1%食物的恢复效果！'))

    class SaladFood(Item):
        id = 205
        name = _('时蔬沙拉')
        kind = _('食物')
        maxCd = 1
        maxDu = 1
        reuse = False
        isUnique = False
        info = _('使用后恢复精神状态，有概率提升身体素质，有概率提升食物的恢复效果。')
        ad = _('膳食指南推荐一般建议每天摄入300-500g、至少5种以上的蔬菜……')

        def useItemAction(self, player):
            rec = r2(5 * player.useFoodScale())
            Notice.add(_('恢复了%s点精神状态！') % rec)
            player.mental += rec
            if rra(player, 70):
                Notice.add(_('提升了1点身体素质！'))
                player.physical += 0.01
            if rra(player, 60):
                Notice.add(_('提升了1%食物的恢复效果！'))
                player.fooduse -= 2

    class PizzaFood(Item):
        id = 206
        name = _('香肠披萨')
        kind = _('食物')
        maxCd = 1
        maxDu = 1
        reuse = False
        isUnique = False
        info = _('使用后恢复精神状态，获得心流，但会降低食物的恢复效果。')
        ad = _('上等的披萨必须具备四个特质：新鲜饼皮、上等芝士、奶酪、顶级比萨酱和新鲜的馅料……')

        def useItemAction(self, player):
            rec = r2(15 * player.useFoodScale())
            Notice.add(_('恢复了%s点精神状态！') % rec)
            player.mental += rec
            player.fooduse += 2
            Notice.add(_('降低了1%食物的恢复效果！'))
            if rra(player, 50):
                Satiety.add(player)
            FocusAttention.add(p)
                

    class BurgerFood(Item):
        id = 207
        name = _('牛肉汉堡')
        kind = _('食物')
        maxCd = 1
        maxDu = 1
        reuse = False
        isUnique = False
        info = _('使用后恢复较多的精神状态。')
        ad = _('热熔芝士yyds！芝士与牛肉饼完美融合，浓香四溢的完美升级！')

        def useItemAction(self, player):
            rec = r2(30 * player.useFoodScale())
            Notice.add(_('恢复了%s点精神状态！') % rec)
            player.mental += rec
            player.fooduse += 1
            Notice.add(_('降低了0.5%食物的恢复效果！'))
            if rra(player, 60):
                Satiety.add(player)

    class BreadFood(Item):
        id = 208
        name = _('凯撒面包')
        kind = _('食物')
        maxCd = 1
        maxDu = 1
        reuse = False
        isUnique = False
        info = _('使用后恢复精神状态，并降低严重程度。')
        ad = _('规定斜切必须要有5道裂口才算标准的长条面包！')

        def useItemAction(self, player):
            rec = r2(10 * player.useFoodScale())
            Notice.add(_('恢复了%s点精神状态！') % rec)
            player.mental += rec
            player.fooduse += 1
            Notice.add(_('降低了1点严重程度！'))
            Notice.add(_('降低了0.5%食物的恢复效果！'))
            player.severity -= 0.01
            if rra(player, 25):
                Satiety.add(player)

    class PastaFood(Item):
        id = 209
        name = _('黑椒意面')
        kind = _('食物')
        maxCd = 1
        maxDu = 1
        reuse = False
        isUnique = False
        info = _('使用后恢复精神状态，提升身体素质或移除1层过劳。')
        ad = _('非常的新鲜，非常的美味。')

        def useItemAction(self, player):
            rec = r2(20 * player.useFoodScale())
            Notice.add(_('恢复了%s点精神状态！') % rec)
            player.mental += rec
            player.fooduse += 1
            Notice.add(_('降低了0.5%食物的恢复效果！'))
            if rra(player, 40):
                Satiety.add(player)
            if rra(player, 70):
                if rra(player, 70):
                    player.physical += 0.01
                    Notice.add(_('身体素质提升了1点！'))
                else:
                    player.physical += 0.02
                    Notice.add(_('身体素质提升了2点！'))
                
            else:
                if PhysProb.has(player):
                    PhysProb.subByType(player)

    class SoupFood(Item):
        id = 210
        name = _('鲑鱼靓汤')
        kind = _('食物')
        maxCd = 1
        maxDu = 1
        reuse = False
        isUnique = False
        info = _('使用后恢复精神状态，提升写作技巧或获得1层精神的平复。')
        ad = _('“现在，它早已死了，只是眼里还闪着一丝诡异的光。”')

        def useItemAction(self, player):
            rec = r2(20 * player.useFoodScale())
            Notice.add(_('恢复了%s点精神状态！') % rec)
            player.mental += rec
            player.fooduse += 1
            Notice.add(_('降低了0.5%食物的恢复效果！'))
            if rra(player, 60):
                Satiety.add(player)
            if rra(player, 70):
                if rra(player, 70):
                    player.writing += 0.01
                    Notice.add(_('写作技巧提升了1点！'))
                else:
                    player.writing += 0.02
                    Notice.add(_('写作技巧提升了2点！'))
            else:
                MentRezB.add(p)

    class SteakFood(Item):
        id = 211
        name = _('战斧牛排')
        kind = _('食物')
        maxCd = 1
        maxDu = 1
        reuse = False
        isUnique = False
        info = _('使用后恢复巨量精神状态并获得饱腹。')
        ad = _('家庭聚会一定要点这道菜，比惠灵顿还哇塞。\n……一个人吃？咋不撑死你呢？')

        def useItemAction(self, player):
            rec = r2(65 * player.useFoodScale())
            Notice.add(_('恢复了%s点精神状态！') % rec)
            player.mental += rec
            player.fooduse += 2
            Notice.add(_('降低了1%食物的恢复效果！'))
            Satiety.add(player, 4)
            Satiety.get(player).duration = ra(player, 2, 3)

    class StreetFood1(Item):
        id = 212
        name = _('一袋糖炒板栗')
        kind = _('食物')
        maxCd = 1
        maxDu = 1
        reuse = False
        isUnique = False
        info = _('使用后恢复精神状态，提升食物恢复效果。')
        ad = _('大多数人都喜欢购买的餐后小零食，也可以当做一顿不怎么管饱的午饭，香味飘散在空气中简单引发食欲。\n不过吃多了可不太妙，你不准备再花更多的钱去看牙齿。')

        def useItemAction(self, player):
            rec = r2(15 * player.useFoodScale())
            Satiety.add(p)
            Notice.add(_('恢复了%s点精神状态！') % rec)
            player.mental += rec
            player.fooduse -= 2
            Notice.add(_('提升了1%食物的恢复效果！'))

    class StreetFood2(Item):
        id = 213
        name = _('油炸小酥肉')
        kind = _('食物')
        maxCd = 0
        maxDu = 2
        reuse = False
        isUnique = False
        info = _('使用后恢复精神状态，不受恢复效果的影响。')
        ad = _('似乎是一家网红小吃店的招牌，手机里到处是它的广告，同样在各种测评里时常出现它的身影。\n看上去金黄酥脆，但是谁知道是不是地沟油做的呢？')

        def useItemAction(self, player):
            rec = r2(20 * f())
            Notice.add(_('恢复了%s点精神状态！') % rec)
            Satiety.add(p)
            player.mental += rec
            player.fooduse +=1
            Notice.add(_('降低了0.5%食物的恢复效果！'))

    class StreetFood3(Item):
        id = 214
        name = _('冰雪蜜城柠檬水')
        kind = _('食物')
        maxCd = 1
        maxDu = 1
        reuse = False
        isUnique = False
        info = _('使用后恢复精神状态，降低严重性。')
        ad = _('谁不喜欢价格亲民又冰爽解渴的柠檬水呢？正值酷暑的大街上极其需要一倍冰冰凉的柠檬水帮你消消暑。\n冰冰凉凉还好喝，但是冷热交加容易胃疼。')

        def useItemAction(self, player):
            rec = r2(5 * player.useFoodScale())
            Notice.add(_('恢复了%s点精神状态！') % rec)
            player.mental += rec
            player.severity -= 0.02
            Notice.add(_('降低了2点严重程度！'))

    class StreetFood4(Item):
        id = 215
        name = _('插着木签的菠萝片')
        kind = _('食物')
        maxCd = 0
        maxDu = 1
        reuse = False
        isUnique = False
        info = _('使用后提升食物恢复效果，也会提升严重程度。')
        ad = _('新鲜的小菠萝，店家特地用盐水洗过一遍的削皮新鲜水果，酸中带甜，可是总会有汁水溅在衣服上。\n当然，最难过的是菠萝会塞牙，祝你好运。')

        def useItemAction(self, player):
            player.severity += 0.01
            Notice.add(_('提升了1点严重程度！'))
            player.fooduse -=1
            Notice.add(_('提升了0.5%食物的恢复效果！'))

    class StreetFood5(Item):
        id = 216
        name = _('冰美式')
        kind = _('食物')
        maxCd = 1
        maxDu = 3
        reuse = False
        isUnique = False
        info = _('使用后获得2层兴奋，永久提升食物恢复的效果。')
        ad = _('A市的人喝咖啡，像进行一场不需要规则的游戏，随性放任，百无禁忌。')

        def useItemAction(self, player):
            player.fooduse -= 2
            ConcInc.add(player, 2)
            Notice.add(_('提升了1%食物的恢复效果！'))

    class StreetFood6(Item):
        id = 217
        name = _('生椰拿铁')
        kind = _('食物')
        maxCd = 1
        maxDu = 3
        reuse = False
        isUnique = False
        info = _('使用后获得1层兴奋和2层紧张，降低2点严重程度。')
        ad = _('“我不在咖啡馆，就在去咖啡馆的路上。”')

        def useItemAction(self, player):
            ConcInc.add(player, 1)
            ConsInc.add(player, 2)
            player.severity -= 0.02
            Notice.add(_('降低了2点严重程度！'))
            player.fooduse += 1
            Notice.add(_('降低了0.5%食物的恢复效果！'))

    class StreetFood7(Item):
        id = 218
        name = _('摩卡咖啡')
        kind = _('食物')
        maxCd = 1
        maxDu = 3
        reuse = False
        isUnique = False
        info = _('使用后获得3层放松。')
        ad = _('让爱恋中的人们了解爱情的甜美和波折，为了告诉我们幸福的简单。')

        def useItemAction(self, player):
            ConsDec.add(player, 3)
            player.fooduse += 1
            Notice.add(_('降低了0.5%食物的恢复效果！'))

    class StreetFood8(Item):
        id = 219
        name = _('奇怪的红茶')
        kind = _('食物')
        maxCd = 1
        maxDu = 3
        reuse = False
        isUnique = False
        info = _('使用后获得2层睡意。')
        ad = _('在你拜访你最喜欢的朋友的家时，可以分享给他品尝，不过要提前问好几分钟后会不会有人敲门。')

        def useItemAction(self, player):
            ConcDec.add(player, 2)
            player.fooduse += 1
            Notice.add(_('降低了0.5%食物的恢复效果！'))

    class StreetFood9(Item):
        id = 220
        name = _('天然矿泉水')
        kind = _('食物')
        maxCd = 1
        maxDu = 7
        reuse = False
        isUnique = False
        info = _('使用后随机提升2点属性。')
        ad = _('“添加了一整个元素周期表的微量元素，纯天然矿物质水就选于秀爱牌天然矿泉水。”')

        def useItemAction(self, player):
            temp = rd(1,3)
            if temp == 1:
                player.working += 0.02
                Notice.add(_('提升了2点工作能力！'))
            elif temp == 2:
                player.physical += 0.02
                Notice.add(_('提升了2点身体素质！'))
            else:
                player.writing += 0.02
                Notice.add(_('提升了2点写作技巧！'))

    
    class StreetFood10(Item):
        id = 221
        name = _('泡面')
        kind = _('食物')
        maxCd = 0
        maxDu = 90
        reuse = False
        isUnique = False
        info = _('精神状态大于0时，精神状态越少，恢复的精神状态越多。\n必定获得饱腹并降低少量食物的恢复效果。')
        ad = _('某种意义上的硬通货。')

        def useItemAction(self, player):
            if 0 < player.mental < 50:
                r = -0.6 * player.mental + 50
                rec = r2(r * player.useFoodScale())
            else:
                rec = r2(20 * player.useFoodScale())
            Notice.add(_('恢复了%s点精神状态！') % rec)
            player.mental += rec
            Satiety.add(player)
            player.fooduse += 2
            Notice.add(_('降低了1%食物的恢复效果！'))

    class Alcohol(Item):
        id = 222
        name = _('梅子酒')
        kind = _('食物')
        maxCd = 1
        maxDu = 90
        reuse = False
        isUnique = False
        info = _('使用后消耗50%的精神状态，低于0时固定降低100点。\n获得2层睡意，2层放松和3层灵感，并提升严重程度。')
        ad = _('“吾身为火，烧尽那些敢于眷恋我的勇者。”')

        def useItemAction(self, player):
            if player.mental < 0:
                player.mental -= 100 * f()
            else:
                player.mental = r2(0.5 * player.mental)
            player.severity += 0.02
            ConcDec.add(player, 2)
            ConsDec.add(player, 2)
            Inspiration.add(player, 3)
            if not player.s4 and player.week >= 2 and MentProb.has(player) and player.today in (6, 7) and player.hal_p != 11:
                renpy.jump("solitus_route_4")

    class Cigarette(Item):
        id = 223
        name = _('香烟')
        kind = _('食物')
        maxCd = 0
        maxDu = 28
        reuse = False
        isUnique = False
        info = _('使用后消耗20%的精神状态，低于0时固定降低100点。\n获得1层灵感，2~3层清醒。\n近期抽过烟使用将不会获得更多效果，同时还会提升严重程度。')
        ad = _('抽烟的人通常短命，它和我算是绝配。')

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
                    s += Smoking.getstack(player)
                Entrance.add(player, ra(player, 2, 3)+s)
    
    class SolitusCookie(Item):
        id = 224
        name = _('一袋社畜饼干')
        kind = _('食物')
        maxCd = 2
        maxDu = -1
        reuse = False
        isUnique = False
        info = _('使用后有概率随机提升1%能力属性。')
        ad = _('尝起来像你自己。')

        def useItemAction(self, player):
            temp = rd(1,5)
            if temp == 3:
                player.workingRegarded += 0.01
                Notice.add(_('工作能力提升了1%！'))
            elif temp == 4:
                player.physicalRegarded += 0.01
                Notice.add(_('身体素质提升了1%！'))
            elif temp == 5:
                player.writingRegarded += 0.01
                Notice.add(_('写作技巧提升了1%！'))
            
            player.fooduse += 1
            Notice.add(_('降低了0.5%食物的恢复效果！'))

        

    class HallukeCookie(Item):
        id = 225
        name = _('一袋小熊饼干')
        kind = _('食物')
        maxCd = 2
        maxDu = -1
        reuse = False
        isUnique = False
        info = _('使用后获得放松。')
        ad = _('尝起来像一维生物。')

        def useItemAction(self, player):
            ConsDec.add(player)
            player.fooduse += 1
            Notice.add(_('降低了0.5%食物的恢复效果！'))
    
    class AcolasCookie(Item):
        id = 226
        name = _('一袋坏狼饼干')
        kind = _('食物')
        maxCd = 2
        maxDu = -1
        reuse = False
        isUnique = False
        info = _('使用后获得兴奋。')
        ad = _('尝起来像99层过劳。')

        def useItemAction(self, player):
            ConcInc.add(player)
            player.fooduse += 1
            Notice.add(_('降低了0.5%食物的恢复效果！'))
    
    class PathosCookie(Item):
        id = 227
        name = _('一袋医生饼干')
        kind = _('食物')
        maxCd = 2
        maxDu = -1
        reuse = False
        isUnique = False
        info = _('使用后获得紧张。')
        ad = _('尝起来像鱼鳃。')

        def useItemAction(self, player):
            ConsInc.add(player)
            player.fooduse += 1
            Notice.add(_('降低了0.5%食物的恢复效果！'))
    
    class DecayCookie(Item):
        id = 228
        name = _('一袋消防员饼干')
        kind = _('食物')
        maxCd = 2
        maxDu = -1
        reuse = False
        isUnique = False
        info = _('使用后获得睡意。')
        ad = _('尝起来像脑浆。')
 
        def useItemAction(self, player):
            ConcDec.add(player)
            player.fooduse += 1
            Notice.add(_('降低了0.5%食物的恢复效果！'))


    class CreamCake(Item):
        id = 229
        name = _('小块奶油蛋糕')
        kind = _('食物')
        maxCd = 1
        maxDu = 7
        reuse = False
        isUnique = False
        info = _('使用后恢复精神状态，移除1层焦虑或过劳。')
        ad = _('平淡的美味。')
 
        def useItemAction(self, player):
            rec = r2(20 * player.useFoodScale())
            player.mental += rec
            Notice.add(_('恢复了%s点精神状态！') % rec)
            for i in (MentProb, PhysProb):
                if i.has(player):
                    i.subByType(player)
                    break
            Satiety.add(p)
            player.fooduse += 1
            Notice.add(_('降低了0.5%食物的恢复效果！'))


    class StrawberryCake(Item):
        id = 230
        name = _('小块草莓蛋糕')
        kind = _('食物')
        maxCd = 1
        maxDu = 7
        reuse = False
        isUnique = False
        info = _('使用后恢复精神状态，额外恢复当前15%的精神状态，降低1点严重程度。')
        ad = _('你最喜欢的味道。')
 
        def useItemAction(self, player):
            rec = r2(20 * player.useFoodScale() + player.mental * 0.15)
            player.mental += rec
            player.severity -= 0.01
            Notice.add(_('恢复了%s点精神状态。') % rec)
            Notice.add(_('降低了1点严重程度！'))
            Satiety.add(p)
            player.fooduse += 1
            Notice.add(_('降低了0.5%食物的恢复效果！'))


    class OrangeCake(Item):
        id = 231
        name = _('小块香橙蛋糕')
        kind = _('食物')
        maxCd = 1
        maxDu = 7
        reuse = False
        isUnique = False
        info = _('使用后恢复精神状态，获得紧迫，安逸，恐惧，渴求，悲伤或澎湃其中之一的状态。')
        ad = _('他最喜欢的味道。')
 
        def useItemAction(self, player):
            rec = r2(20 * player.useFoodScale())
            player.mental += rec
            Notice.add(_('恢复了%s点精神状态！') % rec)
            l = list(filter(lambda x: not x.has(player), (Restlessness, Contentment, Desire, Sadness, Agony, Dread)))
            if l:
                rca(player, l).add(player)
            Satiety.add(p)
            player.fooduse += 1
            Notice.add(_('降低了0.5%食物的恢复效果！'))
    

    


    ########################################################################################

    class HallukeItem1(Item):
        id = 500
        name = _('{color=#9500ff}Halluke的旧护膝{/color}')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1  # 数字
        isUnique = True
        canQuit = False
        info = _('身体素质+15%。\n体魄恢复的精神状态+50%。\n体魄消失的概率-50%。\n身体素质获取加成提升1点。')
        ad = _('对他来说正好的护膝在你腿上就有些稍紧了，不过无论如何，都是从他身上换下来的装备。\n当你面对着这件道具时，心里总有一种莫名的冲动。')

        def enableAction(self, player):
            if AcolasItem1.has(player):
                Achievement300.achieve()
                Achievement.show()
            player.physicalRegarded += 0.15
            player.physicalGain += 0.01

        def disableAction(self, player):
            player.physicalRegarded -= 0.15
            player.physicalGain -= 0.01

    class AcolasItem1(Item):
        id = 510
        name = _('{color=#9500ff}Acolas的旧笔记{/color}')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1  # 数字
        isUnique = True
        canQuit = False
        info = _('工作能力+15%。\n工作速度+15%。\n工作消耗的精神状态-30%。\n工作能力获取加成提升1点。')
        ad = _('都是他还在上大学的时候写下的学习笔记，不仅包含了基础知识，还有各种面试会考到的例题。\n无论是完整度还是十分干练的手写体都可以称得上完美一词。')

        def enableAction(self, player):
            if HallukeItem1.has(player):
                Achievement300.achieve()
                Achievement.show()
            player.workingRegarded += 0.15
            player.workingGain += 0.01
            player.workSpeed += 0.15

        def disableAction(self, player):
            player.workingRegarded -= 0.15
            player.workingGain -= 0.01
            player.workSpeed -= 0.15
    

    class AcolasItem2(Item):
        id = 511
        name = _('Acolas的未完成作品（阶段1）')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1  # 数字
        isUnique = True
        canQuit = False
        info = _('需要完善基础结构和程序源码的设计稿。')

        def __init__(self, player):
            super(AcolasItem2, self).__init__(player)
            self.progress = 0
        
        @classmethod
        def getPrincipalInfo(cls):
            pro_info = ''
            type_info = _('\n\n') + cls.kind
            if cls.has(p):
                pro_info = _('\n\n已完成进度：%s%s\n') % (cls.get(p).progress, '%')

            if cls.isUnique:
                if not cls.has(p):
                    uni_info = _('\n唯一\n\n{color=#ffff00}未拥有{/color}')
                else:
                    uni_info = _('\n唯一')
            else:
                uni_info = ''

            return cls.info + type_info + pro_info + uni_info
    

    class AcolasItem3(Item):
        id = 512
        name = _('Acolas的未完成作品（阶段2）')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1  # 数字
        isUnique = True
        canQuit = False
        info = _('需要加入游戏剧情和文案的设计稿。')

        def __init__(self, player):
            super(AcolasItem3, self).__init__(player)
            self.progress = 0
        
        @classmethod
        def getPrincipalInfo(cls):
            pro_info = ''
            type_info = _('\n\n') + cls.kind
            if cls.has(p):
                pro_info = _('\n\n已完成进度：%s%s\n') % (cls.get(p).progress, '%')

            if cls.isUnique:
                if not cls.has(p):
                    uni_info = _('\n唯一\n\n{color=#ffff00}未拥有{/color}')
                else:
                    uni_info = _('\n唯一')
            else:
                uni_info = ''

            return cls.info + type_info + pro_info + uni_info

    
    class AcolasItem4(Item):
        id = 513
        name = _('Acolas的未完成作品（阶段3）')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1  # 数字
        isUnique = True
        canQuit = False
        info = _('需要为整体润色的设计稿。')

        def __init__(self, player):
            super(AcolasItem4, self).__init__(player)
            self.progress = 0
        
        @classmethod
        def getPrincipalInfo(cls):
            pro_info = ''
            type_info = _('\n\n') + cls.kind
            if cls.has(p):
                pro_info = _('\n\n已完成进度：%s%s\n') % (cls.get(p).progress, '%')

            if cls.isUnique:
                if not cls.has(p):
                    uni_info = _('\n唯一\n\n{color=#ffff00}未拥有{/color}')
                else:
                    uni_info = _('\n唯一')
            else:
                uni_info = ''

            return cls.info + type_info + pro_info + uni_info



    class SteamerTicket(Item):
        id = 599
        name = _('{color=#9500ff}德里莫号船票{/color}')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1
        isUnique = False
        canQuit = False
        info = _('凭此船票登上德里莫号。')
        ad = _('“知名轮船酒店德里莫号将停泊于A市，于本周末，登船享受一日住店，绕海域一圈，甲板开放，房间整洁，享受美妙海上风光。”')


    class Sticker59(Item):
        id = 600
        name = _('{color=#9500ff}59号贴纸{/color}')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1
        isUnique = True
        canQuit = False
        info = _('全部属性提升了。')  # 普通结局获得 持有本收藏品可进入真结局
        ad = _('白色的方形贴纸，中央打印着黑色的数字59，你似乎十分熟悉这个数字，但又完全回忆不起来。')

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
        name = _('{color=#9500ff}苹果汽水标签{/color}')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1
        isUnique = True
        canQuit = False
        info = _('在商店中解锁可购买道具：苹果汽水。')  # 真结局获得
        ad = _('红色的标签上打印着夸张的字体，是？？？喜欢喝的汽水品牌。')

    class CitrusJuiceSticker(Item):
        id = 602
        name = _('{color=#9500ff}橘子汽水标签{/color}')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1
        isUnique = True
        canQuit = False
        info = _('在商店中解锁可购买道具：橘子汽水。')  # pa结局获得
        ad = _('橙色的标签上打印着夸张的字体，是？？？喜欢喝的汽水品牌。')


    class ExaminationReport(Item):
        id = 603
        name = _('{color=#9500ff}A市医院体检报告单{/color}')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1
        isUnique = True
        canQuit = False
        info = _('购买实验药物的消费降低15%。')  # 治愈结局获得 不写效果了到时候直接用has查
        ad = _('上面记录着你所有的标准体检报告内容，医师结语为一切正常，但你仍被痛苦困扰着。')

    class PlaceboBottle(Item):
        id = 604
        name = _('{color=#9500ff}空的安慰剂药瓶{/color}')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1
        isUnique = True
        canQuit = False
        info = _('大幅提升药物的治疗效果，因为你相信。')  # 安慰剂结局获得
        ad = _('骗子不仅需要具备欺骗他人的能力，更要懂得欺骗自己的内心。')

        def enableAction(self, player):
            player.drugRecovery += 0.2

        def disableAction(self, player):
            player.drugRecovery -= 0.2

    
    class PathosDoll(Item):
        id = 605
        name = _('{color=#9500ff}黑色狮子玩偶{/color}')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1
        isUnique = False
        info = _('持有时，休息日的操作界面中会解锁该道具的立绘。')
        ad = _('这东西太几把难夹到了。')


    class BadmintonRacket(Item):
        id = 610
        name = _('羽毛球拍')
        kind = _('收藏品')
        maxCd = -1
        maxDu = 14  # 数字
        isUnique = True
        info = _('身体素质提升5%。')
        ad = _('普通的球拍，对你来说使用起来十分顺手。')

        def enableAction(self, player):
            player.physicalRegarded += 0.05

        def disableAction(self, player):
            player.physicalRegarded -= 0.05


    class Humidifier(Item):
        id = 611
        name = _('小型加湿器')
        kind = _('收藏品')
        maxCd = -1
        maxDu = 28  # 数字
        isUnique = True
        info = _('降低10%睡眠消耗的精神状态。')
        ad = _('桶面造型的加湿器，让你在干燥的夜晚入眠。')

        def enableAction(self, player):
            player.deteriorateConsumption -= 0.1

        def disableAction(self, player):
            player.deteriorateConsumption += 0.1


    class MusicBox(Item):
        id = 612
        name = _('八音盒')
        kind = _('收藏品')
        maxCd = -1
        maxDu = 28  # 数字
        isUnique = True
        info = _('每日有概率降低严重程度。')
        ad = _('转动发条便可以周而复始地播放一首十分经典的名为《Myosotis》的曲目。')

        def afterSleepAction(self, player):
            if not self.broken:
                if rra(player, 50):
                    player.severity -= 0.01
                    Notice.add(_('由于八音盒，降低了1点严重程度。'))


    class ClockTower(Item):
        id = 613
        name = _('钟塔摆件')
        kind = _('收藏品')
        maxCd = -1
        maxDu = 28  # 数字
        isUnique = True
        info = _('起床后随机恢复少量精神状态。')
        ad = _('小巧精致的钟塔模型，据说是还原了已经失落的国家“阿斯卡隆”的建筑风格制成的。')

        def afterSleepAction(self, player):
            if not self.broken:
                r = ra(player, 7.5, 15)
                Notice.add(_('由于钟塔摆件，恢复了%s点精神状态。') % r)
                player.mental += r



    class GymTicket(Item):
        id = 614
        name = _('健身房的有效会员卡')
        kind = _('收藏品')
        maxCd = -1
        maxDu = 1
        isUnique = True
        info = _('持有有效的会员卡可以进入健身房，仅本日有效。')
        ad = _('Topaz健身房的会员卡，上面印有琥珀色的logo。')

        def timeUpAction(self, player):
            GymBrokenTicket.add(player)
            player.items.remove(self)
            

    class GymBrokenTicket(Item):
        id = 615
        name = _('健身房的无效会员卡')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1
        isUnique = False
        info = _('物品仅有收藏价值。')
        ad = _('Topaz健身房的会员卡，上面印有琥珀色的logo。')

    class WriterProof(Item):
        id = 616
        name = _('金牌作者证明')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1
        isUnique = True
        info = _('严重程度百分比降低，收到的委托更容易出现更高的价格修正。')
        ad = _('写作平台的作者证明，你的粉丝已经破万了，这是你不曾想过的。')

        def enableAction(self, player):
            player.severityRegarded -= 0.15

        def disableAction(self, player):
            player.severityRegarded += 0.15

    class VipCard(Item):
        id = 617
        name = _('夜店Vip卡')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1
        isUnique = False
        info = _('物品仅有收藏价值。')
        ad = _('上面写着一家名为“Endorphins”的男同酒吧地址以及详细信息，联系方式是……\n谁会想去这种地方啊！而且我为什么要收集这东西啊！')

    class SexyPic(Item):
        id = 618
        name = _('色情照片')
        kind = _('收藏品')
        maxCd = 1
        maxDu = -1
        isUnique = False
        reuse = False
        info = _('使用后获得勃起。')
        ad = _('知名男演员于秀爱的色情写真，照片里的他裸体坐在白色的大床中央，双手向后支撑身体，而身边则围绕一群肌肉雄兽……\n我焯太烧辣，我不行了，兄弟们我先冲啦！')

        def useItemAction(self, player):
            Erection.add(player)

    class TomatoBrooch(Item):
        id = 620
        name = _('番茄胸针')
        kind = _('收藏品')
        maxCd = -1
        maxDu = 28
        isUnique = True
        info = _('降低5%的严重性。')
        ad = _('十分漂亮，但胸针如果放在衣服上又太张扬，放在包上又很容易被蹭掉或者偷走……总之还是放在抽屉里最安全……')

        def enableAction(self, player):
            player.severityRegarded -= 0.05

        def disableAction(self, player):
            player.severityRegarded += 0.05
        

    class PaperStar(Item):
        id = 621
        name = _('千纸鹤')
        kind = _('收藏品')
        maxCd = 1
        maxDu = -1
        isUnique = False
        reuse = False
        info = _('使用后有概率获得灵感，未获得则恢复少量精神状态。')
        ad = _('真的有人会折这东西折几千个吗？')

        def enableAction(self, player):
            if rra(player, 30):
                Inspiration.add(player)
            else:
                r = ra(player, 2, 7)
                Notice.add(_('由于千纸鹤，恢复了%s点精神状态。') % r)
                player.mental += r

    
    class Flower1(Item):
        id = 622
        name = _('一束木兰')
        kind = _('收藏品')
        maxCd = -1
        maxDu = 5
        isUnique = True
        info = _('持有时，降低5%的严重程度。\n\n无法被维修工具组修复。')
        ad = _('花语：高尚的灵魂。')

        def enableAction(self, player):
            player.severityRegarded -= 0.05
        
        def disableAction(self, player):
            player.severityRegarded += 0.05

    
    class Flower2(Item):
        id = 623
        name = _('一把勿忘我')
        kind = _('收藏品')
        maxCd = -1
        maxDu = 5
        isUnique = True
        info = _('持有时，每天结束后获得1层灵感。\n\n无法被维修工具组修复。')
        ad = _('花语：请不要忘记我真诚的爱。')

        def afterSleepAction(self, player):
            if not self.broken:
                if not Inspiration.has(player):
                    Inspiration.add(player, 1)
                    Inspiration.get(player).duration += 1
                else:
                    Inspiration.add(player, 1)

    
    class Flower3(Item):
        id = 624
        name = _('一捧万寿菊')
        kind = _('收藏品')
        maxCd = -1
        maxDu = 5
        isUnique = True
        info = _('持有时，每天结束后移除一层焦虑。\n\n无法被维修工具组修复。')
        ad = _('花语：健康长寿。')

        def afterSleepAction(self, player):
            if not self.broken:
                MentProb.subByType(player)

    
    class Sneakers(Item):
        id = 625
        name = _('运动鞋')
        kind = _('收藏品')
        maxCd = -1
        maxDu = 14  # 数字
        isUnique = True
        info = _('身体素质提升5%。')
        ad = _('穿上它，你就不用穿休闲鞋去打羽毛球了。')

        def enableAction(self, player):
            player.physicalRegarded += 0.05

        def disableAction(self, player):
            player.physicalRegarded -= 0.05

    class FileFolder(Item):
        id = 626
        name = _('档案夹套装')
        kind = _('收藏品')
        maxCd = -1
        maxDu = 14  # 数字
        isUnique = True
        info = _('工作能力提升5%。')
        ad = _('一大堆五颜六色的档案夹，可以分类各种各样的纸质数据。')

        def enableAction(self, player):
            player.workingRegarded += 0.05

        def disableAction(self, player):
            player.workingRegarded -= 0.05

    
    class NotePad(Item):
        id = 627
        name = _('记事本')
        kind = _('收藏品')
        maxCd = -1
        maxDu = 14  # 数字
        isUnique = True
        info = _('工作能力提升5%。')
        ad = _('包装精美的记事本，可以用来记录会议内容。')

        def enableAction(self, player):
            player.workingRegarded += 0.05

        def disableAction(self, player):
            player.workingRegarded -= 0.05

    class FixKit(Item):
        id = 628
        name = _('维修工具组')
        kind = _('工具')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('使用后选择一个带有耐久度的收藏品，将其耐久度恢复至最大值。')
        ad = _('曾经这个道具是一瞬间修好所有道具，后来主角说这是压榨，于是现在就变成只修一个道具了。')

        def use(self, player):
            renpy.show_screen(_screen_name='fix_select', player=player)
            
        def useItem(self, player, i):
            if self.checkAvailable(player) != True:
                Notice.add(self.checkAvailable(player))
            else:
                Stat.record(player, type(self))
                Notice.add(_('已使用物品：')+ self.name)
                if self.maxCd>0:
                    player.itemcd[type(self)] = self.maxCd 
                i.get(player).du = i.maxDu
            Notice.show()
            

    class Knife(Item):
        id = 629
        name = _('水果刀')
        kind = _('工具')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('使用后获得受伤和痛苦，同时获得大量精神状态，并降低3%的严重程度倍率。')
        ad = _('“没事的。\n虽然看起来很痛，但伤痕不算什么的。\n因为真正痛的并不是手腕。”')

        def useItemAction(self, player):
            renpy.transition(Dissolve(0.2), layer='master')
            renpy.show("veinmask")

            MentPun.clearByType(p)
            MentProb.clearByType(p)
            Injured.add(p)
            p.checkTask()
            Pain.add(p)
            
            rec = r2(ra(player, 6000, 9000)*0.01)
            player.severityRegarded -= 0.03
            player.mental += rec
            Notice.add(_('将手腕出划开数道伤口后，恢复了%s点精神状态。')%rec)

    
    class Bondage(Item):
        id = 630
        name = _('外科医疗工具组')
        kind = _('工具')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('如果已经受伤，在使用之后的每天结束时，根据恢复率自动恢复受伤，并获得全额的恢复奖励。\n如果没有受伤则什么也不会发生。')
        ad = _('和你在某大型拼单电商网站发的广告上只卖九块九得工具组差不多，附赠的那瓶医用酒精里好像还有小黑点在蠕动。')

        def useItemAction(self, player):
            if Injured.has(p):
                Injured.get(p).stacks=0
                Notice.add(_('你将伤口消毒并用绷带包扎好自己的受伤部位，希望它能自己复原。'))
            else:
                Notice.add(_('你将伤口消毒并用绷带包扎好自己的受伤部位……等等，你并没有受伤啊，你到底在干什么？'))

    class RecordingPen(Item):
        id = 631
        name = _('录音笔')
        kind = _('工具')
        maxCd = 7
        maxDu = -1  # 数字
        isUnique = True
        info = _('使用后将一半的灵感等量转化成写作素材，同时延长未转化的灵感的持续时间至最大值。')
        ad = _('按我来看，如果你有空去录音然后再找时间转化成文字，还不如拿出刷短视频的功夫直接码字……算了，这只是个游戏，不要计较太多。')

        def useItemAction(self, player):
            if Inspiration.has(p):
                g = int(Inspiration.getstack(player) * 0.5)
                Inspiration.get(p).stacks -= g
                Inspiration.get(p).duration = Inspiration.maxDuration
                FixedInspiration.add(player, g)

    
    class FasciaGun(Item):
        id = 632
        name = _('筋膜枪')
        kind = _('工具')
        maxCd = 7
        maxDu = -1  # 数字
        isUnique = True
        info = _('使用后全部的酸痛转化为1层体魄。')
        ad = _('对于你来说这东西的主战场可能不是肌肉而是……')

        def useItemAction(self, player):
            if Soreness.has(p):
                Soreness.clearByType(player)
                Physique.add(p)

    class Fridge(Item):
        id = 633
        name = _('小型冰箱')
        kind = _('工具')
        maxCd = 0
        maxDu = -1  # 数字
        isUnique = True
        info = _('可以将食物放入其中使其停止计算持续时间，最多容纳3件食物。')
        ad = _('透ki哟透马磊！')
        maxstore = 3

        def use(self, player):
            renpy.show_screen(_screen_name='fridge_check', player=player, fridge=self)

        def __init__(self, player):
            super(Fridge, self).__init__(player)
            self.items = [None] * self.maxstore

        def store(self):
            store = 0
            for i in self.items:
                store += i.amounts
            return store

        def canput(self):
            if self.store() < self.maxstore:
                return True
            return _('小型冰箱已满。')

        def put(self, player, item, poz):
            putitem = dcp(item)
            item.sub(player)
            putitem.amounts = 1
            self.items[poz] = putitem

        def take(self, player, poz):
            if self.items[poz] in player.items:
                oldItem = type(self.items[poz]).getByItem(player, self.items[poz])
                oldItem.addStackAction(player)
                oldItem.amounts += 1
            else:
                takeitem = dcp(self.items[poz])
                player.items.append(takeitem)

            self.items[poz] = None

    class Cactus(Item):
        id = 634
        name = _('仙人掌盆栽')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1
        isUnique = True
        info = _('持有时，解锁仙人掌盆栽，在公司时可以为其浇水。')
        ad = _('应该不需要每天都浇水，对吧？')

        def __init__(self, player):
            super(Cactus, self).__init__(player)
            self.progress = 0
            self.level = 1
            self.wet = 50

        def water(self, player):
            renpy.sound.play(audio.watering)
            self.wet += ra(player, 90, 120)
            if self.wet >= 1000:
                Achievement308.achieve()
                Achievement.show()

        def sprite(self):
            return 'gui/object/cactus_%s.png' % self.level

        def cond_info(self):
            if self.wet < -120:
                return _('看上去仙人掌正在享受转化为仙人掌干的进程。')
            if self.wet < -20:
                return _('看上去有些干燥。')
            if self.wet < 30:
                return _('看上去还行。')
            if self.wet < 70:
                return _('看上去不错。')
            if self.wet < 100:
                return _('看上去比较湿润。')
            if self.wet < 120:
                return _('看上去过于湿润了。')
            if self.wet >= 1000:
                return _('你一定是疯了。')

            return _('看上去仙人掌正在享受泥浆泡泡浴。')

        def developer_info(self, player):
            if not config.developer and not CactusCheat.has(player):
                return None
            deathpercent = 0
            if self.wet < -120:
                deathpercent = int(min(100, (-120 - self.wet)*2))
            if self.wet > 120:
                deathpercent = int(min(100, (self.wet - 120)*2))
            
            growpercent = int(max(min(100, 120 - abs(self.wet - 50) * 1.5), 10))
            return _('等级：%s\n成长度：%s%s\n湿润度：%s\n\n死亡概率：%s%s\n成长概率：%s%s') % (self.level, int(self.progress*100/7), '%', self.wet, deathpercent, '%', growpercent, '%')

        def afterSleepAction(self, player):
            if self.wet < -120:
                if rra(player, (-120 - self.wet)*2):
                    DeadCactus.add(player)
                    player.items.remove(self)
                    return

            if self.wet > 120:
                if rra(player, (self.wet - 120)*2):
                    DeadCactus.add(player)
                    player.items.remove(self)
                    return

            if rra(player, max(10, 120 - abs(self.wet - 50) * 1.5)):  # 0~70
                self.progress += 1
            
            if self.progress >= 7:
                self.progress = 0
                self.level += 1
            
            if self.level >= 7:
                WellCactus.add(player)
                player.items.remove(self)
                return
            
            self.wet -= ra(player, 15, 25)
    
    class WellCactus(Item):
        id = 635
        name = _('盛开的仙人掌盆栽')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1
        isUnique = True
        info = _('持有时，降低20%的严重度倍率。')
        ad = _('你人生中仅有的值得你骄傲的东西。')

        def enableAction(self, player):
            Achievement306.achieve()
            Achievement.show()
            player.severityRegarded -= 0.2

        def disableAction(self, player):
            player.severityRegarded += 0.2

        def sprite(self):
            return 'gui/object/cactus_7.png'

        def __init__(self, player):
            super(WellCactus, self).__init__(player)
            self.progress = 0
            self.level = 7
            self.wet = 50

        def water(self, player):
            renpy.sound.play(audio.watering)
            self.wet += ra(player, 90, 120)
            if self.wet >= 1000:
                Achievement308.achieve()
                Achievement.show()

        def developer_info(self, player):
            if not config.developer and not CactusCheat.has(player):
                return None
            return _('等级：%s\n成长度：%s%s\n湿润度：%s') % (self.level, int(self.progress*100/7), '%', self.wet)


        def cond_info(self):
            if self.wet < -240:
                return _('也许你已经忘记里这里存在着一盆盛开的仙人掌，土壤干燥得像是沙漠。\n不过盛开的仙人掌为了不让你伤心，它挺住了干旱。')
            if self.wet < -120:
                return _('盛开的仙人掌说如果再干燥一点，对于其他仙人掌来说就危险了。')
            if self.wet < -20:
                return _('盛开的仙人掌说如果现在浇水的话就正好了。')
            if self.wet < 30:
                return _('盛开的仙人掌说现在有些干燥，不过还能撑得住。')
            if self.wet < 70:
                return _('盛开的仙人掌说它觉得在这个区间内最舒服。')
            if self.wet < 100:
                return _('盛开的仙人掌说现在有些潮湿，不过还能撑得住。')
            if self.wet < 120:
                return _('盛开的仙人掌说如果再潮湿一点，对于其他仙人掌来说就危险了。')
            if self.wet >= 1000:
                return _('盛开的仙人掌知道你疯了，但没关系，因为它是盛开的仙人掌，它愿意为了你变成水生植物。\n只要你喜欢。')

            return _('看上去盛开的仙人掌正在享受泥浆泡泡浴。\n不过盛开的仙人掌为了不让你伤心，它挺住了洪涝。')

        def afterSleepAction(self, player):           
            self.wet -= ra(player, 15, 25)
            self.progress += 1

    class DeadCactus(Item):
        id = 636
        name = _('死亡的仙人掌盆栽')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1
        isUnique = True
        info = _('持有时，提升20%的严重度倍率。')
        ad = _('仙人掌你都养不活，你还能干点啥？')

        def cond_info(self):
            return _('这东西已经开始发烂发臭了。')

        def sprite(self):
            return 'gui/object/cactus_0.png'

        def developer_info(self, player):
            return None

        def enableAction(self, player):
            player.severityRegarded += 0.2

        def disableAction(self, player):
            player.severityRegarded -= 0.2

    class CactusFood(Item):
        id = 637
        name = _('仙人掌肥料')
        kind = _('食物')
        maxCd = 7
        maxDu = 90
        reuse = False
        isUnique = False
        info = _('拥有仙人掌盆栽时，提升仙人掌的成长度。')
        ad = _('好吧，这东西也能被归类到食物中吗？')

        def sound(self):
            renpy.sound.play(audio.itemdefault)

        def checkAvailable(self, player):
            if self.broken:
                return _('物品已过期！不可被使用！')
            if not Cactus.has(player):
                return _('你需要先拥有一盆仙人掌盆栽。')
            if type(self) not in player.itemcd:
                return True
            else:
                return _('物品仍在冷却时间中！')

        def useItemAction(self, player):
            if Cactus.has(player):
                cactus = Cactus.get(player)
                cactus.progress += 1
                
                if cactus.progress >= 7:
                    cactus.progress = 0
                    cactus.level += 1
                
                if cactus.level >= 7:
                    WellCactus.add(player)
                    player.items.remove(cactus)

    class ToyDuck(Item):
        id = 638
        name = _('小黄鸭')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1
        isUnique = True
        info = _('持有时，解锁小黄鸭，在公司时可以点击。')
        ad = _('这个东西存在的意义是什么……')

    class CactusCheat(Item):
        id = 639
        name = _('仙人掌养殖指南')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1
        isUnique = True
        info = _('持有时，可以查看仙人掌的具体状态。')
        ad = _('总得有人看到这个精致的仙人掌数据界面，对吧？')


    class ChaoticPendulum(Item):
        id = 696
        name = _('混沌摆')
        kind = _('工具')
        maxCd = 0
        maxDu = -1  # 数字
        isUnique = True
        info = _('使用后允许快速跳过日程的等待时间，过夜动画以及强制加载的时间。\n再次使用可以切换为关闭模式。')
        ad = _('“我猜玩家80%的游玩时间或许都是盯着加载的几个句号看。”')

        @classmethod
        def getPrincipalInfo(cls):
            state_info = '{color=#fde827}快进模式：启动中{/color}\n\n' if persistent.nowaiting else '{color=#006eff}快进模式：未开启{/color}\n\n'
            type_info = '\n\n' + cls.kind

            if cls.isUnique:
                if not cls.has(p):
                    uni_info = _('\n唯一\n\n{color=#fde827}未拥有{/color}')
                else:
                    uni_info = _('\n唯一')
            else:
                uni_info = ''

            return state_info + cls.info + type_info + uni_info

        def useItemAction(self, player):
            if persistent.nowaiting:
                persistent.nowaiting = False
            else:
                persistent.nowaiting = True

    class Sandglass(Item):
        id = 697
        name = _('奇怪的沙漏')
        kind = _('工具')
        maxCd = 0
        maxDu = -1  # 数字
        isUnique = True
        info = _('使用后穿越到下个周五的早上，同时完成本周所有的工作。\n使用后视为作弊，不会获得生存分数。')
        ad = _('“垃圾游戏真的没意思，我就想看个剧情不行？”')

        def checkAvailable(self, player):
            if player.week >= 14 or AcolasItem4.has(player):
                return _('似乎什么都没有发生。')
            return True

        def sound(self):
            renpy.sound.play(audio.sandglass)

        def useItemAction(self, player):
            player.onOutside = False
            player.onVacation = False
            player.cheat = True
            player.achievedGoal = player.goal + 0.01
            for i in range(8):
                player.dateChange()
                if player.today==5:
                    break
            if WeatherTornado.has(player):
                WeatherTornado.clearByType(player)
                WeatherSunny.add(player)
            renpy.jump('sandglass_label')

    class TicketRoot(Item):
        id = 698
        name = _('票根')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1
        isUnique = False
        info = _('物品仅有收藏价值。')
        ad = _('一大堆花里胡哨的票根，火车票电影票游泳馆入场券展览馆入场券应有尽有。')

    class Trash(Item):
        id = 699
        name = _('杂物')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1
        isUnique = False
        info = _('物品仅有收藏价值。')
        ad = _('心血来潮买的乱七八糟的小摆件，至少它们曾经让你开心过，或者没有，但那已经不重要了，现在你已经对它们失去了兴趣。')


    class UnfinishedCommission(Item):
        id = 700
        name = _('未完成的文稿')
        kind = _('文稿')
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
            info2 = _('\n\n已完成字数：')+str(cInfo[0])+_('\n文稿总价值：')+str(cInfo[1])+_('\n共消耗灵感：')+str(cInfo[2])

            return info1 + info2

        def write(self, player):
            cms = self.comm.write(player)
            player.items.append(cms)
            self.remove(player)


    class FinishedCommission(Item):
        id = 701
        name = _('已完成的文稿')
        kind = _('文稿')
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
            info2 = _('\n\n已完成字数：')+str(cInfo[0])+_('\n文稿总价值：')+str(cInfo[1])+_('\n共消耗灵感：')+str(cInfo[2])

            return info1 + info2

        def getReward(self, player):
            money = r2(self.comm.contentInfo()[1])
            ins = int(0.2 * self.comm.contentInfo()[2])
            if money <= 0:
                money = 0.0
            player.money += money
            
            Notice.add(_('完成委托！'))

            if money>0:
                Notice.add(_('获得了%s元报酬。') % money)
            else:
                Notice.add(_('未获得报酬！'))

            if ins > 0:
                FixedInspiration.add(player, ins)
                Notice.add(_('获得了%s层写作素材！') % ins)
            else:
                Notice.add(_('未获得新的写作素材！'))

            if not WriterProof.has(player) and player.popularity >= 10000:
                Notice.add(_('由于您的粉丝数已经超过一万，平台特颁发作家证明，以资鼓励。'))
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
                Notice.add(_('已将文稿发布到写作平台！\n平台没有新增粉丝。'))
            elif up < 0:
                player.popularity += up
                Notice.add(_('已将文稿发布到写作平台！\n流失了%s个新粉丝。') % up)
            else:
                if up+player.popularity > 40000:
                    up = 40000 - player.popularity
                player.popularity += up
                Notice.add(_('已将文稿发布到写作平台！\n涨了%s个新粉丝。') % up)

            if ins > 0:
                FixedInspiration.add(player, ins)
                Notice.add(_('恢复了%s层灵感！') % ins)

            if not WriterProof.has(player) and player.popularity >= 10000:
                Notice.add(_('由于您的粉丝数已经超过一万，平台特颁发作家证明，以资鼓励。'))
                WriterProof.add(player)
            
            Notice.show()
            self.remove(player)
            

    def wr(p):
        Inspiration.add(p, 10)
        FreewheelingWriting.executeTask(p)
        Notice.show()

