screen screen_phone_gallery(player):

    predict False
    style_prefix "gameUI"
    zorder 600
    

    
    frame:
        
        if phone_page == 5:
            at app_inner_show(220, -65)
        else:
            at app_inner_hide(220, -65)
        

        
        background None
        xcenter 0.5
        ycenter 0.5
        yoffset -10
        
        use barrier('', 0)

        add "gui/phone/wallpaper/camera.webp":
            xcenter 0.5

        text "画廊" xpos 0.92 xanchor 1.0 ypos 0.085 size 40 style "phonew"

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
                        spacing 20
                        if Achievement103.has() or config.developer:
                            frame:
                                background None
                                xsize 530
                                ysize 300
                                imagebutton idle 'gui/phone/gallery/be3.jpg':
                                    action Hide("info"), Show(screen="screen_phone_gallery_show", pic="images/cg/be3.jpg")
                                    at app_transform
                                    
                                text "“目睹”":
                                    style "phonew"
                                    xfill True
                                    yalign 1.0
                                    size 35
                                    xpos 0.02

                                text "——EmoFox":
                                    style "phonew"
                                    xfill True
                                    xanchor 1.0
                                    yalign 1.0
                                    size 20
                                    yoffset 5
                                    xpos 0.95

                        if Achievement404.has() or config.developer:
                            frame:
                                background None
                                xsize 530
                                ysize 300
                                imagebutton idle 'gui/phone/gallery/se.jpg':
                                    action Hide("info"), Show("screen_phone_gallery_show_solitary"), Show(screen="screen_phone_gallery_show", pic="images/cg/se.webp")
                                    at app_transform
                                    
                                text "“存在”":
                                    style "phonew"
                                    xfill True
                                    yalign 1.0
                                    size 35
                                    xpos 0.02
                                
                                text "——Inufuto":
                                    style "phonew"
                                    xfill True
                                    yalign 1.0
                                    yoffset 5
                                    xanchor 1.0
                                    size 20
                                    xpos 0.95
                            
                    

                        null height 300
                                


        frame:
            background None
            xpos 0.03
            ypos 0.06
            imagebutton auto "gui/phone/backw_%s.png":
                action SetVariable("phone_page", 0), Hide("info")
                hover_sound audio.cursor
            

                
    
    key 'K_ESCAPE' action SetVariable("phone_page", 0), Hide("info")




screen screen_phone_gallery_show(pic):

    zorder 10000
    add pic at center

    use barrier("screen_phone_gallery_show")






screen screen_phone_gallery_show_solitary():

    zorder 10000
    add "movie_se_background" xalign 1.0
    add "movie_se_mask" xcenter 0.5 ycenter 0.5 at se_transform

    use barrier("screen_phone_gallery_show_solitary")
