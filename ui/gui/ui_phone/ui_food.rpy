

screen screen_food(player, item, name, money, mode=0):
    python:
        money = int(money * player.foodPrice)
        if GameDifficulty5.has(player):
            money = int(money * 1.25)

        def isclosed(player, item, n=0.1):
            if not GameDifficulty4.has(player) and not GameDifficulty5.has(player):
                return False
            MAXPOINT = 1000
            pseed = rs(player, 1, MAXPOINT)
            iseed = rh(item.id, player, 1, MAXPOINT)
            if abs(pseed - iseed) < MAXPOINT * n:
                return True
            return False



    if not isclosed(player, item):
        frame:
            ysize 130
            xfill True
            background None
            imagebutton idle "gui/phone/food/"+item.__name__+".jpg":
                action [Hide("info"), Show(screen="screen_phone_food_selected", player=player, item=item, money=money, mode=mode)]
                hovered Show(screen="info", t=name, i=_('价格：')+str(money)+_('\n\n')+item.info, a=item.ad)
                unhovered Hide("info")
                background Frame("gui/style/musicplayer_[prefix_]background.png", tile=gui.frame_tile)
                activate_sound audio.cursor
                xfill True
                yalign 0.5
                at app_transform
            text name:
                xpos 0.25
                size 35
                style "foodname"
                yalign 0.0
            text _("￥")+str(money):
                xpos 0.25
                style "foodprice"
                size 30
                yalign 1.0
        null height 2


screen screen_phone_food_selected(player, item, money, mode=0):
    use barrier(screen="screen_phone_food_selected")
    python:
        def spec(player, mode):
            if mode == 1:
                player.buyrandom = True

    style_prefix "info"
    zorder 650
    default pp = renpy.get_mouse_pos()
    python:
        p = pp
        if p[0] < 1500:
            xc = 0.0
            trans = trans_toLeft
        else:
            xc = 1.0
            trans = trans_toRight
        xc = 0.0 if p[0] < 1500 else 1.0
        yc = 0.0 if p[1] < 540 else 1.0
    frame:
        pos pp
        xanchor xc
        yanchor yc
        xsize 300
        ysize 220
        at trans()
        has vbox
        
        
        
        frame:
            background None
            ysize 50
            textbutton _("{size=-3}购买并使用{/size}"):
                if item not in player.itemcd:
                    action [Hide("screen_phone_food_selected"), Hide("food_use"), Function(buyAndUse, player=player, item=item, money=money), Function(spec, player, mode)]
                else:
                    action Function(showNotice, ["你今天已经吃过该食物了。"]), Hide("screen_phone_food_selected")
                background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor 
                text_style "white"
                text_size 30

        frame:
            background None
            ysize 50
            textbutton _("{size=-3}购买{/size}"):
                action [Hide("screen_phone_food_selected"), Hide("food_use"), Function(buy, player=player, item=item, money=money), Function(spec, player, mode)]
                background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor 
                text_style "white"
                text_size 30


        frame:
            background None
            ysize 50
            
            python:
                t=item.name
                i=_('价格：')+str(money)+_('\n\n')+item.info
                a=item.ad

            textbutton _("{size=-3}详情{/size}"):
                action [Hide("screen_phone_food_selected"), Show(screen="info_use",t=t, i=i, a=a, pp=renpy.get_mouse_pos())]
                background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor 
                text_style "white"
                text_size 30

        

        frame:
            background None
            ysize 50
            textbutton _("{size=-3}取消{/size}"):
                action Hide("screen_phone_food_selected")
                background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor 
                text_style "white"
                text_size 30



    


screen screen_phone_food(player):


    predict False
    style_prefix "gameUI"
    zorder 600
    
    
    if player.times == 2:
        $store = '1'
        $storename = '曼玲早餐铺'
        $storeinfo = '一日之计在于晨，而没有早餐的清晨是不完整的......'
    elif player.times == 5:
        $store = '2'
        $storename = '芝士诱惑私房餐厅'
        $storeinfo = '本店选用优质芝士，假一赔十......'
    elif player.times == 10:
        $store = '3'
        $storename = 'Endorphins西餐厅'
        $storeinfo = '亲爱的顾客您好，有食物问题请致电我们的店长S......'
    else:
        $store = '4'
        $storename = '优选便利店'
        $storeinfo = '欢迎光临，本店24小时开业，满18元起送......'



    frame:
        
        if phone_page == 9:
            at app_inner_show(110, 50)
        else:
            at app_inner_hide(110, 50)

        
        background None
        xcenter 0.5
        ycenter 0.5
        yoffset -10
        
        use barrier('', 0)

        add "gui/phone/wallpaper/food.webp":
            xcenter 0.5

        add "gui/phone/food/header"+store+".jpg":
            xcenter 0.5
        

        text storename style 'phone' size 40 xpos 0.01 ycenter 0.18
        text storeinfo style "foodname" xpos 0.01 ypos 290 size 17 color "#383838"
        add "gui/phone/food/icon"+store+".jpg":
            xcenter 0.85
            ycenter 0.18

        frame:
            
            background None
            xalign 0.5
            yalign 0.55
            ysize 1300
            xsize 582
            



            frame:
                ypos 320
                background None
                vbox:
                    spacing 2
                    if store == '1':
                        use screen_food(player, ToastFood, _("早餐必备厚蛋吐司"), 15)
                        use screen_food(player, CoffeeFood, _("月巴克手冲咖啡"), 10)
                        use screen_food(player, SaladFood, _("香醋汁时蔬沙拉"), 15)

                    elif store == '2':
                        use screen_food(player, PizzaFood, _("分量满满香肠披萨"), 25)
                        use screen_food(player, BurgerFood, _("双层安格斯牛肉汉堡"), 30)
                        use screen_food(player, BreadFood, _("奶油夹心凯撒面包"), 25)

                    elif store == '3':
                        use screen_food(player, PastaFood, _("那不勒斯番茄意面"), 30)
                        use screen_food(player, SoupFood, _("超浓郁碗装鱼翅汤"), 35)
                        use screen_food(player, SteakFood, _("迷迭香真空烹调战斧牛排"), 55)

                    elif store == '4':
                        use screen_food(player, Cigarette, _("一包香烟"), 250)
                        use screen_food(player, Alcohol, _("梅子酒"), 40)

                        if rrs(player, 20) and not player.buyrandom:
                            $temp = rcs(player, (1,1,1,2,2,2,3,3,3,4))
                            if temp == 1:
                                use screen_food(player, Cola, _("听装冰镇可乐"), 40, 1)
                            elif temp == 2:
                                use screen_food(player, StreetFood10, _("食本道速食面"), 30, 1)
                            elif temp == 3:
                                use screen_food(player, StreetFood9, _("弱碱性纯天然矿泉水"), 20, 1)
                            elif temp == 4:
                                use screen_food(player, Strawberry, _("新鲜奶油草莓"), 50, 1)
            


                                



            frame:
                background None
                xpos 0.03
                ypos 0.06
                imagebutton auto "gui/phone/backw_%s.png":
                    action SetVariable("phone_page", 0), Hide("info")
                    hover_sound audio.cursor
            

                
    
    key 'K_ESCAPE' action SetVariable("phone_page", 0), Hide("info")