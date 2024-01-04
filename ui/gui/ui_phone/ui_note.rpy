screen screen_phone_note(player):

    predict False
    style_prefix "gameUI"
    zorder 600

    default status = Stat.stato_check(player)
    default page = 0
    
    frame:
        
        if phone_page == 8:
            at app_inner_show(0, 50)
        else:
            at app_inner_hide(0, 50)
        

        
        background None
        xcenter 0.5
        ycenter 0.5
        yoffset -10
        
        use barrier('', 0)

        add "gui/phone/wallpaper/camera.webp":
            xcenter 0.5

        if page == 0:
            text "统计" xpos 0.92 xanchor 1.0 ypos 0.085 size 40 style "phonew"
        elif page == 1:
            text "本局统计" xpos 0.92 xanchor 1.0 ypos 0.085 size 40 style "phonew"
        elif page == 2:
            text "全局统计" xpos 0.92 xanchor 1.0 ypos 0.085 size 40 style "phonew"

        frame:
            
            background None
            xalign 0.5
            ypos 150
            ysize 800
            xsize 582
            

            if page == 0:
                vbox:
                    spacing 30
                    xalign 0.5
                    null height 10
                    frame:
                        background None
                        xsize 449
                        ysize 200
                        xalign 0.5
                        
                        button:
                            at app_transform
                            background Frame('#bebebe')
                            xfill True
                            yfill True
                            action SetLocalVariable("page", 1)
                            xalign 0.5
                            yalign 0.5
                        text '本局游戏统计':
                            style 'foodname'
                            xalign 0.5
                            size 60

                    frame:
                        background None
                        xsize 449
                        ysize 200
                        xalign 0.5
                        
                        
                        button:
                            at app_transform
                            background Frame('#bebebe')
                            action SetLocalVariable("page", 2)
                            xfill True
                            yfill True
                            xalign 0.5
                            yalign 0.5
                        text '全局游戏统计':
                            style 'foodname'
                            xalign 0.5
                            size 60

            else:

                viewport:
                    xcenter 0.5
                    mousewheel True
                    draggable True
                    scrollbars "vertical"

                    frame:
                        background None
                        xsize 540
                    
                        vbox:
                            spacing 15
                            
                            if page == 1:
                                use screen_stato(player.LocalStatisticso)

                                use screen_stat(player.LocalStatistics)
                            if page == 2:
                                use screen_stato(persistent.GlobalStatisticso)
                                use screen_stat(persistent.GlobalStatistics)
                        
                            null height 300
                                


        frame:
            background None
            xpos 0.03
            ypos 0.06
            imagebutton auto "gui/phone/backw_%s.png":
                if page == 0:
                    action SetVariable("phone_page", 0), Hide("info")
                else:
                    action SetLocalVariable("page", 0), Hide("info")
                hover_sound audio.cursor
            

                
    
    key 'K_ESCAPE' action SetVariable("phone_page", 0), Hide("info")


screen screen_stat(stat):

    default items = Stat.get(stat)

    if not stat:
        text _('暂无可用数据') style "phonew":
            xfill True
    else:

        vbox:
            for i in items:

                text Stat.basenames[Stat.getbase(i[0][0]).__name__][1] style "phonew":
                    xfill True
                    size 20

                for j in i:

                    frame:
                        background None
                        ysize 50
                        textbutton '':
                            xsize (515 * j[1] / i[0][1])
                            background Frame('#bebebe')
                            text_size 40
                            ysize 45
                            yalign 0.5

                        text str(j[1]) style "white":
                            xalign 0.975
                            yalign 0.5

                        text j[0].name style "white":
                            xalign 0.02
                            yalign 0.5
                null height 10

screen screen_stato(stat):
    

    if stat:
        
        vbox:
            spacing 5
            text '整体' style "phonew":
                xfill True
                size 20

            use screen_stato_block(stat, '+精神状态', 'rec')
            use screen_stato_block(stat, '-精神状态', 'con')
            use screen_stato_block(stat, '+工作能力', 'worup')
            use screen_stato_block(stat, '-工作能力', 'wordown')
            use screen_stato_block(stat, '+写作技巧', 'wriup')
            use screen_stato_block(stat, '-写作技巧', 'wridown')
            use screen_stato_block(stat, '+身体素质', 'phyup')
            use screen_stato_block(stat, '-身体素质', 'phydown')
            use screen_stato_block(stat, '+严重程度', 'sevup')
            use screen_stato_block(stat, '-严重程度', 'sevdown')
            

                  

screen screen_stato_block(stat, name, key):
    if key in stat:
        frame:
            background None
            ysize 40

            textbutton name text_style "phonew":
                yalign 0.5
                xfill True

            text str(stat[key]) style "phonew":
                xalign 0.975
                yalign 0.5
                