init python early:

    class Achievement:
        id = 0
        name = None
        icon = "gui/achievements/unknownAchievement.png"
        info = None

        @classmethod
        def achieve(cls):
            if cls not in persistent.achievements:
                import time
                Notice.add(['已达成成就：%s！' % cls.name] )
                persistent.achievements[cls] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

        @classmethod
        def done(cls):
            l = list(filter(lambda x: x in persistent.achievements, ALLACHIEVEMENTS))
            sortByID(l)
            return l
        
        @classmethod
        def undone(cls):
            l = list(filter(lambda x: x not in persistent.achievements, ALLACHIEVEMENTS))
            sortByID(l)
            return l

        @classmethod
        def time(cls):
            if cls not in persistent.achievements:
                return 0
            return persistent.achievements[cls]
        
        @classmethod
        def clear(cls):
            persistent.achievements = {}
        
        @classmethod
        def all(cls):
            for i in ALLACHIEVEMENTS:
                i.achieve()
                
        @classmethod
        def has(cls):
            return cls in persistent.achievements

        @classmethod
        def reachAnyEnd(cls, p):
            if p.route == 'a':
                Achievement501.achieve()
            if p.route == 'h':
                Achievement502.achieve()
            if GameDifficulty5.has(p):
                Achievement600.achieve()
            if GameModule1.has(p):
                Achievement601.achieve()
            if GameModule2.has(p):
                Achievement700.achieve()


    class Achievement100(Achievement):
        id = 100
        name = '我已经站在你世界的顶端了'
        icon = "gui/achievements/achievement100.png"
        info = '在医院的天台坠落。'


    class Achievement101(Achievement):
        id = 101
        name = '世间泰坦仅允我喘息'
        icon = "gui/achievements/achievement101.png"
        info = '死于精神状态过低。'


    class Achievement102(Achievement):
        id = 102
        name = '深陷其足下泥泞'
        icon = "gui/achievements/achievement102.png"
        info = '死于没有药物。'

    class Achievement103(Achievement):
        id = 103
        name = '肉与肉与肉与肉的豪华盛宴'
        icon = "gui/achievements/achievement103.png"
        info = '死于没有在地震前做好准备。'

    class Achievement104(Achievement):
        id = 104
        name = '不能重启的我们只能前进'
        icon = "gui/achievements/achievement104.png"
        info = '死于废墟之中。'

    class Achievement105(Achievement):
        id = 105
        name = '我们的神灵从未向这里看过一眼'
        icon = "gui/achievements/achievement105.png"
        info = '死于放弃治疗。'
    
    class Achievement106(Achievement):
        id = 106
        name = '对你来说我的一切是否都没有意义？'
        icon = "gui/achievements/achievement106.png"
        info = '成功使Halluke自杀。'
    
    class Achievement107(Achievement):
        id = 107
        name = '我想要的是你永远都不会赐予我的认同'
        icon = "gui/achievements/achievement107.png"
        info = '成功使Acolas死于过劳。'


    class Achievement200(Achievement):
        id = 200
        name = '我的意愿限制于桎梏之中'
        icon = "gui/achievements/achievement200.png"
        info = '触发主角的第1段特殊剧情。'

    class Achievement201(Achievement):
        id = 201
        name = '愉悦的人生交由你我主宰'
        icon = "gui/achievements/achievement201.png"
        info = '触发主角的第2段特殊剧情。'
    
    class Achievement202(Achievement):
        id = 202
        name = '为你读我写的青涩的诗韵'
        icon = "gui/achievements/achievement202.png"
        info = '触发主角的第3段特殊剧情。'

    class Achievement203(Achievement):
        id = 203
        name = '仿生人可以梦见电子羊吗'
        icon = "gui/achievements/achievement203.png"
        info = '触发主角的第4段特殊剧情。'

    class Achievement204(Achievement):
        id = 204
        name = '佯装自己不需要喜乐哀愁'
        icon = "gui/achievements/achievement204.png"
        info = '触发主角的第5段特殊剧情。'
    
    class Achievement205(Achievement):
        id = 205
        name = '你在饥肠辘辘地等着我吧'
        icon = "gui/achievements/achievement205.png"
        info = '触发主角的第6段特殊剧情。'



    class Achievement300(Achievement):
        id = 300
        name = '让我濒临涨破的心承受足够多的爱'
        icon = "gui/achievements/achievement300.png"
        info = '在一个存档中获取所有可攻略人物的特殊物品。'

    class Achievement301(Achievement):
        id = 301
        name = '轻轻地温柔地狂暴地亲吻我吧'
        icon = "gui/achievements/achievement301.png"
        info = '在一个存档中使所有可攻略人物死亡。'

    class Achievement302(Achievement):
        id = 302
        name = '这是个被伦理所支配的世界'
        icon = "gui/achievements/achievement302.png"
        info = '购买所有书店售卖的书籍。'
    
    class Achievement303(Achievement):
        id = 303
        name = '#0000FF'
        icon = "gui/achievements/achievement303.png"
        info = '阅读《不要读这本书》。'

    class Achievement304(Achievement):
        id = 601
        name = '也许我会试着尝试烂醉一场'
        icon = "gui/achievements/achievement304.png"
        info = '摄入过量的普通药物。'
    
    




    class Achievement400(Achievement):
        id = 400
        name = '为了能够让你学会如何去爱'
        icon = "gui/achievements/achievement400.png"
        info = '完成普通结局。'

    class Achievement401(Achievement):
        id = 401
        name = '如果能成为你就好了'
        icon = "gui/achievements/achievement401.png"
        info = '完成真实结局。'

    class Achievement402(Achievement):
        id = 402
        name = '我已经一无所有'
        icon = "gui/achievements/achievement402.png"
        info = '完成治愈结局。'
    
    
    class Achievement501(Achievement):
        id = 501
        name = '扯掉羽毛'
        icon = "gui/achievements/achievement501.png"
        info = '与Acolas完成除坏结局外任意结局。'

    class Achievement502(Achievement):
        id = 502
        name = '摔裂我的喙'
        icon = "gui/achievements/achievement502.png"
        info = '与Halluke完成除坏结局外任意结局。'

    '''
    class Achievement503(Achievement):
        id = 501
        name = '放飞嚎叫'
        icon = "gui/achievements/achievement503.png"
        info = '与Depline完成除坏结局外任意结局。'
    '''

    class Achievement504(Achievement):
        id = 502
        name = '踏入乌托邦的大门'
        icon = "gui/achievements/achievement504.png"
        info = '完成Acolas的隐藏剧情。'
    
    class Achievement505(Achievement):
        id = 502
        name = '这一切仿佛从未发生'
        icon = "gui/achievements/achievement505.png"
        info = '完成Halluke的隐藏剧情。'
    
    class Achievement600(Achievement): # 高难成就
        id = 600
        name = '我拒绝消亡'
        icon = "gui/achievements/achievement600.png"
        info = '以硬核难度完成除坏结局外任意结局。'
    
    class Achievement601(Achievement):
        id = 601
        name = '我才不是什么可悲的受害者'
        icon = "gui/achievements/achievement601.png"
        info = '开启挑战模式模组后完成除坏结局外任意结局。'

    class Achievement602(Achievement):
        id = 601
        name = '轻轻地温柔地狂暴地亲吻我吧'
        icon = "gui/achievements/achievement602.png"
        info = '在废墟下存活超过20天。'
    
    class Achievement603(Achievement):
        id = 601
        name = '试试看我们能够承受多少痛楚'
        icon = "gui/achievements/achievement603.png"
        info = '超过7天没有使用实验药物。'
    
    class Achievement700(Achievement): # 模组成就
        id = 601
        name = '六百一十七张笔记'
        icon = "gui/achievements/achievement700.png"
        info = '开启无尽之旅模组后完成除坏结局外任意结局。'

    class Achievement800(Achievement): # 模组成就
        id = 601
        name = '仿真肺叶'
        icon = "gui/achievements/achievement800.png"
        info = '找到作弊模式的开关。'

    #class Achievement602(Achievement):
    #    id = 602
    #    name = '我即是孤独，我即是完美'
    #    icon = "gui/achievements/achievement602.png"
    #    info = '完成除坏结局外任意结局，分数在150000以上。'