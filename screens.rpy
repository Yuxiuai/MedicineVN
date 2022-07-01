################################################################################
## 初始化
################################################################################

init offset = -1


################################################################################
## 样式
################################################################################

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



################################################################################
## 游戏内界面
################################################################################


## 对话界面 ########################################################################
##
## 对话界面用于向玩家显示对话。它需要两个参数，“who”和“what”，分别是叙述人的名称
## 和所叙述的内容。（如果没有名称，参数“who”可以是“None”。）
##
## 此界面必须创建一个 id 为“what”的文本可视控件，因为 Ren'Py 使用它来管理文本显
## 示。它还可以创建 id 为“who”和 id 为“window”的可视控件来应用样式属性。
##
## https://www.renpy.cn/doc/screen_special.html#say

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

## 通过 Character 对象使名称框可用于样式化。
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


## 输入界面 ########################################################################
##
## 此界面用于显示 renpy.input。“prompt”参数用于传递文本提示。
##
## 此界面必须创建一个 id 为“input”的输入可视控件来接受各种输入参数。
##
## https://www.renpy.cn/doc/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
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


## 选择界面 ########################################################################
##
## 此界面用于显示由“menu”语句生成的游戏内选项。参数“items”是一个对象列表，每个对
## 象都有标题和操作字段。
##
## https://www.renpy.cn/doc/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## 若为 True，菜单内的叙述会使用旁白角色。若为 False，叙述会显示为菜单内的文字说
## 明。
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


## 快捷菜单界面 ######################################################################
##
## 快捷菜单显示于游戏内，以便于访问游戏外的菜单。

screen quick_menu():
    pass

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
                #alternate [Skip(fast=True, confirm=True), Hide("info")]
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
                #alternate [Skip(fast=True, confirm=True), Hide("info")]
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


## 此语句确保只要玩家没有明确隐藏界面，就会在游戏中显示“quick_menu”界面。
#init python:
#    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## 标题和游戏菜单界面
################################################################################

## 导航界面 ########################################################################
##
## 该界面包含在标题菜单和游戏菜单中，并提供导航到其他菜单，以及启动游戏。

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing



        if not main_menu:

            textbutton _("历史") action ShowMenu("history")

            #textbutton _("保存") action ShowMenu("save")

            #textbutton _("读取") action ShowMenu("load")

        textbutton _("设置") action ShowMenu("preferences")

        if persistent.ne or config.developer:
            textbutton _("鸣谢") action Start("credits")

        if config.developer == True and main_menu:
            textbutton _("快速开始") action Start("testStart")

        if not main_menu:

            textbutton _("标题界面") action Start("to_the_title")
            if persistent.SaverClass[0]:
                textbutton _("回到今天早上") action Start("load_today")
            if persistent.SaverClass[1]:
                textbutton _("回到昨天早上") action Show(screen="confirm",message="是否回到昨天？当前的进度将会丢失。", yes_action=Start("load_yesterday"), no_action=Hide("confirm"))
            if persistent.SaverClass[2]:
                textbutton _("回到上周五早上") action Show(screen="confirm",message="是否回到上一个周五的早晨？当前的进度将会丢失。", yes_action=Start("load_lastweek"), no_action=Hide("confirm"))

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## 标题菜单界面 ######################################################################
##
## 用于在 Ren'Py 启动时显示标题菜单。
##
## https://www.renpy.cn/doc/screen_special.html#main-menu

screen main_menu():

    ## 此代码可确保替换掉任何其他菜单屏幕。
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background
    use main_menu_navigation()


screen main_menu_navigation():
    add "gui/logo.png" at trans_mainmenu(0.3)
        
    vbox:
        xcenter 0.182
        ycenter 0.752
        spacing gui.navigation_spacing
        if persistent.SaverClass[0]:
            textbutton _ ("{color=#000000}{alpha=*0.7}{size=+4}    继续{/color}{/size}{/alpha}") at trans_mainmenu(0.35)
            textbutton _("{color=#000000}{alpha=*0.7}{size=+4}从头开始{/color}{/size}{/alpha}") at trans_mainmenu(0.5)
        else:
            textbutton _ ("{color=#000000}{alpha=*0.7}{size=+4}    继续{/color}{/size}{/alpha}") at trans_mainmenu(0.35)
            textbutton _("{color=#000000}{alpha=*0.7}{size=+4}从头开始{/color}{/size}{/alpha}") at trans_mainmenu(0.5)

        textbutton _("{color=#000000}{alpha=*0.7}{size=+4}    设置{/color}{/size}{/alpha}") at trans_mainmenu(0.75)
        textbutton _("")
        textbutton _("{color=#000000}{alpha=*0.7}{size=+4}    退出{/color}{/size}{/alpha}") at trans_mainmenu(0.9)
    
    vbox:
        xcenter 0.932
        ycenter 0.977
        textbutton _("{color=#000000}{alpha=*0.7}{size=-4}Version：[config.version]{/color}{/size}{/alpha}")  at trans_mainmenu(1.05):
            xalign 1.0
        textbutton _("{color=#000000}{size=-4}{alpha=*0.7}药：绝望的解决手段{/color}{/size}{/alpha}")  at trans_mainmenu(1.3):
            xalign 1.0
    
    vbox:
        xcenter 0.18
        ycenter 0.75
        spacing gui.navigation_spacing
        if persistent.SaverClass[0]:
            textbutton _ ("{size=+4}    继续{/size}"):
                action Start("load_today")
                at trans_mainmenu(0.35)

            textbutton _("{size=+4}从头开始{/size}"):
                action Show(screen="confirm",message="是否删除上一个存档，重新开始游玩？\n（遗失的存档无法找回）", yes_action=Start(), no_action=Hide("confirm"))
                at trans_mainmenu(0.5)

            
        else:
            
            textbutton _ ("{size=+4}{color=#8888887f}    继续{/size}{/color}"):
                action NullAction()
                at trans_mainmenu(0.45)

            textbutton _("{size=+4}从头开始{/size}"):
                action Start()
                at trans_mainmenu(0.6)
    
        textbutton _("{size=+4}    设置{/size}"):
            action ShowMenu("preferences")
            at trans_mainmenu(0.75)
    
        textbutton _("")
    
        textbutton _("{size=+4}    退出{/size}"):
            action Quit(confirm=not main_menu)
            at trans_mainmenu(0.9)
    vbox:
        xcenter 0.93
        ycenter 0.975
        textbutton _("{color=#FFFFFF}{size=-4}Version：[config.version]") at trans_mainmenu(1.05):
            xalign 1.0
        textbutton _("{color=#FFFFFF}{size=-4}药：绝望的解决手段") at trans_mainmenu(1.3):
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


## 游戏菜单界面 ######################################################################
##
## 此界面列出了游戏菜单的基本共同结构。可使用界面标题调用，并显示背景、标题和导
## 航菜单。
##
## “scroll”参数可以是“None”，也可以是“viewport”或“vpgrid”。当此界面与一个或多个
## 子菜单同时使用时，这些子菜单将被转移（放置）在其中。

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## 导航部分的预留空间。
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

                        vbox:
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


## 关于界面 ########################################################################
##
## 此界面提供有关游戏和 Ren'Py 的制作人员和版权信息。
##
## 此界面没有什么特别之处，因此它也是如何制作自定义界面的一个例子。

screen about():

    tag menu

    ## 此“use”语句将包含“game_menu”界面到此处。子级“vbox”将包含在“game_menu”界面
    ## 的“viewport”内。
    use game_menu(_("关于"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("版本 [config.version!t]\n")

            ## “gui.about”通常在 options.rpy 中设置。
            if gui.about:
                text "[gui.about!t]\n"

            text _("引擎：{a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## 读取和保存界面 #####################################################################
##
## 这些界面负责让玩家保存游戏并能够再次读取。由于它们几乎完全一样，因此它们都是
## 以第三方界面“file_slots”来实现的。
##
## https://www.renpy.cn/doc/screen_special.html#save https://www.renpy.cn/doc/
## screen_special.html#load


screen save():

    tag menu

    use preferences()


screen load():

    tag menu
    
    use preferences()



screen diff_select(player=player):
    use barrier(screen="diff_select")
    style_prefix "info"
    zorder 400
    default pp = renpy.get_mouse_pos()
    $p = pp
    if p[0] < 1500:
        $xc = 0.0
        $trans = trans_toLeft
    else:
        $xc = 1.0
        $trans = trans_toRight
    $xc = 0.0 if p[0] < 1500 else 1.0
    $yc = 0.0 if p[1] < 540 else 1.0
    frame:
        pos pp
        padding (15, 15)
        xanchor xc
        yanchor yc
        xsize 150
        at trans()
        vbox:
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

screen window_select():
    use barrier(screen="window_select")
    style_prefix "info"
    zorder 400
    default pp = renpy.get_mouse_pos()
    $p = pp
    if p[0] < 1500:
        $xc = 0.0
        $trans = trans_toLeft
    else:
        $xc = 1.0
        $trans = trans_toRight
    $xc = 0.0 if p[0] < 1500 else 1.0
    $yc = 0.0 if p[1] < 540 else 1.0
    frame:
        pos pp
        padding (15, 15)
        xanchor xc
        yanchor yc
        xsize 150
        at trans()
        vbox:
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

screen lang_select():
    use barrier(screen="lang_select")
    style_prefix "info"
    zorder 400
    default pp = renpy.get_mouse_pos()
    $p = pp
    if p[0] < 1500:
        $xc = 0.0
        $trans = trans_toLeft
    else:
        $xc = 1.0
        $trans = trans_toRight
    $xc = 0.0 if p[0] < 1500 else 1.0
    $yc = 0.0 if p[1] < 540 else 1.0
    frame:
        pos pp
        padding (15, 15)
        xanchor xc
        yanchor yc
        xsize 150
        at trans()
        vbox:
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
            #frame:
            #    background None
            #    ysize 50
            #    textbutton _("English") text_style 'white':
            #        action [Language('english'),Hide("lang_select")]
            #        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
            #        xfill True
            #        activate_sound audio.cursor
            #    if preferences.language == 'english':
            #        imagebutton idle "gui/phone/right_.png":
            #            xalign 0.975
            #            yalign 0.5

screen notify_select():
    use barrier(screen="notify_select")
    style_prefix "info"
    zorder 400
    default pp = renpy.get_mouse_pos()
    $p = pp
    if p[0] < 1500:
        $xc = 0.0
        $trans = trans_toLeft
    else:
        $xc = 1.0
        $trans = trans_toRight
    $xc = 0.0 if p[0] < 1500 else 1.0
    $yc = 0.0 if p[1] < 540 else 1.0
    frame:
        pos pp
        padding (15, 15)
        xanchor xc
        yanchor yc
        xsize 230
        at trans()
        vbox:
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
    $p = pp
    if p[0] < 1500:
        $xc = 0.0
        $trans = trans_toLeft
    else:
        $xc = 1.0
        $trans = trans_toRight
    $xc = 0.0 if p[0] < 1500 else 1.0
    $yc = 0.0 if p[1] < 540 else 1.0
    frame:
        pos pp
        padding (15, 15)
        xanchor xc
        yanchor yc
        xsize 300
        at trans()
        vbox:
            frame:
                background None
                ysize 50

                $i_gm1 = '偏头痛\n\n小幅度提升药物的回复效果，但每完成一个日程后以百分比随机消耗较大范围内的当前精神状态。\n\n{color=#ff0000}仅在第一周内可添加！\n添加后无法解除！{/color}'

                textbutton _("偏头痛") text_style 'white':
                    if player.week < 2:
                        action [Hide("info"),Show(screen="info_confirm", i=i_gm1,width=600,pp=renpy.get_mouse_pos(),act=Function(GameMode1.add, player))]
                    else:
                        action [Hide("info"),Show(screen="info_use", i=i_gm1,width=600,pp=renpy.get_mouse_pos())]

                    hovered Show(screen='info', i=i_gm1,width=600)
                    unhovered Hide('info')
                    background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                    xfill True
                    activate_sound audio.cursor
                if GameMode1.has(player):
                    imagebutton idle "gui/phone/right_.png":
                        xalign 0.975
                        yalign 0.5
            
            frame:
                background None
                ysize 50

                $i_gm2 = '药价膨胀\n\n药价的自然增长幅度提升至2.5倍。\n\n{color=#ff0000}仅在第一周内可添加！\n添加后无法解除！{/color}'
                
                textbutton _("药价膨胀") text_style 'white':
                    if player.week < 2:
                        action [Hide("info"),Show(screen="info_confirm", i=i_gm2,width=600,pp=renpy.get_mouse_pos(),act=Function(GameMode2.add, player))]
                    else:
                        action [Hide("info"),Show(screen="info_use", i=i_gm2,width=600,pp=renpy.get_mouse_pos())]

                    hovered Show(screen='info', i=i_gm2 ,width=600)
                    unhovered Hide('info')
                    background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                    xfill True
                    activate_sound audio.cursor
                if GameMode2.has(player):
                    imagebutton idle "gui/phone/right_.png":
                        xalign 0.975
                        yalign 0.5
                         
            frame:
                background None
                ysize 50

                $i_gm3 = '自卑感\n\n立刻获得15点全属性，但过夜有较低概率失去2%点随机属性，一定概率永久提升1%严重程度。\n\n{color=#ff0000}仅在第一周内可添加！\n添加后无法解除！{/color}'
                
                textbutton _("自卑感") text_style 'white':
                    if player.week < 3:
                        action [Hide("info"),Show(screen="info_confirm", i=i_gm3,width=600,pp=renpy.get_mouse_pos(),act=Function(GameMode3.add, player))]
                    else:
                        action [Hide("info"),Show(screen="info_use", i=i_gm3,width=600,pp=renpy.get_mouse_pos())]

                    hovered Show(screen='info', i=i_gm3 ,width=600)
                    unhovered Hide('info')
                    background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                    xfill True
                    activate_sound audio.cursor
                if GameMode3.has(player):
                    imagebutton idle "gui/phone/right_.png":
                        xalign 0.975
                        yalign 0.5

            frame:
                background None
                ysize 50

                $i_gm4 = '理财不善\n\n过夜有概率失去小部分金钱。\n\n{color=#ff0000}仅在第一周内可添加！\n添加后无法解除！{/color}'
                
                textbutton _("理财不善") text_style 'white':
                    if player.week < 3:
                        action [Hide("info"),Show(screen="info_confirm", i=i_gm4,width=600,pp=renpy.get_mouse_pos(),act=Function(GameMode4.add, player))]
                    else:
                        action [Hide("info"),Show(screen="info_use", i=i_gm4,width=600,pp=renpy.get_mouse_pos())]

                    hovered Show(screen='info', i=i_gm4 ,width=600)
                    unhovered Hide('info')
                    background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                    xfill True
                    activate_sound audio.cursor
                if GameMode4.has(player):
                    imagebutton idle "gui/phone/right_.png":
                        xalign 0.975
                        yalign 0.5

            frame:
                background None
                ysize 50

                $i_gm5 = '效率低下\n\n每周需要完成的工作提升15%。\n\n{color=#ff0000}仅在第一周内可添加！\n添加后无法解除！{/color}'
                
                textbutton _("效率低下") text_style 'white':
                    if player.week < 3:
                        action [Hide("info"),Show(screen="info_confirm", i=i_gm5,width=600,pp=renpy.get_mouse_pos(),act=Function(GameMode5.add, player))]
                    else:
                        action [Hide("info"),Show(screen="info_use", i=i_gm5,width=600,pp=renpy.get_mouse_pos())]

                    hovered Show(screen='info', i=i_gm5 ,width=600)
                    unhovered Hide('info')
                    background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                    xfill True
                    activate_sound audio.cursor
                if GameMode5.has(player):
                    imagebutton idle "gui/phone/right_.png":
                        xalign 0.975
                        yalign 0.5
            
            frame:
                background None
                ysize 10

            frame:
                background None
                ysize 50
                textbutton _("确定") text_style 'white':
                    action Hide("challenges_select")
                    text_xalign 0.5
                    background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                    xfill True
                    activate_sound audio.cursor

    key 'K_ESCAPE' action Hide("info_confirm")

## 设置界面 ########################################################################
##
## 设置界面允许玩家配置游戏以更好地适应自己的习惯。
##
## https://www.renpy.cn/doc/screen_special.html#preferences

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
                    $challenges = 0
                    background None
                    ysize 50
                    textbutton _("模组管理") text_style 'white':
                        action [Show(screen='challenges_select',player=player)]
                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if GameMode1.has(player):
                        $challenges+=1
                    if GameMode2.has(player):
                        $challenges+=1
                    if GameMode3.has(player):
                        $challenges+=1
                    if GameMode4.has(player):
                        $challenges+=1
                    if GameMode5.has(player):
                        $challenges+=1
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
                    action NullAction()
                    background Frame("gui/style/grey_idle_background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                    xfill True

                bar value Preference("music volume"):
                    xsize 1000
                    xalign 0.975
                    yoffset 4

                textbutton str(int(100*preferences.get_volume('music'))) + '%' text_style 'white':
                    action NullAction()
                    xalign 0.18
                    yalign 0.2

            frame:
                background None
                ysize 50
                textbutton _("音效音量") text_style 'white':
                    action NullAction()
                    background Frame("gui/style/grey_idle_background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                    xfill True


                bar value Preference("sound volume"):
                    xsize 1000
                    xalign 0.975
                    yoffset 4

                textbutton str(int(100*preferences.get_volume('sfx'))) + '%' text_style 'white':
                    action NullAction()
                    xalign 0.18
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

            textbutton '{size=-5}游戏设置{/size}' text_style "white":
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
                textbutton _("关闭起床等待时间") text_style 'white':
                    action [ToggleVariable("persistent.quickAlarm", true_value=True, false_value=False), Function(renpy.save_persistent)]
                    hovered Show(screen='info', i='关闭起床等待时间\n\n勾选此项后，使主角更快起床而不用听较久的闹钟。',width=600)
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
                    textbutton _("跳过日程等待时间和过场动画（测试）") text_style 'white':
                        action [ToggleVariable("persistent.nowaiting", true_value=True, false_value=False), Function(renpy.save_persistent)]
                        hovered Show(screen='info', i='跳过日程等待时间和过场动画（测试）\n\n勾选此项后，游戏进行日程的等待时间和过场动画的播放时间缩短至0.1秒。',width=600)
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
                    textbutton _("跳过开场动画（测试）") text_style 'white':
                        action [ToggleVariable("persistent.nosplash", true_value=True, false_value=False), Function(renpy.save_persistent)]
                        hovered Show(screen='info', i='跳过开场动画（测试）\n\n勾选此项后，打开游戏不再出现开场动画。',width=600)
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
                    textbutton _("关闭人物剧情（测试）") text_style 'white':
                        action [ToggleVariable("persistent.noplot", true_value=True, false_value=False), Function(renpy.save_persistent)]
                        hovered Show(screen='info', i='关闭人物剧情（测试）\n\n勾选此项后，进行日程不会触发人物剧情。',width=600)
                        unhovered Hide('info')
                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if persistent.noplot:
                        imagebutton idle "gui/phone/right_.png":
                            xalign 0.975
                            yalign 0.2

                frame:
                    background None
                    ysize 50
                    textbutton _("关闭死亡判定（测试）") text_style 'white':
                        action [ToggleVariable("persistent.nomedicine", true_value=True, false_value=False), Function(renpy.save_persistent)]
                        hovered Show(screen='info', i='关闭死亡判定（测试）\n\n勾选此项后，跳过早上的吃药阶段，精神值低于0也不会死亡。',width=600)
                        unhovered Hide('info')
                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor
                    if persistent.nomedicine:
                        imagebutton idle "gui/phone/right_.png":
                            xalign 0.975
                            yalign 0.2
    
    #use navigation




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


## 历史界面 ########################################################################
##
## 这是一个向玩家显示对话历史的界面。虽然此界面没有任何特殊之处，但它必须访问储
## 存在“_history_list”中的对话历史记录。
##
## https://www.renpy.cn/doc/history.html

screen history():

    tag menu

    ## 避免预缓存此屏幕，因为它可能非常大。
    predict False

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


                            ## 若角色颜色已设置，则从“Character”对象中读取颜色到叙述
                            ## 人文本中。
                            if "color" in h.who_args:
                                text_color h.who_args["color"]
                        #$ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                        text h.what:
                            xpos 0.04
                            yalign 0.5
                            substitute False
                            size 29
                            xsize 1000
                            #if "color" in h.what_args:
                            #    color h.what_args["color"]
                    else:
                        #$ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                        text h.what:
                            yalign 0.5
                            substitute False
                            size 29
                            xsize 1000
                            #if "color" in h.what_args:
                            #    color h.what_args["color"]

        if not _history_list:
            label _("对话历史记录为空。")

## 此代码决定了允许在历史记录屏幕上显示哪些标签。
## 此语句决定了允许在历史记录界面上显示哪些标签。

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


## 帮助界面 ########################################################################
##
## 提供有关键盘和鼠标映射信息的界面。它使用其它界面
## （“keyboard_help”，“mouse_help“和”gamepad_help“）来显示实际的帮助内容。

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



################################################################################
## 其他界面
################################################################################


## 确认界面 ########################################################################
##
## 当 Ren'Py 需要询问玩家有关确定或取消的问题时，会调用确认界面。
##
## https://www.renpy.cn/doc/screen_special.html#confirm

screen confirm(message, yes_action=None, no_action=None):

    ## 显示此界面时，确保其他界面无法输入。
    modal True

    zorder 1000

    style_prefix "transparent"
    

    add "gui/overlay/confirm.png"

    frame:
        xalign .5
        yalign .5
        padding (60, 40)

        vbox:
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

    ## 右键点击退出并答复“no”（取消）。
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


## 快进指示界面 ######################################################################
##
## “skip_indicator”界面用于指示快进正在进行中。
##
## https://www.renpy.cn/doc/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("正在快进")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## 此变换用于一个接一个地闪烁箭头。
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
    ## 我们必须使用包含“BLACK RIGHT-POINTING SMALL TRIANGLE”字形的字体。
    font "DejaVuSans.ttf"


## 通知界面 ########################################################################
##
## 通知界面用于向玩家显示消息。（例如，当游戏快速保存或已截屏时。）
##
## https://www.renpy.cn/doc/screen_special.html#notify-screen

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
    #pause(2)
    #linear 0.1 xoffset 50
    #linear 0.15 xoffset 100
    #linear 0.05 xoffset -25
    #linear 0.05 xoffset 0
    

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


## NVL 模式界面 ####################################################################
##
## 此界面用于 NVL 模式的对话和菜单。
##
## https://www.renpy.cn/doc/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## 在“vpgrid”或“vbox”中显示对话框。
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## 如果给定，则显示“menu”。 如果“config.narrator_menu”设置为“True”，
        ## 则“menu”可能显示不正确，如前述。
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## 此语句控制一次可以显示的 NVL 模式条目的最大数量。
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



################################################################################
## 移动设备界面
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## 由于鼠标可能不存在，我们将快捷菜单替换为更容易触摸且按钮更少更大的版本。
screen quick_menu():
    variant "touch"

    pass


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
