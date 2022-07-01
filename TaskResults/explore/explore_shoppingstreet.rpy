label explore_shop:
    $temp = ra(p, 1, 6)
    $jumplabel = 'explore_shop_' + str(temp)
    $renpy.jump(jumplabel)

label explore_shop_1:
    scene arcade with fade
    "进入了一家新开的游戏厅。"
    "你对大多数游戏都不感兴趣，不过你注意到了一排抓娃娃机。"
    "价格为10元一次。"
    "试试手气？"
    jump explore_shop_1_catch
    

label explore_shop_1_catch:
    scene arcade with dissolve
    menu:
        "夹一次" if p.money>10:
            scene toys with dissolve
            $p.money -= 10
            $temp=rd(1,10)
            if temp==1:
                "你看着夹子缓缓下落，张开爪子，抓住那只黑色的有点像你认识的那个医生一样的娃娃。"
                "娃娃被夹子夹住，挪到空中……"
                "夹子正在夹着娃娃，缓缓移动到出口上方……"
                "夹子马上就要靠近出口了……！"
                "马上要抓到了！……"
                "啊…！娃娃从出口出来了！不可思议！"
                $PathosDoll.add(p)
                $p.severity -= 0.06
                $showNotice(['降低了6点严重程度。'])
                scene arcade with fade
                "心满意足了，该回去了。"
                jump GoOutside_result
            elif temp==2 or temp==3:
                "你看着夹子缓缓下落，张开爪子，抓住那只黑色的有点像你认识的那个医生一样的娃娃。"
                "娃娃被夹子夹住，挪到空中……"
                "夹子正在夹着娃娃，缓缓移动到出口上方……"
                "夹子马上就要靠近出口了……！"
                "马上要抓到了！……"
                "啊…！娃娃掉在了出口边上，就差一点点！"
                $p.severity += 0.02
                $showNotice(['提升了2点严重程度。'])
                pass
            elif temp==4 or temp==5:
                "你看着夹子缓缓下落，张开爪子，抓住那只黑色的有点像你认识的那个医生一样的娃娃。"
                "娃娃被夹子夹住，挪到空中……"
                "夹子正在夹着娃娃，缓缓移动到出口上方……"
                "夹子马上就要靠近出口了……！"
                "啊…！娃娃离开了夹子，掉下去了，就差一点！"
                $p.severity += 0.01
                $showNotice(['提升了1点严重程度。'])
                pass
            elif temp==6 or temp==7:
                "你看着夹子缓缓下落，张开爪子，抓住那只黑色的有点像你认识的那个医生一样的娃娃。"
                "娃娃被夹子夹住，挪到空中……"
                "夹子正在夹着娃娃，缓缓移动到出口上方……"
                "啊…！娃娃掉下去了，好可惜。"
                pass
            else:
                "你看着夹子缓缓下落，张开爪子，抓住那只黑色的有点像你认识的那个医生一样的娃娃。"
                "娃娃被夹子夹住，挪到空中……"
                "啊…！娃娃掉下去了，好可惜。"
                pass
            "还要继续吗？"
            menu:
                "继续":
                    jump explore_shop_1_catch
                "结束战斗":
                    "就到这里吧。"
                    "唉。"
                    jump GoOutside_result
        "算了":
            "就到这里吧。"
            "唉。"
            jump GoOutside_result


label explore_shop_2:
    scene store with fade
    "去小卖店溜达溜达好了。"
    $temp = p.money
    call screen screen_explore_store(p)
    if p.money==temp:
        "没啥东西，走了。"
    else:
        "收获满满……"
    jump GoOutside_result

screen screen_explore_store(player):
    #tag gamegui
    use barrier(screen="screen_explore_store", mode=0)

    $ items = [StreetFood9, StreetFood10, Cola, BadmintonRacket, Sneakers, NotePad, FileFolder]

    #modal True
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
                    textbutton '{size=+10}杂货{/size}':
                        text_style "gameUI"
                        xoffset -5
                        yoffset -5
                        action NullAction()

                    imagebutton auto "gui/icons/task_icon/exit_%s.png":
                        xalign 1.0
                        action [Hide("screen_explore_store"), Return()]

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
                            use screen_explore_store_show(player, items)
                    
screen screen_explore_store_show(player, items):
    
    vbox:
        xsize 640
        $typename = '杂货'
        hbox:
            textbutton '{size=-5}'+typename+'{/size}' text_style "white":
                action NullAction()
                xfill True
                xalign 1.0
                activate_sound audio.cursor
                #background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)

        vbox:
            #xalign 1.0
            for ite in items:
                frame:
                    background None
                    ysize 60
                    xfill True
                    $ite_name = ite.name
                    $money = r2(0.08 * player.price* rh(ite.id, player, 700, 1500) * 0.001)
                    if ite.kind == '收藏品':
                        $money = r2(money*4)
                    if ite == Cola:
                        $money = r2(money*2)
                    $info = ite.getPrincipalInfo()
                    $ad = ite.ad

                    frame:
                        background None
                        textbutton ite_name text_style "white":
                            action [Hide("info3"),Show(screen="screen_explore_store_use", player=player,money=money, book=ite(player), pp=renpy.get_mouse_pos(), t=ite_name, i1=info, a1=ad)]
                            hovered [Show(screen="info3", t=ite_name, i1=info, a1=ad)]
                            unhovered Hide("info3")
                            background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            activate_sound audio.cursor
                            xfill True
                        textbutton str(money) text_style "white":
                            xpos 1.0
                            xoffset -40
                            xanchor 1.0

                    null height 2
        


        null height 30
        textbutton ''

screen screen_explore_store_use(player,money, book, pp, t=None, i1=None, a1=None, i2=None, a2=None, width=400):
    default num = '1'
    style_prefix "info"
    use barrier(screen="screen_explore_store_use")
    zorder 3000
    $p = pp
    $yc = 0.0 if p[1] < 540 else 1.0
    if p[0] < 1500:
        $xc = 0.0
        $trans = trans_toLeft
    else:
        $xc = 1.0
        $trans = trans_toRight
    frame:
        pos p
        padding (15, 15)
        xanchor xc
        yanchor yc
        at trans()
        vbox:
            align p
            if t is not None:
                label t+'\n':
                    text_style "info_text"
                    xsize width
            if i1 is not None:
                null height -8
                label '{size=-2}'+i1+'{/size}':
                    text_style "info_text"
                    xsize width
            if a1 is not None:
                $a1 = '{i}' + a1 + '{/i}'
                null height 13
                label a1:
                    text_style "admonition_text"
                    xsize width
            if i2 is not None:
                null height -6
                label '{size=-2}'+i2+'{/size}':
                    text_style "info_text"
                    xsize width
            if a2 is not None:
                $a2 = '{i}' + a2 + '{/i}'
                null height 13
                label a2:
                    text_style "admonition_text"
                    xsize width
            null height 30
            hbox:
                xalign 0.5
                hbox:
                    textbutton _("{size=-3}数量：{/size}"):
                        action NullAction()
                        activate_sound audio.cursor
                    frame:
                        background None
                        xsize 70
                        yalign 0.5
                        input:
                            value ScreenVariableInputValue("num")
                            style "white"
                            length 4
                            allow '0123456789'
                null width 10
                textbutton _("{size=-3}购买{/size}"):
                    action [Hide("screen_explore_store_use"), Function(buy, player=player, item=book, nums=int(num) if num!=''else 0, money=money)]
                    activate_sound audio.cursor
                null width 40
                textbutton _("{size=-3}取消{/size}"):
                    action Hide("screen_explore_store_use")
                    activate_sound audio.cursor


label explore_shop_3:
    scene store with dissolve
    "逛到了当地有名的小吃街。"
    "随便买点小吃好了……"
    $temp = p.money
    call screen screen_explore_buystreetfood(p)
    if p.money==temp:
        "没啥想吃的，还是算了。"
    else:
        "买了好多东西……回去再吃吧。"
    jump GoOutside_result


screen screen_explore_buystreetfood(player):
    #tag gamegui
    use barrier(screen="screen_explore_buystreetfood", mode=0)

    $ items = [StreetFood1, StreetFood2, StreetFood3, StreetFood4]

    #modal True
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
                    textbutton '{size=+10}购买小吃{/size}':
                        text_style "gameUI"
                        xoffset -5
                        yoffset -5
                        action NullAction()

                    imagebutton auto "gui/icons/task_icon/exit_%s.png":
                        xalign 1.0
                        action [Hide("screen_explore_buystreetfood"), Return()]

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
                            use screen_explore_buystreetfood_show(player, items)
                    
screen screen_explore_buystreetfood_show(player, items):
    
    vbox:
        xsize 640
        $typename = '小吃'
        $typei = itemKindInfo('食物', 'i')
        $typea = itemKindInfo('食物', 'a')
        hbox:
            textbutton '{size=-5}'+typename+'{/size}' text_style "white":
                action NullAction()
                hovered Show(screen="info", i=typei, a=typea)
                unhovered Hide("info")
                xfill True
                xalign 1.0
                activate_sound audio.cursor
                #background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)

        vbox:
            #xalign 1.0
            for ite in items:
                frame:
                    background None
                    ysize 60
                    xfill True
                    $ite_name = ite.name
                    $money = r2(0.02 * player.price* rh(ite.id, player, 700, 1500) * 0.001)
                    if ite.name == '插着木签的菠萝片':
                        $money = r2(money/2)
                    $info = ite.getPrincipalInfo()
                    $ad = ite.ad

                    frame:
                        background None
                        textbutton ite_name text_style "white":
                            action [Hide("info3"),Show(screen="screen_explore_buystreetfood_use", player=player,money=money, book=ite(player), pp=renpy.get_mouse_pos(), t=ite_name, i1=info, a1=ad)]
                            hovered [Show(screen="info3", t=ite_name, i1=info, a1=ad)]
                            unhovered Hide("info3")
                            background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            activate_sound audio.cursor
                            xfill True
                        textbutton str(money) text_style "white":
                            xpos 1.0
                            xoffset -40
                            xanchor 1.0

                    null height 2
        


        null height 30
        textbutton ''

screen screen_explore_buystreetfood_use(player,money, book, pp, t=None, i1=None, a1=None, i2=None, a2=None, width=400):
    default num = '1'
    style_prefix "info"
    use barrier(screen="screen_explore_buystreetfood_use")
    zorder 3000
    $p = pp
    $yc = 0.0 if p[1] < 540 else 1.0
    if p[0] < 1500:
        $xc = 0.0
        $trans = trans_toLeft
    else:
        $xc = 1.0
        $trans = trans_toRight
    frame:
        pos p
        padding (15, 15)
        xanchor xc
        yanchor yc
        at trans()
        vbox:
            align p
            if t is not None:
                label t+'\n':
                    text_style "info_text"
                    xsize width
            if i1 is not None:
                null height -8
                label '{size=-2}'+i1+'{/size}':
                    text_style "info_text"
                    xsize width
            if a1 is not None:
                $a1 = '{i}' + a1 + '{/i}'
                null height 13
                label a1:
                    text_style "admonition_text"
                    xsize width
            if i2 is not None:
                null height -6
                label '{size=-2}'+i2+'{/size}':
                    text_style "info_text"
                    xsize width
            if a2 is not None:
                $a2 = '{i}' + a2 + '{/i}'
                null height 13
                label a2:
                    text_style "admonition_text"
                    xsize width
            null height 30
            hbox:
                xalign 0.5
                hbox:
                    textbutton _("{size=-3}数量：{/size}"):
                        action NullAction()
                        activate_sound audio.cursor
                    frame:
                        background None
                        xsize 70
                        yalign 0.5
                        input:
                            value ScreenVariableInputValue("num")
                            style "white"
                            length 4
                            allow '0123456789'
                null width 10
                textbutton _("{size=-3}购买{/size}"):
                    action [Hide("screen_explore_buystreetfood_use"), Function(buy, player=player, item=book, nums=int(num) if num!=''else 0, money=money)]
                    activate_sound audio.cursor
                null width 40
                textbutton _("{size=-3}取消{/size}"):
                    action Hide("screen_explore_buystreetfood_use")
                    activate_sound audio.cursor


label explore_shop_4:
    scene giftshop with fade
    "逛到了一家看起来很豪华的礼品店。"
    "进去瞅瞅。"
    $temp = p.money
    call screen screen_explore_buystreetgift(p)
    if p.money==temp:
        "没好东西，不买了。"
    else:
        "这个东西还挺好的……回去放在我桌子上……"
    jump GoOutside_result


screen screen_explore_buystreetgift(player):
    #tag gamegui
    use barrier(screen="screen_explore_buystreetgift", mode=0)

    $ items = list(filter(lambda x: x.hasByType(p)!=True, (Humidifier, MusicBox, ClockTower, TomatoBrooch)))
    $ items.append(PaperStar)


    #modal True
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
                    textbutton '{size=+10}礼品店{/size}':
                        text_style "gameUI"
                        xoffset -5
                        yoffset -5
                        action NullAction()

                    imagebutton auto "gui/icons/task_icon/exit_%s.png":
                        xalign 1.0
                        action [Hide("screen_explore_buystreetgift"), Return()]

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
                            use screen_explore_buystreetgift_show(player, items)
                    
screen screen_explore_buystreetgift_show(player, items):
    
    vbox:
        xsize 640
        $typename = '收藏品'
        $typei = itemKindInfo('收藏品', 'i')
        $typea = itemKindInfo('收藏品', 'a')
        hbox:
            textbutton '{size=-5}'+typename+'{/size}' text_style "white":
                action NullAction()
                hovered Show(screen="info", i=typei, a=typea)
                unhovered Hide("info")
                xfill True
                xalign 1.0
                activate_sound audio.cursor
                #background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)

        vbox:
            #xalign 1.0
            for ite in items:
                frame:
                    background None
                    ysize 60
                    xfill True
                    $ite_name = ite.name
                    $money = r2(0.4 * player.price* rh(ite.id, player, 700, 1500) * 0.001)
                    if ite.name == '千纸鹤':
                        $money = r2(0.03 * player.price * rh(ite.id, player, 700, 1500) * 0.001)
                    $info = ite.getPrincipalInfo()
                    $ad = ite.ad

                    frame:
                        background None
                        textbutton ite_name text_style "white":
                            action [Hide("info3"),Show(screen="screen_explore_buystreetgift_use", player=player,money=money, book=ite(player), pp=renpy.get_mouse_pos(), t=ite_name, i1=info, a1=ad)]
                            hovered [Show(screen="info3", t=ite_name, i1=info, a1=ad)]
                            unhovered Hide("info3")
                            background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            activate_sound audio.cursor
                            xfill True
                        textbutton str(money) text_style "white":
                            xpos 1.0
                            xoffset -40
                            xanchor 1.0

                    null height 2
        


        null height 30
        textbutton ''

screen screen_explore_buystreetgift_use(player,money, book, pp, t=None, i1=None, a1=None, i2=None, a2=None, width=400):
    default num = '1'
    style_prefix "info"
    use barrier(screen="screen_explore_buystreetgift_use")
    zorder 3000
    $p = pp
    $yc = 0.0 if p[1] < 540 else 1.0
    if p[0] < 1500:
        $xc = 0.0
        $trans = trans_toLeft
    else:
        $xc = 1.0
        $trans = trans_toRight
    frame:
        pos p
        padding (15, 15)
        xanchor xc
        yanchor yc
        at trans()
        vbox:
            align p
            if t is not None:
                label t+'\n':
                    text_style "info_text"
                    xsize width
            if i1 is not None:
                null height -8
                label '{size=-2}'+i1+'{/size}':
                    text_style "info_text"
                    xsize width
            if a1 is not None:
                $a1 = '{i}' + a1 + '{/i}'
                null height 13
                label a1:
                    text_style "admonition_text"
                    xsize width
            if i2 is not None:
                null height -6
                label '{size=-2}'+i2+'{/size}':
                    text_style "info_text"
                    xsize width
            if a2 is not None:
                $a2 = '{i}' + a2 + '{/i}'
                null height 13
                label a2:
                    text_style "admonition_text"
                    xsize width
            null height 30
            hbox:
                xalign 0.5
                hbox:
                    textbutton _("{size=-3}数量：{/size}"):
                        action NullAction()
                        activate_sound audio.cursor
                    frame:
                        background None
                        xsize 70
                        yalign 0.5
                        input:
                            value ScreenVariableInputValue("num")
                            style "white"
                            length 4
                            allow '0123456789'
                null width 10
                textbutton _("{size=-3}购买{/size}"):
                    action [Hide("screen_explore_buystreetgift_use"), Function(buy, player=player, item=book, nums=int(num) if num!=''else 0, money=money), Return()]
                    activate_sound audio.cursor
                null width 40
                textbutton _("{size=-3}取消{/size}"):
                    action Hide("screen_explore_buystreetgift_use")
                    activate_sound audio.cursor



label explore_shop_5:
    scene cafe with fade
    "难得出门，喝点新鲜的咖啡好了。"
    $temp = p.money
    call screen screen_explore_buycoffee(p)
    if p.money==temp:
        "算了，都太贵了。"
    else:
        "今晚加班的时候喝……"
    jump GoOutside_result


screen screen_explore_buycoffee(player):
    #tag gamegui
    use barrier(screen="screen_explore_buycoffee", mode=0)

    $ items = [StreetFood5, StreetFood6, StreetFood7, StreetFood8]

    #modal True
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
                    textbutton '{size=+10}咖啡厅{/size}':
                        text_style "gameUI"
                        xoffset -5
                        yoffset -5
                        action NullAction()

                    imagebutton auto "gui/icons/task_icon/exit_%s.png":
                        xalign 1.0
                        action [Hide("screen_explore_buycoffee"), Return()]

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
                            use screen_explore_buycoffee_show(player, items)
                    
screen screen_explore_buycoffee_show(player, items):
    
    vbox:
        xsize 640
        $typename = '咖啡'
        $typei = itemKindInfo('食物', 'i')
        $typea = itemKindInfo('食物', 'a')
        hbox:
            textbutton '{size=-5}'+typename+'{/size}' text_style "white":
                action NullAction()
                hovered Show(screen="info", i=typei, a=typea)
                unhovered Hide("info")
                xfill True
                xalign 1.0
                activate_sound audio.cursor
                #background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)

        vbox:
            #xalign 1.0
            for ite in items:
                frame:
                    background None
                    ysize 60
                    xfill True
                    $ite_name = ite.name
                    $money = r2(0.04 * player.price* rh(ite.id, player, 500, 2000) * 0.001)
                    $info = ite.getPrincipalInfo()
                    $ad = ite.ad

                    frame:
                        background None
                        textbutton ite_name text_style "white":
                            action [Hide("info3"),Show(screen="screen_explore_buycoffee_use", player=player,money=money, book=ite(player), pp=renpy.get_mouse_pos(), t=ite_name, i1=info, a1=ad)]
                            hovered [Show(screen="info3", t=ite_name, i1=info, a1=ad)]
                            unhovered Hide("info3")
                            background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            activate_sound audio.cursor
                            xfill True
                        textbutton str(money) text_style "white":
                            xpos 1.0
                            xoffset -40
                            xanchor 1.0

                    null height 2
        


        null height 30
        textbutton ''

screen screen_explore_buycoffee_use(player,money, book, pp, t=None, i1=None, a1=None, i2=None, a2=None, width=400):
    default num = '1'
    style_prefix "info"
    use barrier(screen="screen_explore_buycoffee_use")
    zorder 3000
    $p = pp
    $yc = 0.0 if p[1] < 540 else 1.0
    if p[0] < 1500:
        $xc = 0.0
        $trans = trans_toLeft
    else:
        $xc = 1.0
        $trans = trans_toRight
    frame:
        pos p
        padding (15, 15)
        xanchor xc
        yanchor yc
        at trans()
        vbox:
            align p
            if t is not None:
                label t+'\n':
                    text_style "info_text"
                    xsize width
            if i1 is not None:
                null height -8
                label '{size=-2}'+i1+'{/size}':
                    text_style "info_text"
                    xsize width
            if a1 is not None:
                $a1 = '{i}' + a1 + '{/i}'
                null height 13
                label a1:
                    text_style "admonition_text"
                    xsize width
            if i2 is not None:
                null height -6
                label '{size=-2}'+i2+'{/size}':
                    text_style "info_text"
                    xsize width
            if a2 is not None:
                $a2 = '{i}' + a2 + '{/i}'
                null height 13
                label a2:
                    text_style "admonition_text"
                    xsize width
            null height 30
            hbox:
                xalign 0.5
                hbox:
                    textbutton _("{size=-3}数量：{/size}"):
                        action NullAction()
                        activate_sound audio.cursor
                    frame:
                        background None
                        xsize 70
                        yalign 0.5
                        input:
                            value ScreenVariableInputValue("num")
                            style "white"
                            length 4
                            allow '0123456789'
                null width 10
                textbutton _("{size=-3}购买{/size}"):
                    action [Hide("screen_explore_buycoffee_use"), Function(buy, player=player, item=book, nums=int(num) if num!=''else 0, money=money)]
                    activate_sound audio.cursor
                null width 40
                textbutton _("{size=-3}取消{/size}"):
                    action Hide("screen_explore_buycoffee_use")
                    activate_sound audio.cursor


label explore_shop_6:
    scene flowershop with fade
    "这里之前有一家花店吗？"
    "进去瞅瞅。"
    $temp = p.money
    call screen screen_explore_buystreetflower(p)
    if p.money==temp:
        "没好东西，不买了。"
    else:
        "这朵花好看……回去放在我桌子上的花瓶里养着……"
    jump GoOutside_result


screen screen_explore_buystreetflower(player):
    #tag gamegui
    use barrier(screen="screen_explore_buystreetflower", mode=0)

    $ items = list(filter(lambda x: x.hasByType(p)!=True, (Flower1, Flower2, Flower3)))


    #modal True
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
                    textbutton '{size=+10}花店{/size}':
                        text_style "gameUI"
                        xoffset -5
                        yoffset -5
                        action NullAction()

                    imagebutton auto "gui/icons/task_icon/exit_%s.png":
                        xalign 1.0
                        action [Hide("screen_explore_buystreetflower"), Return()]

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
                            use screen_explore_buystreetflower_show(player, items)
                    
screen screen_explore_buystreetflower_show(player, items):
    
    vbox:
        xsize 640
        $typename = '感兴趣的花'
        $typei = itemKindInfo('收藏品', 'i')
        $typea = itemKindInfo('收藏品', 'a')
        hbox:
            textbutton '{size=-5}'+typename+'{/size}' text_style "white":
                action NullAction()
                hovered Show(screen="info", i=typei, a=typea)
                unhovered Hide("info")
                xfill True
                xalign 1.0
                activate_sound audio.cursor
                #background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)

        vbox:
            #xalign 1.0
            for ite in items:
                frame:
                    background None
                    ysize 60
                    xfill True
                    $ite_name = ite.name
                    $money = r2(0.2 * player.price * rh(ite.id, player, 700, 1500) * 0.001)
                    $info = ite.getPrincipalInfo()
                    $ad = ite.ad

                    frame:
                        background None
                        textbutton ite_name text_style "white":
                            action [Hide("info3"),Show(screen="screen_explore_buystreetflower_use", player=player,money=money, book=ite(player), pp=renpy.get_mouse_pos(), t=ite_name, i1=info, a1=ad)]
                            hovered [Show(screen="info3", t=ite_name, i1=info, a1=ad)]
                            unhovered Hide("info3")
                            background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            activate_sound audio.cursor
                            xfill True
                        textbutton str(money) text_style "white":
                            xpos 1.0
                            xoffset -40
                            xanchor 1.0
                    null height 2
        null height 30
        textbutton ''

screen screen_explore_buystreetflower_use(player,money, book, pp, t=None, i1=None, a1=None, i2=None, a2=None, width=400):
    default num = '1'
    style_prefix "info"
    use barrier(screen="screen_explore_buystreetflower_use")
    zorder 3000
    $p = pp
    $yc = 0.0 if p[1] < 540 else 1.0
    if p[0] < 1500:
        $xc = 0.0
        $trans = trans_toLeft
    else:
        $xc = 1.0
        $trans = trans_toRight
    frame:
        pos p
        padding (15, 15)
        xanchor xc
        yanchor yc
        at trans()
        vbox:
            align p
            if t is not None:
                label t+'\n':
                    text_style "info_text"
                    xsize width
            if i1 is not None:
                null height -8
                label '{size=-2}'+i1+'{/size}':
                    text_style "info_text"
                    xsize width
            if a1 is not None:
                $a1 = '{i}' + a1 + '{/i}'
                null height 13
                label a1:
                    text_style "admonition_text"
                    xsize width
            if i2 is not None:
                null height -6
                label '{size=-2}'+i2+'{/size}':
                    text_style "info_text"
                    xsize width
            if a2 is not None:
                $a2 = '{i}' + a2 + '{/i}'
                null height 13
                label a2:
                    text_style "admonition_text"
                    xsize width
            null height 30
            hbox:
                xalign 0.5
                hbox:
                    textbutton _("{size=-3}数量：{/size}"):
                        action NullAction()
                        activate_sound audio.cursor
                    frame:
                        background None
                        xsize 70
                        yalign 0.5
                        input:
                            value ScreenVariableInputValue("num")
                            style "white"
                            length 4
                            allow '0123456789'
                null width 10
                textbutton _("{size=-3}购买{/size}"):
                    action [Hide("screen_explore_buystreetflower_use"), Function(buy, player=player, item=book, nums=int(num) if num!=''else 0, money=money)]
                    activate_sound audio.cursor
                null width 40
                textbutton _("{size=-3}取消{/size}"):
                    action Hide("screen_explore_buystreetflower_use")
                    activate_sound audio.cursor

