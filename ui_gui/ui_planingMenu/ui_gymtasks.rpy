screen screen_gymtasks(player):
    #tag gamegui
    use barrier(screen="screen_gymtasks", mode=0)
    default only_avaiable_gymtask = True
    default unlocked_but_can_unlock = False

    $ gymtasks = sliceTypeArr(getSubclasses(GymTask))
    $ gymtasks[0].remove(NoSport)

    #modal True
    zorder 200
    drag:
        xcenter 0.503
        ycenter 0.48
        frame:
            at trans_toRight()
            style "translucent_frame"
            xsize 800
            ysize 800
            hbox:


                frame:
                    background None
                    xsize 400
                    ysize 800
                    frame:
                        background None
                        vbox:
                        #xoffset -15
                        #yoffset -10
                            textbutton '{size=+10}健身日程安排{/size}':
                                xoffset -15
                                yoffset -10
                                text_style "gameUI"
                            null height 350
                            textbutton '筛选设置':
                                xoffset -10
                                yoffset -10
                                text_style "white"
                            frame:
                                background None
                                vbox:
                                    if only_avaiable_gymtask == True:
                                        textbutton '{color=#9370db}仅显示当前可安排的健身日程{/color}' text_style "gameUI":
                                            action [SetLocalVariable("only_avaiable_gymtask", False), Hide("info"), Hide("info3")]
                                            activate_sound audio.cursor
                                            #background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                            xfill True
                                    else:
                                        textbutton '仅显示当前可安排的健身日程' text_style "gameUI":
                                            action [SetLocalVariable("only_avaiable_gymtask", True), Hide("info"), Hide("info3")]
                                            activate_sound audio.cursor
                                            #background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                            xfill True
                                    
                                    if unlocked_but_can_unlock == True:
                                        textbutton '{color=#9370db}仅显示未解锁但已达成解锁条件的健身日程{/color}' text_style "gameUI":
                                            action [SetLocalVariable("unlocked_but_can_unlock", False), Hide("info"), Hide("info3")]
                                            activate_sound audio.cursor
                                            #background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                            xfill True
                                    else:
                                        textbutton '仅显示未解锁但已达成解锁条件的健身日程' text_style "gameUI":
                                            action [SetLocalVariable("unlocked_but_can_unlock", True), Hide("info"), Hide("info3")]
                                            activate_sound audio.cursor
                                            #background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                            xfill True
                                

                    frame:
                        background None
                        ysize 400
                        xsize 380
                        ypos 60
                        xpos 0
                        use gymplan_show(player)

                frame:
                    background None
                    xsize 400
                    ysize 800

                    imagebutton auto "gui/icons/task_icon/exit_%s.png":
                        xalign 0.98
                        action [Hide("screen_gymtasks"),Hide("info"),Hide("info3"),Return()]
                        activate_sound audio.cursor

                    frame:
                        background None
                        ysize 700
                        xsize 400
                        ypos 60
                        xpos -15

                        viewport:
                            mousewheel True
                            #draggable True
                            scrollbars "vertical"
                            use gymtasks_show(player, gymtasks, only_avaiable_gymtask, unlocked_but_can_unlock)
                    frame:
                        #xoffset -10
                        background None
                        ysize 40

    key 'K_ESCAPE' action [Hide("screen_gymtasks"),Hide("info"),Hide("info3"),Return()]
        
                

screen gymtasks_show(player, gymtasks, only_avaiable_gymtask, unlocked_but_can_unlock):

    python:
        def returnOnlyAvaiablegymtask(player, gymtasks):
            newgymtasks = []
            for i in gymtasks:
                l = list(filter(lambda x:x.checkAvailable(player, player.today, player.findNoSport()) == True, i))
                if l!= []:
                    newgymtasks.append(l)
            return newgymtasks

        def returnUnlockedButCanUnlock(player, gymtasks):
            newgymtasks = []
            for i in gymtasks:
                l = list(filter(lambda x:x.unlocked == False and x.unlockCond(player) == True, i))
                if l!= []:
                    newgymtasks.append(l)
            return newgymtasks
    
    vbox:
        if only_avaiable_gymtask:
            $gymtasks = returnOnlyAvaiablegymtask(player, gymtasks)
        if unlocked_but_can_unlock:
            $gymtasks = returnUnlockedButCanUnlock(player, gymtasks)
        xsize 460
        default isFold = {
            '无难度':False,
            '低难度':False,
            '中难度':False,
            '高难度':False
        }
        for i in gymtasks:
            $i.sort(key=lambda x: x.id)
            $typename = i[0].kind
            $typei = taskKindInfo('运动类', 'i')
            $typea = taskKindInfo('运动类', 'a')
            hbox:
                if isFold[typename] == False:
                    textbutton '{size=-5}'+typename+'{/size}' text_style "white":
                        action [SetDict(isFold, typename, True),Hide("info")]
                        hovered Show(screen="info", i=typei+'\n\n单击以折叠该类日程。', a=typea)
                        unhovered Hide("info")
                        xfill True
                        xalign 1.0
                        activate_sound audio.cursor
                        xoffset -5
                        #background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                
                    imagebutton idle "gui/style/folded.png":
                        xoffset -150
                        yoffset 10
                        #at reverse
                        #xanchor 0.0
                else:

                    textbutton '{size=-5}'+typename+'{/size}' text_style "white":
                        action [SetDict(isFold, typename, False),Hide("info")]
                        hovered Show(screen="info", i=typei+'\n\n单击以展开该类日程。', a=typea)
                        unhovered Hide("info")
                        xfill True
                        xalign 1.0
                        activate_sound audio.cursor
                        xoffset -5
                        #background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)


                    imagebutton idle "gui/style/folded.png":
                        xoffset -150
                        yoffset 10
                        at reverse
                        #xanchor 0.0

            if isFold[typename] == False:
                vbox:
                    #xalign 1.0
                    for ite in i:
                        frame:
                            background None
                            ysize 60
                            xfill True
                            $ite_name = ite.name

                            $ type_info = ''
                            if ite.kind != None:
                                $ type_info = '\n\n'+ite.kind
                            frame:
                                background None
                                if ite.checkAvailable(player, player.today, player.findNoSport()) != True:

                                    $error_info = '无法安排该健身日程！\n' + ite.checkAvailable(player, player.today, player.findNoSport())

                                    textbutton ite_name text_style "grey":
                                        action [Hide("info3"), Show(screen="gymtask_unlock", player=player, item=ite, pp=renpy.get_mouse_pos(), t=ite_name, i1=ite.info + type_info, a1=ite.ad)]
                                        hovered Show(screen="info3", t=ite_name, i1=ite.info + type_info + red('\n\n' +error_info), a1=ite.ad)
                                        unhovered Hide("info3")
                                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                        xfill True
                                        activate_sound audio.error

                                else:

                                    textbutton ite_name text_style "white":
                                        action [Hide("info3"), Show(screen="gymtask_use", player=player, item=ite, pp=renpy.get_mouse_pos(), t=ite_name, i1=ite.info + type_info, a1=ite.ad)]
                                        hovered Show(screen="info3", t=ite_name, i1=ite.info + type_info, a1=ite.ad)
                                        unhovered Hide("info3")
                                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                        xfill True
                                        activate_sound audio.cursor

                        null height 2
        null height 30
        textbutton ''


screen gymplan_show(player):
    $times = ('{size=-5}时段1{/size}', '{size=-5}时段2{/size}', '{size=-5}时段3{/size}')


    vbox:
        xsize 460
        for i in range(3):
            $ ctc_info = '\n\n单击以取消该健身日程安排。' if player.gymplan[i].name != '未安排健身日程' else '\n\n在右侧选择要安排在该时间段的健身日程。'
            $ type_info = ''
            if player.gymplan[i].kind != None:
                $ type_info = '\n\n'+player.gymplan[i].kind

            textbutton times[i] text_style "white":
                action NullAction()
                xsize 330
                xoffset -5
                #background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
            frame:
                background None
                ysize 60
                xsize 330
                frame:
                    background None
                    textbutton player.gymplan[i].name text_style "white":
                        action [Hide("info3"), Function(player.removegymtask, i)]
                        hovered Show(screen="info3", t=player.gymplan[i].name, i1=player.gymplan[i].info+type_info + ctc_info, a1=player.gymplan[i].ad)
                        unhovered Hide("info3")
                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                        xsize 330
                        activate_sound audio.cursor
            null height 2
        null height 30
        

        
screen gymtask_use(player, item, pp, t=None, i1=None, a1=None, i2=None, a2=None, width=400):
    style_prefix "info"
    use barrier(screen="gymtask_use")
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
                spacing 40
                textbutton _("{size=-3}添加健身日程{/size}"):
                    action [Hide("gymtask_use"), Function(player.setgymtask, item)]
                    activate_sound audio.cursor
                textbutton _("{size=-3}返回{/size}"):
                    action Hide("gymtask_use")
                    activate_sound audio.cursor
    key 'K_ESCAPE' action Hide("gymtask_use")


screen gymtask_unlock(player, item, pp, t=None, i1=None, a1=None, i2=None, a2=None, width=400):
    style_prefix "info"
    use barrier(screen="gymtask_unlock")
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
                spacing 40
                #$error_info = '无法安排该健身日程！\n' + item.checkAvailable(player, player.today, player.findNoSport())
                textbutton _("{size=-3}解锁健身日程{/size}"):
                    action [Function(item.unlockClass, player), Hide("gymtask_unlock")]
                    activate_sound audio.cursor
                textbutton _("{size=-3}返回{/size}"):
                    action Hide("gymtask_unlock")
                    activate_sound audio.cursor

    key 'K_ESCAPE' action Hide("gymtask_unlock")