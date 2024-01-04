init python:
    def initshopinv(player):
        fishes = []
        for _ in range(ra(player, 3, 6)):
            rf = RawFish(player)
            rf.qty = r2(ra(player, 5, 25)*0.066*(1+player.fishpower*0.01))
            fishes.append(rf)
        return fishes

screen GoFishing_dashboard(player, fishgame=None, poz=None):
    style_prefix "info"

    drag:
        xpos 0.15
        ypos 0.02
        frame at trans_toRight(0.2):
            xsize 300
            ysize 300
            background 
            vbox:
                text "基础信息" style "gameL"
                text "精力 " + str(player.fishenergy) style "white"
                text "渔力 " + str(player.fishpower) style "white"
                text "捕获力 " + str(player.fishpoint) style "white"
                text "暴击率 " + str(player.fishcrit) + '%' style "white"
                if fishgame:
                    if not fishgame.hasA1:
                        $breakprob = str(1+fishgame.time*0.25)
                    else:
                        $breakprob = '0.0'
                    text "渔场信息" style "gameL"
                    text "难度 " + str(fishgame.hard) style "white"
                    text '挣脱概率 ' + breakprob + '%' style "white"
                    $a,b,c,d = fishgame.prob(poz)
                    text "宝藏概率 " + r2s(a) + '%' style "white"
                    text "垃圾概率 " + r2s(b) + '%' style "white"
                    text "???概率 " + r2s(c) + '%' style "white"



screen GoFishing_select_rod(player):
    python:
        allrods = (FishingRod1,FishingRod2, FishingRod3, FishingRod4,FishingRod99)
        hasrods = list(filter(lambda x: x.has(p), allrods))
        hasrods = [x.get(p) for x in hasrods]



    zorder 200
    drag:
        xcenter 0.5
        ycenter 0.48
        frame:
            at trans_toRight()
            style "translucent_frame"
            xsize 700
            ysize 800
            vbox:
                frame:
                    background None
                    yalign 0.001
                    textbutton '{size=+10}选择要使用的鱼竿{/size}':
                        text_style "gameUI"
                        xoffset -5
                        yoffset -5
                        action NullAction()

                    imagebutton auto "gui/exit_%s.png":
                        xalign 1.0
                        action [Hide("GoFishing_select_rod"), Return()]

                    frame:
                        background None
                        ysize 700
                        xsize 650
                        ypos 60
                        xpos 25

                        viewport:
                            mousewheel True
                            draggable True
                            #scrollbars "vertical"
                            vbox:

                                xsize 620
                                $typename = '工具'
                                $typei = itemKindInfo('工具', 'i')
                                $typea = itemKindInfo('工具', 'a')
                                hbox:
                                    textbutton '{size=-5}'+typename+'{/size}' text_style "white":
                                        action NullAction()
                                        hovered Show(screen="info", i=typei, a=typea)
                                        unhovered Hide("info")
                                        xfill True
                                        xalign 1.0
                                        xoffset -5
                                        activate_sound audio.cursor

                                vbox:
                                    for ite in hasrods:
                                        frame:
                                            background None
                                            ysize 90
                                            xfill True
                                                
                                                

                                            textbutton ite.name text_style "white":
                                                action [Hide("GoFishing_select_rod"),Hide("info_i"),Return(),Function(player.rtn, ite)]
                                                hovered Show(screen="info_i", player=player, item=ite)
                                                unhovered Hide("info_i")
                                                background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                                                activate_sound audio.cursor
                                                xfill True
                                                yfill True
                                                text_xpos 0.125
                                            imagebutton idle ite.icon():
                                                #xalign 0.5
                                                yalign 0.5
                                                xoffset 4

                                        null height 2
                                    null height 30
                        textbutton ''




screen GoFishing_screen_shop(player, shopinv):
    
    python:
        fishes = list(filter(lambda x: type(x) in (RawFish, RawFishFrozen), player.items))


        def trade(player, toitems, item, money=0):
            if player.money < money:
                Notice.add(_('你的钱不够。'))
            else:
                player.money -= money
                Notice.add(_('购买成功！花费%s元购买了%s！') % (money, item.name))
                player.items.append(item)
                if item in toitems:
                    del toitems[toitems.index(item)]
            Notice.show()

        def sell(player, toitems, item, money=0):
            player.money += money
            Notice.add(_('成功卖出%s！获得了%s元！') % (item.name, money))
            if item in player.items:
                del player.items[player.items.index(item)]
            toitems.append(item)
            Notice.show()


    zorder 200
    drag:
        xcenter 0.5
        ycenter 0.48
        frame:
            at trans_toRight()
            style "translucent_frame"
            xsize 700
            ysize 800
            vbox:
                frame:
                    background None
                    yalign 0.001
                    textbutton '{size=+10}鱼商{/size}':
                        text_style "gameUI"
                        xoffset -5
                        yoffset -5
                        action NullAction()

                    imagebutton auto "gui/exit_%s.png":
                        xalign 1.0
                        action [Hide("GoFishing_screen_shop"), Return()]

                    frame:
                        background None
                        ysize 700
                        xsize 650
                        ypos 60
                        xpos 25

                        viewport:
                            mousewheel True
                            draggable True
                            scrollbars "vertical"
                            vbox:

                                xsize 620
                                $typei = itemKindInfo('食物', 'i')
                                $typea = itemKindInfo('食物', 'a')
                                if shopinv:
                                    hbox:
                                        textbutton '{size=-5}对方持有的生鱼{/size}' text_style "white":
                                            action NullAction()
                                            hovered Show(screen="info", i=typei, a=typea)
                                            unhovered Hide("info")
                                            xfill True
                                            xalign 1.0
                                            xoffset -5
                                            activate_sound audio.cursor

                                    vbox:
                                        for ite in shopinv:
                                            frame:
                                                background None
                                                ysize 90
                                                xfill True
                                                    
                                                $money = r2(ite.qty * player.fishprice * player.price * 0.01 * 0.25 * 1.1)

                                                textbutton ite.name text_style "white":
                                                    action Function(trade, player=player, toitems=shopinv ,item=ite, money=money),Hide("info_buy_i")
                                                    hovered [Show(screen="info_buy_i", player=player, item=ite)]
                                                    unhovered Hide("info_buy_i")
                                                    background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                                                    activate_sound audio.cursor
                                                    xfill True
                                                    yfill True
                                                    text_xpos 0.125
                                                imagebutton idle ite.icon():
                                                    #xalign 0.5
                                                    yalign 0.5
                                                    xoffset 4

                                                textbutton str(money) text_style "white":
                                                    xpos 1.0
                                                    xoffset -40
                                                    xanchor 1.0
                                                    yalign 0.5


                                            null height 2
                                if fishes:
                                    hbox:
                                        textbutton '{size=-5}你持有的生鱼{/size}' text_style "white":
                                            action NullAction()
                                            hovered Show(screen="info", i=typei, a=typea)
                                            unhovered Hide("info")
                                            xfill True
                                            xalign 1.0
                                            xoffset -5
                                            activate_sound audio.cursor

                                    vbox:
                                        for ite in fishes:
                                            frame:
                                                background None
                                                ysize 90
                                                xfill True
                                                    
                                                    
                                                $money = r2(ite.qty * player.fishprice * player.price * 0.01 * 0.25)

                                                textbutton ite.name text_style "white":
                                                    action Function(sell, player=player, toitems=shopinv ,item=ite, money=money),Hide("info_i")
                                                    hovered Show(screen="info_i", player=player, item=ite)
                                                    unhovered Hide("info_i")
                                                    background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                                                    activate_sound audio.cursor
                                                    xfill True
                                                    yfill True
                                                    text_xpos 0.125
                                                imagebutton idle ite.icon():
                                                    #xalign 0.5
                                                    yalign 0.5
                                                    xoffset 4

                                                textbutton str(money) text_style "white":
                                                    xpos 1.0
                                                    xoffset -40
                                                    xanchor 1.0
                                                    yalign 0.5


                                            null height 2
                                        null height 30
                        textbutton ''

screen GoFishing_screen_fire(player):
    python:
        rawfishes = list(filter(lambda x: type(x) in (RawFish, RawFishFrozen), player.items))
        cookedfishes = list(filter(lambda x: type(x) == CookedFish, player.items))


    zorder 200
    drag:
        xcenter 0.5
        ycenter 0.48
        frame:
            at trans_toRight()
            style "translucent_frame"
            xsize 700
            ysize 800
            vbox:
                frame:
                    background None
                    yalign 0.001
                    textbutton '{size=+10}处理鱼肉{/size}':
                        text_style "gameUI"
                        xoffset -5
                        yoffset -5
                        action NullAction()

                    imagebutton auto "gui/exit_%s.png":
                        xalign 1.0
                        action [Hide("GoFishing_eatfish"), Return()]

                    frame:
                        background None
                        ysize 700
                        xsize 650
                        ypos 60
                        xpos 25

                        viewport:
                            mousewheel True
                            draggable True
                            scrollbars "vertical"
                            vbox:

                                xsize 620
                                $typei = itemKindInfo('食物', 'i')
                                $typea = itemKindInfo('食物', 'a')
                                if rawfishes:
                                    hbox:
                                        textbutton '{size=-5}生鱼{/size}' text_style "white":
                                            action NullAction()
                                            hovered Show(screen="info", i=typei, a=typea)
                                            unhovered Hide("info")
                                            xfill True
                                            xalign 1.0
                                            xoffset -5
                                            activate_sound audio.cursor

                                    vbox:
                                        for ite in rawfishes:
                                            frame:
                                                background None
                                                ysize 90
                                                xfill True
                                                    
                                                    

                                                textbutton ite.name text_style "white":
                                                    action Function(ite.cook,player),Hide("info_i")
                                                    hovered Show(screen="info_i", player=player, item=ite)
                                                    unhovered Hide("info_i")
                                                    background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                                                    activate_sound audio.bake
                                                    xfill True
                                                    yfill True
                                                    text_xpos 0.125
                                                imagebutton idle ite.icon():
                                                    #xalign 0.5
                                                    yalign 0.5
                                                    xoffset 4

                                                textbutton '品质：'+str(ite.qty) text_style "white":
                                                    xpos 1.0
                                                    xoffset -40
                                                    xanchor 1.0
                                                    yalign 0.5


                                            null height 2

                                if cookedfishes:
                                    hbox:
                                        textbutton '{size=-5}熟鱼{/size}' text_style "white":
                                            action NullAction()
                                            hovered Show(screen="info", i=typei, a=typea)
                                            unhovered Hide("info")
                                            xfill True
                                            xalign 1.0
                                            xoffset -5
                                            activate_sound audio.cursor

                                    vbox:
                                        for ite in cookedfishes:
                                            frame:
                                                background None
                                                ysize 90
                                                xfill True
                                                    
                                                textbutton ite.name text_style "white":
                                                    action Function(ui_itemUse, item=ite, player=player),Hide("info_i")
                                                    hovered Show(screen="info_i", player=player, item=ite)
                                                    unhovered Hide("info_i")
                                                    background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                                                    #activate_sound audio.itemeat
                                                    xfill True
                                                    yfill True
                                                    text_xpos 0.125
                                                imagebutton idle ite.icon():
                                                    #xalign 0.5
                                                    yalign 0.5
                                                    xoffset 4

                                                textbutton '品质：'+str(ite.qty) text_style "white":
                                                    xpos 1.0
                                                    xoffset -40
                                                    xanchor 1.0
                                                    yalign 0.5


                                            null height 2

                                    null height 30
                        textbutton ''

label GoFishing_beginning:
    play music audio.sliceoflife fadein 5
    if HotelBuff.has(p):
        scene location_hotel with fade
        "虽然我还是很想在这里一直躺着，但还是出去一下好了……"
    elif CafeBuff.has(p):
        scene location_cafe with fade
        "该离开这里了。"
        $CafeBuff.clearByType(p)
    elif BookstoreBuff.has(p):
        scene location_bookstore with fade 
        "该离开这里了。"
        $BookstoreBuff.clearByType(p)
    else:
        scene livingroom with fade
    
    $ p.onOutside = True
    $ParkBuff.add(p)
    $p.times+=1
    scene parkin with fade
    play music audio.lakesidebreeze
    "坐车抵达了森林公园……"
    $allrods = (FishingRod1,FishingRod2,FishingRod3,FishingRod4,FishingRod99)
    $haverods = sum([int(x.has(p)) for x in allrods])
    if haverods == 0:
        "……我的鱼竿呢？"
        "不会是在哪里丢了吧……真糟糕……只能回家去了。"
        jump GoFishing_result
    elif haverods == 1:
        $userod = list(filter(lambda x: x.has(p), allrods))[0].get(p)
        
    else:
        call screen GoFishing_select_rod(p)
        $userod = p.retval

    if not userod or type(userod) not in allrods:
        "……我的鱼竿呢？"
        "不会是在哪里丢了吧……真糟糕……只能回家去了。"
        jump GoFishing_result
    $p.fishenergy = p.fishmaxenergy
    $fire = False
    $userod.equipAction(p)

    $shopinv = initshopinv(p)
    jump GoFishing_park
    
label GoFishing_park:
    show screen GoFishing_dashboard(p)
    $poz = 'parkin'
    scene parkin with fade
    menu:
        "去哪里呢？"
        "商店":
            jump GoFishing_shop
        "池塘" if p.fishenergy > 0:
            $poz = 'pond'
            jump GoFishing_fishloop
        "湖泊" if p.fishenergy > 0:
            $poz = 'lake'
            jump GoFishing_fishloop
        "篝火":
            jump GoFishing_fire
        "离开":
            jump GoFishing_result

label GoFishing_fire:
    scene bonfire with fade
    if not fire:
        $fire = True
        "我回到上次我们架起篝火的位置，这里仍然有着被火烧过的木炭痕迹。"
        play sound audio.bonfire
        "升起火焰，木头的灰烬和火星随吹过的风飘起，只是这次没有他的气息。"
    menu:
        "篝火旁。"
        "处理鱼肉":
            call screen GoFishing_screen_fire(p)
            jump GoFishing_fire
        
        "休息" if p.fishenergy>0:
            menu:
                "休息会消耗所有精力，确定吗？"
                "确定":
                    call Task_processing from _call_Task_processing_20
                    scene bonfire with fade
                    "在火焰边休息了一会。"
                    $temp = r2(20 * RestTask.getRecoScale(p) * f())
                    $p.mental += temp
                    $showNotice(['恢复了%s点精神状态。'%temp])
                    $p.fishenergy = 0
                    jump GoFishing_fire
                "返回":
                    jump GoFishing_fire
        "离开":
            $fire = False
            "我熄灭了火焰，离开了这里。"
            jump GoFishing_park
                
        






label GoFishing_shop:
    if 9 not in p.visitedStore:
        $p.visitedStore.add(9)
        "我注意到湖边似乎有一家商店，上次来的时候完全没注意到。"
        scene fishshop with fade
        "我推开门，所见几乎全都是各种各样的鱼类，一只黑狼正坐在摆放着那些鱼的摊位的附近看手机，见我推门便抬起头来。"
        creefo_"“嗨，看你十分面生，看你拿着的鱼竿，一定是新来这边钓鱼的吧？”"
        creefo"“叫我Creefo就行，我在这里收购你们钓上来的鱼，你也可以在我这里买其他人钓上来的鱼。”"
        creefo"“收购价每周变化一次，记得常来看看哦。”"
        "他看上去十分友善，又有些熟悉。"
        $ss('blush')
        s"“你好，我是[p.name]……”"
        $sh()
        "和别人打招呼真让人害羞……"
        creefo"“哈哈，你还蛮可爱的，来看看商品吧。”"
    scene fishshop with fade
    menu:
        "Creefo的商店，那只黑狼正看着你。"
        "商店":
            call screen GoFishing_screen_shop(p, shopinv)
            jump GoFishing_shop
        "交谈":
            jump GoFishing_talk
        "离开":
            creefo"“之后再来玩哦。”"
            "他挥了挥手。"
            jump GoFishing_park
    
label GoFishing_talk:
    menu:
        "说些什么？"
        "想了解你更多一点":
            creefo"“叫我Creefo就行，我在这里收购你们钓上来的鱼，你也可以在我这里买其他人钓上来的鱼。”"
            creefo"“29岁，单身，目前就住在附近的村子里，没什么特别的能力，一直以卖鱼为生。”"
            creefo"“其他的我就没什么好说的了。”"
            jump GoFishing_talk
        "池塘和湖泊有什么区别？":
            creefo"“池塘是新手比较喜欢去的地方，那里的鱼游动速度都较慢，但大小和品质都不如湖泊区。”"
            creefo"“除此之外，池塘钓到垃圾的概率高一点，极少能钓到好东西，而湖泊钓到垃圾的概率较低，更容易钓到有用的东西。”"
            creefo"“不过品质越高的鱼游动速度也更快，如果你自认为是个高手，就去湖泊钓鱼吧！”"
            jump GoFishing_talk
        "精力，渔力和捕获力是什么？":
            creefo"“每1点渔力可以让你在钓鱼时提升1\%鱼的品质，降低1\%鱼游动的速度，提升1\%宝藏出现的概率，降低1\%垃圾出现的概率。”"
            creefo"“而捕获力可以增加你点击鱼的图标时提升的捕获率，换句话说捕获力越高，需要点击鱼的次数越少。”"
            creefo"“更换更好的钓具能够提升这些数值，来让你更好地对抗那些品质较高的鱼。”"
            creefo"“而精力则是代表你在这一回合里还能钓多少的鱼，当精力不足的时候，你还可以在公园里四处转转，但不能钓鱼了。”"
            creefo"“食用新鲜的熟鱼可以恢复精力，你可以在钓完鱼后到篝火旁烤些鱼，吃过之后用恢复的精力再去钓几次。”"
            jump GoFishing_talk
        "鱼类价格与品质":
            creefo"“虽然我每周都会根据行情更改价格，但唯一不变的是品质越高的鱼能卖给我的价格也越多。”"
            creefo"“虽然通常来说最好是你这边刚钓上来的鱼直接就卖给我，但可能因为行情较差，你不想卖给我。”"
            creefo"“你也可以在商店街的工具店买一个小型冰箱，来把生鱼变成冻生鱼，虽然这样做会降低一些品质，但具体要怎么做还是看你。”"
            creefo"“你也可以从我这里买新鲜的鱼，把它们冻住之后再等到下一周价格提升时转卖给我。”"
            creefo"“听起来有点像股票？哈哈……我只是一个卖鱼的罢了……”"
            jump GoFishing_talk
        "调情":
            $ss()
            s"“……”"
            $ss('scared_mouth normal2_eyes awkward_eyebrow')
            s"“……那个。”"
            $ss('smile_mouth smile_eyes smile_eyebrow blush')
            s"“今晚有时间和我出来吃个晚饭吗？”"
            $sh()
            $temp=rd(0,7)
            if temp==0:
                creefo"“嗯？……我比你大那么多，也对我感兴趣？”"
                creefo"“就别逗我了。”"
            elif temp==1:
                creefo"“如果你邀请我钓鱼可能还更有成功率一点。”"
                creefo"“但我不喜欢钓鱼。”"
            elif temp==2:
                creefo"“不行哦。”"

            elif temp==3:
                creefo"“嗯？那个时候我很忙。”"
            elif temp==4:
                creefo"“你这小家伙，居然敢调戏我。”"
                creefo"“方圆几里都没什么人，我想做什么……别人都不知道哦。”"
            elif temp==5:
                creefo"“你这小家伙，居然敢调戏我。”"
                creefo"“方圆几里都没什么人，我想做什么……别人都不知道哦。”"
            elif temp==6:
                creefo"“你这小家伙，居然敢调戏我。”"
                creefo"“方圆几里都没什么人，我想做什么……别人都不知道哦。”"
            elif temp==7:
                creefo"“你这小家伙，居然敢调戏我。”"
                creefo"“方圆几里都没什么人，我想做什么……别人都不知道哦。”"
            if temp<4:
                $ss('sweat')
                s"“好吧。”"
                $sh()
            else:
                $ss('blush sweat')
                s"“啊……我……”"
                $sh()
            jump GoFishing_talk
        "没什么要说的了":
            jump GoFishing_shop




label GoFishing_fishloop:
    if poz == 'pond':
        scene fishpond with fade
    else:
        scene fishbg with fade
    if p.fishenergy == 0:
        "我好累……已经没法继续钓鱼了……"
        jump GoFishing_park
    $fishgame = FishGame(p)
    show screen GoFishing_dashboard(p, fishgame, poz)
    play music audio.lakesidebreeze
    "准备钓鱼吧……"
    call Task_processing from _call_Task_processing_48
    '有鱼上钩了！'
    if type(userod) != FishingRod99:
        call screen screen_fishing(p, fishgame, poz)
    else:
        "钓竿开始自动收线……"
        $p.retval = fishgame.getfish(p, poz)
    jump GoFishing_fishloopend

label GoFishing_fishloopend:
    if userod:
        $userod.use(p)
        
    if p.retval == 0:
        pass
    elif type(userod) == FishingRod4 and rra(p, 33):
        $Notice.add('因为使用了较好的鱼竿，并没有消耗精力。')
    else:
        $p.fishenergy -= 1
        $Notice.add('消耗了1点精力！')

    

    if p.retval == -2:
        $Notice.show()
        $pause(0.3)
        "啊……线断了……"
        "我应该换一个好点的线的……"
    elif p.retval == -1:
        $Notice.show()
        $pause(0.3)
        "啊……鱼跑了……"
        "就差一点……"
    elif p.retval == 0:
        $Notice.show()
        $pause(0.3)
        "我已经没法继续战斗了……节省精力钓下一条好了……"
    else:
        if type(p.retval) == RawFish:
            $p.items.append(p.retval)
        else:
            $p.retval.add(p)
        $random_fish()
        $pause(0.3)
        scene fishsuccess with dissolve
        $Notice.show()
        if p.retval == GoldFish:
            $userod.goldfishes += 1
            if not userod.goldfishmon:
                $userod.goldfishmon = p.mon
                $userod.goldfishday = p.day
            "似乎钓上来一个金光闪闪的东西……"
            "是黄金鱼！"
        elif p.retval in (FishingAccessory1,FishingAccessory2,FishingAccessory3,FishingAccessory4,FishingItem1,FishingItem2,FishingItem3,FishingItem4):
            $userod.treasure += 1
            "浮上来一个小袋子，打开来看居然是[p.retval.name]！"
        elif p.retval in (FishingTrash1,FishingTrash2,FishingTrash3,FishingTrash4,FishingTrash5):
            $userod.trash += 1
            "钓到了[p.retval.name]……运气真差……"
        else:
            $userod.fishes += 1
            $userod.qtys += p.retval.qty
            "哦哦！钓到了品质为[p.retval.qty]的生鱼！"
    "……"
    jump GoFishing_fishloop














label GoFishing_result:
    if userod:
        $userod.unequipAction(p)
    $ParkBuff.clearByType(p)
    hide screen GoFishing_dashboard
    $p.updateAfterTask(GoOutside)
    if rra(p, 50):
        $Novelty.add(p)
    if rra(p, 25):
        $PhysRezB.add(p)
    if rra(p, 33):
        $Relaxation.add(p)
    stop music fadeout 5
    
    if p.times==4:
        scene morningrun with fade
    elif p.times==8:
        scene afternoonrun with fade
    else:
        scene nightrun with fade
    "回去的路上……"
    $p.times+=1
    $ p.onOutside = False
    if WeatherSmog.has(p):
        $WeatherSmog.get(p).check(p)
    $Notice.show()
    jump after_executing_task_label



