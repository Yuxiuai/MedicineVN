init python:

    def switch_developer():
        config.developer = not config.developer
    













screen screen_phone_cheat(player):

    predict False
    style_prefix "gameUI"
    zorder 600
    

    
    frame:
        
        if phone_page == 15:
            at app_inner_show(220, -150)
        else:
            at app_inner_hide(220, -150)
        

        
        background None
        xcenter 0.5
        ycenter 0.5
        yoffset -10
        
        use barrier('', 0)

        add "gui/phone/wallpaper/camera.webp":
            xcenter 0.5

        
        text "赞助者菜单" xpos 0.92 xanchor 1.0 ypos 0.07 size 40 style "phonew"

        frame:
            
            background None
            xalign 0.5
            ypos 150
            ysize 800
            xsize 582
            
            use screen_phone_inner(player)


        frame:
            background None
            xpos 0.03
            ypos 0.06
            imagebutton auto "gui/phone/backw_%s.png":
                action SetVariable("phone_page", 0), Hide("info")
                hover_sound audio.cursor
            

                
    
    key 'K_ESCAPE' action SetVariable("phone_page", 0), Hide("info")


























screen screen_phone_cheat_title(brief):

    textbutton _('{size=-5}%s{/size}') % brief:
        action NullAction()
        xfill True
        activate_sound audio.cursor
        xoffset -8
        text_style "white"

screen screen_phone_cheat_slot(player, brief, act):
    frame:
        background None
        ysize 60
        xfill True
        frame:
            background None
            textbutton brief text_style "white":
                action act, Function(player.when_cheat)
                background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor
        null height 2



screen screen_phone_inner(player):

    python:
        def cdclear(player):
            player.itemcd = {}

        def unlockallshop(player):
            player.visitedStore = {1,2,3,4,5,6,7,8}

    default page = 0

    viewport:
        xcenter 0.5
        mousewheel True
        draggable True
        scrollbars "vertical"

        frame:
            background None
            xsize 540

                    

            vbox:
                xfill True
                if page == 0:
                    use screen_phone_cheat_title(_('整体'))

                    vbox:   
                        
                        use screen_phone_cheat_slot(player, _('过一天'), [Function(player.newDay), Function(player.cheat_times), Function(Notice.show)])
                        use screen_phone_cheat_slot(player, _('刷新道具cd'), [Function(cdclear, player), Function(player.cheat_times), Function(Notice.show)])
                        use screen_phone_cheat_slot(player, _('解锁全音乐'), Function(unlockallmusic))
                        use screen_phone_cheat_slot(player, _('解锁全商业街'), Function(unlockallshop, player))

                    use screen_phone_cheat_title(_('获得'))
                    vbox:
                        use screen_phone_cheat_slot(player, _('状态'), SetLocalVariable("page", 1))
                        use screen_phone_cheat_slot(player, _('道具'), SetLocalVariable("page", 2))
                        use screen_phone_cheat_slot(player, _('成就'), SetLocalVariable("page", 3))

                    use screen_phone_cheat_title(_('跳关'))

                    vbox:   
                        use screen_phone_cheat_slot(player, _('设定废墟下男友为Halluke'), Function(player.cheat_route, 'h'))
                        use screen_phone_cheat_slot(player, _('设定废墟下男友为Acolas'), Function(player.cheat_route, 'a'))
                        use screen_phone_cheat_slot(player, _('进入废墟阶段'), [Jump('earthquake')])

                        use screen_phone_cheat_slot(player, _('进入治愈线'), [Jump('CureEndingBeginning')])

                    


                elif page == 1:
                    

                    vbox:   
                        use screen_phone_cheat_slot(player, _('返回'), SetLocalVariable("page", 0))

                        use screen_phone_cheat_title(_('状态'))
                        use screen_phone_cheat_slot(player, _('获得全状态'), [Function(allE, player), Function(Notice.show)])
                        use screen_phone_cheat_title(_('详细'))
                        for i in ALLEFFECTS:
                            if not i.hide:
                                use screen_phone_cheat_slot(player, i.name, [Function(i.add, player), Function(Notice.show)])

                elif page == 2:
                    

                    vbox:   
                        use screen_phone_cheat_slot(player, _('返回'), SetLocalVariable("page", 0))
                        use screen_phone_cheat_title(_('道具'))
                        use screen_phone_cheat_slot(player, _('获得全道具'), [Function(allI, player), Function(Notice.show)])
                        use screen_phone_cheat_title(_('详细'))
                        for i in ALLITEMS:
                            use screen_phone_cheat_slot(player, i.name, [Function(i.add, player), Function(Notice.show)])

                elif page == 3:
                    
                    vbox:   
                        use screen_phone_cheat_slot(player, _('返回'), SetLocalVariable("page", 0))
                        use screen_phone_cheat_title(_('成就'))
                        use screen_phone_cheat_slot(player, _('获得全成就'), [Function(Achievement.all), Function(Achievement.show), Function(Notice.show)])
                        use screen_phone_cheat_title(_('详细'))
                    
                        for i in ALLACHIEVEMENTS:
                            use screen_phone_cheat_slot(player, i.name, [Function(i.achieve), Function(Achievement.show)])
