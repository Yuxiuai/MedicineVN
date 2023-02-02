screen screen_phone_music(player):
    #tag gamegui
    modal True

    zorder 600
    frame:
        at trans_app(150, 170)
        style "translucent_frame"
        background None
        xcenter 0.5
        ycenter 0.5
        ysize 750
        xsize 400
        add "gui/phone/phone_desktop_.png":
            xcenter 0.51
            ycenter 0.46

        $playlist = mr.unlocked_playlist()
        
        frame:
            #use screen_phone_bg_
            background None
            xcenter 0.5
            ycenter 0.5
            ysize 750
            xsize 400
            frame:
                background None
                #xpos 0.41
                frame:
                    background None
                    ypos 0.5
                    ysize 80
                    xfill True
                    vbox:
                        text _("{size=+5}音乐播放器{/size}") style "white"
                    if config.developer: 
                        imagebutton idle "gui/reset_w.png":
                            action Function(unlockallmusic)
                            hover_sound audio.cursor
                            xpos 0.9
                            ypos 0.05
            frame:
                background None
                ypos 0.15
                viewport:
                    ysize 475
                    mousewheel True
                    draggable True
                    if len(playlist)>10:
                        scrollbars "vertical"
                    vbox:
                        spacing 4
                        for i in playlist:
                            $name = musicFormat(i)
                            textbutton name:
                                if renpy.music.get_playing()==i:
                                    action NullAction()
                                    hover_sound audio.cursor
                                    hovered Show(screen="info",i=dictMusicCommet[name])
                                    unhovered Hide("info")  
                                    background Frame("gui/style/musicplayer_hover_background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                    text_style "white"
                                    xfill True
                                else:
                                    action Function(renpy.music.play, i)
                                    hover_sound audio.cursor
                                    hovered Show(screen="info",i=dictMusicCommet[name])
                                    unhovered Hide("info")  
                                    background Frame("gui/style/musicplayer_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                    text_style "white"
                                    xfill True
                                    activate_sound audio.cursor



            frame:
                background None
                ypos 0.83
                xfill True
                ysize 65
                
                hbox:
                    xalign 0.5
                    spacing 20

                    imagebutton idle "gui/phone/music/random.png":
                        action [mr.RandomPlay(),renpy.restart_interaction]
                        hovered Show(screen="info",i=_('随机播放'), width=100)
                        unhovered Hide("info")  
                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                        activate_sound audio.cursor
                        yfill True

                    imagebutton idle "gui/phone/music/previous.png":
                        action [mr.Previous(),renpy.restart_interaction]
                        hovered Show(screen="info",i=_('播放上一首'), width=125)
                        unhovered Hide("info")  
                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                        activate_sound audio.cursor
                        yfill True

                    if not renpy.music.get_playing():

                        imagebutton idle "gui/phone/music/play.png":
                            action [mr.Play(),renpy.restart_interaction]
                            hovered Show(screen="info",i=_('播放第一首'), width=125)
                            unhovered Hide("info")  
                            background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            activate_sound audio.cursor
                            yfill True

                    else:
                        
                        imagebutton idle "gui/phone/music/stop.png":
                            action [mr.Stop(),renpy.restart_interaction]
                            hovered Show(screen="info",i=_('停止播放'), width=100)
                            unhovered Hide("info")  
                            background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            activate_sound audio.cursor
                            yfill True


                    imagebutton idle "gui/phone/music/next.png":
                        action [mr.Next(),renpy.restart_interaction]
                        hovered Show(screen="info",i=_('播放下一首'), width=125)
                        unhovered Hide("info")  
                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                        activate_sound audio.cursor
                        yfill True

                    

                    imagebutton idle "gui/phone/music/close.png":
                        action [Hide("screen_phone_music"),Hide("info"),Show(screen="screen_phone", player=player)]
                        hovered Show(screen="info",i=_('关闭播放器'), width=125)
                        unhovered Hide("info")  
                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                        activate_sound audio.cursor
                        yfill True
    
    key 'K_ESCAPE' action [Hide("screen_phone_music"),Hide("info"),Show(screen="screen_phone", player=player)]