init python:
    def fun_screen_phone_music_progress(st, at):
        pos = renpy.music.get_pos()
        maxd = renpy.music.get_duration()
        if not pos:
            pos = 0
        if not maxd:
            maxd = 0
        pos = int(pos)
        maxd = int(maxd)
        if maxd != 0:
            d = Text("%s:%s / %s:%s" % (pos//60, str(pos-(pos//60)*60).zfill(2), maxd//60, str(maxd-(maxd//60)*60).zfill(2)),style='phonew', size=25)
        else:
            d = Text("%s:%s / ?:??" % (pos//60, str(pos-(pos//60)*60).zfill(2)),style='phonew', size=25)
        return d, 1

image screen_phone_music_progress = DynamicDisplayable(fun_screen_phone_music_progress)

screen screen_phone_music(player):

    predict False
    style_prefix "gameUI"
    zorder 600
    

    $playlist = mr.unlocked_playlist()

    

        

    frame:
        
        if phone_page == 10:
            at app_inner_show(220, 50)
        else:
            at app_inner_hide(220, 50)
        

        
        background None
        xcenter 0.5
        ycenter 0.5
        yoffset -10
        
        use barrier('', 0)

        add "gui/phone/wallpaper/camera.webp":
            xcenter 0.5

        text "音乐" xpos 0.92 xanchor 1.0 ypos 0.085 size 40 style "phonew"

        frame:
            
            background None
            xalign 0.5
            ypos 150
            ysize 700
            xsize 582
            
            viewport:
                xcenter 0.5
                mousewheel True
                draggable True
                scrollbars "vertical"

                vbox:
                    spacing 4
                    for i in playlist:
                        frame:
                            xfill True
                            ysize 95
                            background None

                            $name = musicFormat(i)
                        


                            imagebutton idle "gui/phone/music/"+name.replace(" ", "_")+".png":
                                
                                if renpy.music.get_playing()==i:
                                    action PauseAudio("music", "toggle")
                                    background Frame("gui/style/musicplayer_hover_background.png", tile=gui.frame_tile)
                                else:
                                    action Function(renpy.music.play, i)
                                    background Frame("gui/style/musicplayer_[prefix_]background.png", tile=gui.frame_tile)
                                    activate_sound audio.cursor
                                
                                hovered Show(screen="info",i=dictMusicCommet[name])
                                unhovered Hide("info")  
                                xfill True
                                at app_transform


                            text name:
                                size 25
                                xpos 0.2
                                style "phonew"
                            
                            if not renpy.music.get_pause() and renpy.music.get_playing()==i:
                                add "gui/phone/music/musicpause.png" xpos 0.9 ycenter 0.5
                            else:
                                add "gui/phone/music/musicplay.png" xpos 0.9 ycenter 0.5

            add "screen_phone_music_progress" ypos 1.03 xalign 0.5

            frame:
                background None
                ypos 1.05
                xfill True
                ysize 65
                
                hbox:
                    xalign 0.5
                    spacing 60

                    imagebutton idle "gui/phone/music/random.png":
                        action mr.RandomPlay()
                        if config.developer:
                            alternate Function(unlockallmusic)
                        hovered Show(screen="info",i=_('随机播放'), width=100)
                        unhovered Hide("info")  
                        at screen_phone_message_friendbox_transform
                        activate_sound audio.cursor
                        yfill True

                    imagebutton idle "gui/phone/music/previous.png":
                        action mr.Previous()
                        hovered Show(screen="info",i=_('播放上一首'), width=125)
                        unhovered Hide("info")  
                        at screen_phone_message_friendbox_transform
                        activate_sound audio.cursor
                        yfill True

                    if renpy.music.get_pause():

                        imagebutton idle "gui/phone/music/play.png":
                            action PauseAudio("music", "toggle")
                            hovered Show(screen="info",i=_('播放'), width=125)
                            unhovered Hide("info")  
                            at screen_phone_message_friendbox_transform
                            activate_sound audio.cursor
                            yfill True

                    else:
                        
                        imagebutton idle "gui/phone/music/stop.png":
                            action PauseAudio("music", "toggle")
                            hovered Show(screen="info",i=_('暂停'), width=100)
                            unhovered Hide("info")  
                            at screen_phone_message_friendbox_transform
                            activate_sound audio.cursor
                            yfill True


                    imagebutton idle "gui/phone/music/next.png":
                        action mr.Next()
                        hovered Show(screen="info",i=_('播放下一首'), width=125)
                        unhovered Hide("info")  
                        at screen_phone_message_friendbox_transform
                        activate_sound audio.cursor
                        yfill True

                    

                    imagebutton idle "gui/phone/music/close.png":
                        action Hide("screen_phone_music"),Hide("info"),SetVariable("phone_page", 0)
                        hovered Show(screen="info",i=_('关闭播放器'), width=125)
                        unhovered Hide("info")  
                        at screen_phone_message_friendbox_transform
                        activate_sound audio.cursor
                        yfill True                   


        frame:
            background None
            xpos 0.03
            ypos 0.06
            imagebutton auto "gui/phone/backw_%s.png":
                action SetVariable("phone_page", 0), Hide("info")
                hover_sound audio.cursor
            

                
    
    key 'K_ESCAPE' action SetVariable("phone_page", 0), Hide("info")


