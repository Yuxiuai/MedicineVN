init python:
    def phone_levi_feed(player):
        player.levi_hunger = min(100, rd(30, 50)+player.levi_hunger)

    def phone_levi_play(player):
        player.levi_joy = min(100, rd(15, 30)+player.levi_joy)

transform phone_levi_wandering():
    xoffset 0
    yoffset 0
    xzoom 1.0
    choice:
        linear rd(50, 300)* 0.01 xoffset -rd(20, 240)
        easein 0.5 xzoom -1.0
        linear rd(50, 300)* 0.01 xoffset rd(20, 240)
        easein 0.5 xzoom 1.0
        linear rd(50, 300)* 0.01 xoffset 0
    choice:
        parallel:
            linear 0.5 xoffset -rd(20, 240)
        parallel:
            easein 0.25 yoffset -rd(20, 100)
            easeout 0.25 yoffset 0
        easein 0.5 xzoom -1.0
        linear 0.5 xoffset 0
        easein 0.5 xzoom 1.0

    choice:
        easein 0.5 xzoom -1.0
        parallel:
            linear 0.5 xoffset rd(20, 240)
        parallel:
            easeout 0.25 yoffset -rd(20, 100)
            easeout 0.25 yoffset 0
        easein 0.5 xzoom 1.0
        linear 0.5 xoffset 0
    choice:
        rd(10, 200) * 0.01
    repeat


transform phone_levi_food():
    alpha 1.0
    xoffset 0
    yoffset 0
    parallel:
        easein 0.5 xoffset rd(-200, 200)
    parallel:
        easeout 0.5 yoffset -220
    0.25
    easein 0.75 alpha 0.0
    xoffset 0
    yoffset 0
    easein 0.5 alpha 1.0
    


screen phone_levi_say(mode=0):
    zorder 3000
    $says = [
        ["别摸啦！","吃的呢？","呼噜呼噜","……喵嗷……","再摸就生气了……","喵喵喵……","嗷……","你知道我是谁么！",],
        ["再来点……","不错的食物……","我来尝尝味道……","好吃……","嗝~","（嚼嚼嚼）……"],
        ]
    $say_xp = rd(760, 1200)
    $say_yp = rd(450, 550)
    frame at trans_Up:
        background None
        xpos say_xp
        ypos say_yp
        if say_xp > 960:
            add 'gui/game/sayr.png' at trans_Up()
        else:
            add 'gui/game/sayl.png' at trans_Up()
        frame:
            background None
            padding (10, 0)
            xsize 170
            ysize 120
            text rcd(says[mode]) style 'white' xalign 0.5
    timer 1.5:
        action Hide('phone_levi_say', transition=Dissolve(0.25))


screen screen_phone_levi(player):
    default feeding = False
    predict False
    style_prefix "gameUI"
    zorder 600
    
    python:
        def diangunsound():
            renpy.sound.play("audio/sound/diangun/%s.mp3" % rd(1, 20),channel='audio')
    
    frame:
        
        if phone_page == 2:
            at app_inner_show(-110, -65)
        else:
            at app_inner_hide(-110, -65)

        
        background None
        xcenter 0.5
        ycenter 0.5
        yoffset -10
        
        use barrier('', 0)

        add "gui/phone/wallpaper/levi.webp":
            xcenter 0.5

        frame:
            
            background None
            xalign 0.5
            yalign 0.55
            ysize 1300
            xsize 582
            frame:
                background None
                xsize 560
                ysize 400
                xcenter 0.5
                ycenter 0.4

                imagebutton idle "gui/phone/levi/leviathan.png":
                    if persistent.diangunlevi:
                        action Function(diangunsound), Show("phone_levi_say"), Function(phone_levi_play, player)
                    else:
                        action Function(CuteLeviathan), Show("phone_levi_say"), Function(phone_levi_play, player)
                    xcenter 0.5
                    yalign 1.0
                    at phone_levi_wandering

            imagebutton idle "gui/phone/levi/food.png":
                if feeding:
                    action NullAction()
                else:
                    action SetLocalVariable("feeding", True), Show(screen="phone_levi_say",mode=1)
                xcenter 0.5
                yalign 0.72
                if not feeding:
                    at app_transform
                else:
                    at phone_levi_food


            frame:
                background None
                xpos 0.03
                ypos 0.06
                imagebutton auto "gui/phone/backw_%s.png":
                    action SetVariable("phone_page", 0), Hide("phone_levi_say"), Hide("info")
                    hover_sound audio.cursor
            
            frame:
                background None
                xpos 0.47
                ypos 0.06
                yoffset -3
                vbox:
                    spacing 10
                    hbox:
                        text "饥饿值" size 25 style "phone"
                        frame:
                            background None
                            xsize 200
                            ysize 30
                            xoffset -2
                            yoffset -5
                            bar:
                                range 100
                                value player.levi_hunger
                                xsize 200
                                ysize 30
                            frame:
                                background Frame("gui/frame.png", Borders(3,3,3,3))
                                xsize 200
                                ysize 30
                            
                            at colorize('#ecad00')
                    
                    hbox:
                        text "娱乐值" size 25 style "phone"
                        frame:
                            background None
                            xsize 200
                            ysize 30
                            xoffset -2
                            yoffset -5
                            
                            bar:
                                range 100
                                value player.levi_joy
                                xsize 200
                                ysize 30
                                at colorize('#ec009d')
                            frame:
                                background Frame("gui/frame.png", Borders(3,3,3,3))
                                xsize 200
                                ysize 30

                

    if feeding:
        timer 0.5 action Play("sound", audio.itemeat)
        timer 2.05 action SetLocalVariable("feeding", False), Function(phone_levi_feed, player)


    key 'K_ESCAPE' action SetVariable("phone_page", 0), Hide("phone_levi_say"), Hide("info")