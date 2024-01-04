screen screen_tasks(player):
    #tag gamegui
    use barrier(screen="screen_tasks", mode=0)
    default show_all_task = False

    python:
        if player.cured > -1:
            tasks = [[CuredWork, CuredRest, CuredHosp]]
        elif player.finalStageDays > -1:
            tasks = [[DespairWaiting, DespairObserve, DespairDistribute]]
        else:
            tasks = sliceArr(ALLTASKS)
            del tasks[0]
        


    #modal True
    zorder 550
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
                            textbutton _('{size=+10}日程安排{/size}'):
                                xoffset -15
                                yoffset -10
                                text_style "gameUI"
                            null height 350
                            textbutton _('设置'):
                                xoffset -10
                                yoffset -10
                                text_style "white"
                            frame:
                                background None
                                textbutton _('显示所有日程') text_style "gameUI":
                                    action [ToggleLocalVariable("show_all_task", True, False), Hide("info"), Hide("info3")]
                                    activate_sound audio.cursor
                                    xfill True

                                if show_all_task:
                                    imagebutton idle "gui/right_.png":
                                        xalign 0.9
                                        

                                

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

                    imagebutton auto "gui/exit_%s.png":
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
                            use tasks_show(player, tasks, show_all_task)
                    frame:
                        #xoffset -10
                        background None
                        ysize 40
    
    key 'K_ESCAPE' action [Hide("screen_tasks",transition=dissolve),Hide("info"),Hide("info3")]

        

screen screen_tasks_extra(player):
    #tag gamegui
    default show_all_task = False

    python:
        tasks = sliceArr(ALLTASKS)
        del tasks[0]
        


    #modal True
    zorder 600
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
                            textbutton _('{size=+10}日程安排{/size}'):
                                xoffset -15
                                yoffset -10
                                text_style "gameUI"
                            null height 430
                            textbutton _('设置'):
                                xoffset -10
                                yoffset -10
                                text_style "white"
                            frame:
                                background None
                                textbutton _('显示所有日程') text_style "gameUI":
                                    action [ToggleLocalVariable("show_all_task", True, False), Hide("info"), Hide("info3")]
                                    activate_sound audio.cursor
                                    xfill True

                                if show_all_task:
                                    imagebutton idle "gui/right_.png":
                                        xalign 0.9
                                        

                                

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

                    imagebutton auto "gui/exit_%s.png":
                        xalign 0.98
                        action [Return(),Hide("info"),Hide("info3")]
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
                            use tasks_show(player, tasks, show_all_task)
                    frame:
                        #xoffset -10
                        background None
                        ysize 40
    
    key 'K_ESCAPE' action [Return(),Hide("info"),Hide("info3")]


screen tasks_show(player, tasks, show_all_task):

    python:
        def returnOnlyAvaiableTask(player, tasks):
            newtasks = []
            for i in tasks:
                l = list(filter(lambda x:x.checkAvailable(player, player.today, player.findNoTask()) == True, i))
                if l!= []:
                    newtasks.append(l)
            return newtasks

        def LockedTaskInLowPriority(x):
            if x.isUnlocked(p):
                return x.id
            return x.id + 1000
    
    vbox:
        python:
            if show_all_task == False:
                tasks = returnOnlyAvaiableTask(player, tasks)

            TasksReadyToUnlock = list(filter(lambda x:x.isUnlocked(p) == False and x.unlockCond(p) == True, ALLTASKS))
            if show_all_task:
                TasksHaveNewPlot = list(filter(lambda x:x.hasplot(p), ALLTASKS))
            else:
                TasksHaveNewPlot = list(filter(lambda x:x.hasplot(p) and x.checkAvailable(p, p.today, p.findNoTask()) == True, ALLTASKS))

        xsize 460

        if persistent.unlocktesttask:


            vbox:
                use print_single_tasks(TestTask, player)


        if TasksReadyToUnlock and p.cured == -1 and p.finalStageDays == -1:
            $TasksReadyToUnlock.sort(key=lambda x: x.id)
            $typename = _('{color=#ffe032}可解锁的日程{/color}')
            $typei = _('该分类下的日程为达成了解锁条件但没解锁的日程。')
            $typea = _('为什么我做一件事也要去解锁？难道我在身体素质不达标之前连跑步都做不到吗？')


            hbox:
                
                textbutton '{size=-5}'+typename+'{/size}' text_style "white":
                    action NullAction()
                    hovered Show(screen="info", i=typei, a=typea)
                    unhovered Hide("info")
                    xfill True
                    xalign 1.0
                    activate_sound audio.cursor
                    xoffset -5
                    

            vbox:
                for ite in TasksReadyToUnlock:
                    use print_single_tasks(ite, player)

        if TasksHaveNewPlot and p.cured == -1 and p.finalStageDays == -1:
            $TasksHaveNewPlot.sort(key=lambda x: x.id)
            $typename = _('{color=#ffe032}可触发新剧情的日程{/color}')
            $typei = _('该分类下的日程为可以触发新的人物剧情的日程。')
            $typea = _('所以我是怎么知道如果我做这件事就能遇上什么新事情的呢？')


            hbox:
                
                textbutton '{size=-5}'+typename+'{/size}' text_style "white":
                    action NullAction()
                    hovered Show(screen="info", i=typei, a=typea)
                    unhovered Hide("info")
                    xfill True
                    xalign 1.0
                    activate_sound audio.cursor
                    xoffset -5
                        

            vbox:
                for ite in TasksHaveNewPlot:
                    use print_single_tasks(ite, player)

        for i in tasks:
            $i.sort(key=LockedTaskInLowPriority)
            $typename = i[0].kind
            $typei = taskKindInfo(typename, 'i')
            $typea = taskKindInfo(typename, 'a')
            hbox:
                textbutton '{size=-5}'+typename+'{/size}' text_style "white":
                    action NullAction()
                    hovered Show(screen="info", i=typei, a=typea)
                    unhovered Hide("info")
                    xfill True
                    xalign 1.0
                    activate_sound audio.cursor
                    xoffset -5
                        
                

            vbox:
                for ite in i:
                    use print_single_tasks(ite, player)
        null height 30
        textbutton ''

screen print_single_tasks(ite, player):
    $lock = True
    if AcolasItem4.has(player):
        $ite = AcolasTask1
    if player.times <= 2 or GameDifficulty1.has(player) or GameDifficulty2.has(player) or persistent.unlockplan:
        $lock = False
    if (player.times == 5 and player.plan[0] == SkipTask) or (player.times == 10 and player.plan[1] == SkipTask):
        $lock = False
    frame:
        background None
        ysize 60
        xfill True
        $ite_name = ite.name

        if ite.hasplot(player):
            $ plot_info = red(_('\n\n会触发新剧情！'))
        else:
            $ plot_info = ''
        $ type_info = ''
        if ite.kind != None:
            $ type_info = _('\n\n')+ite.kind
        frame:
            background None
            if ite.checkAvailable(player, player.today, player.findNoTask()) != True:

                $error_info = _('无法安排该日程！\n') + ite.checkAvailable(player, player.today, player.findNoTask())

                $locked_name = "？？？"
                $locked_info = "？？？？？？？？\n？？？？？？？？？？？"
                

                $show_name = ite_name if ite.isUnlocked(player) else locked_name
                $show_info = ite.info + type_info + plot_info if ite.isUnlocked(player) else locked_info
                $show_a = ite.ad if ite.isUnlocked(player) else locked_info

                textbutton show_name text_style "grey":
                    if persistent.actionquickly:
                        action Hide("info"),Function(ite.unlockClass, player)
                    else:
                        action [Hide("info"), Show(screen="task_unlock", player=player, item=ite, pp=renpy.get_mouse_pos(), t=show_name, i=show_info + red(_('\n\n') +error_info), a=show_a)]
                    hovered Show(screen="info", t=show_name, i=show_info + red(_('\n\n') +error_info), a=show_a)
                    unhovered Hide("info")
                    background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                    xfill True
                    activate_sound audio.error

            else:

                textbutton ite_name text_style "white":
                    if lock and player.findNoTask() == 2 and player.plan[2] != NoTask:
                        action Function(showNotice, [_('你已经定好日程了，你不想再随意调整。')])
                    else:
                        if persistent.actionquickly:
                            action [Hide("info"), Function(player.setTask, ite)]
                        else:
                            action [Hide("info"), Show(screen="info_confirm", text=_('添加日程'), act=Function(player.setTask, ite), pp=renpy.get_mouse_pos(), t=ite_name, i=ite.info + type_info + plot_info, a=ite.ad)]
                    hovered Show(screen="info", t=ite_name, i=ite.info + type_info + plot_info, a=ite.ad)
                    unhovered Hide("info")
                    background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                    xfill True
                    activate_sound audio.cursor
    null height 2


screen plan_show(player):
    $lock = True
    if player.times <= 2 or GameDifficulty1.has(player) or GameDifficulty2.has(player) or persistent.unlockplan:
        $lock = False
    if (player.times == 5 and player.plan[0] == SkipTask) or (player.times == 10 and player.plan[1] == SkipTask):
        $lock = False
    $times = (_('{size=-5}上午{/size}'), _('{size=-5}下午{/size}'), _('{size=-5}夜晚{/size}'), _('{size=-5}深夜{/size}'))
    $tasknums = 3 if not Stayuplate.has(player) else 4

    vbox:
        xsize 460
        for i in range(tasknums):
            $ plot_info = red(_('\n\n会触发新剧情！')) if player.plan[i].hasplot(player) else ''
            $ ctc_info = _('\n\n单击以取消该日程安排。') if player.plan[i].name != _('未安排') else _('\n\n在右侧选择要安排在该时间段的日程。')
            $ type_info = ''
            if player.plan[i].kind != None:
                $ type_info = _('\n\n')+player.plan[i].kind

            textbutton times[i] text_style "white":
                action NullAction()
                xsize 330
                xoffset -5
                #background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
            frame:
                background None
                ysize 60
                xsize 330
                frame:
                    background None
                    if player.plancheck[i]:
                        $showtaskname = _('{s}%s{/s}') % player.plan[i].name
                    else:
                        $showtaskname = player.plan[i].name
                    textbutton showtaskname text_style "white":
                        if player.plan[i] == SkipTask:
                            action Function(showNotice, [_('你已经睡过了这一整个时间段。')])
                        elif lock and i != 3:
                            action Function(showNotice, [_('你已经定好日程了，你不想再随意调整。')])
                        elif player.hal_p == 50 and player.today == 6 and i == 1 and player.plan[1] == BadmintonClass:
                            action Function(showNotice, [_('我就是为了这个才请假的。')])
                        else:
                            action [Hide("info"), Function(player.removeTask, i)]
                        hovered Show(screen="info", t=player.plan[i].name, i=player.plan[i].info+type_info + ctc_info+ plot_info, a=player.plan[i].ad)
                        unhovered Hide("info")
                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                        xsize 330
                        activate_sound audio.cursor
            null height 2
        null height 30
        

        
screen task_use(player, item, pp, t=None, i=None, a=None, width=400):
    style_prefix "info"
    use barrier(screen="task_use")
    zorder 3000
    $p = pp
    $yc = 0.0 if p[1] < 540 else 1.0
    if width == 400:
        if a:
            if len(i) + len(a) > 150:
                $width = 600
        else:
            if len(i) > 100:
                $width = 600
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
                label '[t!t]\n':
                    text_style "info_text"
                    xsize width
            if i is not None:
                null height -8
                label '{size=-2}'+i+'{/size}':
                    text_style "info_text"
                    xsize width
            if a is not None:
                null height 13
                label '{i}[a!t]{/i}':
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

    key 'K_ESCAPE' action Hide("task_use"),Hide("info")


screen task_unlock(player, item, pp, t=None, i=None, a=None, width=400):
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
    if width == 400:
        if a:
            if len(i) + len(a) > 150:
                $width = 600
        else:
            if len(i) > 100:
                $width = 600
    frame:
        pos p
        padding (15, 15)
        xanchor xc
        yanchor yc
        at trans()
        vbox:
            align p
            if t is not None:
                label '[t!t]\n':
                    text_style "info_text"
                    xsize width
            if i is not None:
                null height -8
                label '{size=-2}'+i+'{/size}':
                    text_style "info_text"
                    xsize width
            if a is not None:
                null height 13
                label '{i}[a!t]{/i}':
                    text_style "admonition_text"
                    xsize width

            null height 30
            hbox:
                xalign 0.5
                spacing 40
                #$error_info = _('无法解锁该日程！\n') + item.unlockClass(player, player.today, player.findNoTask())
                if not item.isUnlocked(player):
                    textbutton _("{size=-3}解锁日程{/size}"):
                        action [Function(item.unlockClass, player), Hide("task_unlock")]
                        activate_sound audio.cursor
                textbutton _("{size=-3}返回{/size}"):
                    action Hide("task_unlock")
                    activate_sound audio.cursor







screen tutorial_screen_tasks(player):
    #tag gamegui
    
    python:

        def returnOnlyAvaiableTask(player, tasks):
            newtasks = []
            for i in tasks:
                l = list(filter(lambda x:x.checkAvailable(player, player.today, player.findNoTask()) == True, i))
                if l!= []:
                    newtasks.append(l)
            return newtasks
        tasks = returnOnlyAvaiableTask(player, sliceArr(ALLTASKS))
        del tasks[0]

    #modal True
    zorder 200
    drag:
        xcenter 0.503
        ycenter 0.35
        frame:
            at trans_toRight()
            style "translucent_frame"
            xsize 800
            ysize 600
            hbox:


                frame:
                    background None
                    xsize 400
                    ysize 600
                    frame:
                        background None
                        vbox:
                        #xoffset -15
                        #yoffset -10
                            textbutton _('{size=+10}日程安排{/size}'):
                                xoffset -15
                                yoffset -10
                                text_style "gameUI"
                                

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
                    ysize 500

                    frame:
                        background None
                        ysize 500
                        xsize 400
                        ypos 60
                        xpos -15

                        viewport:
                            mousewheel True
                            #draggable True
                            scrollbars "vertical"
                            
                            
                            vbox:

                                xsize 460

                                for i in tasks:
                                    $typename = i[0].kind
                                    $typei = taskKindInfo(typename, 'i')
                                    $typea = taskKindInfo(typename, 'a')
                                    hbox:
                                        textbutton '{size=-5}'+typename+'{/size}' text_style "white":
                                            action NullAction()
                                            hovered Show(screen="info", i=typei, a=typea)
                                            unhovered Hide("info")
                                            xfill True
                                            xalign 1.0
                                            activate_sound audio.cursor
                                            xoffset -5

                                    vbox:
                                        for ite in i:
                                            use print_single_tasks(ite, player)
                                null height 30
                                textbutton ''
                    frame:
                        #xoffset -10
                        background None
                        ysize 40