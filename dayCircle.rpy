label wakeup:
    $quick_menu = False
    $_game_menu_screen = None
    $renpy.block_rollback()
    scene black with fade
    play music audio.alarm
    $pause(2)
    scene bedroom with dissolve
    $quick_menu = True

    $ Saver.save()
    $Notify.add('存档已保存！')
    $Notify.show()
    jump alarmCircle

label alarmCircle:
    $renpy.block_rollback()
    $pause(2)
    menu:
        "关闭闹钟":
            stop music
            play sound audio.button
            scene bedroom with fade
            show screen screen_dashboard(p)
            pass
        "不理会":
            scene black with fade
            $pause(2)
            jump alarmCircle
    $pause(2)
    jump medicineTake

label medicineTake:
    menu:
        "吃药":
            if p.meds >0:
                $temp = p.mental
                call screen screen_useMed(p)
                if p.mental != temp:
                    "我拿起桌边早就提前盛好水的玻璃杯，将药瓶中的药物吞下。"
                    "……"
                else:
                    jump dontusemed_pro
            elif p.mental>0:
                "已经没有药了吗？"
                "我看着空瓶。"
                if p.today == 5:
                    "今天就可以买更多的了。"
                    "妈的，凭什么我活着就得这么难受。"
                else:
                    "……好吧，马上就到周五了，冷静，冷静，只要少工作多休息就行……"
            else:
                jump ending2
        "不吃药":
            jump dontusemed

    if p.mental < 0:
        "不……不行，头还是很痛……"
        jump medicineTake
    else:
        "也许好点了。"
        jump beforeCircle

label dontusemed:
    if p.mental < 0:
        jump ending1
    else:
        jump beforeCircle

label beforeCircle:
    
    if p.hal_p == 11 and p.today == 6:
        scene livingroom with fade
        '本以为能睡个好觉，妈的，突然被要求加班，什么情况啊那么急，就不能等周一再弄？我真是日了Halifax这个臭傻逼。'
        '这啥卵老板我真服了。'
        '噢……今天好像是Halluke体育考试啊……'
        '给他发个消息告诉他一声吧……'
        $Message.new(p, p.name, 'Halluke','……我一直没胆量和你说明这件事，怕你知道我不是学校学生就对我敬而远之了。\n你说得对，我确实不是大学生，我已经工作1年了，就在H公司。\n总之我想和你说，今天老板突然要求我们加班，可能没法去帮你发球了。\n\n抱歉，祝考试顺利。',seen=True)
        '左手还在刷牙，我用右手快速打字给他发了消息。'
        '……'
        '点击发送，这样应该会好一点吧……'
        '噢！要迟到了……我得赶快出门了……'
        scene morningrun with fade
        $p.onOutside = True
        $p.times = 1
        "……"
        $p.onOutside = False
        $p.onVacation = False
    elif p.today in (1, 2, 3, 4 ,5):
        scene livingroom with fade
        "……"
        "洗漱好了，穿衣服上班了。"
        scene morningrun with fade
        $p.onOutside = True
        $p.times = 1
        "上班……"
        "……"
        $p.onOutside = False
        $p.onVacation = False
    else:
        scene workarea with fade
    jump dayCircle


label dayCircle:
    $ renpy.block_rollback()
    $p.times = 2

    
    if p.onVacation == False:
        scene office with fade
        play music audio.survivingdawn
        "打完卡了，该准备计划一下今天要做的事了。"
    else:
        play music audio.rareleisure
        "难得的假期，该准备计划一下今天要做的事了。"
    $beforemusic=renpy.music.get_playing()
    $p.beforeSchedule()
    show screen screen_dashboard(p)
    jump TaskExecuting
    
label TaskExecuting:

    if p.times == 2:
        $Message.allret(p)
        
        call screen screen_index(p)
        hide screen info
        hide screen info2
        hide screen info3
        if renpy.music.get_playing()!=beforemusic:
            play music beforemusic fadein 5

        $p.times+=1
        jump TaskExecuting
    elif p.times == 3:
        $p.stime()
        if BookRiskEffect.has(p):
            $constemp = p.mental
        $labelname = p.plan[0].__name__ + '_beginning'
        $renpy.jump(labelname)
    elif p.times == 5:
        if renpy.music.get_playing()!=beforemusic:
            play music beforemusic fadein 5
        if BookRiskEffect.has(p) and constemp > p.mental:
            $BookRiskEffect.cons += constemp - p.mental
            $BookRiskEffect.renewInfo()
        if p.onVacation:
            scene workarea with fade
            if rra(p, 60):
                $MentRezB.add(p)
        else:
            scene office with fade
        "上午的工作做完了，差不多该点个外卖吃午饭了。"
        $Message.allret(p)
        call screen screen_index(p)
        hide screen info
        hide screen info2
        hide screen info3
        $p.times+=1
        jump TaskExecuting
    elif p.times == 6:
        "午休结束了……"
        $p.times+=1
        jump TaskExecuting
    elif p.times == 7:
        if BookRiskEffect.has(p):
            $constemp = p.mental
        $labelname = p.plan[1].__name__ + '_beginning'
        $renpy.jump(labelname)
    elif p.times == 9:
        if renpy.music.get_playing()!=beforemusic:
            play music beforemusic fadein 5
        if BookRiskEffect.has(p) and constemp > p.mental:
            $BookRiskEffect.cons += constemp - p.mental
            $BookRiskEffect.renewInfo()
        if p.plan[1] != p.plan[0]:
            $Inspiration.add(p)
        if p.onVacation == True:
            if rra(p, 60):
                $MentRezB.add(p)
            scene workarea with fade
            "有点累了，稍微摸会鱼吧……"
            $p.times+=1
            scene workarea with fade
            "好了，该准备做晚上要做的事了。"
            $Message.allret(p)
            call screen screen_index(p)
            hide screen info
            hide screen info2
            hide screen info3
            $p.times+=1
            jump TaskExecuting
        else:
            scene office with fade
            "准备下班了……"
            $p.times+=1
        jump TaskExecuting
    elif p.times == 10:
        if p.hal_p == 11:
            scene nightrun with fade
            $p.onOutside = True
            "下班途中……"
            $p.times+=1
            scene black with dissolve
            "……"
            play sound unlocking
            $pause(0.5)
            play sound audio.button
            scene livingroom
            $p.onOutside = False
            $p.onVacation = True
            "终于下班了，给Halluke发个消息，看看他怎么样了吧。"
        elif p.onVacation == False:
            scene nightrun with fade
            $p.onOutside = True
            "下班途中……"
            $p.times+=1
            scene black with dissolve
            "……"
            play sound unlocking
            $pause(0.5)
            play sound audio.button
            scene livingroom
            $p.onOutside = False
            $p.onVacation = True
            "终于到家了。"
            "该准备一下晚上要做的事了。"
        else:
            $p.times+=1
            jump TaskExecuting
        $Message.allret(p)
        call screen screen_index(p)
        hide screen info
        hide screen info2
        hide screen info3
        if p.hal_p == 11:
            '我……被Halluke删了好友？'
            '不会吧……为什么？'
            '仅仅是因为我没去和他考试？'
            '可……但……这到底是为什么？'
            '我重新添加为好友，得到的却只有红色的拒绝。'
            '……'
            play music audio.meaninglessemotion
            '某种挫败感交杂着怒火冲上大脑。'
            '所以我做了这么多，结果却是这样的么？'
            '我还没鼓起勇气先说再见，就先被他这种什么也不用担心，什么也不用顾虑的家伙删了？'
            '现在还有时间，我必须去找他问个清楚。'
            jump halluke_route_10
        jump TaskExecuting
    elif p.times == 11:
        if BookRiskEffect.has(p):
            $constemp = p.mental
        $labelname = p.plan[2].__name__ + '_beginning'
        $renpy.jump(labelname)
    elif p.times == 13:
        if renpy.music.get_playing()!=beforemusic:
            play music beforemusic fadein 5
        if BookRiskEffect.has(p) and constemp > p.mental:
            $BookRiskEffect.cons += constemp - p.mental
            $BookRiskEffect.renewInfo()
        if p.plan[2] != p.plan[1]:
            $Inspiration.add(p)
        if p.today in (6, 7):
            if rra(p, 60):
                $MentRezB.add(p)
        scene livingroom with fade
        "一天又快结束了，睡觉之前做些什么呢？"
        $Message.allret(p)
        call screen screen_index(p)
        hide screen info
        hide screen info2
        hide screen info3
        $p.times+=1
        jump TaskExecuting
    elif p.times == 14:
        scene bedroom with fade
        jump dayEnd
    else:
        "游戏时间发生错误！"
        jump to_the_title

label dayEnd:
    "该睡觉了。"
    $p.newDay()
    call loading from _call_loading_1
    jump wakeup




































screen screen_useMed(player):
    #tag gamegui
    use barrier(screen="screen_useMed", mode=0)

    $ items = list(filter(lambda x: type(x).kind=='实验药物' and not x.broken, player.items))

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
                    textbutton '{size=+10}使用药物{/size}':
                        text_style "gameUI"
                        xoffset -5
                        yoffset -5
                        action NullAction()

                    imagebutton auto "gui/icons/task_icon/exit_%s.png":
                        xalign 1.0
                        action Show(screen="screen_useMed_confirm",player=player)

                    frame:
                        background None
                        ysize 640
                        xsize 700
                        ypos 60
                        xpos 15

                        viewport:
                            mousewheel True
                            draggable True
                            use screen_useMed_show(player, items)
                    

screen screen_useMed_show(player, items):
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
                xalign 1.0
                activate_sound audio.cursor
                #background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)

        vbox:
            #xalign 1.0
            for ite in items:
                frame:
                    background None
                    ysize 60
                    xfill True
                    $ite_name = type(ite).name
                    $ite_pre = ite.getPrefixInfo()
                    $ite_main = ite.getPrincipalInfo() + type(ite).getBenefit(player)
                    $ite_suf = ite.getSuffixInfo()

                    frame:
                        background None
                        textbutton ite_name text_style "white":
                            action [Hide("info3"),Show(screen="screen_useMed_use", player=player, book=ite, pp=renpy.get_mouse_pos(), t=ite_name, i1=ite_pre, i2='\n'+ite_main+ite_suf, a2=type(ite).ad)]
                            hovered [Show(screen="info3", t=ite_name, i1=ite_pre, i2='\n'+ite_main+ite_suf, a2=type(ite).ad)]
                            unhovered Hide("info3")
                            background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            activate_sound audio.cursor
                            xfill True

                    null height 2
        null height 30
        textbutton ''

screen screen_useMed_use(player, book, pp, t=None, i1=None, a1=None, i2=None, a2=None, width=600):
    style_prefix "info"
    use barrier(screen="screen_useMed_use")
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
                textbutton _("{size=-3}使用{/size}"):
                    action [Hide("screen_useMed_use"), Function(ui_itemUse, item=book, player=player),Return(None)]
                    activate_sound audio.cursor
                textbutton _("{size=-3}取消{/size}"):
                    action Hide("screen_useMed_use")
                    activate_sound audio.cursor


screen screen_useMed_confirm(player, i="不吃药吗？如果精神状态过低将导致游戏结束。", width=400, pp=renpy.get_mouse_pos()):
    use barrier(screen="screen_useMed_confirm")
    style_prefix "info"
    zorder 400
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
                label _(i):
                    text_style "info_text"
                    xsize width
            null height 30
            hbox:
                xalign 0.5
                spacing 40
                textbutton _("{size=-3}确定{/size}"):
                    action [Hide("screen_useMed_confirm"), Return(None)]
                    activate_sound audio.cursor
                textbutton _("{size=-3}返回{/size}"):
                    action Hide("screen_useMed_confirm")
                    activate_sound audio.cursor


