label explore_bookshop:
    scene library with fade
    "我推开了Ascalon书店的大玻璃门。"
    "前台本还在玩手机的白色老虎因为我的开门动作而抬起头来，随后便对我露出个微笑。"
    "真是可爱的小家伙。"
    "……"
    "买些新书吧。"
    $temp = p.money
    call screen screen_explore_buybook(p)
    if temp > p.money:
        zaster"一共是这些钱哦，请保管好书籍——"
    else:
        zaster"这就要走了吗，下次再来哦。"
    s"嗯。"
    s"那个……"
    s"下次见。"
    "在对话里额外添加一些无关紧要的客套话就是我唯一能够尝试的聊天手段了，但很明显这并不会让他注意到我……"
    "或者说，我们之间好像总是隔着什么……"
    "算了，该回去了。"
    jump GoOutside_result


screen screen_explore_buybook(player):
    #tag gamegui
    use barrier(screen="screen_explore_buybook", mode=0)

    $ allbooks = list(filter(lambda x: x.__base__==BookBase, getSubclasses(Item)))
    $ allbooks.remove(ProfessionalBookWorking)
    $ allbooks.remove(ProfessionalBookWriting)
    $ allbooks.remove(ProfessionalBookSeverity)

    $ items = list(filter(lambda x: x not in [type(x) for x in list(filter(lambda x: type(x).kind=='书本', p.items))], allbooks))
    $items.sort(key=lambda x: x.id)

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
                    textbutton '{size=+10}购买书籍{/size}':
                        text_style "gameUI"
                        xoffset -5
                        yoffset -5
                        action NullAction()

                    imagebutton auto "gui/icons/task_icon/exit_%s.png":
                        xalign 1.0
                        action [Hide("screen_explore_buybook"), Return()]

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
                            use screen_explore_buybook_show(player, items)
                    
screen screen_explore_buybook_show(player, items):
    vbox:
        xsize 640
        vbox:
            xsize 640
            $typename = '专业类书本'
            $typei = itemKindInfo('书本', 'i')
            $typea = itemKindInfo('书本', 'a')
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
                $professBooks = [ProfessionalBookWorking, ProfessionalBookWriting, ProfessionalBookSeverity]
                for ite in professBooks:
                    frame:
                        background None
                        ysize 60
                        xfill True
                        $ite_name = ite.name
                        $money = r2(0.2 * player.price * rh(ite.id, player, 850, 1150) * 0.001)
                        $info = ite.getPrincipalInfo()
                        $ad = ite.ad
                        frame:
                            background None
                            textbutton ite_name text_style "white":
                                action [Hide("info3"),Show(screen="screen_explore_buybook_use", player=player,money=money, book=ite(player), pp=renpy.get_mouse_pos(), t=ite_name, i1=info,a1=ad)]
                                hovered [Show(screen="info3", t=ite_name, i1=info,a1=ad)]
                                unhovered Hide("info3")
                                background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                activate_sound audio.cursor
                                xfill True
                            textbutton str(money) text_style "white":
                                xpos 1.0
                                xoffset -40
                                xanchor 1.0

        null height 10

        vbox:
            xsize 640
            $typename = '未收藏的书本'
            $typei = itemKindInfo('书本', 'i')
            $typea = itemKindInfo('书本', 'a')
            hbox:
                if len(items) > 0:
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
                        if ite_name == '《不要读这本书》':
                            $ite_name = '《不要买这本书》'
                        $money = r2(0.5 * player.price * rh(ite.id, player, 700, 1500) * 0.001)
                        $info = ite.getPrincipalInfo()
                        $ad = ite.ad
                        frame:
                            background None
                            textbutton ite_name text_style "white":
                                action [Hide("info3"),Show(screen="screen_explore_buybook_use", player=player,money=money, book=ite(player), pp=renpy.get_mouse_pos(), t=ite_name, i1=info,a1=ad)]
                                hovered [Show(screen="info3", t=ite_name, i1=info,a1=ad)]
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

screen screen_explore_buybook_use(player,money, book, pp, t=None, i1=None, a1=None, i2=None, a2=None, width=400):
    default num = '1'
    style_prefix "info"
    use barrier(screen="screen_explore_buybook_use")
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
                    action [Hide("screen_explore_buybook_use"), Function(buy, player=player, item=book, nums=int(num) if num!=''else 0, money=money)]
                    activate_sound audio.cursor
                null width 40
                textbutton _("{size=-3}取消{/size}"):
                    action Hide("screen_explore_buybook_use")
                    activate_sound audio.cursor

screen screen_explore_buybook_confirm(player, i="不买了？关闭将直接离开商店。", width=400, pp=renpy.get_mouse_pos()):
    use barrier(screen="screen_explore_buybook_confirm")
    style_prefix "info"
    zorder 400
    $p = pp
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
            null height 30
            hbox:
                xalign 0.5
                spacing 40
                textbutton _("{size=-3}确定{/size}"):
                    action [Hide("screen_explore_buybook_confirm"),Return(None)]
                    activate_sound audio.cursor
                textbutton _("{size=-3}返回{/size}"):
                    action Hide("screen_explore_buybook_confirm")
                    activate_sound audio.cursor


