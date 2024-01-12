init -10 python early:

    

    class MedicineA(MedicineBase):
        id = 100
        name = _('药物{font=arial.ttf}α{/font}')
        kind = _('实验药物')
        info = _('在起床时使用该药物时，恢复额外的精神状态。')
        ad = _('“目前还不明确具体的使用频率，药物使用频率依你的头疼剧烈程度而定。我的建议是早上吃，等你头再疼的时候继续吃……另外一周后就不要再用上一周的过期药物了……”\n我的主治医师Pathos在我每次买药之前都会和我念叨一遍，我都听腻了，难道他真以为我是那种什么都记不住的三岁小孩吗？')

        @property
        def e_(self):
            return DrugEA

        @classmethod
        def getSpecEffects(cls, player):
            if p.times == 0:
                return 1 + (0.4 - 0.04 * player.week)
            return 1.0

        @classmethod
        def recovery(cls, player, prev=False):
            rec = 90
            if player.times == 0 or player.times == 101:
                rec *= 1 + (0.4 - 0.04 * player.week)
                #Notice.add(_('在起床时使用，恢复了额外30%的精神状态。'))
            return rec


    class MedicineB(MedicineBase):
        id = 101
        name = _('药物{font=arial.ttf}β{/font}')
        kind = _('实验药物')
        info = _('当前的精神状态越少，恢复的精神状态越多，低于阈值时恢复效果将大幅度下降。')
        ad = _('“这种药只有在非常紧急的时候才能服用！因为目前了解的是这种药物服用之后会产生大量幻觉，以及各种尚不明确原因的效果……就算你喜欢这种幻觉，这药也不是为了让你当合法致幻剂用的！”\n为什么不能？写东西之前把这个丢进嘴里，灵感就会像泉水似的往外喷！')

        @property
        def e_(self):
            return DrugEB

        @classmethod
        def getSpecEffects(cls, player):
            rec = (-0.6 - 0.08 * player.week) * max(-120*(1+0.1 * player.week), player.mental) + 80
            return r2(rec / 85)

        @classmethod
        def recovery(cls, player, prev=False):
  
            rec = (-0.6 - 0.08 * player.week) * max(-120*(1+0.1 * player.week), player.mental) + 80
            
            if rec < 20:
                rec = 20
                if prev==False:
                    player.gain_abi(0.02, 'sev', due='使用该药物时精神状态过高')
            
            #Notice.add(_('恢复了相当于药物基础恢复量的') + r2s(s) + _('%的精神状态。'))
            return rec


    class MedicineC(MedicineBase):
        id = 102
        name = _('药物{font=arial.ttf}γ{/font}')
        kind = _('实验药物')
        info = _('单次服用恢复较少精神状态，但每次完成日程后都会恢复较多精神状态。\n基础精神状态消耗越多，恢复的越多。')

        ad = _('“这种药物对肠胃影响很大，也会影响你的味觉，虽然没法立刻缓解头疼，但是长远来看对你的头疼恢复效果还是要比前面几种药好一点的。”\n真不喜欢吃这药，如果吃美食都没有了快乐，那我活着还有什么乐趣……')

        @property
        def e_(self):
            return DrugEC

        @classmethod
        def getSpecEffects(cls, player):
            return Task.getConsScale(player)

        @classmethod
        def recovery(cls, player, prev=False):
            return 40

        @classmethod
        def expectedReco(cls, player):
            times = 3
            if player.times >= 4:
                times -= 1
            if player.times >= 8:
                times -= 1
            if player.times >= 12:
                times -= 1

            t = 4.5 * player.week
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
        info = _('恢复大量精神状态。')
        ad = _('“你已经不需要其他的药了。”')

        def useItemAction(self, player):
            r = rd(200000, 400000) * 0.01
            if player.mental < 0:
                r += -player.mental
            player.gain_mental(r, stat=self.name)
            DrugED.add(player)
            for i in [DrugD, DrugW, DrugEA, DrugEB, DrugEC, Deterioration]:
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

            return info.rstrip() + '\n'

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
        maxCd = 1
        maxDu = 28
        reuse = False
        isUnique = False
        info = _('移除所有兴奋，降低睡眠消耗的精神状态，但会提升严重程度，并降低专注度。')
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
        maxCd = 1
        maxDu = 28
        reuse = False
        isUnique = False
        info = _('服用后降低少量专注度，若没有生病则提升严重程度。\n使用后会延长1天生病的持续时间并根据层数提升恢复率，但本效果结束时则会减少生病的持续时间。')
        ad = _('建议用水送服，没有水的话那么用酒应该也可以？')
        p=0.15

        def useItemAction(self, player):
            if PhysPun.has(player):
                DrugColdrexEffect.add(player)
            else:
                player.severity += 0.05


    class DrugIbuprofen(Item):
        id = 302
        name = _('头疼药')
        kind = _('普通药物')
        maxCd = 1
        maxDu = 28
        reuse = False
        isUnique = False
        info = _('服用后每完成一个日程随层数百分比恢复微量精神状态。')
        ad = _('也许你单纯买来当糖豆吃。')
        p=0.05

        def useItemAction(self, player):
            DrugIbuprofenEffect.add(player)

    class DrugIbuprofenB(Item):
        id = 303
        name = _('镇痛药')
        kind = _('普通药物')
        maxCd = 3
        maxDu = 28
        reuse = False
        isUnique = False
        info = _('第一次服用后提升1%的严重倍率，之后每次服用，提升的严重倍率都会翻倍，过夜不会消耗精神状态。')
        ad = _('我应该放弃这东西，但每当夜晚因痛苦无法入眠时，它便会出现在我的回忆中。')
        p=0.8

        def getPrincipalInfo(self):
            if not p:
                return self.info
            info = '\n\n使用后提升严重倍率：{color=#f00}%s%s{/color}' % (2**DrugIbuprofenBEffect_.getstack(p), '%')
            return self.info + info

        def useItemAction(self, player):
            Notice.add('由于镇痛药，提升了%s%s的严重倍率！' % (2**DrugIbuprofenBEffect_.getstack(player), '%'))
            player.severityRegarded += 2**DrugIbuprofenBEffect_.getstack(player)*0.01
            DrugIbuprofenBEffect.add(player)
            DrugIbuprofenBEffect_.add(player)

    class DrugVitamin(Item):
        id = 304
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
            if GameDifficulty1.has(player) or GameDifficulty2.has(player):
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
            if GameDifficulty1.has(player) or GameDifficulty2.has(player):
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
        p=0.75

        def useItemAction(self, player):
            if GameDifficulty1.has(player) or GameDifficulty2.has(player):
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
        info = _('在简单模式下，使用后降低2%的严重度。')
        ad = _('“比毒药更加甘甜。”')
        p=0.75

        def useItemAction(self, player):
            if GameDifficulty1.has(player) or GameDifficulty2.has(player):
                s = r2(player.severity * 0.02)
                player.gain_abi(-s, 'sev', stat=self.name)

    

    
    class DrugAspirin(Item):
        id = 309
        name = _('阿司匹林')
        kind = _('普通药物')
        maxCd = 2
        maxDu = 28
        reuse = False
        isUnique = False
        info = _('在硬核模式下，使用后使下一个日程精神状态消耗减少100%。')
        ad = _('“倘若周围一团漆黑，那就只能静等眼睛习惯黑暗。”')
        p=0.33

        def useItemAction(self, player):
            if GameDifficulty4.has(player) or GameDifficulty5.has(player):
                DrugAspirinEffect.add(player)

    class Drugdextropropoxyphene(Item):
        id = 310
        name = _('右丙氧芬')
        kind = _('普通药物')
        maxCd = 4
        maxDu = 28
        reuse = False
        isUnique = False
        info = _('在硬核模式下，使用后移除药物依赖，且一段时间内不会获得药物依赖。')
        ad = _('“我们的正常之处，就在于懂得自己的不正常。”')
        p=0.25

        def useItemAction(self, player):
            if GameDifficulty4.has(player) or GameDifficulty5.has(player):
                DrugdextropropoxypheneEffect.add(player)
                DrugD.clearByType(player)


    class DrugMethylphenidate(Item):
        id = 311
        name = _('利他林')
        kind = _('普通药物')
        maxCd = 2
        maxDu = 28
        reuse = False
        isUnique = False
        info = _('在硬核模式下，使用后使工作能力、身体素质和写作技巧提升15%，同时获得能力时额外获得1点，同时移除利他林的副作用。\n效果结束时，降低30%的专注度。')
        ad = _('“不要同情自己，同情自己是卑劣懦夫干的勾当。”')
        p=0.5

        def useItemAction(self, player):
            if GameDifficulty4.has(player) or GameDifficulty5.has(player):
                DrugMethylphenidateEffect.add(player)
                DrugMethylphenidateEffect_1.clearByType(player)

    

    class DrugAntibiotic(Item):
        id = 397
        name = _('抗生素')
        kind = _('普通药物')
        maxCd = 7
        maxDu = 28
        reuse = False
        isUnique = False
        info = _('将生病转化为3层过劳，未生病则提升严重程度。')
        ad = _('如果我是一团青霉菌。\n那么我将献给你。\n我的盘尼西林。')
        p=0.25

        def useItemAction(self, player):
            if PhysPun.has(player):
                PhysPun.clearByType(player)
                PhysProb.add(player, 3)
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
        info = _('将偏执转化为3层焦虑，未生病则提升严重程度。')
        ad = _('如果我是一株得病的小麦。\n那么我将献给你。\n我的麦角二乙酰胺。')
        p=0.25

        def useItemAction(self, player):
            if MentPun.has(player):
                MentPun.clearByType(player)
                MentProb.add(player, 3)
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
            showNotice(['什么也没有发生。'])

    ####################################################################################################

    class BookBase(Item):
        canQuit = False

        def __init__(self, player):
            super(BookBase, self).__init__(player)
            self.progress = 0
        
        def sound(self):
            pass

        def checkAvailable(self, player):
            if type(self) in player.itemcd:
                return _('书籍仍在冷却时间中！')
            if not BookQuickReadEffect.has(player) and not Freshness.has(player):
                return _('书籍只能在进行阅读日程或存在特殊状态时才可阅读！')
            if BookstoreBuff.has(player):
                return _('书店内无法速读！')
            return True

        def use(self, player): # 速读时
            if self.checkAvailable(player) != True:
                Notice.add(self.checkAvailable(player))
            else:
                self.sound()
                Notice.add(_('已阅读书籍：')+ self.name)
                player.itemcd[type(self)] = self.maxCd
                if Freshness.has(player):
                    Freshness.subByType(player)
                else:
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
        kind = _('书籍')
        maxCd = 7
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
        kind = _('书籍')
        maxCd = 14
        maxDu = -1
        isUnique = True
        info = _('当写作素材与灵感层数不低于25层时，阅读本书籍将获得10层写作素材，一定时间内写作技巧提升30%。')
        ad = _('“在写作之前，最好先花些时间在笔记本上设计人物，搜集情节，或者记下脑海中曾涌现过的东西，直到动笔的那一刻到来。”')
        bookEffect_ = BookWriEffect

        def useItemAction(self, player):
            if FixedInspiration.getstack(player) + Inspiration.getstack(player)>= 25:
                self.bookEffect_.add(player)
                FixedInspiration.add(player, 10)

    class BookConc(BookBase):
        id = 402
        name = _('《海边的于秀爱》')
        kind = _('书籍')
        maxCd = 14
        maxDu = -1
        isUnique = True
        info = _('阅读本书籍后，移除所有的焦虑和过劳，持续时间内也不会获得过劳和焦虑。')
        ad = _('“于是我们领教了世界是何等凶顽，同时又得知世界也可以变得温存和美好。”')
        bookEffect_ = BookConcEffect

        def useItemAction(self, player):
            self.bookEffect_.add(player)

    class BookPhysPun(BookBase):
        id = 403
        name = _('《呼吸训练》')
        kind = _('书籍')
        maxCd = 7
        maxDu = -1
        isUnique = True
        info = _('阅读后获得1层书籍效果，每层提升20%生病和受伤的恢复率。\n如果在效果期间成功治愈生病或受伤，则结束效果并降低2%的严重程度。\n如果未能成功治愈，则额外获得1层该状态。')
        ad = _('“我的精神需要我的身体，就像菌菇需要泥土。”')
        bookEffect_ = BookPhysPunEffect

        def useItemAction(self, player):
            self.bookEffect_.add(player)

    
    class BookQuickRead(BookBase):
        id = 404
        name = _('《量子波动速读》')
        kind = _('书籍')
        maxCd = 14
        maxDu = -1
        isUnique = True
        info = _('阅读本书籍后，你可以{color=#fde827}速读{/color}两本任意书籍。\n\n{color=#fde827}速读：可以在道具栏中直接阅读书籍而不需要进行阅读书籍的日程。{/color}')
        ad = _('“1分钟可以看完10万字的书！”\n“闭着眼睛就能和书发生感应！”\n“不需要翻开书籍就能理解书中内容！”')
        bookEffect_ = BookQuickReadEffect

        def useItemAction(self, player):
            self.bookEffect_.add(player, 2)

    class BookWor(BookBase):
        id = 405
        name = _('《保持清醒的秘诀》')
        kind = _('书籍')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('阅读本书籍将提升20%的工作速度，降低20%工作类日程消耗的精神状态，且每次进行工作类日程时，额外完成10%的当周工作量。')
        ad = _('“我为一种躁动的向往所俘。我似乎产生了某种……企图。究竟是何企图？”')
        bookEffect_ = BookWorEffect

        def useItemAction(self, player):
            self.bookEffect_.add(player)


    class BookIns(BookBase):
        id = 406
        name = _('《2001年的弹珠机》')
        kind = _('书籍')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('阅读本书籍后效果持续时间内获得灵感时额外获得2层。')
        ad = _('“迟早要失去的东西并没有太多意义. 必失之物的荣光并非真正的荣光。”')
        bookEffect_ = BookInsEffect

        def useItemAction(self, player):
            self.bookEffect_.add(player)

    class BookLevi(BookBase):
        id = 407
        name = _('《海神记》')
        kind = _('书籍')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('立刻刷新所有书籍的冷却时间。')
        ad = _('“他曾经有很多名字：始源，深寂，永黑之蓝，涅柔斯，无名之游兽………但现在他只有一个名字，利维坦……”')

        def useItemAction(self, player):
            for i in player.itemcd:
                if i in ALLBOOKS:
                    player.itemcd[i] = 0

            for k in list(player.itemcd.keys()):
                if player.itemcd[k] == 0:
                    del player.itemcd[k]

            player.itemcd[type(self)] = 14

    class BookSport(BookBase):
        id = 409
        name = _('《阿斯卡隆之春》')
        kind = _('书籍')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('阅读本书籍后，进行室外运动时不会获得坏结果，且额外获得2层酸痛，并还有25%的概率获得1层体魄。')
        ad = _('“我正伫立于现实的边缘。你会想念我吗，如果我轻轻一跃？”')

        def useItemAction(self, player):
            BookSportEffect.add(player)
            
    class BookWrite(BookBase):
        id = 410
        name = _('《亚斯塔禄之冬》')
        kind = _('书籍')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('阅读本书籍后，进行读流行小说，读感伤文学或读传统文学日程时会给予你1层独特灵感，每层在获得时提供少量精神状态并降低严重程度，并在下一次委托写作时提高5%这次写作的写作技巧，或是提高5%随笔写作获得的粉丝量。')
        ad = _('“呼吸吧，趁你还能呼吸的时候。”')

        def useItemAction(self, player):
            BookWriteEffect.add(player)


    class BookCM(BookBase):
        id = 411
        name = _('《深沉之雨》')
        kind = _('书籍')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('阅读本书籍后，降低15%过夜消耗的精神状态，并在起床时降低1点严重程度，同时有10%的概率结束该效果。')
        ad = _('“要下雨了，不过是恰到好处的那种雨。”')
        bookEffect_ = BookCMEffect

        def useItemAction(self, player):
            self.bookEffect_.add(player)

    class BookMED(BookBase):
        id = 412
        name = _('《实用百科全书》')
        kind = _('书籍')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('进行日程时提升1点随机属性，同时有10%的概率结束该效果。')
        ad = _('也许你会需要里面的知识，但为什么不问问百度呢……')
        bookEffect_ = BookMEDEffect

        def useItemAction(self, player):
            self.bookEffect_.add(player)

    class AMaverickLion(BookBase):
        id = 413
        name = _('《一只特立独行的狮子》')
        kind = _('书籍')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('阅读本书籍后如果精神状态高于100，则记录当前的精神状态，当效果消失时或因精神状态过低即将崩溃时，使精神状态提升至记录的数值。')
        ad = _('“它们会自由自在地闲逛，饥则进行捕食渴则饮，春天来临时还要谈谈爱情。”')
        bookEffect_ = AMaverickLionEffect

        def useItemAction(self, player):
            self.bookEffect_.add(player)

            

    class BookHeal(BookBase):
        id = 414
        name = _('《神，我们，或所有的士兵》')
        kind = _('书籍')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('阅读该书籍后，一段时间内基础能力大幅下降，但效果结束后一段时间内基础能力大幅提升。')
        ad = _('“明天王子就会来见他，守卫这样说。他知道这其实是什么意思，被圈养的生活将迎来终结，但他好像对此没有什么特别的情绪。”')

        def useItemAction(self, player):
            BookHealEffect_1.add(player)

    
    class BookRisk(BookBase):
        id = 417
        name = _('《世界之终与冷漠之城》')
        kind = _('书籍')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('阅读本书籍后获得存在感。')
        ad = _('“我要坐在有阳光的地方，像猫舔奶碗那样一字不漏地把报纸上下看遍左右看遍，然后把世人在阳光下开展的各种生之片段吸入体内，滋润每一个细胞。”')
        bookEffect_ = Novice

        def useItemAction(self, player):
            if not Novice.has(player):
                Novice.add(player)
                Novice.get(player).duration = 4

    class BookSevUp(BookBase):
        id = 418
        name = _('《热病》')
        kind = _('书籍')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('阅读本书籍后恢复精神状态至200.0，但持续时间内将暂时提升严重程度。')
        ad = _('“我知道，我只是觉得，今晚应该是我的终点了，这是我的预感。”\n我突然很想再吃一次那种名为凯撒面包的食物，我怀念那硬实的口感，它让我想起面前这只狼坚实的拥抱。')
        bookEffect_ = BookSevUpEffect

        def useItemAction(self, player):
            player.mental = 200.0
            self.bookEffect_.add(player)

            
    class BookSevDown(BookBase):
        id = 419
        name = _('《紫罗兰的洗礼》')
        kind = _('书籍')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('阅读本书籍后获得等同于灵感层数的书籍效果，每层使严重倍率降低2%，但每次使用都会降低20%的效果。\n总计使用次数超过5次后，存档则会损坏。')
        ad = _('“起来吧，我的仆从，欢唱着迎接我的到来。')
        bookEffect_ = BookSevDownEffect

        def getPrincipalInfo(self):
            if p:
                s = BookSevDownEffect_.getstack(p)
                if s < 5:
                    info = '\n\n{color=#8433cc}已接受布道：%s次{/color}' % s
                    return self.info + info
                else:
                    return '\n\n{color=#fedb74}接受我吧。{/color}\n\n'
            return self.info

        @classmethod
        def icon(cls):
            if p:
                return 'gui/items/419_%s.png' % BookSevDownEffect_.getstack(p)
            return'gui/items/419.png'


        def useItemAction(self, player):
            if BookSevDownEffect_.getstack(player) == 5:
                import time
                BookSevDownEffect_2.add(player)
                Saver.save(player)
                time.sleep(2)
                renpy.quit()
            else:
                self.bookEffect_.add(player, Inspiration.getstack(player))
    
    class BookUndead(BookBase):
        id = 420
        name = _('《国境以北星空以南》')
        kind = _('书籍')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('阅读本书籍时若精神状态低于10，则暂时降低专注度，使精神状态不会低于10。')
        ad = _('“追求得到之日即其终止之时，寻觅的过程亦即失去的过程。”')
        bookEffect_ = BookUndeadEffect

        def useItemAction(self, player):
            if player.mental < 10:
                self.bookEffect_.add(player)

    class BookRandConc(BookBase):
        id = 421
        name = _('《寻羊历险记》')
        kind = _('书籍')
        maxCd = 7
        maxDu = -1  # 数字
        isUnique = True
        info = _('阅读本书籍后持续时间内判定日程结果时会判定两次，并取其中最高的一次。\n当获得优结果时，降低1点严重度。')
        ad = _('“意志无法分割，或者百分之百继承，或者百分之百消失。”')
        bookEffect_ = BookRandConcEffect

        def useItemAction(self, player):
            self.bookEffect_.add(player)

    class Bookdont(BookBase):
        id = 449
        name = _('《不要读这本书》')
        kind = _('书籍')
        maxCd = 105
        maxDu = -1  # 数字
        isUnique = True
        info = _('不要看这本书的简介不要看这本书的简介不要看这本书的简介不要看这本书的简介不要看这本书的简介不要看这本书的简介')
        ad = _('不要看这本书的内容不要看这本书的内容不要看这本书的内容不要看这本书的内容不要看这本书的内容不要看这本书的内容不要看这本书的内容')

        def useItemAction(self, player):
            renpy.jump('bookdont')
    



    class ProfessionalBookWorking(BookBase):
        id = 497
        name = _('计算机科学专业书籍')
        kind = _('专业类书籍')
        maxCd = 3
        maxDu = -1  # 数字
        reuse = False
        isUnique = False
        canQuit = True
        info = _('阅读本书籍后随机提升工作能力并消耗该书，永久提升2%的工作速度，并获得心流。')
        ad = _('数据结构、设计模式，软件架构，程序测试，操作系统，计算机组成原理……')

        def checkAvailable(self, player):
            if type(self) in player.itemcd:
                return _('书籍仍在冷却时间中！')
            if not BookQuickReadEffect.has(player) and not Relaxation.has(player):
                return _('书籍只能在进行阅读日程或存在特殊状态时才可阅读！')
            
            return True

        def use(self, player):
            if self.checkAvailable(player) != True:
                Notice.add(self.checkAvailable(player))
            else:
                Stat.record(player, type(self))
                Notice.add(_('已速读书籍：')+ self.name)
                player.itemcd[type(self)] = self.maxCd 
                if Relaxation.has(player):
                    Relaxation.subByType(player)
                else:
                    BookQuickReadEffect.subByType(player)
                self.readBook(player, 2)
            Notice.show()

        def useItemAction(self, player):
            g = rca(player, (1,2,2, 3, 3, 4))
            player.gain_abi(0.01 * g, 'wor', stat=self.name)
            FocusAttention.add(player)
            player.workSpeed += 0.02

    class ProfessionalBookWriting(BookBase):
        id = 498
        name = _('文字运用专业书籍')
        kind = _('专业类书籍')
        maxCd = 3
        maxDu = -1  # 数字
        reuse = False
        isUnique = False
        canQuit = True
        info = _('阅读本书籍后随机提升写作技巧并消耗该书，永久提升2%的专注度，并获得4层灵感。')
        ad = _('虽然都是些老掉牙的写法，看这些还不如去读点别人写的小说。')

        def checkAvailable(self, player):
            if type(self) in player.itemcd:
                return _('书籍仍在冷却时间中！')
            if not BookQuickReadEffect.has(player) and not Relaxation.has(player):
                return _('书籍只能在进行阅读日程或存在特殊状态时才可阅读！')
            return True

        def use(self, player):
            if self.checkAvailable(player) != True:
                Notice.add(self.checkAvailable(player))
            else:
                Stat.record(player, type(self))
                Notice.add(_('已速读书籍：')+ self.name)
                player.itemcd[type(self)] = self.maxCd 
                if Relaxation.has(player):
                    Relaxation.subByType(player)
                else:
                    BookQuickReadEffect.subByType(player)
                self.readBook(player, 2)
            Notice.show()

        def useItemAction(self, player):
            g = rca(player, (1,2,2, 3, 3,4))
            player.gain_abi(g * 0.01, 'wri', stat=self.name)
            Inspiration.add(player, 4)
            player.workConcentration += 2

    class ProfessionalBookSeverity(BookBase):
        id = 499
        name = _('心理学专业书籍')
        kind = _('专业类书籍')
        maxCd = 3
        maxDu = -1  # 数字
        reuse = False
        isUnique = False
        canQuit = True
        info = _('阅读本书籍后降低1~5点严重程度并消耗该书，永久降低2%的严重程度倍率，并随机获得数层精神的释放和精神的平复。')
        ad = _('测测你是哪种人格？是NTXL！')

        def checkAvailable(self, player):
            if type(self) in player.itemcd:
                return _('书籍仍在冷却时间中！')
            if not BookQuickReadEffect.has(player) and not Relaxation.has(player):
                return _('书籍只能在进行阅读日程或存在特殊状态时才可阅读！')
            return True

        def use(self, player):
            if self.checkAvailable(player) != True:
                Notice.add(self.checkAvailable(player))
            else:
                Stat.record(player, type(self))
                Notice.add(_('已速读书籍：')+ self.name)
                player.itemcd[type(self)] = self.maxCd 
                if Relaxation.has(player):
                    Relaxation.subByType(player)
                else:
                    BookQuickReadEffect.subByType(player)
                self.readBook(player, 2)
            Notice.show()

        def useItemAction(self, player):
            g = rca(player, (1, 2, 2, 3, 3, 4, 5)) * 0.01
            player.gain_abi(-g, 'sev', stat=self.name)
            MentRezA.add(player, rca(player,(0, 1, 1, 2)))
            MentRezB.add(player, rca(player,(0, 1, 1, 2)))
            
            player.severityRegarded -= 0.02
            Notice.add(_('降低了2%的严重程度倍率！'))
    

    ##################################################################################################################

    
    class AppleJuice(Item):
        id = 200
        name = _('苹果汽水')
        kind = _('食物')
        maxCd = 1
        maxDu = 14
        reuse = False
        isUnique = False
        info = _('使用后重新分配睡意，兴奋，紧张和放松。')
        ad = _('“亚斯塔禄牌苹果汽水，比同类品牌产品多添加20%纯果汁！”')

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


    class CitrusJuice(Item):
        id = 201
        name = _('橘子汽水')
        kind = _('食物')
        maxCd = 1
        maxDu = 14
        reuse = False
        isUnique = False
        info = _('使用后移除1层饱腹。')
        ad = _('“阿斯卡隆牌橘子汽水，喝到就是赚到！”')

        def useItemAction(self, player):
            Satiety.subByType(player)

    class Cola(Item):
        id = 202
        name = _('罐装可乐')
        kind = _('食物')
        maxCd = 1
        maxDu = 14
        reuse = False
        isUnique = False
        info = _('使用后获得心流。')
        ad = _('“The choice of a new generation.”')

        def useItemAction(self, player):
            FocusAttention.add(p)

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
            player.gain_mental(rec, stat=self.name)
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
        info = _('使用后恢复精神状态，有概率提升身体素质，有概率提升食物的恢复效果。\n可以移除营养不良。')
        ad = _('膳食指南推荐一般建议每天摄入300-500g、至少5种以上的蔬菜……')

        def useItemAction(self, player):
            rec = r2(5 * player.useFoodScale())
            player.gain_mental(rec, stat=self.name)
            Malnutrition.clearByType(player)
            Malnutrition_.clearByType(player)
            if rra(player, 70):
                player.gain_abi(0.01, 'phy', stat=self.name)
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
            player.gain_mental(rec, stat=self.name)
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
            player.gain_mental(rec, stat=self.name)
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
        info = _('使用后恢复精神状态，并降低严重程度。\n可以移除营养不良。')
        ad = _('规定斜切必须要有5道裂口才算标准的长条面包！')

        def useItemAction(self, player):
            rec = r2(10 * player.useFoodScale())
            player.gain_mental(rec, stat=self.name)
            player.fooduse += 1
            Notice.add(_('降低了0.5%食物的恢复效果！'))
            Malnutrition.clearByType(player)
            Malnutrition_.clearByType(player)
            player.gain_abi(-0.01, 'sev', stat=self.name)
            if rra(player, 25):
                Satiety.add(player)

    class PastaFood(Item):
        id = 209
        name = _('番茄意面')
        kind = _('食物')
        maxCd = 1
        maxDu = 1
        reuse = False
        isUnique = False
        info = _('使用后恢复精神状态，提升身体素质或移除1层过劳。\n可以移除营养不良。')
        ad = _('非常的新鲜，非常的美味。')

        def useItemAction(self, player):
            rec = r2(20 * player.useFoodScale())
            player.gain_mental(rec, stat=self.name)
            player.fooduse += 1
            Notice.add(_('降低了0.5%食物的恢复效果！'))
            Malnutrition.clearByType(player)
            Malnutrition_.clearByType(player)
            if rra(player, 40):
                Satiety.add(player)
            if rra(player, 70):
                if rra(player, 70):
                    player.gain_abi(0.01, 'phy', stat=self.name)
                else:
                    player.gain_abi(0.02, 'phy', stat=self.name)
                
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
        info = _('使用后恢复精神状态，提升写作技巧或获得1层精神的平复。\n可以移除营养不良。')
        ad = _('“现在，它早已死了，只是眼里还闪着一丝诡异的光。”')

        def useItemAction(self, player):
            rec = r2(20 * player.useFoodScale())
            player.gain_mental(rec, stat=self.name)
            player.fooduse += 1
            Notice.add(_('降低了0.5%食物的恢复效果！'))
            Malnutrition.clearByType(player)
            Malnutrition_.clearByType(player)
            if rra(player, 60):
                Satiety.add(player)
            if rra(player, 70):
                if rra(player, 70):
                    player.gain_abi(0.01, 'wri', stat=self.name)
                else:
                    player.gain_abi(0.02, 'wri', stat=self.name)
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
        info = _('使用后恢复巨量精神状态并获得饱腹。\n可以移除营养不良。')
        ad = _('家庭聚会一定要点这道菜，比惠灵顿还哇塞。\n……一个人吃？咋不撑死你呢？')

        def useItemAction(self, player):
            rec = r2(40 * player.useFoodScale())
            player.gain_mental(rec, stat=self.name)
            player.fooduse += 2
            Notice.add(_('降低了1%食物的恢复效果！'))
            Satiety.add(player, 4)
            Malnutrition.clearByType(player)
            Malnutrition_.clearByType(player)

    class StreetFood1(Item):
        id = 212
        name = _('袋装糖炒板栗')
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
            player.gain_mental(rec, stat=self.name)
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
            Satiety.add(p)
            player.gain_mental(rec, stat=self.name)
            player.fooduse +=1
            Notice.add(_('降低了0.5%食物的恢复效果！'))

    class StreetFood3(Item):
        id = 214
        name = _('烤冷面')
        kind = _('食物')
        maxCd = 1
        maxDu = 1
        reuse = False
        isUnique = False
        info = _('使用后恢复精神状态，降低严重程度。')
        ad = _('不是用火烤的面条哦，是酸甜鲜香的烤冷面！')

        def useItemAction(self, player):
            rec = r2(10 * player.useFoodScale())
            player.gain_mental(rec, stat=self.name)
            player.gain_abi(-0.02, 'sev', stat=self.name)

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
            player.gain_abi(0.01, 'sev', stat=self.name)
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
        info = _('使用后获得1层优质咖啡，2层兴奋。')
        ad = _('A市的人喝咖啡，像进行一场不需要规则的游戏，随性放任，百无禁忌。')

        def useItemAction(self, player):
            player.fooduse -= 2
            if player.experience == 'wri':
                CoffeeHQ2.add(player)
            else:
                CoffeeHQ.add(player)
            ConcInc.add(player, 2)
            player.fooduse += 1
            Notice.add(_('降低了0.5%食物的恢复效果！'))

    class StreetFood6(Item):
        id = 217
        name = _('生椰拿铁')
        kind = _('食物')
        maxCd = 1
        maxDu = 3
        reuse = False
        isUnique = False
        info = _('使用后获得1层优质咖啡，降低2点严重程度。')
        ad = _('“我不在咖啡馆，就在去咖啡馆的路上。”')

        def useItemAction(self, player):
            if player.experience == 'wri':
                CoffeeHQ2.add(player)
            else:
                CoffeeHQ.add(player)
            player.gain_abi(-0.02, 'sev', stat=self.name)
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
        info = _('使用后获得1层优质咖啡，3层放松。')
        ad = _('让爱恋中的人们了解爱情的甜美和波折，为了告诉我们幸福的简单。')

        def useItemAction(self, player):
            ConsDec.add(player, 3)
            if player.experience == 'wri':
                CoffeeHQ2.add(player)
            else:
                CoffeeHQ.add(player)
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
            temp = ra(player, 1,3)
            if player.experience == 'wri':
                temp = ra(player, 2,3)
            if temp == 1:
                player.gain_abi(0.02, 'wor', stat=self.name)
            elif temp == 2:
                player.gain_abi(0.02, 'phy', stat=self.name)
            else:
                player.gain_abi(0.02, 'wri', stat=self.name)

    
    class StreetFood10(Item):
        id = 221
        name = _('泡面')
        kind = _('食物')
        maxCd = 0
        maxDu = 90
        reuse = False
        isUnique = False
        info = _('精神状态大于0时，精神状态越少，恢复的精神状态越多。\n必定获得饱腹并降低少量食物的恢复效果，小概率获得营养不良。')
        ad = _('某种意义上的硬通货。')

        def useItemAction(self, player):
            if 0 < player.mental < 50:
                r = -0.6 * player.mental + 50
                rec = r2(r * player.useFoodScale())
            else:
                rec = r2(20 * player.useFoodScale())
            player.gain_mental(rec, stat=self.name)
            Satiety.add(player)
            player.fooduse += 2
            if rra(player, 20):
                Malnutrition.add(player)
            Notice.add(_('降低了1%食物的恢复效果！'))

    class StreetFood11(Item):
        id = 222
        name = _('柠檬水')
        kind = _('食物')
        maxCd = 1
        maxDu = 1
        reuse = False
        isUnique = False
        info = _('使用后恢复精神状态。')
        ad = _('普通的柠檬水，便宜又好喝。')
        p=0.05

        def useItemAction(self, player):
            rec = r2(15 * player.useFoodScale())
            player.gain_mental(rec, stat=self.name)

    class StreetFood12(Item):
        id = 223
        name = _('椰椰茶冻')
        kind = _('食物')
        maxCd = 1
        maxDu = 1
        reuse = False
        isUnique = False
        info = _('使用后恢复精神状态，降低严重程度。')
        ad = _('椰子香味和淡淡的乌龙茶香简直是绝配。')
        p=0.1

        def useItemAction(self, player):
            rec = r2(15 * player.useFoodScale())
            player.gain_abi(-0.02, 'sev', stat=self.name)
            player.gain_mental(rec, stat=self.name)

    class StreetFood13(Item):
        id = 224
        name = _('抹茶幸运冰')
        kind = _('食物')
        maxCd = 1
        maxDu = 1
        reuse = False
        isUnique = False
        info = _('使用后恢复精神状态，获得1点工作能力，身体素质和写作技巧。')
        ad = _('虽然我对抹茶不感兴趣，但它真的很好吃。')
        p=0.15

        def useItemAction(self, player):
            rec = r2(15 * player.useFoodScale())
            player.gain_mental(rec, stat=self.name)
            player.gain_abi(0.01, 'wor', stat=self.name)
            player.gain_abi(0.01, 'phy', stat=self.name)
            player.gain_abi(0.01, 'wri', stat=self.name)

    class Alcohol(Item):
        id = 225
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
                player.gain_mental(-100 * f(), stat=self.name)
            else:
                player.mental = r2(0.5 * player.mental)
            player.severity += 0.02
            ConcDec.add(player, 2)
            ConsDec.add(player, 2)
            Inspiration.add(player, 3)
            if not player.s4 and player.week >= 2 and MentProb.has(player) and player.today in (6, 7) and player.hal_p != 11:
                renpy.jump("solitus_route_4")

    class Cigarette(Item):
        id = 226
        name = _('盒装香烟')
        kind = _('消耗品')
        maxCd = 0
        maxDu = 28
        reuse = True
        isUnique = True
        info = _('使用后消耗烟盒内1根香烟，提升严重程度，获得2~4层清醒，暂时移除难耐的效果。\n已存在清醒状态时使用不会获得更多效果，同时还会提升严重程度。')
        ad = _('抽烟的人通常短命，它和我算是绝配。')

        def __init__(self, player):
            super(type(self), self).__init__(player)
            self.cap = 12

        def getPrefixInfo(self, player):

            cd_info = _('可重复使用  ')

            if self.broken:
                du_info = _('已变质  ')
            elif self.du == 1:
                du_info = _('即将变质：明天  ')
            else:
                du_info = _('即将变质：')+str(self.du)+_('天后  ')

            du_info += _('\n\n{color=#fde827}存放香烟：')+str(self.cap)+_('根  {/color}')

            return _('数量：')+str(self.amounts)+ '\n' + cd_info + '\n'+du_info+ '\n'

        def useItemAction(self, player):
            player.severity += 0.01
            if Entrance.has(player):
                player.severity += 0.05
            else:
                Entrance.add(player, ra(player, 2, 4))
            self.cap -= 1
            if self.cap == 0:
                self.sub(player)
                Notice.add(_('已消耗完所有的香烟！'))



    class CreamCake(Item):
        id = 227
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
            player.gain_mental(rec, stat=self.name)
            for i in (MentProb, PhysProb):
                if i.has(player):
                    i.subByType(player)
                    break
            Satiety.add(p)
            player.fooduse += 1
            Notice.add(_('降低了0.5%食物的恢复效果！'))


    class StrawberryCake(Item):
        id = 228
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
            player.gain_mental(rec, stat=self.name)
            player.gain_abi(-0.01, 'sev', stat=self.name)
            Satiety.add(p)
            player.fooduse += 1
            Notice.add(_('降低了0.5%食物的恢复效果！'))


    class OrangeCake(Item):
        id = 229
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
            player.gain_mental(rec, stat=self.name)
            l = list(filter(lambda x: not x.has(player), (Restlessness, Contentment, Desire, Sadness, Agony, Dread)))
            if l:
                rca(player, l).add(player)
            Satiety.add(p)
            player.fooduse += 1
            Notice.add(_('降低了0.5%食物的恢复效果！'))
    

    
    
    class Strawberry(Item):
        id = 232
        name = _('一盒草莓')
        kind = _('食物')
        maxCd = 0
        maxDu = 2
        reuse = False
        isUnique = False
        info = _('使用后恢复精神状态，不受食物恢复效果的影响，提升食物的恢复效果，移除1层焦虑和过劳。')
        ad = _('天赐的奖励。')
 
        def useItemAction(self, player):
            rec = r2(20 * f())
            player.gain_mental(rec, stat=self.name)
            for i in (MentProb, PhysProb):
                if i.has(player):
                    i.subByType(player)
            player.fooduse -= 2
            Notice.add(_('提升了1%食物的恢复效果！'))
            
            
    class ChewingGum(Item):
        id = 233
        name = _('瓶装什锦口香糖')
        kind = _('消耗品')
        maxCd = 1
        maxDu = 28
        reuse = True
        isUnique = True
        info = _('使用后食用1粒口香糖，随机获得一种持续1天的状态。')
        ad = _('为什么不给我一个单一口味的口香糖呢？什么叫懒得写那么多道具啊！')

        def __init__(self, player):
            super(type(self), self).__init__(player)
            self.cap = 7

        def getPrefixInfo(self, player):

            cd_info = _('可重复使用  ')

            if self.broken:
                du_info = _('已变质  ')
            elif self.du == 1:
                du_info = _('即将变质：明天  ')
            else:
                du_info = _('即将变质：')+str(self.du)+_('天后  ')

            du_info += _('\n\n{color=#fde827}存放口香糖：')+str(self.cap)+_('粒  {/color}')

            return _('数量：')+str(self.amounts)+ '\n' + cd_info + '\n'+du_info+ '\n'

        def useItemAction(self, player):
            
            
            ChewingGumEffect.add(player)
            self.cap -= 1
            if self.cap == 0:
                self.sub(player)
                Notice.add(_('已消耗完所有的口香糖！'))

    class DeplineItem1(Item):
        id = 234
        name = _('“11号街”挂耳咖啡包')
        kind = _('食物')
        maxCd = 1
        maxDu = -1
        reuse = False
        isUnique = False
        info = _('使用后获得1层优质咖啡以及最大层数的兴奋。')
        ad = _('“苦味之外还有些许淡淡的柑橘香味。”')

        def useItemAction(self, player):
            if player.experience == 'wri':
                CoffeeHQ2.add(player)
            else:
                CoffeeHQ.add(player)
            ConcInc.add(player, 10)

    class RawFish(Item):
        id = 235
        name = _('生鱼')
        kind = _('食物')
        maxCd = 1
        maxDu = 1
        reuse = False
        isUnique = False
        info = _('使用后降低大量精神状态，放入小型冰箱一天后会变成冻鱼，可以卖给Creefo，也可以烤制成熟鱼。')
        ad = _('虽然我是一只拟人化的动物，但也不代表我想过祖先的生活。')

        def __eq__(self, other):
            return False

        def __init__(self, player):
            super(type(self), self).__init__(player)
            self.qty = 0.1

        def getPrincipalInfo(self):
            info = '\n\n鱼肉品质：%s' % self.qty
            return self.info + info

        def useItemAction(self, player):
            rec = r2(200 * f())
            player.gain_mental(-rec, stat=self.name)
            Notice.add(_('为什么要吃生的啊！'))
            Achievement312.achieve()
            Achievement.show()

        def timeUpAction(self, player):
            RottedFish.add(player)

        def frozen(self, player):
            ff = RawFishFrozen(player)
            punish = ra(player, 8000, 9500) * 0.01
            oldqty = self.qty
            ff.qty = r2(self.qty * 0.01 * punish)
            Notice.add('存储于小型冰箱的生鱼变成了冻生鱼！品质降低了%s点！'%(oldqty-ff.qty))
            return ff

        def cook(self, player):
            ff = CookedFish(player)
            ff.qty = self.qty
            showNotice(['品质为%s的生鱼变成了熟鱼！'%(self.qty)])
            self.sub(player)
            player.items.append(ff)


    
    class CookedFish(Item):
        id = 236
        name = _('熟鱼')
        kind = _('食物')
        maxCd = 1
        maxDu = 2
        reuse = False
        isUnique = False
        info = _('使用后恢复精神状态，降低严重程度，提升工作能力，身体素质和写作技巧之中最低的一项能力，质量越好提升得越多。\n钓鱼时，可以在消耗完所有精力后额外恢复精力，质量越好提升得越多。\n存在饱腹效果时使用无效。\n可以移除营养不良。')
        ad = _('当你闻到它的气味时，便会想起和他湖边钓鱼的经历。')

        def __eq__(self, other):
            return False

        def __init__(self, player):
            super(type(self), self).__init__(player)
            self.qty = 0.1

        def getPrincipalInfo(self):
            info = '\n\n鱼肉品质：%s' % self.qty
            return self.info + info

        def useItemAction(self, player):
            rec = r2(20 * player.useFoodScale() * self.qty)
            player.gain_mental(rec, stat=self.name)
            if Satiety.has(player):
                return
            t = r2(max(self.qty - 1.5, 0) * 0.01)
            player.gain_abi(-t, 'sev', stat=self.name)
            fe = int(0.5 * self.qty)
            player.fishenergy += fe
            Notice.add(_('恢复了%s点钓鱼精力！' % fe))
            Malnutrition.clearByType(player)
            Malnutrition_.clearByType(player)
            abilitylist = [
                ['wor', player.working],
                ['phy', player.physical],
                ['wri', player.writing],
            ]
            if player.experience == 'wri':
                abilitylist.pop(-1)
            abilitylist.sort(key=lambda x: x[1])
            t = int(2 * self.qty)
            player.gain_abi(0.01 * t, abilitylist[0][0], stat=self.name)
            if rra(player, 50):
                Satiety.add(player)

        def timeUpAction(self, player):
            RottedFish.add(player)

        def frozen(self, player):
            ff = CookedFishFrozen(player)
            punish = ra(player, 3000, 6000) * 0.01
            oldqty = self.qty
            ff.qty = r2(self.qty * 0.01 * punish)
            Notice.add('存储于小型冰箱的熟鱼变成了冻熟鱼！品质降低了%s点！'%(oldqty-ff.qty))
            return ff

    class RawFishFrozen(Item):
        id = 237
        name = _('冻生鱼')
        kind = _('食物')
        maxCd = 0
        maxDu = 7
        reuse = False
        isUnique = False
        info = _('冷冻后鱼肉品质较低的生鱼，但是保存时间更久了，可以卖给Creefo，也可以烤制成熟鱼。')
        ad = _('它的眼里已经不再有诡异的光了。')

        def __eq__(self, other):
            return False

        def __init__(self, player):
            super(type(self), self).__init__(player)
            self.qty = 0.1

        def getPrincipalInfo(self):
            info = '\n\n鱼肉品质：%s' % self.qty
            return self.info + info

        def useItemAction(self, player):
            rec = r2(400 * f())
            player.gain_mental(-rec, stat=self.name)
            Notice.add(_('为什么要吃又冰又生的鱼啊！'))
            Achievement312.achieve()
            Achievement.show()

        def timeUpAction(self, player):
            RottedFish.add(player)

        def cook(self, player):
            ff = CookedFish(player)
            ff.qty = self.qty
            showNotice(['品质为%s的冻生鱼变成了熟鱼！'%(self.qty)])
            self.sub(player)
            player.items.append(ff)

    class CookedFishFrozen(Item):
        id = 238
        name = _('冻熟鱼')
        kind = _('食物')
        maxCd = 0
        maxDu = 7
        reuse = False
        isUnique = False
        info = _('使用后恢复精神状态，降低严重程度，提升工作能力，身体素质和写作技巧之中最低的一项能力，质量越好提升得越多。\n存在饱腹效果时使用无效。\n可以移除营养不良。')
        ad = _('不那么好吃，但还能接受。')

        def __eq__(self, other):
            return False

        def __init__(self, player):
            super(type(self), self).__init__(player)
            self.qty = 0.1

        def getPrincipalInfo(self):
            info = '\n\n鱼肉品质：%s' % self.qty
            return self.info + info

        def useItemAction(self, player):
            rec = r2(5 * player.useFoodScale() * self.qty)
            player.gain_mental(rec, stat=self.name)
            if Satiety.has(player):
                return
            t = r2(max(self.qty - 1.5, 0) * 0.01)
            player.gain_abi(-t, 'sev', stat=self.name)
            Malnutrition.clearByType(player)
            Malnutrition_.clearByType(player)
            abilitylist = [
                ['wor', player.working],
                ['phy', player.physical],
                ['wri', player.writing],
            ]
            if player.experience == 'wri':
                abilitylist.pop(-1)
            abilitylist.sort(key=lambda x: x[1])
            t = int(2 * self.qty)
            player.gain_abi(0.01 * t, abilitylist[0][0], stat=self.name)
            if rra(player, 50):
                Satiety.add(player)
        
        def timeUpAction(self, player):
            RottedFish.add(player)
    
    class RottedFish(Item):
        id = 239
        name = _('腐烂的鱼肉')
        kind = _('食物')
        maxCd = -1
        maxDu = -1
        isUnique = False
        info = _('严重程度提升20%。')
        ad = _('你为什么要留着这东西，只能说明你是一个变态。')

        def addStackAction(self, player):  # 每次添加层数的操作，一般是某些根据层数给予效果的Effect需要设置
            player.severityRegarded += 0.2

        def subStackAction(self, player):  # 减少层数的操作，前者的反向函数
            player.severityRegarded -= 0.2

    class GoldFish(Item):
        id = 240
        name = _('黄金鱼')
        kind = _('收藏品')
        maxCd = 0
        maxDu = -1
        reuse = False
        isUnique = False
        info = _('持有时，降低30%的严重程度。')
        ad = _('开局就送1000抽，如果你抽到了这只鱼，那就说明你是真正的欧皇！')

        def __eq__(self, other):
            return False

        def getPrincipalInfo(self):
            info = '\n\n鱼肉品质：{color=#FFD700}999999{/color}'
            return self.info + info

        def useItemAction(self, player):
            player.gain_mental(1, stat=self.name)


    class SolitusCookie(Item):
        id = 295
        name = _('袋装葡萄味饼干')
        kind = _('食物')
        maxCd = 1
        maxDu = 180
        reuse = False
        isUnique = False
        info = _('使用后恢复1点精神状态。')
        ad = _('尝起来像你自己。')

        def useItemAction(self, player):
            player.gain_mental(1, stat=self.name)
            player.fooduse += 1
            Notice.add(_('降低了0.5%食物的恢复效果！'))

        

    class HallukeCookie(Item):
        id = 296
        name = _('袋装奶油味饼干')
        kind = _('食物')
        maxCd = 1
        maxDu = 180
        reuse = False
        isUnique = False
        info = _('使用后获得放松。')
        ad = _('尝起来像一维生物。')

        def useItemAction(self, player):
            ConsDec.add(player)
            player.fooduse += 1
            Notice.add(_('降低了0.5%食物的恢复效果！'))
    
    class AcolasCookie(Item):
        id = 297
        name = _('袋装西瓜味饼干')
        kind = _('食物')
        maxCd = 1
        maxDu = 180
        reuse = False
        isUnique = False
        info = _('使用后获得兴奋。')
        ad = _('尝起来像99层过劳。')

        def useItemAction(self, player):
            ConcInc.add(player)
            player.fooduse += 1
            Notice.add(_('降低了0.5%食物的恢复效果！'))
    
    class PathosCookie(Item):
        id = 298
        name = _('袋装蓝莓味饼干')
        kind = _('食物')
        maxCd = 1
        maxDu = 180
        reuse = False
        isUnique = False
        info = _('使用后获得紧张。')
        ad = _('尝起来像鱼鳃。')

        def useItemAction(self, player):
            ConsInc.add(player)
            player.fooduse += 1
            Notice.add(_('降低了0.5%食物的恢复效果！'))
    
    class DecayCookie(Item):
        id = 299
        name = _('袋装薄荷味饼干')
        kind = _('食物')
        maxCd = 1
        maxDu = 180
        reuse = False
        isUnique = False
        info = _('使用后获得睡意。')
        ad = _('尝起来像脑浆。')
 
        def useItemAction(self, player):
            ConcDec.add(player)
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
    
    class DeplineItem2(Item):
        id = 501
        name = _('小榴莲毛绒玩偶')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1  # 数字
        isUnique = True
        canQuit = False
        info = _('食物的恢复效果提升15%。')
        ad = _('希望我下一次买的榴莲里的果肉也能这么饱满……')

        def enableAction(self, player):
            player.foodRecovery += 0.15

        def disableAction(self, player):
            player.foodRecovery -= 0.15
    

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
    
    class AcolasItem5(Item):
        id = 514
        name = _('已完成的项目（阶段1）')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1  # 数字
        isUnique = True
        info = _('已完成程序的工程文件。')
        ad = '值得吗？'

        def enableAction(self, player):
            Achievement450.achieve()
            Achievement.show()
    

    class AcolasItem6(Item):
        id = 515
        name = _('已完成的项目（阶段2）')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1  # 数字
        isUnique = True
        info = _('已完成文案的工程文件。')
        ad = '也许……值得？'


    class AcolasItem7(Item):
        id = 516
        name = _('已完成的项目（阶段3）')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1  # 数字
        isUnique = True
        info = _('已完成润色的工程文件。')
        ad = '当你能看到这个道具的说明时，就代表你作弊了。'

        def enableAction(self, player):
            if AcolasItem5.has(player):
                Achievement451.achieve()
                Achievement.show()

    class AcolasItem2(Item):
        id = 511
        name = _('未完成的项目（阶段1）')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1  # 数字
        isUnique = True
        canQuit = False
        upper = AcolasItem5
        info = _('需要完善基础结构和程序源码的设计稿。')
        ad = '两周时间……就算没完成的话，他也会原谅我的吧？'

        def __init__(self, player):
            super(AcolasItem2, self).__init__(player)
            self.progress = 0

        def work(self, player):
            cons = r2(100 * AcolasTask1.getConsScale(player))
            a = 10 * player.workSpeed * f()
            if self.progress <= 33:
                a *= ra(player, 80, 100) * 0.01
            elif self.progress <= 66:
                a *= ra(player, 60, 80) * 0.01
            else:
                a *= ra(player, 120, 150) * 0.01
            self.progress += r2(a)
            Notice.add(_('完成了%s%s的进度。') % (r2(a), '%'))
            if 100 > self.progress:
                Notice.add(_('还差%s%s。') % (r2(100-self.progress), '%'))
            player.gain_mental(-cons, stat=self.name)
            player.gain_abi(0.05, 'sev', stat=self.name)
            PhysProb.add(player, 3)
            player.updateAfterTask(AcolasTask1)
            if self.progress >= 100:
                self.upper.add(player)
                self.remove(player)
                renpy.jump("AcolasTask1_end")
            else:
                renpy.jump("AcolasTask1_result")
                
        
        @classmethod
        def getPrincipalInfo(cls):
            pro_info = ''
            type_info = _('\n\n') + cls.kind
            if cls.has(p):
                pro_info = _('\n\n已完成进度：%s%s\n') % (cls.get(p).progress, '%')

            if cls.isUnique:
                uni_info = _('\n唯一')
            else:
                uni_info = ''

            return cls.info + type_info + pro_info + uni_info
    

    class AcolasItem3(Item):
        id = 512
        name = _('未完成的项目（阶段2）')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1  # 数字
        isUnique = True
        canQuit = False
        upper = AcolasItem6
        info = _('需要加入游戏剧情和文案的设计稿。')
        ad = '……我不能辜负他对我的期待。'

        def __init__(self, player):
            super(AcolasItem3, self).__init__(player)
            self.progress = 0
        
        def work(self, player):
            cons = r2(100 * AcolasTask1.getConsScale(player))
            a = 10 * player.workSpeed * f()
            if self.progress <= 33:
                a *= ra(player, 80, 120) * 0.01
            elif self.progress <= 66:
                a *= ra(player, 50, 80) * 0.01
            else:
                a *= ra(player, 30, 50) * 0.01
            self.progress += r2(a)
            Notice.add(_('完成了%s%s的进度。') % (r2(a), '%'))
            if 100 > self.progress:
                Notice.add(_('还差%s%s。') % (r2(100-self.progress), '%'))
            player.gain_mental(-cons, stat=self.name)
            player.gain_abi(0.05, 'sev', stat=self.name)
            PhysProb.add(player, 3)
            player.updateAfterTask(AcolasTask1)
            if self.progress >= 100:
                self.upper.add(player)
                self.remove(player)
                renpy.jump("AcolasTask1_end")
            elif player.times == 12 and (player.today == 4 or player.today == 5 and int(player.st()[0]) < 6) and player.aco_p == 8:
                renpy.jump("AcolasTask1_loop")
            else:
                renpy.jump("AcolasTask1_result")

        @classmethod
        def getPrincipalInfo(cls):
            pro_info = ''
            type_info = _('\n\n') + cls.kind
            if cls.has(p):
                pro_info = _('\n\n已完成进度：%s%s\n') % (cls.get(p).progress, '%')

            if cls.isUnique:
                uni_info = _('\n唯一')
            else:
                uni_info = ''

            return cls.info + type_info + pro_info + uni_info

    
    class AcolasItem4(Item):
        id = 513
        name = _('未完成的项目（阶段3）')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1  # 数字
        isUnique = True
        canQuit = False
        upper = AcolasItem7
        info = _('需要为整体润色的设计稿。')
        ad = '……'

        def __init__(self, player):
            super(AcolasItem4, self).__init__(player)
            self.progress = 0
        
        def work(self, player):
            cons = r2(100 * AcolasTask1.getConsScale(player))
            cons += abs(player.mental * 0.5)
            if self.progress < 1:
                a = self.progress * (1 + self.progress)
            elif self.progress < 10:
                a = self.progress * (1 + self.progress * 0.01)
            else:
                a = self.progress * (self.progress * 0.01) + 5
            if a == 0:
                a = 0.01
            self.progress += r2(a)
            Notice.add(_('完成了%s%s的进度。') % (r2(a), '%'))
            if 100 > self.progress:
                Notice.add(_('还差%s%s。') % (r2(100-self.progress), '%'))
            player.gain_mental(-cons, stat=self.name)
            player.gain_abi(0.05, 'sev', stat=self.name)
            PhysProb.add(player, 3)
            player.updateAfterTask(AcolasTask1)
            if self.progress >= 100:
                self.upper.add(player)
                self.remove(player)
                renpy.jump("Acolas_hidden_plot2")
            elif player.times == 12:
                aa = 0.01 * int(a)
                if aa > 0:
                    player.gain_abi(aa, 'sev', stat=self.name)
                p.color = (100 - self.progress)* 0.01
                if p.color < 0:
                    p.color = 0.0
                renpy.jump("AcolasTask2_loop")
            else:
                renpy.jump("AcolasTask1_result")
                
        @classmethod
        def getPrincipalInfo(cls):
            pro_info = ''
            type_info = _('\n\n') + cls.kind
            if cls.has(p):
                pro_info = _('\n\n已完成进度：%s%s\n') % (cls.get(p).progress, '%')

            if cls.isUnique:
                uni_info = _('\n唯一')
            else:
                uni_info = ''

            return cls.info + type_info + pro_info + uni_info


    class WriterItem1(Item):
        id = 517
        name = _('未完成的小说原稿')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1  # 数字
        isUnique = True
        canQuit = False
        info = _('当拥有回忆片段时通过撰写小说日程来提升小说进度，只能记录一个人的故事。')
        ad = '什么样的欲望在驱使着我们？'

        def __init__(self, player):
            super(WriterItem1, self).__init__(player)
            self.progress = 0
            self.route = None

        def work(self, player):
            if not self.route:
                if WriterItem3.has(player):
                    self.route = 'Halluke'
                elif WriterItem4.has(player):
                    self.route = 'Depline'
            if self.route == 'Halluke':
                wi = WriterItem3.get(player)
            elif self.route == 'Depline':
                wi = WriterItem4.get(player)

            player.retval = rcd(wi.texts)
            wi.sub(player)

            cons = r2(40 * SpecialWriting.getConsScale(player))
            if WriterBuff2.has(player):
                cons *= -1
                WriterBuff2.clearByType(player)
            a = r2(2 * f())
            self.progress += a
            Notice.add(_('完成了%s%s的进度。') % (a, '%'))
            
            player.gain_mental(-cons, stat=self.name)
            if 100 > self.progress:
                Notice.add(_('还差%s%s。') % (r2(100-self.progress), '%'))
            else:
                WriterItem2.add(player)
                self.remove(player)
                
        
        @classmethod
        def getPrincipalInfo(cls):
            pro_info = ''
            type_info = _('\n\n') + cls.kind
            if cls.has(p) and cls.get(p).route:
                pro_info = _('\n\n已完成进度：%s%s\n') % (cls.get(p).progress, '%')
                pro_info += '\n描绘了与' + cls.get(p).route + '的故事。'

            uni_info = _('\n唯一')

            return cls.info + type_info + pro_info + uni_info
    

    class WriterItem2(Item):
        id = 518
        name = _('已完成的小说原稿')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1  # 数字
        isUnique = True
        info = '结束了，但还是缺点什么……'
        ad = '我将在第二日重见光明……'   
    
    class WriterItem3(Item):
        id = 519
        name = _('与Halluke的回忆片段')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1  # 数字
        info = '用于撰写小说日程。'
        ad = '什么……是爱？'

        def __eq__(self, other):
            if type(self) != type(other):
                return False
            if self.du != other.du:
                return False
            if self.gotWeek != other.gotWeek:
                return False
            if self.gotDay != other.gotDay:
                return False
            return True

        def __init__(self, player):
            super(WriterItem3, self).__init__(player)
            self.texts = None
            self.getText(player.hal_p)

        def getText(self, week):
            weekinfo = [
                ["……"],
                ["“Neon在训练场里遇见了Druke，他的目光无法从他的身上移开……”", "“Neon出神地注视着Druke，以至于忘记了问他的名字……”","“Neon心想，下一次见到他一定要问他的名字。”"],
                ["“Neon想做些什么，但他只是在一旁看着。”","“Neon听到了别人称他为Druke，他将铭记这个名字。”","“Druke打败了一个对手，崇拜的情绪在Neon心中浮现。”"],
                ["“Neon窥视着Druke，目光像是想穿过Druke身上仅有的一层布料。”","“Neon躺在床上，脑中都是那只白虎兽人的模样……”","“Neon回忆着Druke拿着巨锤横扫的模样，不知为何，他的身体逐渐有了一丝反应……”"],
                ["“Neon在训练场上紧握着手中的剑，他的对手是一个魔法师……”","“Neon躲开了对手射过来的箭矢，冲刺过去用剑砍掉了对方的弓。”","“Neon训练得十分卖力，而Druke则偶尔会在远处看向他，这应该是Druke第一次注意到他……”","“Druke看向训练场中的Neon，虽然那只白狼看上去软弱，但实际上还挺能厉害的。”"],
                ["“Neon用剑径直刺向Druke，却被他用锤柄轻易地挡开，Neon则被金属反震震得手臂发麻……”","“横扫过来的巨锤在快要击打到Neon腰部时突然停下，很明显Neon输了，但他十分开心。”","“训练时间结束，Druke并没有和Neon说太多道别的话，毕竟他们还不熟。”","“Neon有些伤心，他不知道下一次还能否和Druke一起训练，又害怕对方如果知道自己喜欢他，会是什么想法。”"],
                ["“‘我的名字是Neon’，虽然只是简单的介绍，但Neon已经鼓足了勇气才开的口。”","“Druke惊异于Neon的拘谨，在互相介绍之后便成为了朋友。”","“虽然他们已经见面很多次了，但这还是他们第一次互相认识对方……”","“他们再一次在训练场中看见对方，就像看到认识的人一样，即便他们连对方的名字都不知道。”"],
                ["“Neon想多和Druke一起训练，于是他们约定每周训练两天，而不是一天。”","“Neon和Druke交换了各自的住址，也许当他们不再来到这个训练场时，他们还可以互相写信……”","“Neon越来越喜欢Druke了，但他不知道该如何向一位同性表达那种感情……”"],
                ["“Neon有些筋疲力尽了，他倒在地上，大口喝着水，而Druke看上去意犹未尽……”","“Druke扶起了倒在地上的Neon，但他却像丢了骨头一样又瘫在地上……”","“‘好累，让我再多休息一会吧……’Neon靠在Druke的胸前，鼻子偷偷嗅闻着他身上淡淡的汗味……”","“‘你再不休息好，我可就要找别人了。’Druke半开玩笑地说，随后Neon便再一次站起身来……”","“在如此高强度的训练下，Druke仍然保持着速度和力量，Neon心想，如果他也有那么强壮，就不会这么累了。”"],
                ["“训练强度愈发提升，Neon显然有些支撑不住了，而Druke早已看出来，于是他便让Neon休息一会……”","“Druke在训练时，护手突然掉在地上，Neon将它捡了起来……”","“Neon看着手中Druke的护手，突然有了一种奇怪的欲望……”","“Neon说他认识一个很厉害的皮匠，能够修好Druke的护手。”"],
                ["“Druke约Neon吃点东西，他们来到了训练场边上的餐馆，点了一些红肉和面包……”","“Neon有些心不在焉，也许只是训练的强度太高了，他想知道自己是否真的喜欢眼前的人。”","“Neon和Druke走到了一家武器店前，他觉得自己的武器应该稍微保养下了，而Druke却觉得没必要。”","“Neon将一把崭新的巨锤送给了Druke，他立刻就抱住了Neon……”"],
                ["……"],
                ["“在一次冒险中，Neon没有辅助好Druke，让他们俩都受了伤……”","“Druke离开了Neon，他想去寻找一个不像Neon那样弱小的队友。”","“Neon接受了这样的现实，他知道自己没必要再找他了，自己明明陪他那么久，只是因为这点事……”","“也许Druke会后悔吧，Neon那样想着，他也走进了酒馆，想认识一位新的同伴。”"],
                ["“Neon听说Druke死了，死于鲁莽和不听新队友的指挥，身受重伤，就算最强大的牧师也没法救活他。”", "“他会记得Druke的，也许曾经的相遇并不美好，但那段记忆存在过。”", "“或许他会想念他，但是生活还要继续，Neon该去往下一个地方了。”"],
            ]
            if -1 < week < 14:
                self.texts = weekinfo[week]
            else:
                self.texts = ["……"]

        @classmethod
        def add(cls, player, times=1):  # 增加新效果或增加层数
            if times == 0:
                return
            if WriterItem2.has(player):
                return
            GuideI.unlock(cls)
            for i in range(times):
                cls.defaultAddItem(player)
            WriterBuff2.add(player)
    
    class WriterItem4(Item):
        id = 520
        name = _('与Depline的回忆片段')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1  # 数字
        info = '用于撰写小说日程。'
        ad = '我是否是一朵独特的玫瑰？'

        def __eq__(self, other):
            if type(self) != type(other):
                return False
            if self.du != other.du:
                return False
            if self.gotWeek != other.gotWeek:
                return False
            if self.gotDay != other.gotDay:
                return False
            return True

        @classmethod
        def add(cls, player, times=1):  # 增加新效果或增加层数
            if times == 0:
                return
            if WriterItem2.has(player):
                return
            GuideI.unlock(cls)
            for i in range(times):
                cls.defaultAddItem(player)
            WriterBuff2.add(player)

    class WriterItem5(Item):
        id = 521
        name = _('{color=#9500ff}完美的小说{/color}')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1  # 数字
        isUnique = True
        info = '……'
        ad = '……' 

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
        info = _('全部属性提升10%。')  # 普通结局获得 持有本收藏品可进入真结局
        ad = _('紫色的贴纸中央打印着白色的数字59，你似乎十分熟悉这个数字，但又完全回忆不起来。\n\n{u}持有本道具再次进入普通结局时，可以进入全新的结局。{/u}')

        def enableAction(self, player):
            player.workingRegarded += 0.1
            player.writingRegarded += 0.1
            player.physicalRegarded += 0.1

        def disableAction(self, player):
            player.workingRegarded -= 0.1
            player.writingRegarded -= 0.1
            player.physicalRegarded -= 0.1

    class OldPic(Item):
        id = 601
        name = _('{color=#9500ff}合照{/color}')
        kind = _('收藏品')
        maxCd = 3
        maxDu = -1  # 数字
        isUnique = True
        canQuit = False
        info = _('严重度-20%。\n使用后移除1层焦虑。')
        ad = _('你应当留着这张照片。')

        def enableAction(self, player):
            player.severityRegarded -= 0.2

        def disableAction(self, player):
            player.severityRegarded += 0.2

        def useItemAction(self, player):
            if MentProb.has(player):
                MentProb.subByType(player)


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


    class TransparentBottle(Item):
        id = 604
        name = _('{color=#9500ff}透明药瓶{/color}')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1
        isUnique = True
        canQuit = False
        info = _('提升20%药物的治疗效果。')
        ad = _('骗子不仅需要具备欺骗他人的能力，更要懂得欺骗自己的内心。')

        def enableAction(self, player):
            player.drugRecovery += 0.2

        def disableAction(self, player):
            player.drugRecovery -= 0.2

    class TrainTicket(Item):
        id = 605
        name = _('{color=#9500ff}失效的火车票{/color}')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1
        isUnique = True
        canQuit = False
        info = _('粉丝上限提升40000。')
        ad = _('其上的字迹已经模糊不清了。')

        def afterSleepAction(self, player):
            if persistent.writerendname:
                TrainTicket.ad = '其上的字迹已经模糊不清了，隐隐约约能看见持票人的名字是%s。' % persistent.writerendname
            else:
                TrainTicket.ad = '其上的字迹已经模糊不清了。'

        def enableAction(self, player):
            player.maxpopularity += 40000

        def disableAction(self, player):
            player.maxpopularity -= 40000
    
    class TheBook(Item):
        id = 606
        name = _('{color=#9500ff}书{/color}')
        kind = _('收藏品')
        maxCd = 0
        maxDu = -1
        isUnique = True
        canQuit = False
        reuse = False
        info = _('使用后消耗该道具，降低严重程度至当前周的严重程度下限，当严重程度高于1.0时，使严重倍率强制变为1.0。')
        ad = _('一本不知道来由的书，你总觉得这文字十分熟悉，故事中主角的遭遇与你相似又不尽相同。')

        def useItemAction(self, player):
            player.severity = 0.1
            player.severityRegarded = min(1.0, player.severityRegarded)


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
        name = _('落雪景观球')
        kind = _('收藏品')
        maxCd = -1
        maxDu = 28  # 数字
        isUnique = True
        info = _('每日有概率降低严重程度。')
        ad = _('拨动底座的按钮便可以周而复始地播放一首十分经典的名为《Myosotis》的曲目。')

        def afterSleepAction(self, player):
            if not self.broken:
                if rra(player, 66):
                    player.gain_abi(-0.01, 'sev',due='落雪景观球')


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
                player.gain_mental(r, self.name, stat=self.name)



    class GymTicket(Item):
        id = 614
        name = _('健身房的有效会员卡')
        kind = _('收藏品')
        maxCd = -1
        maxDu = 1
        isUnique = True
        info = _('持有有效的会员卡可以进入健身房，仅本日有效。')
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
        name = _('{color=#9500ff}色情照片{/color}')
        kind = _('收藏品')
        maxCd = 3
        maxDu = -1
        isUnique = False
        reuse = True
        info = _('使用后获得勃起。')
        ad = _('知名男演员于秀爱的签名写真，照片中的他大开双腿展露出雄伟的下身，随后便是面带潮红的微笑和挺立的乳头……\n我焯太烧辣，我不行了，兄弟们我先冲啦！')

        def useItemAction(self, player):
            Erection.add(player)

    class PathosDoll(Item):
        id = 619
        name = _('{color=#9500ff}黑色狮子玩偶{/color}')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1
        isUnique = False
        info = _('降低5%的严重程度。\n在安排日程环节时可以点击。')
        ad = _('这东西太几把难夹到了。')

        def enableAction(self, player):
            Achievement313.achieve()
            Achievement.show()
            player.severityRegarded -= 0.05

        def disableAction(self, player):
            player.severityRegarded += 0.05

    class TomatoBrooch(Item):
        id = 620
        name = _('番茄胸针')
        kind = _('收藏品')
        maxCd = -1
        maxDu = 28
        isUnique = True
        info = _('降低5%的严重程度。')
        ad = _('十分漂亮，但胸针如果放在衣服上又太张扬，放在包上又很容易被蹭掉或者偷走……总之还是放在抽屉里最安全……')

        def enableAction(self, player):
            player.severityRegarded -= 0.05

        def disableAction(self, player):
            player.severityRegarded += 0.05
        

    

    
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
    
    class Flower4(Item):
        id = 624.1
        name = _('一支玫瑰花')
        kind = _('收藏品')
        maxCd = -1
        maxDu = 1
        isUnique = True
        info = _('没有任何效果。')
        ad = _('并不能让你获得真正的爱。')

        def enableAction(self, player):
            Achievement305.achieve()
            Achievement.show()
    
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

    class Knife(Item):
        id = 628
        name = _('水果刀')
        kind = _('工具')
        maxCd = 14
        maxDu = -1  # 数字
        isUnique = True
        info = _('使用后获得受伤和痛苦，恢复大量精神状态，并降低2%的严重程度。')
        ad = _('“没事的。\n虽然看起来很痛，但伤痕不算什么的。\n因为真正痛的并不是手腕。”')

        def useItemAction(self, player):
            renpy.transition(Dissolve(0.2), layer='master')
            renpy.show("veinmask")

            MentPun.clearByType(p)
            MentProb.clearByType(p)
            Injured.add(p)
            p.checkTask()
            Pain.add(p)
            
            rec = r2(ra(player, 4000, 7000)*0.01)
            temp = r2(0.02 * player.severity)
            player.gain_abi(-temp, 'sev', stat=self.name)
            player.gain_mental(rec, stat=self.name)

    class FixKit(Item):
        id = 629
        name = _('维修工具组')
        kind = _('工具')
        maxCd = 14
        maxDu = 4  # 数字
        isUnique = True
        info = _('使用后选择一个带有耐久度的收藏品或工具，无法修复自身，将其耐久度恢复至最大值。')
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

    class Bondage(Item):
        id = 630
        name = _('外科医疗工具组')
        kind = _('工具')
        maxCd = 14
        maxDu = 4  # 数字
        isUnique = True
        info = _('如果已经受伤，在使用之后的每天结束时，根据恢复率自动恢复受伤，并获得全额的恢复奖励。\n如果没有受伤则什么也不会发生。')
        ad = _('和你在某大型拼单电商网站发的广告上只卖九块九的工具组差不多，附赠的那瓶医用酒精里好像还有小黑点在蠕动。')

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
        maxDu = 4  # 数字
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
        maxDu = 4  # 数字
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
        
        def taskuse(self, player, poz):

            if self.items[poz].checkAvailable(player) != True:
                Notice.add(self.items[poz].checkAvailable(player))
            else:
                self.items[poz].sound()
                Stat.record(player, type(self.items[poz]))
                Notice.add(_('已使用物品：')+ self.items[poz].name)
                if self.items[poz].maxCd>0:
                    player.itemcd[type(self.items[poz])] = self.items[poz].maxCd 
                self.items[poz].useItemAction(player)
                routine_music(player)
                self.items[poz] = None
            Notice.show()
        
        def afterSleepAction(self, player):
            for i in range(len(self.items)):
                if type(self.items[i]) in (RawFish, CookedFish):
                    self.items[i] = self.items[i].frozen(player)


            
            

    class Cactus(Item):
        id = 634
        name = _('仙人掌盆栽')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1
        isUnique = True
        info = _('在安排日程环节时可以为其浇水。')
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
        info = _('持有时，降低15%的严重度倍率。')
        ad = _('你人生中仅有的值得你骄傲的东西。')

        def enableAction(self, player):
            Achievement306.achieve()
            Achievement.show()
            player.severityRegarded -= 0.15

        def disableAction(self, player):
            player.severityRegarded += 0.15

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
        info = _('持有时，提升15%的严重度倍率。')
        ad = _('仙人掌你都养不活，你还能干点啥？')

        def cond_info(self):
            return _('这东西已经开始发烂发臭了。')

        def sprite(self):
            return 'gui/object/cactus_0.png'

        def developer_info(self, player):
            return None

        def enableAction(self, player):
            player.severityRegarded += 0.15

        def disableAction(self, player):
            player.severityRegarded -= 0.15

    class CactusFood(Item):
        id = 637
        name = _('仙人掌肥料')
        kind = _('消耗品')
        maxCd = 7
        maxDu = 90
        reuse = False
        isUnique = False
        info = _('拥有仙人掌盆栽时，提升仙人掌的成长度。\n不能在非工作时间使用。')
        ad = _('由你不想知道的东西构成。')

        def sound(self):
            renpy.sound.play(audio.itemdefault)

        def checkAvailable(self, player):
            if self.broken:
                return _('物品已过期！不可被使用！')
            if not Cactus.has(player):
                return _('你需要先拥有一盆仙人掌盆栽。')
            if player.onVacation and not player.experience == 'wri':
                return _('只有在公司才能为仙人掌施肥。')
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
        info = _('在安排日程环节时可以点击。')
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
    
    class Mask(Item):
        id = 640
        name = _('一次性口罩')
        kind = _('消耗品')
        maxCd = 0
        maxDu = 90
        reuse = False
        info = _('仅一次当本日天气为雾霾时，获得效果以免疫雾霾的部分负面效果。')
        ad = _('并不能防止你生病。')

        def useItemAction(self, player):
            MaskEffect.add(player)

    class SunnyDoll(Item):
        id = 641
        name = _('晴天娃娃')
        kind = _('收藏品')
        maxCd = -1
        maxDu = 14
        isUnique = True
        info = _('晴天出现的几率提升15%，如果本日不是晴天，降低1点严重程度。\n简单难度下，此概率提升至50%。')
        ad = _('我们拜请天气之子，带来永恒的晴天。')



    class CoffeeMachine(Item):
        id = 642
        name = _('{color=#9500ff}咖啡机{/color}')
        kind = _('工具')
        maxCd = 0
        maxDu = -1  # 数字
        isUnique = True
        info = _('根据已有的材料制作一杯咖啡。')
        ad = _('拥有一台咖啡机也算是我小时候的梦想之一吧。')

        def use(self, player):
            if self.checkAvailable(player) != True:
                showNotice([self.checkAvailable(player)])
            else:
                renpy.show_screen(_screen_name='coffee_selected', player=player)
            

        def checkAvailable(self, player):
            if not Coffee1.has(player):
                return _('你至少需要一袋袋装咖啡豆才能制作咖啡。')
            return True

        def useItem(self, player, i):
            Stat.record(player, type(self))
            Notice.show()

    class Coffee1(Item):
        id = 643
        name = _('袋装咖啡豆')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1
        info = _('用于制作咖啡。')
        ad = _('你绝对不想生吃这东西。')
        p = 0.1

    
    class Coffee2(Item):
        id = 644
        name = _('盒装椰汁')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1
        info = _('用于制作生椰拿铁。')
        ad = _('你很想尝尝味道，但你怕不小心喝光一整瓶。')
        p = 0.15

    
    class Coffee3(Item):
        id = 645
        name = _('盒装牛奶')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1
        info = _('用于制作摩卡咖啡。')
        ad = _('产自一位雄性精牛……我开玩笑的。')
        p = 0.15



    class FishingRod(Item):
        id = 646
        name = _('竹木鱼竿')
        kind = _('工具')
        maxCd = -1
        maxDu = 6  # 数字
        isUnique = True
        info = _('最基础的钓鱼竿，可以在森林公园钓鱼。')
        ad = _('就像是新手教学会直接赠送的鱼竿一样，很便宜但容易坏。')

        def __init__(self, player):
            super(FishingRod, self).__init__(player)
            self.fishes = 0
            self.qtys = 0
            self.trash = 0
            self.treasure = 0
            self.goldfishes = 0
            self.goldfishmon = None
            self.goldfishday = None

        def getPrincipalInfo(self):
            if not p:
                return self.info
            showinfo = '\n\n已使用此鱼竿钓上 %s 条鱼，共计品质 %s。\n钓上垃圾 %s 次，钓到宝藏 %s 次，钓到黄金鱼 %s 次。' % (self.fishes, self.qtys, self.trash, self.treasure, self.goldfishes)
            if self.goldfishday:
                showinfo += '\n\n%s月%s日那天对你来说一定很特别，你在这天用这根钓竿第一次钓上了一条黄金鱼。' % (self.goldfishmon, self.goldfishday)
            return self.info + showinfo

        def use(self, player):
            Stat.record(player, type(self))
                
            Notice.add(_('已使用物品：')+ self.name)
            if self.maxCd>0:
                player.itemcd[type(self)] = self.maxCd 
            if self.du > 0:
                if FishingAccessory3.has(player) and rra(player, 33):
                    Notice.add(_('由于钓具箱，没有消耗耐久。'))
                else:
                    self.du -= 1
                    if self.du == 0:
                        Notice.add(self.name + _('已损坏！'))
                        self.broken = True
                        self.timeUpAction(player)
                        self.disableAction(player)
            
            self.useItemAction(player)
                
            Notice.show()

        def equipAction(self, player):
            pass

        def unequipAction(self, player):
            pass

    class FishingRod1(FishingRod):
        id = 646
        name = _('竹木鱼竿')
        kind = _('工具')
        maxCd = -1
        maxDu = 6  # 数字
        isUnique = True
        info = _('最基础的钓鱼竿，可以在森林公园钓鱼。')
        ad = _('就像是新手教学会直接赠送的鱼竿一样，很便宜但容易坏。')
        p = 0.5


    class FishingRod2(FishingRod):
        id = 647
        name = _('玻璃纤维钓竿')
        kind = _('工具')
        maxCd = -1
        maxDu = 12  # 数字
        isUnique = True
        info = _('稍微好一点的钓鱼竿，可以在森林公园钓鱼。\n提高10点渔力，提高1点捕获力。')
        ad = _('能经受较大的弯折，但十分重。')
        p = 3

        def equipAction(self, player):
            player.fishpower += 10
            player.fishpoint += 1

        def unequipAction(self, player):
            player.fishpower -= 10
            player.fishpoint -= 1

    class FishingRod3(FishingRod):
        id = 648
        name = _('碳纤维鱼竿')
        kind = _('工具')
        maxCd = -1
        maxDu = 24  # 数字
        isUnique = True
        info = _('精致的钓鱼竿，可以在森林公园钓鱼。\n提高30点渔力，提高2点捕获力，提高5%暴击率。')
        ad = _('又轻又结实，十分优秀的钓鱼竿。')
        p = 6

        def equipAction(self, player):
            player.fishpower += 30
            player.fishpoint += 2
            player.fishcrit += 5

        def unequipAction(self, player):
            player.fishpower -= 30
            player.fishpoint -= 2
            player.fishcrit -= 5

    class FishingRod4(FishingRod):
        id = 649
        name = _('钛合金鱼竿')
        kind = _('工具')
        maxCd = -1
        maxDu = 48  # 数字
        isUnique = True
        info = _('顶级钓鱼竿，可以在森林公园钓鱼。\n提高50点渔力，提高3点捕获力，提高10%暴击率。\n钓鱼时有33%的概率不消耗精力。')
        ad = _('宣传语是“永不空军”。')
        p = 20

        def equipAction(self, player):
            player.fishpower += 50
            player.fishpoint += 3
            player.fishcrit += 10

        def unequipAction(self, player):
            player.fishpower -= 50
            player.fishpoint -= 3
            player.fishcrit -= 10

    class FishingAccessory1(Item):
        id = 650
        name = _('优质钓鱼线')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1  # 数字
        isUnique = True
        info = _('钓鱼线永远都不会断。')
        ad = _('它曾参加过古筝计划。')
        p = 5


    class FishingAccessory2(Item):
        id = 651
        name = _('渔夫耳环')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1  # 数字
        isUnique = True
        info = _('渔力增加10点。')
        ad = _('它来自一位喜欢给人发布钓鱼任务的渔夫。')

        def enableAction(self, player):
            player.fishpower += 10

        def disableAction(self, player):
            player.fishpower -= 10

    class FishingAccessory3(Item):
        id = 652
        name = _('钓具箱')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1  # 数字
        isUnique = True
        info = _('鱼竿有33%的概率不消耗耐久。')
        ad = _('如果你有工匠作坊，就可以把这些东西合成到一起了。')
        p = 5

    
    class FishingAccessory4(Item):
        id = 653
        name = _('小丑鱼拟饵')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1  # 数字
        isUnique = True
        info = _('降低33%钓到垃圾的概率，提高33%钓到宝藏的概率。')
        ad = _('海之眷顾III')
        p = 5

    class FishingTrash1(Item):
        id = 654
        name = _('旧报纸')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1  # 数字
        info = _('垃圾。')
        ad = _('它看起来不好吃。')

    class FishingTrash2(Item):
        id = 655
        name = _('破碎的眼镜')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1  # 数字
        info = _('垃圾。')
        ad = _('有人又要为了看到别人而花钱了。')

    class FishingTrash3(Item):
        id = 656
        name = _('浮木')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1  # 数字
        info = _('垃圾。')
        ad = _('不可以骂人哦。')
    
    class FishingTrash4(Item):
        id = 657
        name = _('腐肉')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1  # 数字
        info = _('垃圾。')
        ad = _('它来自于一只不太开心的僵尸。')

    class FishingTrash5(Item):
        id = 658
        name = _('破钓竿')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1  # 数字
        info = _('垃圾。')
        ad = _('它并没有任何附魔。')


    class FishingItem1(Item):
        id = 659
        name = _('命名牌')
        kind = _('收藏品')
        maxCd = 0
        maxDu = -1  # 数字
        reuse = False
        info = _('使用后修改自己的名字。')
        ad = _('为什么不是修改别人的？')

        def use(self, player):
            renpy.show_screen(_screen_name='screen_rename', player=player)

    class FishingItem2(Item):
        id = 660
        name = _('鹦鹉螺壳')
        kind = _('收藏品')
        maxCd = -1
        maxDu = -1  # 数字
        info = _('提升1点捕获力，5%暴击率。')
        ad = _('用于制作潮涌核心，但你需要有一个工作台。')

        def enableAction(self, player):
            player.fishpoint += 1
            player.fishcrit += 5
        
        def disableAction(self, player):
            player.fishpoint -= 1
            player.fishcrit -= 5
    
    class FishingItem3(Item):
        id = 661
        name = _('神秘液体瓶')
        kind = _('收藏品')
        maxCd = 0
        maxDu = -1  # 数字
        isUnique = False
        reuse = False
        info = _('使用后钓鱼最大精力值永久提升1点，最多提升3次，如果已提升3次，那么使用后会永久提升5点渔力。')
        ad = _('内容物看上去十分粘稠。')

        def useItemAction(self, player):
            if player.fishmaxenergy < 6:
                player.fishmaxenergy += 1
                Notice.add('这东西的味道真奇怪……总之钓鱼最大精力值永久提升了1点。')
            else:
                player.fishpower += 5
                Notice.add('这东西的味道真奇怪……总之渔力永久提升了5点。')

    class FishingItem4(Item):
        id = 662
        name = _('金戒指')
        kind = _('收藏品')
        maxCd = 0
        maxDu = -1  # 数字
        info = _('使用后卖出以获得大量金钱。')
        ad = _('也许你可以坐等它升值。')

        def useItemAction(self, player):
            money = int(player.price * ra(player, 8, 12) * f())
            player.money += money
            Notice.add('卖出金戒指后，你获得了%s元。'%money)
            self.sub(player)

        def getPrincipalInfo(self):
            if not p:
                return self.info
            showinfo = '\n\n预计获得金钱：%s ~ %s' % (int(p.price * 7.2), int(p.price * 13.2))
            return self.info + showinfo

    class Tarot(Item):
        id = 663
        name = _('塔罗牌盒')
        kind = _('工具')
        maxCd = 1
        maxDu = -1  # 数字
        isUnique = True
        info = _('抽取一张卡牌，并没有实际作用。')
        ad = _('卡面全部都被绘制成了猫咪的样子，除了恶魔牌——一只招手的金毛犬。')
        cardset = ('愚者','魔术师','女祭司','女皇','皇帝','教皇','恋人','战车','力量','隐者','命运之轮','正义','倒吊人','死神','节制','恶魔','塔','星星','月亮','太阳','审判','世界')

        def __init__(self, player):
            super(Tarot, self).__init__(player)
            self.card = '正位：愚者'

        def getPrincipalInfo(self):
            if not p:
                return self.info
                
            if p.getcd(type(self)) == 1:
                return self.info + '\n\n今日卡牌：%s' % self.card
            return self.info + '\n\n{color=#f00}今日还未抽卡{/color}'


        def useItemAction(self, player):
            if rs(player,1,2)==1:
                self.card = '正位：'
            else:
                self.card = '逆位：'
            self.card += rcs(player,self.cardset)
            Notice.add('今日抽到的卡牌是：%s！' % self.card)
    
    class D6(Item):
        id = 664
        name = _('六面骰')
        kind = _('工具')
        maxCd = 0
        maxDu = -1  # 数字
        isUnique = True
        info = _('抽取1~6的数字，并没有实际作用。')
        ad = _('透明的骰子，适合丢在你朋友的脸上。')
        
        def useItemAction(self, player):
            Notice.add('你掷出了%s！' % rd(1,6))

    class D20(Item):
        id = 665
        name = _('二十面骰')
        kind = _('工具')
        maxCd = 0
        maxDu = -1  # 数字
        isUnique = True
        info = _('抽取1~20的数字，并没有实际作用。')
        ad = _('哈！大失败！')
        
        def useItemAction(self, player):
            point = rd(1,20)
            Notice.add('你掷出了%s！' % point)
            if point == 1:
                Notice.add('哈哈，大失败！')
            if point == 20:
                Notice.add('惊了，居然是大成功。')

    class D1000(Item):
        id = 666
        name = _('一千面骰')
        kind = _('工具')
        maxCd = 0
        maxDu = -1  # 数字
        isUnique = True
        info = _('抽取1~1000的数字，并没有实际作用。')
        ad = _('嗯？这不就是一个球吗！')
        
        def useItemAction(self, player):
            Notice.add('你掷出了%s！' % rd(1,1000))

    class PackOfInstantNoodles(Item):
        id = 695
        name = _('一箱方便面')
        kind = _('消耗品')
        maxCd = 0
        maxDu = -1
        reuse = False
        info = _('使用后获得12个泡面。')
        ad = _('你不喜欢吃泡面，但你更不喜欢深夜饿肚子。')

        def useItemAction(self, player):
            StreetFood10.add(p, 12)

    class FishingRod99(FishingRod):
        id = 696
        name = _('超级无敌钓竿')
        kind = _('工具')
        maxCd = -1
        maxDu = -1  # 数字
        isUnique = True
        info = _('最强钓鱼竿，可以在森林公园钓鱼。\n提高100点渔力，全自动钓鱼。')
        ad = _('你已经用钱征服了这个钓鱼游戏，现在去干点别的吧？')
        p = 50

        def equipAction(self, player):
            player.fishpower += 100

        def unequipAction(self, player):
            player.fishpower -= 100

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
            info2 = '\n\n平均写作技巧：'+str(cInfo[3])+'\n已完成字数：'+str(cInfo[0])+'\n文稿总价值：'+str(cInfo[1])+'\n共消耗灵感：'+str(cInfo[2])

            return info1 + info2

        def write(self, player, exact=False):
            cms = self.comm.write(player, exact)
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
            info2 = '\n\n平均写作技巧：'+str(cInfo[3])+'\n已完成字数：'+str(cInfo[0])+'\n文稿总价值：'+str(cInfo[1])+'\n共消耗灵感：'+str(cInfo[2])

            return info1 + info2

        def getReward(self, player):
            player.doneComm += 1
            money = r2(self.comm.contentInfo()[1])
            ins = int(0.2 * self.comm.contentInfo()[2]-10*player.writing_grade())
            if money <= 0:
                money = 0.0
            player.money += money
            commwri = self.comm.contentInfo()[3]

            
            player.recentCommWri.append(commwri)
            player.recentCommIns.append(self.comm.contentInfo()[2])

            if len(player.recentCommWri) == 4:
                player.recentCommWri.pop(0)
                player.recentCommIns.pop(0)
            
            
            Notice.add(_('完成委托！'))
            if commwri < self.comm.require:
                punish = commwri/self.comm.require
                honor = 10+int(100-punish*100)
                player.writing_honor -= honor
                money = r2(money*punish*0.75)
                if money>0:
                    player.gainCommPrice += money
                    Notice.add(_('因为没能达到写作要求，只获得了%s元报酬。') % money)
                    Notice.add(_('失去了%s点信誉分。') % honor)
                else:
                    Notice.add(_('未获得报酬！'))
                    Notice.add(_('因为没能达到写作要求，失去了%s点信誉分。') % honor)
            else:
                if money>0:
                    player.gainCommPrice += money
                    Notice.add(_('获得了%s元报酬。') % money)
                    if player.experience == 'wri':
                        self.writing_popularity = 0.5 + 0.25 * ra(player, 1, 6)

                        di = self.comm.contentInfo()[2] * 0.5 * (commwri/self.comm.require)**2

                        maxpopularity = player.maxpopularity
                        up = self.comm.predictpopularity(player, di)
                        if self.comm.remarks:
                            up *= (1 + self.comm.remarks[0] * 0.05)
                            up = int(up)

                        ins = int(0.5 * (di-10*player.writing_grade()))
                        if player.popularity + up <= 1000 or player.popularity >= maxpopularity:
                            Notice.add(_('已将文稿发布到写作平台！\n平台没有新增粉丝。'))
                        elif up < 0:
                            player.popularity += up
                            Notice.add(_('已将文稿发布到写作平台！\n流失了%s个新粉丝。') % up)
                        else:
                            if up+player.popularity > maxpopularity:
                                up = maxpopularity - player.popularity
                            player.popularity += up
                            Notice.add(_('已将文稿发布到写作平台！\n涨了%s个新粉丝。') % up)

                        if not WriterProof.has(player) and player.popularity >= 20000:
                            Notice.add(_('由于您的粉丝数已经超过20000，平台特颁发作家证明，以资鼓励。'))
                            WriterProof.add(player)
                        




                else:
                    Notice.add(_('未获得报酬！'))
                    if player.writing_honor<100:
                        honor = min(10, 100-player.writing_honor)
                        player.writing_honor+=honor
                        Notice.add(_('恢复了%s点信誉分。') % honor)

            if ins > 0:
                FixedInspiration.add(player, ins)
                Notice.add(_('恢复了%s层写作素材！') % ins)
            Notice.show()
            self.remove(player)

        def uploadToSocial(self, player):
            di = self.comm.contentInfo()[2]
            player.doneFree += 1
            maxpopularity = player.maxpopularity
            up = self.comm.predictpopularity(player, di)
            if self.comm.remarks:
                up *= (1 + self.comm.remarks[0] * 0.05)
                up = int(up)

            ins = int(0.5 * (di-10*player.writing_grade()))
            if player.popularity + up <= 1000 or player.popularity >= maxpopularity:
                Notice.add(_('已将文稿发布到写作平台！\n平台没有新增粉丝。'))
            elif up < 0:
                player.popularity += up
                Notice.add(_('已将文稿发布到写作平台！\n流失了%s个新粉丝。') % up)
            else:
                if up+player.popularity > maxpopularity:
                    up = maxpopularity - player.popularity
                player.popularity += up
                Notice.add(_('已将文稿发布到写作平台！\n涨了%s个新粉丝。') % up)

            if ins > 0:
                FixedInspiration.add(player, ins)
                Notice.add(_('恢复了%s层写作素材！') % ins)

            if not WriterProof.has(player) and player.popularity >= 20000:
                Notice.add(_('由于您的粉丝数已经超过20000，平台特颁发作家证明，以资鼓励。'))
                WriterProof.add(player)
            
            Notice.show()
            self.remove(player)

    def timeUpAction(self, player):  # 时间结束的操作，不包括删除Effect的操作，一般是持续时间为0转化为其他Effect时调用
        player.writing_honor -= 20
        Notice.add(_('因为没能在限定时间内完成委托，失去了20点信誉分。'))



    def wr(p):
        Inspiration.add(p, 10)
        FreewheelingWriting.executeTask(p)
        Notice.show()



