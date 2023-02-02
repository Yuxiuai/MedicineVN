
screen screen_phone_address(player):
    #tag gamegui
    modal True
    style_prefix "gameUI"
    zorder 600
    

    frame:
        at trans_app(-150, 280)
        background None
        xalign 0.5
        yalign 0.5
        ysize 750
        xsize 400

        #add "gui/phone/phone_desktop.png":
        #    xcenter 0.5
        #    ycenter 0.45
        add "gui/phone/address/address.png":
            xcenter 0.5
            ycenter 0.45

        #label _("{size=-10}{color=#000000}联系人"):
        #    xpos 0.41
        #    ypos 0.2

        frame:
            ypos 90
            background None
            vbox:
                spacing 2
                frame:
                    ysize 75
                    xfill True
                    background None
                    imagebutton idle "gui/phone/address/parents.png":
                        action [Hide("info"),Hide("screen_phone_address"),Show(screen="screen_phone_address_profile",who=0, player=player)]
                        hovered Show(screen="info", i=_('你的父母。\n\n虽然你们很久都不通一次电话，但如果你手头很紧，也许可以和你的父母借一点钱。'), a=_('虽然并没有发生过不好的回忆，但……'))
                        unhovered Hide("info")  
                        background Frame("gui/style/white_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                        activate_sound audio.cursor
                        xfill True
                        yalign 0.5
                    textbutton _("父母"):
                        xpos 0.25
                        hover_sound audio.cursor
                        text_style "white"
                        yalign 0.5
                null height 2

                if player.sol_p>=0:
                    frame:
                        ysize 75
                        xfill True
                        background None
                        imagebutton idle "gui/phone/address/Pathos.png":
                            action [Hide("info"),Hide("screen_phone_address"),Show(screen="screen_phone_address_profile",who=1, player=player)]
                            hovered Show(screen="info", i=_('Pathos\n总喜欢摆着臭脸但却偶尔让人觉得可爱的主治医师。'), a=_('臭猪b，不想听到他声音。'))
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

                if player.sol_p>=0:
                    frame:
                        ysize 75
                        xfill True
                        background None
                        imagebutton idle "gui/phone/address/Arnel.png":
                            action [Hide("info"),Hide("screen_phone_address"),Show(screen="screen_phone_address_profile",who=2, player=player)]
                            hovered Show(screen="info", i=_('Arnel\n经常抓你偷懒睡觉的俊俏白狼部门主管，如果需要请假就给他打电话。'), a=_('好想请假好想请假好想请假好想请假好想请假好想请假……'))
                            unhovered Hide("info")  
                            background Frame("gui/style/white_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            activate_sound audio.cursor
                            xfill True
                            yalign 0.5
                        textbutton "Arnel":
                            xpos 0.25
                            hover_sound audio.cursor
                            text_style "white"
                            yalign 0.5
                null height 2

                if player.aco_p>2:
                    frame:
                        ysize 75
                        xfill True
                        background None
                        imagebutton idle "gui/phone/address/Acolas.png":
                            action [Hide("info"),Hide("screen_phone_address"),Show(screen="screen_phone_address_profile",who=3, player=player)]
                            hovered Show(screen="info", i=_('Acolas\n负责很多项目的技术总监，私底下和工作中完全不同的帅气黑狼。'), a=_('老公'))
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

                if player.hal_p>6 and player.hal_p != 51:
                    frame:
                        ysize 75
                        xfill True
                        background None
                        imagebutton idle "gui/phone/address/Halluke.png":
                            action [Hide("info"),Hide("screen_phone_address"),Show(screen="screen_phone_address_profile",who=4, player=player)]
                            hovered Show(screen="info", i=_('Halluke\n就读于A市大学，不擅长表达的白熊大学生。'), a=_('老婆'))
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

                if player.dep_p>10:
                    frame:
                        ysize 75
                        xfill True
                        background None
                        imagebutton idle "gui/phone/address/Depline.png":
                            action [Hide("info"),Hide("screen_phone_address"),Show(screen="screen_phone_address_profile",who=5, player=player)]
                            hovered Show(screen="info", i=_('Depline\n莓博上的赤松Akamatsu，喜欢画画、远足的赤狐自由画师。'), a=_('神'))
                            unhovered Hide("info")  
                            background Frame("gui/style/white_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            activate_sound audio.cursor
                            xfill True
                            yalign 0.5
                        textbutton "Depline":
                            xpos 0.25
                            hover_sound audio.cursor
                            text_style "white"
                            yalign 0.5


        frame:
            background None
            xpos 0.8
            ypos 0.83
            imagebutton auto "gui/phone/back_%s.png":
                action [Hide("screen_phone_address"),Hide("info"),Show(screen="screen_phone", player=player)]
                hover_sound audio.cursor
    key 'K_ESCAPE' action [Hide("screen_phone_address"),Hide("info"),Show(screen="screen_phone", player=player)]





screen screen_phone_address_profile(who, player):
    #tag gamegui
    modal True
    style_prefix "gameUI"
    zorder 600

    $ infolist = [
        [_('父母'),"gui/phone/address/parents_profile.png", 'call_parents'],
        ['Pathos',"gui/phone/address/pathos_profile.png", 'call_Pathos'],
        ['Arnel',"gui/phone/address/arnel_profile.png", 'call_Arnel'],
        ['Acolas',"gui/phone/address/acolas_profile.png", 'call_Acolas'],
        ['Halluke',"gui/phone/address/halluke_profile.png", 'call_Halluke'],
        ['Depline',"gui/phone/address/depline_profile.png", 'call_Depline']
    ]
    
    #add "gui/phone/phone_desktop.png":
    #    xcenter 0.5
    #    ycenter 0.45
    

    frame:
        at trans_Down()
        background None
        xalign 0.5
        yalign 0.5
        ysize 750
        xsize 400

        add infolist[who][1]:
            xcenter 0.5
            ycenter 0.45
        
        frame:
            ypos 0.17
            xfill True
            ysize 40
            background None

            textbutton _('{size=-10}{color=#000000}') + infolist[who][0] + _('{/size}{/color}'):
                xalign 0.5
                xoffset 0.28

        frame:
            background None
            ypos 0.26
            $calllabel = infolist[who][2]
            imagebutton idle "gui/phone/address/call_btn.png":
                action [Hide("info"),Hide("screen_phone_bg"),Hide("screen_phone_address_profile"), Jump(calllabel)]
                hovered Show(screen="info", i=_('给') + infolist[who][0] + _('打电话'), width = 200)
                unhovered Hide("info")  
                background Frame("gui/style/white_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                activate_sound audio.cursor
                xfill True
                yalign 0.5
                xoffset 5

            #textbutton _('{color=ffffff}1XX XXXX XXXX') text_style "white"
                
                #imagebutton auto "gui/phone/address/call_%s.png":
                #    #action [Hide("info"),Hide("screen_phone_address_profile",transition=dissolve),Hide("screen_phone_address",transition=dissolve),Call("call_parents")]
                #    action NullAction()
                #    hover_sound audio.cursor
                #    hovered Show(screen="info", i=_('', a=')')
                #    unhovered Hide("info") 


        frame:
            background None
            xpos 0.8
            ypos 0.83
            imagebutton auto "gui/phone/back_%s.png":
                action [Hide("screen_phone_address_profile"),Hide("info"),Show(screen="screen_phone_address", player=player)]
                hover_sound audio.cursor
                
    key 'K_ESCAPE' action [Hide("screen_phone_address_profile"),Hide("info"),Show(screen="screen_phone_address", player=player)]
