screen screen_buyMed(player):
    #tag gamegui
    use barrier(screen="screen_buyMed", mode=0)

    $ med = [MedicineA]
    $ otherMed = list(filter(lambda x: x.kind == '普通药物', getSubclasses(Item)))
    $ otherMed.sort(key=lambda x:x.id)
    if player.sol_p>=1:
        $med.append(MedicineB)
    if player.sol_p>=3:
        $med.append(MedicineC)
    #if player.sol_p>=10:
    #    items.append(MedicineD)
    $ items = [med, otherMed]

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
                    textbutton '{size=+10}购买药物{/size}':
                        text_style "gameUI"
                        xoffset -5
                        yoffset -5
                        action NullAction()

                    imagebutton auto "gui/icons/task_icon/exit_%s.png":
                        xalign 1.0
                        action [Hide("screen_buyMed"), Return()]

                    frame:
                        background None
                        ysize 700
                        xsize 650
                        ypos 60
                        xpos 25
                        viewport:
                            mousewheel True
                            draggable True
                            if len(med) + len(otherMed)>8:
                                scrollbars "vertical"

                            use screen_buyMed_show(player, items)
                    

screen screen_buyMed_show(player, items):
    vbox:
        if player.today==5:
            vbox:
                xsize 640
                $typename = '实验药物'
                $typei = itemKindInfo('实验药物', 'i')
                $typea = itemKindInfo('实验药物', 'a')
                hbox:
                    textbutton '{size=-5}'+typename+'{/size}' text_style "white":
                        action NullAction()
                        hovered Show(screen="info", i=typei, a=typea)
                        unhovered Hide("info")
                        xfill True
                        xoffset -10
                        activate_sound audio.cursor
                        #background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)

                vbox:
                    #xalign 1.0
                    for ite in items[0]:
                        frame:
                            background None
                            ysize 60
                            xfill True

                            frame:
                                background None
                                textbutton ite.name text_style "white":
                                    action [Hide("info3"),Show(screen="screen_buyMed_use", player=player,money=player.price, book=ite, pp=renpy.get_mouse_pos(), t=ite.name, i1=ite.getPrincipalInfo(), a1=ite.ad)]
                                    hovered [Show(screen="info3", t=ite.name, i1=ite.getPrincipalInfo(), a1=ite.ad)]
                                    unhovered Hide("info3")
                                    background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                    activate_sound audio.cursor
                                    xfill True

                                textbutton str(player.price) text_style "white":
                                    xpos 1.0
                                    xoffset -30
                                    xanchor 1.0

                            null height 2
        
        if player.week > 0:
            if player.today==5:
                null height 10
            vbox:
                xsize 640
                $typename = '普通药物'
                $typei = itemKindInfo('普通药物', 'i')
                $typea = itemKindInfo('普通药物', 'a')
                hbox:
                    textbutton '{size=-5}'+typename+'{/size}' text_style "white":
                        action NullAction()
                        hovered Show(screen="info", i=typei, a=typea)
                        unhovered Hide("info")
                        xfill True
                        xalign 1.0
                        activate_sound audio.cursor
                        #background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)

                vbox:
                    #xalign 1.0
                    for ite in items[1]:
                        frame:
                            background None
                            ysize 60
                            xfill True
                            $money = r2(player.price * rh(ite.id, player, 850, 1150) * 0.001 * ite.p)
                            frame:
                                background None
                                textbutton ite.name text_style "white":
                                    action [Hide("info3"),Show(screen="screen_buyMed_use", player=player, money=money,book=ite, pp=renpy.get_mouse_pos(), t=ite.name, i1=ite.getPrincipalInfo(), a1=ite.ad)]
                                    hovered [Show(screen="info3", t=ite.name, i1=ite.getPrincipalInfo(), a1=ite.ad)]
                                    unhovered Hide("info3")
                                    background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                    activate_sound audio.cursor
                                    xfill True

                                textbutton str(money) text_style "white":
                                    xpos 1.0
                                    xoffset -40
                                    xanchor 1.0

                            null height 2
                    
        null height 30
        textbutton ''

screen screen_buyMed_use(player, book,money, pp, t=None, i1=None, a1=None, i2=None, a2=None, width=400):
    style_prefix "info"
    default num = '1'
    use barrier(screen="screen_buyMed_use")
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
                hbox:
                    textbutton _("{size=-3}数量：{/size}"):
                        action NullAction()
                        activate_sound audio.cursor
                    frame:
                        background None
                        xsize 70
                        yalign 0.5
                        input:
                            value ScreenVariableInputValue("num")
                            style "white"
                            length 4
                            allow '0123456789'
                null width 10
                textbutton _("{size=-3}购买{/size}"):
                    action [Hide("screen_buyMed_use"), Function(buy, player=player, item=book, nums=int(num) if num!=''else 0, money=money)]
                    activate_sound audio.cursor
                null width 40
                textbutton _("{size=-3}取消{/size}"):
                    action Hide("screen_buyMed_use")
                    activate_sound audio.cursor