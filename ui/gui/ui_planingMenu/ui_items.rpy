screen screen_items(player):
    use barrier(screen="screen_items", mode=0)
    python:
        def switchmode():
            persistent.uiItemsSorted += 1
            if persistent.uiItemsSorted > 2:
                persistent.uiItemsSorted = 0

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
                    textbutton '{size=+10}库存{/size}':
                        text_style "white"
                        xoffset -5
                        yoffset -5
                        action NullAction()

                    imagebutton auto "gui/sort_%s.png":
                        xalign 0.92
                        hovered Show(screen="info", i='点击后切换道具的显示模式。')
                        unhovered Hide("info")
                        action [Function(switchmode),Hide("info")]

                    imagebutton auto "gui/exit_%s.png":
                        xalign 1.0
                        action [Hide("screen_items",transition=dissolve),Hide("info")]
                    
                    frame:
                        background None
                        ysize 680
                        xsize 980
                        xpos 10
                        ypos 80

                        viewport:
                            mousewheel True
                            draggable True
                            scrollbars "vertical"
                            if persistent.uiItemsSorted == 0:
                                use screen_items_sortedinner(player)
                            elif persistent.uiItemsSorted == 1:
                                use screen_items_sortedinner2(player)
                            else:
                                use screen_items_inner(player)
    key 'K_ESCAPE' action [Hide("screen_items",transition=dissolve),Hide("info"),Hide("info_i")]

screen screen_items_selected(player, item):
    use barrier(screen="screen_items_selected")
    style_prefix "info"
    zorder 650
    default pp = renpy.get_mouse_pos()
    python:
        p = pp
        if p[0] < 1500:
            xc = 0.0
            trans = trans_toLeft
        else:
            xc = 1.0
            trans = trans_toRight
        xc = 0.0 if p[0] < 1500 else 1.0
        yc = 0.0 if p[1] < 540 else 1.0
    frame:
        pos pp
        xanchor xc
        yanchor yc
        xsize 300
        at trans()
        vbox:
        
        
            if (BookQuickReadEffect.has(player) or Relaxation.has(player)) and player.canRead >= 0 and item.kind == _('专业类书籍'):
                frame:
                    background None
                    ysize 50
                    textbutton _("{color=#ffff00}{size=-3}速读{/size}{/color}"):
                        action [Hide("screen_items_selected"), Function(ui_itemUse, item=item, player=player)]
                        background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor 
                        text_style "white"
                        text_size 30

            
            

            elif (BookQuickReadEffect.has(player) or (Freshness.has(player) and not BookstoreBuff.has(player))) and player.canRead >= 0 and item.kind == _('书籍'):
                frame:
                    background None
                    ysize 50
                    textbutton _("{color=#ffff00}{size=-3}速读{/size}{/color}"):
                        action [Hide("screen_items_selected"), Function(ui_itemUse, item=item, player=player)]
                        background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor 
                        text_style "white"
                        text_size 30                
                                
            else:
                frame:
                    background None
                    ysize 50
                    textbutton _("{size=-3}使用{/size}"):
                        action [Hide("screen_items_selected"), Function(ui_itemUse, item=item, player=player)]
                        background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor 
                        text_style "white"
                        text_size 30      

            if type(item) == SexyPic:
                frame:
                    background None
                    ysize 50
                    textbutton _("{color=#ff94c6}{size=-3}欣赏{/size}{/color}"):
                        action [Hide("screen_items_selected"), Hide("info"), Show(screen="screen_phone_gallery_show", pic="images/cg/SexyPic.webp"),Function(Achievement314.achieve), Function(Achievement.show)]
                        background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor 
                        text_style "white"
                        text_size 30   

            if type(item) == FinishedCommission:
                if item.comm.freewheeling:
                    frame:
                        background None
                        ysize 50
                        textbutton _("{size=-3}发布到公众平台{/size}"):
                            action [Hide("screen_items_selected"), Function(item.uploadToSocial, player=player)]
                            background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                            xfill True
                            activate_sound audio.cursor 
                            text_style "white"
                            text_size 30            
                else:           
                    frame:
                        background None
                        ysize 50
                        textbutton _("{size=-3}交稿{/size}"):
                            if item.comm.broken:
                                action [Hide("screen_items_selected"), Function(showNotice, messages=[_('委托已过期，无法交付。')])]
                            else:
                                action [Hide("screen_items_selected"), Function(item.getReward, player=player)]
                            background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                            xfill True
                            activate_sound audio.cursor 
                            text_style "white"
                            text_size 30
            if not item.star:
                frame:
                    background None
                    ysize 50
                    textbutton _("{size=-3}添加到快捷栏{/size}"):
                        action [Hide("screen_items_selected"), Function(ui_itemStar, item=item)]
                        background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor 
                        text_style "white"
                        text_size 30
            else:
                frame:
                    background None
                    ysize 50
                    textbutton _("{size=-3}从快捷栏中移出{/size}"):
                        action [Hide("screen_items_selected"), Function(ui_itemUnstar, item=item)]
                        background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor 
                        text_style "white"
                        text_size 30

            if not item.blocked:
                frame:
                    background None
                    ysize 50
                    textbutton _("{size=-3}禁用快捷栏{/size}"):
                        action [Hide("screen_items_selected"), Function(ui_itemBlock, item=item)]
                        background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor 
                        text_style "white"
                        text_size 30
            else:
                frame:
                    background None
                    ysize 50
                    textbutton _("{size=-3}启用快捷栏{/size}"):
                        action [Hide("screen_items_selected"), Function(ui_itemUnblock, item=item)]
                        background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                        xfill True
                        activate_sound audio.cursor 
                        text_style "white"
                        text_size 30

            frame:
                background None
                ysize 50
                
                python:
                    ite_name = type(item).name
                    ite_pre = item.getPrefixInfo(player)
                    ite_main = item.getPrincipalInfo()
                    if type(item) in (MedicineA, MedicineB, MedicineC, MedicineD):
                        ite_main = '%s\n\n{color=#fde827}%s{/color}' % (ite_main, type(item).getrecoveryinfo(player))
                    ite_suf = item.getSuffixInfo()
                    ite_ad = item.ad if type(item) not in (FinishedCommission, UnfinishedCommission) else item.comm.inputs
                    if ite_ad is None:
                        ite_ad = ''

                    t=ite_name
                    i=ite_pre+'\n'+ite_main+ite_suf
                    a=ite_ad

                textbutton _("{size=-3}详情{/size}"):
                    action [Hide("screen_items_selected"), Show(screen="info_use",t=ite_name, i=ite_pre+'\n'+ite_main+ite_suf, a=ite_ad, pp=renpy.get_mouse_pos())]
                    background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                    xfill True
                    activate_sound audio.cursor 
                    text_style "white"
                    text_size 30

            frame:
                background None
                ysize 50
                textbutton _("{size=-3}丢弃{/size}"):
                    if item.amounts == 1:
                        action Hide("screen_items_selected"), Function(ui_itemQuit, item=item, player=player)
                    else:
                        action Hide("screen_items_selected"), Show(screen="screen_items_quitnum",player=player,item=item)
                    background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                    xfill True
                    activate_sound audio.cursor 
                    text_style "white"
                    text_size 30

            frame:
                background None
                ysize 50
                textbutton _("{size=-3}取消{/size}"):
                    action Hide("screen_items_selected")
                    background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                    xfill True
                    activate_sound audio.cursor 
                    text_style "white"
                    text_size 30
            null height 13


screen screen_items_inner(player):
    python:
        def geticon(player, item):
            if not type(item) in player.itemcd:
                return item.icon()
            cd = player.itemcd[type(item)]
            return Composite((75, 75), (0, 0), item.icon(), (0, 0), 'gui/items/cooldown.png', (0, 0),Fixed(Text(str(cd), size=30,xcenter=0.5, ycenter=0.5)))

    hbox:
        box_wrap True
        for item in player.items:

            frame:
                xsize 75
                ysize 75
                background None
                imagebutton idle geticon(player, item):
                    action Show(screen="screen_items_selected", player = player, item=item)
                    hovered Show(screen="info_i", player=player, item=item)
                    unhovered Hide("info_i")

                if item.amounts > 1:
                    text str(item.amounts) size 25
            null height 2


screen screen_items_sortedinner(player):
    python:
        def geticon(player, item):
            if not type(item) in player.itemcd:
                return item.icon()
            cd = player.itemcd[type(item)]
            return Composite((75, 75), (0, 0), item.icon(), (0, 0), 'gui/items/cooldown.png', (0, 0),Fixed(Text(str(cd), size=30,xcenter=0.5, ycenter=0.5)))

    $sorteditems = sliceArr(player.items)
    vbox:
        for items in sorteditems:
            $typename = items[0].kind
            if not typename:
                $typename = '？？？'
                $typei = '？？？'
                $typea = '\n？？？'
            else:
                $typei = itemKindInfo(typename, 'i')
                $typea = itemKindInfo(typename, 'a')
            textbutton typename text_style 'white':
                action NullAction()
                hovered Show(screen="info", i=typei, a=typea)
                unhovered Hide("info")
                background Frame("gui/style/grey_hover_background.png", tile=gui.frame_tile)
                xfill True
                ysize 40

            hbox:
                box_wrap True
                for item in items:
                    frame:
                        xsize 75
                        ysize 75
                        background None
                        imagebutton idle geticon(player, item):
                            action Show(screen="screen_items_selected", player = player, item=item)
                            hovered Show(screen="info_i", player=player, item=item)
                            unhovered Hide("info_i")

                        if item.amounts > 1:
                            text str(item.amounts) size 25
                    null height 2
            null height 10


screen screen_items_sortedinner2(player):
    python:
        def geticon(player, item):
            if not type(item) in player.itemcd:
                return item.icon()
            cd = player.itemcd[type(item)]
            return Composite((75, 75), (0, 0), item.icon(), (0, 0), 'gui/items/cooldown.png', (0, 0),Fixed(Text(str(cd), size=30,xcenter=0.5, ycenter=0.5)))

    $sorteditems = sliceArr(player.items)
    vbox:
        for items in sorteditems:
            $typename = items[0].kind
            if not typename:
                $typename = '？？？'
                $typei = '？？？'
                $typea = '\n？？？'
            else:
                $typei = itemKindInfo(typename, 'i')
                $typea = itemKindInfo(typename, 'a')
            textbutton typename text_style 'white':
                action NullAction()
                hovered Show(screen="info", i=typei, a=typea)
                unhovered Hide("info")
                background Frame("gui/style/grey_hover_background.png", tile=gui.frame_tile)
                xfill True
                ysize 40

            hbox:
                box_wrap True
                for item in items:
                    $showname = item.name
                    if len(showname) >= 9:
                        $showname='{size=-5}'+showname+'{/size}'

                    frame:
                        background None
                        xsize 300
                        ysize 90
                        textbutton showname text_style "white":
                            action Show(screen="screen_items_selected", player = player, item=item)
                            hovered Show(screen="info_i", player=player, item=item)
                            unhovered Hide("info_i")
                            background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                            activate_sound audio.cursor
                            xfill True
                            yfill True
                            text_xpos 0.28
                        imagebutton idle geticon(player, item):
                            #xalign 0.5
                            yalign 0.5
                            xoffset 4
                        
                        if item.amounts > 1:
                            text str(item.amounts) size 25


                        
                    null height 2


screen info_i(player, item, width=400, pp=renpy.get_mouse_pos()):
    style_prefix "info"
    zorder 1000

    python:
        ite_name = type(item).name
        ite_pre = item.getPrefixInfo(player)
        ite_main = item.getPrincipalInfo()
        if type(item) in (MedicineA, MedicineB, MedicineC, MedicineD):
            ite_main = '%s\n\n{color=#fde827}%s{/color}' % (ite_main, type(item).getrecoveryinfo(player))
        ite_suf = item.getSuffixInfo()
        ite_ad = item.ad if type(item) not in (FinishedCommission, UnfinishedCommission) else item.comm.inputs
        if ite_ad is None:
            ite_ad = ''

        t=ite_name
        i=ite_pre+'\n'+ite_main+ite_suf
        a=ite_ad

    
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




screen screen_items_quitnum(player, item):
    use barrier(screen="screen_items_quitnum", mode=0)
    style_prefix "info"
    default nums = str(item.amounts)
    zorder 99999
    frame at trans_Up:
        padding (15, 15)
        xcenter 0.5
        ycenter 0.45
        
        if nums and int(nums) > item.amounts:
            $nums = str(item.amounts)
        $shownum = nums if nums else '0'
        
        vbox:
            
            frame:
                background None
                xalign 0.5
                ysize 100
                yoffset 20
                $showtext = "当前有 %s 个 %s ，丢弃 %s 个 %s。" % (item.amounts, item.name, shownum, item.name)
                textbutton showtext:
                    action NullAction()
                    activate_sound audio.cursor 
                    text_style "white"
                    text_size 27
                    text_xalign 0.5

            hbox:
                xalign 0.5
                frame:
                    xalign 0.5
                    background None
                    ysize 100
                    textbutton '0':
                        if nums and nums != '0':
                            action SetLocalVariable("nums", nums+'0')
                        background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                        xsize 80
                        yfill True
                        activate_sound audio.cursor 
                        text_style "white"
                        text_size 27
                        text_xalign 0.5
                if nums and nums != '0':
                    key "K_0" action SetLocalVariable("nums", nums+'0')
                    key "K_KP0" action SetLocalVariable("nums", nums+'0')
                    

                for i in range(1, 10):
                    frame:
                        background None
                        ysize 100
                        textbutton str(i):
                            action SetLocalVariable("nums", nums+str(i))
                            background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                            xsize 80
                            yfill True
                            activate_sound audio.cursor 
                            text_style "white"
                            text_size 27
                            text_xalign 0.5
                    key "K_%s"%i action SetLocalVariable("nums", nums+str(i))
                    key "K_KP%s"%i action SetLocalVariable("nums", nums+str(i))
            hbox:
                spacing 80
                xalign 0.5
                frame:
                    background None
                    ysize 100
                    textbutton "删除":
                        if len(nums)>1:
                            action SetLocalVariable("nums", nums[:len(nums)-1])
                        else:
                            action SetLocalVariable("nums", '')
                        background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                        xsize 100
                        yfill True
                        activate_sound audio.cursor 
                        text_style "white"
                        text_size 27
                        text_xalign 0.5
                
                

                frame:
                    background None
                    ysize 100
                    textbutton "清零":
                        action SetLocalVariable("nums", '')
                        background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                        xsize 100
                        yfill True
                        activate_sound audio.cursor 
                        text_style "white"
                        text_size 27
                        text_xalign 0.5

                frame:
                    background None
                    ysize 100
                    $maxnums = str(item.amounts)
                    textbutton "最大":
                        
                        if maxnums == '0':
                            action SetLocalVariable("nums", '')
                        else:
                            action SetLocalVariable("nums", maxnums)
                        background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                        xsize 100
                        yfill True
                        activate_sound audio.cursor 
                        text_style "white"
                        text_size 27
                        text_xalign 0.5
                frame:
                    background None
                    ysize 100
                    textbutton "确定":
                        if not nums:
                            action Function(showNotice, ["数量不能为空。"])
                        else:
                            action Function(ui_itemQuit, item=item, player=player, nums=int(nums)),Hide("screen_items_quitnum")
                        background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                        xsize 100
                        yfill True
                        activate_sound audio.cursor 
                        text_style "white"
                        text_size 27
                        text_xalign 0.5

                
                frame:
                    background None
                    ysize 100
                    textbutton "返回":
                        action Hide("screen_items_quitnum")
                        background Frame("gui/style/select_[prefix_]background.png", tile=gui.frame_tile)
                        xsize 100
                        yfill True
                        activate_sound audio.cursor 
                        text_style "white"
                        text_size 27
                        text_xalign 0.5

            if len(nums)>1:
                key 'K_BACKSPACE' action SetLocalVariable("nums", nums[:len(nums)-1])
            else:
                key 'K_BACKSPACE' action SetLocalVariable("nums", '')

            if not nums:
                key 'K_RETURN' action Function(showNotice, ["数量不能为空。"])
                key 'K_KP_ENTER' action Function(showNotice, ["数量不能为空。"])
            else:
                key 'K_RETURN' action Function(ui_itemQuit, item=item, player=player, nums=nums),Hide("screen_items_quitnum")
                key 'K_KP_ENTER' action Function(ui_itemQuit, item=item, player=player, nums=nums),Hide("screen_items_quitnum")
                    
            key 'K_ESCAPE' action Hide("screen_items_quitnum")