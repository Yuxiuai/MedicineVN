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
                    use screen_food(player, ToastFood, "早餐必备厚蛋吐司", 15, renpy.get_mouse_pos())
                    use screen_food(player, CoffeeFood, "月巴克手冲咖啡", 10, renpy.get_mouse_pos())
                    use screen_food(player, SaladFood, "香醋汁时蔬沙拉", 15, renpy.get_mouse_pos())

                if player.times == 5:
                    use screen_food(player, PizzaFood, "分量满满香肠披萨", 25, renpy.get_mouse_pos())
                    use screen_food(player, BurgerFood, "双层安格斯牛肉汉堡", 30, renpy.get_mouse_pos())
                    use screen_food(player, BreadFood, "奶油夹心凯撒面包", 25, renpy.get_mouse_pos())

                if player.times > 5:
                    use screen_food(player, PastaFood, "那不勒斯黑椒意面", 30, renpy.get_mouse_pos())
                    use screen_food(player, SoupFood, "超浓郁鲑鱼靓汤", 35, renpy.get_mouse_pos())
                    use screen_food(player, SteakFood, "好吃到哇塞的战斧牛排", 55, renpy.get_mouse_pos())


        text _("{size=-5}精品烟酒特供：{/size}"):
            style "food"
            xpos 0.04
            ypos 0.53

        frame:
            ypos 410
            background None
            vbox:
                spacing 2
                use screen_food(player, Cigarette, "香烟", 25, renpy.get_mouse_pos())
                use screen_food(player, Alcohol, "梅子酒", 35, renpy.get_mouse_pos())
                
        frame:
            background None
            xpos 0.8
            ypos 0.83
            imagebutton auto "gui/phone/back_%s.png":
                action [Hide("screen_phone_food"),Hide("info"),Show(screen="screen_phone", player=player)]
                hover_sound audio.cursor
    
    key 'K_ESCAPE' action [Hide("screen_phone_food"),Hide("info"),Show(screen="screen_phone", player=player)]
    
screen screen_food(player, item, name, money, pp):
    $money = int(money * player.foodPrice)
    frame:
        ysize 75
        xfill True
        background None
        imagebutton idle "gui/phone/food/"+item.__name__+".png":
            action [Hide("info"), Show(screen="food_use", player=player, item=item, money=money, pp=renpy.get_mouse_pos(), t=name, a=item.ad)]
            hovered Show(screen="info", t=name, i='价格：'+str(money)+'\n\n'+item.info, a=item.ad)
            unhovered Hide("info")
            background Frame("gui/style/musicplayer_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
            activate_sound audio.cursor
            xfill True
            yalign 0.5
        if len(name)>9:
            $name='{size=-2}'+name+'{/size}'
        textbutton name:
            xpos 0.18
            hover_sound audio.cursor
            text_style "white"
            yalign 0.5
        textbutton "￥"+str(money):
            xpos 0.8
            hover_sound audio.cursor
            text_style "white"
            yalign 0.5
    null height 2

screen food_use(player, item, money, t=None, a=None, width=400, pp=renpy.get_mouse_pos()):
    use barrier(screen="food_use")
    style_prefix "info"
    zorder 400
    $p = pp
    $i='价格：'+str(money)+'\n\n'+item.info
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
            if t is not None:
                label t+'\n':
                    text_style "info_text"
                    xsize width
            if i is not None:
                label i:
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
                    textbutton _("{size=-3}{color=#8d8d8d}购买并使用{/size}{/color}"):
                        action NullAction()
                        activate_sound audio.error
                textbutton _("{size=-3}取消{/size}"):
                    action Hide("food_use")
                    activate_sound audio.cursor

    key 'K_ESCAPE' action Hide("food_use")