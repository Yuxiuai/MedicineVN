screen screen_phone_video_address(player):
    #tag gamegui
    modal True
    style_prefix "gameUI"
    zorder 100
    

    frame:
        at trans_app(70, 50)
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

                frame:
                    ysize 75
                    xfill True
                    background None
                    $sol_i = '个人剧情'
                    $sol_a = '《社畜福瑞重度头疼》'
                    imagebutton idle "gui/phone/address/Solitus.png":
                        action [Hide("info"),Hide("screen_phone_video_address"),Show(screen="screen_phone_video_show",who='solitus', player=player)]
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
                    $pa_i = '和Pathos曾发生过的故事'
                    $pa_a = '《从小白鼠到感情PUA》'
                    imagebutton idle "gui/phone/address/Pathos.png":
                        action [Hide("info"),Hide("screen_phone_video_address"),Show(screen="screen_phone_video_show",who='pathos', player=player)]
                        hovered Show(screen="info", i=pa_i, a=pa_a)
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
                    $aco_i = '和Acolas曾发生过的故事'
                    $aco_a = '《霸道总裁爱上我》'
                    imagebutton idle "gui/phone/address/Acolas.png":
                        action [Hide("info"),Hide("screen_phone_video_address"),Show(screen="screen_phone_video_show",who='acolas', player=player)]
                        hovered Show(screen="info", i=aco_i, a=aco_a)
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
                    $hal_i = '和Halluke曾发生过的故事'
                    $hal_a = '《社恐之间的交流》'
                    imagebutton idle "gui/phone/address/Halluke.png":
                        action [Hide("info"),Hide("screen_phone_video_address"),Show(screen="screen_phone_video_show",who='halluke', player=player)]
                        hovered Show(screen="info", i=hal_i, a=hal_a)
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
                    $dep_i = '和？？？曾发生过的故事\n（当前版本尚未开放）'
                    $dep_a = '……'
                    imagebutton idle "gui/phone/address/Depline.png":
                        #action [Hide("info"),Hide("screen_phone_video_address"),Show(screen="screen_phone_video_show",who='depline', player=player)]
                        action NullAction()
                        hovered Show(screen="info", i=dep_i, a=dep_a)
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
                action [Hide("screen_phone_video_address"),Hide("info"),Show(screen="screen_phone", player=player)]
                hover_sound audio.cursor

    key 'K_ESCAPE' action [Hide("screen_phone_video_address"),Hide("info"),Show(screen="screen_phone", player=player)]



        
screen screen_phone_video_show(player, who='pathos'):

    default d_routes = {
        'solitus':['第一天', '第二天', '第三天'],
        'pathos':['解锁第二种药物', '解锁第三种药物'],
        'halluke':['初次偷拍','Halluke的能力展示','厕所自慰','初次视线交汇'],
        'acolas':['电梯偶遇','性骚扰式自我介绍'],
    }

    #tag gamegui
    modal True
    style_prefix "gameUI"
    zorder 100
    frame:
        at trans_Down()
        background None
        xalign 0.5
        yalign 0.5
        ysize 750
        xsize 430
        frame:
            background Frame("gui/style/white_hover_background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
            ypos 0.05
            xpos 0.05
            xsize 380
            text _("以下为已解锁的相关剧情：") style "white"

        frame:
            background None
    
            viewport:
                ypos 0.15
                ysize 530
                mousewheel True
                draggable True
                scrollbars "vertical"
                yinitial 0.01
                use screen_phone_videos(player, who, d_routes[who])
        

        frame:
            background None
            xpos 0.8
            ypos 0.83
            imagebutton auto "gui/phone/back_%s.png":
                action [Hide("screen_phone_video_show"),Hide("info"),Show(screen="screen_phone_video_address", player=player)]
                hover_sound audio.cursor

    key 'K_ESCAPE' action [Hide("screen_phone_video_show"),Hide("info"),Show(screen="screen_phone_video_address", player=player)]


screen screen_phone_videos(player, who, routes):

    frame:
        background None
        vbox:
            xsize 370

            for i in range(len(routes)): 
                $labelname = who + '_route_' + str(i)
                if renpy.seen_label(labelname):
                    frame:
                        ysize 80
                        xsize 335
                        xpos 15
                        background Frame("gui/style/transparent.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                        textbutton routes[i] text_style "white":
                            action [SetVariable("replaying", True),Hide("screen_phone_video_show"),Hide("screen_phone_bg"),Jump(labelname)]
                            background Frame("gui/style/white_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            xfill True
                            yfill True
                            text_xoffset 85
                            activate_sound audio.cursor
                        imagebutton idle "gui/phone/video.png":
                            yalign 0.5
                            xalign 0.05
                    null height 2
            null height 10
            textbutton ''
            

