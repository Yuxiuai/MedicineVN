init offset = -1










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





screen quick_menu()


screen quickmenu(player):
    zorder 100

    if quick_menu:
        hbox:
            xcenter 0.8
            ycenter 0.75
            xalign 0.5
            spacing 25
            if config.rollback_enabled == True:
                imagebutton auto "gui/quickmenu/rollback_%s.png":
                    action [Rollback(), Hide("info")]
                    hovered Show(screen="info", i='回退', a='想要回到过去的人太多了，你应该珍惜回退的机会。')
                    unhovered Hide("info")
            imagebutton auto "gui/quickmenu/history_%s.png":
                action [ShowMenu('history'), Hide("info")]
                hovered Show(screen="info", i='历史记录', a='这份记录描述着清醒时与睡梦中的世界。')
                unhovered Hide("info")
            imagebutton auto "gui/quickmenu/skip_%s.png":
                selected_hover "gui/quickmenu/skip_selected_idle.png"
                action [Skip(), Hide("info")]
                hovered Show(screen="info", i='快进', a='在时间之中，无物还能保持原有的姿态。')

                unhovered Hide("info")
            imagebutton auto "gui/quickmenu/auto_%s.png":
                selected_hover "gui/quickmenu/auto_selected_idle.png"
                hovered Show(screen="info", i='自动前进', a='懒惰之人的选择。')
                action [Preference("auto-forward", "toggle"), Hide("info")]
                unhovered Hide("info")
            imagebutton auto "gui/quickmenu/hide_%s.png":
                hovered Show(screen="info", i='隐藏界面', a='方便大家欣赏美丽的裆部立绘。')
                action [HideInterface(), Hide("info")]
                unhovered Hide("info")
            imagebutton auto "gui/quickmenu/settings_%s.png":
                hovered Show(screen="info", i='设置', a='“路？我们要去的地方不需要……路。”')
                action [ShowMenu(screen='preferences',player=player), Hide("info")]
                unhovered Hide("info")


screen quickmenu(player):
    variant "touch"

    zorder 100

    if quick_menu:
        hbox:
            xcenter 0.8
            ycenter 0.75
            xalign 0.5
            spacing 40
            if config.rollback_enabled == True:
                imagebutton auto "gui/quickmenu/rollback_%s.png":
                    action [Rollback(), Hide("info")]
                    hovered Show(screen="info", i='回退', a='想要回到过去的人太多了，你应该珍惜回退的机会。')
                    unhovered Hide("info")
            imagebutton auto "gui/quickmenu/history_%s.png":
                action [ShowMenu('history'), Hide("info")]
                hovered Show(screen="info", i='历史记录', a='这份记录描述着清醒时与睡梦中的世界。')
                unhovered Hide("info")
            imagebutton auto "gui/quickmenu/skip_%s.png":
                selected_hover "gui/quickmenu/skip_selected_idle.png"
                action [Skip(), Hide("info")]
                hovered Show(screen="info", i='快进', a='在时间之中，无物还能保持原有的姿态。')

                unhovered Hide("info")
            imagebutton auto "gui/quickmenu/auto_%s.png":
                selected_hover "gui/quickmenu/auto_selected_idle.png"
                hovered Show(screen="info", i='自动前进', a='懒惰之人的选择。')
                action [Preference("auto-forward", "toggle"), Hide("info")]
                unhovered Hide("info")
            imagebutton auto "gui/quickmenu/hide_%s.png":
                hovered Show(screen="info", i='隐藏界面', a='方便大家欣赏美丽的裆部立绘。')
                action [HideInterface(), Hide("info")]
                unhovered Hide("info")
            imagebutton auto "gui/quickmenu/settings_%s.png":
                hovered Show(screen="info", i='设置', a='“路？我们要去的地方不需要……路。”')
                action [ShowMenu(screen='preferences',player=player), Hide("info")]
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

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing



        if not main_menu:

            textbutton _("历史") action ShowMenu("history")



        textbutton _("读取") action ShowMenu("load")

        textbutton _("设置") action ShowMenu("preferences")

        textbutton _("成就") action ShowMenu("achievements")

        if persistent.ne or config.developer:
            textbutton _("鸣谢") action Start("credits")

        if config.developer == True and main_menu:
            textbutton _("快速开始") action Start("testStart")

        if not main_menu:

            textbutton _("标题界面") action Start("to_the_title")

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")








screen main_menu():




    style_prefix "main_menu" tag menu

    add gui.main_menu_background
    use main_menu_navigation()


screen main_menu_navigation():
    python:
        def getstarttime(x):
            return 0.3 + 0.15 * x
    add "gui/logo.png" at trans_mainmenu(getstarttime(0))

    vbox:
        xcenter 0.182
        ycenter 0.752
        spacing gui.navigation_spacing
        if persistent.savefile[0]:
            textbutton _ ("{color=#000000}{alpha=*0.7}{size=+4}    继续{/color}{/size}{/alpha}") at trans_mainmenu(getstarttime(1))
            textbutton _("{color=#000000}{alpha=*0.7}{size=+4}从头开始{/color}{/size}{/alpha}") at trans_mainmenu(getstarttime(2))
        else:
            textbutton _ ("{color=#000000}{alpha=*0.7}{size=+4}    继续{/color}{/size}{/alpha}") at trans_mainmenu(getstarttime(1))
            textbutton _("{color=#000000}{alpha=*0.7}{size=+4}从头开始{/color}{/size}{/alpha}") at trans_mainmenu(getstarttime(2))

        textbutton _("{color=#000000}{alpha=*0.7}{size=+4}    读取{/color}{/size}{/alpha}") at trans_mainmenu(getstarttime(3))
        textbutton _("{color=#000000}{alpha=*0.7}{size=+4}    设置{/color}{/size}{/alpha}") at trans_mainmenu(getstarttime(4))
        textbutton _("")
        textbutton _("{color=#000000}{alpha=*0.7}{size=+4}    退出{/color}{/size}{/alpha}") at trans_mainmenu(getstarttime(5))

    vbox:
        xcenter 0.932
        ycenter 0.977
        textbutton _("{color=#000000}{alpha=*0.7}{size=-4}Version：[config.version]{/color}{/size}{/alpha}") at trans_mainmenu(getstarttime(6)):
            xalign 1.0
        textbutton _("{color=#000000}{size=-4}{alpha=*0.7}药：绝望的解决手段{/color}{/size}{/alpha}") at trans_mainmenu(getstarttime(7)):
            xalign 1.0

    vbox:
        xcenter 0.18
        ycenter 0.75
        spacing gui.navigation_spacing
        if persistent.savefile[0]:
            textbutton _ ("{size=+4}    继续{/size}"):
                action Function(Save.load, persistent.savefile[0])
                at trans_mainmenu(getstarttime(1))

            textbutton _("{size=+4}从头开始{/size}"):
                action Show(screen="confirm",message="是否删除上一个存档，重新开始游玩？\n（遗失的存档无法找回）", yes_action=Start(), no_action=Hide("confirm"))
                at trans_mainmenu(getstarttime(2))


        else:

            textbutton _ ("{size=+4}{color=#8888887f}    继续{/size}{/color}"):
                action NullAction()
                at trans_mainmenu(getstarttime(1))

            textbutton _("{size=+4}从头开始{/size}"):
                action Start()
                at trans_mainmenu(getstarttime(2))

        textbutton _("{size=+4}    读取{/size}"):
            action ShowMenu("load")
            at trans_mainmenu(getstarttime(3))

        textbutton _("{size=+4}    设置{/size}"):
            action ShowMenu("preferences")
            at trans_mainmenu(getstarttime(4))

        textbutton _("")

        textbutton _("{size=+4}    退出{/size}"):
            action Quit(confirm=not main_menu)
            at trans_mainmenu(getstarttime(5))
    vbox:
        xcenter 0.93
        ycenter 0.975
        textbutton _("{color=#FFFFFF}{size=-4}Version：[config.version]") at trans_mainmenu(getstarttime(6)):
            xalign 1.0
        textbutton _("{color=#FFFFFF}{size=-4}药：绝望的解决手段") at trans_mainmenu(getstarttime(7)):
            xalign 1.0




style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

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

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

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

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

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




    use game_menu(_("关于"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("版本 [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"

            text _("引擎：{a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size










screen saving_info(t=None, i=None, a=None, width=400, pp=renpy.get_mouse_pos(), slot, mode):
    use barrier(screen="saving_info")
    style_prefix "info"
    zorder 400
    $ (xc,trans) = (0.0,trans_toLeft) if pp[0] < 1500 else (1.0,trans_toRight)
    $ yc = 0.0 if pp[1] < 540 else 1.0
    frame:
        pos pp
        padding (15, 15)
        xanchor xc
        yanchor yc
        at trans()

        has vbox:
            align pp
        if t is not None:
            label t+'\n':
                text_style "info_text"
                xsize width
        if i is not None:
            label '{size=-2}' + i + '{/size}':
                text_style "info_text"
                xsize width
        if a is not None:
            null height 16
            label '{i}' + a + '{/i}':
                text_style "admonition_text"
                xsize width
        null height 30
        hbox:
            xalign 0.5
            spacing 15
            textbutton _("{size=-3}读档{/size}"):
                action [Function(Save.load, slot), Return()]
                activate_sound audio.cursor
            if mode < 0:
                textbutton _("{size=-3}保留{/size}"):
                    action [Function(Save.record, slot), Function(renpy.save_persistent), Hide("saving_info")]
                    activate_sound audio.cursor
            else:
                textbutton _("{size=-3}删除{/size}"):
                    action [Function(Save.delete, mode), Function(renpy.save_persistent), Hide("saving_info")]
                    activate_sound audio.cursor
            textbutton _("{size=-3}返回{/size}"):
                action Hide("saving_info")
                activate_sound audio.cursor

    key 'K_ESCAPE' action Hide("saving_info")

screen saveslot(slot, mode=-1):
    python:
        savename = '空存档'
        slotname = None
        slotinfo = None
        if slot:
            if slot.cured > -1:
                savename = '「%s」⎟手术后的第%s天' % (slot.name, slot.cured)
            elif Despair.has(slot):
                savename = '「%s」⎟废墟下的第%s天' % (slot.name, slot.finalStageDays)
            else:
                savename = '「%s」⎟第%s周⎟%s' % (slot.name, slot.week, weekdayFormat(slot.today))

            if mode >= 0:
                savename += '⎟%s' % slot.savetime
            slotname = '{size=+5}'+slot.name+'{/size}'
            slotinfo = '精神状态: %s\n剩余药物: %s\n所持金钱: %s\n工作进度: %s\n\n严重程度: %s\n工作能力: %s\n身体素质: %s\n写作技巧: %s' % (slot.mental, slot.meds(), slot.money, r2(slot.achievedGoal/slot.goal), slot.severity, slot.working, slot.physical, slot.writing)
            if hasattr(slot, 'version'):
                slotinfo += '\n\n存档版本：%s' % slot.version 

    frame:
        background None
        ysize 50
        textbutton savename text_style 'white':
            if slot:
                action Show(screen="saving_info", t=slotname, i=slotinfo, slot=slot, mode=mode)
            elif not slot and not persistent.savefile[0]:
                action Show(screen="info_use", i='起过名后才能存档。', width=250)
            else:
                action Function(Save.record_poz, mode)
            background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
            xfill True
            activate_sound audio.cursor
        if mode > -1:
            textbutton str(mode+1) text_style 'white':
                action NullAction()
                xalign 0.975
                yalign 0.2
        if mode == -1:
            textbutton '今天' text_style 'white':
                action NullAction()
                xalign 0.975
                yalign 0.2
        if mode == -2:
            textbutton '昨天' text_style 'white':
                action NullAction()
                xalign 0.975
                yalign 0.2



screen load():
    tag menu


    use game_menu(_("读取"), scroll="viewport"):

        vbox:
            spacing 10

            if not persistent.savefile[0] and not persistent.savefile[1] and not persistent.savefile[2]:

                textbutton '{size=-5}目前还没有存档。{/size}' text_style "white":
                    action NullAction()
                    xfill True
                    xalign 1.0
                    activate_sound audio.cursor
                    xoffset -5

            if persistent.savefile[0] or persistent.savefile[1]:

                textbutton '{size=-5}暂时存档{/size}' text_style "white":
                    action NullAction()
                    xfill True
                    xalign 1.0
                    activate_sound audio.cursor
                    xoffset -5

            if persistent.savefile[0]:

                use saveslot(persistent.savefile[0])

            if persistent.savefile[1]:

                use saveslot(persistent.savefile[1], -2)

            if persistent.savefile[2]:

                textbutton '{size=-5}已保存的存档{/size}' text_style "white":
                    action NullAction()
                    xfill True
                    xalign 1.0
                    activate_sound audio.cursor
                    xoffset -5

                for poz, slot in enumerate(persistent.savefile[2]):
                    use saveslot(slot, poz)



screen save():
    tag menu


    use preferences()



screen diff_select(player=player):
    use barrier(screen="diff_select")
    style_prefix "info"
    zorder 400
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
        xsize 150
        at trans()
        has vbox
        frame:
            background None
            ysize 50
            textbutton _("极易") text_style 'white':
                action [Function(GameDifficulty1.add, player),Hide("diff_select"),Hide('info')]
                hovered Show(screen='info', i='游戏难度：极易\n\n勾选此项后，将游戏难度设置为极易。\n在此难度下，大幅度降低精神状态的消耗，睡眠消耗的精神状态并大幅度提高精神状态的恢复。',width=600)
                unhovered Hide('info')
                background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor
            if GameDifficulty1.has(player):
                imagebutton idle "gui/phone/right_.png":
                    xalign 1.0
                    yalign 0.5

        frame:
            background None
            ysize 50
            textbutton _("较易") text_style 'white':
                action [Function(GameDifficulty2.add, player),Hide("diff_select"),Hide('info')]
                hovered Show(screen='info', i='游戏难度：较易\n\n勾选此项后，将游戏难度设置为较易。\n在此难度下，低精神状态的消耗，睡眠消耗的精神状态并提高精神状态的恢复。',width=600)
                unhovered Hide('info')
                background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor
            if GameDifficulty2.has(player):
                imagebutton idle "gui/phone/right_.png":
                    xalign 1.0
                    yalign 0.5

        frame:
            background None
            ysize 50
            textbutton _("一般") text_style 'white':
                action [Function(GameDifficulty3.add, player),Hide("diff_select"),Hide('info')]
                hovered Show(screen='info', i='游戏难度：一般\n\n勾选此项后，将游戏难度设置为一般。',width=600)
                unhovered Hide('info')
                background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor
            if GameDifficulty3.has(player):
                imagebutton idle "gui/phone/right_.png":
                    xalign 1.0
                    yalign 0.5

        frame:
            background None
            ysize 50
            textbutton _("较难") text_style 'white':
                action [Function(GameDifficulty4.add, player),Hide("diff_select"),Hide('info')]
                hovered Show(screen='info', i='游戏难度：较难\n\n勾选此项后，将游戏难度设置为较难。\n在此难度下，提高精神状态的消耗和睡眠消耗的精神状态。',width=600)
                unhovered Hide('info')
                background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor
            if GameDifficulty4.has(player):
                imagebutton idle "gui/phone/right_.png":
                    xalign 1.0
                    yalign 0.5

        frame:
            background None
            ysize 50
            textbutton _("极难") text_style 'white':
                action [Function(GameDifficulty5.add, player),Hide("diff_select"),Hide('info')]
                hovered Show(screen='info', i='游戏难度：极难\n\n勾选此项后，将游戏难度设置为极难。\n在此难度下，提升更多精神状态的消耗，睡眠消耗的精神状态并降低精神状态的恢复。',width=600)
                unhovered Hide('info')
                background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor
            if GameDifficulty5.has(player):
                imagebutton idle "gui/phone/right_.png":
                    xalign 1.0
                    yalign 0.5

    key 'K_ESCAPE' action Hide("info_confirm")

screen window_select:
    use barrier(screen="window_select")
    style_prefix "info"
    zorder 400
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
        xsize 150
        at trans()
        has vbox
        frame:
            background None
            ysize 50
            textbutton _("窗口") text_style 'white':
                action [SetVariable("preferences.fullscreen", False),Hide("window_select"),Hide('info')]
                hovered Show(screen='info', i='窗口\n\n勾选此项后，游戏以窗口模式进行。',width=600)
                unhovered Hide('info')
                background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor
            if not preferences.fullscreen:
                imagebutton idle "gui/phone/right_.png":
                    xalign 0.975
                    yalign 0.5
        frame:
            background None
            ysize 50
            textbutton _("全屏") text_style 'white':
                action [SetVariable("preferences.fullscreen", True),Hide("window_select"),Hide('info')]
                hovered Show(screen='info', i='全屏\n\n勾选此项后，游戏以全屏模式进行。',width=600)
                unhovered Hide('info')
                background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor
            if preferences.fullscreen:
                imagebutton idle "gui/phone/right_.png":
                    xalign 0.975
                    yalign 0.5

screen lang_select:
    use barrier(screen="lang_select")
    style_prefix "info"
    zorder 400
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
            textbutton _("中文") text_style 'white':
                action [Language(None),Hide("lang_select")]
                background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor
            if preferences.language == None:
                imagebutton idle "gui/phone/right_.png":
                    xalign 0.975
                    yalign 0.5
        frame:
            background None
            ysize 50
            textbutton _("English") text_style 'white':
                action [Language('english'),Hide("lang_select")]
                background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor
            if preferences.language == 'english':
                imagebutton idle "gui/phone/right_.png":
                    xalign 0.975
                    yalign 0.5













screen notify_select:
    use barrier(screen="notify_select")
    style_prefix "info"
    zorder 400
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
        xsize 230
        at trans()
        has vbox
        frame:
            background None
            ysize 50
            textbutton _("较短（3秒）") text_style 'white':
                action [SetVariable("persistent.notifyDuration", 3),Function(renpy.save_persistent), Hide("notify_select")]
                background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor
            if persistent.notifyDuration == 3:
                imagebutton idle "gui/phone/right_.png":
                    xalign 0.975
                    yalign 0.5
        frame:
            background None
            ysize 50
            textbutton _("正常（5秒）") text_style 'white':
                action [SetVariable("persistent.notifyDuration", 5),Function(renpy.save_persistent), Hide("notify_select")]
                background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor
            if persistent.notifyDuration == 5:
                imagebutton idle "gui/phone/right_.png":
                    xalign 0.975
                    yalign 0.5
        frame:
            background None
            ysize 50
            textbutton _("较久（10秒）") text_style 'white':
                action [SetVariable("persistent.notifyDuration", 10),Function(renpy.save_persistent), Hide("notify_select")]
                background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor
            if persistent.notifyDuration == 10:
                imagebutton idle "gui/phone/right_.png":
                    xalign 0.975
                    yalign 0.5

screen challenges_select(player=player):
    use barrier(screen="challenges_select")
    style_prefix "info"
    zorder 400
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

            $ i_gm1 = '开启该模式后，锁定难度为极难，同时游戏的难度会大幅上升，具体效果如下。\n\n偏头痛：每完成一个日程都会额外随机消耗精神状态。\n资源供给：立刻获得1000元，但后续药价的自然增长幅度提升150%。\n自卑感：立刻获得20点全属性，但过夜后每个能力属性都有50%的概率失去1%，25%的概率永久提升1%严重程度。\n理财不善：所持金钱大于500元时，过夜后失去10%的当前金钱。\n效率低下：每周需要完成的工作每周都会提升3%。\n药物过敏：药物恢复效果小幅度提升15%，过夜后有33%的概率提升随机一种已经使用过的药物的抗药性。\n\n{color=#ff0000}仅在第一周内可添加！\n添加后无法解除！{/color}'

            textbutton _("挑战模式") text_style 'white':
                if player.week < 2:
                    action [Hide("info"),Show(screen="info_confirm", i=i_gm1,width=600,pp=renpy.get_mouse_pos(),act=Function(GameModule1.add, player))]
                else:
                    action [Hide("info"),Show(screen="info_use", i=i_gm1,width=600,pp=renpy.get_mouse_pos())]

                hovered Show(screen='info', i=i_gm1,width=600)
                unhovered Hide('info')
                background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor
            if GameModule1.has(player):
                imagebutton idle "gui/phone/right_.png":
                    xalign 0.975
                    yalign 0.5

        frame:
            background None
            ysize 50

            $ i_gm2 = '（由糖迷白提供）\n获得名为无尽之旅的书籍，阅读后可以随机获得一张全新的带有特殊效果的手稿。\n\n{color=#ff0000}添加后无法解除！{/color}'

            textbutton _("无尽之旅") text_style 'white':
                action [Hide("info"),Show(screen="info_confirm", i=i_gm2,width=600,pp=renpy.get_mouse_pos(),act=Function(GameModule2.add, player))]
                hovered Show(screen='info', i=i_gm2 ,width=600)
                unhovered Hide('info')
                background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor
            if GameModule2.has(player):
                imagebutton idle "gui/phone/right_.png":
                    xalign 0.975
                    yalign 0.5



    key 'K_ESCAPE' action Hide("info_confirm")

screen music_setting:
    use barrier(screen="music_setting")
    style_prefix "info"
    zorder 400
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
            bar value Preference("music volume"):
                xfill True

screen sound_setting:
    use barrier(screen="sound_setting")
    style_prefix "info"
    zorder 400
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
            bar value Preference("sound volume"):
                xfill True




#renpy.get_game_runtime()
screen achievements(player=None):
    tag menu


    use game_menu(_("成就"), scroll="viewport"):

        vbox:
            spacing 10
            textbutton '{size=-5}成就总览{/size}' text_style "white":
                action NullAction()
                xfill True
                xalign 1.0
                activate_sound audio.cursor
                xoffset -5
            frame:
                background None
                ysize 50
                textbutton _("已达成的成就") text_style 'white':
                    action NullAction()
                    background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                    xfill True
                    activate_sound audio.cursor
                textbutton '%s / %s' % (len(Achievement.done()), len(getSubclasses(Achievement))) text_style 'white':
                    action NullAction()
                    xalign 0.975
                    yalign 0.2
            
            frame:
                background None
                ysize 50
                $runtime_h = int(persistent.runtime//60//60)
                $runtime_m = int((persistent.runtime - runtime_h *60*60)//60)
                $runtime_s = int((persistent.runtime - runtime_h *60*60 - runtime_m *60))
                textbutton _("游玩时间") text_style 'white':
                    action NullAction()
                    background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                    xfill True
                    activate_sound audio.cursor
                textbutton '%s小时%s分%s秒' % (runtime_h, runtime_m, runtime_s) text_style 'white':
                    action NullAction()
                    xalign 0.975
                    yalign 0.2
            if Achievement.done():
                textbutton '{size=-5}已达成的成就{/size}' text_style "white":
                    action NullAction()
                    xfill True
                    xalign 1.0
                    activate_sound audio.cursor
                    xoffset -5
                

            for i in Achievement.done():
                frame:
                    background None
                    ysize 110
                    hbox:
                        imagebutton idle i.icon
                        null width 10
                        vbox:
                            text i.name style 'white':
                                xfill True
                                yoffset 20
                            text i.info style 'admonition_text':
                                xfill True
                                yoffset 13
                    textbutton '{size=-7}%s 解锁{/size}' % (persistent.achievements[i]) text_style 'white':
                        action NullAction()
                        xalign 0.975
                        yalign 0.2
            if Achievement.undone():
                textbutton '{size=-5}未达成的成就{/size}' text_style "white":
                    action NullAction()
                    xfill True
                    xalign 1.0
                    activate_sound audio.cursor
                    xoffset -5

            for i in Achievement.undone():
                frame:
                    background None
                    ysize 110
                    hbox:
                        imagebutton idle "gui/achievements/unknownAchievement.png"
                        null width 10
                        vbox:
                            text '？' * len(i.name) style 'white':
                                xfill True
                                yoffset 20
                            text '？' * len(i.info) style 'admonition_text':
                                xfill True
                                yoffset 13




screen preferences(player=None):
    tag menu


    use game_menu(_("设置"), scroll="viewport"):

        vbox:
            spacing 10
            if player:
                textbutton '{size=-5}游戏性设置{/size}' text_style "white":
                    action NullAction()
                    xfill True
                    xalign 1.0
                    activate_sound audio.cursor
                    xoffset -5
                frame:
                    background None
                    ysize 50
                    textbutton _("游戏难度") text_style 'white':
                        if GameModule1.has(player):
                            action [Show(screen="info_use", i='难度已被锁定，无法更改难度。',width=300,pp=renpy.get_mouse_pos())]
                        else:
                            action [Show(screen='diff_select',player=player)]
                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if GameDifficulty1.has(player):
                        textbutton _("极易") text_style 'white':
                            action NullAction()
                            xalign 0.975
                            yalign 0.2
                    if GameDifficulty2.has(player):
                        textbutton _("较易") text_style 'white':
                            action NullAction()
                            xalign 0.975
                            yalign 0.2
                    if GameDifficulty3.has(player):
                        textbutton _("一般") text_style 'white':
                            action NullAction()
                            xalign 0.975
                            yalign 0.2
                    if GameDifficulty4.has(player):
                        textbutton _("较难") text_style 'white':
                            action NullAction()
                            xalign 0.975
                            yalign 0.2
                    if GameDifficulty5.has(player):
                        textbutton _("极难") text_style 'white':
                            action NullAction()
                            xalign 0.975
                            yalign 0.2

                frame:
                    $ challenges = 0
                    background None
                    ysize 50
                    textbutton _("模组管理") text_style 'white':
                        action [Show(screen='challenges_select',player=player)]
                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if GameModule1.has(player):
                        $ challenges+=1
                    if GameModule2.has(player):
                        $ challenges+=1
                    textbutton '已开启模组数：%s' % challenges text_style 'white':
                        action NullAction()
                        xalign 0.975
                        yalign 0.2




            textbutton '{size=-5}系统设置{/size}' text_style "white":
                action NullAction()
                xfill True
                xalign 1.0
                activate_sound audio.cursor
                xoffset -5

            if renpy.variant("pc") or renpy.variant("web"):
                frame:
                    background None
                    ysize 50
                    textbutton _("显示") text_style 'white':
                        action [Show(screen='window_select')]
                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if not preferences.fullscreen:
                        textbutton _("窗口") text_style 'white':
                            action NullAction()
                            xalign 0.975
                            yalign 0.2
                    if preferences.fullscreen:
                        textbutton _("全屏") text_style 'white':
                            action NullAction()
                            xalign 0.975
                            yalign 0.2


            frame:
                background None
                ysize 50
                textbutton _("语言") text_style 'white':
                    action [Show(screen='lang_select')]
                    background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                    xfill True
                    activate_sound audio.cursor
                if preferences.language == None:
                    textbutton _("中文") text_style 'white':
                        action NullAction()
                        xalign 0.975
                        yalign 0.2
                if preferences.language == 'english':
                    textbutton _("English") text_style 'white':
                        action NullAction()
                        xalign 0.975
                        yalign 0.2

            frame:
                background None
                ysize 50
                textbutton _("音乐音量") text_style 'white':
                    action Show(screen='music_setting')
                    background Frame("gui/style/grey_idle_background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                    xfill True


                textbutton str(int(100*preferences.get_volume('music'))) + '%' text_style 'white':
                    action NullAction()
                    xalign 0.975
                    yalign 0.2

            frame:
                background None
                ysize 50
                textbutton _("音效音量") text_style 'white':
                    action Show(screen='sound_setting')
                    background Frame("gui/style/grey_idle_background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                    xfill True

                textbutton str(int(100*preferences.get_volume('sfx'))) + '%' text_style 'white':
                    action NullAction()
                    xalign 0.975
                    yalign 0.2


            frame:
                background None
                ysize 50
                textbutton _("跳过未读文本") text_style 'white':
                    action [ToggleVariable("preferences.skip_unseen", true_value=True, false_value=False), Function(renpy.save_persistent)]
                    background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                    xfill True
                    activate_sound audio.cursor
                if preferences.skip_unseen:
                    imagebutton idle "gui/phone/right_.png":
                        xalign 0.975
                        yalign 0.2

            textbutton '{size=-5}个性化设置{/size}' text_style "white":
                action NullAction()
                xfill True
                xalign 1.0
                activate_sound audio.cursor
                xoffset -5

            frame:
                background None
                ysize 50
                textbutton _("精确显示状态效果") text_style 'white':
                    action [ToggleVariable("persistent.PreciseDisplay", true_value=True, false_value=False), Function(renpy.save_persistent)]
                    hovered Show(screen='info', i='数值详细显示\n\n勾选此项后，游戏内的状态的介绍文字将更详细地描述其效果。\n\n例：\n提升少量精神状态消耗 -> 提升10%精神状态消耗。',width=600)
                    unhovered Hide('info')
                    background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                    xfill True
                    activate_sound audio.cursor
                if persistent.PreciseDisplay:
                    imagebutton idle "gui/phone/right_.png":
                        xalign 0.975
                        yalign 0.2

            frame:
                background None
                ysize 50
                textbutton _("显示基础能力数值") text_style 'white':
                    action [ToggleVariable("persistent.PreciseDisplayAbilities", true_value=True, false_value=False), Function(renpy.save_persistent)]
                    hovered Show(screen='info', i='显示基础能力数值\n\n勾选此项后，显示面板数值的同时也显示基础数值。\n\n例：\n工作能力 1.1 -> 工作能力 1.1(1.05)',width=600)
                    unhovered Hide('info')
                    background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                    xfill True
                    activate_sound audio.cursor
                if persistent.PreciseDisplayAbilities:
                    imagebutton idle "gui/phone/right_.png":
                        xalign 0.975
                        yalign 0.2

            frame:
                background None
                ysize 50
                textbutton _("显示具体工作目标") text_style 'white':
                    action [ToggleVariable("persistent.PreciseDisplayGoal", true_value=True, false_value=False), Function(renpy.save_persistent)]
                    hovered Show(screen='info', i='显示具体工作目标\n\n勾选此项后，显示工作目标的格式将以具体的数值显示。\n\n例：\n工作进度 10% -> 工作进度 1.0/10.0(10%)',width=600)
                    unhovered Hide('info')
                    background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                    xfill True
                    activate_sound audio.cursor
                if persistent.PreciseDisplayGoal:
                    imagebutton idle "gui/phone/right_.png":
                        xalign 0.975
                        yalign 0.2

            frame:
                background None
                ysize 50
                textbutton _("减少起床等待时间") text_style 'white':
                    action [ToggleVariable("persistent.quickAlarm", true_value=True, false_value=False), Function(renpy.save_persistent)]
                    hovered Show(screen='info', i='减少起床等待时间\n\n勾选此项后，起床便可立刻关闭闹钟。',width=600)
                    unhovered Hide('info')
                    background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                    xfill True
                    activate_sound audio.cursor
                if persistent.quickAlarm:
                    imagebutton idle "gui/phone/right_.png":
                        xalign 0.975
                        yalign 0.2


            frame:
                background None
                ysize 50
                textbutton _("禁用对话音效") text_style 'white':
                    action [ToggleVariable("persistent.disablecharactervoice", true_value=True, false_value=False), Function(renpy.save_persistent)]
                    hovered Show(screen='info', i='禁用对话音效\n\n勾选此项后，显示对话界面的文字时不再播放嘟嘟嘟的音效。',width=600)
                    unhovered Hide('info')
                    background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                    xfill True
                    activate_sound audio.cursor
                if persistent.disablecharactervoice:
                    imagebutton idle "gui/phone/right_.png":
                        xalign 0.975
                        yalign 0.2


            frame:
                background None
                ysize 50
                textbutton _("消息框停留时长") text_style 'white':
                    action [Show(screen='notify_select')]
                    background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                    xfill True
                    activate_sound audio.cursor
                if persistent.notifyDuration == 3:
                    textbutton _("较短") text_style 'white':
                        action NullAction()
                        xalign 0.975
                        yalign 0.2
                if persistent.notifyDuration == 5:
                    textbutton _("正常") text_style 'white':
                        action NullAction()
                        xalign 0.975
                        yalign 0.2
                if persistent.notifyDuration == 10:
                    textbutton _("较久") text_style 'white':
                        action NullAction()
                        xalign 0.975
                        yalign 0.2

            if config.developer:
                textbutton '{size=-5}测试菜单{/size}' text_style "white":
                    action NullAction()
                    xfill True
                    xalign 1.0
                    activate_sound audio.cursor
                    xoffset -5

                frame:
                    background None
                    ysize 50
                    textbutton _("允许回退") text_style 'white':
                        action [ToggleVariable("config.rollback_enabled", true_value=True, false_value=False)]
                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if config.rollback_enabled:
                        imagebutton idle "gui/phone/right_.png":
                            xalign 0.975
                            yalign 0.2
                frame:
                    background None
                    ysize 50
                    textbutton _("允许随时调整日程") text_style 'white':
                        action [ToggleVariable("persistent.unlockplan", true_value=True, false_value=False)]
                        hovered Show(screen='info', i='允许随时调整日程\n\n勾选此项后，你可以在任意时间调整自己的日程。',width=600)
                        unhovered Hide('info')
                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if persistent.unlockplan:
                        imagebutton idle "gui/phone/right_.png":
                            xalign 0.975
                            yalign 0.2

                frame:
                    background None
                    ysize 50
                    textbutton _("跳过日程等待时间和过场动画") text_style 'white':
                        action [ToggleVariable("persistent.nowaiting", true_value=True, false_value=False), Function(renpy.save_persistent)]
                        hovered Show(screen='info', i='跳过日程等待时间和过场动画\n\n勾选此项后，游戏进行日程的等待时间和过场动画的播放时间缩短至0.1秒。',width=600)
                        unhovered Hide('info')
                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if persistent.nowaiting:
                        imagebutton idle "gui/phone/right_.png":
                            xalign 0.975
                            yalign 0.2

                frame:
                    background None
                    ysize 50
                    textbutton _("跳过开场动画") text_style 'white':
                        action [ToggleVariable("persistent.nosplash", true_value=True, false_value=False), Function(renpy.save_persistent)]
                        hovered Show(screen='info', i='跳过开场动画\n\n勾选此项后，打开游戏不再出现开场动画。',width=600)
                        unhovered Hide('info')
                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if persistent.nosplash:
                        imagebutton idle "gui/phone/right_.png":
                            xalign 0.975
                            yalign 0.2

                frame:
                    background None
                    ysize 50
                    textbutton _("关闭人物剧情") text_style 'white':
                        action [ToggleVariable("persistent.nocharacterplot", true_value=True, false_value=False), Function(renpy.save_persistent)]
                        hovered Show(screen='info', i='关闭人物剧情\n\n勾选此项后，进行日程不会触发人物剧情。',width=600)
                        unhovered Hide('info')
                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if persistent.nocharacterplot:
                        imagebutton idle "gui/phone/right_.png":
                            xalign 0.975
                            yalign 0.2

                frame:
                    background None
                    ysize 50
                    textbutton _("关闭死亡判定") text_style 'white':
                        action [ToggleVariable("persistent.nomedicine", true_value=True, false_value=False), Function(renpy.save_persistent)]
                        hovered Show(screen='info', i='关闭死亡判定\n\n勾选此项后，跳过早上的吃药阶段，精神值低于0也不会死亡。',width=600)
                        unhovered Hide('info')
                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if persistent.nomedicine:
                        imagebutton idle "gui/phone/right_.png":
                            xalign 0.975
                            yalign 0.2

                frame:
                    background None
                    ysize 50
                    textbutton _("解锁测试日程") text_style 'white':
                        action [ToggleVariable("persistent.unlocktesttask", true_value=True, false_value=False), Function(renpy.save_persistent)]
                        hovered Show(screen='info', i='解锁测试日程\n\n勾选此项后，解锁测试日程以快速跳过每天。',width=600)
                        unhovered Hide('info')
                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if persistent.unlocktesttask:
                        imagebutton idle "gui/phone/right_.png":
                            xalign 0.975
                            yalign 0.2



screen stat_navi(player=None):

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        textbutton _("状态图鉴") action ShowMenu(screen="screen_guidee", player=player, gd=GuideE.done(), gud=GuideE.undone())

        textbutton _("道具图鉴") action ShowMenu(screen="screen_guidei", player=player, gd=GuideI.done(), gud=GuideI.undone())

        if player:
            textbutton _("本局游戏") action ShowMenu(screen="screen_stat_local", player=player)

        textbutton _("全局数据") action ShowMenu(screen="screen_stat_global", player=player)

        textbutton "" action NullAction()

        textbutton _("清除数据") action Show(screen='info_confirm', i='你确定要清除全局数据的统计数据吗？\n（不会清除图鉴数据）', act=Function(Stat.clear))

        







screen screen_guidee(player, gd, gud):

    tag menu

    use game_menu(_("状态图鉴"), scroll="viewport", navi=False):

        vbox:
            spacing 10
            textbutton '{size=-5}状态图鉴{/size}' text_style "white":
                action NullAction()
                xfill True
                xalign 1.0
                activate_sound audio.cursor
                xoffset -5
            frame:
                background None
                ysize 50
                textbutton _("解锁进度") text_style 'white':
                    action NullAction()
                    background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                    xfill True
                    activate_sound audio.cursor
                textbutton '%s / %s' % (len(gd), len(getSubclasses(Effect))) text_style 'white':
                    action NullAction()
                    xalign 0.975
                    yalign 0.2

            null height 5

            if gd:
                textbutton '{size=-5}已获得过的状态{/size}' text_style "white":
                    action NullAction()
                    xfill True
                    
                    activate_sound audio.cursor
                    xoffset -5
                

            for i in gd:
                frame:
                    background None
                    ysize 50
                    textbutton i.name text_style 'white':
                        action NullAction()
                        hovered Show(screen="info", i=i.info, a=i.ad)
                        unhovered Hide("info")
                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                        xfill True

                    textbutton '{size=-7}%s 解锁{/size}' % (persistent.guide[i]) text_style 'white':
                        action NullAction()
                        xalign 0.975
                        yoffset 3

            null height 20

    use stat_navi(player)


screen screen_guidei(player, gd, gud):
    
    tag menu

    use game_menu(_("道具图鉴"), scroll="viewport", navi=False):

        vbox:
            spacing 10
            textbutton '{size=-5}道具图鉴{/size}' text_style "white":
                action NullAction()
                xfill True
                
                activate_sound audio.cursor
                xoffset -5
            frame:
                background None
                ysize 50
                textbutton _("解锁进度") text_style 'white':
                    action NullAction()
                    background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                    xfill True
                    activate_sound audio.cursor
                textbutton '%s / %s' % (len(gd), len(getSubclasses(Item))) text_style 'white':
                    action NullAction()
                    xalign 0.975
                    yalign 0.2

            null height 5
            
            if gd:
                textbutton '{size=-5}已获得过的道具{/size}' text_style "white":
                    action NullAction()
                    xfill True
                    
                    activate_sound audio.cursor
                    xoffset -5
            

            for i in gd:
                frame:
                    background None
                    ysize 50
                    textbutton i.name text_style 'white':
                        action NullAction()
                        hovered Show(screen="info", i=i.info, a=i.ad)
                        unhovered Hide("info")
                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                        xfill True

                    textbutton '{size=-7}%s 解锁{/size}' % (persistent.guide[i]) text_style 'white':
                        action NullAction()
                        xalign 0.975
                        yoffset 3

    use stat_navi(player)





screen screen_stat_local(player):
    tag menu
    $ pp = player
    if pp != p:
        $ pp = p

    use game_menu(_("本局游戏统计"), scroll="viewport", navi=False):
        use screen_stat(pp.LocalStatistics)
    use stat_navi(pp)

screen screen_stat_global(player):
    tag menu

    use game_menu(_("全局数据统计"), scroll="viewport", navi=False):
        use screen_stat(persistent.GlobalStatistics)
    use stat_navi(player)

screen screen_stat(stat):

    default items = Stat.get(stat)

    if not stat:
        textbutton '{size=-5}暂无可用数据{/size}' text_style "white":
            action NullAction()
            xfill True
            xalign 1.0
            xoffset -5
    else:

        vbox:
            spacing 10
            for i in items:

                textbutton Stat.basenames[Stat.getbase(i[0][0]).__name__][1] text_style "white":
                    action NullAction()
                    xfill True
                    xalign 1.0
                    activate_sound audio.cursor
                    xoffset -5

                $ maxrange = i[0][1]

                for j in i:

                    frame:
                        background None
                        ysize 50
                        textbutton '' text_style 'white':
                            action NullAction()
                            background Frame("gui/style/grey_idle_background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            xfill True
                            activate_sound audio.cursor
                        bar:
                            value j[1]
                            range maxrange
                            xsize 1200
                            yoffset 3
                            xoffset 5
                        textbutton str(j[1]) text_style 'white':
                            action NullAction()
                            xalign 0.975
                            yalign 0.2

                        textbutton j[0].name text_style 'white':
                            action NullAction()
                            background None
                            activate_sound audio.cursor
                            xoffset 5


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
                            xsize 1000


                    else:

                        text h.what:
                            yalign 0.5
                            substitute False
                            size 29
                            xsize 1000



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
    tag menu


    default device = "keyboard"

    use game_menu(_("帮助"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("键盘") action SetScreenVariable("device", "keyboard")
                textbutton _("鼠标") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("手柄") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("回车")
        text _("推进对话并激活界面。")

    hbox:
        label _("空格")
        text _("推进对话但不激活选项。")

    hbox:
        label _("方向键")
        text _("导航界面。")

    hbox:
        label _("Esc")
        text _("访问游戏菜单。")

    hbox:
        label _("Ctrl")
        text _("按住时快进对话。")

    hbox:
        label _("Tab")
        text _("切换对话快进。")

    hbox:
        label _("Page Up")
        text _("回退至先前的对话。")

    hbox:
        label _("Page Down")
        text _("向前至之后的对话。")

    hbox:
        label "H"
        text _("隐藏用户界面。")

    hbox:
        label "S"
        text _("截图。")

    hbox:
        label "V"
        text _("切换辅助{a=https://www.renpy.org/l/voicing}自动朗读{/a}。")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("左键点击")
        text _("推进对话并激活界面。")

    hbox:
        label _("中键点击")
        text _("隐藏用户界面。")

    hbox:
        label _("右键点击")
        text _("访问游戏菜单。")

    hbox:
        label _("鼠标滚轮上\n点击回退操作区")
        text _("回退至先前的对话。")

    hbox:
        label _("鼠标滚轮下")
        text _("向前至之后的对话。")


screen gamepad_help():

    hbox:
        label _("右扳机键\nA/底键")
        text _("推进对话并激活界面。")

    hbox:
        label _("左扳机键\n左肩键")
        text _("回退至先前的对话。")

    hbox:
        label _("右肩键")
        text _("向前至之后的对话。")


    hbox:
        label _("十字键，摇杆")
        text _("导航界面。")

    hbox:
        label _("开始，向导")
        text _("访问游戏菜单。")

    hbox:
        label _("Y/顶键")
        text _("隐藏用户界面。")

    textbutton _("校准") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0














screen confirm(message, yes_action=None, no_action=None):


    modal True

    zorder 1000

    style_prefix "transparent"


    add "gui/overlay/confirm.png"

    frame:
        xalign .5
        yalign .5
        padding (60, 40)

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
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
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

    zorder 100
    style_prefix "skip"

    frame:

        has hbox:
            spacing 9

        text _("正在快进")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



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
        text "[message!tq]"
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
