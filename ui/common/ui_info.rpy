screen info(t=None, i=None, a=None, width=400, pp=renpy.get_mouse_pos()):

    style_prefix "info"
    zorder 1000
    python:
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


screen info3(t=None, i1=None, a1=None, i2=None, a2=None, width=400, pp=renpy.get_mouse_pos()):

    style_prefix "info"
    zorder 1000
    python:
        (xc,trans) = (0.0,trans_toLeft) if pp[0] < 1500 else (1.0,trans_toRight)
        yc = 0.0 if pp[1] < 540 else 1.0
        if i1:
            if width == 400 and len(i1) > 400:
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
            if i1 is not None:
                label '{size=-2}[i1!t]{/size}':
                    text_style "info_text"
                    xsize width
                
            if a1 is not None:
                null height 16
                label '{i}[a1!t]{/i}':
                    text_style "admonition_text"
                    xsize width
            if i2 is not None:
                label '{size=-2}[i2!t]{/size}':
                    text_style "info_text"
                    xsize width
                
            if a2 is not None:
                null height 16
                label '{i}[a2!t]{/i}':
                    text_style "admonition_text"
                    xsize width


screen info_use(t=None,i=None, a=None, width=400, pp=renpy.get_mouse_pos()):
    use barrier(screen="info_use")
    style_prefix "info"
    zorder 1000
    python:
        (xc,trans) = (0.0,trans_toLeft) if pp[0] < 1500 else (1.0,trans_toRight)
        yc = 0.0 if pp[1] < 540 else 1.0
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
                textbutton _("{size=-3}确定{/size}"):
                    action Hide("info_use",transition=dissolve)
                    activate_sound audio.cursor

    key 'K_ESCAPE' action Hide("info_use",transition=dissolve)


screen info_confirm(act, t=None, i=None, a=None, width=400, pp=renpy.get_mouse_pos(),text=_('确定'),r=False):
    use barrier(screen="info_confirm")
    style_prefix "info"
    zorder 1000
    python:
        (xc,trans) = (0.0,trans_toLeft) if pp[0] < 1500 else (1.0,trans_toRight)
        yc = 0.0 if pp[1] < 540 else 1.0
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
            if i is not None:
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
                spacing width/4
                textbutton _("{size=-3}[text!t]{/size}"):
                    if r:
                        action [act,Hide("info_confirm",transition=dissolve),Return()]
                    else:
                        action [act,Hide("info_confirm",transition=dissolve)]
                    activate_sound audio.cursor
                textbutton _("{size=-3}返回{/size}"):
                    action Hide("info_confirm",transition=dissolve)
                    activate_sound audio.cursor

    key 'K_ESCAPE' action Hide("info_confirm",transition=dissolve)



screen info3_use(t=None, i1=None, a1=None, i2=None, a2=None, width=400, pp=renpy.get_mouse_pos()):
    use barrier(screen="info3_use")
    style_prefix "info"
    zorder 1000
    python:
        (xc,trans) = (0.0,trans_toLeft) if pp[0] < 1500 else (1.0,trans_toRight)
        yc = 0.0 if pp[1] < 540 else 1.0
        if i1:
            if width == 400 and len(i1) > 400:
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
            if i1 is not None:
                label '{size=-2}[i1!t]{/size}':
                    text_style "info_text"
                    xsize width
                
            if a1 is not None:
                null height 16
                label '{i}[a1!t]{/i}':
                    text_style "admonition_text"
                    xsize width
            
            if i2 is not None:
                
                label '{size=-2}[i2!t]{/size}':
                    text_style "info_text"
                    xsize width
                
            if a2 is not None:
                null height 16
                label '{i}[a2!t]{/i}':
                    text_style "admonition_text"
                    xsize width
            null height 30
            hbox:
                xalign 0.5
                textbutton _("{size=-3}确定{/size}"):
                    action Hide("info3_use",transition=dissolve)
                    activate_sound audio.cursor

    key 'K_ESCAPE' action Hide("info3_use",transition=dissolve)




############################################################



screen info_e(eff, width=400, pp=renpy.get_mouse_pos()):

    style_prefix "info"
    zorder 1000
    python:
        t = eff.name
        i = eff.getPrefixInfo(p)+eff.getPrincipalInfo()+eff.getSuffixInfo()
        a = eff.ad

        (xc,trans) = (0.0,trans_toLeft) if pp[0] < 1500 else (1.0,trans_toRight)
        yc = 0.0 if pp[1] < 540 else 1.0
        if width == 400:
            if a:
                if len(i) + len(a) > 300:
                    width = 800
                elif len(i) + len(a) > 200:
                    width = 600
            else:
                if len(i) > 200:
                    width = 800
                elif len(i) > 150:
                    width = 600
        

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
            if i is not None:
                label '{size=-2}[i!t]{/size}':
                    text_style "info_text"
                    xsize width
            if a is not None:
                null height 16
                label '{i}[a!t]{/i}':
                    text_style "admonition_text"
                    xsize width
