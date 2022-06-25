screen screen_tasks(player):
    #tag gamegui
    use barrier(screen="screen_tasks")
    default only_avaiable_task = True
    default unlocked_but_can_unlock = False

    $ tasks = sliceTypeArr(getSubclasses(Task))
    $ del tasks[0]

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
                            textbutton '{size=+10}日程安排{/size}':
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
                                    if only_avaiable_task == True:
                                        textbutton '{color=#9370db}仅显示当前可安排的日程{/color}' text_style "gameUI":
                                            action [SetLocalVariable("only_avaiable_task", False), Hide("info"), Hide("info3")]
                                            activate_sound audio.cursor
                                            #background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                            xfill True
                                    else:
                                        textbutton '仅显示当前可安排的日程' text_style "gameUI":
                                            action [SetLocalVariable("only_avaiable_task", True), Hide("info"), Hide("info3")]
                                            activate_sound audio.cursor
                                            #background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                            xfill True
                                    
                                    if unlocked_but_can_unlock == True:
                                        textbutton '{color=#9370db}仅显示未解锁但已达成解锁条件的日程{/color}' text_style "gameUI":
                                            action [SetLocalVariable("unlocked_but_can_unlock", False), Hide("info"), Hide("info3")]
                                            activate_sound audio.cursor
                                            #background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                            xfill True
                                    else:
                                        textbutton '仅显示未解锁但已达成解锁条件的日程' text_style "gameUI":
                                            action [SetLocalVariable("unlocked_but_can_unlock", True), Hide("info"), Hide("info3")]
                                            activate_sound audio.cursor
                                            #background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                            xfill True
                                

                    frame:
                        #xoffset -10
                        background None
                        ysize 400
                        xsize 380
                        ypos 60
                        xpos 10
                        use plan_show(player)

                frame:
                    background None
                    xsize 400
                    ysize 800

                    imagebutton auto "gui/icons/task_icon/exit_%s.png":
                        xalign 0.98
                        action [Hide("screen_tasks",transition=dissolve),Hide("info"),Hide("info3")]
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
                            use tasks_show(player, tasks, only_avaiable_task, unlocked_but_can_unlock)
                    frame:
                        #xoffset -10
                        background None
                        ysize 40
    
    key 'K_ESCAPE' action [Hide("screen_tasks",transition=dissolve),Hide("info"),Hide("info3")]
    key 'q' action [Hide("screen_tasks",transition=dissolve),Hide("info"),Hide("info3")]
    key 'w' action [Hide("screen_tasks",transition=dissolve),Hide("info"),Hide("info3")]
    key 'e' action [Hide("screen_tasks",transition=dissolve),Hide("info"),Hide("info3")]
    key 'r' action [Hide("screen_tasks",transition=dissolve),Hide("info"),Hide("info3")]

        
                

screen tasks_show(player, tasks, only_avaiable_task, unlocked_but_can_unlock):

    python:
        def returnOnlyAvaiableTask(player, tasks):
            newtasks = []
            for i in tasks:
                l = list(filter(lambda x:x.checkAvailable(player, player.today, player.findNoTask()) == True, i))
                if l!= []:
                    newtasks.append(l)
            return newtasks

        def returnUnlockedButCanUnlock(player, tasks):
            newtasks = []
            for i in tasks:
                l = list(filter(lambda x:x.unlocked == False and x.unlockCond(player) == True, i))
                if l!= []:
                    newtasks.append(l)
            return newtasks
    
    vbox:
        if only_avaiable_task:
            $tasks = returnOnlyAvaiableTask(player, tasks)
        if unlocked_but_can_unlock:
            $tasks = returnUnlockedButCanUnlock(player, tasks)
        xsize 460
        default isFold = {
            '工作类':False,
            '运动类':False,
            '写作类':False,
            '休息类':False,
            '特殊类':False
        }
        for i in tasks:
            $i.sort(key=lambda x: x.id)
            $typename = i[0].kind
            $typei = taskKindInfo(typename, 'i')
            $typea = taskKindInfo(typename, 'a')
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
                        xoffset -140
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
                        xoffset -140
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

                            if ite.hasplot(player):
                                $ plot_info = red('\n\n会触发新剧情！')
                            else:
                                $ plot_info = ''
                            $ type_info = ''
                            if ite.kind != None:
                                $ type_info = '\n\n'+ite.kind
                            frame:
                                background None
                                if ite.checkAvailable(player, player.today, player.findNoTask()) != True:

                                    $error_info = '无法安排该日程！\n' + ite.checkAvailable(player, player.today, player.findNoTask())

                                    textbutton '{color=#b3b3b3}' + ite_name + '{/color}' text_style "white":
                                        action [Hide("info3"), Show(screen="task_unlock", player=player, item=ite, pp=renpy.get_mouse_pos(), t=ite_name, i1=ite.info + type_info + plot_info + red('\n\n' +error_info), a1=ite.ad)]
                                        hovered Show(screen="info3", t=ite_name, i1=ite.info + type_info + plot_info + red('\n\n' +error_info), a1=ite.ad)
                                        unhovered Hide("info3")
                                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                        xfill True
                                        activate_sound audio.error

                                else:

                                    textbutton ite_name text_style "white":
                                        action [Hide("info3"), Show(screen="task_use", player=player, item=ite, pp=renpy.get_mouse_pos(), t=ite_name, i1=ite.info + type_info + plot_info, a1=ite.ad)]
                                        hovered Show(screen="info3", t=ite_name, i1=ite.info + type_info + plot_info, a1=ite.ad)
                                        unhovered Hide("info3")
                                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                                        xfill True
                                        activate_sound audio.cursor

                        null height 2
        null height 30
        textbutton ''


screen plan_show(player):
    $times = ('{size=-5}上午{/size}', '{size=-5}下午{/size}', '{size=-5}夜晚{/size}')


    vbox:
        xsize 460
        for i in range(3):
            $ plot_info = red('\n\n会触发新剧情！') if player.plan[i].hasplot(player) else ''
            $ ctc_info = '\n\n单击以取消该日程安排。' if player.plan[i].name != '未安排' else '\n\n在右侧选择要安排在该时间段的日程。'
            $ type_info = ''
            if player.plan[i].kind != None:
                $ type_info = '\n\n'+player.plan[i].kind

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
                    textbutton player.plan[i].name text_style "white":
                        action [Hide("info3"), Function(player.removeTask, i)]
                        hovered Show(screen="info3", t=player.plan[i].name, i1=player.plan[i].info+type_info + ctc_info+ plot_info, a1=player.plan[i].ad)
                        unhovered Hide("info3")
                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                        xsize 330
                        activate_sound audio.cursor
            null height 2
        null height 30
        

        
screen task_use(player, item, pp, t=None, i1=None, a1=None, i2=None, a2=None, width=400):
    style_prefix "info"
    use barrier(screen="task_use")
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
                textbutton _("{size=-3}添加日程{/size}"):
                    action [Hide("task_use"), Function(player.setTask, item)]
                    activate_sound audio.cursor
                textbutton _("{size=-3}返回{/size}"):
                    action Hide("task_use")
                    activate_sound audio.cursor

    key 'K_ESCAPE' action Hide("task_use")


screen task_unlock(player, item, pp, t=None, i1=None, a1=None, i2=None, a2=None, width=400):
    style_prefix "info"
    use barrier(screen="task_unlock")
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
                #$error_info = '无法解锁该日程！\n' + item.unlockClass(player, player.today, player.findNoTask())
                if not item.unlocked:
                    textbutton _("{size=-3}解锁日程{/size}"):
                        action [Function(item.unlockClass, player), Hide("task_unlock")]
                        activate_sound audio.cursor
                textbutton _("{size=-3}返回{/size}"):
                    action Hide("task_unlock")
                    activate_sound audio.cursor