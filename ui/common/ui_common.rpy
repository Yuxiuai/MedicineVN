

screen ctc(arg=None):
    zorder 100
    add "gui/ctc.png" xalign 0.93 yalign 0.96 at ctc_bob



screen barrier(screen, mode=1,tr=dissolve):
    if mode == 0:
        button:
            xfill True
            yfill True
            action NullAction()
    else:
        button:
            xfill True
            yfill True
            action Hide(screen, transition=tr)
    



screen freeze(time=None): #show screen freeze(5)
    modal True
    zorder 50
    timer time:
        action Hide(screen="freeze")

    button:
        xfill True
        yfill True
        action NullAction()

screen cfreeze(time=None): #call screen freeze(5)
    modal True
    zorder 50
    timer time:
        action Return()

    button:
        xfill True
        yfill True
        action NullAction()


screen screen_buylist_selected(player, item, money, pp=renpy.get_mouse_pos(),only_buy_one=False):
    use barrier(screen="screen_buylist_selected")
    style_prefix "info"
    zorder 650
    default pp = renpy.get_mouse_pos()
    $yss = 3
    default num = '1'
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
        ysize 20 + 50 * yss
        at trans()
        has vbox
        if item.isUnique and item.has(player) and item.maxDu != -1:
            $hasuniquetext='你已经拥有了该道具，购买会恢复其耐久度至最大值，确定购买吗？\n已拥有的 %s 的耐久度为 %s 天，购买后可更新为 %s 天。'%(item.name, item.get(player).du, item.maxDu)
        frame:
            background None
            ysize 50
            textbutton _("购买"):
                if only_buy_one:
                    if player.money < money:
                        action [Hide("screen_buylist_selected"), Function(buy, player=player, item=item, nums=1, money=money)]
                    else:
                        action [Hide("screen_buylist_selected"), Function(buy, player=player, item=item, nums=1, money=money), Return()]
                elif item.isUnique and item.has(player) and item.maxDu != -1:
                    
                    action Hide("screen_buylist_selected"),Show(screen="info_confirm", i=hasuniquetext, act=[Hide("screen_buylist_selected"), Function(buy, player=player, item=item, nums=1, money=money)], text=_('确定'), pp=renpy.get_mouse_pos())
                elif item.isUnique or player.money < money:
                    action [Hide("screen_buylist_selected"), Function(buy, player=player, item=item, nums=1, money=money)]
                else:
                    action Hide("screen_buylist_selected"), Show(screen="screen_buylist_selected_buynum", player=player, item=item, money=money)
                background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor 
                text_style "white"
                text_size 27      



        frame:
            background None
            ysize 50
            

            textbutton _("详情"):
                action [Hide("screen_buylist_selected"), Show(screen="info_buy_i_use",player=player, item=item, pp=renpy.get_mouse_pos())]
                background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor 
                text_style "white"
                text_size 27


        frame:
            background None
            ysize 50
            textbutton _("取消"):
                action Hide("screen_buylist_selected")
                background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor 
                text_style "white"
                text_size 27

        if not only_buy_one:
            key 'K_RETURN' action [Hide("screen_buylist_selected"), Function(buy, player=player, item=item, nums=int(num) if num!=''else 0, money=money)]
            key 'K_KP_ENTER' action [Hide("screen_buylist_selected"), Function(buy, player=player, item=item, nums=int(num) if num!=''else 0, money=money)]
        key 'K_ESCAPE' action Hide("screen_buylist_selected")

screen screen_buylist_selected_buynum(player, item, money):
    use barrier(screen="screen_buylist_selected_buynum", mode=0)
    style_prefix "info"
    default nums = ''
    zorder 99999
    frame at trans_Up:
        padding (15, 15)
        xcenter 0.5
        ycenter 0.45
        
        if len(nums) > 3:
            $nums = '999'
        $shownum = nums if nums else '0'
        
        vbox:
            
            frame:
                background None
                xalign 0.5
                ysize 100
                yoffset 20
                $showtext = "购买 %s 个 %s，共计 %s 元。" % (shownum, item.name, money*int(shownum))
                textbutton showtext:
                    action NullAction()
                    activate_sound audio.cursor 
                    text_style "white"
                    text_size 27
                    text_xalign 0.5

            hbox:
                xalign 0.5
                frame:
                    xalign 0.5
                    background None
                    ysize 100
                    textbutton '0':
                        if nums and nums != '0':
                            action SetLocalVariable("nums", nums+'0')
                        background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                        xsize 80
                        yfill True
                        activate_sound audio.cursor 
                        text_style "white"
                        text_size 27
                        text_xalign 0.5
                if nums and nums != '0':
                    key "K_0" action SetLocalVariable("nums", nums+'0')
                    key "K_KP0" action SetLocalVariable("nums", nums+'0')
                    

                for i in range(1, 10):
                    frame:
                        background None
                        ysize 100
                        textbutton str(i):
                            action SetLocalVariable("nums", nums+str(i))
                            background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                            xsize 80
                            yfill True
                            activate_sound audio.cursor 
                            text_style "white"
                            text_size 27
                            text_xalign 0.5
                    key "K_%s"%i action SetLocalVariable("nums", nums+str(i))
                    key "K_KP%s"%i action SetLocalVariable("nums", nums+str(i))
            hbox:
                spacing 80
                xalign 0.5
                frame:
                    background None
                    ysize 100
                    textbutton "删除":
                        if len(nums)>1:
                            action SetLocalVariable("nums", nums[:len(nums)-1])
                        else:
                            action SetLocalVariable("nums", '')
                        background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                        xsize 100
                        yfill True
                        activate_sound audio.cursor 
                        text_style "white"
                        text_size 27
                        text_xalign 0.5
                
                

                frame:
                    background None
                    ysize 100
                    textbutton "清零":
                        action SetLocalVariable("nums", '')
                        background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                        xsize 100
                        yfill True
                        activate_sound audio.cursor 
                        text_style "white"
                        text_size 27
                        text_xalign 0.5

                frame:
                    background None
                    ysize 100
                    $maxnums = str(int(player.money/money))
                    textbutton "最大":
                        
                        if maxnums == '0':
                            action SetLocalVariable("nums", '')
                        else:
                            action SetLocalVariable("nums", maxnums)
                        background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                        xsize 100
                        yfill True
                        activate_sound audio.cursor 
                        text_style "white"
                        text_size 27
                        text_xalign 0.5
                frame:
                    background None
                    ysize 100
                    textbutton "购买":
                        if not nums:
                            action Function(showNotice, ["数量不能为空。"])
                        elif player.money >= int(nums)*money:
                            action [Hide("screen_buylist_selected_buynum"), Function(buy, player=player, item=item, nums=int(nums), money=money)]
                        else:
                            action Function(showNotice, ["你的钱不够。"])
                        background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                        xsize 100
                        yfill True
                        activate_sound audio.cursor 
                        text_style "white"
                        text_size 27
                        text_xalign 0.5

                   
                        

                    
                
                frame:
                    background None
                    ysize 100
                    textbutton "返回":
                        action Hide("screen_buylist_selected_buynum")
                        background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                        xsize 100
                        yfill True
                        activate_sound audio.cursor 
                        text_style "white"
                        text_size 27
                        text_xalign 0.5

            if len(nums)>1:
                key 'K_BACKSPACE' action SetLocalVariable("nums", nums[:len(nums)-1])
            else:
                key 'K_BACKSPACE' action SetLocalVariable("nums", '')

            if not nums:
                key 'K_RETURN' action Function(showNotice, ["数量不能为空。"])
                key 'K_KP_ENTER' action Function(showNotice, ["数量不能为空。"])
            elif player.money >= int(nums)*money:
                key 'K_RETURN' action [Hide("screen_buylist_selected_buynum"), Function(buy, player=player, item=item, nums=int(nums), money=money)]
                key 'K_KP_ENTER' action [Hide("screen_buylist_selected_buynum"), Function(buy, player=player, item=item, nums=int(nums), money=money)]
            else:
                key 'K_RETURN' action Function(showNotice, ["你的钱不够。"])
                key 'K_KP_ENTER' action Function(showNotice, ["你的钱不够。"])
                    
            key 'K_ESCAPE' action Hide("screen_buylist_selected_buynum")
            


screen screen_buylist(player, items, p, d, n=None, r=False, ds=True, only_buy_one=False):
    # n: 自定义类名
    # p: 相对于药价的价格，例如当p为1时，所有道具的基础价格和药价相等；当p为0.5时，所有道具的基础价格为药价的一半；当p=-1时，则使用物品的p成员变量来定义价格
    # d：浮动大小，如d为30时，相对于基础价格浮动大小为*70%~130%
    # r: 为真时，只允许购买一个物品
    python:

        def havediscount(player, item, n=0.1):
            MAXPOINT = 1000
            pseed = rs(player, 1, MAXPOINT)
            iseed = rh(item.id, player, 1, MAXPOINT)
            if abs(pseed - iseed) < MAXPOINT * n * 0.05:
                return 0.7
            if abs(pseed - iseed) < MAXPOINT * n * 0.5:
                return 0.8
            if abs(pseed - iseed) < MAXPOINT * n:
                return 0.9
            return False


    if len(items)>0:
        vbox:
            xsize 620
            if n:
                $typename = n
            else:
                $typename = items[0].kind
            $typei = itemKindInfo(items[0].kind, 'i')
            $typea = itemKindInfo(items[0].kind, 'a')
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
                for ite in items:
                    frame:
                        background None
                        ysize 90
                        xfill True
                        python:
                            if p==-1:
                                money = r2(ite.p * player.price * rh(ite.id, player, 1000-d*10, 1000+d*10) * 0.001)
                            else:
                                money = r2(p * player.price * rh(ite.id, player, 1000-d*10, 1000+d*10) * 0.001)

                            if GameDifficulty5.has(player):
                                money = r2(money * 1.2)

                            showmoney = str(money)

                            discount = havediscount(player, ite)
                            if discount and ds:
                                money = r2(money*discount)
                                showmoney = _('%s{color=#fde827}（-%s%s）{/color}') % (money, int(100-discount*100), '%')
                            else:
                                showmoney = str(money)
                            
                            

                        textbutton ite.name text_style "white":
                            action [Hide("info_buy_i"),Show(screen="screen_buylist_selected", player=player, item=ite(player), money=money, pp=renpy.get_mouse_pos(),only_buy_one=only_buy_one)]
                            hovered [Show(screen="info_buy_i", player=player, item=ite(player))]
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

                        textbutton str(showmoney) text_style "white":
                            xpos 1.0
                            xoffset -40
                            xanchor 1.0
                            yalign 0.5
                    null height 2



screen info_buy_i(player, item, width=400, pp=renpy.get_mouse_pos()):
    style_prefix "info"
    zorder 1000

    python:
        ite_name = item.name
        ite_main = item.getPrincipalInfo()
        if type(item) in (MedicineA, MedicineB, MedicineC, MedicineD):
            ite_main = '%s\n\n{color=#fde827}%s{/color}' % (ite_main, item.getrecoveryinfo(player))
        ite_ad = item.ad if item not in (FinishedCommission, UnfinishedCommission) else item.comm.inputs
        if ite_ad is None:
            ite_ad = ''

        t=ite_name
        i=ite_main
        a=ite_ad

        amounts = item.getamounts(player)
        if amounts > 0:
            i = _('{color=#fde827}已拥有数量：%s{/color}\n\n%s') % (amounts, i)
        else:
            i = _('{color=#fde827}未拥有{/color}\n\n%s') % (i)
        if item.maxDu != -1:
            if item.kind == '工具':
                i = _('%s\n\n{color=#fde827}可使用次数：%s次{/color}') % (i, item.maxDu)
            else:
                i = _('%s\n\n{color=#fde827}保质期：%s天{/color}') % (i, item.maxDu)
        else:
            i = _('%s\n\n{color=#fde827}不会损坏{/color}') % i
        if item.maxCd == 0:
            i = _('%s\n{color=#fde827}无冷却时间{/color}') % i
        elif item.maxCd != -1:
            i = _('%s\n{color=#fde827}冷却时间：%s天{/color}') % (i, item.maxCd)

    
        (xc,trans) = (0.0,trans_toLeft) if pp[0] < 1500 else (1.0,trans_toRight)
        yc = 0.0 if pp[1] < 540 else 1.0
        if width == 400:
            if a:
                if len(i) + len(a) > 150:
                    width = 600
            else:
                if len(i) > 100:
                    width = 600
    frame:
        pos pp
        padding (15, 15)
        xanchor xc
        yanchor yc
        at trans()

        
        hbox:
            vbox:
                align pp
                    

                if t is not None:
                    label '[t!t]\n':
                        text_style "info_text"
                        xsize width
                if i is not None:
                    label '{size=-2}[i!t]{/size}':
                        text_style "info_text"
                        xsize width
                if a is not None:
                    null height 16
                    label '{i}[a!t]{/i}':
                        text_style "admonition_text"
                        xsize width
            null width -75
            vbox:
                add item.icon()



screen info_buy_i_use(player, item, width=400, pp=renpy.get_mouse_pos()):
    style_prefix "info"
    use barrier(screen="info_buy_i_use")
    zorder 1000

    python:
        ite_name = item.name
        ite_main = item.getPrincipalInfo()
        if type(item) in (MedicineA, MedicineB, MedicineC, MedicineD):
            ite_main = '%s\n\n{color=#fde827}%s{/color}' % (ite_main, item.getrecoveryinfo(player))
        ite_ad = item.ad if item not in (FinishedCommission, UnfinishedCommission) else item.comm.inputs
        if ite_ad is None:
            ite_ad = ''

        t=ite_name
        i=ite_main
        a=ite_ad

        amounts = item.getamounts(player)
        if amounts > 0:
            i = _('{color=#fde827}已拥有数量：%s{/color}\n\n%s') % (amounts, i)
        else:
            i = _('{color=#fde827}未拥有{/color}\n\n%s') % (i)
        if item.maxDu != -1:
            if item.kind == '工具':
                i = _('%s\n\n{color=#fde827}可使用次数：%s次{/color}') % (i, item.maxDu)
            else:
                i = _('%s\n\n{color=#fde827}保质期：%s天{/color}') % (i, item.maxDu)
        else:
            i = _('%s\n\n{color=#fde827}不会损坏{/color}') % i
        if item.maxCd == 0:
            i = _('%s\n{color=#fde827}无冷却时间{/color}') % i
        elif item.maxCd != -1:
            i = _('%s\n{color=#fde827}冷却时间：%s天{/color}') % (i, item.maxCd)

    
        (xc,trans) = (0.0,trans_toLeft) if pp[0] < 1500 else (1.0,trans_toRight)
        yc = 0.0 if pp[1] < 540 else 1.0
        if width == 400:
            if a:
                if len(i) + len(a) > 150:
                    width = 600
            else:
                if len(i) > 100:
                    width = 600
    frame:
        pos pp
        padding (15, 15)
        xanchor xc
        yanchor yc
        at trans()

        
        hbox:
            vbox:
                align pp
                    

                if t is not None:
                    label '[t!t]\n':
                        text_style "info_text"
                        xsize width
                if i is not None:
                    label '{size=-2}[i!t]{/size}':
                        text_style "info_text"
                        xsize width
                if a is not None:
                    null height 16
                    label '{i}[a!t]{/i}':
                        text_style "admonition_text"
                        xsize width

            null width -75
            vbox:
                add item.icon()








































screen coffee_selected(player):
    use barrier(screen="coffee_selected")
    style_prefix "info"
    if renpy.get_screen('screen_items'):
        default quick = False
    else:
        default quick = True

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
    frame at trans:
        pos pp
        xanchor xc
        yanchor yc
        xsize 300
        vbox:
        
        
            if Coffee1.has(player):
                frame:
                    background None
                    ysize 50
                    textbutton _("制作冰美式"):
                        if quick:
                            action [Hide("coffee_selected"), Function(ui_itemUse, StreetFood5(player), player), Function(Coffee1.get(player).sub, player)]
                        else:
                            action [Hide("coffee_selected"), Function(StreetFood5.add, player), Function(Coffee1.get(player).sub, player)]
                        background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor 
                        text_style "white"
                        text_size 27


            
            

            if Coffee1.has(player) and Coffee2.has(player):
                frame:
                    background None
                    ysize 50
                    textbutton _("制作生椰拿铁"):
                        if quick:
                            action [Hide("coffee_selected"), Function(ui_itemUse, StreetFood6(player), player), Function(Coffee1.get(player).sub, player), Function(Coffee2.get(player).sub, player)]
                        else:
                            action [Hide("coffee_selected"), Function(StreetFood6.add, player), Function(Coffee1.get(player).sub, player), Function(Coffee2.get(player).sub, player)]
                        
                        background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor 
                        text_style "white"
                        text_size 27                
                                
            if Coffee1.has(player) and Coffee3.has(player):
                frame:
                    background None
                    ysize 50
                    textbutton _("制作摩卡咖啡"):
                        if quick:
                            action [Hide("coffee_selected"), Function(ui_itemUse, StreetFood7(player), player), Function(Coffee1.get(player).sub, player), Function(Coffee3.get(player).sub, player)]
                        else:
                            action [Hide("coffee_selected"), Function(StreetFood7.add, player), Function(Coffee1.get(player).sub, player), Function(Coffee3.get(player).sub, player)]
                        
                        background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor 
                        text_style "white"
                        text_size 27      
 


            frame:
                background None
                ysize 50
                textbutton _("取消"):
                    action Hide("coffee_selected")
                    background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                    xfill True
                    activate_sound audio.cursor 
                    text_style "white"
                    text_size 27
            null height 13




screen fix_select(player):
    use barrier(screen="fix_select")
    style_prefix "info"
    zorder 1000
    default pp = renpy.get_mouse_pos()
    $ p = pp
    if p[0] < 1500:
        $ xc = 0.0
        $ trans = trans_toLeft
    else:
        $ xc = 1.0
        $ trans = trans_toRight
    $ xc = 0.0 if p[0] < 1500 else 1.0
    $ yc = 0.0 if p[1] < 540 else 1.0
    $ fixlist = list(filter(lambda x: x.kind in ('收藏品', '工具') and x.id not in (622, 623, 624, 629) and x.du < x.maxDu and not x.broken, player.items))
    $ yss = len(fixlist) + 1
    if len(fixlist) == 0:
        $ yss = 2
    frame:
        pos pp
        padding (15, 15)
        xanchor xc
        yanchor yc
        xsize 400
        ysize yss* 50
        
        at trans()
        
        
        
        if len(fixlist) > 0:
            vbox:
                for i in fixlist:
                    frame:
                        background None
                        ysize 50
                        textbutton i.name text_style 'white':
                            action [Function(FixKit.get(player).useItem, player, type(i)),Hide("fix_select"),Hide('info')]
                            background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                            xfill True
                            activate_sound audio.cursor
                        $du_name = _('（%s / %s）') % (i.du, i.maxDu)
                        textbutton du_name text_style 'white':
                            xalign 1.0
        else:
            textbutton _('{size=-5}目前还没有需要修理的道具。{/size}') text_style "white":
                action NullAction()
                xfill True
                xalign 1.0
                activate_sound audio.cursor
                xoffset -5


screen fridge_check(player, fridge):
    use barrier(screen="fridge_check")
    style_prefix "info"
    zorder 1000
    default pp = renpy.get_mouse_pos()
    $ p = pp
    if p[0] < 1500:
        $ xc = 0.0
        $ trans = trans_toLeft
    else:
        $ xc = 1.0
        $ trans = trans_toRight
    $ xc = 0.0 if p[0] < 1500 else 1.0
    $ yc = 0.0 if p[1] < 540 else 1.0
    $ fridgelen = len(fridge.items)

    frame:
        pos pp
        padding (15, 15)
        xanchor xc
        yanchor yc
        xsize 500
        ysize 60 * fridgelen
        
        at trans()
        
        
        
        vbox:
            for i in range(len(fridge.items)):
                frame:
                    background None
                    ysize 50
                    if fridge.items[i]:
                        textbutton fridge.items[i].name text_style 'white':
                            if renpy.get_screen('screen_items'):
                                action [Function(fridge.take, player, i),Hide('info')]
                            else:
                                action [Function(fridge.taskuse, player, i),Hide('info')]
                            
                            background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                            xfill True
                            activate_sound audio.cursor
                        if fridge.items[i]:
                            $du_name = _('新鲜度：（%s / %s）') % (fridge.items[i].du, fridge.items[i].maxDu)
                            textbutton du_name text_style 'white':
                                xalign 1.0
                    else:
                        textbutton _('空位置') text_style 'white':
                            action [Show(screen='fridge_select', player=player, fridge=fridge, poz=i),Hide('info')]
                            background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                            xfill True
                            activate_sound audio.cursor


screen fridge_select(player, fridge, poz):
    use barrier(screen="fridge_select")
    style_prefix "info"
    zorder 1000
    default pp = renpy.get_mouse_pos()
    $ p = pp
    if p[0] < 1500:
        $ xc = 0.0
        $ trans = trans_toLeft
    else:
        $ xc = 1.0
        $ trans = trans_toRight
    $ xc = 0.0 if p[0] < 1500 else 1.0
    $ yc = 0.0 if p[1] < 540 else 1.0
    $ fixlist = list(filter(lambda x: x.kind == _('食物') and not x.broken, player.items))
    $ yss = len(fixlist) + 1
    if len(fixlist) == 0:
        $ yss = 2
    frame:
        pos pp
        padding (15, 15)
        xanchor xc
        yanchor yc
        xsize 400
        ysize yss* 50
        
        at trans()
        
        
        
        if len(fixlist) > 0:
            vbox:
                for i in range(len(fixlist)):
                    frame:
                        background None
                        ysize 50
                        textbutton fixlist[i].name text_style 'white':
                            action [Function(fridge.put, player, fixlist[i], poz),Hide("fridge_select"),Hide('info')]
                            background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                            xfill True
                            activate_sound audio.cursor
                        $du_name = _('（%s / %s）') % (fixlist[i].du, fixlist[i].maxDu)
                        textbutton du_name text_style 'white':
                            xalign 1.0
        else:
            textbutton _('{size=-5}目前还没有能够放进冰箱的食物。{/size}') text_style "white":
                action NullAction()
                xfill True
                xalign 1.0
                activate_sound audio.cursor
                xoffset -5

screen screen_BookRandConcEffect(player,adj):
    style_prefix "info"
    default num = ''
    zorder 3000
    use barrier(screen="screen_BookRandConcEffect", mode=0)
    python:
        def advantageReroll(player):
            import random
            seed = player.seed + player.safe
            random.seed(seed)
            perf1 = random.randint(int(1), int(100))
            random.seed(seed+0.001)
            perf2 = random.randint(int(1), int(100))
            if perf1 > perf2:
                return perf1, False
            return perf2, True

    frame at trans_Up:
        padding (15, 15)
        xcenter 0.5
        ycenter 0.45

        $perf, advantaged = advantageReroll(player)
        
        $res=int(perf)+int(adj)
        if res > 85:
            $clr = '{color=#05ff50}'
        elif res > 58:
            $clr = '{color=#05b0ff}'
        elif res > 18:
            $clr = '{color=#fbff05}'
        else:
            $clr = '{color=#ff4c05}'

        vbox:
            
            vbox:
                xalign 0.5
                $i1 = "下个日程获得的日程结果为：%s" % int(perf)
                $i2 = "日程调整值为：%s" % int(adj)
                $i3 = "最终结果为：[clr]%s{/color}" % (res)

                text i1:
                    style "white"
                    size 20
                    xalign 0.5
                text i2:
                    style "white"
                    size 20
                    xalign 0.5
                text i3:
                    style "white"
                    size 30
                    xalign 0.5
                null height 10
                text "是否消耗一层状态来修改日程结果？":
                    style "white"
                    size 30
                    xalign 0.5
                null height 10
                text "注：1~18为{color=#ff4c05}差{/color}；19~58为{color=#fbff05}中{/color}；59~85为{color=#05b0ff}良{/color}；86~100为{color=#05ff50}优{/color}。":
                    style "white"
                    size 18
                    xalign 0.5
                text "但运动类日程的{color=#ff4c05}差{/color}结果普遍阈值较高。":
                    style "white"
                    size 18
                    xalign 0.5

            hbox:
                spacing 80
                xalign 0.5
                frame:
                    background None
                    ysize 100
                    textbutton "修改":
                        if BookRandConcEffect.getstack(player) > 1:
                            action Function(player.afterUseSeed), Function(player.afterUseSeed), Function(BookRandConcEffect.subByType, player)
                        else:
                            action Function(player.afterUseSeed), Function(player.afterUseSeed), Function(BookRandConcEffect.subByType, player),Return()
                        background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                        xsize 300
                        yfill True
                        activate_sound audio.dice
                        text_style "white"
                        text_size 27
                        text_xalign 0.5
                
                

                frame:
                    background None
                    ysize 100
                    textbutton "选择当前结果":
                        if advantaged:
                            action Function(player.afterUseSeed), Return()
                        else:
                            action Return()
                        background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                        xsize 300
                        yfill True
                        activate_sound audio.cursor 
                        text_style "white"
                        text_size 27
                        text_xalign 0.5
                
                    
                