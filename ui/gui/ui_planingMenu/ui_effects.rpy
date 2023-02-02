screen screen_effects(player):
    #tag gamegui
    use barrier(screen="screen_effects")

    $ effects = sliceArr(player.effects)

    #modal True
    zorder 600
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
                    textbutton _('{size=+10}角色效果{/size}'):
                        text_style "gameUI"
                        xoffset -5
                        yoffset -5
                        action NullAction()

                    imagebutton auto "gui/exit_%s.png":
                        xalign 1.0
                        action [Hide("screen_effects",transition=dissolve),Hide("info")]
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
                            scrollbars "vertical"
                            use effects_show(player, effects)
    
    key 'K_ESCAPE' action [Hide("screen_effects",transition=dissolve),Hide("info")]
                    

screen effects_show(player, effects):
    vbox:
        xsize 640
        default isFold = {
            _('天气'):False,
            _('状态'):False,
            _('增益'):False,
            _('药物反应'):False,
            _('学识'):False,
            _('伤痕'):False
        }
        for i in effects:
            $typename = type(i[0]).kind
            $typei = effectKindInfo(typename, 'i')
            $typea = effectKindInfo(typename, 'a')
            hbox:
                if isFold[typename] == False:
                    textbutton '{size=-5}'+typename+'{/size}' text_style "white":
                        action [SetDict(isFold, typename, True),Hide("info")]
                        hovered Show(screen="info", i=typei+_('\n\n单击以折叠该类日程。'), a=typea)
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
                        hovered Show(screen="info", i=typei+_('\n\n单击以展开该类日程。'), a=typea)
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

                            $ite_pre = ite.getPrefixInfo(player)
                            $ite_main = ite.getPrincipalInfo()
                            $ite_suf = ite.getSuffixInfo()

                            frame:
                                background None
                                textbutton ite.name text_style "white":
                                    action [Hide("info"),Show(screen="info_use", pp=renpy.get_mouse_pos(), t=type(ite).name, i=ite_pre+ite_main + ite_suf, a=ite.ad)]
                                    hovered Show(screen="info", t=type(ite).name, i=ite_pre+ite_main + ite_suf, a=ite.ad)
                                    unhovered Hide("info")
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