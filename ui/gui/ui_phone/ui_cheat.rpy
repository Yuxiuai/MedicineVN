init python:

    def switch_developer():
        config.developer = not config.developer
    

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
                background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor
        null height 2


screen screen_phone_cheat(player):

    #tag gamegui
    modal True
    style_prefix "gameUI"
    zorder 600
    drag:
        xalign 0.5
        yalign 0.4
        frame:
            at trans_Down()
            background Frame("gui/style/grey_idle_background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
            ysize 750
            xsize 750
            textbutton _('{color=#ffffff}作弊界面{/color}')

            frame:
                background None

                viewport:
                    ypos 0.09
                    ysize 650
                    mousewheel True
                    draggable True
                    scrollbars "vertical"
                    use screen_phone_inner(player)

            frame:
                background None
                xpos 0.9
                ypos -0.01
                imagebutton auto "gui/phone/back__%s.png":
                    action [Hide("screen_phone_cheat"),Hide("info")]
                    hover_sound audio.cursor

    key 'K_ESCAPE' action [Hide("screen_phone_cheat"),Hide("info")]


screen screen_phone_inner(player):

    frame:
        background None
        vbox:
            xfill True
            use screen_phone_cheat_title(_('整体'))

            vbox:   
                if not config.developer:
                    use screen_phone_cheat_slot(player, _('解锁菜单中隐藏选项'), Function(switch_developer))

                if config.developer:
                    use screen_phone_cheat_slot(player, _('关闭菜单中隐藏选项'), Function(switch_developer))
                
                use screen_phone_cheat_slot(player, _('过一天'), [Function(player.newDay), Function(player.cheat_times)])
                use screen_phone_cheat_slot(player, _('获得全状态'), Function(allE, player))
                use screen_phone_cheat_slot(player, _('获得全道具'), Function(allI, player))
                use screen_phone_cheat_slot(player, _('获得全成就'), [Function(Achievement.all), Function(Achievement.show)])
                use screen_phone_cheat_slot(player, _('解锁全音乐'), Function(unlockallmusic))
                use screen_phone_cheat_slot(player, _('刷新当前委托'), Function(player.refreshUnacComm))
                use screen_phone_cheat_slot(player, _('设定废墟下男友为Halluke'), Function(player.cheat_route, 'h'))
                use screen_phone_cheat_slot(player, _('设定废墟下男友为Acolas'), Function(player.cheat_route, 'a'))
                use screen_phone_cheat_slot(player, _('进入废墟阶段'), [Jump('earthquake')])
                use screen_phone_cheat_slot(player, _('进入治愈线'), [Jump('CureEndingBeginning')])

            use screen_phone_cheat_title(_('数值'))

            vbox:
                use screen_phone_cheat_slot(player, _('精神状态 +1'), Function(player.cheat_ment, 1))
                use screen_phone_cheat_slot(player, _('精神状态 +10'), Function(player.cheat_ment, 10))
                use screen_phone_cheat_slot(player, _('精神状态 +100'), Function(player.cheat_ment, 100))

                use screen_phone_cheat_slot(player, _('精神状态 -1'), Function(player.cheat_ment, -1))
                use screen_phone_cheat_slot(player, _('精神状态 -10'), Function(player.cheat_ment, -10))
                use screen_phone_cheat_slot(player, _('精神状态 -100'), Function(player.cheat_ment, -100))

                use screen_phone_cheat_slot(player, _('严重程度 +0.01'), Function(player.cheat_sev, 0.01))
                use screen_phone_cheat_slot(player, _('严重程度 +0.1'), Function(player.cheat_sev, 0.1))
                use screen_phone_cheat_slot(player, _('严重程度 +1.0'), Function(player.cheat_sev, 1))

                use screen_phone_cheat_slot(player, _('严重程度 -0.01'), Function(player.cheat_sev, -0.01))
                use screen_phone_cheat_slot(player, _('严重程度 -0.1'), Function(player.cheat_sev, -0.1))
                use screen_phone_cheat_slot(player, _('严重程度 -1.0'), Function(player.cheat_sev, -1))

                use screen_phone_cheat_slot(player, _('工作能力 +0.01'), Function(player.cheat_wor, 0.01))
                use screen_phone_cheat_slot(player, _('工作能力 +0.1'), Function(player.cheat_wor, 0.1))
                use screen_phone_cheat_slot(player, _('工作能力 +1.0'), Function(player.cheat_wor, 1))

                use screen_phone_cheat_slot(player, _('工作能力 -0.01'), Function(player.cheat_wor, -0.01))
                use screen_phone_cheat_slot(player, _('工作能力 -0.1'), Function(player.cheat_wor, -0.1))
                use screen_phone_cheat_slot(player, _('工作能力 -1.0'), Function(player.cheat_wor, -1))

                use screen_phone_cheat_slot(player, _('身体素质 +0.01'), Function(player.cheat_phy, 0.01))
                use screen_phone_cheat_slot(player, _('身体素质 +0.1'), Function(player.cheat_phy, 0.1))
                use screen_phone_cheat_slot(player, _('身体素质 +1.0'), Function(player.cheat_phy, 1))

                use screen_phone_cheat_slot(player, _('身体素质 -0.01'), Function(player.cheat_phy, -0.01))
                use screen_phone_cheat_slot(player, _('身体素质 -0.1'), Function(player.cheat_phy, -0.1))
                use screen_phone_cheat_slot(player, _('身体素质 -1.0'), Function(player.cheat_phy, -1))

                use screen_phone_cheat_slot(player, _('写作能力 +0.01'), Function(player.cheat_wri, 0.01))
                use screen_phone_cheat_slot(player, _('写作能力 +0.1'), Function(player.cheat_wri, 0.1))
                use screen_phone_cheat_slot(player, _('写作能力 +1.0'), Function(player.cheat_wri, 1))

                use screen_phone_cheat_slot(player, _('写作能力 -0.01'), Function(player.cheat_wri, -0.01))
                use screen_phone_cheat_slot(player, _('写作能力 -0.1'), Function(player.cheat_wri, -0.1))
                use screen_phone_cheat_slot(player, _('写作能力 -1.0'), Function(player.cheat_wri, -1))


            use screen_phone_cheat_title(_('状态'))

            vbox:   
                for i in ALLEFFECTS:
                    use screen_phone_cheat_slot(player, i.name, Function(i.add, player))

            use screen_phone_cheat_title(_('道具'))

            vbox:   
                for i in ALLITEMS:
                    use screen_phone_cheat_slot(player, i.name, Function(i.add, player))

            use screen_phone_cheat_title(_('成就'))

            vbox:   
                for i in ALLACHIEVEMENTS:
                    use screen_phone_cheat_slot(player, i.name, Function(i.achieve))
