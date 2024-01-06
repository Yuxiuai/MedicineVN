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


    
    $showname = effect.name
    if len(showname) >= 9:
        $showname='{size=-5}'+showname+'{/size}'

    frame:
        background None
        xsize 295
        ysize 90
        textbutton showname text_style "white":
            action [Hide("info"),Show(screen="screen_effects_use", pp=renpy.get_mouse_pos(), effect=effect, player=player)]
            hovered Show(screen="info", t=effect.name, i=effect.getPrefixInfo(player)+effect.getPrincipalInfo() + effect.getSuffixInfo(), a=effect.ad)
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



screen screen_effects_use(player, effect, width=400, pp=renpy.get_mouse_pos()):
    use barrier(screen="screen_effects_use")
    style_prefix "info"
    zorder 1000
    python:
        (xc,trans) = (0.0,trans_toLeft) if pp[0] < 1500 else (1.0,trans_toRight)
        yc = 0.0 if pp[1] < 540 else 1.0

        t=effect.name
        i=effect.getPrefixInfo(player)+effect.getPrincipalInfo() + effect.getSuffixInfo()
        a=effect.ad

        if i:
            if width == 400 and len(i) > 400:
                width = 800
    frame:
        pos pp
        padding (15, 15)
        xanchor xc
        yanchor yc
        at trans()

        vbox:
            align pp
            if t is not None:
                label '[t!t]\n':
                    text_style "info_text"
                    xsize width
            label '{size=-2}[i!t]{/size}':
                text_style "info_text"
                xsize width
            if a is not None:
                null height 16
                label '{i}[a!t]{/i}':
                    text_style "admonition_text"
                    xsize width
            null height 30
            hbox:
                xalign 0.5
                spacing 50
                if persistent.sponsor or config.developer:
                    textbutton _("{size=-3}{color=#ff0000}移除{/color}{/size}"):
                        action Function(effect.sub, player), Hide("screen_effects_use",transition=dissolve)
                        activate_sound audio.cursor
                textbutton _("{size=-3}确定{/size}"):
                    action Hide("screen_effects_use",transition=dissolve)
                    activate_sound audio.cursor

    key 'K_ESCAPE' action Hide("screen_effects_use",transition=dissolve),Hide("info")