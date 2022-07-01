screen screen_phone_food(player):
    #tag gamegui
    modal True
    style_prefix "gameUI"
    zorder 100
    

    frame:
        at trans_app(70, 170)
        background None
        xalign 0.5
        yalign 0.5
        ysize 750
        xsize 400

        #add "gui/phone/phone_desktop.png":
        #    xcenter 0.5
        #    ycenter 0.45
        #add "gui/phone/address/address.png":
        #    xcenter 0.5
        #    ycenter 0.45

        #label _("{size=-10}{color=#000000}联系人"):
        #    xpos 0.41
        #    ypos 0.2
        text _("{size=+5}吃了吗外卖{/size}"):
            style "food"
            xpos 0.04
            ypos 0.08
        if player.times < 5:
            text _("{size=-5}上午好！黄金会员Solitus！{/size}"):
                style "food"
                xpos 0.04
                ypos 0.13
        if player.times == 5:
            text _("{size=-5}中午好！黄金会员Solitus！{/size}"):
                style "food"
                xpos 0.04
                ypos 0.13
        if player.times > 5:
            text _("{size=-5}晚上好！黄金会员Solitus！{/size}"):
                style "food"
                xpos 0.04
                ypos 0.13

        frame:
            ypos 120
            background None
            vbox:
                spacing 2

                if player.times < 5:
                    frame:
                        ysize 75
                        xfill True
                        background None
                        imagebutton idle "gui/phone/food/toast.png":
                            action [Hide("info"), Show(screen="food_use", player=player, item=ToastFood, money=10, pp=renpy.get_mouse_pos(), a=ToastFood.ad)]
                            hovered Show(screen="info", i="早餐必备厚蛋吐司"+'\n'+'价格：'+str(10)+'\n\n'+ToastFood.info, a=ToastFood.ad)
                            unhovered Hide("info")
                            background Frame("gui/style/musicplayer_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            activate_sound audio.cursor
                            xfill True
                            yalign 0.5
                        textbutton _("早餐必备厚蛋吐司"):
                            xpos 0.18
                            hover_sound audio.cursor
                            text_style "white"
                            yalign 0.5
                        textbutton _("￥10"):
                            xpos 0.8
                            hover_sound audio.cursor
                            text_style "white"
                            yalign 0.5
                    null height 2
                    frame:
                        ysize 75
                        xfill True
                        background None
                        imagebutton idle "gui/phone/food/coffee.png":
                            action [Hide("info"), Show(screen="food_use", player=player, item=CoffeeFood, money=10, pp=renpy.get_mouse_pos(), a=CoffeeFood.ad)]
                            hovered Show(screen="info", i="月巴克手冲咖啡"+'\n'+'价格：'+str(10)+'\n\n'+CoffeeFood.info, a=CoffeeFood.ad)
                            background Frame("gui/style/musicplayer_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            unhovered Hide("info")
                            activate_sound audio.cursor
                            xfill True
                            yalign 0.5
                        textbutton _("月巴克手冲咖啡"):
                            xpos 0.18
                            hover_sound audio.cursor
                            text_style "white"
                            yalign 0.5
                        textbutton _("￥10"):
                            xpos 0.8
                            hover_sound audio.cursor
                            text_style "white"
                            yalign 0.5
                    null height 2
                    frame:
                        ysize 75
                        xfill True
                        background None
                        imagebutton idle "gui/phone/food/salad.png":
                            action [Hide("info"), Show(screen="food_use", player=player, item=SaladFood, money=20, pp=renpy.get_mouse_pos(), a=SaladFood.ad)]
                            hovered Show(screen="info", i="香醋汁时蔬沙拉"+'\n'+'价格：'+str(20)+'\n\n'+SaladFood.info, a=SaladFood.ad) 
                            background Frame("gui/style/musicplayer_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            unhovered Hide("info")
                            activate_sound audio.cursor
                            xfill True
                            yalign 0.5
                        textbutton _("香醋汁时蔬沙拉"):
                            xpos 0.18
                            hover_sound audio.cursor
                            text_style "white"
                            yalign 0.5
                        textbutton _("￥20"):
                            xpos 0.8
                            hover_sound audio.cursor
                            text_style "white"
                            yalign 0.5
                    null height 2

                if player.times == 5:

                    frame:
                        ysize 75
                        xfill True
                        background None
                        imagebutton idle "gui/phone/food/pizza.png":
                            action [Hide("info"), Show(screen="food_use", player=player, item=PizzaFood, money=25, pp=renpy.get_mouse_pos(), a=PizzaFood.ad)]
                            hovered Show(screen="info", i="分量满满香肠披萨"+'\n'+'价格：'+str(25)+'\n\n'+PizzaFood.info, a=PizzaFood.ad)
                            background Frame("gui/style/musicplayer_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            unhovered Hide("info")
                            activate_sound audio.cursor
                            xfill True
                            yalign 0.5
                        textbutton _("分量满满香肠披萨"):
                            xpos 0.18
                            hover_sound audio.cursor
                            text_style "white"
                            yalign 0.5
                        textbutton _("￥25"):
                            xpos 0.8
                            hover_sound audio.cursor
                            text_style "white"
                            yalign 0.5
                    null height 2
                    frame:
                        ysize 75
                        xfill True
                        background None
                        imagebutton idle "gui/phone/food/burger.png":
                            action [Hide("info"), Show(screen="food_use", player=player, item=BurgerFood, money=30, pp=renpy.get_mouse_pos(), a=BurgerFood.ad)]
                            hovered Show(screen="info", i="双层安格斯牛肉汉堡"+'\n'+'价格：'+str(30)+'\n\n'+BurgerFood.info, a=BurgerFood.ad) 
                            background Frame("gui/style/musicplayer_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            unhovered Hide("info")
                            activate_sound audio.cursor
                            xfill True
                            yalign 0.5
                        textbutton _("双层安格斯牛肉汉堡"):
                            xpos 0.18
                            hover_sound audio.cursor
                            text_style "white"
                            yalign 0.5
                        textbutton _("￥30"):
                            xpos 0.8
                            hover_sound audio.cursor
                            text_style "white"
                            yalign 0.5
                    null height 2
                    frame:
                        ysize 75
                        xfill True
                        background None
                        imagebutton idle "gui/phone/food/bread.png":
                            action [Hide("info"), Show(screen="food_use", player=player, item=BreadFood, money=20, pp=renpy.get_mouse_pos(), a=BreadFood.ad)]
                            hovered Show(screen="info", i="奶油夹心凯撒面包"+'\n'+'价格：'+str(20)+'\n\n'+BreadFood.info, a=BreadFood.ad) 
                            background Frame("gui/style/musicplayer_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            unhovered Hide("info")
                            activate_sound audio.cursor
                            xfill True
                            yalign 0.5
                        textbutton _("奶油夹心凯撒面包"):
                            xpos 0.18
                            hover_sound audio.cursor
                            text_style "white"
                            yalign 0.5
                        textbutton _("￥20"):
                            xpos 0.8
                            hover_sound audio.cursor
                            text_style "white"
                            yalign 0.5
                    null height 2

                if player.times > 5:

                    frame:
                        ysize 75
                        xfill True
                        background None
                        imagebutton idle "gui/phone/food/pasta.png":
                            action [Hide("info"), Show(screen="food_use", player=player, item=PastaFood, money=25, pp=renpy.get_mouse_pos(), a=PastaFood.ad)]
                            hovered Show(screen="info", i="那不勒斯黑椒意面"+'\n'+'价格：'+str(25)+'\n\n'+PastaFood.info, a=PastaFood.ad) 
                            background Frame("gui/style/musicplayer_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            unhovered Hide("info")
                            activate_sound audio.cursor
                            xfill True
                            yalign 0.5
                        textbutton _("那不勒斯黑椒意面"):
                            xpos 0.18
                            hover_sound audio.cursor
                            text_style "white"
                            yalign 0.5
                        textbutton _("￥25"):
                            xpos 0.8
                            hover_sound audio.cursor
                            text_style "white"
                            yalign 0.5
                    null height 2
                    frame:
                        ysize 75
                        xfill True
                        background None
                        imagebutton idle "gui/phone/food/soup.png":
                            action [Hide("info"), Show(screen="food_use", player=player, item=SoupFood, money=30, pp=renpy.get_mouse_pos(), a=SoupFood.ad)]
                            hovered Show(screen="info", i="超浓郁鲑鱼靓汤"+'\n'+'价格：'+str(30)+'\n\n'+SoupFood.info, a=SoupFood.ad) 
                            background Frame("gui/style/musicplayer_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            unhovered Hide("info")
                            activate_sound audio.cursor
                            xfill True
                            yalign 0.5
                        textbutton _("超浓郁鲑鱼靓汤"):
                            xpos 0.18
                            hover_sound audio.cursor
                            text_style "white"
                            yalign 0.5
                        textbutton _("￥30"):
                            xpos 0.8
                            hover_sound audio.cursor
                            text_style "white"
                            yalign 0.5
                    null height 2
                    frame:
                        ysize 75
                        xfill True
                        background None
                        imagebutton idle "gui/phone/food/steak.png":
                            action [Hide("info"), Show(screen="food_use", player=player, item=SteakFood, money=60, pp=renpy.get_mouse_pos(), a=SteakFood.ad)]
                            hovered Show(screen="info", i="好吃到哇塞的战斧牛排"+'\n'+'价格：'+str(60)+'\n\n'+SteakFood.info, a=SteakFood.ad) 
                            background Frame("gui/style/musicplayer_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            unhovered Hide("info")
                            activate_sound audio.cursor
                            xfill True
                            yalign 0.5
                        textbutton _("{size=-2}好吃到哇塞的战斧牛排{/size}"):
                            xpos 0.18
                            hover_sound audio.cursor
                            text_style "white"
                            yalign 0.5
                        textbutton _("￥60"):
                            xpos 0.8
                            hover_sound audio.cursor
                            text_style "white"
                            yalign 0.5
                    null height 2

        text _("{size=-5}精品烟酒特供：{/size}"):
            style "food"
            xpos 0.04
            ypos 0.53

        frame:
            ypos 410
            background None
            vbox:
                spacing 2
                frame:
                    ysize 75
                    xfill True
                    background None
                    imagebutton idle "gui/phone/food/cig.png":
                        action [Hide("info"), Show(screen="food_use", player=player, item=Cigarette, money=20, pp=renpy.get_mouse_pos(), a=Cigarette.ad)]
                        hovered Show(screen="info", i="香烟"+'\n'+'价格：'+str(20)+'\n\n'+Cigarette.info, a=Cigarette.ad)
                        unhovered Hide("info")
                        background Frame("gui/style/musicplayer_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                        activate_sound audio.cursor
                        xfill True
                        yalign 0.5
                    textbutton _("香烟"):
                        xpos 0.18
                        hover_sound audio.cursor
                        text_style "white"
                        yalign 0.5
                    textbutton _("￥20"):
                        xpos 0.8
                        hover_sound audio.cursor
                        text_style "white"
                        yalign 0.5
                null height 2
                frame:
                    ysize 75
                    xfill True
                    background None
                    imagebutton idle "gui/phone/food/alc.png":
                        action [Hide("info"), Show(screen="food_use", player=player, item=Alcohol, money=40, pp=renpy.get_mouse_pos(), a=Alcohol.ad)]
                        hovered Show(screen="info", i="梅子酒"+'\n'+'价格：'+str(40)+'\n\n'+Alcohol.info, a=Alcohol.ad)
                        background Frame("gui/style/musicplayer_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                        unhovered Hide("info")
                        activate_sound audio.cursor
                        xfill True
                        yalign 0.5
                    textbutton _("梅子酒"):
                        xpos 0.18
                        hover_sound audio.cursor
                        text_style "white"
                        yalign 0.5
                    textbutton _("￥40"):
                        xpos 0.8
                        hover_sound audio.cursor
                        text_style "white"
                        yalign 0.5
                
        frame:
            background None
            xpos 0.8
            ypos 0.83
            imagebutton auto "gui/phone/back_%s.png":
                action [Hide("screen_phone_food"),Hide("info"),Show(screen="screen_phone", player=player)]
                hover_sound audio.cursor
    
    key 'K_ESCAPE' action [Hide("screen_phone_food"),Hide("info"),Show(screen="screen_phone", player=player)]


screen food_use(player, item, money, a=None, width=400, pp=renpy.get_mouse_pos()):
    use barrier(screen="food_use")
    style_prefix "info"
    zorder 400
    $p = pp
    $i=item.name+'\n'+'价格：'+str(money)+'\n\n'+item.info
    if p[0] < 1500:
        $xc = 0.0
        $trans = trans_toLeft
    else:
        $xc = 1.0
        $trans = trans_toRight
    $xc = 0.0 if p[0] < 1500 else 1.0
    $yc = 0.0 if p[1] < 540 else 1.0
    frame:
        pos pp
        padding (15, 15)
        xanchor xc
        yanchor yc
        at trans()
        vbox:
            align pp
            if i is not None:
                label _(i):
                    text_style "info_text"
                    xsize width
            if a is not None:
                $a = '{i}' + a
                null height 13
                label _(a):
                    text_style "admonition_text"
                    xsize width
            null height 30
            hbox:
                xalign 0.5
                spacing 40
                textbutton _("{size=-3}购买{/size}"):
                    action [Hide("food_use"), Function(buy, player=player, item=item, money=money)]
                    activate_sound audio.cursor
                if item.__name__ not in player.itemcd:
                    textbutton _("{size=-3}购买并使用{/size}"):
                        action [Hide("food_use"), Function(buyAndUse, player=player, item=item, money=money)]
                        activate_sound audio.cursor
                else:
                    textbutton _("{size=-3}购买并使用{/size}") text_style "grey":
                        action NullAction()
                        activate_sound audio.error
                textbutton _("{size=-3}取消{/size}"):
                    action Hide("food_use")
                    activate_sound audio.cursor

    key 'K_ESCAPE' action Hide("food_use")