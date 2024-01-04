transform screen_phone_wallpaper_locked:
    matrixcolor BrightnessMatrix(-0.2)


screen screen_phone_wallpaper(player):

    predict False
    style_prefix "gameUI"
    zorder 600
    
    default papers = [
        "wallpaper_1",
        "wallpaper_2",
        "wallpaper_3",
        "wallpaper_4",
        "wallpaper_5",
        "wallpaper_aco",
        "wallpaper_hal",
        "wallpaper_des",
        "wallpaper_ruin",
        "wallpaper_te", 
        "wallpaper_we", 
        "wallpaper_se", 
        "wallpaper_ce", 
        "wallpaper_toy", 
    ]

    default cond = {
        "wallpaper_1": [True,''],
        "wallpaper_2": [True,''],
        "wallpaper_3": [True,''],
        "wallpaper_4": [True,''],
        "wallpaper_5": [True,''],
        "wallpaper_aco": [Achievement450.has(),'只有这次我在你的身侧微笑'],
        "wallpaper_hal": [Achievement452.has(),'我知道终有一天会如愿以偿'],
        "wallpaper_des": [Achievement551.has(),'可靠的前辈'],
        "wallpaper_te": [Achievement401.has(),'如果能成为你就好了'],
        "wallpaper_ce": [Achievement402.has(),'我已经一无所有'],
        "wallpaper_se": [Achievement403.has(),'我们活在一个没有生命的茧中'],
        "wallpaper_we": [Achievement404.has(),'存在'],
        "wallpaper_ruin": [Achievement602.has(),'一首赞歌摇篮曲'],
        "wallpaper_toy": [Achievement313.has(),'最伟大的成就'],
    }

    default pos = papers.index(player.phone_wallpaper)

    python:
        
        def setwallpaper(player, wallpaper):
            player.phone_wallpaper = wallpaper

        def leftwallpaper(pos, papers):
            pos -= 1
            if pos <= -1:
                pos = len(papers)-1
            return pos

        def rightwallpaper(pos, papers):
            pos += 1
            if pos >= len(papers):
                pos = 0
            return pos


    frame:
        
        if phone_page == 13:
            at app_inner_show(0, 230)
        else:
            at app_inner_hide(0, 230)
        

        
        background None
        xcenter 0.5
        ycenter 0.5
        yoffset -10
        
        use barrier('', 0)

        
        
        if not cond[papers[pos]][0]:
            add papers[pos] xcenter 0.5:
                at screen_phone_wallpaper_locked

            vbox:
                xalign 0.5
                yalign 0.3
                text "完成成就":
                    style "phone"
                    xalign 0.5
                text "“" + cond[papers[pos]][1] + "”":
                    style "phone"
                    xalign 0.5
                text "以解锁该壁纸":
                    style "phone"
                    xalign 0.5
                    
        
        else:
            add papers[pos] xcenter 0.5



        text "更换壁纸" xpos 0.92 xanchor 1.0 ypos 0.085 size 40 style "phone"

        frame:
            
            background None
            xalign 0.5
            ypos 150
            ysize 800
            xsize 582
            

            frame:
                background None
                ypos 0.85
                xfill True
                ysize 65

                hbox:
                    xalign 0.5
                    spacing 60

                    textbutton "上一张":

                        action SetLocalVariable("pos", leftwallpaper(pos, papers))
                        text_style "phone"
                        text_size 40

                    textbutton "应用":
                        if cond[papers[pos]][0]:
                            action Function(setwallpaper, player, papers[pos]), SetVariable("phone_page", 0), Hide("info")
                        else:
                            action NullAction()
                            activate_sound audio.error
                        text_style "phone"
                        text_size 40


                    textbutton "下一张":

                        action SetLocalVariable("pos", rightwallpaper(pos, papers))
                        text_style "phone"
                        text_size 40

                    
                        

                    
                                


        frame:
            background None
            xpos 0.03
            ypos 0.06
            imagebutton auto "gui/phone/backw_%s.png":
                action SetVariable("phone_page", 0), Hide("info")
                hover_sound audio.cursor
            
    
    key 'K_ESCAPE' action SetVariable("phone_page", 0), Hide("info")