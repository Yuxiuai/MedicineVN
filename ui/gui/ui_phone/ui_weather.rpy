

screen screen_phone_weather(player):


    predict False
    style_prefix "gameUI"
    zorder 600
    $weathers = player.weatherforcast()
    
    frame:
        
        if phone_page == 99:
            at app_inner_show(220, -430)
        else:
            at app_inner_hide(220, -430)

        
        background None
        xcenter 0.5
        ycenter 0.5
        yoffset -10
        
        use barrier('', 0)

        add "gui/phone/wallpaper/ruin.webp":
            xcenter 0.5

        add "gui/phone/wallpaper/%s.webp" % type(player.effects[0]).__name__:
            xcenter 0.5

        add "gui/phone/wallpaper/weathermask.webp":
            xcenter 0.5


        frame:
            background None
            
            xalign 0.5
            yalign 0.55
            ysize 1300
            xsize 582
            



            frame:
                ypos 400
                background None
                vbox:
                    for i in weathers:
                        use screen_phone_weather_label(i)
                    

            frame:
                background None
                xpos 0.03
                ypos 0.06
                imagebutton auto "gui/phone/backw_%s.png":
                    action SetVariable("phone_page", 0), Hide("info")
                    #if config.developer:
                    #    alternate Function(player.newDay)
                    hover_sound audio.cursor
                 
        

    key 'K_ESCAPE' action SetVariable("phone_page", 0), Hide("info")


screen screen_phone_weather_label(i):
    frame:
        ysize 80
        xsize 550
        background None

        text i[0]:
            yalign 0.5
            style "phonew"
            size 50
            xoffset 5
            at screen_phone_message_friendbox_transform

        text i[1].name:
            yalign 0.5
            style "phonew"
            size 50
            xoffset 435
            at screen_phone_message_friendbox_transform

