label explore_shop_1:
    scene arcade with fade
    "进入了游戏厅。"
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
            $temp=rd(1,8)
            $p.visitedStore.add(1)
            if temp==1:
                "你看着夹子缓缓下落，张开爪子，抓住那只黑色的有点像你认识的那个医生一样的娃娃。"
                "娃娃被夹子夹住，挪到空中……"
                "夹子正在夹着娃娃，缓缓移动到出口上方……"
                "夹子马上就要靠近出口了……！"
                "马上要抓到了！……"
                "啊…！娃娃从出口出来了！不可思议！"
                
                if not PathosDoll.has(p):
                    $PathosDoll.add(p)
                    $p.gain_abi(-0.1, 'sev', stat='外出：夹娃娃')
                else:
                    $PathosDoll.add(p)
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
                $p.gain_abi(0.02, 'sev', stat='外出：夹娃娃')
                $Notice.show()
                pass
            elif temp==4 or temp==5:
                "你看着夹子缓缓下落，张开爪子，抓住那只黑色的有点像你认识的那个医生一样的娃娃。"
                "娃娃被夹子夹住，挪到空中……"
                "夹子正在夹着娃娃，缓缓移动到出口上方……"
                "夹子马上就要靠近出口了……！"
                "啊…！娃娃离开了夹子，掉下去了，就差一点！"
                $p.gain_abi(0.01, 'sev', stat='外出：夹娃娃')
                $Notice.show()
                pass
            elif temp==6:
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
    "去零食店买点零食吃好了……"
    $temp = p.money
    call screen screen_explore_store(p)
    $p.visitedStore.add(2)
    if p.money==temp:
        "没啥东西，走了。"
    else:
        "收获满满……"
    jump GoOutside_result

screen screen_explore_store(player):
    use barrier(screen="screen_explore_store", mode=0)

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
                    textbutton '{size=+10}零食店{/size}':
                        text_style "gameUI"
                        xoffset -5
                        yoffset -5
                        action NullAction()

                    imagebutton auto "gui/exit_%s.png":
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
                            python:
                                drinks = [AppleJuice, CitrusJuice, Cola]
                                
                                cookie = [SolitusCookie]
                                if DecayCookie in persistent.unlocked_items:
                                    cookie.append(DecayCookie)
                                if PathosCookie in persistent.unlocked_items:
                                    cookie.append(PathosCookie)
                                if AcolasCookie in persistent.unlocked_items:
                                    cookie.append(AcolasCookie)
                                if HallukeCookie in persistent.unlocked_items:
                                    cookie.append(HallukeCookie)
                            vbox:
                                use screen_buylist(player, [StreetFood9, StreetFood10, ChewingGum], p=0.2, d=15, n='零食')
                                null height 10
                                use screen_buylist(player, drinks, p=0.15, d=20, n='饮料')
                                null height 10
                                use screen_buylist(player, cookie, p=0.1, d=0, n='饼干')
                                null height 30
                                textbutton ''
                    
label explore_shop_3:
    scene foodstand with dissolve
    "逛到了当地有名的小吃街。"
    "随便买点小吃好了……"

    $temp = p.money
    call screen screen_explore_buystreetfood(p)
    $p.visitedStore.add(3)
    if p.money==temp:
        "没啥想吃的，还是算了。"
    else:
        "买了好多东西……回去再吃吧。"
    jump GoOutside_result


screen screen_explore_buystreetfood(player):
    use barrier(screen="screen_explore_buystreetfood", mode=0)

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

                    imagebutton auto "gui/exit_%s.png":
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
                            vbox:
                                use screen_buylist(player, [StreetFood1, StreetFood2], p=0.2, d=30, n='热食')
                                null height 10
                                use screen_buylist(player, [StreetFood3, StreetFood4], p=0.1, d=30, n='冷食')
                                if player.dep_p > 4:
                                    null height 10
                                    use screen_buylist(player, [StreetFood11,StreetFood12,StreetFood13], p=-1, d=30, n='饮料')
                                null height 30
                                textbutton ''

label explore_shop_4:
    scene giftshop with fade
    "逛到了一家看起来很豪华的礼品店。"
    "进去瞅瞅。"
    $temp = p.money
    call screen screen_explore_buystreetgift(p)
    $p.visitedStore.add(4)
    if p.money==temp:
        "没好东西，不买了。"
    else:
        "这个东西还挺好的……回去放在我桌子上……"
    jump GoOutside_result


screen screen_explore_buystreetgift(player):
    #tag gamegui
    use barrier(screen="screen_explore_buystreetgift", mode=0)

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

                    imagebutton auto "gui/exit_%s.png":
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
                            vbox:
                                use screen_buylist(player, [TomatoBrooch, ToyDuck, SunnyDoll], p=0.8, d=30, n='礼品')
                                null height 10
                                use screen_buylist(player, [Humidifier, MusicBox, ClockTower], p=1.5, d=30, n='贵重礼品')
                                null height 30
                                textbutton ''


label explore_shop_5:
    scene cafe with fade
    if p.times<11:
        "咖啡渣的气味充斥着这家咖啡厅，如果我想在这里呆一段时间，应该去买杯咖啡……"
    else:
        "已经很晚了，买完咖啡就尽快离开好了……"
    $temp = p.money
    call screen screen_explore_buycoffee(p)
    $p.visitedStore.add(5)
    if p.money==temp:
        "算了，都太贵了。"
        jump GoOutside_result
    else:
        if p.times<11:
            menu:
                "要去找个座位呆一会么？"
                "找一个空位":
                    pass
                "离开":
                    jump GoOutside_result
        else:
            jump GoOutside_result
    $p.times+=1
    $CafeBuff.add(p)
    $Notice.show()
    $p.onOutside = False
    jump after_executing_task_label
    
label explore_shop_5_end:
    "差不多该回去了……"
    $CafeBuff.clearByType(p)
    jump before_operate_screen_label

screen screen_explore_buycoffee(player):
    #tag gamegui
    use barrier(screen="screen_explore_buycoffee", mode=0)

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

                    imagebutton auto "gui/exit_%s.png":
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
                            vbox:
                                use screen_buylist(player, [StreetFood5, StreetFood6, StreetFood7, StreetFood8], p=0.4, d=30, n='咖啡')
                                null height 10
                                use screen_buylist(player, [CreamCake, StrawberryCake, OrangeCake], p=0.4, d=20, n='蛋糕')
                                if CoffeeMachine.has(player):
                                    null height 10
                                    use screen_buylist(player, [Coffee1, Coffee2, Coffee3], p=-1, d=0, ds=False, n='咖啡材料')

                                null height 30
                                textbutton ''

label explore_shop_6:
    scene flowershop with fade
    "这里之前有一家花店吗？"
    "进去瞅瞅。"
    $temp = p.money
    call screen screen_explore_buystreetflower(p)
    $p.visitedStore.add(6)
    if p.money==temp:
        "没好东西，不买了。"
    else:
        "这朵花好看……回去放在我桌子上的花瓶里养着……"
    jump GoOutside_result


screen screen_explore_buystreetflower(player):
    #tag gamegui
    use barrier(screen="screen_explore_buystreetflower", mode=0)


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

                    imagebutton auto "gui/exit_%s.png":
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
                            vbox:
                                $flowers = [Flower1, Flower2, Flower3]
                                if player.mon == 5 and player.day in (20, 21):
                                    $flowers.append(Flower4)
                                use screen_buylist(player, flowers, p=0.6, d=30, n='鲜花')
                                null height 10

                                if not Cactus.has(player) and not WellCactus.has(player):
                                    use screen_buylist(player, [Cactus], p=0.5, d=30, n='仙人掌')
                                    null height 10
                                    
                                use screen_buylist(player, [CactusFood], p=0.35, d=30, n='仙人掌相关')
                                null height 30
                                textbutton ''

label explore_shop_7:
    scene store with fade
    "街尾有一家新开的工具店，进去看看？"
    $temp = p.money
    call screen screen_explore_store2(p)
    $p.visitedStore.add(7)
    if p.money==temp:
        "没啥东西，走了。"
    else:
        "收获满满……"
    jump GoOutside_result

screen screen_explore_store2(player):
    use barrier(screen="screen_explore_store2", mode=0)

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
                    textbutton '{size=+10}工具{/size}':
                        text_style "gameUI"
                        xoffset -5
                        yoffset -5
                        action NullAction()

                    imagebutton auto "gui/exit_%s.png":
                        xalign 1.0
                        action [Hide("screen_explore_store2"), Return()]

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
                                use screen_buylist(player, [Knife], p=0.5, d=20, n='刀具')
                                null height 10
                                use screen_buylist(player, [FixKit, Bondage], p=0.8, d=20, n='工具组')
                                null height 10
                                use screen_buylist(player, [RecordingPen, FasciaGun, Fridge], p=1, d=20, n='小电器')
                                null height 10
                                use screen_buylist(player, [Tarot, D6, D20, D1000], p=0.35, d=10, n='玩具')
                                null height 10
                                use screen_buylist(player, [Knife], p=0.5, d=20, n='刀具')
                                if GoFishing.isUnlocked(player):
                                    null height 10
                                    use screen_buylist(player, [FishingRod1,FishingRod2,FishingRod3,FishingRod4,FishingRod99], p=-1, d=50, n='鱼竿')
                                    null height 10
                                    use screen_buylist(player, [FishingAccessory1,FishingAccessory3,FishingAccessory4], p=-1, d=50, n='渔具')
                                null height 30
                                textbutton ''


label explore_shop_8:
    scene store with fade
    "是之前去过的文体用品店……？"
    "进去看看吧。"
    $temp = p.money
    call screen screen_explore_store3(p)
    $p.visitedStore.add(8)
    if p.money==temp:
        "没啥东西，走了。"
    else:
        "收获满满……"
    jump GoOutside_result

screen screen_explore_store3(player):
    use barrier(screen="screen_explore_store3", mode=0)

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
                    textbutton '{size=+10}文体用品{/size}':
                        text_style "gameUI"
                        xoffset -5
                        yoffset -5
                        action NullAction()

                    imagebutton auto "gui/exit_%s.png":
                        xalign 1.0
                        action [Hide("screen_explore_store3"), Return()]

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
                                use screen_buylist(player, [BadmintonRacket, Sneakers, NotePad, FileFolder], p=0.8, d=20, n='文体用品')
                                null height 30
                                textbutton ''