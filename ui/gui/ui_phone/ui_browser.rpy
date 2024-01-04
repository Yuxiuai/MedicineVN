screen screen_phone_browser(player):

    predict False
    style_prefix "gameUI"
    zorder 600
    

    default page = 0
    frame:
        
        if phone_page == 14:
            at app_inner_show(110, 230)
        else:
            at app_inner_hide(110, 230)
        

        
        background None
        xcenter 0.5
        ycenter 0.5
        yoffset -10
        
        use barrier('', 0)

        add "gui/phone/wallpaper/camera.webp":
            xcenter 0.5

        text "图鉴" xpos 0.92 xanchor 1.0 ypos 0.07 size 40 style "phonew"

        frame:
            
            background None
            xalign 0.5
            ypos 150
            ysize 800
            xsize 582
            
            viewport:
                xcenter 0.5
                mousewheel True
                draggable True
                scrollbars "vertical"

                frame:
                    background None
                    xsize 540
                    

                    
                        

                    vbox:
                        vbox:
                            spacing 10
                            text _('{size=-5}状态图鉴{/size}') style "white":
                                xfill True
                            frame:
                                background None
                                ysize 50
                                bar:
                                    value len(GuideE.done())
                                    range len(ALLEFFECTS)
                                    xfill True
                                    ysize 50
                                    yalign 0.5
                                text _("解锁进度") style 'white':
                                    xfill True
                                    yalign 0.5
                                    xoffset 10
                                text _('%s / %s') % (len(GuideE.done()), len(ALLEFFECTS)) style 'white':
                                    xalign 0.975
                                    yalign 1.0

                            null height 5

                            if GuideE.done():
                                text _('{size=-5}已获得过的状态{/size}') style "white":
                                    xfill True
                                

                            for i in GuideE.done():
                                frame:
                                    background None
                                    ysize 100
                                    
                                    textbutton i.name text_style 'white':
                                        action NullAction()
                                        hovered Show(screen="info", i=i.info, a=i.ad)
                                        unhovered Hide("info")
                                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                                        xfill True
                                        yfill True
                                        text_xpos 0.17

                                    add i.icon() yalign 0.5 xoffset 2

                                    text _('{size=-7}%s 解锁{/size}') % (persistent.guide[i]) style 'white':
                                        xalign 0.975
                                        yalign 1.0

                            null height 20

                        vbox:
                            spacing 10
                            text _('{size=-5}道具图鉴{/size}') style "white":
                                xfill True
                            frame:
                                background None
                                ysize 50
                                bar:
                                    value len(GuideI.done())
                                    range len(ALLITEMS)
                                    xfill True
                                    ysize 50
                                    yalign 0.5
                                text _("解锁进度") style 'white':
                                    xfill True
                                    yalign 0.5
                                    xoffset 10
                                text _('%s / %s') % (len(GuideI.done()), len(ALLITEMS)) style 'white':
                                    xalign 0.975
                                    yalign 1.0

                            null height 5
                            
                            if GuideI.done():
                                text _('{size=-5}已获得过的道具{/size}') style "white":
                                    xfill True
                            

                            for i in GuideI.done():
                                frame:
                                    background None
                                    ysize 100
                                    
                                    textbutton i.name text_style 'white':
                                        action NullAction()
                                        hovered Show(screen="info_i_type", player=player, item=i)
                                        unhovered Hide("info_i_type")
                                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                                        xfill True
                                        yfill True
                                        text_xpos 0.17

                                    add i.icon() yalign 0.5 xoffset 2

                                    text _('{size=-7}%s 解锁{/size}') % (persistent.guide[i]) style 'white':
                                        xalign 0.975
                                        yalign 1.0

                        null height 100
                                


        frame:
            background None
            xpos 0.03
            ypos 0.06
            imagebutton auto "gui/phone/backw_%s.png":
                action SetVariable("phone_page", 0), Hide("info")
                hover_sound audio.cursor
            

                
    
    key 'K_ESCAPE' action SetVariable("phone_page", 0), Hide("info")


