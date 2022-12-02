
screen screen_tr_readingbook(player):
    #tag gamegui
    use barrier(screen="screen_tr_readingbook", mode=0)

    $ items = list(filter(lambda x: type(x).kind=='书本' and type(x) not in p.itemcd, p.items))

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
                    textbutton '{size=+10}阅读书籍{/size}':
                        text_style "gameUI"
                        xoffset -5
                        yoffset -5
                        action NullAction()

                    imagebutton auto "gui/exit_%s.png":
                        xalign 1.0
                        action Show(screen="screen_tr_readingbook_confirm",player=player)

                    frame:
                        background None
                        ysize 700
                        xsize 650
                        ypos 60
                        xpos 25

                        viewport:
                            mousewheel True
                            draggable True
                            if len(player.items)>8:
                                scrollbars "vertical"
                            use screen_tr_readingbook_show(player, items)
                    

screen screen_tr_readingbook_show(player, items):
    vbox:
        xsize 640
        $typename = '当前可阅读的书本'
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
            #xalign 1.0
            for ite in items:
                frame:
                    background None
                    ysize 60
                    xfill True
                    $ite_name = ite.name
                    $ite_pre = ite.getPrefixInfo(player)
                    $ite_main = ite.getPrincipalInfo()
                    $ite_suf = ite.getSuffixInfo()

                    frame:
                        background None
                        textbutton ite_name text_style "white":
                            action [Hide("info"),Show(screen="info_confirm", text='选择',act=[Function(player.rtn, ite), Return()], pp=renpy.get_mouse_pos(), t=ite_name, i=ite_pre+'\n'+ite_main+ite_suf, a=type(ite).ad)]
                            hovered [Show(screen="info", t=ite_name, i=ite_pre+'\n'+ite_main+ite_suf, a=type(ite).ad)]
                            unhovered Hide("info")
                            background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            activate_sound audio.cursor
                            xfill True

                    null height 2
        null height 30
        textbutton ''


screen screen_tr_readingbook_confirm(player, i="确定不选择书本吗？这将会导致本日程直接结束。", width=400, pp=renpy.get_mouse_pos()):
    use barrier(screen="screen_tr_readingbook_confirm")
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
                label i:
                    text_style "info_text"
                    xsize width
            null height 30
            hbox:
                xalign 0.5
                spacing 40
                textbutton _("{size=-3}确定{/size}"):
                    action [Hide("screen_tr_readingbook_confirm"), Function(player.rtn, None),Return(None)]
                    activate_sound audio.cursor
                textbutton _("{size=-3}返回{/size}"):
                    action Hide("screen_tr_readingbook_confirm")
                    activate_sound audio.cursor


