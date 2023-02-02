screen screen_items(player):
    #tag gamegui
    use barrier(screen="screen_items")

    $ items = sliceArr(player.items)

    #modal True
    zorder 600
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
                    textbutton _('{size=+10}库存{/size}'):
                        text_style "gameUI"
                        xoffset -5
                        yoffset -5
                        action NullAction()

                    imagebutton auto "gui/exit_%s.png":
                        xalign 1.0
                        action [Hide("screen_items",transition=dissolve),Hide("info")]
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
    
    key 'K_ESCAPE' action [Hide("screen_items",transition=dissolve),Hide("info")]
                    

screen items_show(player, items):
    vbox:
        xsize 640
        default isFold = {
            _('置顶'):False,
            _('实验药物'):False,
            _('普通药物'):False,
            _('书本'):False,
            _('手稿'):False,
            _('食物'):False,
            _('工具'):False,
            _('收藏品'):False,
            _('文稿'):False
        }

        $staritems = list(filter(lambda x: x.star == True, player.items))
        if len(staritems)>0:
            $typei = itemKindInfo('置顶', 'i')
            $typea = itemKindInfo('置顶', 'a')

            

            hbox:
                if isFold[_('置顶')] == False:
                    textbutton _('{size=-5}置顶{/size}') text_style "white":
                        action [SetDict(isFold, _('置顶'), True),Hide("info")]
                        hovered Show(screen="info", i=typei+_('\n\n单击以折叠该类物品。'), a=typea)
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

                    textbutton _('{size=-5}置顶{/size}') text_style "white":
                        action [SetDict(isFold, _('置顶'), False),Hide("info")]
                        hovered Show(screen="info", i=typei+_('\n\n单击以展开该类物品。'), a=typea)
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
                    
            if isFold[_('置顶')] == False:
                vbox:

                    for ite in staritems:
                        frame:
                            background None
                            ysize 60
                            xfill True
                            $showstyle = 'grey' if type(ite) in player.itemcd else "white"
                            frame:
                                background None
                                textbutton ite.name text_style showstyle:
                                    action [Hide("info"),Show(screen="item_use", player=player, item=ite, pp=renpy.get_mouse_pos())]
                                    hovered [Show(screen="info_i", player=player, item=ite)]
                                    unhovered Hide("info_i")
                                    background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                    activate_sound audio.cursor
                                    xfill True
                                textbutton str(ite.amounts) text_style showstyle:
                                    xpos 1.0
                                    xoffset -40
                                    xanchor 1.0

                        null height 2

                    


        for i in items:
            $typename = type(i[0]).kind
            $typei = itemKindInfo(typename, 'i')
            $typea = itemKindInfo(typename, 'a')
            hbox:
                if isFold[typename] == False:
                    textbutton '{size=-5}'+typename+'{/size}' text_style "white":
                        action [SetDict(isFold, typename, True),Hide("info")]
                        hovered Show(screen="info", i=typei+_('\n\n单击以折叠该类物品。'), a=typea)
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
                        hovered Show(screen="info", i=typei+_('\n\n单击以展开该类物品。'), a=typea)
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
                            $showstyle = 'grey' if type(ite) in player.itemcd else "white"
                            frame:
                                background None
                                textbutton ite.name text_style showstyle:
                                    action [Hide("info"),Show(screen="item_use", player=player, item=ite, pp=renpy.get_mouse_pos())]
                                    hovered [Show(screen="info_i", player=player, item=ite)]
                                    unhovered Hide("info_i")
                                    background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                    activate_sound audio.cursor
                                    xfill True
                                textbutton str(ite.amounts) text_style showstyle:
                                    xpos 1.0
                                    xoffset -40
                                    xanchor 1.0

                        null height 2
        null height 30
        textbutton ''

screen info_i(player, item, width=400, pp=renpy.get_mouse_pos()):
    
    style_prefix "info"
    zorder 1000

    python:
        item.name = type(item).name
        ite_pre = item.getPrefixInfo(player)
        ite_main = item.getPrincipalInfo()
        if type(item) in (MedicineA, MedicineB, MedicineC, MedicineD):
            ite_main = '%s\n\n{color=#fde827}%s{/color}' % (ite_main, type(item).getrecoveryinfo(player))
        ite_suf = item.getSuffixInfo()
        ite_ad = item.ad if type(item) not in (FinishedCommission, UnfinishedCommission) else item.comm.inputs
        if ite_ad is None:
            ite_ad = ''

        t=item.name
        i=ite_pre+'\n'+ite_main+ite_suf
        a=ite_ad

    
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
    #frame:
    #    pos pp
    #    padding (15, 15)
    #    xanchor xc
    #    yanchor yc
    #    background None
    #    at trans()
        #imagebutton idle ite.icon():
        #    xpos width - 100
    


screen item_use(player, item, pp, width=400):
    style_prefix "info"
    zorder 1000
    use barrier(screen="item_use")
    python:
        item.name = type(item).name
        ite_pre = item.getPrefixInfo(player)
        ite_main = item.getPrincipalInfo()
        if type(item) in (MedicineA, MedicineB, MedicineC, MedicineD):
            ite_main = '%s\n\n{color=#fde827}%s{/color}' % (ite_main, type(item).getrecoveryinfo(player))
        ite_suf = item.getSuffixInfo()
        ite_ad = item.ad if type(item) not in (FinishedCommission, UnfinishedCommission) else item.comm.inputs
        if ite_ad is None:
            ite_ad = ''

        t=item.name
        i=ite_pre+'\n'+ite_main+ite_suf
        a=ite_ad

    
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
        #frame:
        #    xalign 0.98
        #    yalign 0.02
        #    imagebutton idle ite.icon()

        vbox:
            align pp
            
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
                spacing 40

                if item.id in (497, 498, 499) and player.canRead >= 0 and (BookQuickReadEffect.has(player) or Relaxation.has(player)):
                    textbutton _("{color=#ffff00}{size=-3}速读{/size}{/color}"):
                        action [Hide("item_use"), Function(ui_itemUse, item=item, player=player)]
                        activate_sound audio.cursor 

                elif BookQuickReadEffect.has(player) and player.canRead >= 0 and item.kind == _('书本'):
                    textbutton _("{color=#ffff00}{size=-3}速读{/size}{/color}"):
                        action [Hide("item_use"), Function(ui_itemUse, item=item, player=player)]
                        activate_sound audio.cursor

                else:
                    textbutton _("{size=-3}使用{/size}"):
                        action [Hide("item_use"), Function(ui_itemUse, item=item, player=player)]
                        activate_sound audio.cursor
                    
                if type(item)==FinishedCommission:
                    if item.comm.freewheeling:
                        textbutton _("{size=-3}发布到公众平台{/size}"):
                            action [Hide("item_use"), Function(item.uploadToSocial, player=player)]
                            activate_sound audio.cursor
                    else:
                    
                        textbutton _("{size=-3}交稿{/size}"):
                            if item.comm.broken:
                                action [Hide("item_use"), Function(showNotice, messages=[_('委托已过期，无法交付。')])]
                            else:
                                action [Hide("item_use"), Function(item.getReward, player=player)]
                            activate_sound audio.cursor
                            
                if not item.star:
                    textbutton _("{size=-3}置顶{/size}"):
                        action [Hide("item_use"), Function(ui_itemStar, item=item)]
                        activate_sound audio.cursor
                else:
                    textbutton _("{size=-3}取消置顶{/size}"):
                        action [Hide("item_use"), Function(ui_itemUnstar, item=item)]
                        activate_sound audio.cursor

                textbutton _("{size=-3}丢弃{/size}"):
                    action [Hide("item_use"), Function(ui_itemQuit, item=item, player=player)]
                    activate_sound audio.cursor

                textbutton _("{size=-3}取消{/size}"):
                    action Hide("item_use")
                    activate_sound audio.cursor

    key 'K_ESCAPE' action Hide("item_use")
