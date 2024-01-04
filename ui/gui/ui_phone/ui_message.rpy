transform screen_phone_message_friendbox_transform():
    
    on idle:
        easein 0.2 matrixcolor IdentityMatrix()
    on hover:
        easein 0.2 matrixcolor BrightnessMatrix(-0.1)

default screen_phone_message_page = 0
define screen_phone_message_i = {
    "Pathos": "总喜欢摆着臭脸的主治医师",
    "Acolas": "负责很多项目的技术总监",
    "Halluke": "就读于A市大学的白熊大学生",
    "Depline": "莓博上的大学生画师",
    "Destot": "我的实习生",
}


screen screen_phone_message(player):


    predict False
    style_prefix "gameUI"
    zorder 600
    
    $ allnotseen = 0
    


    frame:
        
        if phone_page == 12:
            at app_inner_show(-110, 230)
        else:
            at app_inner_hide(-110, 230)

        
        background None
        xcenter 0.5
        ycenter 0.5
        yoffset -10
        
        use barrier('', 0)

        add "gui/phone/wallpaper/message.webp":
            xcenter 0.5

        

        frame:
            
            background None
            xalign 0.5
            yalign 0.55
            ysize 1300
            xsize 582
            



            frame:
                ypos 150
                background None
                if screen_phone_message_page == 0:
                    vbox:
                        if player.sol_p>=0:
                            $notseen = len([mes for mes in p.messages['Pathos'] if not mes.seen and mes.fro != player.name])
                            $allnotseen += notseen
                            use screen_phone_message_friendbox(player, 'Pathos', notseen)
                        if player.aco_p>2:
                            $notseen = len([mes for mes in p.messages['Acolas'] if not mes.seen and mes.fro != player.name])
                            $allnotseen += notseen
                            use screen_phone_message_friendbox(player, 'Acolas', notseen)
                        if player.hal_p>6 and player.hal_p != 51:
                            $notseen = len([mes for mes in p.messages['Halluke'] if not mes.seen and mes.fro != player.name])
                            $allnotseen += notseen
                            if p.hal_p == 99:
                                use screen_phone_message_friendbox(player, 'Halluke', notseen, 'Halluke_')
                            else:
                                use screen_phone_message_friendbox(player, 'Halluke', notseen)
                        if player.dep_p>0:
                            use screen_phone_message_friendbox(player, 'Depline', notseen)
                        if player.des_p>=2:    
                            $notseen = len([mes for mes in p.messages['Destot'] if not mes.seen and mes.fro != player.name])
                            $allnotseen += notseen
                            use screen_phone_message_friendbox(player, 'Destot', notseen)
                else:
                    if screen_phone_message_page == 'Halluke' and p.hal_p == 99:
                        use screen_phone_message_inner(player, screen_phone_message_page, 'Halluke_')
                    else:
                        use screen_phone_message_inner(player, screen_phone_message_page)


                    




                                



            frame:
                background None
                xpos 0.03
                ypos 0.06
                imagebutton auto "gui/phone/back_%s.png":
                    if screen_phone_message_page == 0:
                        action SetVariable("phone_page", 0), Hide("info")
                    else:
                        action SetVariable("screen_phone_message_page", 0),SetVariable("screen_phone_message_send",''), Hide("info")
                    hover_sound audio.cursor
                    
        if screen_phone_message_page == 0:
            $nametext = "某信"
            if allnotseen:
                $nametext = "某信([allnotseen])"
        else:
            $nametext = screen_phone_message_page
        
        
        text nametext xpos 0.98 xanchor 1.0 ypos 0.085 size 30 style "foodname"

    if screen_phone_message_page == 0:
        key 'K_ESCAPE' action SetVariable("phone_page", 0), Hide("info")
    else:
        key 'K_ESCAPE' action SetVariable("screen_phone_message_page", 0),SetVariable("screen_phone_message_send",''), Hide("info")



screen screen_phone_message_friendbox(player, name, notseen, headname=None):
    if not headname:
        $headname = name
    frame:
        ysize 110
        xsize 550
        background None
        imagebutton idle "gui/phone/message/"+ headname +".png":
            action SetVariable("screen_phone_message_page", name), Hide("info"), Function(Message.see, player, name, name), Function(Message.messort, player, name)
            hovered Show(screen="info", i=screen_phone_message_i[name])
            unhovered Hide("info")  
            xfill True
            activate_sound audio.cursor
            background Frame("#f8f8f8")
            yalign 0.5
            xpos 5
            at screen_phone_message_friendbox_transform
        if notseen:
            text "[name]([notseen])":
                xpos 0.22
                style "foodname"
                yalign 0.0
                size 35
        else:
            text "[name]":
                xpos 0.22
                style "foodname"
                yalign 0.0
                size 35
        if Message.hasNew(player, name):
            add "gui/phone/message/point.png" xpos 95 yoffset -10
        if player.messages[name]:
            $lastmes = player.messages[name][-1].what
            $lastmes = lastmes.replace("\n", "")
            if player.messages[name][-1].fro == player.name:
                $lastmes = '我:' + lastmes
            if len(lastmes) >= 16:
                $lastmes = lastmes[:16] + "……"
        else:
            $lastmes = "你们已经是好友了，一起来聊天吧！"
        text lastmes:
            xpos 0.22
            style "phone_message"
            yalign 1.0
            size 23

transform screen_phone_message_icon():
    zoom 0.5


transform screen_phone_message_send_hide():
    xzoom 1.0
    xanchor 1.0
    easein 0.5 xzoom 0.0

default screen_phone_message_send = ''

screen screen_phone_message_inner(player, name, headname=None):
    if not headname:
        $headname = name
    $allmes = player.messages[name]
    $ya = ui.adjustment()

    viewport id "vp":
        xfill True
        ysize 700
        mousewheel True
        draggable True
        yinitial 1.0
        yadjustment ya
        vbox:
            frame:
                background None
                xfill True
                xpos 7
                frame:
                    xalign 0.5
                    background Frame("gui/style/white_hover_background.png", tile=gui.frame_tile)
                    vbox:
                        text _('{color=#000000}{size=-19}你们已经是好友了，一起来聊天吧！{/color}{/size}'):
                            xalign 0.5
            for i in allmes:
                $ali = 0.0
                $head = "gui/phone/message/"+ headname +".png"
                if i.fro == player.name:
                    $ali = 1.0
                    $head = "gui/phone/message/Solitus.png"

                frame:
                    background None
                    xfill True
                    frame:
                        xalign ali
                        background None
                        hbox:
                            box_reverse (True if i.fro == p.name else False)
                            
                            add head:
                                at screen_phone_message_icon
                                xalign ali
                            null width 10
                            vbox:
                                
                                null height 1
                                textbutton _('{color=#000000}{size=-8}[i.what]{/color}{/size}'):
                                    ypadding 10
                                    xpadding 10
                                    background Frame("gui/phone/message/green.png" if i.fro == p.name else "gui/phone/message/white.png")
                                    xalign ali
                                    xmaximum 470
                                null height 5
                                text _('{color=#000000}{size=-17}[i.info]{/color}{/size}'):
                                    xalign ali

                if i.seen == None:
                    frame:
                        background None
                        xfill True
                        xpos 7
                        frame:
                            xalign 0.5
                            background Frame("gui/style/white_hover_background.png", tile=gui.frame_tile)
                            vbox:
                                text _('{color=#000000}{size=-19}发送失败，对方已经不是您的好友。{/color}{/size}'):
                                    xalign 0.5
    hbox:
        ypos 0.58
        spacing 10

        frame:
            ysize 45
            xsize 400
            yalign 0.5
            
            background Frame("gui/phone/message/white.png")
            viewport:
                mousewheel True
                draggable True
                yinitial 1.0
            
                input:
                    value VariableInputValue("screen_phone_message_send")
                    length 45
                    exclude "\"\'[]{}%$@?!#^&*\(\)"
                    color '#000000'
                    size 30
                    copypaste True
                    
                    
        imagebutton idle "gui/phone/message/send.png":
            if screen_phone_message_send:
                action Function(Message.new, player, player.name, name, screen_phone_message_send, chachong=False, pos=''),SetVariable("screen_phone_message_send",'')
                activate_sound audio.message
            else:
                action NullAction()
                activate_sound audio.error

            yalign 0.5
            
            at app_transform


        
        imagebutton idle "gui/phone/message/random.png":
            if name in ret_mes_randomkeyword:
                action SetVariable('screen_phone_message_send', rcd(ret_mes_randomkeyword[name]))
                activate_sound audio.dice
            else:
                action NullAction()
                activate_sound audio.error
            yalign 0.5
        
    if screen_phone_message_send:
        key 'K_RETURN' action [Function(Message.new, player, player.name, name, screen_phone_message_send, chachong=False, pos=''),SetVariable("screen_phone_message_send",''), Play("audio", audio.message)]
        key 'K_KP_ENTER' action [Function(Message.new, player, player.name, name, screen_phone_message_send, chachong=False, pos=''),SetVariable("screen_phone_message_send",''), Play("audio", audio.message)]
