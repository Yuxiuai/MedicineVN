init python early:

    comm_names = [_("设定委托"), _("同人清水委托"), _("甜文委托"), _("感伤委托"), _("色文委托"), _("设定背景委托"), _("人物背景故事委托"), _("外包游戏剧情文案"), _("网络游戏游戏世界观背景")]
    comm_informal_names = [_("阳台"), _("窗户"), _("风"), _("都市"), _("眼皮"), _("愤怒"), _("入迷"), _("气泡，旋涡"),
                        _("放浪"), _("征服者"), _("我"), _("被害者"), _("假意"), _("研究"), _("撤离"), _("品味"),
                        _("恐惧"), _("余烬"), _("败者"), _("诋毁与拯救"), _("嘈杂"), _("吊兰调研笔记"),
                        _("外星生命调研笔记"), _("被捕食者调研笔记"), _("触摸"), _("与触手"), _("共浴"),
                        _("逝者"), _("水妖"), _("服务"), _("待命"), _("他和为他工作之人"), _("深入"), _("极寒"),
                        _("刻印"), _("鱼水"), _("报酬"), _("远行"), _("洗濯"), _("擢升"), _("奖励"), _("讨伐"),
                        _("晋升胸针"), _("断骨"), _("讴歌终焉之诗"), _("阿斯卡隆漫游指南"), _("活着"), _("未知之物")]


    class Comm:
        def __init__(self, player):
            def wri(p):
                return r2(ra(p, 85, 105) * 0.01 * player.wri())

            def genePrice(player):
                if not WriterProof.has(player):
                    pr = 0.8
                    pr += (player.wri() - 1) / 4
                    f = ((player.wri() - 1) / 4) + 1
                    while rra(player, 60):
                        pr += ra(player, 10 * f, 30 * f) * 0.01
                    if pr > 2.5:
                        pr = 2.5
                else:
                    pr = 0.75
                    pr += (player.wri() - 1) / 4
                    f = ((player.wri() - 1) / 4) + 1
                    r = 0
                    while rra(player, 60):
                        pr += ra(player, 5 * f, 25 * f) * 0.01
                    if pr > 3.5:
                        pr = 3.5
                
                return r2(pr)

            self.name = rca(player, comm_names)
            self.require = wri(player)
            self.priceFluctuation = genePrice(player)
            self.needWord = -1
            self.needInspiration = -1
            self.du = -1
            if rra(player, 40) or self.priceFluctuation > 1.5:
                self.needWord = int(self.require**2 * 1000 * f())
            if rra(player, 40) or self.priceFluctuation > 1.5:
                self.needInspiration = ra(player, 20, 35)
            if rra(player, 40) or self.priceFluctuation > 1.5:
                self.du = ra(player, 7, 21)
            self.writeCounts = 0
            self.content = []
            self.info = ""
            self.inputs = None
            self.remarks = []
            self.broken = False
            self.freewheeling = False

        def __eq__(self, other):
            return id(other) == id(self)

        def show(self):
            print(_('委托名:%s, 写作技巧需求:%s\n价格修正:%s倍') % (self.name, self.require, self.priceFluctuation))
            if self.needWord != -1:
                print(_('字数需求:%s ') % self.needWord, end='')
            else:
                print(_('无字数需求 '), end='')
            if self.needInspiration != -1:
                print(_('灵感需求:%s ') % self.needInspiration, end='')
            else:
                print(_('无灵感需求 '), end='')
            if self.du != -1:
                print(_('委托到期时间:%s') % self.du)
            else:
                print(_('无时间要求'))

        def commInfo(self):
            info1 = _('{size=+2}委托内容：') + self.name + _('{/size}\n写作技巧需求：') + str(self.require) + _('\n价格修正：') + str(
                int(self.priceFluctuation * 100)) + '%'

            if self.needWord != -1:
                info2 = _('\n字数需求：') + str(self.needWord)
            else:
                info2 = _('\n无字数需求 ')

            if self.needInspiration != -1:
                info2 += _('\n灵感需求：') + str(self.needInspiration)
            else:
                info2 += _('\n无灵感需求 ')
                
            if self.broken:
                info2 += _('\n{color=#ff0000}委托已超时{/color}')
            elif self.du != -1:
                info2 += _('\n委托到期时间：') + str(self.du)
            else:
                info2 += _('\n无时间要求')
            
            if config.developer:
                info2 += '\n\n{color=#fde827}预计收益：\n灵感为1：%s\n灵感为50：%s\n灵感为100：%s\n灵感为200：%s{/color}' % tuple(self.predictvalue(p))

            return info1 + info2

        def contentInfo(self):
            word = 0
            rewara = 0
            ins = 0
            for i in self.content:
                word += i[0]
                rewara += i[1]
                ins += i[2]

            if rewara <= 0:
                rewara = 0.0

            return [int(word), r2(rewara), ins]

        def predictvalue(self, player, ins=None):
            playerwri = min(5, player.wri())

            price = -0.04 * playerwri ** 2 + 0.3 * playerwri + 0.7
            price *= 150
            if EffectGameModule2_2.has(player):
                price *= 1.3

            
            
            word = int(playerwri**2 * 1000 * f())
            if self.needWord != -1:
                valueword = self.needWord / self.require
            else:
                valueword = word / playerwri
            

            if not ins:
                ins = 100
                value = ins * 0.075 * price * self.priceFluctuation * player.writeValuable

                if self.needInspiration != -1:
                    value *= 1.05

                if self.du != -1:
                    value *= 1.05

                if self.needWord != -1:
                    value *= 1.05
                    if word > self.needWord:
                        reward = value * valueword
                    else:
                        reward = value * valueword
                else:
                    reward = value * valueword

                reward *= 0.001

                return [r2(reward*0.01), r2(reward*0.5), r2(reward), r2(reward*2)]

            value = ins * 0.075 * price * self.priceFluctuation * player.writeValuable

            if self.needInspiration != -1:
                value *= 1.05

            if self.du != -1:
                value *= 1.05

            if self.needWord != -1:
                value *= 1.05
                if word > self.needWord:
                    reward = value * valueword
                else:
                    reward = value * valueword
            else:
                reward = value * valueword

            reward *= 0.001

            return r2(reward), word

        def predictpopularity(self, player, ins):
            di = ins
            np = player.popularity/1000
            r = 0.5 * (di - 7)
            up = int(r * (np-np*np/100) * 120)

            return up





        def write(self, player):
            if player.retval1 is not None:
                self.inputs = player.retval1
                player.retval1 = None

            EffectGameModule2_2.clearByType(player)

            ins = 1
            if Inspiration.has(player):
                ins += Inspiration.getstack(player)
                Inspiration.clearByType(player)
            if FixedInspiration.has(player):
                ins += FixedInspiration.getstack(player)
                FixedInspiration.clearByType(player)

            reward, word = self.predictvalue(player, ins)


            MentRezA.add(player, int(ins * 0.15))
            if self.freewheeling:
                Notice.add(_('已进行一次随笔写作，已写字数%s，共消耗灵感%s层，预计可以涨粉%s个。') % (word, ins, self.predictpopularity(player, ins)))
            else:
                Notice.add(_('已进行一次委托写作，已写字数%s，共消耗灵感%s层，预计价值%s元。') % (word, ins, reward))

            g = int(ins / 5 + player.writingGain)

            if g >= 1:
                player.writing += g * 0.01
                Notice.add(_('额外获得%s点写作技巧。') % g)

            if len(self.content) == 0:
                self.content.append([int(word), r2(reward), ins])
            else:
                self.content.append([int(word), 0, ins])

            self.writeCounts += 1

            word = 0
            rewara = 0
            ins = 0
            for i in self.content:
                word += i[0]
                ins += i[2]
                rewara += i[1]
                    

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
                cms.comm = self
                return cms

            cms = UnfinishedCommission(player)
            cms.comm = self
            return cms

            # self.inputs.append(inputs)

        def checkWritable(self, player):
            if self.broken:
                return _('委托已经超出期限！')
            if player.wri() < self.require:
                return _('写作技巧未达要求！')
            if self.needInspiration != -1:
                ins = 0
                if Inspiration.has(player):
                    ins += Inspiration.getstack(player)
                if FixedInspiration.has(player):
                    ins += FixedInspiration.getstack(player)
                if ins < self.needInspiration - self.contentInfo()[-1]:
                    return _('灵感层数未达要求！')
            return True

        def timeUpdate(self, player):
            if self.du > 0:
                self.du -= 1
                if self.du == 0:
                    self.broken = True
