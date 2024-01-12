init python early:

    comm_names = [_("设定委托"), _("同人清水委托"), _("甜文委托"), _("感伤委托"), _("色文委托"), _("设定背景委托"), _("人物背景故事委托"), _("外包游戏剧情文案"), _("网络游戏游戏世界观背景")]
    comm_informal_names = [_("阳台"), _("窗户"), _("风"), _("都市"), _("眼皮"), _("愤怒"), _("入迷"), _("气泡，旋涡"),
                        _("放浪"), _("征服者"), _("我"), _("被害者"), _("假意"), _("研究"), _("撤离"), _("品味"),
                        _("恐惧"), _("余烬"), _("败者"), _("诋毁与拯救"), _("嘈杂"), _("吊兰调研笔记"),
                        _("外星生命调研笔记"), _("被捕食者调研笔记"), _("触摸"), _("与触手"), _("共浴"),
                        _("逝者"), _("水妖"), _("服务"), _("待命"), _("他和为他工作之人"), _("深入"), _("极寒"),
                        _("刻印"), _("鱼水"), _("报酬"), _("远行"), _("奖励"), _("讨伐"),
                        _("晋升胸针"), _("断骨"), _("阿斯卡隆漫游指南"), _("活着"), _("未知之物")]


    class Comm:
        def __init__(self, player):
            def wri(p):
                wg = player.writing_grade()
                if rra(player, min(5 * player.week, 50)) or wg<0.5:
                    return r2(ra(p, 50, 300) * 0.01)
                return r2(ra(p, 85, 115) * 0.01 * wg)

            def genePrice(player):
                if WriterProof.has(player):
                    pr = 0.8
                    pr += (player.wri() - 1) / 3.5
                    f = ((player.wri() - 1) / 3.5) + 1
                    while rra(player, 70 - 2.5 * player.week):
                        pr += ra(player, 10 * f, 25 * f) * 0.01
                    if pr > 3.5:
                        pr = 3.5
                else:
                    pr = 0.75
                    pr += (player.wri() - 1) / 4
                    f = ((player.wri() - 1) / 4) + 1
                    while rra(player, 70 - 2.5 * player.week):
                        pr += ra(player, 5 * f, 20 * f) * 0.01
                    if pr > 2.5:
                        pr = 2.5
                
                pr *= 1 + player.writing_valuebouns()
                return r2(pr)

            self.name = rca(player, comm_names)
            self.require = wri(player)
            self.priceFluctuation = genePrice(player)
            self.needWord = -1
            self.needInspiration = -1
            self.du = -1
            if rra(player, 40) or self.priceFluctuation > 1.5:
                self.needWord = int(self.require**2 * 10 * ra(player, 75, 225)*0.01) * 100
            if rra(player, 40) or self.priceFluctuation > 1.5:
                self.needInspiration = int(player.writing_grade() * ra(player, 5, 20))
            if rra(player, 40) or self.priceFluctuation > 1.5:
                self.du = ra(player, 2, 7)
            self.writeCounts = 0
            self.content = []
            self.info = ""
            self.inputs = None
            self.remarks = []
            self.broken = False
            self.freewheeling = False

        def __eq__(self, other):
            return id(other) == id(self)

        def commInfo(self):
            if self.freewheeling:
                return '{size=+2}委托内容：' + self.name + '{/size}'
            info1 = _('{size=+2}委托内容：') + self.name + _('{/size}\n水平需求：') + str(self.require) + _('\n提出价格：') + str(self.require*100*self.priceFluctuation) + "/千字"

            info2 = "\n需求："
            if self.needWord == -1 and self.needInspiration == -1 and self.du == -1:
                info2 += "\n · 无需求"
            else:
                if self.needWord != -1 :
                    info2 += "\n · 字数需求：" + str(self.needWord)
                if self.needInspiration != -1 :
                    info2 += "\n · 灵感需求：" + str(self.needInspiration)
                if self.broken:
                    info2 += "\n · 委托已超时："
                elif self.du != -1 :
                    info2 += "\n · 时间需求：" + str(self.du)
            
            return info1 + info2

        def contentInfo(self):
            word = 0
            rewara = 0
            ins = 0
            wri = 0
            for i in self.content:
                word += i[0]
                rewara += i[1]
                ins += i[2]
                wri += i[3]
            if self.content:
                wri = r2(wri/len(self.content))
            if rewara <= 0:
                rewara = 0.0

            return [int(word), r2(rewara), ins, wri]

        def predictvalue(self, player, ins=None,exact=False):
            playerwri = player.wri()
            word = int(playerwri**2 * 1000 * f())
            if exact and self.needWord != -1:
                if word > self.needWord:
                    word = self.needWord
                
                elif word < self.needWord and word*1.5 >= self.needWord:
                    word = self.needWord
                    sev = max(int((self.needWord - word) * 10 / (word * 0.5)),2)*ra(player, 8, 12)*f()
                    player.gain_mental(-sev, due='精准写作')

            if Stayuplate.has(player):
                word = int(word * 0.5)
                
            
            value = self.require*0.1*self.priceFluctuation


            if self.needWord != -1:
                reward = value * self.needWord
            else:
                reward = value * word

            return r2(reward), word

        def predictpopularity(self, player, ins):
            di = ins
            np = player.popularity/1000
            r = 0.5 * (di - 7)
            up = int(r * (np-np*np/100) * 60)
            up *= 1.0 - player.week * 0.025

            return int(up)





        def write(self, player, exact=False):
            if player.retval1 is not None:
                self.inputs = player.retval1
                player.retval1 = None

            ins = 1
            if exact and self.needInspiration != -1:
                
                needins = self.needInspiration
                if Inspiration.has(player):
                    igs = Inspiration.getstack(player)
                    if needins <= igs:
                        
                        Inspiration.subByType(player, needins)
                        ins = self.needInspiration
                        needins = 0

                    else:
                        needins -= igs
                        Inspiration.clearByType(player)
                        ins += igs

                if FixedInspiration.has(player) and needins > 0:
                    igs = FixedInspiration.getstack(player)
                    if needins <= igs:
                        
                        FixedInspiration.subByType(player, needins)
                        ins = self.needInspiration
                        needins = 0
                        
                    else:
                        needins -= igs
                        FixedInspiration.clearByType(player)
                        ins += igs

            else:
                
                if Inspiration.has(player):
                    ins += Inspiration.getstack(player)
                    Inspiration.clearByType(player)
                if FixedInspiration.has(player):
                    ins += FixedInspiration.getstack(player)
                    FixedInspiration.clearByType(player)

            reward, word = self.predictvalue(player, ins, exact)


            MentRezA.add(player, int(ins * 0.15))
            if self.freewheeling:
                Notice.add(_('已进行一次随笔写作，已写字数%s，共消耗灵感%s层，预计可以涨粉%s个。') % (word, ins, self.predictpopularity(player, ins)))
            else:
                Notice.add(_('已进行一次委托写作，已写字数%s，共消耗灵感%s层，预计价值%s元。') % (word, ins, reward))

            g = int(ins / 5 + player.writingGain)

            if g >= 1: 
                player.gain_abi(g * 0.01, 'wri', extra=True, stat='委托写作')


            pwri = player.wri()
            if SpecialInspiration.has(player):
                gs = SpecialInspiration.getstack(player)
                pwri *= (1 + gs * 0.05)
                self.remarks.append(gs)
                SpecialInspiration.clearByType(player)

            if len(self.content) == 0:
                self.content.append([int(word), r2(reward), ins, pwri])
            else:
                self.content.append([int(word), 0, ins, pwri])

            self.writeCounts += 1

            word = 0
            rewara = 0
            ins = 0
            wri = 0
            for i in self.content:
                word += i[0]
                ins += i[2]
                rewara += i[1]
                wri += i[3]

            if self.content:
                wri = r2(wri/len(self.content))
            finished = 0

            if self.needWord != -1:
                if word >= self.needWord:
                    finished += 1
            else:
                if word > 0:
                    finished += 1

            if self.needInspiration != -1:
                if ins >= self.needInspiration:
                    finished += 1
            else:
                finished += 1


            if finished == 2:
                CommissionReward.add(player)
                cms = FinishedCommission(player)
                GuideI.unlock(FinishedCommission)
                cms.comm = self
                return cms

            cms = UnfinishedCommission(player)
            cms.comm = self
            return cms

            # self.inputs.append(inputs)

        def checkWritable(self, player):
            if self.broken:
                return _('委托已经超出期限！')
            return True

        def timeUpdate(self, player):
            if self.du > 0:
                self.du -= 1
                if self.du == 0:
                    self.broken = True
