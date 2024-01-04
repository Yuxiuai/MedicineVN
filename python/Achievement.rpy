init python early:

    class Achievement:
        id = 0
        name = None
        hide = False
        icon = "gui/achievements/unknownAchievement.png"
        info = None
        textcolor = "#fde827"
        undisplayedAchs = []

        @classmethod
        def check(cls):
            deletedKeys = []
            for i in persistent.achievements.keys():
                if i.id >= 10000:
                    deletedKeys.append(i)
            for i in deletedKeys:
                del persistent.achievements[i]



        @classmethod
        def achieve(cls):
            if cls not in persistent.achievements:
                import time
                persistent.achievements[cls] = time.strftime(_('%Y.%m.%d %H:%M:%S'),time.localtime(time.time()))
                cls.undisplayedAchs.append(cls)
                cls._achieve()

        @classmethod
        def _achieve(cls):
            pass

        @classmethod
        def done(cls):
            l = list(filter(lambda x: x in persistent.achievements, ALLACHIEVEMENTS))
            sortByID(l)
            return l
        
        @classmethod
        def hdone(cls):
            l = list(filter(lambda x: x in persistent.achievements, ALLHIDEACHIEVEMENTS))
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
            ac = getSubclasses(Achievement)
            for i in ac:
                if i.id < 10000:
                    i.achieve()
            cls.show()
                
        @classmethod
        def has(cls):
            return cls in persistent.achievements

        @classmethod
        def show(cls):
            if renpy.get_screen("screen_achievement_notify"):
                renpy.hide_screen("screen_achievement_notify")
                renpy.show_screen("screen_achievement_notify", cls.undisplayedAchs)
            else:
                renpy.show_screen("screen_achievement_notify", cls.undisplayedAchs)
            if cls.undisplayedAchs:
                renpy.sound.play(audio.achieve,'audio')
            cls.undisplayedAchs = []

        @classmethod
        def reachAnyEnd(cls, p):
            
            if p.route == 'a':
                Achievement501.achieve()
                
            if p.route == 'h':
                Achievement502.achieve()
                
            if p.des_p not in (-1, 99) and p.experience != 'wri':
                Achievement552.achieve()
            if not GameDifficulty1.has(p):
                persistent.gametimes += 1



        @classmethod
        def pretreatment(cls, p):
            scoreP = dcp(p)

            for i in range(len(scoreP.effects) - 1, -1, -1):
                if scoreP.effects[i].kind != _('伤痕'):
                    scoreP.effects[i].clear(scoreP)
            for i in range(len(scoreP.items) - 1, -1, -1):
                scoreP.items[i].remove(scoreP)

            return scoreP



        @classmethod
        def calScore(cls, p):
            score = 0
            scoreP = cls.pretreatment(p)
            

            if p.experience == 'wri':
                score += scoreP.phy() * 1750
                score += scoreP.wri() * 1750
            else:
                score += scoreP.wor() * 1000
                score += scoreP.phy() * 1250
                score += scoreP.wri() * 1250
            score -= scoreP.sev() * 2000
            
            score += scoreP.popularity * 0.1
            score -= scoreP.fooduse * 10

            avares = 0
            for i in scoreP.medinfo:
                avares += scoreP.medinfo[i].res
            score -= avares * 10 / max(1, len(scoreP.medinfo))

            if GameDifficulty5.has(scoreP):
                score *= 2

            return int(score)
            

            #score /= max(1, scoreP.week)
            #score = int(score)

            #if scoreP.cheat:
            #    showNotice([_('因为这个存档使用过作弊功能，所以不计分数！')])
            #else:
            #    showNotice([_('获得分数：%s！') % score])
            #    persistent.highestscore = max(score, persistent.highestscore)



    class Achievement100(Achievement):
        id = 100
        name = _('我已经站在你世界的顶端了')
        icon = "gui/achievements/achievement100.png"
        info = _('在序章的医院天台坠落。')
        textcolor = "#FF4500"

    class Achievement100_1(Achievement):
        id = 100.1
        name = _('社会性死亡')
        icon = "gui/achievements/achievement100_1.png"
        info = _('在序章中社死。')
        textcolor = "#FF4500"
        
    class Achievement101(Achievement):
        id = 101
        name = _('在我品尝爱或咖啡的苦涩之前')
        icon = "gui/achievements/achievement101.png"
        info = _('死于精神状态过低。')
        textcolor = "#FF4500"


    class Achievement102(Achievement):
        id = 102
        name = _('用剪刀剪下连接着我的牵线')
        icon = "gui/achievements/achievement102.png"
        info = _('死于没有药物。')
        textcolor = "#FF4500"

    class Achievement103(Achievement):
        id = 103
        name = _('肉与肉与肉与肉的豪华盛宴')
        icon = "gui/achievements/achievement103.png"
        info = _('死于没有在地震前做好准备。')
        textcolor = "#FF4500"

    class Achievement104(Achievement):
        id = 104
        name = _('不能重启的我们只能前进')
        icon = "gui/achievements/achievement104.png"
        info = _('死于废墟之中。')
        textcolor = "#FF4500"

    class Achievement105(Achievement):
        id = 106
        name = _('我们的神灵从未向这里看过一眼')
        icon = "gui/achievements/achievement105.png"
        info = _('死于放弃治疗。')
        textcolor = "#FF4500"
    

    class Achievement106(Achievement):
        id = 105
        name = _('想象你依然存在')
        icon = "gui/achievements/achievement106.png"
        info = _('高难度下死于伤痕。')
        textcolor = "#FF4500"

    

    
    class Achievement150(Achievement):
        id = 150
        name = _('对你来说我的一切是否都没有意义？')
        icon = "gui/achievements/achievement150.png"
        info = _('成功使Halluke自杀。')
        hide = True
        textcolor = "#ff0000"

        @classmethod
        def _achieve(cls):
            persistent.unlocked_items.append(HallukeCookie)
            Notice.ladd(HallukeCookie)
    
    class Achievement151(Achievement):
        id = 151
        name = _('我想要的是你永远都不会赐予我的认同')
        icon = "gui/achievements/achievement151.png"
        info = _('成功使Acolas死于过劳。')
        hide = True
        textcolor = "#ff0000"

        @classmethod
        def _achieve(cls):
            persistent.unlocked_items.append(AcolasCookie)
            Notice.ladd(AcolasCookie)


    class Achievement200(Achievement):
        id = 200
        name = _('想象你仍然活着')
        icon = "gui/achievements/achievement200.png"
        info = _('触发主角的第1段特殊剧情。')
        textcolor = "#9500ff"

    class Achievement201(Achievement):
        id = 201
        name = _('愉悦的人生交由你我主宰')
        icon = "gui/achievements/achievement201.png"
        info = _('触发主角的第2段特殊剧情。')
        textcolor = "#9500ff"
    
    class Achievement202(Achievement):
        id = 202
        name = _('为你读我写的青涩幼稚的诗韵')
        icon = "gui/achievements/achievement202.png"
        info = _('触发主角的第3段特殊剧情。')
        textcolor = "#9500ff"

    class Achievement203(Achievement):
        id = 203
        name = _('仿生人会梦见电子羊吗')
        icon = "gui/achievements/achievement203.png"
        info = _('触发主角的第4段特殊剧情。')
        textcolor = "#9500ff"

    class Achievement204(Achievement):
        id = 204
        name = _('佯装自己不需要喜乐哀愁')
        icon = "gui/achievements/achievement204.png"
        info = _('触发主角的第5段特殊剧情。')
        textcolor = "#9500ff"
    
    class Achievement205(Achievement):
        id = 205
        name = _('你在饥肠辘辘地等着我吧')
        icon = "gui/achievements/achievement205.png"
        info = _('触发主角的第6段特殊剧情。')
        textcolor = "#9500ff"

    class Achievement206(Achievement):
        id = 206
        name = _('意淫无罪')
        icon = "gui/achievements/achievement206.png"
        info = _('触发主角的第7段特殊剧情。')
        textcolor = "#9500ff"
    
    class Achievement299(Achievement):
        id = 299
        name = _('0xCAFEBABE')
        icon = "gui/achievements/achievement299.png"
        info = _('触发Pathos的隐藏剧情。')
        hide = True
        textcolor = "#9500ff"



    class Achievement300(Achievement):
        id = 300
        name = _('让我濒临涨破的心承受足够多的爱')
        icon = "gui/achievements/achievement300.png"
        info = _('在一个存档中获取所有可攻略人物的特殊物品。')
        textcolor = "#ff00d4"

    class Achievement301(Achievement):
        id = 301
        name = _('轻轻地温柔地狂暴地亲吻我吧')
        icon = "gui/achievements/achievement301.png"
        info = _('在一个存档中使所有可攻略人物死亡。')
        hide = True
        textcolor = "#ff00d4"

    class Achievement302(Achievement):
        id = 302
        name = _('这是个被伦理所支配的世界')
        icon = "gui/achievements/achievement302.png"
        info = _('购买所有书店售卖的书籍。')
        textcolor = "#008cff"
    
    class Achievement303(Achievement):
        id = 303
        name = _('#0000FF')
        icon = "gui/achievements/achievement303.png"
        info = _('阅读《不要读这本书》。')
        textcolor = "#008cff"

    class Achievement304(Achievement):
        id = 304
        name = _('也许我会试着烂醉一场')
        icon = "gui/achievements/achievement304.png"
        info = _('在一天之内使用三种实验药物。')
        textcolor = "#9500ff"

    class Achievement305(Achievement):
        id = 305
        name = _('二手玫瑰')
        icon = "gui/achievements/achievement305.png"
        info = _('获得一支玫瑰。')
        hide = True
        textcolor = "#ff009d"
    
    class Achievement306(Achievement):
        id = 306
        name = _('光合作用')
        icon = "gui/achievements/achievement306.png"
        info = _('获得盛开的仙人掌盆栽。')
        textcolor = "#00ff00"

    class Achievement307(Achievement):
        id = 307
        name = _('摸鱼之王')
        icon = "gui/achievements/achievement307.png"
        info = _('在2048小游戏中合成出2048。')
        hide = True
        textcolor = "#c300ff"

    class Achievement308(Achievement):
        id = 308
        name = _('阿斯卡隆之海')
        icon = "gui/achievements/achievement308.png"
        info = _('浇水使仙人掌盆栽的湿润度达到1000以上。')
        hide = True
        textcolor = "#c300ff"

    class Achievement309(Achievement):
        id = 309
        name = _('这是……')
        icon = "gui/achievements/achievement309.png"
        info = _('听到不属于这个世界的音乐。')
        hide = True
        textcolor = "#ff0000"

    class Achievement310(Achievement):
        id = 310
        name = _('狂乱的鸡尾酒')
        icon = "gui/achievements/achievement310.png"
        info = _('获得50种不同的状态。')
        hide = True
        textcolor = "#9500ff"
    
    class Achievement311(Achievement):
        id = 311
        name = _('退款失败')
        icon = "gui/achievements/achievement311.png"
        info = _('游玩时长超过2小时。')
        textcolor = "#9500ff"

    class Achievement312(Achievement):
        id = 312
        name = _('腥味十足的生意')
        icon = "gui/achievements/achievement312.png"
        info = _('食用一条生鱼。')
        hide = True
        textcolor = "#659ff7"

    class Achievement313(Achievement):
        id = 313
        name = _('最伟大的成就')
        icon = "gui/achievements/achievement313.png"
        info = _('获得黑色狮子玩偶。')
        textcolor = "#516589"

    class Achievement314(Achievement):
        id = 314
        name = _('开始打胶！')
        icon = "gui/achievements/achievement314.png"
        info = _('欣赏知名男演员于秀爱的签名写真。')
        textcolor = "#ff94c6"
    
    class Achievement315(Achievement):
        id = 315
        name = _('不期而遇')
        icon = "gui/achievements/achievement315.png"
        info = _('在游泳馆偶遇某人。')
        textcolor = "#ff94c6"

    

    #class Achievement314(Achievement):
    #    id = 314
    #    name = _('我身已死')
    #    icon = "gui/achievements/achievement314.png"
    #    info = _('获得5层饥饿感。')
    #    textcolor = "#ff0000"
    #    hide = True

    


    class Achievement400(Achievement):
        id = 400
        name = _('为了能够让你学会如何去爱')
        icon = "gui/achievements/achievement400.png"
        info = _('完成普通结局。')
        textcolor = "#9500ff"

        @classmethod
        def _achieve(cls):
            persistent.unlocked_items.append('arnelpics')
            Notice.ladd('arnelpics')

    class Achievement401(Achievement):
        id = 401
        name = _('如果能成为你就好了')
        icon = "gui/achievements/achievement401.png"
        info = _('完成真实结局。')
        textcolor = "#50B097"

        @classmethod
        def _achieve(cls):
            persistent.unlocked_items.append(DecayCookie)
            Notice.ladd(DecayCookie)

    class Achievement402(Achievement):
        id = 402
        name = _('我已经一无所有')
        icon = "gui/achievements/achievement402.png"
        info = _('完成治愈结局。')
        textcolor = "#516589"

        @classmethod
        def _achieve(cls):
            persistent.unlocked_items.append(PathosCookie)
            Notice.ladd(PathosCookie)
            persistent.unlocked_items.append('pathospics')
            Notice.ladd('pathospics')

    class Achievement403(Achievement):
        id = 403
        name = _('我们活在一个没有生命的茧中')
        icon = "gui/achievements/achievement403.png"
        info = _('完成虚伪结局。')
        textcolor = "#ff0000"
    
    class Achievement404(Achievement):
        id = 404
        name = _('存在')
        icon = "gui/achievements/achievement404.png"
        info = _('完成孤独结局。')
        textcolor = "#9500ff"

        @classmethod
        def _achieve(cls):
            persistent.unlocked_items.append('solituspics')
            Notice.ladd('solituspics')

        
    class Achievement405(Achievement):
        id = 405
        name = _('融解')
        icon = "gui/achievements/achievement405.png"
        info = _('完成作家结局。')
        textcolor = "#9500ff"

    class Achievement450(Achievement):
        id = 450
        name = _('只有这次我在你的身侧微笑')
        icon = "gui/achievements/achievement450.png"
        info = _('完成Acolas的第一个游戏项目。')
        hide = True
        textcolor = "#9500ff"

    class Achievement451(Achievement):
        id = 451
        name = _('告诉我何时能让我们结束这一切')
        icon = "gui/achievements/achievement451.png"
        info = _('完成Acolas的三个项目。')
        textcolor = "#ff0000"
        hide = True

    class Achievement452(Achievement):
        id = 452
        name = _('我知道终有一天会如愿以偿')
        icon = "gui/achievements/achievement452.png"
        info = _('在与Halluke的恋爱期间让他保持情绪稳定。')
        hide = True
        textcolor = "#9500ff"
    
    
    class Achievement501(Achievement):
        id = 501
        name = _('扯掉羽毛')
        icon = "gui/achievements/achievement501.png"
        info = _('完成Acolas的剧情并达到结局。')
        textcolor = "#f92828"

        @classmethod
        def _achieve(cls):
            persistent.unlocked_items.append('acolaspics')
            Notice.ladd('acolaspics')

    class Achievement502(Achievement):
        id = 502
        name = _('摔裂尖喙')
        icon = "gui/achievements/achievement502.png"
        info = _('完成Halluke的剧情并达到结局。')
        textcolor = "#f5f2eb"

        @classmethod
        def _achieve(cls):
            persistent.unlocked_items.append('hallukepics')
            Notice.ladd('hallukepics')
    
    #class AchievementDeplineA(Achievement):
    #    #id = 502
    #    #name = _('放飞嘶嚎')
    #    #icon = "gui/achievements/achievementdeplinea.png"
    #    #info = _('完成Depline的A结局。')
    






    class Achievement504(Achievement):
        id = 504
        name = _('踏入乌托邦的大门')
        icon = "gui/achievements/achievement504.png"
        info = _('完成Acolas的隐藏剧情。')
        hide = True
        textcolor = "#ff0000"
    
    class Achievement505(Achievement):
        id = 505
        name = _('这一切仿佛从未发生')
        icon = "gui/achievements/achievement505.png"
        info = _('完成Halluke的隐藏剧情。')
        hide = True
        textcolor = "#ff0000"
    
    #class Achievement506(Achievement):
    #    #id = 506
    #    #name = _('')
    #    #icon = "gui/achievements/achievement506.png"
    #    #info = _('完成Depline的隐藏剧情。')


    class Achievement507(Achievement):
        id = 507
        name = _('入迷之梦')
        icon = "gui/achievements/achievement507.png"
        info = _('完成Acolas的宾馆隐藏剧情。')
        hide = True
        textcolor = "#ff94c6"

    class Achievement508(Achievement):
        id = 508
        name = _('安逸之梦')
        icon = "gui/achievements/achievement507.png"
        info = _('完成Halluke的宾馆隐藏剧情。')
        hide = True
        textcolor = "#ff94c6"



    class Achievement550(Achievement):
        id = 550
        name = _('无色而透明的我')
        icon = "gui/achievements/achievement550.png"
        info = _('完成Destot的全部人物剧情。')
        textcolor = "#33ffbe"

        @classmethod
        def _achieve(cls):
            persistent.unlocked_items.append('destotpics')
            Notice.ladd('destotpics')

    class Achievement551(Achievement):
        id = 551
        name = _('可靠的前辈')
        icon = "gui/achievements/achievement551.png"
        info = _('完成Destot的最后全部人物剧情时，Destot的能力值在100以上。')
        textcolor = "#9500ff"
        
    class Achievement552(Achievement):
        id = 552
        name = _('我最亲爱的朋友啊')
        icon = "gui/achievements/achievement552.png"
        info = _('在完成其他结局前Destot仍在实习。')
        hide = True
        textcolor = "#ff0000"
    
    
    class Achievement600(Achievement): # 高难成就
        id = 600
        name = _('我才不是什么可悲的受害者')
        icon = "gui/achievements/achievement600.png"
        info = _('以地狱难度完成游戏。')
        textcolor = "#ff0080"
    
    #class Achievement601(Achievement):
    #    id = 601
    #    name = _('我才不是什么可悲的受害者')
    #    icon = "gui/achievements/achievement601.png"
    #    info = _('开启挑战模式模组完成游戏。')
    #    textcolor = "#ff0080"

    class Achievement602(Achievement):
        id = 602
        name = _('一首赞歌摇篮曲')
        icon = "gui/achievements/achievement602.png"
        info = _('在废墟之下存活超过20天。')
        textcolor = "#ff0080"
    
    class Achievement603(Achievement):
        id = 603
        name = _('试试看我们能够承受多少痛楚')
        icon = "gui/achievements/achievement603.png"
        info = _('没有使用过实验药物完成游戏。')
        textcolor = "#ff0080"
    
    class Achievement604(Achievement):
        id = 604
        name = _('音乐鉴赏家')
        icon = "gui/achievements/achievement604.png"
        info = _('解锁全部音乐。')
        textcolor = "#ff0080"

    class Achievement800(Achievement):
        id = 10001
        name = _('已删除的成就')
        icon = "gui/achievements/unknownAchievement.png"
        info = _('该成就现已被删除。')
        hide = True
        textcolor = "#b9b9b9"

    class Achievement701(Achievement): # 模组成就
        id = 10002
        name = _('已删除的成就')
        icon = "gui/achievements/unknownAchievement.png"
        info = _('该成就现已被删除。')
        hide = True
        textcolor = "#b9b9b9"







transform screen_achievement_notify_appear(wait = 0):
    xoffset 100
    alpha 0.0 
    pause(wait)
    easein 0.2 xoffset -100 alpha 1.0
    linear 0.2 xoffset -40
    linear 0.05 xoffset -20
    linear 0.05 xoffset 10
    linear 0.1 xoffset 6  # 1
    pause(persistent.notifyDuration-1)
    easein 0.2 xoffset -50
    easein 0.2 xoffset 200 alpha 0
    #linear 0.1 xoffset 50
    #linear 0.15 xoffset 100
    #linear 0.05 xoffset -25
    #linear 0.05 xoffset 0



screen screen_achievement_notify(achievements):

    zorder 12000
    style_prefix "info"
    frame:
        background None
        xalign 1.0
        ypos 25
        vbox:
            spacing 10
            for i in range(len(achievements)):
                $achievement = achievements[i]
                frame at screen_achievement_notify_appear(0.2 * i):
                    padding (10, 10)
                    xsize 500
                    ysize 120
                    xalign 1.0
                    hbox:
                        imagebutton idle achievement.icon
                        null width 15
                        vbox:   
                            text '{color=%s}%s{/color}' % (achievement.textcolor, achievement.name)
                            text '{size=-3}%s{/size}' % achievement.info
                    
                    text '{size=-3}%s{/size}' % achievement.time() style "admonition_text":
                        xalign 0.98
                        yalign 0.98
                

    timer (0.2 * len(achievements) + persistent.notifyDuration) action Hide('achievement_screen_notify')
