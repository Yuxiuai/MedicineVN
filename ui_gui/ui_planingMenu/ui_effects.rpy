screen screen_effects(player):
    #tag gamegui
    use barrier(screen="screen_effects")

    $ effects = sliceArr(player.effects)

    #modal True
    zorder 200
    drag:
        xcenter 0.5
        ycenter 0.48
        frame:
            at trans_toRight()
            style "translucent_frame"
            xsize 700
            ysize 800
            vbox:
                frame:
                    background None
                    yalign 0.001
                    textbutton '{size=+10}角色效果{/size}':
                        text_style "gameUI"
                        xoffset -5
                        yoffset -5
                        action NullAction()

                    imagebutton auto "gui/icons/task_icon/exit_%s.png":
                        xalign 1.0
                        action [Hide("screen_effects",transition=dissolve),Hide("info"),Hide("info3")]
                        #alternate Function(allI, player=player)

                    frame:
                        background None
                        ysize 700
                        xsize 650
                        ypos 60
                        xpos 25

                        viewport:
                            mousewheel True
                            draggable True
                            if len(player.effects)>9:
                                scrollbars "vertical"
                            use effects_show(player, effects)
    
    key 'K_ESCAPE' action [Hide("screen_effects",transition=dissolve),Hide("info"),Hide("info3")]
    key 'q' action [Hide("screen_effects",transition=dissolve),Hide("info"),Hide("info3")]
    key 'w' action [Hide("screen_effects",transition=dissolve),Hide("info"),Hide("info3")]
    key 'e' action [Hide("screen_effects",transition=dissolve),Hide("info"),Hide("info3")]
    key 'r' action [Hide("screen_effects",transition=dissolve),Hide("info"),Hide("info3")]
                    

screen effects_show(player, effects):
    vbox:
        xsize 640
        default isFold = {
            '天气':False,
            '状态':False,
            '增益':False,
            '药物反应':False,
            '学识':False,
            '伤痕':False
        }
        for i in effects:
            $typename = type(i[0]).kind
            $typei = effectKindInfo(typename, 'i')
            $typea = effectKindInfo(typename, 'a')
            hbox:
                if isFold[typename] == False:
                    textbutton '{size=-5}'+typename+'{/size}' text_style "white":
                        action [SetDict(isFold, typename, True),Hide("info")]
                        hovered Show(screen="info", i=typei+'\n\n单击以折叠该类日程。', a=typea)
                        unhovered Hide("info")
                        xfill True
                        xalign 1.0
                        activate_sound audio.cursor
                        #background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)

                    imagebutton idle "gui/style/folded.png":
                        xoffset -85
                        yoffset 10

                else:

                    textbutton '{size=-5}'+typename+'{/size}' text_style "white":
                        action [SetDict(isFold, typename, False),Hide("info")]
                        hovered Show(screen="info", i=typei+'\n\n单击以展开该类日程。', a=typea)
                        unhovered Hide("info")
                        xfill True
                        xalign 1.0
                        activate_sound audio.cursor
                        #background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)

                    imagebutton idle "gui/style/folded.png":
                        xoffset -85
                        yoffset 10
                        at reverse
            if isFold[typename] == False:
                vbox:
                    #xalign 1.0
                    for ite in i:
                        frame:
                            background None
                            ysize 60
                            xfill True

                            $ite_pre = ite.getPrefixInfo()
                            $ite_main = ite.getPrincipalInfo()
                            $ite_suf = ite.getSuffixInfo()

                            frame:
                                background None
                                textbutton type(ite).name text_style "white":
                                    action [Hide("info3"),Show(screen="effect_use", player=player, item=ite, pp=renpy.get_mouse_pos(), t=type(ite).name, i1=ite_pre, i2=ite_main + ite_suf, a2=type(ite).ad)]
                                    hovered Show(screen="info3", t=type(ite).name, i1=ite_pre, i2=ite_main + ite_suf, a2=type(ite).ad)
                                    unhovered Hide("info3")
                                    background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                    activate_sound audio.cursor
                                    xfill True
                                $stacks = str(ite.stacks) if ite.stacks>1 else ''
                                textbutton stacks text_style "white":
                                    xpos 1.0
                                    xoffset -45
                                    xanchor 1.0

                        null height 2
        null height 30
        textbutton ''


screen effect_use(player, item, pp, t=None, i1=None, a1=None, i2=None, a2=None, width=400):
    style_prefix "info"
    use barrier(screen="effect_use")
    zorder 3000
    $p = pp
    $yc = 0.0 if p[1] < 540 else 1.0
    if p[0] < 1500:
        $xc = 0.0
        $trans = trans_toLeft
    else:
        $xc = 1.0
        $trans = trans_toRight
    frame:
        pos p
        padding (15, 15)
        xanchor xc
        yanchor yc
        at trans()
        vbox:
            align p
            if t is not None:
                label t+'\n':
                    text_style "info_text"
                    xsize width
            if i1 is not None:
                null height -8
                label '{size=-2}'+i1+'{/size}':
                    text_style "info_text"
                    xsize width
            if a1 is not None:
                $a1 = '{i}' + a1 + '{/i}'
                null height 13
                label a1:
                    text_style "admonition_text"
                    xsize width
            if i2 is not None:
                null height -6
                label '{size=-2}'+i2+'{/size}':
                    text_style "info_text"
                    xsize width
            if a2 is not None:
                $a2 = '{i}' + a2 + '{/i}'
                null height 13
                label a2:
                    text_style "admonition_text"
                    xsize width
            null height 30
            hbox:
                xalign 0.5
                textbutton _("{size=-3}确定{/size}"):
                    action Hide("effect_use")
                    activate_sound audio.cursor
