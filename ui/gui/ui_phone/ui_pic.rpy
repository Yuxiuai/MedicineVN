
screen screen_phone_pic_address(player):
    #tag gamegui
    modal True
    style_prefix "gameUI"
    zorder 600
    

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
                        $sol_i = _('存有我自己照片的文件夹')
                        $sol_a = _('……虽然我倒是偶尔会搞几张自拍给别人看啦。')
                        imagebutton idle "gui/phone/address/Solitus.png":
                            action [Hide("info"),Hide("screen_phone_pic_address"),Hide("screen_phone_bg"),Show(screen="screen_phone_pic_show",who='solitus', player=player)]
                            hovered Show(screen="info", i=sol_i, a=sol_a)
                            unhovered Hide("info")  
                            background Frame("gui/style/white_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            activate_sound audio.cursor
                            xfill True
                            yalign 0.5
                        textbutton "Solitus":
                            xpos 0.25
                            hover_sound audio.cursor
                            text_style "white"
                            yalign 0.5
                                
                    null height 2
                if Achievement402.has() or config.developer:
                    frame:
                        ysize 75
                        xfill True
                        background None
                        $pa_i = _('存有Pathos私密照片的隐藏文件夹')
                        $pa_a = _('原来白大褂下面的是……色情的双丁！？')
                        imagebutton idle "gui/phone/address/Pathos.png":
                            action [Hide("info"),Hide("screen_phone_pic_address"),Hide("screen_phone_bg"),Show(screen="screen_phone_pic_show",who='pathos', player=player)]
                            hovered Show(screen="info", i=pa_i, a=pa_a)
                            unhovered Hide("info")  
                            background Frame("gui/style/white_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            activate_sound audio.cursor
                            xfill True
                            yalign 0.5
                        textbutton "Pathos":
                            xpos 0.25
                            hover_sound audio.cursor
                            text_style "white"
                            yalign 0.5
                                
                    null height 2

                if Achievement501.has() or config.developer:
                    frame:
                        ysize 75
                        xfill True
                        background None
                        $aco_i = _('存有Acolas私密照片的隐藏文件夹')
                        $aco_a = _('果然……这鼓胀的裆部之下……硬起来肯定有20cm多吧？')
                        imagebutton idle "gui/phone/address/Acolas.png":
                            action [Hide("info"),Hide("screen_phone_pic_address"),Hide("screen_phone_bg"),Show(screen="screen_phone_pic_show",who='acolas', player=player)]
                            hovered Show(screen="info", i=aco_i, a=aco_a)
                            unhovered Hide("info")  
                            background Frame("gui/style/white_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            activate_sound audio.cursor
                            xfill True
                            yalign 0.5
                        textbutton "Acolas":
                            xpos 0.25
                            hover_sound audio.cursor
                            text_style "white"
                            yalign 0.5

                    null height 2

                if Achievement502.has() or config.developer:
                    frame:
                        ysize 75
                        xfill True
                        background None
                        $hal_i = _('存有Halluke私密照片的隐藏文件夹')
                        $hal_a = _('居然拍到了尿尿的场景……也太色了！')
                        imagebutton idle "gui/phone/address/Halluke.png":
                            action [Hide("info"),Hide("screen_phone_pic_address"),Hide("screen_phone_bg"),Show(screen="screen_phone_pic_show",who='halluke', player=player)]
                            hovered Show(screen="info", i=hal_i, a=hal_a)
                            unhovered Hide("info")  
                            background Frame("gui/style/white_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            activate_sound audio.cursor
                            xfill True
                            yalign 0.5
                        textbutton "Halluke":
                            xpos 0.25
                            hover_sound audio.cursor
                            text_style "white"
                            yalign 0.5
                    null height 2

                if False:
                    frame:
                        ysize 75
                        xfill True
                        background None
                        $dep_i = _('存有？？？私密照片的隐藏文件夹\n（当前版本尚未开放）')
                        $dep_a = _('……')
                        imagebutton idle "gui/phone/address/Depline.png":
                            action [Hide("info"),Hide("screen_phone_pic_address"),Hide("screen_phone_bg"),Show(screen="screen_phone_pic_show",who='depline', player=player)]
                            hovered Show(screen="info", i=dep_i, a=dep_a)
                            unhovered Hide("info")  
                            background Frame("gui/style/white_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            activate_sound audio.cursor
                            xfill True
                            yalign 0.5
                        textbutton "？？？":
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
    zorder 600
    drag:
        xalign 0.1
        yalign 0.4
        frame:
            at trans_Down()
            background Frame("gui/style/grey_idle_background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
            ysize 750
            xsize 300
            textbutton _('{color=#ffffff}')+who.capitalize()+_('{/color}')

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
                xpos 0.8
                ypos -0.01
                imagebutton auto "gui/phone/back__%s.png":
                    action [Hide("screen_phone_pic_show"),Hide("info"),Show("screen_phone_bg"),Show(screen="screen_phone_pic_address", player=player), Function(renpy.hide, who, 'screens')]
                    hover_sound audio.cursor

    key 'K_ESCAPE' action [Hide("screen_phone_pic_show"),Hide("info"),Show("screen_phone_bg"),Show(screen="screen_phone_pic_address", player=player)]

    
screen screen_phone_pic_show_solitus(player):

    frame:
        background None
        vbox:
            xfill True
            default attrs = solitus_attrs
            default attrsD = {
                _('外观'):0,
                _('头部'):0,
                _('眉毛'):0,
                _('眼睛'):0,
                _('嘴'):0,
                _('眼镜'):0,
                _('汗液'):0,
                _('生气'):0,
                _('开心'):0,
                _('脸红'):0,
                _('眼泪'):0,
                _('小情绪'):0,
                _('符号'):0
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
                                        action [Function(renpy.show, 'solitus '+i[2][j][1], at_list=[truecenter], layer='screens', zorder=0), SetDict(attrsD, i[0], j)]
                                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                        xfill True
                                        activate_sound audio.cursor
                                if attrsD[i[0]] == j:
                                    imagebutton idle "gui/right_.png":
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
                _('外观'):0,
                _('下体'):0,
                _('眉毛'):0,
                _('眼睛'):0,
                _('嘴'):0,
                _('眼镜'):0,
                _('听诊器'):0,
                _('汗液'):0,
                _('生气'):0,
                _('脸红'):0
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
                                        action [Function(renpy.show, 'pathos '+i[2][j][1], layer='screens', zorder=0), SetDict(attrsD, i[0], j)]

                                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                        xfill True
                                        activate_sound audio.cursor
                                if attrsD[i[0]] == j:
                                    imagebutton idle "gui/right_.png":
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
                _('外观'):0,
                _('下体'):0,
                _('眉毛'):0,
                _('眼睛'):0,
                _('嘴'):0,
                _('眼镜'):0,
                _('汗液'):0,
                _('脸红'):0,
                _('眼泪'):0,
                _('尿液'):0
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
                                        action [Function(renpy.show, 'halluke '+i[2][j][1], layer='screens', zorder=0), SetDict(attrsD, i[0], j)]
                                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                        xfill True
                                        activate_sound audio.cursor
                                if attrsD[i[0]] == j:
                                    imagebutton idle "gui/right_.png":
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
                _('外观'):0,
                _('下体'):0,
                _('眉毛'):0,
                _('眼睛'):0,
                _('嘴'):0,
                _('耳机'):0,
                _('手机'):0,
                _('汗液'):0,
                _('墨镜'):0,
                _('项链'):0,
                _('生气'):0,
                _('眼泪'):0,
                _('脸红'):0
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
                                        action [Function(renpy.show, 'acolas '+i[2][j][1], layer='screens', zorder=0), SetDict(attrsD, i[0], j)]
                                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                        xfill True
                                        activate_sound audio.cursor
                                if attrsD[i[0]] == j:
                                    imagebutton idle "gui/right_.png":
                                        xalign 0.95
                                        yoffset 6
                            null height 2
            null height 10
            textbutton ''