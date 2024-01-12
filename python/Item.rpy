init python early:
    
    class Item:
        id = None
        name = None
        kind = None
        maxCd = 0  # -1 不可使用 0 没有使用cd
        maxDu = -1  # -1 不可损坏 0 已损坏
        isUnique = False  # 为True时，最大amount为1
        canQuit = True
        reuse = True
        info = None
        ad = None
        

        def __init__(self, player):
            self.amounts = 1
            self.du = self.maxDu
            self.broken = False
            self.star = False
            self.blocked = False
            self.gotWeek = player.week
            self.gotDay = player.today

        def __eq__(self, other):
            if type(self) != type(other):
                return False
            if self.du != other.du:
                return False
            if self.maxDu == -1: # 如果都为不可损坏而且满足上述条件，即便购买时间不同也认为相等
                return True
            if self.gotWeek != other.gotWeek:
                return False
            if self.gotDay != other.gotDay:
                return False
            return True

        def getPrefixInfo(self, player):

            if self.maxCd == -1 or self.broken or self.maxCd == -1:
                cd_info = _('不可使用  ')
            elif type(self) not in player.itemcd:
                if self.reuse:
                    cd_info = _('可重复使用  ')
                else:
                    cd_info = _('使用后消耗  ')
            else:
                cd_info = _('可使用时间：')+str(player.itemcd[type(self)])+_('天后  ')

            if self.maxDu == -1:
                du_info = _('不会损坏  ')
            elif self.kind in ('食物','实验药物','普通药物'):
                if self.broken:
                    du_info = _('已变质  ')
                elif self.du == 1:
                    du_info = _('即将变质：明天  ')
                else:
                    du_info = _('即将变质：')+str(self.du)+_('天后  ')
            elif self.kind == '工具':
                if self.broken:
                    du_info = _('已损坏  ')
                else:
                    du_info = _('耐久度：')+str(self.du)+_('  ')
                
            else:
                if self.broken:
                    du_info = _('已损坏  ')
                elif self.du == 1:
                    du_info = _('即将损坏：明天  ')
                else:
                    du_info = _('即将损坏：')+str(self.du)+_('天后  ')

            return _('数量：')+str(self.amounts)+ '\n' + cd_info + '\n'+du_info+ '\n'

        @classmethod
        def icon(cls):
            path = 'gui/items/%s.png' % cls.id
            if not renpy.loadable(path):
                path = 'gui/items/unknown.png'
            return path





        @classmethod
        def getPrincipalInfo(cls):
            type_info = _('\n\n') + cls.kind

            if cls.isUnique:
                uni_info = _('\n唯一')
            else:
                uni_info = ''

            return cls.info + type_info + uni_info

        def getSuffixInfo(self):
            return _('\n\n获取日期：第%s周的%s') % (self.gotWeek, weekdayFormat(self.gotDay))

        def timeUpdate(self, player):
            if self.du:
                if self.du > 0:
                    if self.kind != '工具':
                        self.du -= 1
                if self.du == 0:
                    if self.kind in ('食物', '实验药物', '普通药物'):
                        Notice.add(self.name + _('已过期！'))
                    else:
                        Notice.add(self.name + _('已损坏！'))
                    self.broken = True
                    self.timeUpAction(player)
                    self.disableAction(player)
                    if persistent.noBrokenItem and not Despair.has(player):
                        player.items.remove(self)
                    elif self.kind == '收藏品':
                        Trash.add(player)
                        player.items.remove(self)
                    
                
            

        @classmethod
        def has(cls, player):
            if not player:
                return False
            return cls in [type(i) for i in list(filter(lambda x: x.broken == False, player.items))]

        @classmethod
        def get(cls, player):  # 需要先用has检测
            return list(filter(lambda x: type(x) == cls and not x.broken, player.items))[0]

        @classmethod
        def getBrokenItemByType(cls, player):  # 需要先用has检测
            return list(filter(lambda x: type(x) == cls and x.broken, player.items))[0]
            
        @classmethod
        def hasByItem(cls, player, item):
            if not player:
                return False
            return item in player.items

        @classmethod
        def getByItem(cls, player, item):  # 需要先用has检测
            return player.items[player.items.index(item)]

        @classmethod
        def getamounts(cls, player):  # 需要先用has检测
            amounts = 0
            for i in player.items:
                if type(i) == cls and not i.broken:
                    amounts += i.amounts
            return amounts

        @classmethod
        def add(cls, player, times=1):  # 增加新效果或增加层数
            if times == 0:
                return
            GuideI.unlock(cls)
            if cls.kind == '书籍':
                Freshness.add(player)
                if len(list(filter(lambda x: x.kind=='书籍' and not x.has(p) and x.id not in (), ALLITEMS))) == 0:
                    Achievement302.achieve()
                    Achievement.show()
                    Notice.show()
            for i in range(times):
                cls.defaultAddItem(player)

        def remove(self, player):
            if not self.broken:
                self.disableAction(player)
            if self in player.items:
                player.items.remove(self)

        def sub(self, player, times=1):  # 减少层数
            if times == 0:
                return
            for i in range(times):
                self.subStackAction(player)
                self.amounts -= 1
                if self.amounts <= 0:
                    self.remove(player)
                    return

        def enableAction(self, player):  # 启用Buff时进行的操作，一般是提供某些数据
            pass

        def disableAction(self, player):  # Buff无效时的操作，无论是被删除还是被转化还是时间到都会调用，enableAction的反向操作，恢复其对数据的修改
            pass

        def addStackAction(self, player):  # 每次添加层数的操作，一般是某些根据层数给予效果的Effect需要设置
            pass

        def subStackAction(self, player):  # 减少层数的操作，前者的反向函数
            pass

        def timeUpAction(self, player):  # 时间结束的操作，不包括删除Effect的操作，一般是持续时间为0转化为其他Effect时调用
            pass

        def afterSleepAction(self, player):  # 睡眠之后的操作，玩家睡眠后触发的效果，也包括起床效果
            pass

        @classmethod
        def defaultAddItem(cls, player):  # 默认的add函数，禁止重写
            newItem = cls(player)

            if cls.isUnique and cls.has(player):
                if cls.maxDu >0:
                    cls.get(player).du = cls.maxDu
                    Notice.add(_('已有%s，刷新了耐久度！') % cls.name)
                else:
                    Notice.add(_('已有%s，无法再次获取！') % cls.name)
            elif not cls.hasByItem(player, newItem):  # 是否存在，如果不存在
                Notice.add(_('获得新物品：%s！') % cls.name)
                newItem.addStackAction(player)
                newItem.enableAction(player)
                player.items.append(newItem)
            else:
                #Notice.add(_('获得%s：%s！') % (cls.kind, cls.name))
                oldItem = cls.getByItem(player, newItem)
                oldItem.addStackAction(player)
                oldItem.amounts += 1
            sortByID(player.items)
            

        def useItemAction(self, player):
            pass

        def checkAvailable(self, player):
            if self.maxCd == -1:
                return _('物品不可被使用！')
            if self.broken:
                return _('物品已过期或损坏！不可被使用！')
            if type(self) not in player.itemcd:
                return True
            else:
                return _('物品仍在冷却时间中！')

        def sound(self):
            if self.kind in (_('食物'), _('普通药物'), _('实验药物')):
                renpy.sound.play(audio.itemdrink)
            elif self.kind in (_('手稿'), _('书籍'), _('专业类书籍')):
                renpy.sound.play(audio.itempaper)
            else:
                renpy.sound.play(audio.itemdefault)

        def use(self, player):
            if self.checkAvailable(player) != True:
                Notice.add(self.checkAvailable(player))
            else:
                self.sound()
                Stat.record(player, type(self))
                Notice.add(_('已使用物品：')+ self.name)
                if self.maxCd>0:
                    player.itemcd[type(self)] = self.maxCd 
                if self.du > 0 and self.kind == '工具':
                    self.du -= 1
                    if self.du == 0:
                        Notice.add(self.name + _('已损坏！'))
                        self.broken = True
                        self.timeUpAction(player)
                        self.disableAction(player)
                
                if Satiety.has(player) and self.kind == '食物':
                    player.severity += r2(0.02 * Satiety.getstack(player))
                    Notice.add(_('由于饱腹，严重程度提升了%s点！') % (2* Satiety.getstack(player)))

                self.useItemAction(player)
                if (GameDifficulty4.has(player) or GameDifficulty5.has(player)) and self.kind == '食物' and not Stomachache_.has(player) and rra(player, 5):
                    Stomachache.add(player)
                
                if not self.reuse:
                    self.sub(player)
                routine_music(player)
            Notice.show()

        def quit(self, player, times=1):
            if times == 0:
                return
            Notice.add(_('已丢弃')+ str(times) +_('个物品：')+ self.name)
            Notice.show()
            self.sub(player, times)
            

        @classmethod
        def afterTaskAction(cls, player, task):  # 日程后
            pass

    def itemKindInfo(kind, mode):
        d = {
            _('实验药物i'):_('实验药物\n\n药效十分迅速，在吞下药物的瞬间即可止痛，但副作用巨大，而且价格时刻都在飙升……\n不过你只需要知道这东西能救你的命就可以。'),
            _('实验药物a'):_('\n为什么只有Pathos医生才有这样的药？话说这些药片里面的具体成分到底是什么，是从哪里来的，为什么一周后就不能吃了……'),
            _('普通药物i'):_('普通药物\n\n具有一定的效果，但总体上不如专用的实验药物，妥善使用也许会比实验药物更有帮助。即便副作用不高，但别忘了你只是个普通的人。'),
            _('普通药物a'):_('\n不吃安眠药就睡不好觉，这日子什么时候能到头？'),
            _('书籍i'):_('书籍\n\n在书店购买获得，阅读后可获得能够逆转局面的效果，但你不会短时间对同一本书燃起阅读欲望，请谨慎使用吧。'),
            _('书籍a'):_('\n为什么我不能天天都看，明明我想看？这种无形的束缚到底是怎么回事？'),
            _('手稿i'):_('手稿\n\n阅读部分书籍后获得，和书籍差别不大，但阅读不需要回合，在正确的情况下使用说不定有神奇的效果。'),
            _('手稿a'):_('\n喜欢我组合拳吗？'),
            _('专业类书籍i'):_('专业类书籍\n\n与书籍类似，但是阅读后会被消耗。'),
            _('专业类书籍a'):_('\n曾经以网课的形式存在。'),
            _('工具i'):_('工具\n\n可重复使用的道具，而且能带来不错的效果。更像是“速读状态下的书籍”。'),
            _('工具a'):_('\n有人说收藏品怎么可以使用呢？于是出现了这个分类。我只不过是关心你们，如果出的书越来越多，你们该读不过来了。'),
            _('食物i'):_('食物\n\n可以恢复较多精神状态，且有不同的效果。使用食物会获得饱腹，有饱腹效果还使用食物就会大幅降低本次恢复效果甚至变为扣除精神状态，频繁使用食物也会逐渐降低食物的恢复效果。'),
            _('食物a'):_('\n如果不点外卖的话，午休时间我就只能吃公司提供的免费工作餐了，倒不是多难吃，就是那东西只是被烹饪到仅仅是能吃的地步……'),
            _('收藏品i'):_('收藏品\n\n带有不同的效果，拥有则永久提升能力，某些特殊的收藏品还会影响游戏结局。'),
            _('收藏品a'):_('\n59……这个数字到底是什么？'),
            _('消耗品i'):_('消耗品\n\n使用后消耗的道具，不一定是放进嘴里吃的东西，但都差不多。'),
            _('消耗品a'):_('\n在没有这个分类之前，仙人掌肥料的分类是食物。'),
            _('文稿i'):_('文稿\n\n未完成的文稿可以在日程中完成，而已完成的文稿可以发布到网上增加人气，也可以交付委托来获得大量金钱。'),
            _('文稿a'):_('\n挖了坑我就不填，就是玩——'),
            _('酒类i'):_('酒类\n\n酒吧里使用的酒，如果你看到了这条信息，说明你用了全物品。'),
            _('酒类a'):_('\n是不是很卡啊？'),
        }
        return d[kind+mode]

    def quickUse(item, player):
        if item.has(player):
            item.get(p).use(p)

    def ui_itemUse(item, player):
        item.use(player)

    def ui_itemStar(item):
        item.star=True
        item.blocked = False

    def ui_itemUnstar(item):
        item.star=False

    def ui_itemBlock(item):
        item.star=False
        item.blocked = True

    def ui_itemUnblock(item):
        item.blocked=False

    def ui_itemQuit(item, player, nums=1):
        if item.canQuit or persistent.allowquitunique:
            item.quit(player, nums)
        else:
            showNotice([_('该物品不能被丢弃！')])

    def buy(player, item, nums=1, money=0):
        if player.money < money * nums:
            Notice.add(_('你的钱不够。'))
        else:
            player.money -= money * nums
            
            if nums == 1:
                Notice.add(_('购买成功！花费%s元购买了%s！') % (money * nums, item.name))
            else:
                Notice.add(_('购买成功！花费%s元购买了%s个%s！') % (money * nums, nums, item.name))
            item.add(player, nums)
        Notice.show()

    def buyAndUse(player, item, nums=1, money=0):
        if player.money < money * nums:
            Notice.add(_('你的钱不够。'))
            Notice.show()
        else:
            player.money -= money * nums
            if nums == 1:
                Notice.add(_('购买成功！花费%s元购买了%s！') % (money * nums, item.name))
            else:
                Notice.add(_('购买成功！花费%s元购买了%s个%s！') % (money * nums, nums, item.name))
            item.add(player, nums)
            item.get(player).use(player)
        
        







    class MedicineBase(Item):
        id = None
        name = None
        kind = _('实验药物')
        maxCd = 0
        maxDu = 8
        isUnique = False
        info = None
        reuse = False
        
        @property
        def e_(self):
            return DrugEA

        @classmethod
        def getMedicineEffects(cls, player):
            return int(cls.getMedicineScale(player, prev=True)* cls.getSpecEffects(player) * 100)

        @classmethod
        def getSpecEffects(cls, player):
            return 1.0

        @classmethod
        def getMedicineRationalUsePercent(cls, player):
            if GameDifficulty4.has(player):
                return 0.0
            elif GameDifficulty1.has(player) or GameDifficulty2.has(player):
                return r2((player.severity - (0.65 + 0.05 * player.week)) * 300)
            return r2((player.severity - (0.65 + 0.05 * player.week)) * 200)

        @classmethod
        def getlastuseinfo(cls, player):
            if cls in player.medinfo:
                return _('\n{color=#fde827}上次使用：%s（%s）\n过夜降低抗药性概率：%s%s\n过夜获得药物依赖概率：%s%s\n合理用药降低严重程度概率：%s%s{/color}\n\n') % (player.medinfo[cls].time(), player.medinfo[cls].lastuse, r2(player.medinfo[cls].updateResistenceChance(player)), '%', r2(player.averDD()), '%', cls.getMedicineRationalUsePercent(player), '%')
            return '\n'

        @classmethod
        def getBenefit(cls, player):
            ge = cls.getMedicineEffects(player)
            cl = '{color=#ffae00}'
            if ge < 67:
                cl = '{color=#FF4500}'
            if ge > 100:
                cl = '{color=#7CFC00}'
            return _('\n{font=DejaVuSans.ttf}• {/font}使用效率：%s%s%s{/color}') % (cl, ge, '%')

        @classmethod
        def getScale(cls, player, prev=True):
            scales = [1.0, 1.0, 1.0]
            rationaluse = True
            for i in player.medinfo:
                if i == cls:
                    if player.medinfo[i].getInterval(player) == 0:
                        scales[0] *= 0.33
                        if not prev:
                            player.medinfo[cls].res += min(player.medinfo[cls].res + ra(player, 3, 5), 80)
                            player.gain_abi(0.03, 'sev', due='连续服药')
                            rationaluse = False
                    if player.medinfo[i].getInterval(player) == 1:
                        scales[1] *= 0.66
                        if not prev:
                            player.medinfo[cls].res += min(player.medinfo[cls].res + ra(player, 1, 3), 80)
                            player.gain_abi(0.01, 'sev', due='连续服药')
                            rationaluse = False
                else:
                    if player.medinfo[i].getInterval(player) == 0:
                        scales[2] *= 0.5
                        if not prev:
                            player.medinfo[cls].res += min(player.medinfo[cls].res + ra(player, 1, 3), 80)
                            player.gain_abi(0.02, 'sev', due='连续服药')
                            rationaluse = False
            if not prev and rationaluse and not GameDifficulty4.has(player) and not GameDifficulty5.has(player):
                if rra(player, cls.getMedicineRationalUsePercent(player)):
                    player.gain_abi(-0.01, 'sev', stat="药物治疗")
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
            ge = cls.getMedicineEffects(player)
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
            extrainfo = ''
            s = cls.getMedicineEffects(player)
            scales = cls.getScale(player)
            
            if cls.res(player) != 0:
                extrainfo += _('—抗药性：-%s%s\n') % (int(cls.res(player)), '%') 

            if scales[0] != 1:
                extrainfo += _('{color=#FF4500}—刚刚使用过本实验药物：*%s%s\n{/color}') % (int(scales[0]*100), '%') 

            if scales[1] != 1:
                extrainfo += _('{color=#ffae00}—近期使用过本实验药物：*%s%s\n{/color}') % (int(scales[1]*100), '%')  

            if scales[2] != 1:
                extrainfo += _('{color=#ffae00}—刚刚使用过其他实验药物：*%s%s\n{/color}') % (int(scales[2]*100), '%') 

            if player.times == 0 and cls==MedicineA:
                extrainfo += _('{color=#fe6363}—早上服用：*%s%s{/color}\n') % (int(MedicineA.getSpecEffects(player)*100) ,'%') 

            if cls==MedicineB:
                extrainfo += _('{color=#7881e8}—该精神状态下服用：*%s%s{/color}\n') % (int(MedicineB.getSpecEffects(player)*100) ,'%') 

            if cls==MedicineC:
                extrainfo += _('{color=#e4f06f}—基础精神消耗加成效果：*%s%s{/color}\n') % (int(MedicineC.getSpecEffects(player)*100) ,'%') 

            if TransparentBottle.has(player):
                extrainfo += _('{color=#7CFC00}—透明药瓶：+20%\n{/color}') 

            if GameDifficulty5.has(player):
                extrainfo += _('{color=#7CFC00}—药物过敏：+20%\n{/color}') 

            return '\n'+info+extrainfo + cls.getlastuseinfo(player)

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

            if type(self) not in player.medinfo:  # 使用后将自身填进已经使用过的药物中
                player.medinfo[type(self)] = MedInfo(type(self))
            if DrugD.has(player):  # 移除对应的药物依赖
                DrugD.clearByType(player)
            if DrugW.has(player):  # 处理对应的戒断反应
                DrugW.get(player).afterDrug(player)

            if Despair.has(player):
                Despair.get(player).afterDrug(player)

            rec = self.recovery(player) * self.getMedicineScale(player)

            player.medinfo[type(self)].updateTime(player) # 更新药物使用时间

            player.gain_mental(r2(rec), '使用了%s'%self.name, stat=self.name)

            if self.res(player) > 50:
                player.gain_abi(0.02, 'sev', due='使用的药物抗药性过高')
            
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