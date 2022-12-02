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
            action Hide(screen)



screen freeze(time=None): #show screen freeze(5)
    modal True
    zorder 50
    if persistent.nowaiting == True:
        $time=0.1
    timer time:
        action Hide(screen="freeze")

    button:
        xfill True
        yfill True
        action NullAction()

screen cfreeze(time=None): #call screen freeze(5)
    modal True
    zorder 50
    if persistent.nowaiting == True:
        $time=0.1
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
    hide screen screen_index
    hide screen screen_items
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





screen screen_buylist(player, items, p, d, n=None, r=False):
    # n: 自定义类名
    # p: 相对于药价的价格，例如当p为1时，所有道具的基础价格和药价相等；当p为0.5时，所有道具的基础价格为药价的一半；当p=-1时，则使用物品的p成员变量来定义价格
    # d：浮动大小，如d为30时，相对于基础价格浮动大小为*70%~130%
    # r: 为真时，只允许购买一个物品
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
                        $ite_name = ite.name
                        if p==-1:
                            $money = r2(ite.p * player.price * rh(ite.id, player, 1000-d*10, 1000+d*10) * 0.001)
                        else:
                            $money = r2(p * player.price * rh(ite.id, player, 1000-d*10, 1000+d*10) * 0.001)
                        $info = ite.getPrincipalInfo()
                        $ad = ite.ad

                        frame:
                            background None
                            textbutton ite_name text_style "white":
                                action [Hide("info"),Show(screen="screen_buy_info", player=player,money=money, item=ite(player), pp=renpy.get_mouse_pos(), t=ite_name, i=info, a=ad, r=r)]
                                hovered [Show(screen="info", t=ite_name, i=info, a=ad)]
                                unhovered Hide("info")
                                background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                activate_sound audio.cursor
                                xfill True
                            textbutton str(money) text_style "white":
                                xpos 1.0
                                xoffset -40
                                xanchor 1.0
                        null height 2

screen screen_buy_info(player, item, money, pp, t=None, i=None, a=None, width=400,r=False):
    style_prefix "info"
    default num = '1'
    use barrier(screen="screen_buy_info")
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
            if i is not None:
                null height -8
                label '{size=-2}'+i+'{/size}':
                    text_style "info_text"
                    xsize width
            if a is not None:
                $a = '{i}' + a + '{/i}'
                null height 13
                label a:
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




screen fix_select(player):
    use barrier(screen="fix_select")
    style_prefix "info"
    zorder 400
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
    $ fixlist = list(filter(lambda x: x.kind == '收藏品' and x.id not in (622, 623, 624) and x.du < x.maxDu and not x.broken, player.items))
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
                        $du_name = '（%s / %s）' % (i.du, i.maxDu)
                        textbutton du_name text_style 'white':
                            xalign 1.0
        else:
            textbutton '{size=-5}目前还没有需要修理的道具。{/size}' text_style "white":
                action NullAction()
                xfill True
                xalign 1.0
                activate_sound audio.cursor
                xoffset -5