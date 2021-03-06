screen screen_phone_commission(player):
    #tag gamegui
    modal True

    default page = 'receive'
    
    style_prefix "gameUI"
    zorder 100
    frame:
        at trans_app(-150, 170)
        background None
        xcenter 0.5
        ycenter 0.5
        ysize 750
        xsize 400
        
        add "gui/phone/phone_desktop_.png":
            xcenter 0.51
            ycenter 0.46
        
    
        if page == 'receive':
            frame:
                at trans_toRight()
                #use screen_phone_bg_
                background None
                xcenter 0.5
                ycenter 0.5
                ysize 750
                xsize 400
                frame:
                    background None
                    #xpos 0.41
                    frame:
                        background None
                        ypos 0.2
                        ysize 80
                        xfill True
                        vbox:
                            text _("{size=+5}欢迎您！作家Solitus！{/size}") style "white"
                            if len(player.unacComm)>0:
                                text _("{size=-5}以下是本日平台用户向您发送的写作委托：{/size}") style "white"
                            else:
                                text _("{size=-5}本日还没有平台用户向您发送任何写作委托。{/size}") style "white"
                if config.developer==True: 
                    imagebutton idle "gui/reset_w.png":
                        action Function(player.refreshUnacComm)
                        #action Function(sp_comm_1)
                        hover_sound audio.cursor
                        xpos 0.85
                        ypos 0.05
                frame:
                    background None
                    ypos 0.16
                    vbox:
                        spacing 2
                        for i in player.unacComm:
                            textbutton i.name:
                                action Show(screen="ucomm_use", player=player, item=i, pp=renpy.get_mouse_pos(),i=i.commInfo())
                                hover_sound audio.cursor
                                hovered Show(screen="info",i=i.commInfo())
                                unhovered Hide("info")  
                                background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                text_style "white"
                                xfill True



                frame:
                    background None
                    ypos 0.83
                    xfill True
                    ysize 50
                    
                    hbox:
                        xalign 0.5
                        spacing 4
                        textbutton '     接稿':
                            action NullAction()
                            hover_sound audio.cursor
                            background Frame("gui/style/grey_s_hover_background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            text_style "white"
                            xsize 120
                            yfill True
                        
                        textbutton '     交稿':
                            action SetLocalVariable("page", 'submission')
                            hover_sound audio.cursor 
                            background Frame("gui/style/grey_s_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            text_style "white"
                            xsize 120
                            yfill True
                        
                        textbutton '     退出':
                            action [Hide("screen_phone_commission"),Hide("info"),Show(screen="screen_phone", player=player)]
                            hover_sound audio.cursor 
                            background Frame("gui/style/grey_s_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            text_style "white"
                            xsize 120
                            yfill True

        if page == 'submission':
            $ comms = list(filter(lambda x: type(x)==UnfinishedCommission or type(x)==FinishedCommission, player.items))
            frame:
                at trans_toLeft()
                #use screen_phone_bg_
                background None
                xcenter 0.5
                ycenter 0.5
                ysize 750
                xsize 400
                frame:
                    background None
                    #xpos 0.41
                    frame:
                        background None
                        ypos 0.5
                        ysize 80
                        xfill True
                        vbox:
                            if len(comms)>0:
                                text _("{size=+5}以下是您已接取的委托：{/size}") style "white"
                            else:
                                text _("{size=+5}您还没有接委托哦。\n请先在接稿侧接取委托吧！{/size}") style "white"
                if len(comms)>0:
                    frame:
                        background None
                        ypos 0.16
                        viewport:
                            ysize 475
                            mousewheel True
                            draggable True
                            if len(comms)>10:
                                scrollbars "vertical"
                            vbox:
                                spacing 2
                                for i in comms:
                                    textbutton i.comm.name:
                                        action Show(screen="comm_use", player=player, item=i, pp=renpy.get_mouse_pos(),i=i.getPrincipalInfo())
                                        hover_sound audio.cursor
                                        hovered Show(screen="info",i=i.getPrincipalInfo())
                                        unhovered Hide("info")  
                                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                        text_style "white"
                                        xfill True



                frame:
                    background None
                    ypos 0.83
                    xfill True
                    ysize 50
                    
                    hbox:
                        xalign 0.5
                        spacing 4

                        textbutton '     接稿':
                            action SetLocalVariable("page", 'receive')
                            hover_sound audio.cursor 
                            background Frame("gui/style/grey_s_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            text_style "white"
                            xsize 120
                            yfill True

                        textbutton '     交稿':
                            action NullAction()
                            hover_sound audio.cursor 
                            background Frame("gui/style/grey_s_hover_background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            text_style "white"
                            xsize 120
                            yfill True
                            

                        textbutton '     退出':
                            action [Hide("screen_phone_commission"),Hide("info"),Show(screen="screen_phone", player=player)]
                            hover_sound audio.cursor
                            background Frame("gui/style/grey_s_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            text_style "white"
                            #xalign 0.5
                            xsize 120
                            yfill True
    key 'K_ESCAPE' action [Hide("screen_phone_commission"),Hide("info"),Show(screen="screen_phone", player=player)]

screen ucomm_use(player, item, i=None, a=None, width=400, pp=renpy.get_mouse_pos()):
    use barrier(screen="ucomm_use")
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
                textbutton _("{size=-3}接稿{/size}"):
                    action [Hide("ucomm_use"), Function(player.receiveComm, comm=item)]
                    activate_sound audio.cursor
                textbutton _("{size=-3}返回{/size}"):
                    action Hide("ucomm_use")
                    activate_sound audio.cursor
    
    key 'K_ESCAPE' action Hide("ucomm_use")

screen comm_use(player, item, i=None, a=None, width=400, pp=renpy.get_mouse_pos()):
    use barrier(screen="comm_use")
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
                if type(item)==FinishedCommission:
                    textbutton _("{size=-3}交稿{/size}"):
                        action [Hide("comm_use"), Function(item.getReward, player=player)]
                        activate_sound audio.cursor
                    textbutton _("{size=-3}发布到公众平台{/size}"):
                        action [Hide("comm_use"), Function(item.uploadToSocial, player=player)]
                        activate_sound audio.cursor
                if type(item)==UnfinishedCommission:
                    textbutton _("{size=-3}放弃委托{/size}"):
                        action [Hide("comm_use"), Function(ui_itemQuit, item=item, player=player)]
                        activate_sound audio.cursor
                textbutton _("{size=-3}返回{/size}"):
                    action Hide("comm_use")
                    activate_sound audio.cursor

    key 'K_ESCAPE' action Hide("comm_use")