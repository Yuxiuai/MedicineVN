init offset = -1

screen menu_labelname(name):
    frame at trans_Down:
        background Frame("gui/style/select_hover_background.png", tile=gui.frame_tile)
        xpos 0.05
        xsize 100
        ysize 200
        yoffset 20
        frame:
            yalign 0.5
            background None
            xsize 500
            text name style "white" size 60

screen screen_button(name, act, at_list=None):
    frame:
        background None
        ysize 60
        textbutton _("[name!t]"):
            action act
            background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
            xfill True
            yfill True
            activate_sound audio.cursor 
            text_style "white"
            text_size 25
            text_xalign 0.5
            text_yalign 0.5
            if at_list:
                at at_list



screen screen_gamemenu(player=None):
    if not player:
        $player = p
    tag menu
    zorder 2000
    use barrier(screen="screen_gamemenu", mode=0)

    python:
        def loadingtip(player):
            if player:
                if player.cured >= 21:
                    return ''
            if player is None:
                tip = rcd(loading_tips) if rrd(80) else rcd(loading_tips_random)
            
            else:
                
                if not Despair.has(player):
                    tip = rcd(loading_tips) if rrd(80) else rcd(loading_tips_random)
                else:
                    tip = rcd(loading_tips_zetsubo)
            return tip

    default tip = loadingtip(player)

    
    #$_windows_hidden = True
    $renpy.sound.stop(channel="chara_voice")
    #$sh()

    

    add "images/gui/gamemenu_background.png"
    #style_prefix "info"
    
    frame at trans_Up:
        background None
        xcenter 0.5
        ycenter 0.45
        xsize 300
        has vbox
        if player is None:
            imagebutton idle "pixel_sol0":
                action NullAction()
                hovered Show(screen="info", i='还没有创建角色哦。')
                unhovered Hide("info")
                xalign 0.5
        else:
            if player.cured < 21 and not Despair.has(player):
                if renpy.showing('pathos'):
                    imagebutton idle "pixel_pa":
                        action NullAction()
                        hovered Show(screen="info", i='别碰我。', width=100)
                        unhovered Hide("info")
                        xalign 0.5
                elif renpy.showing('acolas'):
                    if not player.onVacation:
                        imagebutton idle "pixel_aco0":
                            action NullAction()
                            hovered Show(screen="info", i='工作做完了吗？', width=150)
                            unhovered Hide("info")
                            xalign 0.5
                    else:
                        imagebutton idle "pixel_aco1":
                            action NullAction()
                            hovered Show(screen="info", i='想吃点什么？', width=150)
                            unhovered Hide("info")
                            xalign 0.5
                elif renpy.showing('halluke'):
                    if player.onShip:
                        imagebutton idle "pixel_hal1":
                            action NullAction()
                            hovered Show(screen="info", i='好开心……', width=100)
                            unhovered Hide("info")
                            xalign 0.5
                    else:
                        imagebutton idle "pixel_hal0":
                            action NullAction()
                            hovered Show(screen="info", i='唔……', width=100)
                            unhovered Hide("info")
                            xalign 0.5
                elif renpy.showing('depline'):
                    imagebutton idle "pixel_dep":
                        action NullAction()
                        hovered Show(screen="info", i='', width=100)
                        unhovered Hide("info")
                        xalign 0.5
                else:
                    if player.onShip:
                        imagebutton idle "pixel_sol2":
                            action NullAction()
                            hovered Show(screen="info", i='这就是恋爱的感觉吗……', width=250)
                            unhovered Hide("info")
                            xalign 0.5
                    elif player.onVacation:
                        imagebutton idle "pixel_sol0":
                            action NullAction()
                            hovered Show(screen="info", i='待会做些什么呢……', width=200)
                            unhovered Hide("info")
                            xalign 0.5
                    else:
                        imagebutton idle "pixel_sol1":
                            action NullAction()
                            hovered Show(screen="info", i='好困……', width=100)
                            unhovered Hide("info")
                            xalign 0.5
            elif Despair.has(player):
                imagebutton idle "pixel_sol3":
                    action NullAction()
                    hovered Show(screen="info", i='……', width=50)
                    unhovered Hide("info")
                    xalign 0.5

        
        null height 80
        
        use screen_button("返回游戏", Return())
        
        null height 20

        use screen_button("读取", ShowMenu("screen_gamemenu_save", player))
        if Saver.get_today():
            use screen_button("重新开始这一天", Function(Saver.load, Saver.get_today()))
        else:
            use screen_button("{color=#8888887f}重新开始这一天{/color}", NullAction())
        
        null height 20
        use screen_button("难度切换", ShowMenu("screen_diff_select", player))

        use screen_button("历史", ShowMenu("screen_gamemenu_history", player))
        use screen_button("成就", ShowMenu("screen_gamemenu_achievement", player))
        use screen_button("设置", ShowMenu("screen_gamemenu_preferences", player))

        null height 20

        use screen_button("标题界面", Start("to_the_title"))
        use screen_button("退出游戏", Quit(confirm=False))

    
    textbutton tip:
        xpos 0.02
        ypos 0.98
        yanchor 1.0
        text_style "gameUI"
        at trans_Up()

    timer 2.5 repeat True action SetLocalVariable("tip", loadingtip(player))
    key 'K_ESCAPE' action Hide("info"),Return()


screen screen_gamemenu_history(player):
    zorder 2001
    tag menu
    style_prefix "game_menu"

    if main_menu:
        add persistent.main_menu_theme.bg

    default page = 0
    default textsize = 30

    frame:
        bottom_padding 45
        top_padding 180
        background "gui/overlay/confirm.png"
        frame:
            background None
            xfill True

            viewport:
                yinitial 1.0
                scrollbars "vertical"
                mousewheel True
                draggable True
                #xfill True
                xsize 1800
                #side_yfill True
                use screen_gamemenu_history_inner(_history_list, page, textsize)

    imagebutton auto "gui/add_%s.png":
        xalign 0.8
        yalign 0.05
        if textsize > 60:
            action NullAction()
            activate_sound audio.error
        else:
            action SetLocalVariable('textsize', textsize + 2)
            activate_sound audio.cursor
        
    imagebutton auto "gui/minus_%s.png":
        xalign 0.85
        yalign 0.05
        if textsize < 10:
            action NullAction()
            activate_sound audio.error
        else:
            action SetLocalVariable('textsize', textsize - 2)
            activate_sound audio.cursor

    imagebutton auto "gui/sort_%s.png":
        xalign 0.9
        yalign 0.05
        if page == 0:
            action SetLocalVariable('page', 1)
        elif page == 1:
            action SetLocalVariable('page', 0)
        activate_sound audio.cursor

    imagebutton auto "gui/exit_%s.png":
        xalign 0.95
        yalign 0.05
        action ShowMenu("screen_gamemenu", player)

    use menu_labelname('历史')
        


screen screen_gamemenu_history_inner(hlist, page, textsize):
    if page == 1:
        $hlist = list(filter(lambda x: x.who == chara_notice, hlist))

    frame:
        style_prefix "history"
        xfill True
        background None
        vbox:
            spacing textsize / 2
            for h in hlist:

                hbox:
                    if h.who == chara_notice:
                        text '{i}' + h.what + '{/i}':
                            yalign 0.5
                            substitute False
                            size textsize
                            color '#b8b8b8b4'
                            xfill True
                    elif h.who:
                        label h.who:
                            style "history_name"
                            substitute False
                            if "color" in h.who_args:
                                text_color h.who_args["color"]
                        text h.what:
                            xpos 0.04
                            yalign 0.5
                            substitute False
                            size textsize
                            xfill True
                    else:
                        text h.what:
                            yalign 0.5
                            substitute False
                            size textsize
                            xfill True

            if not hlist:
                text _("历史记录为空。")



screen screen_gamemenu_achievement(player):
    zorder 2001
    tag menu
    style_prefix "game_menu"

    if main_menu:
        add persistent.main_menu_theme.bg

    frame:
        bottom_padding 45
        top_padding 180
        background "gui/overlay/confirm.png"
        frame:
            background None
            xfill True
            xpos 0.13

            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                #xfill True
                xsize 1450
                #side_yfill True
            
                use screen_gamemenu_achievement_inner()


    imagebutton auto "gui/exit_%s.png":
        xalign 0.95
        yalign 0.05
        if main_menu:
            action Return()
        else:
            action ShowMenu("screen_gamemenu", player)

    use menu_labelname('成就')

screen screen_gamemenu_achievement_inner():
    frame:
        background None
        vbox:
            spacing 10
            text _('{size=-5}成就总览{/size}') style "white":
                xfill True
            frame:
                background None
                ysize 50
                textbutton _("已达成的成就") text_style 'white':
                    background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                    xfill True
                text _('%s / %s') % (len(persistent.achievements), len(ALLACHIEVEMENTS)+len(Achievement.hdone())) style 'white':
                    xalign 0.975
                    yalign 1.0
            
            frame:
                background None
                ysize 50
                default runtime_h = int(persistent.runtime//60//60)
                default runtime_m = int((persistent.runtime - runtime_h *60*60)//60)
                default runtime_s = int((persistent.runtime - runtime_h *60*60 - runtime_m *60))
                textbutton _("游玩时间") text_style 'white':
                    background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                    xfill True
                text _('%s小时%s分%s秒') % (runtime_h, runtime_m, runtime_s) style 'white':
                    xalign 0.975
                    yalign 1.0
            
            frame:
                background None
                ysize 50
                textbutton _("通关次数") text_style 'white':
                    background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                    xfill True
                text str(persistent.gametimes) style 'white':
                    xalign 0.975
                    yalign 1.0
            
            frame:
                background None
                ysize 50
                textbutton _("最高分数") text_style 'white':
                    background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                    xfill True
                text str(persistent.highestscore) style 'white':
                    xalign 0.975
                    yalign 1.0

            if Achievement.done() or Achievement.hdone():
                text _('{size=-5}已达成的成就{/size}') style "white":
                    xfill True


            for i in Achievement.done() + Achievement.hdone():
                frame:
                    background None
                    ysize 110
                    xoffset 5
                    hbox:
                        add i.icon
                        null width 10
                        vbox:
                            text '{color=%s}[i.name!t]{/color}' % i.textcolor style 'white':
                                xfill True
                                yoffset 20
                            text i.info style 'admonition_text':
                                xfill True
                                yoffset 13
                    text _('{size=-7}%s 解锁{/size}') % (persistent.achievements[i]) style 'white':
                        xalign 0.975
                        yalign 1.0

            if Achievement.undone():
                text _('{size=-5}未达成的成就{/size}') style "white":
                    xfill True
                

            for i in Achievement.undone():
                frame:
                    background None
                    ysize 110
                    xoffset 5
                    hbox:
                        add "gui/achievements/unknownAchievement.png"
                        null width 10
                        vbox:
                            text _('？') * len(i.name) style 'white':
                                xfill True
                                yoffset 20
                            text i.info style 'admonition_text':
                                xfill True
                                yoffset 13



transform highlight:
    matrixcolor BrightnessMatrix(0.2)

transform lowlight:
    matrixcolor BrightnessMatrix(-0.2)

transform hoverlight:
    on idle:
        easein 0.2 matrixcolor IdentityMatrix()
    on hover:
        easein 0.2 matrixcolor BrightnessMatrix(0.2)

screen screen_gamemenu_preferences(player):
    zorder 2001
    tag menu
    style_prefix "game_menu"

    if main_menu:
        add persistent.main_menu_theme.bg

    default page = 0
    

    frame:
        bottom_padding 45
        top_padding 180
        background "gui/overlay/confirm.png"

        frame:
            background None
            xfill True
            xpos 0.13
            
            

            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                #xfill True
                xsize 1450
                
                #side_yfill True
                use screen_gamemenu_preferences_inner(player, page)

    if config.developer or persistent.sponsor:
        frame:
            background None
            xpos 0.15
            xanchor 0.0
            yalign 0.075
            hbox:
                spacing 5
                textbutton "默认设置" action SetLocalVariable("page", 0) text_style "white" text_xalign 0.5:
                    if page == 0:
                        background Frame("gui/style/grey_hover_background.png", tile=gui.frame_tile)
                    else:
                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                    xsize 200
                textbutton "测试" action SetLocalVariable("page", 99) text_style "white" text_xalign 0.5:
                    if page == 99:
                        background Frame("gui/style/grey_hover_background.png", tile=gui.frame_tile)
                    else:
                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                    xsize 200

    imagebutton auto "gui/exit_%s.png":
        xalign 0.95
        yalign 0.05
        if main_menu:
            action Return()
        else:
            action ShowMenu("screen_gamemenu", player)

    use menu_labelname('设置')

    key 'K_ESCAPE' action Hide("info"),Return()

screen screen_gamemenu_preferences_inner(player, page):
    frame:
        background None
        vbox:
            spacing 10               

            if page == 0:
                text _('{size=-5}系统设置{/size}') style "white":
                    xfill True

                if renpy.variant("pc") or renpy.variant("web"):
                    frame:
                        background None
                        ysize 50
                        textbutton _("显示") text_style 'white':
                            action [Show(screen='window_select')]
                            background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                            xfill True
                            activate_sound audio.cursor
                        if not preferences.fullscreen:
                            text _("窗口") style 'white':
                                xalign 0.975
                                yalign 1.0
                        if preferences.fullscreen:
                            text _("全屏") style 'white':
                                xalign 0.975
                                yalign 1.0

                frame:
                    background None
                    ysize 50
                    textbutton _("主界面主题") text_style 'white':
                        action [Show(screen='mainmenutheme_select')]
                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor

                    if persistent.main_menu_theme == Theme_train:
                        text _("列车") style 'white':
                            xalign 0.975
                            yalign 1.0
                    elif persistent.main_menu_theme == Theme_acolas:
                        text _("Acolas") style 'white':
                            xalign 0.975
                            yalign 1.0
                    else:
                        text _("旧版") style 'white':
                            xalign 0.975
                            yalign 1.0
                #frame:
                #    background None
                #    ysize 50
                #    textbutton _("语言") text_style 'white':
                #        action [Show(screen='lang_select')]
                #        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                #        xfill True
                #        activate_sound audio.cursor
                #    if preferences.language == None:
                #        text "中文" style 'white':
                #            xalign 0.975
                #            yalign 1.0
                #    if preferences.language == 'english':
                #        text "English (Machine-Translated)" style 'white':
                #            xalign 0.975
                #            yalign 1.0

                frame:
                    background None
                    ysize 50
                    textbutton _("音乐音量") text_style 'white':
                        action Show(screen='music_setting')
                        background Frame("gui/style/grey_idle_background.png", tile=gui.frame_tile)
                        xfill True


                    text str(int(100*preferences.get_volume('music'))) + '%' style 'white':
                        xalign 0.975
                        yalign 1.

                frame:
                    background None
                    ysize 50
                    textbutton _("音效音量") text_style 'white':
                        action Show(screen='sound_setting')
                        background Frame("gui/style/grey_idle_background.png", tile=gui.frame_tile)
                        xfill True

                    text str(int(100*preferences.get_volume('sfx'))) + '%' style 'white':
                        xalign 0.975
                        yalign 1.0


                frame:
                    background None
                    ysize 50
                    textbutton _("跳过未读文本") text_style 'white':
                        action [ToggleVariable("preferences.skip_unseen", true_value=True, false_value=False), Function(renpy.save_persistent)]
                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                        hovered Show(screen='info', i=_('跳过未读文本\n\n勾选此项后，游戏内未读过的文字也可以快进。'),width=600)
                        unhovered Hide('info')
                        xfill True
                        activate_sound audio.cursor
                    if preferences.skip_unseen:
                        add "gui/right_.png":
                            xalign 0.975
                            yalign 0.2

                if persistent.gametimes >= 1 or config.developer:
                    frame:
                        background None
                        ysize 50
                        textbutton _("跳过日程等待时间和过场动画") text_style 'white':
                            action [ToggleVariable("persistent.nowaiting", true_value=True, false_value=False), Function(renpy.save_persistent)]
                            hovered Show(screen='info', i=_('跳过日程等待时间和过场动画\n\n勾选此项后，游戏进行日程的等待时间和过场动画的播放时间缩短至0.1秒。'),width=600)
                            unhovered Hide('info')
                            background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                            xfill True
                            activate_sound audio.cursor
                        if persistent.nowaiting:
                            add "gui/right_.png":
                                xalign 0.975
                                yalign 0.2
                
                frame:
                    background None
                    ysize 50
                    textbutton _("禁用文字音效") text_style 'white':
                        action [ToggleVariable("persistent.disablecharactervoice", true_value=True, false_value=False), Function(renpy.save_persistent)]
                        hovered Show(screen='info', i=_('禁用文字音效\n\n勾选此项后，剧情文字不再出现音效。'),width=600)
                        unhovered Hide('info')
                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if persistent.disablecharactervoice:
                        add "gui/right_.png":
                            xalign 0.975
                            yalign 0.2

            

            
                text _('{size=-5}游戏设置{/size}') style "white":
                    xfill True

                
                frame:
                    background None
                    ysize 50
                    textbutton _("快捷操作") text_style 'white':
                        action [ToggleVariable("persistent.actionquickly", true_value=True, false_value=False), Function(renpy.save_persistent)]
                        hovered Show(screen='info', i=_('快捷操作\n\n勾选此项后，不再显示确定界面，使操作更加迅捷。\n（推荐电脑玩家点出）'),width=600)
                        unhovered Hide('info')
                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if persistent.actionquickly:
                        add "gui/right_.png":
                            xalign 0.975
                            yalign 0.2
                       

                frame:
                    background None
                    ysize 50
                    textbutton _("自动移除已损道具") text_style 'white':
                        action [ToggleVariable("persistent.noBrokenItem", true_value=True, false_value=False), Function(renpy.save_persistent)]
                        hovered Show(screen='info', i=_('自动移除已损道具\n\n勾选此项后，当道具损坏时移除道具。\n（游戏的特殊阶段中无效。）'),width=600)
                        unhovered Hide('info')
                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if persistent.noBrokenItem:
                        add "gui/right_.png":
                            xalign 0.975
                            yalign 0.2

                frame:
                    background None
                    ysize 50
                    textbutton _("禁用自动填充快捷栏") text_style 'white':
                        action [ToggleVariable("persistent.forbidnostarquickitem", true_value=True, false_value=False), Function(renpy.save_persistent)]
                        hovered Show(screen='info', i=_('禁用自动填充快捷栏\n\n勾选此项后，快捷栏中只会出现你设置的道具。'),width=600)
                        unhovered Hide('info')
                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if persistent.forbidnostarquickitem:
                        add "gui/right_.png":
                            xalign 0.975
                            yalign 0.2
                
                frame:
                    background None
                    ysize 50
                    textbutton _("禁用主角立绘") text_style 'white':
                        action [ToggleVariable("persistent.nosolitussprite", true_value=True, false_value=False), Function(renpy.save_persistent)]
                        hovered Show(screen='info', i=_('禁用主角立绘\n\n勾选此项后，不再显示主角的立绘，一定程度上能够缓解手机玩家闪退的情况。\n（不推荐电脑玩家点出）'),width=600)
                        unhovered Hide('info')
                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if persistent.nosolitussprite:
                        add "gui/right_.png":
                            xalign 0.975
                            yalign 0.2
                
                frame:
                    background None
                    ysize 50
                    textbutton _("剧情时隐藏数值界面") text_style 'white':
                        action [ToggleVariable("persistent.clearscreenwhenplot", true_value=True, false_value=False), Function(renpy.save_persistent)]
                        hovered Show(screen='info', i=_('剧情时隐藏数值界面\n\n勾选此项后，进入剧情时会隐藏两侧的数值界面。'),width=600)
                        unhovered Hide('info')
                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if persistent.clearscreenwhenplot:
                        add "gui/right_.png":
                            xalign 0.975
                            yalign 0.2


                
                

                text _('{size=-5}信息显示设置{/size}') style "white":
                    xfill True


                frame:
                    background None
                    ysize 50
                    textbutton _("显示基础能力数值") text_style 'white':
                        action [ToggleVariable("persistent.PreciseDisplayAbilities", true_value=True, false_value=False), Function(renpy.save_persistent)]
                        hovered Show(screen='info', i=_('显示基础能力数值\n\n勾选此项后，显示当前数值的同时也显示增幅前的数值。\n\n例：\n工作能力 1.1 -> 工作能力 1.1(1.05)'),width=600)
                        unhovered Hide('info')
                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if persistent.PreciseDisplayAbilities:
                        add "gui/right_.png":
                            xalign 0.975
                            yalign 0.2

                frame:
                    background None
                    ysize 50
                    textbutton _("显示具体工作目标") text_style 'white':
                        action [ToggleVariable("persistent.PreciseDisplayGoal", true_value=True, false_value=False), Function(renpy.save_persistent)]
                        hovered Show(screen='info', i=_('显示具体工作目标\n\n勾选此项后，显示工作目标的格式将以具体的数值显示。\n\n例：\n工作进度 10% -> 工作进度 1.0/10.0(10%)'),width=600)
                        unhovered Hide('info')
                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if persistent.PreciseDisplayGoal:
                        add "gui/right_.png":
                            xalign 0.975
                            yalign 0.2
                
                frame:
                    background None
                    ysize 50
                    textbutton _("显示抗药性原因") text_style 'white':
                        action [ToggleVariable("persistent.PreciseMedDisplay", true_value=True, false_value=False), Function(renpy.save_persistent)]
                        hovered Show(screen='info', i=_('显示抗药性原因\n\n勾选此项后，游戏内的药物的介绍文字将更详细地描述其抗药性原因，但也可能因为信息过长导致操作部分超出屏幕。\n\n例：\n预计恢复100.0（140%）点精神状态\n->\n预计恢复100.0点精神状态。\n使用效率：140%\n\n其中：\n    早上使用：*140%'),width=600)
                        unhovered Hide('info')
                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if persistent.PreciseMedDisplay:
                        add "gui/right_.png":
                            xalign 0.975
                            yalign 0.2
                


            
            
            
            if page == 99:
                
                text _('{size=-5}测试菜单{/size}') style "white":
                    xfill True
                default rollbacksetting = config.rollback_enabled  #因为不知名的bug导致这里只能这么写
                frame:
                    background None
                    ysize 50
                    textbutton _("允许回退") text_style 'white':
                        action [ToggleVariable("config.rollback_enabled", true_value=True, false_value=False), SetLocalVariable("rollbacksetting", not rollbacksetting)]
                        hovered Show(screen='info', i=_('允许回退\n\n勾选此项后，你可以向前回滚，没有回滚图标的情况下只能用鼠标滚轮。'),width=600)
                        unhovered Hide('info')
                        
                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if rollbacksetting:
                        add "gui/right_.png":
                            xalign 0.975
                            yalign 0.2
                frame:
                    background None
                    ysize 50
                    textbutton _("允许随时调整日程") text_style 'white':
                        action [ToggleVariable("persistent.unlockplan", true_value=True, false_value=False)]
                        hovered Show(screen='info', i=_('允许随时调整日程\n\n勾选此项后，你可以在任意时间调整自己的日程。'),width=600)
                        unhovered Hide('info')
                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if persistent.unlockplan:
                        add "gui/right_.png":
                            xalign 0.975
                            yalign 0.2
                
                frame:
                    background None
                    ysize 50
                    textbutton _("允许丢弃无法丢弃的道具") text_style 'white':
                        action [ToggleVariable("persistent.allowquitunique", true_value=True, false_value=False), Function(renpy.save_persistent)]
                        hovered Show(screen='info', i=_('允许丢弃无法丢弃的道具\n\n勾选此项后，你可以丢弃不能丢弃的道具，但丢弃某些道具可能导致无法进行部分剧情。'),width=600)
                        unhovered Hide('info')
                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if persistent.allowquitunique:
                        add "gui/right_.png":
                            xalign 0.975
                            yalign 0.2
                
                
                frame:
                    background None
                    ysize 50
                    textbutton _("跳过开场动画") text_style 'white':
                        action [ToggleVariable("persistent.nosplash", true_value=True, false_value=False), Function(renpy.save_persistent)]
                        hovered Show(screen='info', i=_('跳过开场动画\n\n勾选此项后，打开游戏不再出现开场动画。'),width=600)
                        unhovered Hide('info')
                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if persistent.nosplash:
                        add "gui/right_.png":
                            xalign 0.975
                            yalign 0.2

                frame:
                    background None
                    ysize 50
                    textbutton _("关闭人物剧情") text_style 'white':
                        action [ToggleVariable("persistent.nocharacterplot", true_value=True, false_value=False), Function(renpy.save_persistent)]
                        hovered Show(screen='info', i=_('关闭人物剧情\n\n勾选此项后，进行日程不会触发人物剧情。'),width=600)
                        unhovered Hide('info')
                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if persistent.nocharacterplot:
                        add "gui/right_.png":
                            xalign 0.975
                            yalign 0.2

                frame:
                    background None
                    ysize 50
                    textbutton _("跳过死亡判定") text_style 'white':
                        action [ToggleVariable("persistent.nomedicine", true_value=True, false_value=False), Function(renpy.save_persistent)]
                        hovered Show(screen='info', i=_('跳过死亡判定\n\n勾选此项后，跳过早上的吃药阶段，精神值低于0也不会死亡。'),width=600)
                        unhovered Hide('info')
                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if persistent.nomedicine:
                        add "gui/right_.png":
                            xalign 0.975
                            yalign 0.2

                frame:
                    background None
                    ysize 50
                    textbutton _("解锁跳过日程") text_style 'white':
                        action [ToggleVariable("persistent.unlocktesttask", true_value=True, false_value=False), Function(renpy.save_persistent)]
                        hovered Show(screen='info', i=_('解锁跳过日程\n\n勾选此项后，解锁跳过日程以快速跳过日程。'),width=600)
                        unhovered Hide('info')
                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if persistent.unlocktesttask:
                        add "gui/right_.png":
                            xalign 0.975
                            yalign 0.2
                
                frame:
                    background None
                    ysize 50
                    textbutton _("解锁全部人物剧情") text_style 'white':
                        action [ToggleVariable("persistent.unlockcharacterplot", true_value=True, false_value=False), Function(renpy.save_persistent)]
                        hovered Show(screen='info', i=_('解锁全部人物剧情\n\n勾选此项后，可以在手机的剧情回顾中查看所有剧情。'),width=600)
                        unhovered Hide('info')
                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if persistent.unlockcharacterplot:
                        add "gui/right_.png":
                            xalign 0.975
                            yalign 0.2
                
                frame:
                    background None
                    ysize 50
                    textbutton _("角色立刻回复消息") text_style 'white':
                        action [ToggleVariable("persistent.replymessagesquickly", true_value=True, false_value=False), Function(renpy.save_persistent)]
                        hovered Show(screen='info', i=_('角色立刻回复消息\n\n勾选此项后，向角色发消息时对方会立刻回复，在部分特殊剧情中没有效果。'),width=600)
                        unhovered Hide('info')
                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if persistent.replymessagesquickly:
                        add "gui/right_.png":
                            xalign 0.975
                            yalign 0.2

                frame:
                    background None
                    ysize 50
                    textbutton _("没收Halluke的手机") text_style 'white':
                        action [ToggleVariable("persistent.noannoyhalluke", true_value=True, false_value=False), Function(renpy.save_persistent)]
                        hovered Show(screen='info', i=_('没收Halluke的手机\n\n勾选此项后，Halluke不再狂发信息给你。'),width=600)
                        unhovered Hide('info')
                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if persistent.noannoyhalluke:
                        add "gui/right_.png":
                            xalign 0.975
                            yalign 0.2

                frame:
                    background None
                    ysize 50
                    textbutton _("电子宠物电棍") text_style 'white':
                        action [ToggleVariable("persistent.diangunlevi", true_value=True, false_value=False), Function(renpy.save_persistent)]
                        hovered Show(screen='info', i=_('电子宠物电棍\n\n勾选此项后，电子宠物应用戳击音效改变。'),width=600)
                        unhovered Hide('info')
                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if persistent.diangunlevi:
                        add "gui/right_.png":
                            xalign 0.975
                            yalign 0.2
                    














screen mainmenutheme_select:
    use barrier(screen="mainmenutheme_select")
    style_prefix "info"
    zorder 2002
    default pp = renpy.get_mouse_pos()
    $ p = pp
    if p[0] < 1500:
        $ xc = 0.0
        $ trans = trans_toLeft
    else:
        $ xc = 1.0
        $ trans = trans_toRight
    $ xc = 0.0 if p[0] < 1500 else 1.0
    $ yc = 0.0 if p[1] < 540 else 1.0
    frame:
        pos pp
        padding (15, 15)
        xanchor xc
        yanchor yc
        xsize 300
        at trans()
        has vbox
        frame:
            background None
            ysize 50
            textbutton _("旧版") text_style 'white':
                action [SetVariable("persistent.main_menu_theme", Theme_old),Hide("mainmenutheme_select"),Hide('info')]
                background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor
            if persistent.main_menu_theme == Theme_old:
                add "gui/right_.png":
                    xalign 0.975
                    yalign 0.5

        frame:
            background None
            ysize 50
            textbutton _("列车") text_style 'white':
                action [SetVariable("persistent.main_menu_theme", Theme_train),Hide("mainmenutheme_select"),Hide('info')]
                background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor
            if persistent.main_menu_theme == Theme_train:
                add "gui/right_.png":
                    xalign 0.975
                    yalign 0.5

        frame:
            background None
            ysize 50
            textbutton _("Acolas") text_style 'white':
                action [SetVariable("persistent.main_menu_theme", Theme_acolas),Hide("mainmenutheme_select"),Hide('info')]
                background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor
            if persistent.main_menu_theme == Theme_acolas:
                add "gui/right_.png":
                    xalign 0.975
                    yalign 0.5




screen window_select:
    use barrier(screen="window_select")
    style_prefix "info"
    zorder 2002
    default pp = renpy.get_mouse_pos()
    $ p = pp
    if p[0] < 1500:
        $ xc = 0.0
        $ trans = trans_toLeft
    else:
        $ xc = 1.0
        $ trans = trans_toRight
    $ xc = 0.0 if p[0] < 1500 else 1.0
    $ yc = 0.0 if p[1] < 540 else 1.0
    frame:
        pos pp
        padding (15, 15)
        xanchor xc
        yanchor yc
        xsize 300
        at trans()
        has vbox
        frame:
            background None
            ysize 50
            textbutton _("窗口") text_style 'white':
                action [SetVariable("preferences.fullscreen", False),Hide("window_select"),Hide('info')]
                hovered Show(screen='info', i=_('窗口\n\n勾选此项后，游戏以窗口模式进行。'),width=600)
                unhovered Hide('info')
                background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor
            if not preferences.fullscreen:
                add "gui/right_.png":
                    xalign 0.975
                    yalign 0.5
        frame:
            background None
            ysize 50
            textbutton _("全屏") text_style 'white':
                action [SetVariable("preferences.fullscreen", True),Hide("window_select"),Hide('info')]
                hovered Show(screen='info', i=_('全屏\n\n勾选此项后，游戏以全屏模式进行。'),width=600)
                unhovered Hide('info')
                background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor
            if preferences.fullscreen:
                add "gui/right_.png":
                    xalign 0.975
                    yalign 0.5

screen lang_select:
    use barrier(screen="lang_select")
    style_prefix "info"
    zorder 2002
    default pp = renpy.get_mouse_pos()
    $ p = pp
    if p[0] < 1500:
        $ xc = 0.0
        $ trans = trans_toLeft
    else:
        $ xc = 1.0
        $ trans = trans_toRight
    $ xc = 0.0 if p[0] < 1500 else 1.0
    $ yc = 0.0 if p[1] < 540 else 1.0
    frame:
        pos pp
        padding (15, 15)
        xanchor xc
        yanchor yc
        xsize 500
        at trans()
        has vbox
        frame:
            background None
            ysize 50
            textbutton "中文" text_style 'white':
                action [Language(None),Hide("lang_select")]
                background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor
            if preferences.language == None:
                add "gui/right_.png":
                    xalign 0.975
                    yalign 0.5
        if False:
            frame:
                background None
                ysize 50
                textbutton "English (Machine-Translated)" text_style 'white':
                    action [Language('english'),Hide("lang_select")]
                    background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                    xfill True
                    activate_sound audio.cursor
                if preferences.language == 'english':
                    add "gui/right_.png":
                        xalign 0.975
                        yalign 0.5


screen notify_select:
    use barrier(screen="notify_select")
    style_prefix "info"
    zorder 2002
    default pp = renpy.get_mouse_pos()
    $ p = pp
    if p[0] < 1500:
        $ xc = 0.0
        $ trans = trans_toLeft
    else:
        $ xc = 1.0
        $ trans = trans_toRight
    $ xc = 0.0 if p[0] < 1500 else 1.0
    $ yc = 0.0 if p[1] < 540 else 1.0
    frame:
        pos pp
        padding (15, 15)
        xanchor xc
        yanchor yc
        xsize 300
        at trans()
        has vbox
        frame:
            background None
            ysize 50
            textbutton _("较短（3秒）") text_style 'white':
                action [SetVariable("persistent.notifyDuration", 3),Function(renpy.save_persistent), Hide("notify_select")]
                background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor
            if persistent.notifyDuration == 3:
                add "gui/right_.png":
                    xalign 0.975
                    yalign 0.5
        frame:
            background None
            ysize 50
            textbutton _("正常（5秒）") text_style 'white':
                action [SetVariable("persistent.notifyDuration", 5),Function(renpy.save_persistent), Hide("notify_select")]
                background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor
            if persistent.notifyDuration == 5:
                add "gui/right_.png":
                    xalign 0.975
                    yalign 0.5
        frame:
            background None
            ysize 50
            textbutton _("较久（10秒）") text_style 'white':
                action [SetVariable("persistent.notifyDuration", 10),Function(renpy.save_persistent), Hide("notify_select")]
                background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor
            if persistent.notifyDuration == 10:
                add "gui/right_.png":
                    xalign 0.975
                    yalign 0.5



screen music_setting:
    use barrier(screen="music_setting")
    style_prefix "info"
    zorder 2002
    default pp = renpy.get_mouse_pos()
    $ p = pp
    if p[0] < 1500:
        $ xc = 0.0
        $ trans = trans_toLeft
    else:
        $ xc = 1.0
        $ trans = trans_toRight
    $ xc = 0.0 if p[0] < 1500 else 1.0
    $ yc = 0.0 if p[1] < 540 else 1.0
    frame:
        pos pp
        padding (15, 15)
        xanchor xc
        yanchor yc
        xsize 510
        at trans()
        has vbox
        frame:
            background None
            ysize 50
            xsize 510
            hbox:
                spacing 10
                bar value Preference("music volume"):
                    xsize 400
                text str(int(100*preferences.get_volume('music'))) + '%' style 'white':
                    xalign 0.975
                    yalign 1.0

screen sound_setting:
    use barrier(screen="sound_setting")
    style_prefix "info"
    zorder 2002
    default pp = renpy.get_mouse_pos()
    $ p = pp
    if p[0] < 1500:
        $ xc = 0.0
        $ trans = trans_toLeft
    else:
        $ xc = 1.0
        $ trans = trans_toRight
    $ xc = 0.0 if p[0] < 1500 else 1.0
    $ yc = 0.0 if p[1] < 540 else 1.0
    frame:
        pos pp
        padding (15, 15)
        xanchor xc
        yanchor yc
        xsize 510
        at trans()
        has vbox
        frame:
            background None
            ysize 50
            hbox:
                spacing 10
                bar value Preference("sound volume"):
                    xsize 400
                text str(int(100*preferences.get_volume('sfx'))) + '%' style 'white':
                    xalign 0.975
                    yalign 1.0
