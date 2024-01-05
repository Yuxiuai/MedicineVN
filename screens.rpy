init offset = -1


init python:
    def _medicine_reload():
        if not main_menu and persistent.savefile:
            global p
            sh()
            newp = None
            for i in range(len(persistent.savefile)):
                for j in range(len(persistent.savefile[i])):
                    if persistent.savefile[i][j].p.seed == p.seed:
                        newp = persistent.savefile[i][j].p
                        newp.restart += 1
                        break
            if not newp:
                newp = persistent.savefile[-1][-1].p
            p = dcp(newp)
            renpy.jump("afterload")

    def _medicine_enablerollback():
        if config.developer:
            config.rollback_enabled = True
            showNotice(['已开启回滚。'])
    #def _medicine_save():


    config.keymap['progress_screen'].remove('K_F2')
    config.keymap['help'].remove('K_F1')
    config.keymap['performance'].remove('K_F3')
    config.keymap['medicine_reload'] = ['K_F2']
    config.keymap['medicine_save'] = ['K_F1']
    config.keymap['medicine_enable_rollback'] = ['K_F3']
    
    config.underlay.append(renpy.Keymap(
        medicine_reload = _medicine_reload,
        medicine_save = ShowMenu("screen_gamemenu_save"),
        medicine_enable_rollback = _medicine_enablerollback,
    ))


    


style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style solid_bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)


















transform change_transform(old_widget, new_widget):
    contains:
        new_widget
        xoffset -100
        alpha 0.0
        linear 0.2 xoffset 0 alpha 1.0
    contains:
        old_widget
        xoffset 0
        alpha 1.0
        linear 0.2 xoffset -100 alpha 0.0

define config.side_image_change_transform = change_transform

transform same_transform(old_widget, new_widget):
    contains:
        old_widget
    contains:
        new_widget with Dissolve(0.2, alpha=True)

define config.side_image_same_transform = same_transform


screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"



    use quickmenu(p)


init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos










screen input(prompt):
    style_prefix "input"

    window:

        has vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

        text prompt style "input_prompt"
        input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width









screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action




define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")



screen quickmenu(player):
    zorder 100
    use replaying_indicator()

    if quick_menu or replaying:
        hbox:
            xcenter 0.8
            ycenter 0.75
            xalign 0.5
            spacing 25
            if replaying:
                imagebutton auto "gui/quickmenu/stopreplay_%s.png":
                    action [Hide("info"), Function(sh), Jump('afterreplay')]
                    hovered Show(screen="info", i=_('结束剧情回顾'), a=_('我的思绪飘荡，而我紧随其后。'))
                    unhovered Hide("info")

            if config.rollback_enabled:
                imagebutton auto "gui/quickmenu/rollback_%s.png":
                    action [Rollback(), Hide("info")]
                    hovered Show(screen="info", i=_('回退'), a=_('想要回到过去的人太多了，你应该珍惜回退的机会。'))
                    unhovered Hide("info")
            imagebutton auto "gui/quickmenu/history_%s.png":
                action [Function(renpy.sound.stop,"chara_voice"),ShowMenu('screen_gamemenu_history', player), Hide("info")]
                hovered Show(screen="info", i=_('历史记录'), a=_('这份记录描述着清醒时与睡梦中的世界。'))
                unhovered Hide("info")
            imagebutton auto "gui/quickmenu/skip_%s.png":
                selected_hover "gui/quickmenu/skip_selected_idle.png"
                action [Skip(), Hide("info")]
                hovered Show(screen="info", i=_('快进'), a=_('在时间之中，无物还能保持原有的姿态。'))

                unhovered Hide("info")
            imagebutton auto "gui/quickmenu/auto_%s.png":
                selected_hover "gui/quickmenu/auto_selected_idle.png"
                hovered Show(screen="info", i=_('自动前进'), a=_('懒惰之人的选择。'))
                action [Preference("auto-forward", "toggle"), Hide("info")]
                unhovered Hide("info")
            imagebutton auto "gui/quickmenu/hide_%s.png":
                hovered Show(screen="info", i=_('隐藏界面'), a=_('方便大家欣赏美丽的裆部立绘。'))
                action [Function(renpy.sound.stop,"chara_voice"),HideInterface(), Hide("info")]
                unhovered Hide("info")
            imagebutton auto "gui/quickmenu/settings_%s.png":
                hovered Show(screen="info", i=_('设置'), a=_('“路？我们要去的地方不需要……路。”'))
                action [ShowMenu(screen='screen_gamemenu',player=player), Hide("info")]
                unhovered Hide("info")


screen quickmenu(player):
    variant "touch"

    zorder 100

    if quick_menu or replaying:
        hbox:
            xcenter 0.8
            ycenter 0.74
            xalign 0.5
            spacing 40
            if replaying:
                imagebutton auto "gui/quickmenu/stopreplay_%s.png":
                    action [Hide("info"), Jump('afterreplay')]
                    hovered Show(screen="info", i=_('结束剧情回顾'), a=_('我的思绪飘荡，而我紧随其后。'))
                    unhovered Hide("info")

            if config.rollback_enabled:
                imagebutton auto "gui/quickmenu/rollback_%s.png":
                    action [Rollback(), Hide("info")]
                    hovered Show(screen="info", i=_('回退'), a=_('想要回到过去的人太多了，你应该珍惜回退的机会。'))
                    unhovered Hide("info")
            imagebutton auto "gui/quickmenu/history_%s.png":
                action [ShowMenu('screen_gamemenu_history', player), Hide("info")]
                hovered Show(screen="info", i=_('历史记录'), a=_('这份记录描述着清醒时与睡梦中的世界。'))
                unhovered Hide("info")
            imagebutton auto "gui/quickmenu/skip_%s.png":
                selected_hover "gui/quickmenu/skip_selected_idle.png"
                action [Skip(), Hide("info")]
                hovered Show(screen="info", i=_('快进'), a=_('在时间之中，无物还能保持原有的姿态。'))

                unhovered Hide("info")
            imagebutton auto "gui/quickmenu/auto_%s.png":
                selected_hover "gui/quickmenu/auto_selected_idle.png"
                hovered Show(screen="info", i=_('自动前进'), a=_('懒惰之人的选择。'))
                action [Preference("auto-forward", "toggle"), Hide("info")]
                unhovered Hide("info")
            imagebutton auto "gui/quickmenu/hide_%s.png":
                hovered Show(screen="info", i=_('隐藏界面'), a=_('方便大家欣赏美丽的裆部立绘。'))
                action [HideInterface(), Hide("info")]
                unhovered Hide("info")
            imagebutton auto "gui/quickmenu/settings_%s.png":
                hovered Show(screen="info", i=_('设置'), a=_('“路？我们要去的地方不需要……路。”'))
                action [ShowMenu(screen='screen_gamemenu',player=player), Hide("info")]
                unhovered Hide("info")






default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")










screen navigation():
    $renpy.sound.stop(channel="chara_voice")
    $sh()

    pass

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")




screen item_unlocked_screen():

    if DecayCookie in Notice.longmessages:
        $Notice.longmessages.remove(DecayCookie)
        use screen_long_notify('已解锁道具：袋装薄荷味饼干\n可以在零食店中购买。')

    elif 'decaypics' in Notice.longmessages:
        $Notice.longmessagesiremoveppend('decaypics')
        use screen_long_notify('已解锁Decay的私人相册。')

    elif 'solituspics' in Notice.longmessages:
        $Notice.longmessages.remove('solituspics')
        use screen_long_notify('已解锁Solitus的私人相册。')

    elif PathosCookie in Notice.longmessages:
        $Notice.longmessages.remove(PathosCookie)
        use screen_long_notify('已解锁道具：袋装葡萄味饼干\n可以在零食店中购买。')

    elif 'pathospics' in Notice.longmessages:
        $Notice.longmessages.remove('pathospics')
        use screen_long_notify('已解锁Pathos的私人相册。')

    elif AcolasCookie in Notice.longmessages:
        $Notice.longmessages.remove(AcolasCookie)
        use screen_long_notify('已解锁道具：袋装西瓜味饼干\n可以在零食店中购买。')

    elif 'acolaspics' in Notice.longmessages:
        $Notice.longmessages.remove('acolaspics')
        use screen_long_notify('已解锁Acolas的私人相册。')

    elif HallukeCookie in Notice.longmessages:
        $Notice.longmessages.remove(HallukeCookie)
        use screen_long_notify('已解锁道具：袋装奶油味饼干\n可以在零食店中购买。')

    elif 'hallukepics' in Notice.longmessages:
        $Notice.longmessages.remove('hallukepics')
        use screen_long_notify('已解锁Halluke的私人相册。')

    elif 'deplinepics' in Notice.longmessages:
        $Notice.longmessagesiremoveppend('deplinepics')
        use screen_long_notify('已解锁depline的私人相册。')

    elif 'destotpics' in Notice.longmessages:
        $Notice.longmessages.remove('destotpics')
        use screen_long_notify('已解锁Destot的私人相册。')

    elif 'arnelpics' in Notice.longmessages:
        $Notice.longmessages.remove('arnelpics')
        use screen_long_notify('已解锁Arnel的私人相册。')
    

image movie_se_background = Movie(play="images/cg/movie_se_background.webm", size=(1460,881))
image movie_se_mask = "images/cg/movie_se_mask.webp"

image movie_aco_cg_background = Movie(play="images/cg/aco_cg_back.webm", size=(1920,1080))

image movie_aco_cg_mask:
    2
    "images/cg/aco_cg_mask2.webp"
    0.05
    "images/cg/aco_cg_mask3.webp"
    0.05
    "images/cg/aco_cg_mask4.webp"
    0.05
    "images/cg/aco_cg_mask5.webp"
    0.065
    "images/cg/aco_cg_mask4.webp"
    0.05
    "images/cg/aco_cg_mask3.webp"
    0.05
    "images/cg/aco_cg_mask2.webp"
    0.05
    repeat

transform se_transform:
    xoffset 0
    yoffset 0
    parallel:
        easein 0.3 xoffset 3
        easein 0.2 xoffset -1
        easein 0.2 xoffset 0
        0.2
        easein 0.3 xoffset 1
        easein 0.2 xoffset -3
        easein 0.3 xoffset 3
        easein 0.2 xoffset -1
        easein 0.2 xoffset 0
        repeat
    parallel:
        easein 0.2 yoffset 8
        easein 0.3 yoffset -4
        easein 0.2 yoffset 0
        0.2
        easein 0.2 yoffset 4
        easein 0.3 yoffset -8
        easein 0.2 yoffset 8
        easein 0.3 yoffset -4
        easein 0.2 yoffset 0
        repeat

transform movie_aco_cg_mask_transform:
    xoffset 0
    yoffset 0
    parallel:
        easein 0.3 xoffset 2
        easein 0.2 xoffset -1
        0.2
        easein 0.3 xoffset 0
        easein 0.2 xoffset 1
        0.75

        repeat
    parallel:
        easein 0.4 yoffset 4
        easein 0.6 yoffset 2
        easein 0.4 yoffset 0
        easein 0.6 yoffset 2
        easein 0.4 yoffset 4
        1
        repeat



screen main_menu():
    
    tag menu
    style_prefix "main_menu"


    # 列车背景
    if persistent.main_menu_theme == Theme_train:
        add "images/cg/se.webp" xalign 1.0
        add 'movie_se_background' xalign 1.0
        add "movie_se_mask" xcenter 0.5 ycenter 0.5 at se_transform
        


    # aco cg 背景
    elif persistent.main_menu_theme == Theme_acolas:
        add "images/cg/aco_cg_back.webp"
        add 'movie_aco_cg_background'
        add "images/cg/aco_cg_mask1.webp" xcenter 0.5 ycenter 0.5 at movie_aco_cg_mask_transform
        add "movie_aco_cg_mask" xcenter 0.5 ycenter 0.5 at movie_aco_cg_mask_transform

    else:
        add persistent.main_menu_theme.bg
    

    $ui_font = persistent.main_menu_theme.ui_font

    python:
        def getstarttime(x):
            return 0.3 + 0.15 * x
    add "gui/logo.png" at trans_mainmenu(getstarttime(0))

         



    vbox:
        xcenter 0.21
        ycenter 0.725
        spacing 10
        

        if Saver.get_newest():
            textbutton _("继续"):
                action Function(Saver.load, Saver.get_newest())
                at trans_mainmenu(getstarttime(1))
                background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                text_style ui_font
                text_size 58
                text_xpos 0.1
                xsize 300

            textbutton _("新游戏"):
                action ShowMenu("screen_init_select")
                background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                at trans_mainmenu(getstarttime(2))
                text_style ui_font
                text_size 58
                text_xpos 0.1
                xsize 300


        else:

            textbutton _("继续"):
                action NullAction()
                at trans_mainmenu(getstarttime(1))
                text_style ui_font
                text_size 58
                text_xpos 0.1
                xsize 300
                text_color '#8888887f'

            textbutton _("新游戏"):
                action ShowMenu("screen_init_select")
                background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                at trans_mainmenu(getstarttime(2))
                text_style ui_font
                text_size 58
                text_xpos 0.1
                xsize 300

        textbutton _("读取"):
            action ShowMenu("screen_gamemenu_save", None)
            background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
            at trans_mainmenu(getstarttime(3))
            text_style ui_font
            text_size 58
            text_xpos 0.1
            xsize 300

        textbutton _("设置"):
            action ShowMenu("screen_gamemenu_preferences", None)
            background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
            at trans_mainmenu(getstarttime(4))
            text_style ui_font
            text_size 58
            text_xpos 0.1
            xsize 300

        textbutton _("成就"):
            action ShowMenu("screen_gamemenu_achievement", None)
            background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
            at trans_mainmenu(getstarttime(5))
            text_style ui_font
            text_size 58
            text_xpos 0.1
            xsize 300

        textbutton ""

        textbutton _("退出"):
            action Quit(confirm=not main_menu)
            background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
            at trans_mainmenu(getstarttime(6))
            text_style ui_font
            text_size 58
            text_xpos 0.1
            xsize 300
            
    vbox:
        xpos 1.01
        ypos 1.02
        imagebutton idle "gui/new.png" at app_transform,trans_mainmenu(getstarttime(12)):
            action ShowMenu("screen_gamemenu_new")
            xalign 1.0
        textbutton "v[config.version]" at trans_mainmenu(getstarttime(7)):
            xalign 1.0
            text_size 28
            text_style ui_font
        textbutton _("药：绝望的解决手段") at trans_mainmenu(getstarttime(8)):
            xalign 1.0
            text_size 28
            text_style ui_font
            if Achievement402.has():
                action Start('eggs1')

    vbox:
        xalign 1.0
        yalign 0.05

        imagebutton idle "gui/qq.png" action OpenURL("http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=ILURTWhqOeD2aSBxb0L_fqccTYv_Wdap&authKey=oWhqP%2BPxzDDPRw5M0W%2FkWcJaQeWYx%2F177xhXyIgc3p80jB84H9kzlFWVOuYphTYE&noverify=0&group_code=797308562") at app_transform,trans_mainmenu(getstarttime(9))
        imagebutton idle "gui/pd.png" action OpenURL("https://pd.qq.com/s/heao2f9kp") at app_transform,trans_mainmenu(getstarttime(10))
        imagebutton idle "gui/afd.png" action OpenURL("https://afdian.net/a/yuxiu") at app_transform,trans_mainmenu(getstarttime(11))
        
    
    use item_unlocked_screen()




style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")










screen game_menu(title, scroll=None, yinitial=0.0, navi=True):

    style_prefix "game_menu"

    add persistent.main_menu_theme.bg

    frame:
        style "game_menu_outer_frame"

        has hbox


        frame:
            style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":

                viewport:
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    has vbox
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial yinitial

                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    transclude

            else:

                transclude
    if navi:
        use navigation

    textbutton _("返回"):
        style "return_button"

        action Return()

    label title at trans_Down()

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/confirm.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1850

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45








screen about():
    tag menu
    pass


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

screen load():
    tag menu
    pass

screen save():
    tag menu
    pass




screen preferences(player=None):
    tag menu
    use screen_gamemenu(player)

                        
                
                


                


screen info_i_type(player, item, width=400, pp=renpy.get_mouse_pos()):
    style_prefix "info"
    zorder 2002

    python:
        t=item.name
        i=item.info
        a=item.ad

    
        (xc,trans) = (0.0,trans_toLeft) if pp[0] < 1500 else (1.0,trans_toRight)
        yc = 0.0 if pp[1] < 540 else 1.0
        if width == 400:
            if a:
                if len(i) + len(a) > 150:
                    width = 600
            else:
                if len(i) > 100:
                    width = 600
    frame:
        pos pp
        padding (15, 15)
        xanchor xc
        yanchor yc
        at trans()

        
        hbox:
            vbox:
                align pp
                    

                if t is not None:
                    label '[t!t]\n':
                        text_style "info_text"
                        xsize width
                if i is not None:
                    label '{size=-2}[i!t]{/size}':
                        text_style "info_text"
                        xsize width
                if a is not None:
                    null height 16
                    label '{i}[a!t]{/i}':
                        text_style "admonition_text"
                        xsize width
            null width -75
            vbox:
                add item.icon()




style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675









screen history():




    predict False tag menu

    use game_menu(_("历史"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        vbox:
            spacing 30
            for h in _history_list:

                hbox:

                    if h.who:

                        label h.who:
                            style "history_name"
                            substitute False




                            if "color" in h.who_args:
                                text_color h.who_args["color"]

                        text h.what:
                            xpos 0.04
                            yalign 0.5
                            substitute False
                            size 29
                            xsize 950


                    else:

                        text h.what:
                            yalign 0.5
                            substitute False
                            size 29
                            xsize 950



        if not _history_list:
            label _("对话历史记录为空。")




define gui.history_allow_tags = { "alt", "noalt" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5







screen help():
    pass












screen confirm(message, yes_action=None, no_action=None):


    modal True
    tag menu

    zorder 99999

    style_prefix "transparent"


    add "gui/overlay/confirm.png"

    frame:
        xalign .5
        yalign .5
        padding (60, 40)
        background '#0000004f'

        has vbox:
            xalign .5
            yalign .5
            spacing 45

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 150

            if yes_action is not None:
                textbutton _("{size=-3}确定{/size}") action yes_action
            if no_action is not None:
                textbutton _("{size=-3}取消{/size}") action no_action


    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame(["gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")








screen skip_indicator():

    zorder 2000
    style_prefix "skip"

    frame:

        has hbox:
            spacing 9

        text _("正在快进")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"

screen replaying_indicator():

    zorder 2000
    style_prefix "skip"
    if replaying and not renpy.get_skipping():
        frame:
            has hbox:
                spacing 9

            text _("剧情回顾中")

            text "•" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "•" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "•" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform delayed_blink(delay, cycle):
    alpha .5

    pause delay
    block:

        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:

    font "DejaVuSans.ttf"








screen notify(message):

    zorder 100
    style_prefix "info"

    frame at notify_appear:
        text _("[message!tq]")
        ypos gui.notify_ypos

    timer 3 action Hide('notify')


transform notify_appear:
    alpha 0.0
    xoffset -100
    easein 0.2 xoffset 100 alpha 1.0
    linear 0.2 xoffset -40
    linear 0.05 xoffset 20
    linear 0.05 xoffset -10
    linear 0.1 xoffset 0







    on hover:
        linear 0.2 xoffset -50
    on hide:

        xoffset 0
        easein 0.2 xoffset 50
        easein 0.2 xoffset -200 alpha 0



style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")









screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing


        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)



        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed:
                yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id



define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")







style pref_vbox:
    variant "medium"
    xsize 675


screen quick_menu():
    variant "touch"




style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
