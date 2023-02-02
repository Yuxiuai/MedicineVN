##########################################################
##                起床和吃药
##
##########################################################

label wakeup:
    stop music
    $ quick_menu = False
    $ _game_menu_screen = None
    $ renpy.block_rollback()
    $ blackmask(p)
    scene black
    if not persistent.nomedicine:
        play music audio.alarm
        if not persistent.quickAlarm:
            $ pause(2)
        scene bedroom at setcolor with dissolve
        $renpy.show('blurred', at_list=[blurr_concentration(p)])
    $ quick_menu = True
    $ _game_menu_screen = "save"
    jump alarmCircle

label alarmCircle:
    if Novice.has(p):
        $Novice.get(p).afterSleepAction(p)
    $ renpy.block_rollback()
    if persistent.nomedicine:
        stop music
        show screen screen_dashboard(p)
        jump before_go_out
    if not persistent.quickAlarm:
        $ pause(2)
    menu:
        "关闭闹钟" if True:
            stop music
            play sound audio.button
            scene bedroom at setcolor with fade
            $renpy.show('blurred', at_list=[blurr_concentration(p)])
            show screen screen_dashboard(p)
            pass
        "不理会" if True:
            scene black with fade
            $ pause(2)
            jump alarmCircle
    $ pause(2)
    jump medicineTake

label medicineTake:
    menu:
        "吃药":
            if p.meds() >0:
                $ temp = p.mental
                scene cupboard at setcolor with dissolve
                call screen screen_useMed(p)
                scene bedroom at setcolor with dissolve
                if p.mental != temp:
                    if p.cured<21:
                        "我拿起桌边早就提前盛好水的玻璃杯，将药瓶中的药物吞下。"
                        "……"
                elif True:
                    jump dontusemed_pro
            elif p.mental>0:
                if p.cured<21:
                    "已经没有药了吗？"
                    "我看着空瓶。"
                if p.today == 5:
                    if p.cured<21:
                        "今天就可以买更多的了。"
                        "妈的，凭什么我活着就得这么难受。"
                elif True:
                    if p.cured<21:
                        "……好吧，马上就到周五了，冷静，冷静，只要少工作多休息就行……"
            else:
                if p.cured>=21:
                    jump CuredBE
                jump ending2
        "不吃药":
            jump dontusemed

    if p.mental < 0:
        if p.cured<21:
            "不……不行，头还是很痛……"
        jump medicineTake
    elif True:
        if p.cured<21:
            "也许好点了。"
        jump before_go_out

label dontusemed:
    if p.mental < 0:
        if p.cured>=21:
            jump CuredBE
        jump ending1
    elif True:
        jump before_go_out

##########################################################
##                日常
##
##########################################################

label before_go_out:
    if p.cured >= 21:
        $ renpy.say(None, countdown(p))

    if p.cured >= 84:
        jump curedRoutine

    if p.hal_p == 11 and p.today == 6 and p.cured < 0 and not SteamerTicket.has(p):
        jump work_overtime_h

    if p.today == 1 and p.week == 2:
        call solitus_route_3 from _call_solitus_route_3
    else:
        scene bathroom at setcolor with fade
        $routine_narrator(p, _("洗漱……"))

    if p.today in (1, 2, 3, 4 , 5) and WeatherTornado.has(p) and not SteamerTicket.has(p):
        jump tornado_event

    if SteamerTicket.has(p) and p.today == 6:
        jump prepare_for_surgery_1_1
    
    elif p.week == 15 and p.today == 6 and p.cured == -1 and not persistent.nocharacterplot:
        jump prepare_for_surgery_2_1

    if p.today in (1, 2, 3, 4 ,5):
        scene livingroom at setcolor with fade
        $renpy.show('blurred', at_list=[blurr_concentration(p)])

        if p.mental < 40:
            $ routine_narrator(p, _("凭什么我要一直坚持到现在啊……好想死啊……"))
        elif p.mental > 100:
            $routine_narrator(p, _("早上吃点什么呢……还是到了公司再点外卖吧……"))
        else:
            $routine_narrator(p, _("准备上班了。"))

        scene morningrun at setcolor with fade
        $ renpy.show('blurred', at_list=[blurr_concentration(p)])

        $ p.onOutside = True
        $ p.times = 1

        if p.mental < 40:
            $ routine_narrator(p, _("只觉得浑身都很疲惫，这样的我肯定撑不到下班吧。"))
        elif p.mental > 100:
            $routine_narrator(p, _("这个时间……应该不会迟到吧……"))
        else:
            $ routine_narrator(p, _("上班途中……"))

        $ p.onOutside = False
        $ p.onVacation = False

        $ p.times = 2
    
        
        $ beforemusic=renpy.music.get_playing()

        jump before_operate_screen_label

    else:

        $ p.times = 2

        $ beforemusic=renpy.music.get_playing()

        jump before_operate_screen_label

label before_operate_screen_label:  ## 回到这里
    $ routine_bg(p)
    $ routine_music(p)
    if p.times == 2:
        if p.onVacation:
            if p.mental < 40:
                $ routine_narrator(p, _("……今天还是在床上一直躺着好了……"))
            elif p.mental > 100:
                $routine_narrator(p, _("我听到了鸟叫声……今天有点想出去散散步呢。"))
            else:
                $routine_narrator(p, _("难得的假期，该准备计划一下今天要做的事了。"))
            $ p.beforeSchedule()
            
        else:
            if p.mental < 40:
                $ routine_narrator(p, _("头好疼啊，我今天能撑到下班吗……"))
            elif p.mental > 100:
                $routine_narrator(p, _("一天的工作开始了，调整好自己的状态吧。"))
            else:
                $routine_narrator(p, _("打完卡了，该准备计划一下今天要做的事了。"))
            $ p.beforeSchedule()
            jump morning_plot_label_office
        
    elif p.times == 5:
        if p.onVacation:
            if p.mental < 40:
                $ routine_narrator(p, _("困死了，就算放假也有种休息不够的感觉……"))
            elif p.mental > 100:
                $routine_narrator(p, _("有点饿了，中午想吃点甜的呢……"))
            else:
                $routine_narrator(p, _("午饭时间……今天吃点什么好呢……"))
        else:
            if p.mental < 40:
                $ routine_narrator(p, _("头晕……想吐……根本没什么胃口吃饭……"))
            elif p.mental > 100:
                $routine_narrator(p, _("上午的工作好像也没有很多……总之吃午饭吧。"))
            else:
                $routine_narrator(p, _("上午的工作做完了，差不多该点个外卖吃午饭了。"))

    elif p.times == 6:
        if p.onVacation:
            if p.mental < 40:
                $ routine_narrator(p, _("小睡一会……"))
            elif p.mental > 100:
                $routine_narrator(p, _("晚点应该出门逛逛……先准备一下吧……"))
            else:
                $routine_narrator(p, _("稍微刷一会手机再做下午的事情吧……"))
        else:
            if p.mental < 40:
                $ routine_narrator(p, _("希望下午没有什么破事，头已经快炸了……"))
            elif p.mental > 100:
                $routine_narrator(p, _("还有几个小时就下班了，至少现在还没有感觉很吃力……"))
            else:
                $routine_narrator(p, _("午休结束了……"))
        $p.times += 1
        jump after_operate_screen_label
    elif p.times == 9:
        if p.onOutside:
            $routine_narrator(p, _("……"))
            $ p.times+=1
            jump before_operate_screen_label

        elif p.onVacation:
            if p.mental < 40:
                $ routine_narrator(p, _("看来放假也没法让我的头疼轻一些……"))
            elif p.mental > 100:
                $routine_narrator(p, _("放假的时间总是很短暂……"))
            else:
                $routine_narrator(p, _("稍微有点累了……摸一会鱼吧……"))

            $ p.times+=1
            $ routine_bg(p)
            $ routine_narrator(p, _("晚点做些什么好呢……"))
            
        else:
            if p.mental < 40:
                $ routine_narrator(p, _("终于结束了……希望我不会死在回家的路上……"))
            elif p.mental > 100:
                $routine_narrator(p, _("下班下班，回家爽摸鱼咯——"))
            else:
                $routine_narrator(p, _("准备下班了……"))
            $ p.times+=1
            $ p.onOutside = True
            jump before_operate_screen_label

            

    elif p.times == 10:
        if p.onVacation and not p.onOutside:
            if p.mental < 40:
                $ routine_narrator(p, _("我现在只想躺在床上……"))
            elif p.mental > 100:
                $routine_narrator(p, _("或许我应该出门走一走？或者看点什么小说之类的？"))
            else:
                $routine_narrator(p, _("好了，该准备做晚上要做的事了。"))
        else:


            if p.mental < 40:
                $ routine_narrator(p, _("再坚持一会……马上就到家了……"))
            elif p.mental > 100:
                $ routine_narrator(p, _("啊……终于快到家了……"))
            else:
                $ routine_narrator(p, _("……"))

            
            scene black with dissolve
            $ routine_narrator(p, _("……"))

            play sound unlocking
            $ pause(0.5)
            play sound audio.button

            $ p.onOutside = False
            $ p.onVacation = True

            $ routine_bg(p)
            $ routine_music(p)

            if p.mental < 40:
                $ routine_narrator(p, _("嘶啊……头快疼死了……"))
            elif p.mental > 100:
                $ routine_narrator(p, _("回到家里总是让我心情很好……"))
            else:
                $ routine_narrator(p, _("到家了。"))
            $ routine_narrator(p, _("……总之该准备做晚上要做的事了。"))

            if p.hal_p == 11 and p.today == 6 and p.cured < 0:
                $ routine_narrator(p, _("给Halluke发个消息，看看他怎么样了吧。"))


    elif p.times >= 13:
        if p.mental < 40:
            $ routine_narrator(p, _("床……头疼药……安眠药……我真的能够活过今晚吗……"))
        elif p.mental > 100:
            $ routine_narrator(p, _("像现在这样头不是很痛就很好……如果我的病被治好了，我会不会更开心呢？"))
        else:
            $routine_narrator(p, _("一天又快结束了，睡觉之前做些什么呢？"))



    jump operate_screen_label


label morning_plot_label_office:
    if p.today == 1 and p.cured == -1 and not SteamerTicket.has(p):
        if p.hal_p == 13:
            jump give_ticket_h
        elif p.aco_p == 12:
            jump give_ticket_a
    else:    
        jump operate_screen_label

label operate_screen_label:
    
    $ Message.allret(p)
    $ p.checkTask()
    if not persistent.keepskippingafteroperate:
        $ renpy.config.skipping = False
    show screen screen_objects(p)
    call screen screen_operate(p)
    hide screen info
    hide screen info2
    hide screen info3

    if p.times in (3, 7, 11, 14):
        jump after_operate_screen_label
    else:
        jump before_operate_screen_label

label after_operate_screen_label:
    if p.hal_p == 11 and p.today == 6 and p.times == 11 and p.cured < 0:
        "我……被Halluke删了好友？"
        "不会吧……为什么？"
        "仅仅是因为我没去和他考试？"
        "可……但……这到底是为什么？"
        "我重新添加为好友，得到的却只有红色的拒绝。"
        "……"
        "某种挫败感交杂着怒火冲上大脑。"
        "所以我做了这么多，结果却是这样的么？"
        "我还没鼓起勇气先说再见，就先被他这种什么也不用担心，什么也不用顾虑的家伙删了？"
        "现在还有时间，我必须去找他问个清楚。"
        $p.onOutside = True
        jump halluke_route_11

    jump executing_task_label


label executing_task_label:
    #$ routine_bg(p)
    $ p.stime()
    if BookRiskEffect.has(p):
        $ constemp = p.mental
    
    if p.times == 14:
        jump before_sleep
    $donextplan(p)

label after_executing_task_label:
    if p.cured<0:
        if BookRiskEffect.has(p) and constemp > p.mental:
            $ BookRiskEffect.cons += constemp - p.mental
            $ BookRiskEffect.renewInfo()

        $tt = p.get_task_time()
        if tt == 2:
            if p.plan[0] != p.plan[1]:
                $ Inspiration.add(p)

        elif tt == -1:
            if p.plan[1] != p.plan[2] and p.plan[2] != WriteDownInspiration:
                $ Inspiration.add(p)

        if p.onVacation:
            if rra(p, 60):
                $ MentRezB.add(p)
    
    jump before_operate_screen_label




label before_sleep:  # 触发部分剧情
    if p.cured < 0 and SteamerTicket.has(p) and p.today == 1 and not persistent.nocharacterplot:
        jump prepare_for_surgery_1

    elif p.cured < 0 and p.week == 15 and p.today == 1 and not persistent.nocharacterplot:
        jump prepare_for_surgery_2

    elif p.cured == 6:
        jump curedroute_phone_1

    elif p.cured == 13:
        jump curedroute_phone_2

    elif p.cured == 20:
        jump curedroute_phone_3

    elif p.cured == 27:
        jump curedroute_phone_4

    else:
        jump before_dayend




label before_dayend:
    scene bedroom at setcolor with fade
    stop music fadeout 5
    $renpy.show('blurred', at_list=[blurr_concentration(p)])
    if p.cured<21:
        if not p.s8 and p.week >= 2 and p.cured==-1 and p.finalStageDays==-1:
            $temp = True
            python:
                for i in p.itemcd:
                    if i.kind == '食物':
                        temp = False
            if temp:
                jump solitus_route_8
            else:
                "该睡觉了。"
        else:
            "该睡觉了。"
        
    elif True:
        "……"
    jump dayEnd


label dayEnd:
    if p.cured == 21:
        $ p.severity = 0.5
        $ LifeIsColorless.add(p)
    if p.cured == 42:
        $ p.severity = 0.3
    if p.cured == 63:
        $ p.severity = 0.2
    if p.cured == 84:
        $ p.severity = 0.1
    $ p.newDay()
    $ Save.save(p)
    $ Notice.add(_('存档已保存！'))
    call loading from _call_loading_1
    $ Notice.show()
    if p.hal_p == 15 or p.aco_p == 14 and p.cured < 0:
        jump before_earthquake
    jump wakeup

label sandglass_label:
    $ Save.save(p)
    $ Notice.add(_('存档已保存！'))
    
    call loading from _call_loading_11
    $ Notice.show()
    if p.hal_p == 15 or p.aco_p == 14 and p.cured < 0:
        jump before_earthquake
    jump wakeup


screen screen_useMed(player):

    if MedicineA.has(player):
        imagebutton idle 'gui/object/mshadow.png':
            at med_bottle_shadow

            xcenter 0.22
            ycenter 0.55
            focus_mask None
        
        imagebutton idle 'gui/object/ma.png':
            at med_bottle

            action [Show(screen="info_confirm",text=_('使用'),act=[Function(quickUse, item=MedicineA, player=player), Hide("info"), Return()],i=MedicineA.getinfo(player) + '\n点击使用。',width=600, a=MedicineA.ad, pp=renpy.get_mouse_pos()), Hide("info")]
            hovered Show(screen="info",i=MedicineA.getinfo(player) + '\n点击使用。',width=600, a=MedicineA.ad)
            unhovered Hide("info")
            #text_style "meda_text"
            #xalign 1.0
            hover_sound audio.itemmed
            activate_sound audio.itemmed
            xcenter 0.22
            ycenter 0.55
            focus_mask None
    
    if MedicineB.has(player):
        imagebutton idle 'gui/object/mshadow.png':
            at med_bottle_shadow

            xcenter 0.28
            ycenter 0.55
            focus_mask None

        imagebutton idle 'gui/object/mb.png':
            at med_bottle
            
            action [Show(screen="info_confirm",text=_('使用'),act=[Function(quickUse, item=MedicineB, player=player), Hide("info"), Return()],i=MedicineB.getinfo(player) + '\n点击使用。',width=600, a=MedicineB.ad, pp=renpy.get_mouse_pos()), Hide("info")]
            hovered Show(screen="info",i=MedicineB.getinfo(player) + '\n点击使用。',width=600, a=MedicineB.ad)
            unhovered Hide("info")
            #text_style "meda_text"
            #xalign 1.0
            hover_sound audio.itemmed
            activate_sound audio.itemmed
            xcenter 0.28
            ycenter 0.55
            focus_mask None

    if MedicineC.has(player):

        imagebutton idle 'gui/object/mshadow.png':
            at med_bottle_shadow

            xcenter 0.34
            ycenter 0.55
            focus_mask None

        imagebutton idle 'gui/object/mc.png':
            at med_bottle

            action [Show(screen="info_confirm",text=_('使用'),act=[Function(quickUse, item=MedicineC, player=player), Hide("info"), Return()],i=MedicineC.getinfo(player) + '\n点击使用。',width=600, a=MedicineC.ad, pp=renpy.get_mouse_pos()), Hide("info")]
            hovered Show(screen="info",i=MedicineC.getinfo(player) + '\n点击使用。',width=600, a=MedicineC.ad)
            unhovered Hide("info")
            #text_style "meda_text"
            #xalign 1.0
            hover_sound audio.itemmed
            activate_sound audio.itemmed
            xcenter 0.34
            ycenter 0.55
            focus_mask None
    
    if MedicineD.has(player):
        
        imagebutton idle 'gui/object/mshadow.png':
            at med_bottle_shadow

            xcenter 0.7
            ycenter 0.55
            focus_mask None

        imagebutton idle 'gui/object/md.png':
            at med_bottle
            
            action [Show(screen="info_confirm",text=_('使用'),act=[Function(quickUse, item=MedicineD, player=player), Hide("info"), Return()],i=MedicineD.getinfo(player) + '\n点击使用。',width=401, a=MedicineD.ad, pp=renpy.get_mouse_pos()), Hide("info")]
            hovered Show(screen="info",i=MedicineD.getinfo(player) + '\n点击使用。',width=401, a=MedicineD.ad)
            unhovered Hide("info")
            #text_style "meda_text"
            #xalign 1.0
            hover_sound audio.itemmed
            activate_sound audio.itemmed
            xcenter 0.7
            ycenter 0.55
            focus_mask None
    
    
    imagebutton auto "gui/menu/home_%s.png":
        at trans_toLeft()
        action Hide("info"), Return()
        unhovered Hide("info")
        hovered Show(screen="info", i=_('不吃药。'), a=_('……'), width=100)
        activate_sound audio.cursor
        xpos 0.9
        ypos 0.85



label curedRoutine:
    show screen screen_dashboard(p)
    $ p.times = curedsettime(p.times)
    if p.cured >= 105:
        jump CE
    if p.times == 3:
        $ p.beforeSchedule()

        $ p.physical = p.physical - p.physical*0.05
        $ p.writing = p.writing - p.writing*0.05
        $ p.popularity = max(1000, p.writing - p.popularity*0.05)
        
        $ gt = CuredTask.gt()
        menu:
            "工作" if p.today in (1, 2, 3, 4, 5) and p.cured < 98:
                $ Stat.record(p,CuredWork)
                jump CuredWork_beginning
            "休息" if p.today in (6, 7) and p.cured < 98:
                $ Stat.record(p,CuredRest)
                jump CuredRest_beginning
            "[gt]" if p.today in (1, 2, 3, 4, 5) and p.cured >= 98:
                $ Stat.record(p,CuredWork)
                jump CuredWork_beginning
            "[gt]" if p.today in (6, 7) and p.cured >= 98:
                $ Stat.record(p,CuredRest)
                jump CuredRest_beginning
            "放弃" if p.cured >= 91:
                jump CuredBE

    if p.times == 7:
        $ gt = CuredTask.gt()
        menu:
            "工作" if p.today in (1, 2, 3, 4, 5) and p.cured < 98:
                $ Stat.record(p,CuredWork)
                jump CuredWork_beginning
            "休息" if p.today in (6, 7) and p.cured < 98:
                $ Stat.record(p,CuredRest)
                jump CuredRest_beginning
            "[gt]" if p.today in (1, 2, 3, 4, 5) and p.cured >= 98:
                $ Stat.record(p,CuredWork)
                jump CuredWork_beginning
            "[gt]" if p.today in (6, 7) and p.cured >= 98:
                $ Stat.record(p,CuredRest)
                jump CuredRest_beginning
            "放弃" if p.cured >= 91:
                jump CuredBE

    if p.times == 11:
        $ gt = CuredTask.gt()
        menu:
            "休息" if p.today in (1, 2, 3, 4, 6, 7) and p.cured < 98:
                $ Stat.record(p,CuredRest)
                jump CuredRest_beginning
            "买药" if p.today == 5 and p.cured < 98:
                $ Stat.record(p,CuredHosp)
                jump CuredHosp_beginning
            "[gt]" if p.today in (1, 2, 3, 4, 6, 7) and p.cured >= 98:
                $ Stat.record(p,CuredRest)
                jump CuredRest_beginning
            "[gt]" if p.today == 5 and p.cured >= 98:
                $ Stat.record(p,CuredHosp)
                jump CuredHosp_beginning
            "放弃" if p.cured >= 91:
                jump CuredBE
    jump dayEnd