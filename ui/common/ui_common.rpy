screen ctc(arg=None):
    zorder 100
    add "gui/ctc.png" xalign 0.93 yalign 0.96 at ctc_bob


screen barrier(screen, mode=1):
    if mode == 0:
        button:
            xfill True
            yfill True
            action NullAction()
    else:
        button:
            xfill True
            yfill True
            action Hide(screen, transition=dissolve)
    
    key 'K_SPACE' action NullAction()
    key 'K_LCTRL' action NullAction()



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



label hide_all_screens:
    hide screen screen_dashboard
    hide screen screen_dashboard_calendar
    hide screen screen_dashboard_medicine
    hide screen screen_dashboard_severity
    hide screen screen_dashboard_abilities
    hide screen screen_dashboard_effects
    hide screen screen_effects
    hide screen screen_operate
    hide screen screen_items
    hide screen screen_objects
    hide screen screen_map
    hide screen screen_notify
    hide screen screen_phone
    hide screen screen_tasks
    hide screen info
    hide screen info2
    hide screen info3
    return

label hide_all_info:
    hide screen info
    hide screen info2
    hide screen info3
    return





screen screen_buylist(player, items, p, d, n=None, r=False, ds=True):
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
            xsize 640
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
                        ysize 60
                        xfill True
                        python:
                            ite_name = ite.name
                            if p==-1:
                                money = r2(ite.p * player.price * rh(ite.id, player, 1000-d*10, 1000+d*10) * 0.001)
                            else:
                                money = r2(p * player.price * rh(ite.id, player, 1000-d*10, 1000+d*10) * 0.001)
                            info = ite.getPrincipalInfo()
                            ad = ite.ad
                            amounts = ite.getamounts(player)
                            if amounts > 0:
                                info = _('{color=#fde827}已拥有数量：%s{/color}\n\n%s') % (amounts, info)
                            if ite.maxDu != -1:
                                info = _('%s\n\n{color=#fde827}保质期：%s天{/color}') % (info, ite.maxDu)
                            else:
                                info = _('%s\n\n{color=#fde827}不会损坏{/color}') % info
                            if ite.maxCd == 0:
                                info = _('%s\n{color=#fde827}无冷却时间{/color}') % info
                            elif ite.maxCd != -1:
                                info = _('%s\n{color=#fde827}冷却时间：%s天{/color}') % (info, ite.maxCd)

                            if config.developer:
                                info += _('\n\n折扣判定：%s') % (abs(rs(player, 1, 1000)-rh(ite.id, player, 1, 1000)))
                            
                            showmoney = str(money)

                            discount = havediscount(player, ite)
                            if discount and ds:
                                money = r2(money*discount)
                                showmoney = _('%s{color=#fde827}（-%s%s）{/color}') % (money, int(100-discount*100), '%')
                            else:
                                showmoney = str(money)
                            
                            


                        frame:
                            background None
                            textbutton ite_name text_style "white":
                                action [Hide("info"),Show(screen="screen_buy_info", player=player,money=money, item=ite(player), pp=renpy.get_mouse_pos(), t=ite_name, i=info, a=ad, r=r)]
                                hovered [Show(screen="info", t=ite_name, i=info, a=ad)]
                                unhovered Hide("info")
                                background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                activate_sound audio.cursor
                                xfill True
                            

                            textbutton str(showmoney) text_style "white":
                                xpos 1.0
                                xoffset -40
                                xanchor 1.0
                        null height 2

screen screen_buy_info(player, item, money, pp, t=None, i=None, a=None, width=400,r=False):
    style_prefix "info"
    default num = '1'
    use barrier(screen="screen_buy_info")
    if width == 400:
        if a:
            if len(i) + len(a) > 150:
                $width = 600
        else:
            if len(i) > 100:
                $width = 600
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
                label '[t!t]\n':
                    text_style "info_text"
                    xsize width
            if i is not None:
                null height -8
                label '{size=-2}'+i+'{/size}':
                    text_style "info_text"
                    xsize width
            if a is not None:
                null height 13
                label '{i}[a!t]{/i}':
                    text_style "admonition_text"
                    xsize width
            null height 30
            hbox:
                xalign 0.5
                if not item.isUnique:
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
                    if r:
                        action [Hide("screen_buy_info"), Function(buy, player=player, item=item, nums=int(num) if num!=''else 0, money=money),Return()]
                    else:
                        action [Hide("screen_buy_info"), Function(buy, player=player, item=item, nums=int(num) if num!=''else 0, money=money)]
                    activate_sound audio.cursor
                null width 40
                textbutton _("{size=-3}取消{/size}"):
                    action Hide("screen_buy_info")
                    activate_sound audio.cursor


screen screen_teststore(player):
    use barrier(screen="screen_teststore", mode=0)

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
                    textbutton _('{size=+10}测试商店{/size}'):
                        text_style "gameUI"
                        xoffset -5
                        yoffset -5
                        action NullAction()

                    imagebutton auto "gui/exit_%s.png":
                        xalign 1.0
                        action [Hide("screen_teststore"), Return()]

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
                                use screen_buylist(player, ALLITEMS, p=1.0, d=20, n=_('测试商品'))
                                null height 30
                                textbutton ''


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
    $ fixlist = list(filter(lambda x: x.kind == _('收藏品') and x.id not in (622, 623, 624) and x.du < x.maxDu and not x.broken, player.items))
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
                            background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
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
                            action [Function(fridge.take, player, i),Hide('info')]
                            background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            xfill True
                            activate_sound audio.cursor
                        $du_name = _('新鲜度：（%s / %s）') % (fridge.items[i].du, fridge.items[i].maxDu)
                        textbutton du_name text_style 'white':
                            xalign 1.0
                    else:
                        textbutton _('空位置') text_style 'white':
                            action [Show(screen='fridge_select', player=player, fridge=fridge, poz=i),Hide('info')]
                            background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
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
                            background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
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