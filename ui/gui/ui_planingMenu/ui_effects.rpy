screen screen_effects(player):
    use barrier(screen="screen_effects", mode=0)
    #tag gamegui
    #modal True
    zorder 550
    drag:
        xcenter 0.5
        ycenter 0.48
        frame:
            at trans_toRight()
            style "translucent_frame"
            xsize 1000
            ysize 800
            vbox:
                frame:
                    background None
                    yalign 0.001
                    textbutton '{size=+10}状态{/size}':
                        text_style "white"
                        xoffset -5
                        yoffset -5
                        action NullAction()

                    imagebutton auto "gui/exit_%s.png":
                        xalign 1.0
                        action [Hide("screen_effects",transition=dissolve),Hide("info")]
                    
                    frame:
                        background None
                        ysize 680
                        xsize 980
                        xpos 10
                        ypos 80

                        use screen_effects_inner(player)
    key 'K_ESCAPE' action [Hide("screen_effects",transition=dissolve),Hide("info")]



screen screen_effects_inner(player):
    $ effects = sliceArr(player.effects)
    if player.effects:
        frame:
            background None
            ysize 670
            xfill True
            viewport:
                mousewheel True
                draggable True
                scrollbars "vertical"
                vbox:
                    for i in effects:
                        use screen_effects_inner_inner(player, i)

        
screen screen_effects_inner_inner(player, effect):
    $typename = effect[0].kind
    $typei = effectKindInfo(typename, 'i')
    $typea = effectKindInfo(typename, 'a')
    textbutton typename text_style 'white':
        action NullAction()
        hovered Show(screen="info", i=typei, a=typea)
        unhovered Hide("info")
        background Frame("gui/style/grey_hover_background.png", tile=gui.frame_tile)
        xfill True
        ysize 40
        
    frame:
        background None

        hbox:
            box_wrap True
            for item in effect:
                use screen_effects_inner_inner_effect(player, item)
                null height 2

screen screen_effects_inner_inner_effect(player, effect):

    python:
        def geticon(effect):
            stack_layer = '' if effect.stacks == 1 else str(effect.stacks)
            return Composite((75, 75), (0, 0), effect.icon(), (0, 0), Fixed(Text(stack_layer, size=30,xcenter=0.9, ycenter=0.2)))


    $effect_pre = effect.getPrefixInfo(player)
    $effect_main = effect.getPrincipalInfo()
    $effect_suf = effect.getSuffixInfo()
    $showname = effect.name
    if len(showname) >= 9:
        $showname='{size=-5}'+showname+'{/size}'

    frame:
        background None
        xsize 295
        ysize 90
        textbutton showname text_style "white":
            action [Hide("info"),Show(screen="info_use", pp=renpy.get_mouse_pos(), t=effect.name, i=effect_pre+effect_main + effect_suf, a=effect.ad)]
            hovered Show(screen="info", t=effect.name, i=effect_pre+effect_main + effect_suf, a=effect.ad)
            unhovered Hide("info")
            background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
            activate_sound audio.cursor
            xfill True
            yfill True
            text_xpos 0.3
        imagebutton idle geticon(effect):
            #xalign 0.5
            yalign 0.5
            xoffset 4
