init python early:
    
    class Item:
        id = None
        name = None
        kind = None
        maxCd = 0  # -1 不可使用 0 没有使用cd
        maxDu = -1  # -1 不可损坏 0 已损坏
        isUnique = False  # 为True时，最大amount为1
        reuse = True
        info = None
        ad = None

        def __init__(self, player):
            self.amounts = 1
            self.du = type(self).maxDu
            self.broken = False
            self.star = False
            self.gotWeek = player.week
            self.gotDay = player.today

        def __eq__(self, other):
            if type(self) != type(other):
                return False
            if self.du != other.du:
                return False
            return True

        def getPrefixInfo(self, player):
            if not type(self).reuse:
                reuse_info = '使用后消耗  '
            else:
                reuse_info = ''
            if type(self).maxCd == -1 or self.du == 0 or type(self).maxCd == -1:
                cd_info = '不可使用  '
            elif type(self).__name__ not in player.itemcd:
                cd_info = '可使用  '
            else:
                cd_info = '可使用时间：'+str(player.itemcd[type(self).__name__])+'天后  '

            if type(self).maxDu == -1:
                du_info = ''
            elif type(self).maxCd==-1:

                if self.du == 0:
                    du_info = '已损坏  '
                else:
                    du_info = '即将损坏：'+str(self.du)+'天后  '
            else:
                if self.du == 0:
                    du_info = '已过期  '
                else:
                    du_info = '即将过期：'+str(self.du)+'天后  '

            return '数量：'+str(self.amounts)+ '\n' +reuse_info+ '\n'+ cd_info + '\n'+du_info
        
        @classmethod
        def getPrincipalInfo(cls):
            type_info = '\n\n' + cls.kind

            if cls.isUnique:
                if not cls.hasByType(p):
                    uni_info = '\n唯一\n\n{color=#ffff00}未拥有{/color}'
                else:
                    uni_info = '\n唯一'
            else:
                uni_info = ''

            return cls.info + type_info + uni_info

        def getSuffixInfo(self):
            return '\n\n获取日期：第%s周的%s' % (self.gotWeek, weekdayFormat(self.gotDay))

        def timeUpdate(self, player):
            if self.du is not None:
                if self.du > 0:
                    self.du -= 1
                    if self.du == 0:
                        Notice.add(type(self).name + '已过期！')
                        self.broken = True
                        self.timeUpAction(player)
                        self.disableAction(player)
                        if self.kind == '收藏品':
                            Trash.add(player)
                            player.items.remove(self)
            

        @classmethod
        def hasByType(cls, player):
            return cls in [type(i) for i in list(filter(lambda x: x.broken == False, player.items))]

        @classmethod
        def getByType(cls, player):  # 需要先用has检测
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
        def add(cls, player, times=1):  # 增加新效果或增加层数
            if times == 0:
                return
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
                if self.amounts == 0:
                    self.remove(player)
                    break

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

            if cls.isUnique and cls.hasByType(player):
                if cls.maxDu >0:
                    cls.getByType(player).du = cls.maxDu
                    Notice.add('已有%s，刷新了损坏期限！' % cls.name)
                else:
                    Notice.add('已有%s，无法再次获取！' % cls.name)
            elif not cls.hasByItem(player, newItem):  # 是否存在，如果不存在
                Notice.add('获得新物品：%s！' % cls.name)
                newItem.addStackAction(player)
                newItem.enableAction(player)
                player.items.append(newItem)
            else:
                #Notice.add('获得%s：%s！' % (cls.kind, cls.name))
                oldItem = cls.getByItem(player, newItem)
                oldItem.addStackAction(player)
                oldItem.amounts += 1
            sortArr(player.items)

        def useItemAction(self, player):
            pass

        def checkAvailable(self, player):
            if type(self).maxCd == -1:
                return '物品不可被使用！'
            if self.broken:
                return '物品已过期！不可被使用！'
            if type(self).__name__ not in player.itemcd:
                return True
            else:
                return '物品仍在冷却时间中！'


        def use(self, player):
            if self.checkAvailable(player) != True:
                Notice.add(self.checkAvailable(player))
            else:
                Notice.add('已使用物品：'+ type(self).name)
                if type(self).maxCd>0:
                    player.itemcd[type(self).__name__] = type(self).maxCd 
                self.useItemAction(player)
                if not type(self).reuse:
                    self.sub(player)
            Notice.show()

        def quit(self, player, times=1):
            if times == 0:
                return
            self.sub(player, times)
            Notice.add('已丢弃'+ str(times) +'个物品：'+ type(self).name)
            Notice.show()

        @classmethod
        def afterTaskAction(cls, player, task):  # 日程后
            pass

    def itemKindInfo(kind, mode):
        d = {
            '置顶i':'置顶道具\n\n你可以在物品的详细信息界面将物品置顶以方便使用。',
            '置顶a':'也算是某种意义上的物品日程表了……今天的矿泉水喝了吗？',
            '实验药物i':'实验药物\n\n药效十分迅速，在吞下药物的瞬间即可止痛，但副作用巨大，而且价格时刻都在飙升，也作为国内稀缺的药物，不过你只需要知道这东西能救你的命就可以。',
            '实验药物a':'为什么只有Pathos医生才有这样的药？话说这些药片里面的具体成分到底是什么，是从哪里来的，为什么一周后就不能吃了……',
            '普通药物i':'普通药物\n\n具有一定的效果，但总体上不如专用的实验药物，妥善使用也许会比实验药物更有帮助。即便副作用不高，但别忘了你只是个普通的人。',
            '普通药物a':'不吃安眠药就睡不好觉，这日子什么时候能到头？',
            '书本i':'书本\n\n在阿斯卡隆书店购买获得，阅读后可获得能够逆转局面的效果，但你不会短时间对同一本书燃起阅读欲望，请谨慎使用吧。',
            '书本a':'为什么我不能天天都看，明明我想看？这种无形的束缚到底是怎么回事？',
            '手稿i':'手稿\n\n阅读部分书本后获得，和书本差别不大，但阅读不需要回合，良好使用的话说不定有神奇的效果。',
            '手稿a':'喜欢我组合拳吗？',
            '食物i':'食物\n\n部分食物可以随时使用，但部分食物只能午餐时间使用，可以恢复较多精神状态且有不同的效果。',
            '食物a':'如果不点外卖的话，午休时间我就只能吃公司提供的免费工作餐了，倒不是多难吃，就是那东西只是被烹饪到仅仅是能吃的地步……',
            '收藏品i':'收藏品\n\n带有不同的效果，拥有则永久提升能力，某些特殊的收藏品还会影响游戏结局。',
            '收藏品a':'59……这个数字到底是什么？',
            '文稿i':'文稿\n\n未完成的文稿可以在日程中完成，而已完成的文稿可以发布到网上增加人气，也可以交付委托来获得大量金钱。',
            '文稿a':'挖了坑我就不填，就是玩——'
        }
        return d[kind+mode]

    def quickUse(item, player):
        if item.hasByType(player):
            item.getByType(p).use(p)

    def ui_itemUse(item, player):
        item.use(player)

    def ui_itemStar(item):
        item.star=True

    def ui_itemUnstar(item):
        item.star=False

    def ui_itemQuit(item, player):
        times = 1
        if item.broken == True:
            times = item.amounts
        item.quit(player, times)

    def buy(player, item, nums=1, money=0):
        if player.money < money * nums:
            Notice.add('你的钱不够。')
        else:
            player.money -= money * nums
            Notice.add('购买成功！花费%s元购买了%s个%s！' % (money* nums, nums, item.name))
            item.add(player, nums)
        Notice.show()

    def buyAndUse(player, item, nums=1, money=0):
        if player.money < money * nums:
            Notice.add('你的钱不够。')
            Notice.show()
        else:
            player.money -= money * nums
            Notice.add('购买成功！花费%s元购买了%s个%s！' % (money* nums, nums, item.name))
            item.add(player, nums)
            item.getByType(player).use(player)
        
        







