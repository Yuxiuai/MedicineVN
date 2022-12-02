
screen screen_phone_pic_address(player):
    #tag gamegui
    modal True
    style_prefix "gameUI"
    zorder 100
    

    frame:
        at trans_app(-40, 50)
        background None
        xalign 0.5
        yalign 0.5
        ysize 750
        xsize 400

        add "gui/phone/address/address.png":
            xcenter 0.51
            ycenter 0.46

        frame:
            ypos 90
            background None
            vbox:
                spacing 2
                if config.developer:
                    frame:
                        ysize 75
                        xfill True
                        background None
                        $sol_i = '存有我自己照片的文件夹'
                        $sol_a = '……虽然我倒是偶尔会搞几张自拍给别人看啦。'
                        imagebutton idle "gui/phone/address/Solitus.png":
                            action [Hide("info"),Hide("screen_phone_pic_address"),Hide("screen_phone_bg"),Show(screen="screen_phone_pic_show",who='solitus', player=player)]
                            hovered Show(screen="info", i=sol_i, a=sol_a)
                            unhovered Hide("info")  
                            background Frame("gui/style/white_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            activate_sound audio.cursor
                            xfill True
                            yalign 0.5
                        textbutton _("Solitus"):
                            xpos 0.25
                            hover_sound audio.cursor
                            text_style "white"
                            yalign 0.5
                                
                    null height 2

                frame:
                    ysize 75
                    xfill True
                    background None
                    $pa_i = '存有Pathos私密照片的隐藏文件夹'
                    $pa_a = '原来白大褂下面的是……色情的双丁！？'
                    $pa_i_locked = pa_i + '\n\n完成真结局后解锁'
                    $pa_a_locked = '原来白大褂下面的是……'
                    imagebutton idle "gui/phone/address/Pathos.png":
                        if Achievement401.has() or config.developer:
                            action [Hide("info"),Hide("screen_phone_pic_address"),Hide("screen_phone_bg"),Show(screen="screen_phone_pic_show",who='pathos', player=player)]
                            hovered Show(screen="info", i=pa_i, a=pa_a)
                        else:
                            action [Hide("info"),Show(screen="info_use", pp=renpy.get_mouse_pos(), i=pa_i_locked, a=pa_a_locked)]
                            hovered Show(screen="info", i=pa_i_locked, a=pa_a_locked)
                        unhovered Hide("info")  
                        background Frame("gui/style/white_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                        activate_sound audio.cursor
                        xfill True
                        yalign 0.5
                    textbutton _("Pathos"):
                        xpos 0.25
                        hover_sound audio.cursor
                        text_style "white"
                        yalign 0.5
                            
                null height 2

                frame:
                    ysize 75
                    xfill True
                    background None
                    $aco_i = '存有Acolas私密照片的隐藏文件夹'
                    $aco_a = '果然……这鼓胀的裆部之下……硬起来肯定有20cm多吧？'
                    $aco_i_locked = aco_i + '\n\n与Acolas完成任意结局后解锁'
                    $aco_a_locked = '果然……这鼓胀的……'
                    imagebutton idle "gui/phone/address/Acolas.png":
                        if Achievement501.has() or config.developer:
                            action [Hide("info"),Hide("screen_phone_pic_address"),Hide("screen_phone_bg"),Show(screen="screen_phone_pic_show",who='acolas', player=player)]
                            hovered Show(screen="info", i=aco_i, a=aco_a)
                        else:
                            action [Hide("info"),Show(screen="info_use", pp=renpy.get_mouse_pos(), i=aco_i_locked, a=aco_a_locked)]
                            hovered Show(screen="info", i=aco_i_locked, a=aco_a_locked)
                        unhovered Hide("info")  
                        background Frame("gui/style/white_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                        activate_sound audio.cursor
                        xfill True
                        yalign 0.5
                    textbutton _("Acolas"):
                        xpos 0.25
                        hover_sound audio.cursor
                        text_style "white"
                        yalign 0.5

                null height 2

                frame:
                    ysize 75
                    xfill True
                    background None
                    $hal_i = '存有Halluke私密照片的隐藏文件夹'
                    $hal_a = '居然拍到了尿尿的场景……也太色了！'
                    $hal_i_locked = hal_i + '\n\n与Halluke完成任意结局后解锁'
                    $hal_a_locked = '居然拍到了……'
                    imagebutton idle "gui/phone/address/Halluke.png":
                        if Achievement502.has() or config.developer:
                            action [Hide("info"),Hide("screen_phone_pic_address"),Hide("screen_phone_bg"),Show(screen="screen_phone_pic_show",who='halluke', player=player)]
                            hovered Show(screen="info", i=hal_i, a=hal_a)
                        else:
                            action [Hide("info"),Show(screen="info_use", pp=renpy.get_mouse_pos(), i=hal_i_locked, a=hal_a_locked)]
                            hovered Show(screen="info", i=hal_i_locked, a=hal_a_locked)
                        unhovered Hide("info")  
                        background Frame("gui/style/white_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                        activate_sound audio.cursor
                        xfill True
                        yalign 0.5
                    textbutton _("Halluke"):
                        xpos 0.25
                        hover_sound audio.cursor
                        text_style "white"
                        yalign 0.5

                null height 2

                frame:
                    ysize 75
                    xfill True
                    background None
                    $dep_i = '存有？？？私密照片的隐藏文件夹\n（当前版本尚未开放）'
                    $dep_a = '……'
                    $dep_i_locked = dep_i + '\n\n与？？？完成任意结局后解锁'
                    $dep_a_locked = '……'
                    imagebutton idle "gui/phone/address/Depline.png":
                        if persistent.DeplineEnding:
                            action [Hide("info"),Hide("screen_phone_pic_address"),Hide("screen_phone_bg"),Show(screen="screen_phone_pic_show",who='depline', player=player)]
                            hovered Show(screen="info", i=dep_i, a=dep_a)
                        else:
                            action [Hide("info"),Show(screen="info_use", pp=renpy.get_mouse_pos(), i=dep_i_locked, a=dep_a_locked)]
                            hovered Show(screen="info", i=dep_i_locked, a=dep_a_locked)
                        unhovered Hide("info")  
                        background Frame("gui/style/white_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                        activate_sound audio.cursor
                        xfill True
                        yalign 0.5
                    textbutton _("？？？"):
                        xpos 0.25
                        hover_sound audio.cursor
                        text_style "white"
                        yalign 0.5



        frame:
            background None
            xpos 0.8
            ypos 0.83
            imagebutton auto "gui/phone/back_%s.png":
                action [Hide("screen_phone_pic_address"),Hide("info"),Show(screen="screen_phone", player=player)]
                hover_sound audio.cursor

    key 'K_ESCAPE' action [Hide("screen_phone_pic_address"),Hide("info"),Show(screen="screen_phone", player=player)]


screen screen_phone_pic_show(player, who='pathos'):

    #tag gamegui
    modal True
    style_prefix "gameUI"
    zorder 100
    drag:
        xalign 0.1
        yalign 0.4
        frame:
            at trans_Down()
            background Frame("gui/style/grey_idle_background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
            ysize 750
            xsize 300
            textbutton '{color=#ffffff}'+who.capitalize()+'{/color}'

            frame:
                background None

                viewport:
                    ypos 0.09
                    ysize 650
                    mousewheel True
                    draggable True
                    scrollbars "vertical"
                    if who == 'solitus':
                        use screen_phone_pic_show_solitus(player)
                    elif who == 'pathos':
                        use screen_phone_pic_show_pathos(player)
                    elif who == 'halluke':
                        use screen_phone_pic_show_halluke(player)
                    elif who == 'acolas':
                        use screen_phone_pic_show_acolas(player)
            
            frame:
                background None
                xpos 0.6
                ypos -0.01
                imagebutton auto "gui/phone/exit__%s.png":
                    action Function(renpy.hide, who)
                    hover_sound audio.cursor

            frame:
                background None
                xpos 0.8
                ypos -0.01
                imagebutton auto "gui/phone/back__%s.png":
                    action [Hide("screen_phone_pic_show"),Hide("info"),Show("screen_phone_bg"),Show(screen="screen_phone_pic_address", player=player)]
                    hover_sound audio.cursor

    key 'K_ESCAPE' action [Hide("screen_phone_pic_show"),Hide("info"),Show("screen_phone_bg"),Show(screen="screen_phone_pic_address", player=player)]

    
screen screen_phone_pic_show_solitus(player):

    frame:
        background None
        vbox:
            xfill True
            default attrs = solitus_attrs
            default attrsD = {
                '外观':0,
                '头巾':0,
                '眉毛':0,
                '眼睛':0,
                '嘴':0,
                '眼镜':0,
                '汗液':0,
                '生气':0,
                '开心':0,
                '脸红':0,
                '眼泪':0,
                '小情绪':0,
                '符号':0
            }
            
            for i in attrs:
                hbox:
                    if i[1] == False:
                        textbutton '{size=-5}'+i[0]+'{/size}' text_style "white":
                            action Function(setfold, i, True)
                            xfill True
                            activate_sound audio.cursor
                            xoffset -8

                        imagebutton idle "gui/style/folded.png":
                            xoffset -30
                            yoffset 10
                    else:
                        textbutton '{size=-5}'+i[0]+'{/size}' text_style "white":
                            action Function(setfold, i, False)
                            xfill True
                            activate_sound audio.cursor
                            xoffset -8

                        imagebutton idle "gui/style/folded.png":
                            xoffset -30
                            yoffset 10
                            at reverse

                if i[1] == False:
                    vbox:   
                        for j in range(len(i[2])):
                            frame:
                                background None
                                ysize 60
                                xfill True
                                $attrname = i[2][j][0]
                                frame:
                                    background None
                                    textbutton attrname text_style "white":
                                        action [Function(renpy.show, 'solitus '+i[2][j][1], at_list=[truecenter]), SetDict(attrsD, i[0], j)]
                                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                        xfill True
                                        activate_sound audio.cursor
                                if attrsD[i[0]] == j:
                                    imagebutton idle "gui/phone/right_.png":
                                        xalign 0.95
                                        yoffset 6
                            null height 2
            null height 10
            textbutton ''


screen screen_phone_pic_show_pathos(player):

    frame:
        background None
        vbox:
            xfill True
            default attrs = pathos_attrs
            default attrsD = {
                '外观':0,
                '下体':0,
                '眉毛':0,
                '眼睛':0,
                '嘴':0,
                '眼镜':0,
                '听诊器':0,
                '汗液':0,
                '生气':0,
                '脸红':0
            }

            for i in attrs:
                hbox:
                    if i[1] == False:
                        textbutton '{size=-5}'+i[0]+'{/size}' text_style "white":
                            action Function(setfold, i, True)
                            xfill True
                            activate_sound audio.cursor
                            xoffset -8

                        imagebutton idle "gui/style/folded.png":
                            xoffset -30
                            yoffset 10
                    else:
                        textbutton '{size=-5}'+i[0]+'{/size}' text_style "white":
                            action Function(setfold, i, False)
                            xfill True
                            activate_sound audio.cursor
                            xoffset -8

                        imagebutton idle "gui/style/folded.png":
                            xoffset -30
                            yoffset 10
                            at reverse

                if i[1] == False:
                    vbox:   
                        for j in range(len(i[2])):
                            frame:
                                background None
                                ysize 60
                                xfill True
                                $attrname = i[2][j][0]
                                frame:
                                    background None
                                    textbutton attrname text_style "white":
                                        action [Function(renpy.show, 'pathos '+i[2][j][1]), SetDict(attrsD, i[0], j)]

                                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                        xfill True
                                        activate_sound audio.cursor
                                if attrsD[i[0]] == j:
                                    imagebutton idle "gui/phone/right_.png":
                                        xalign 0.95
                                        yoffset 6
                            null height 2
            null height 10
            textbutton ''



screen screen_phone_pic_show_halluke(player):

    frame:
        background None
        vbox:
            xfill True
            default attrs = halluke_attrs

            default attrsD = {
                '外观':0,
                '下体':0,
                '眉毛':0,
                '眼睛':0,
                '嘴':0,
                '眼镜':0,
                '汗液':0,
                '脸红':0,
                '眼泪':0,
                '尿液':0
            }

            for i in attrs:
                hbox:
                    if i[1] == False:
                        textbutton '{size=-5}'+i[0]+'{/size}' text_style "white":
                            action Function(setfold, i, True)
                            xfill True
                            activate_sound audio.cursor
                            xoffset -8

                        imagebutton idle "gui/style/folded.png":
                            xoffset -30
                            yoffset 10
                    else:
                        textbutton '{size=-5}'+i[0]+'{/size}' text_style "white":
                            action Function(setfold, i, False)
                            xfill True
                            activate_sound audio.cursor
                            xoffset -8

                        imagebutton idle "gui/style/folded.png":
                            xoffset -30
                            yoffset 10
                            at reverse

                if i[1] == False:
                    vbox:   
                        for j in range(len(i[2])):
                            frame:
                                background None
                                ysize 60
                                xfill True
                                $attrname = i[2][j][0]
                                frame:
                                    background None
                                    textbutton attrname text_style "white":
                                        action [Function(renpy.show, 'halluke '+i[2][j][1]), SetDict(attrsD, i[0], j)]
                                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                        xfill True
                                        activate_sound audio.cursor
                                if attrsD[i[0]] == j:
                                    imagebutton idle "gui/phone/right_.png":
                                        xalign 0.95
                                        yoffset 6
                            null height 2
            null height 10
            textbutton ''



screen screen_phone_pic_show_acolas(player):

    frame:
        background None
        vbox:
            xfill True
            default attrs = acolas_attrs

            default attrsD = {
                '外观':0,
                '下体':0,
                '眉毛':0,
                '眼睛':0,
                '嘴':0,
                '耳机':0,
                '手机':0,
                '汗液':0,
                '墨镜':0,
                '项链':0,
                '生气':0,
                '眼泪':0,
                '脸红':0
            }

            for i in attrs:
                hbox:
                    if i[1] == False:
                        textbutton '{size=-5}'+i[0]+'{/size}' text_style "white":
                            action Function(setfold, i, True)
                            xfill True
                            activate_sound audio.cursor
                            xoffset -8

                        imagebutton idle "gui/style/folded.png":
                            xoffset -30
                            yoffset 10
                    else:
                        textbutton '{size=-5}'+i[0]+'{/size}' text_style "white":
                            action Function(setfold, i, False)
                            xfill True
                            activate_sound audio.cursor
                            xoffset -8

                        imagebutton idle "gui/style/folded.png":
                            xoffset -30
                            yoffset 10
                            at reverse

                if i[1] == False:
                    vbox:   
                        for j in range(len(i[2])):
                            frame:
                                background None
                                ysize 60
                                xfill True
                                $attrname = i[2][j][0]
                                frame:
                                    background None
                                    textbutton attrname text_style "white":
                                        action [Function(renpy.show, 'acolas '+i[2][j][1]), SetDict(attrsD, i[0], j)]
                                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                        xfill True
                                        activate_sound audio.cursor
                                if attrsD[i[0]] == j:
                                    imagebutton idle "gui/phone/right_.png":
                                        xalign 0.95
                                        yoffset 6
                            null height 2
            null height 10
            textbutton ''