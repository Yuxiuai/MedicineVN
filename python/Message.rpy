init python early:

    ret_mes = { # 空字符串代表已读
        'Pathos': {
            '。*': ['', '', '', _('别叫')],
        },
        'Halluke': {
            '做什么': ['刚刚打了个瞌睡……抱歉没及时回你。','刚才在看书。','刚刚在上课。','在写作业，有什么事吗？','只是躺在床上而已……','就只是在刷手机','没做什么……','在打羽毛球，你要来玩吗？'],
            '干什么': ['刚刚打了个瞌睡……抱歉没及时回你。','刚才在看书。','刚刚在上课。','在写作业，有什么事吗？','只是躺在床上而已……','就只是在刷手机','没做什么……','在打羽毛球，你要来玩吗？'],
            '在吗': ['在的啊，什么事？', '在的，有什么事？','啊……没看到你的消息，有什么事！'],
            '喜欢你': ['真的？今天又不是愚人节，就别逗我了……','你这家伙……不会和所有人都这么说吧？','是嘛……谢啦……','唉？别开这种玩笑啊……','不许再逗我了。','瞎说什么呢……','喂，这种话不要乱说！','……'],
            '喜欢我': ['真的？今天又不是愚人节，就别逗我了……','你这家伙……不会和所有人都这么说吧？','是嘛……谢啦……','唉？别开这种玩笑啊……','不许再逗我了。','瞎说什么呢……','喂，这种话不要乱说！','……'],
            '爱你': ['真的？今天又不是愚人节，就别逗我了……','你这家伙……不会和所有人都这么说吧？','是嘛……谢啦……','唉？别开这种玩笑啊……','不许再逗我了。','瞎说什么呢……','喂，这种话不要乱说！','……'],
            '约会': ['又在开玩笑，吃饭的话可以哦。','约什么会啊，瞎说话……','你这家伙……不会和所有人都这么说吧？','真的？今天又不是愚人节，就别逗我了……','是嘛……谢啦……','唉？别开这种玩笑啊……','不许再逗我了。','瞎说什么呢……','喂，这种话不要乱说！','……'],
            '恋爱': ['你这家伙……不会和所有人都这么说吧？','真的？今天又不是愚人节，就别逗我了……','唉？别开这种玩笑啊……','不许再逗我了。','瞎说什么呢……','喂，这种话不要乱说！','……'],
            '亲': ['你这家伙……不会和所有人都这么说吧？','真的？今天又不是愚人节，就别逗我了……','唉？别开这种玩笑啊……','不许再逗我了。','瞎说什么呢……','喂，这种话不要乱说！','……'],
            '摸': ['你这家伙……不会和所有人都这么说吧？','真的？今天又不是愚人节，就别逗我了……','唉？别开这种玩笑啊……','不许再逗我了。','瞎说什么呢……','喂，这种话不要乱说！','……'],
            '抱': ['你这家伙……不会和所有人都这么说吧？','真的？今天又不是愚人节，就别逗我了……','唉？别开这种玩笑啊……','不许再逗我了。','瞎说什么呢……','喂，这种话不要乱说！','……'],
            '喜欢吃什么': ['喜欢吃巧克力吧？大概。','没什么特别喜欢的，非要说就是巧克力吧，不过吃了会变胖。','甜的东西……巧克力之类的。'],
            '最近如何': ['感觉还好……学习上稍微有点难度……','之前打羽毛球的时候动作太大，拉伤了……最近在休息……','最近还好吧，没发生什么特别的……','最近还行？','也就那样。','不好不坏吧……','还好……','最近没怎么……','前段时间发现了一家奶茶店，那家店还挺好喝的……','最近天天在打游戏……','最近还行，你呢？','最近感觉出汗很多，可能是身体在逐渐变强大起来呢！','昨天去公园溜达了一会，居然丢了100块！幸好我还有生活费！','最近去看了电影，不过感觉没什么意思……'],
            '最近怎么样': ['感觉还好……学习上稍微有点难度……','之前打羽毛球的时候动作太大，拉伤了……最近在休息……','最近还好吧，没发生什么特别的……','最近还行？','也就那样。','不好不坏吧……','还好……','最近没怎么……','前段时间发现了一家奶茶店，那家店还挺好喝的……','最近天天在打游戏……','最近还行，你呢？','最近感觉出汗很多，可能是身体在逐渐变强大起来呢！','昨天去公园溜达了一会，居然丢了100块！幸好我还有生活费！','最近去看了电影，不过感觉没什么意思……'],
            '回复': ['稍微有点忙……','忘记看信息了……抱歉……','刚刚睡着了……','刚刚在上课……'],
            '羽毛球': ['要和我打羽毛球吗？好啊，周末来玩吧！','那这周末来我们学校打吧？','最近有点懒得打，不过周末你陪我打我就来。','要和我打羽毛球的话得到周末打，平时还挺忙的。'],
            '知道了':['好诶。', '嗯嗯', '好', '好的'],
            '好':['好诶。', '嗯嗯', '好', '好的'],
            '。*': ['……','嗯？','啥？','什么……','有什么事吗？', '怎么了……', '什么事？'],
        },
        
        'Acolas': {
            '做什么': ['稍微有点忙，等会回你。','在研究一个蛮有趣的算法。','在看C++最近又更新了什么没用的新东西。','反正就是在工作。','在喝咖啡。','在咖啡营地吃东西。','在散步。','在锻炼。'],
            '干什么': ['稍微有点忙，等会回你。','在研究一个蛮有趣的算法。','在看C++最近又更新了什么没用的新东西。','反正就是在工作。','在喝咖啡。','在咖啡营地吃东西。','在散步。','在锻炼。'],
            '在吗': ['在。', '你直接说找我干什么就行。','',''],
            '喜欢你': ['当然。','怎么突然问这个？','又想让我请你吃东西了？','说吧，想要我帮你干什么？','工作进度做不完了么？','','',''],
            '喜欢我': ['当然。','怎么突然问这个？','又想让我请你吃东西了？','说吧，想要我帮你干什么？','工作进度做不完了么？','','',''],
            '爱你': ['当然。','怎么突然问这个？','又想让我请你吃东西了？','说吧，想要我帮你干什么？','工作进度做不完了么？','','',''],
            '约会': ['行啊，周五你开完会，我们再聊聊这周干什么去。','周五别忘了来开会，别提前走了我找都找不着你。','下周带你去再吃一次咖啡营地吧。','你想吃火锅了？','知道了，你想来我家里约会？','怪忙的捏。','最近有点忙，以后再说。'],
            '恋爱': ['当然。','怎么突然问这个？','又想让我请你吃东西了？','说吧，想要我帮你干什么？','工作进度做不完了么？','','',''],
            '亲': ['当然。','怎么突然问这个？','又想让我请你吃东西了？','说吧，想要我帮你干什么？','工作进度做不完了么？','','',''],
            '摸': ['当然。','怎么突然问这个？','又想让我请你吃东西了？','说吧，想要我帮你干什么？','工作进度做不完了么？','','',''],
            '抱': ['当然。','怎么突然问这个？','又想让我请你吃东西了？','说吧，想要我帮你干什么？','工作进度做不完了么？','','',''],
            '喜欢吃什么': ['没什么特别喜欢吃的，说实话，大多数东西都是又贵又不好吃。','喜欢吃肉，是不是有点太广泛了？','只能说我没什么忌口。'],
            '最近如何': ['最近工作还比较顺利，新算法也挺容易理解的。','不如关心一下你自己的工作进度吧。','应该是我问你吧，你这家伙天天偷懒，能完成每周的任务吗？','也就那样。','一般般。','还行。'],
            '最近怎么样': ['最近工作还比较顺利，新算法也挺容易理解的。','不如关心一下你自己的工作进度吧。','应该是我问你吧，你这家伙天天偷懒，能完成每周的任务吗？','也就那样。','一般般。','还行。'],
            '回复': ['我又不像你一样，天天有那么多闲工夫。','没时间看手机。','懒得回。','因为我在忙。'],
            '项目': ['稍微还有点瑕疵，不指望你能帮我修好，不用你担心其实。','我自己来就行。','还行。','没什么问题。'],
            '游戏': ['稍微还有点瑕疵，不指望你能帮我修好，不用你担心其实。','我自己来就行。','还行。','没什么问题。'],
            '知道了':['嗯。'],
            '好':['嗯。'],
            '。*': ['……', '有事情就打电话问我吧。', '嗯？', '听不懂你在说什么。'],
        },
        
        #'Halluke': ['', '……', _('嗯。')],
        'Depline': {
            
        },

        'Destot': {
            '做什么': ['在研究你之前发给我的文档','在看网课','在看书','在工作哦，我可没偷懒','在吃零食，你也要吃点吗？','在……摸鱼','在看手机'],
            '干什么': ['在研究你之前发给我的文档','在看网课','在看书','在工作哦，我可没偷懒','在吃零食，你也要吃点吗？','在……摸鱼','在看手机'],
            '在吗': ['啥事！', '在的，要找我吗','在啊，有什么事又要让我做','1'],
            '喜欢你': ['诶？','我也喜欢前辈哦','诶嘿嘿','其实我……不对，前辈是和开玩笑呢吧？','又在逗我，我要生气了'],
            '喜欢我': ['有点……','呃呃不说这个，还有什么要我做的工作吗','！不要乱说','羞死人了真的别说这些'],
            '爱你': ['诶？','我也喜欢前辈哦','诶嘿嘿','其实我……不对，前辈是和开玩笑呢吧？','又在逗我，我要生气了'],
            '约会': ['想吃点什么呢','又想吃自助了？','想吃什么','想吃什么就尽管和我说吧！'],
            '恋爱': ['诶？','我也喜欢前辈哦','诶嘿嘿','其实我……不对，前辈是和开玩笑呢吧？','又在逗我，我要生气了'],
            '亲': ['诶？','我也喜欢前辈哦','诶嘿嘿','其实我……不对，前辈是和开玩笑呢吧？','又在逗我，我要生气了'],
            '摸': ['诶？','我也喜欢前辈哦','诶嘿嘿','其实我……不对，前辈是和开玩笑呢吧？','又在逗我，我要生气了'],
            '抱': ['诶？','我也喜欢前辈哦','诶嘿嘿','其实我……不对，前辈是和开玩笑呢吧？','又在逗我，我要生气了'],
            '喜欢吃什么': ['别看我是小兔子，我也是会吃点肉的，不过还是喜欢吃菜。','生菜？胡萝卜？我觉得都挺好吃的','喜欢吃麻辣烫吧，放很多蔬菜那种，要一起吃吗？'],
            '最近如何': ['还好，就是家里人总问我工作能赚多少钱，前辈工资肯定很高吧？哦！我好像不能问这些……','其实还好，最近工作也不太忙……','挺好的，有前辈你帮我，现在我能写很多新东西了','还好啦，前辈怎么样呢'],
            '最近怎么样': ['还好，就是家里人总问我工作能赚多少钱，前辈工资肯定很高吧？哦！我好像不能问这些……','其实还好，最近工作也不太忙……','挺好的，有前辈你帮我，现在我能写很多新东西了','还好啦，前辈怎么样呢'],
            '回复': ['刚刚睡着了！抱歉！需要我做什么吗！','写入迷了没看手机……','啊……忘记回了……有什么事嘛','啊啊我有点忙，有什么事！'],
            '知道了':['那我就先去干活了！'],
            '好':['那我就先去干活了！'],
            '谢':['谢什么！我应该的呀！','前辈教我那么多东西，我当然要回报前辈，这点小钱不算什么的！','不用谢不用谢，前辈吃得好我就开心！','没事没事，以后还需要你教我更多东西呢！'],
            '恭喜':['嘿嘿嘿……还不是前辈教导有方嘛！','没有前辈我是不能过审核的，感谢前辈！','诶嘿嘿……毕业之后就能和前辈一起工作了……'],
            '。*': ['这样啊', '原来如此', '好！', '可以！'],
        },
    }

    ret_mes_randomkeyword = {
        'Halluke': ['在吗？','刚刚在做什么呢？','刚刚去干什么了？','在干什么呢？','平时喜欢吃什么？','我喜欢你','亲一下','来抱抱','摸摸你','来打羽毛球吗？','最近如何？','最近怎么样？','怎么才回复我？','最近怎么样？','来约会吗！'],
        'Acolas': ['在吗？','刚刚在做什么呢？','刚刚去干什么了？','在干什么呢？','平时喜欢吃什么？','我喜欢你','亲一下','来抱抱','摸摸你','你的游戏项目如何了？','最近如何？','最近怎么样？','怎么才回复我？','最近怎么样？','来约会吗！'],
        'Destot': ['在吗？','刚刚在做什么呢？','刚刚去干什么了？','在干什么呢？','平时喜欢吃什么？','我喜欢你','亲一下','来抱抱','摸摸你','最近如何？','最近怎么样？','怎么才回复我？','最近怎么样？','来约会吗！','谢谢你的食物……','恭喜你签下协议！'],
    }




















    ret_mes_halluke_mad = {
        '1':['早啊！！', '早上好啊啵啵啵！', '呜呜呜好困不想起床', '早上好早上好', '早早早', '早上好呀', '早！！',
            '现在才觉得一个人睡觉真的好孤独', '要是能和你同居就好了……',
            '昨晚想你想到掉眼泪了……', '昨晚上做梦梦见你了……', '不想起……'],
        '2':['今天中午吃点什么，拍来看看', '中午没什么好吃的好想你', '中午了好想你', 
            '早上的课好无聊……一直想你', '下午做点什么？唔果然还是找你聊天吧', '真想现在就去找你玩', '想你想你想你想你想你想你想你想你想你'],
        '3':['终于能休息一会了', '晚饭吃点啥', '想你……', '一会来打个球不', '想和你多玩一会嘛', '好想你……上课太无聊', '想翘课和你出去开房……'],
        '4':['晚安哦啵啵啵', '晚上有好好吃夜宵吗', '今天也是爱你的一天！', '你说我活着还有什么意义吗……果然还是因为有你', 
            '我们什么时候能睡一张床上……', '我好像还没来过你家……', '想你想得睡不着！好兴奋！'],
        'random':['啵啵啵啵啵啵啵啵', '啵啵啵啵', '啵啵', '亲亲', '亲亲亲亲', '亲亲亲亲亲亲', '亲亲亲亲亲亲亲亲亲亲', 
            '想你想你好想你', '想你……', '好喜欢你……', '好爱你……', '想和你永远在一起', '怎么不回消息……', '为什么不理我……', 
            '在干嘛', '在干嘛在干嘛', '在干什么呢', '又不搭理我', '心好累', '永远爱你！', '随便吧', '呵呵……', '哎呀……一有点什么就好想和你说点……', '不知道说点什么，来烦你好了！你不会真觉得我烦人吧！', 
            '好无聊陪我玩', '陪我玩陪我玩陪我玩', '陪陪我嘛！', '快陪我嘛！', '回个话好不好！！', '回个话！！', '快回话！！', '人呢！！', '死哪去了！！'],
        'upset':['我又做错了什么吗？为什么不回我……', '好痛苦……', '难过……', '反正你其实也不喜欢我吧？', 
            '如果从我家窗户跳下去是不是就解脱了', '哈哈哈……其实你根本就不喜欢我吧？', '好空虚好寂寞啊……', '想哭', '为什么……为什么这么对我', '你就是想让我死对吧？', '好难过……', '再不回我消息我真的会疯掉……', '为什么不回我信息……'],
        


    }

    class Message:

        def __init__(self, what, mon, day, fro, to, h, m, seen=False):
            self.what = what
            self.mon = mon
            self.day = day
            self.fro = fro
            self.to = to
            self.h = h
            self.m = m
            self.seen = seen

        def __eq__(self, other):
            if self.what != other.what:
                return False
            if self.fro != other.fro:
                return False
            if self.to != other.to:
                return False
            return True

        @classmethod
        def codereply(cls, player, what):
            player.cheat = True
            st = player.st()
            cls.new(player, 'Pathos', 'Pathos', what, h=st[0], m=st[1],seen=True, chachong=False)

        @classmethod
        def new(cls, player, fro, to, what, h=None, m=None, seen=False, pos='b', chachong=True):
            
            if player.cured != -1 or player.finalStageDays != -1:
                return
            if what!='':
                if to == 'Halluke' and player.hal_p == 11 and player.today == 6 and player.times == 10 and seen==False:
                    seen = None
                    renpy.music.stop()
                if to == 'Halluke' and player.hal_p in (98, 99):
                    seen = None
                elif to == 'Destot' and player.des_p == 99:
                    seen = None
                elif to == 'Depline' and player.dep_0 == 8:
                    senn = None
                if m and h:
                    pos = ''
                st = player.st()
                if h == None:
                    h = st[0]
                if m == None:
                    m = st[1]
                if pos == 'b':
                    randomtime = cls.randomtime(player, cls.now(player, h, m))
                    h = str(int(randomtime/60))
                    m = str(randomtime - int(h)*60)
                elif pos == 'a':
                    m = rd(int(m), 59)
                m = str(m)
                h = str(h)
                
                mes = cls(what, player.mon, player.day, fro, to, h, m, seen)
                if cls.now(player) < cls.now(player, mes.h, mes.m):
                    mes.day -= 1
                
                if len(mes.m)<2:
                    mes.m='0' + mes.m
                if len(mes.h)<2:
                    mes.h='0' + mes.h

                if persistent.replymessagesquickly:
                    mes.h = player.st()[0]
                    mes.m = player.st()[1]
                    
                if mes in player.messages[to]:
                    if chachong:
                        pass
                    else:
                        player.messages[to].append(mes)
                else:
                    player.messages[to].append(mes)
                
                if fro == to:
                    Notice.add('%s发来了一条消息！' % to)
                
                if mes.what == 'nrZQqj1LfuDq' and to == 'Pathos' and fro != to:
                    if not persistent.sponsor:
                        persistent.sponsor = True
                        cls.codereply(player, '指令正确。')
                        cls.codereply(player, 'NO7140狮型机器人为您服务。')
                    else:
                        cls.codereply(player, '我的主人，随时为您服务。')
                        
                    cls.codereply(player, '您可以输入/help来获取我的功能。')
                    cls.codereply(player, '除此之外，我还为您安装了一个神秘应用，可以刷取道具和状态。')
                    cls.codereply(player, '而且菜单还获得了一个新的分页，内含一些其他的设置。')

                    
                if mes.what[0] == '/' and to == 'Pathos' and persistent.sponsor:
                    if mes.what[:5] == '/help':
                        if mes.what == '/help':
                            cls.codereply(player, '这里是赞助者专用指令界面，具体使用方法为两种：\n1、输入【/数值名】以查询该数值。\n2、输入【/数值名 数值】可以修改该数值，例如输入【/mental 100】可以将你的精神状态设置为100.0。\n输入时需需要保证类型相同，比如你不能将你的精神状态设置为“abc”。\n修改数值前建议先查询一下原数值的格式，比如修改专注度时，+30%专注度实际上是30，而修改精神状态消耗率时，+30%实际上是1.3。\n当属性值为True或是False时，只能修改成这两个的其中一个，可以认为是开启或是关闭，比如将属性名s4修改成True，系统会认为你已经在这个存档中解锁了个人剧情1。\n如果属性值为None，则我们无法判定这里填什么样的数据是合法的，所以不能在这里修改。\n关于数值名都有什么，可以再次输入【/help】，再接空格和数字1~8之间的数，例如【/help 1】。\n不建议修改帮助界面列出的之外的属性，可能会导致游戏崩溃。因修改数据导致的游戏崩溃，存档错误等结果概不负责。')
                        elif mes.what == '/help 1':
                            cls.codereply(player, '玩家数据部分：\n【name】代表你的名字，修改会导致聊天记录错误。\n【seed】种子，修改后可使本日随机事件出现变化。\n【safe】辅助种子，修改后可使本日随机事件出现变化。')
                        elif mes.what == '/help 2':
                            cls.codereply(player, '基础数值部分：\n【mental】精神状态。\n【severity】严重程度。\n【working】工作能力。\n【physical】身体素质。\n【writing】写作能力。\n【money】所持金钱。\n【price】药物价格。\n【priceIncrease】药价涨幅。\n【wages】本周工资。\n【goal】总工作目标。\n【achievedGoal】已完成的工作。\n【popularity】平台人气。')
                        elif mes.what == '/help 3':
                            cls.codereply(player, '时间部分：\n【mon】月。\n【day】日。\n【week】周数。\n【today】星期。\n【times】时间段，如果不了解时间段具体如何工作请不要修改。\n【spec_hour】表面小时，可以以此修改表面上的时间。\n【spec_min】表面分钟，可以以此修改表面上的时间。\n【onVacation】判断是否在放假，不建议修改，可能导致日程混乱。\n【onOutside】判断是否在外面，不建议修改，可能导致日程混乱。')
                        elif mes.what == '/help 4':
                            cls.codereply(player, '剧情部分：\n【hal_p】Halluke的剧情进度。\n【aco_p】Acolas的剧情进度。\n【sol_p】Pathos的剧情进度。\n【s4】【s5】【s6】【s7】【s8】【s9】分别对应1~7个人剧情，')
                        elif mes.what == '/help 5':
                            cls.codereply(player, '基础倍率部分：\n【basicConsumption】基础精神状态消耗。\n【basicRecovery】基础精神状态恢复。\n【basicConcentration】基础专注度。\n【workingGain】工作能力获取加成。\n【physicalGain】身体素质获取加成。\n【writingGain】写作技巧获取加成。\n【workingRegarded】工作能力倍率。\n【physicalRegarded】身体素质倍率。\n【writingRegarded】写作技巧倍率。\n【severityRegarded】严重程度倍率。\n【foodRecovery】食物恢复效果。\n【fooduse】降低的食物恢复率，每增加1点都代表降低了0.5%的基础食物恢复率。\n【drugRecovery】药物恢复效果。\n【deteriorateConsumption】睡眠消耗率。')
                        elif mes.what == '/help 6':
                            cls.codereply(player, '其他倍率部分：\n【sportConsumption】运动类日程消耗率。\n【sportRecovery】运动类日程恢复率。\n【sportConcentration】运动类日程专注度。\n【writeConsumption】写作类日程消耗率。\n【outdoorSportRecovery】外出运动恢复率。\n【writeRecovery】写作类日程恢复率。\n【writeConcentration】写作类日程专注度。\n【workConsumption】工作类日程消耗率。\n【workRecovery】工作类日程恢复率。\n【workConcentration】工作类日程专注度。\n【homeConsumption】家中日程消耗率。\n【homeConcentration】家中日程专注度。\n【sleepRecovery】睡觉类日程的恢复率，比如在床上休息和小睡。\n【writeValuable】写作价值率。\n【workSpeed】额外工作速度。\n【foodPrice】外卖价格率。')
                        elif mes.what == '/help 7':
                            cls.codereply(player, '日程限制部分：\n【canOutdoorSport】能否室外跑步，当大于-1时代表可以。\n【canWrite】能否完成委托，当大于-1时代表可以。\n【canRead】能否读小说，当大于-1时代表可以。\n【canSport】能否运动类，当大于-1时代表可以。\n【canExplore】能否外出，当大于-1时代表可以。')
                        elif mes.what == '/help 8':
                            cls.codereply(player, '其他：\n【hadAskedForMoney】是否和家里人要过钱。\n【hadAskedForLeave】是否请过假。\n【finalStageDays】在废墟下度过的天数。\n【aggra】随时间上升的严重程度倍率。\n【version】当前游戏版本。\n【playtime】该存档的游戏时长。\n【restart】该存档的读档次数。')

                        else:
                            cls.codereply(player, '输入有误。')


                    elif ' ' in mes.what:
                        cls.see(player, fro, to)
                        pos = mes.what.index(' ') + 1
                        after = mes.what[pos:]
                        attr = mes.what[1:pos-1]
                        if not hasattr(player, attr):
                            cls.codereply(player, '不存在名为%s的属性。' % attr)
                        elif callable(getattr(player, attr)):
                            cls.codereply(player, '禁止修改函数。')
                        elif type(getattr(player, attr)) in (None, list, dict, set):
                            cls.codereply(player, '禁止修改危险属性。')
                        else:
                            targettype = type(getattr(player, attr))
                            try:
                                finalattr = targettype(after)
                            except:
                                cls.codereply(player, '修改失败。\n可能是因为您试图将一个本该是数字的变量设置成字符。')
                            else:
                                before = getattr(player, attr)
                                setattr(player, attr, finalattr)
                                after = getattr(player, attr)
                                cls.codereply(player, '已修改。', )
                    else:

                        cls.see(player, fro, to)
                        attr = what[1:]
                        if not hasattr(player, attr):
                            cls.codereply(player, '不存在名为%s的属性。' % attr)
                        elif callable(getattr(player, attr)):
                            cls.codereply(player, '禁止修改函数及危险属性。')
                        elif type(getattr(player, attr)) in (None, list, dict, set):
                            cls.codereply(player, '禁止修改危险属性。')
                        else:
                            cls.codereply(player, str(getattr(player, attr)))

                    Notice.show()
                elif persistent.replymessagesquickly and fro == player.name:
                    cls.ret(player, to)
                    cls.see(player, fro, to)
                    cls.see(player, to, to)
                    Notice.show()
        @classmethod
        def messort(cls, player, to):
            if not player.messages[to]:
                return
            last = 0
            for i in range(len(player.messages[to])-1,-1,-1):
                if player.messages[to][i].fro != player.messages[to][i].to:
                    break
                last += 1

            if last <= 1:
                return
            
            l = p.messages[to][-i:]
            whats = [x.what for x in l]
            p.messages[to] = p.messages[to][:-i]
            l = sorted(l, key=lambda x: (int(x.mon), int(x.day), int(x.h), int(x.m)))

            for i in range(len(l)):
                l[i].what = whats[i]

            p.messages[to].extend(l)
            

        @classmethod
        def new_s(cls, player, fro, to, whats, h=None, m=None, seen=False, pos='b', chachong=True): #至少2条消息
            num_mes = len(whats)
            
            for what in whats:
                cls.new(player, fro, to, what, h, m, seen, pos, chachong)
            '''
            l = p.messages[to][-num_mes:]
            p.messages[to] = p.messages[to][:-num_mes]
            l = sorted(l, key=lambda x: (int(x.mon), int(x.day), int(x.h), int(x.m)))

            for i in range(len(l)):
                l[i].what = whats[i]

            p.messages[to].extend(l)
            '''

        @classmethod
        def now(self, player, h=None, m=None):
            if h == None:
                h = player.st()[0]
            if m == None:
                m = player.st()[1]
            return int(h)*60 + int(m)
        
        @classmethod
        def randomtime(cls, player, timestamp):
            timestamps = (470, 720, 1020, 1260, 1439)
            if 0 <= timestamp < 720:
                if rra(player, 50):
                    return ra(player, 1320, 1439)
                else:
                    return ra(player, 0, 470)
            elif 720 <= timestamp < 1020:
                return ra(player, 470, 720)
            elif 1020 <= timestamp < 1260:
                return ra(player, 720, 1020)
            elif 1260 <= timestamp < 1439:
                return ra(player, 1050, 1260)

        @property
        def info(self):
            if self.seen == True:
                seeninfo = _('已读')
            elif self.seen == False:
                seeninfo = _('未读')
            else:
                seeninfo = _('{color=#ff0000}发送失败{/color}')

            return _('%s月%s日 %s:%s %s') % (self.mon, self.day, self.h, self.m, seeninfo)

        @classmethod
        def clear(cls, to):
            player.messages[to] = []

        @classmethod
        def see(cls, player, fro ,to):
            for i in player.messages[to]:
                if i.seen == False and i.fro == fro:
                    if to == 'Halluke' != fro and player.hal_p in (98, 99):
                        pass
                    elif to == 'Acolas' != fro and player.aco_p in (98, 99):
                        pass
                    
                    else:
                        i.seen = True

        @classmethod
        def hasMes(cls, player, to, mes):
            for i in player.messages[to]:
                if mes in i.what:
                    return True
            return False

        @classmethod
        def hasNew(cls, player, to): # 是否单个人有新消息
            return False in [i.seen for i in list(filter(lambda x: x.fro != player.name, player.messages[to]))]
        
        @classmethod
        def hasNewMes(cls, player): # 是否所有人有新消息
            if player.cured != -1 or player.finalStageDays != -1:
                return False
            return True in [cls.hasNew(player, i) for i in player.messages]

        @classmethod
        def allret(cls, player):
            for i in player.messages:
                if False in [mes.seen for mes in list(filter(lambda x: x.fro == player.name, player.messages[i]))]:
                    cls.ret(player, i)

        @classmethod
        def ret(cls, player, who):
            cls.see(player, player.name, who)


            if who == 'Halluke' and player.hal_p in (12, 13, 98, 99):
                return
            
            elif who == 'Acolas' and player.aco_p in (98, 99):
                return

            elif who == 'Destot' and player.des_p == 99:
                return

            elif who == 'Depline' and player.dep_p < 3:
                return

            else:
                mes = ''
                lastmes = None
                for i in range(len(player.messages[who])-1,-1,-1):
                    if player.messages[who][i].fro != player.messages[who][i].to:
                        lastmes = player.messages[who][i].what
                        break
                if lastmes:

                    for i in ret_mes[who]:
                        if i in lastmes:
                            mes = rca(player, ret_mes[who][i])
                            break
                    if not mes:
                        mes = rca(player, ret_mes[who]['。*'])
                    if mes:
                        cls.new(player, who, who, mes, seen=False, chachong=False)



        