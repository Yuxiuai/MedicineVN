
screen screen_phone_message_address(player):
    #tag gamegui
    modal True
    style_prefix "gameUI"
    zorder 100
    

    frame:
        at trans_app(-40, 280)
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

                if player.sol_p>=0:
                    frame:
                        ysize 75
                        xfill True
                        background None
                        imagebutton idle "gui/phone/address/Pathos.png":
                            action [Hide("info"),Hide("screen_phone_message_address"),Show(screen="screen_phone_message_weixin",who='Pathos', player=player), Function(Message.see, player, 'Pathos', 'Pathos')]
                            hovered Show(screen="info", i='Pathos\n总喜欢摆着臭脸但却偶尔让人觉得可爱的主治医师。', a='臭猪b，不想听到他声音。')
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
                        if Message.hasNew(player, 'Pathos'):
                            $icon = "gui/phone/message/new_%s.png"
                        else:
                            $icon = "gui/phone/message/talk_%s.png"
                        imagebutton auto icon:
                            xpos 0.82
                            hover_sound audio.cursor
                            yalign 0.7
                null height 2

                if player.aco_p>2:
                    frame:
                        ysize 75
                        xfill True
                        background None
                        imagebutton idle "gui/phone/address/Acolas.png":
                            action [Hide("info"),Hide("screen_phone_message_address"),Show(screen="screen_phone_message_weixin",who='Acolas', player=player), Function(Message.see, player, 'Acolas', 'Acolas')]
                            hovered Show(screen="info", i='Acolas\n负责很多项目的技术总监，私底下和工作中完全不同的帅气黑狼。', a='老公')
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
                        if Message.hasNew(player, 'Acolas'):
                            $icon = "gui/phone/message/new_%s.png"
                        else:
                            $icon = "gui/phone/message/talk_%s.png"
                        imagebutton auto icon:
                            xpos 0.82
                            hover_sound audio.cursor
                            yalign 0.7
                null height 2

                if player.hal_p>6:
                    frame:
                        ysize 75
                        xfill True
                        background None
                        imagebutton idle "gui/phone/address/Halluke.png":
                            action [Hide("info"),Hide("screen_phone_message_address"),Show(screen="screen_phone_message_weixin",who='Halluke', player=player), Function(Message.see, player, 'Halluke', 'Halluke')]
                            hovered Show(screen="info", i='Halluke\n就读于A市大学，不擅长表达的白熊大学生。', a='老婆')
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
                        if Message.hasNew(player, 'Halluke'):
                            $icon = "gui/phone/message/new_%s.png"
                        else:
                            $icon = "gui/phone/message/talk_%s.png"
                        imagebutton auto icon:
                            xpos 0.82
                            hover_sound audio.cursor
                            yalign 0.7
                null height 2

                if player.dep_p>10:
                    frame:
                        ysize 75
                        xfill True
                        background None
                        imagebutton idle "gui/phone/address/Depline.png":
                            action [Hide("info"),Hide("screen_phone_message_address"),Show(screen="screen_phone_message_weixin",who='Depline', player=player), Function(Message.see, player, 'Depline', 'Depline')]
                            hovered Show(screen="info", i='Depline\n莓博上的赤松Akamatsu，喜欢画画、远足的赤狐自由画师。', a='神')
                            unhovered Hide("info")  
                            background Frame("gui/style/white_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            activate_sound audio.cursor
                            xfill True
                            yalign 0.5
                        textbutton _("Depline"):
                            xpos 0.25
                            hover_sound audio.cursor
                            text_style "white"
                            yalign 0.5
                        if Message.hasNew(player, 'Depline'):
                            $icon = "gui/phone/message/new_%s.png"
                        else:
                            $icon = "gui/phone/message/talk_%s.png"
                        imagebutton auto icon:
                            xpos 0.82
                            hover_sound audio.cursor
                            yalign 0.7


        frame:
            background None
            xpos 0.8
            ypos 0.83
            imagebutton auto "gui/phone/back_%s.png":
                action [Hide("screen_phone_message_address"),Hide("info"),Show(screen="screen_phone", player=player)]
                hover_sound audio.cursor

    key 'K_ESCAPE' action [Hide("screen_phone_message_address"),Hide("info"),Show(screen="screen_phone", player=player)]





screen screen_phone_message_weixin(who, player, trans=trans_Down()):
    #tag gamegui
    modal True
    style_prefix "gameUI"
    zorder 100

    default send = ''


    frame:
        at trans
        background None
        xalign 0.5
        yalign 0.5
        ysize 750
        xsize 400

        add "gui/phone/message/weixin.png":
            xcenter 0.5
            ycenter 0.45
        
        frame:
            ypos 0.06
            xfill True
            ysize 40
            background None

            textbutton '{size=-10}{color=#000000}' + who + '{/size}{/color}':
                xalign 0.5
        frame:
            ypos 0.14
            xfill True
            ysize 450
            background None
            viewport:
                xoffset 15
                xfill True
                mousewheel True
                draggable True
                scrollbars "vertical"
                yinitial 1.0
                vbox:
                    for i in player.messages[who]:
                        if i.fro == p.name: 
                            $ali = 1.0
                        else:
                            $ali = 0.0
                        frame:
                            background None
                            xfill True
                            xpos 7
                            frame:
                                xalign ali
                                background Frame("gui/style/white_hover_background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                vbox:
                                    text '{color=#000000}{size=-17}{font=C.ttf}'+i.fro+'{/font}{/color}{/size}':
                                        xalign ali
                                    null height 1
                                    text '{color=#000000}{size=-16}'+i.what+'{/color}{/size}':
                                        xalign ali
                                    null height 5
                                    text '{color=#000000}{size=-17}'+i.info()+'{/color}{/size}':
                                        xalign ali



        frame:
            background None
            ysize 78
            xsize 650
            xpos 15
            ypos 0.77
            yoffset -3
            viewport:
                xsize 290
                mousewheel True
                draggable True
                yinitial 1.0
            
                input:
                    value ScreenVariableInputValue("send")
                    style "white"
                    xsize 290
                    xalign 0.0
                    yalign 0.0
                    length 100
                    exclude "\"\'[]{}%$@?!#^&*\(\)"

        frame:
            background None
            xpos 0.79
            ypos 0.77
            imagebutton auto "gui/phone/message/send_%s.png":
                action [Function(Message.new, player, player.name, who, send, False), Hide("screen_phone_message_weixin"), Show(screen = "screen_phone_message_weixin", who=who, player=player, trans=None)]
                hover_sound audio.cursor

        frame:
            background None
            xpos 0.01
            ypos 0.05
            imagebutton auto "gui/phone/back_%s.png":
                action [Hide("screen_phone_message_weixin"),Hide("info"),Show(screen="screen_phone_message_address", player=player), Function(Message.see, player, who, who)]
                hover_sound audio.cursor

    key 'K_RETURN' action [Function(Message.new, player, player.name, who, send, False), Hide("screen_phone_message_weixin"), Show(screen = "screen_phone_message_weixin", who=who, player=player, trans=None)]
    key 'K_KP_ENTER' action [Function(Message.new, player, player.name, who, send, False), Hide("screen_phone_message_weixin"), Show(screen = "screen_phone_message_weixin", who=who, player=player, trans=None)]
    key 'K_ESCAPE' action [Hide("screen_phone_message_weixin"),Hide("info"),Show(screen="screen_phone_message_address", player=player), Function(Message.see, player, who, who)]