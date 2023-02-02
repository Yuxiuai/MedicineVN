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
            elif self.maxCd==-1:
                if self.broken:
                    du_info = _('已损坏  ')
                elif self.du == 1:
                    du_info = _('即将损坏：明天  ')
                else:
                    du_info = _('即将损坏：')+str(self.du)+_('天后  ')
            else:
                if self.broken:
                    du_info = _('已变质  ')
                elif self.du == 1:
                    du_info = _('即将变质：明天  ')
                else:
                    du_info = _('即将变质：')+str(self.du)+_('天后  ')

            return _('数量：')+str(self.amounts)+ '\n' + cd_info + '\n'+du_info+ '\n'

        @classmethod
        def icon(cls):
            return 'gui/items/100.png'





        @classmethod
        def getPrincipalInfo(cls):
            type_info = _('\n\n') + cls.kind

            if cls.isUnique:
                if not cls.has(p):
                    uni_info = _('\n唯一\n\n{color=#fde827}未拥有{/color}')
                else:
                    uni_info = _('\n唯一')
            else:
                uni_info = ''

            return cls.info + type_info + uni_info

        def getSuffixInfo(self):
            return _('\n\n获取日期：第%s周的%s') % (self.gotWeek, weekdayFormat(self.gotDay))

        def timeUpdate(self, player):
            if self.du:
                if self.du > 0:
                    self.du -= 1
                if self.du == 0:
                    Notice.add(self.name + _('已过期！'))
                    self.broken = True
                    self.timeUpAction(player)
                    self.disableAction(player)
                    if self.kind == _('收藏品') and type(self) != GymTicket:
                        Trash.add(player)
                        player.items.remove(self)
                    
                
            

        @classmethod
        def has(cls, player):
            return cls in [type(i) for i in list(filter(lambda x: x.broken == False, player.items))]

        @classmethod
        def get(cls, player):  # 需要先用has检测
            return list(filter(lambda x: type(x) == cls and not x.broken, player.items))[0]

        @classmethod
        def getBrokenItemByType(cls, player):  # 需要先用has检测
            return list(filter(lambda x: type(x) == cls and x.broken, player.items))[0]
            
        @classmethod
        def hasByItem(cls, player, item):
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
            for i in range(times):
                cls.defaultAddItem(player)

        def remove(self, player):
            if not self.broken:
                self.disableAction(player)
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
                    Notice.add(_('已有%s，刷新了损坏期限！') % cls.name)
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
                return _('物品已过期！不可被使用！')
            if type(self) not in player.itemcd:
                return True
            else:
                return _('物品仍在冷却时间中！')

        def sound(self):
            if self.kind in (_('食物'), _('普通药物'), _('实验药物')):
                renpy.sound.play(audio.itemdrink)
            elif self.kind in (_('手稿'), _('书本')):
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
                self.useItemAction(player)
                if not self.reuse:
                    self.sub(player)
                if renpy.music.get_playing() == audio.enjoysuffering and player.mental > 20:
                    routine_music(player)
                if player.mental > 20:
                    blackmask(player)
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
            _('置顶i'):_('置顶道具\n\n你可以在物品的详细信息界面将物品置顶以方便使用。'),
            _('置顶a'):_('\n也算是某种意义上的物品日程表了……今天的矿泉水喝了吗？'),
            _('实验药物i'):_('实验药物\n\n药效十分迅速，在吞下药物的瞬间即可止痛，但副作用巨大，而且价格时刻都在飙升，也作为国内稀缺的药物，不过你只需要知道这东西能救你的命就可以。'),
            _('实验药物a'):_('\n为什么只有Pathos医生才有这样的药？话说这些药片里面的具体成分到底是什么，是从哪里来的，为什么一周后就不能吃了……'),
            _('普通药物i'):_('普通药物\n\n具有一定的效果，但总体上不如专用的实验药物，妥善使用也许会比实验药物更有帮助。即便副作用不高，但别忘了你只是个普通的人。'),
            _('普通药物a'):_('\n不吃安眠药就睡不好觉，这日子什么时候能到头？'),
            _('书本i'):_('书本\n\n在阿斯卡隆书店购买获得，阅读后可获得能够逆转局面的效果，但你不会短时间对同一本书燃起阅读欲望，请谨慎使用吧。'),
            _('书本a'):_('\n为什么我不能天天都看，明明我想看？这种无形的束缚到底是怎么回事？'),
            _('手稿i'):_('手稿\n\n阅读部分书本后获得，和书本差别不大，但阅读不需要回合，良好使用的话说不定有神奇的效果。'),
            _('手稿a'):_('\n喜欢我组合拳吗？'),
            _('工具i'):_('工具\n\n可重复使用的道具，而且能带来不错的效果。更像是“速读状态下的书籍”。'),
            _('工具a'):_('\n有人说收藏品怎么可以使用呢？于是出现了这个分类。我只不过是关心你们，如果出的书越来越多，你们该读不过来了。'),
            _('食物i'):_('食物\n\n可以恢复较多精神状态，且有不同的效果。使用食物会获得饱腹，有饱腹效果还使用食物就会大幅降低本次恢复效果甚至变为扣除精神状态，频繁使用食物也会逐渐降低食物的恢复效果。'),
            _('食物a'):_('\n如果不点外卖的话，午休时间我就只能吃公司提供的免费工作餐了，倒不是多难吃，就是那东西只是被烹饪到仅仅是能吃的地步……'),
            _('收藏品i'):_('收藏品\n\n带有不同的效果，拥有则永久提升能力，某些特殊的收藏品还会影响游戏结局。'),
            _('收藏品a'):_('\n59……这个数字到底是什么？'),
            _('文稿i'):_('文稿\n\n未完成的文稿可以在日程中完成，而已完成的文稿可以发布到网上增加人气，也可以交付委托来获得大量金钱。'),
            _('文稿a'):_('\n挖了坑我就不填，就是玩——')
        }
        return d[kind+mode]

    def quickUse(item, player):
        if item.has(player):
            item.get(p).use(p)

    def ui_itemUse(item, player):
        item.use(player)

    def ui_itemStar(item):
        item.star=True

    def ui_itemUnstar(item):
        item.star=False

    def ui_itemQuit(item, player):
        if item.canQuit:
            if item.broken:
                item.quit(player, item.amounts)
            else:
                item.quit(player, 1)
        else:
            showNotice([_('该物品不能被丢弃！')])

    def buy(player, item, nums=1, money=0):
        if player.money < money * nums:
            Notice.add(_('你的钱不够。'))
        else:
            player.money -= money * nums
            Notice.add(_('购买成功！花费%s元购买了%s个%s！') % (money* nums, nums, item.name))
            item.add(player, nums)
        Notice.show()

    def buyAndUse(player, item, nums=1, money=0):
        if player.money < money * nums:
            Notice.add(_('你的钱不够。'))
            Notice.show()
        else:
            player.money -= money * nums
            Notice.add(_('购买成功！花费%s元购买了%s个%s！') % (money* nums, nums, item.name))
            item.add(player, nums)
            item.get(player).use(player)
        
        







