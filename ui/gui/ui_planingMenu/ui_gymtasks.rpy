screen screen_gymtasks(player):
    #tag gamegui
    use barrier(screen="screen_gymtasks", mode=0)
    default show_all_task = False

    $ gymtasks = sliceArr(ALLGYMTASKS)
    $ gymtasks[0].remove(NoSport)

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
                            textbutton _('{size=+10}健身日程安排{/size}'):
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

                    imagebutton auto "gui/exit_%s.png":
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
                            use gymtasks_show(player, gymtasks, show_all_task)
                    frame:
                        #xoffset -10
                        background None
                        ysize 40

    key 'K_ESCAPE' action [Hide("screen_gymtasks"),Hide("info"),Hide("info3"),Return()]
        
                

screen gymtasks_show(player, gymtasks, show_all_task):

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
        if show_all_task == False:
            $gymtasks = returnOnlyAvaiableTask(player, gymtasks)


        $UnlockedButCanUnlock = list(filter(lambda x:x.isUnlocked(p) == False and x.unlockCond(p) == True, ALLGYMTASKS))

        xsize 460

        if UnlockedButCanUnlock:
            $UnlockedButCanUnlock.sort(key=lambda x: x.id)
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
                for ite in UnlockedButCanUnlock:
                    use print_single_gymtasks(ite, player)



        for i in gymtasks:
            $i.sort(key=LockedTaskInLowPriority)
            $typename = i[0].kind
            $typei = taskKindInfo('运动类', 'i')
            $typea = taskKindInfo('运动类', 'a')
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
                #xalign 1.0
                for ite in i:
                    use print_single_gymtasks(ite, player)
                        
        null height 30
        textbutton ''


screen print_single_gymtasks(ite, player):
    frame:
        background None
        ysize 60
        xfill True
        $ite_name = ite.name

        $ type_info = ''
        if ite.kind != None:
            $ type_info = _('\n\n')+ite.kind
        frame:
            background None
            if ite.checkAvailable(player, player.today, player.findNoSport()) != True:

                $error_info = _('无法安排该健身日程！\n') + ite.checkAvailable(player, player.today, player.findNoSport())

                $locked_name = "？？？"
                $locked_info = "？？？？？？？？\n？？？？？？？？？？？"
                

                $show_name = ite_name if ite.isUnlocked(player) else locked_name
                $show_info = ite.info + type_info  if ite.isUnlocked(player) else locked_info
                $show_a = ite.ad if ite.isUnlocked(player) else locked_info

                textbutton show_name text_style "grey":
                    if persistent.actionquickly:
                        action Hide("info"),Function(ite.unlockClass, player)
                    else:
                        action [Hide("info"), Show(screen="info_confirm", text=_('解锁健身日程'),act=Function(ite.unlockClass, player), pp=renpy.get_mouse_pos(), t=show_name, i=show_info + red(_('\n\n') +error_info), a=show_a)]
                    hovered Show(screen="info", t=show_name, i=show_info + red(_('\n\n') +error_info), a=show_a)
                    unhovered Hide("info")
                    background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                    xfill True
                    activate_sound audio.error

            else:

                textbutton ite_name text_style "white":
                    if persistent.actionquickly:
                        action [Hide("info"), Function(player.setgymtask, ite)]
                    else:
                        action [Hide("info"), Show(screen="info_confirm",text=_('添加到健身日程'),act=Function(player.setgymtask, ite), pp=renpy.get_mouse_pos(), t=ite_name, i=ite.info + type_info, a=ite.ad)]
                    hovered Show(screen="info", t=ite_name, i=ite.info + type_info, a=ite.ad)
                    unhovered Hide("info")
                    background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                    xfill True
                    activate_sound audio.cursor

    null height 2

screen gymplan_show(player):
    $times = (_('{size=-5}时段1{/size}'), _('{size=-5}时段2{/size}'), _('{size=-5}时段3{/size}'))


    vbox:
        xsize 460
        for i in range(3):
            $ ctc_info = _('\n\n单击以取消该健身日程安排。') if player.gymplan[i].name != _('未安排健身日程') else _('\n\n在右侧选择要安排在该时间段的健身日程。')
            $ type_info = ''
            if player.gymplan[i].kind != None:
                $ type_info = _('\n\n')+player.gymplan[i].kind

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
                    textbutton player.gymplan[i].name text_style "white":
                        action [Hide("info"), Function(player.removegymtask, i)]
                        hovered Show(screen="info", t=player.gymplan[i].name, i=player.gymplan[i].info+type_info + ctc_info, a=player.gymplan[i].ad)
                        unhovered Hide("info")
                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                        xsize 330
                        activate_sound audio.cursor
            null height 2
        null height 30
        
