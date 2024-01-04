
screen screen_tr_readingbook(player, nums=2):
    #tag gamegui

    python:
        def bookexecute(books, book, nums):
            if book in books:
                books.remove(book)
            elif len(books) < nums:
                books.append(book)
            else:
                showNotice(["最多添加%s本书！"%nums])
        
        def allocate(books, nums):
            
            result = [x.progress for x in books]
            l = len(result)
            for i in range(l):
                if result[i]>=2:
                    continue
                elif nums >= 1:
                    result[i]+=1
                    nums -= 1
                else:
                    break
            for i in range(l):
                if result[i]>=2:
                    continue
                elif nums >= 1:
                    result[i]+=1
                    nums -= 1
                else:
                    break

            return result

        items1 = list(filter(lambda x: x.kind == '书籍' and type(x) not in p.itemcd, p.items))
        items2 = list(filter(lambda x: x.kind == '专业类书籍' and type(x) not in p.itemcd, p.items))
        if BookstoreBuff.has(player):
            nums *= 2

    default books = []

    #modal True
    zorder 200

    drag:
        xcenter 0.5
        ycenter 0.48
        frame:
            at trans_toRight()
            style "translucent_frame"
            xsize 1020
            ysize 800
            vbox:
                frame:
                    background None
                    yalign 0.001
                    text _('{size=+10}选择书籍进行阅读{/size}'):
                        style "white"
                        align(.0, .0)

                    imagebutton auto "gui/exit_%s.png":
                        xalign 1.0
                        action Show(screen="screen_tr_readingbook_confirm",player=player)

                    frame:
                        background None
                        ysize 700
                        xsize 475
                        ypos 60
                        xpos 25

                        viewport:
                            mousewheel True
                            draggable True
                            if len(items1) + len(items2) > 8:
                                scrollbars "vertical"
                            vbox:
                                xsize 450

                                hbox:
                                    textbutton '{size=-5}可阅读的书籍{/size}' text_style "white":
                                        action NullAction()
                                        hovered Show(screen="info", i=itemKindInfo('书籍', 'i'), a=itemKindInfo('书籍', 'a'))
                                        unhovered Hide("info")
                                        xfill True
                                        xalign 1.0
                                        #background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)

                                vbox:
                                    #xalign 1.0
                                    for ite in items1:
                                        if ite not in books:
                                            frame:
                                                background None
                                                ysize 60
                                                xfill True
                                                $ite_name = ite.name
                                                $ite_pre = ite.getPrefixInfo(player)
                                                $ite_main = ite.getPrincipalInfo()
                                                $ite_suf = ite.getSuffixInfo()

                                                frame:
                                                    background None
                                                    textbutton ite_name text_style "white":
                                                        if persistent.actionquickly:
                                                            action Hide("info"),Function(bookexecute, books, ite, nums)
                                                        else:
                                                            action [Hide("info"),Show(screen="info_confirm", text=_('选择'),act=[Function(bookexecute, books, ite, nums)], pp=renpy.get_mouse_pos(), t=ite_name, i=ite_pre+'\n'+ite_main+ite_suf, a=ite.ad)]
                                                        hovered [Show(screen="info", t=ite_name, i=ite_pre+'\n'+ite_main+ite_suf, a=ite.ad)]
                                                        unhovered Hide("info")
                                                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                                                        if len(books)==2:
                                                            activate_sound audio.error
                                                        else:
                                                            activate_sound audio.cursor
                                                        xfill True
                                                    text str(ite.progress*50) + '%' style "white":
                                                        xalign 0.98
                                                        yoffset 6
                                                        size 20

                                                null height 2
                                
                                hbox:
                                    textbutton '{size=-5}可阅读的专业类书籍{/size}' text_style "white":
                                        action NullAction()
                                        hovered Show(screen="info", i=itemKindInfo('专业类书籍', 'i'), a=itemKindInfo('专业类书籍', 'a'))
                                        unhovered Hide("info")
                                        xfill True
                                        xalign 1.0
                                        #background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)

                                vbox:
                                    #xalign 1.0
                                    for ite in items2:
                                        if ite not in books:
                                            frame:
                                                background None
                                                ysize 60
                                                xfill True
                                                $ite_name = ite.name
                                                $ite_pre = ite.getPrefixInfo(player)
                                                $ite_main = ite.getPrincipalInfo()
                                                $ite_suf = ite.getSuffixInfo()

                                                frame:
                                                    background None
                                                    textbutton ite_name text_style "white":
                                                        if persistent.actionquickly:
                                                            action Hide("info"),Function(bookexecute, books, ite, nums)
                                                        else:
                                                            action [Hide("info"),Show(screen="info_confirm", text=_('选择'),act=[Function(bookexecute, books, ite, nums)], pp=renpy.get_mouse_pos(), t=ite_name, i=ite_pre+'\n'+ite_main+ite_suf, a=ite.ad)]
                                                        hovered [Show(screen="info", t=ite_name, i=ite_pre+'\n'+ite_main+ite_suf, a=ite.ad)]
                                                        unhovered Hide("info")
                                                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                                                        if len(books)==2:
                                                            activate_sound audio.error
                                                        else:
                                                            activate_sound audio.cursor
                                                        xfill True
                                                    text str(ite.progress*50) + '%' style "white":
                                                        xalign 0.98
                                                        yoffset 6
                                                        size 20

                                                null height 2
                    frame:
                        background None
                        ysize 700
                        xsize 475
                        ypos 60
                        xpos 500

                        vbox:
                            xsize 450

                            hbox:
                                $booknums = len(books)
                                textbutton '{size=-5}已选择的书籍（[booknums]/[nums]）{/size}' text_style "white":
                                    action NullAction()
                                    hovered Show(screen="info", i=itemKindInfo('书籍', 'i'), a=itemKindInfo('书籍', 'a'))
                                    unhovered Hide("info")
                                    xfill True
                                    xalign 1.0
                                    #background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)

                            vbox:
                                #xalign 1.0
                                $allocate_list = allocate(books, nums)

                                for no, ite in enumerate(books):
                                    frame:
                                        background None
                                        ysize 60
                                        xfill True
                                        $ite_name = ite.name
                                        $ite_pre = ite.getPrefixInfo(player)
                                        $ite_main = ite.getPrincipalInfo()
                                        $ite_suf = ite.getSuffixInfo()

                                        frame:
                                            background None
                                            textbutton ite_name text_style "white":
                                                if persistent.actionquickly:
                                                    action Hide("info"),Function(bookexecute, books, ite, nums)
                                                else:
                                                    action [Hide("info"),Show(screen="info_confirm", text=_('选择'),act=[Function(bookexecute, books, ite, nums)], pp=renpy.get_mouse_pos(), t=ite_name, i=ite_pre+'\n'+ite_main+ite_suf, a=ite.ad)]
                                                hovered [Show(screen="info", t=ite_name, i=ite_pre+'\n'+ite_main+ite_suf, a=ite.ad)]
                                                unhovered Hide("info")
                                                background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                                                if len(books)==2:
                                                    activate_sound audio.error
                                                else:
                                                    activate_sound audio.cursor
                                                xfill True

                                            text str(ite.progress*50) + '% -> ' + str(min(2, ite.progress + allocate_list[no])*50) + '%' style "white":
                                                xalign 0.98
                                                yoffset 6
                                                size 20

                                        null height 2

            imagebutton:
                idle "images/gui/opening/ok_idle.png"
                if books:
                    action Function(player.rtn, list(zip(books,allocate_list))), Return()
                    hover "images/gui/opening/ok_hover.png"
                    activate_sound audio.click1
                else:
                    action NullAction()
                    activate_sound audio.error
                xalign 0.95
                yalign 0.95
                                    
                            
                    



screen screen_tr_readingbook_confirm(player, i=_("确定不选择书籍吗？这将会导致本日程直接结束。"), width=400, pp=renpy.get_mouse_pos()):
    use barrier(screen="screen_tr_readingbook_confirm")
    style_prefix "info"
    zorder 1000
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
        at trans()
        vbox:
            align pp
            if i is not None:
                label i:
                    text_style "info_text"
                    xsize width
            null height 30
            hbox:
                xalign 0.5
                spacing 40
                textbutton _("{size=-3}确定{/size}"):
                    action [Hide("screen_tr_readingbook_confirm"), Function(player.rtn, []),Return()]
                    activate_sound audio.cursor
                textbutton _("{size=-3}返回{/size}"):
                    action Hide("screen_tr_readingbook_confirm")
                    activate_sound audio.cursor


