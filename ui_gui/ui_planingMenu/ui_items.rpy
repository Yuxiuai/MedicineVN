screen screen_items(player):
    #tag gamegui
    use barrier(screen="screen_items")

    $ items = sliceArr(player.items)

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
                    textbutton '{size=+10}库存{/size}':
                        text_style "gameUI"
                        xoffset -5
                        yoffset -5
                        action NullAction()

                    imagebutton auto "gui/icons/task_icon/exit_%s.png":
                        xalign 1.0
                        action [Hide("screen_items",transition=dissolve),Hide("info"),Hide("info3")]
                        #alternate Function(allI, player=player)

                    frame:
                        background None
                        ysize 700
                        xsize 650
                        ypos 60
                        xpos 25

                        viewport:
                            mousewheel True
                            draggable True
                            if len(player.items)>7:
                                scrollbars "vertical"
                            use items_show(player, items)
    
    key 'K_ESCAPE' action [Hide("screen_items",transition=dissolve),Hide("info"),Hide("info3")]
    key 'q' action [Hide("screen_items",transition=dissolve),Hide("info"),Hide("info3")]
    key 'w' action [Hide("screen_items",transition=dissolve),Hide("info"),Hide("info3")]
    key 'e' action [Hide("screen_items",transition=dissolve),Hide("info"),Hide("info3")]
    key 'r' action [Hide("screen_items",transition=dissolve),Hide("info"),Hide("info3")]
                    

screen items_show(player, items):
    vbox:
        xsize 640
        default isFold = {
            '实验药物':False,
            '普通药物':False,
            '书本':False,
            '手稿':False,
            '食物':False,
            '收藏品':False,
            '文稿':False
        }
        for i in items:
            $typename = type(i[0]).kind
            $typei = itemKindInfo(typename, 'i')
            $typea = itemKindInfo(typename, 'a')
            hbox:
                if isFold[typename] == False:
                    textbutton '{size=-5}'+typename+'{/size}' text_style "white":
                        action [SetDict(isFold, typename, True),Hide("info")]
                        hovered Show(screen="info", i=typei+'\n\n单击以折叠该类物品。', a=typea)
                        unhovered Hide("info")
                        xfill True
                        xalign 1.0
                        xoffset -5
                        activate_sound audio.cursor
                        #background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)

                    imagebutton idle "gui/style/folded.png":
                        xoffset -85
                        yoffset 10

                else:

                    textbutton '{size=-5}'+typename+'{/size}' text_style "white":
                        action [SetDict(isFold, typename, False),Hide("info")]
                        hovered Show(screen="info", i=typei+'\n\n单击以展开该类物品。', a=typea)
                        unhovered Hide("info")
                        xfill True
                        xalign 1.0
                        xoffset -5
                        activate_sound audio.cursor
                        #background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)

                    imagebutton idle "gui/style/folded.png":
                        xoffset -85
                        yoffset 10
                        at reverse
            if isFold[typename] == False:
                vbox:
                    #xalign 1.0
                    for ite in i:
                        frame:
                            background None
                            ysize 60
                            xfill True
                            $ite_name = type(ite).name
                            $ite_pre = ite.getPrefixInfo()
                            $ite_main = ite.getPrincipalInfo()
                            if type(ite).kind == '实验药物':
                                $ite_main += type(ite).getBenefit(player)
                            $ite_suf = ite.getSuffixInfo()
                            $ite_ad = type(ite).ad if type(ite) not in (FinishedCommission, UnfinishedCommission) else ite.comm.inputs
                            if ite_ad is None:
                                $ite_ad = ''

                            frame:
                                background None
                                textbutton ite_name text_style "white":
                                    action [Hide("info3"),Show(screen="item_use", player=player, item=ite, pp=renpy.get_mouse_pos(), t=ite_name, i1=ite_pre, i2='\n'+ite_main+ite_suf, a2=ite_ad)]
                                    hovered [Show(screen="info3", t=ite_name, i1=ite_pre, i2='\n'+ite_main+ite_suf, a2=ite_ad)]
                                    unhovered Hide("info3")
                                    background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                    activate_sound audio.cursor
                                    xfill True
                                textbutton str(ite.amounts) text_style "white":
                                    xpos 1.0
                                    xoffset -40
                                    xanchor 1.0

                        null height 2
        null height 30
        textbutton ''

screen item_use(player, item, pp, t=None, i1=None, a1=None, i2=None, a2=None, width=400):
    style_prefix "info"
    use barrier(screen="item_use")
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
                spacing 40
            
                if BookQuickReadEffect.has(player) and player.canRead >= 0 and type(item).kind == '书本':
                    textbutton _("{color=#ffff00}{size=-3}速读{/size}{/color}"):
                        action [Hide("item_use"), Function(ui_itemUse, item=item, player=player)]
                        activate_sound audio.cursor
                else:
                    textbutton _("{size=-3}使用{/size}"):
                        action [Hide("item_use"), Function(ui_itemUse, item=item, player=player)]
                        activate_sound audio.cursor
                    
                if type(item)==FinishedCommission:
                    textbutton _("{size=-3}发布到公众平台{/size}"):
                        action [Hide("item_use"), Function(item.uploadToSocial, player=player)]
                        activate_sound audio.cursor
                textbutton _("{size=-3}丢弃{/size}"):
                    action [Hide("item_use"), Function(ui_itemQuit, item=item, player=player)]
                    activate_sound audio.cursor
                textbutton _("{size=-3}取消{/size}"):
                    action Hide("item_use")
                    activate_sound audio.cursor

    key 'K_ESCAPE' action Hide("item_use")
