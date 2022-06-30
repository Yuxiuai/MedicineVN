screen screen_dashboard(player):
    #tag gamegui
    use screen_dashboard_calendar(player)
    use screen_dashboard_medicine(player)
    use screen_dashboard_severity(player)
    use screen_dashboard_abilities(player)
    use screen_dashboard_effects(player)

screen screen_dashboard_calendar(player):
    style_prefix "gameUI"
    zorder 100
    $ weekday = weekdayFormat(player.today)
    $ cons = player.aggravationConsumption()
    $ info = '\n消耗倍率：' + num_str(player.deteriorateConsumption, rev = True)
    $ info2 = '\n过夜预计消耗的精神状态约为：' + str(cons)
    $ ad = '时间正在一刻不停地流逝，无可避免的死亡正在前方等待，而悔恨和不甘正在堆积。'
    if Despair.has(player):
        $ ad = "即将抵达的死亡。"

    vbox:
        xpos 0.02
        ypos 0.02
        $showHour=player.st()[0]
        $showMin=player.st()[1]
        $weather=type(player.effects[0])
        $wea_name = weather.name
        if persistent.PreciseDisplay:
            $wea_info = weather.info_p
        else:
            $wea_info = weather.info
        $wea_ad = weather.ad
        if player.onOutside:
            $ poz = '在外面'
        elif player.onVacation:
            $ poz = '在家中'
        else:
            $ poz = '在公司'
        $wea_t = '本日天气为：' + wea_name +'\n预计明日天气为：' + player.newMorningWeather(True).name
        if Despair.has(player):
            textbutton _("废墟下的第[player.finalStageDays]天")xalign 0.0:
                at trans_Down(0.2)
                #action Function(allE, player=player)
                action [Hide("info3"),Show(screen="info3_use", pp=renpy.get_mouse_pos(), t=wea_t, i1=wea_info, a1=wea_ad, i2=info2+info, a2=ad)]
                hovered Show(screen="info3",t=wea_t, i1=wea_info, a1=wea_ad, i2=info2+info, a2=ad)
                unhovered Hide("info3")
                text_style "gameUI"
                hover_sound audio.cursor
        else:
            textbutton _("[player.mon]月[player.day]日  第[player.week]周  [wea_name]\n[weekday]  [showHour]:[showMin]  [poz]")xalign 0.0:
                at trans_Down(0.2)
                #action Function(allE, player=player)
                action [Hide("info3"),Show(screen="info3_use", pp=renpy.get_mouse_pos(), t=wea_t, i1=wea_info, a1=wea_ad, i2=info2+info, a2=ad)]
                hovered Show(screen="info3",t=wea_t, i1=wea_info, a1=wea_ad, i2=info2+info, a2=ad)
                unhovered Hide("info3")
                text_style "gameUI"
                hover_sound audio.cursor


screen screen_dashboard_medicine(player):
    style_prefix "gameUI"
    zorder 100
    $ hasMed = False
    $ tim = 0.2
    $ drugReco = int(player.basicRecovery * player.drugRecovery * 100)
    $ quickuse_info = '\n点击可快捷使用。'
    vbox:
        xalign 0.98
        yalign 0.02
        
        if MedicineA.hasByType(player):
            $tim += 0.05
            $ hasMed = True
            $ info1 = '预计恢复'+str(MedicineA.expectedReco(player))+'点精神状态。'+MedicineA.getResInfo(player)+ quickuse_info
            $ ad1 = MedicineA.ad
            textbutton str(MedicineA.getByType(player).amounts) + _("    药物{font=arial.ttf}α{/font}"):
                at med_menu(tim)
                action [Show(screen="med_use",player=player,med=MedicineA, i=info1,a=ad1, pp=renpy.get_mouse_pos()), Hide("info")]
                hovered Show(screen="info",i=info1,a=ad1)
                unhovered Hide("info")
                text_style "meda_text"
                xalign 1.0
                hover_sound audio.cursor

        if MedicineB.hasByType(player):
            $tim += 0.05
            $ hasMed = True
            $ info2 = '预计恢复'+str(MedicineB.expectedReco(player))+'点精神状态。'+MedicineB.getResInfo(player)+ quickuse_info
            $ ad2 = MedicineB.ad
            textbutton str(MedicineB.getByType(player).amounts) + _("    药物{font=arial.ttf}β{/font}"):
                at med_menu(tim)
                action [Show(screen="med_use",player=player,med=MedicineB, i=info2,a=ad2, pp=renpy.get_mouse_pos()), Hide("info")]
                hovered Show(screen="info",i=info2,a=ad2)
                unhovered Hide("info")
                text_style "medb_text"
                xalign 1.0
                hover_sound audio.cursor

        if MedicineC.hasByType(player):
            $tim += 0.05
            $ hasMed = True
            $ info3 = '预计总共恢复'+str(MedicineC.expectedReco(player))+'点精神状态。' +MedicineC.getResInfo(player)+ quickuse_info
            $ ad3 = MedicineC.ad
            textbutton str(MedicineC.getByType(player).amounts) + _("    药物{font=arial.ttf}γ{/font}"):
                at med_menu(tim)
                action [Show(screen="med_use",player=player,med=MedicineC, i=info3,a=ad3, pp=renpy.get_mouse_pos()), Hide("info")]
                hovered Show(screen="info",i=info3,a=ad3)
                unhovered Hide("info")
                text_style "medc_text"
                xalign 1.0
                hover_sound audio.cursor

        if MedicineD.hasByType(player):
            $ hasMed = True
            $tim += 0.05
            $ info4 = '预计恢复'+glitchtext(5)+'点精神状态。' + MedicineD.getResInfo(player)+ quickuse_info
            $ ad4 = MedicineD.ad
            textbutton str(MedicineD.getByType(player).amounts) + _("    药物{font=arial.ttf}δ{/font}"):
                at med_menu(tim)
                action [Show(screen="med_use",player=player,med=MedicineD, i=info4,a=ad4, pp=renpy.get_mouse_pos()), Hide("info")]
                hovered Show(screen="info",i=info4,a=ad4)
                unhovered Hide("info")
                text_style "medd_text"
                xalign 1.0
                hover_sound audio.cursor

        if not hasMed:
            textbutton _("你已经没有药了。"):
                at trans_toLeft(tim)
                action NullAction()
                text_style "gameUI"
                xalign 1.0


screen med_use(med,player, i=None, a=None, width=400, pp=renpy.get_mouse_pos()):
    use barrier(screen="med_use")
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
            if a is not None:
                $a = '{i}' + a
                null height 16
                label _(a):
                    text_style "admonition_text"
                    xsize width
            null height 30
            hbox:
                xalign 0.5
                spacing 40
                textbutton _("{size=-3}使用{/size}"):
                    action [Function(quickUse, item=med, player=player), Hide("info"), Hide("med_use")]
                    activate_sound audio.cursor
                textbutton _("{size=-3}返回{/size}"):
                    action Hide("med_use")
                    activate_sound audio.cursor


screen screen_dashboard_severity(player):
    style_prefix "gameUI"
    $ info0 = '衡量当前对疼痛忍耐度的重要指标。\n\n劳累或精神紧张时会消耗，反之做一些放松的事时则会恢复。\n当早晨起床时所有实验药物都被消耗，且精神状态低于0时，游戏结束。'
    $ info1 = '\n\n基础精神状态消耗倍率：' + num_str(Task.getConsScale(player),rev=True)
    $ info2 = '\n基础精神状态恢复倍率：' + num_str(Task.getRecoScale(player))
    $ ad = '你天生罹患的偏头痛似乎没有办法治愈，药效随着时间流逝正在减弱。\n如果你没有在疼痛突破防线之前咽下药物，那么也许你便再也没有机会见到第二天的太阳了。'
    zorder 100
    vbox:
        xcenter 0.5
        ypos 0.02
        textbutton _("精神状态\n") + str(player.mental):
            at trans_Down(0.2)
            action [Hide("info"),Show(screen="info_use", pp=renpy.get_mouse_pos(), i=info0 + info1 + info2, a=ad)]
            hovered Show(screen="info", i=info0 + info1 + info2, a=ad)
            unhovered Hide("info")
            text_style "gameUIM"
            hover_sound audio.cursor

default prog_mode = 1

screen screen_dashboard_abilities(player):
    style_prefix "gameUI"
    $showtime = 0.2
    zorder 100
    vbox:
        xpos 0.02
        ypos 0.13

        vbox:
            label _("基础") text_style "gameL":
                at trans_toRight(0.2)
            $ info = '今日种子：' + str(player.seed)# + '\n当前Safe指数：' + str(player.safe)
            $ info1 = '\n\n专注度可以使日程的获得更好的结果以获得更多的能力提升。\n\n基础专注度修正：' + num_str(Task.getConcScale(player), '++')
            $ info2 = '\n\n每使用一次食物或药物都会减少对应的恢复效率。\n\n食物恢复效率：' + num_str(player.useFoodScale())
            $ info3 = '\n药物恢复效率：' + num_str(player.useDrugScale())
            if player.name == 'Solitus':
                $ad = '我的名字，非常适合我。'
            else:
                $ad = '别人称呼我的方式，即便我并不喜欢这个名字。'
            textbutton player.name:
                at trans_toRight(showtime)
                action [Hide("info"),Show(screen="info_use", pp=renpy.get_mouse_pos(), i=info+info1+info2+info3, a=ad)]
                hovered Show(screen="info", i=info+info1+info2+info3, a=ad)
                unhovered Hide("info")
                text_style "gameUI"
                hover_sound audio.cursor

        vbox:
            $showtime += 0.05
            label _("情况") text_style "gameL":
                at trans_toRight(showtime)
            $meds = player.meds()
            if player.money < 300:
                $ info_money = '我没有钱了，我只能努力工作然后祈祷自己会不在这个期间被公司开除。'
            elif player.money > 1000 and meds > 0:
                $ info_money = '我已经买过这周要吃的药了，这些空闲的钱应该能让我美美过上一周。'
            elif player.money < 1500 and meds == 0:
                $ info_money = '这些钱……足够我买药吗？'
            elif player.money < 3000 and meds == 0:
                $ info_money = '呼，我喜欢发工资的感觉，但这些钱马上就会被购买药物的开销消耗殆尽。'
            elif player.money > player.price * 8:
                $ info_money = '也许这次我可以不用把所有的钱拿来买药。'
            else:
                $ info_money = '这些钱能买些什么呢……'
            $showtime += 0.05
            textbutton _("所持金钱 ") + str(player.money):
                at trans_toRight(showtime)
                action [Hide("info"),Show(screen="info_use", pp=renpy.get_mouse_pos(), i='购买药物和其他能够保障生存的东西。', a=info_money)]
                hovered Show(screen="info",i='购买药物和其他能够保障生存的东西。', a=info_money)
                unhovered Hide("info")
                text_style "gameUI"
                hover_sound audio.cursor
            $showtime += 0.05
            textbutton _("药物价格 ") + str(player.price):
                at trans_toRight(showtime)
                action [Hide("info"),Show(screen="info_use", pp=renpy.get_mouse_pos(), i='下周药价涨价幅度：' + str(player.priceIncrease) + '%', a='努力赚钱，要么就被疯涨的药价压倒。')]
                hovered Show(screen="info", i='下周药价涨价幅度：' + str(player.priceIncrease) + '%', a='努力赚钱，要么就被疯涨的药价压倒。')
                unhovered Hide("info")
                text_style "gameUI"
                hover_sound audio.cursor
            $showtime += 0.05
            $paid_info, wages_info = player.calWorkPaid()
            $paid_info = '\n\n预计获得收入：' + str(paid_info)
            $wages_info = '\n预计下周工资：' + str(wages_info)
            $w_info = '每周在发过工资后都会根据工作能力和上周的工作完成度加薪。' + paid_info + wages_info
            $w_a = '偶尔我也想着，如果我再也不需要买药的话，那这些钱够我吃多少好吃的，玩多少好玩的呢？'
            textbutton _("本周工资 ") + str(player.wages):
                at trans_toRight(showtime)
                action [Hide("info"),Show(screen="info_use", pp=renpy.get_mouse_pos(), i=w_info, a=w_a)]
                hovered Show(screen="info",i=w_info,a=w_a)
                unhovered Hide("info")
                text_style "gameUI"
                hover_sound audio.cursor
            
            #textbutton _("工作目标 ") + str(player.goal):
            #    action NullAction()
            #    hovered Show(screen="info", i='工作速度加成：' + str(int((player.workSpeed-1) * 100)) + '%', a='就算我再努力工作，估计也是在这个小破职位，永远也不会升职。')
            #    unhovered Hide("info")
            #    text_style "gameUI"  # 判定升职后修改
            
            $per = player.achievedGoal/player.goal
            if per == 0:
                $ info_acg = '又是新的一周，看看这周我要被分配哪些工作……'
            elif per < 0.3 and player.today < 3:
                $ info_acg = '这周才刚开始我就累了。'
            elif per < 0.4 and player.today < 5:
                $ info_acg = '完了，这绝对做不完了……'
            elif per < 0.9 and player.today < 5:
                $ info_acg = '糟糕……我是不是摸鱼摸太多了……不会做不完工作吧……'
            elif per >= 1 and player.today < 5:
                $ info_acg = '这周也是勉强糊弄过去了，总之发工资前都可以狂摸鱼啦！'
            else:
                $ info_acg = '偶尔回头看看自己做的工作，也很有成就感就是了……'
            $showtime += 0.05
            $info_goal = '工作速度加成：' + str(int((player.workSpeed-1) * 100)) + '%\n\n如果在周五之前没有达到100%以上，只会获得一半的每周工资。'
            $showgoal = "工作进度 " + str(int(per*100)) + '%'
            if persistent.PreciseDisplayGoal:
                $showgoal = "工作进度 " + str(player.achievedGoal) + ' / ' + str(player.goal) + " (" + str(int(per*100)) + '%)'

            textbutton showgoal:
                at trans_toRight(showtime)
                action [Hide("info"),Show(screen="info_use",i=info_goal, a=info_acg,pp=renpy.get_mouse_pos())]
                hovered Show(screen="info",i=info_goal, a=info_acg)
                unhovered Hide("info")
                text_style "gameUI"
                hover_sound audio.cursor

            if player.popularity < 1500:
                $ info_po = '这辈子都没想过我这个只会写点黄文的家伙也有人喜欢……'
            elif player.popularity < 5000:
                $ info_po = '诶……意外有很多人喜欢我呢……我不会就此成名出书吧——好吧，我至少应该先不死……'
            elif player.popularity < 10000:
                $ info_po = '居然已经超过5000多粉丝了吗……'
            elif player.popularity >= 10000:
                $ info_po = '已经有这么多人喜欢我写的作品了……我真的很感动，不为了我，也为了认可我文章的人继续活着。'
            $showtime += 0.05
            $info_por = '平台人气会提升每早在平台上收到打赏的概率和金额。\n\n写作后产生的已完成的文稿，写作时消耗的{color=#ffff00}灵感{/color}越多，上传文稿获得的粉丝越多。\n\n{color=#ff0000}上传的文稿消耗的灵感低于10层时会掉粉！{/color}\n\n粉丝数最低为1000。'
            textbutton _("平台人气 ") + str(player.popularity):
                at trans_toRight(showtime)
                action [Hide("info"),Show(screen="info_use", pp=renpy.get_mouse_pos(), i=info_por, a=info_po)]
                hovered Show(screen="info",i=info_por,a=info_po)
                unhovered Hide("info")
                text_style "gameUI"
                hover_sound audio.cursor

        vbox:
            $showtime += 0.05
            label _("状态") text_style "gameL":
                at trans_toRight(showtime)

            $ sev_info0 = '衡量病情是否严重的重要指标。\n\n严重程度会对所有日程的精神状态消耗、恢复和专注度造成负面影响，也会提升睡眠消耗的精神状态。\n\n基础严重程度：' + str(player.severity) +'('+ num_str(player.severityRegarded, '+', rev=True) + ')'
            $ sev_info_details  = '\n\n对基础精神状态消耗的影响：' + num_str(player.sev(),l='**', rev=True) + '\n对基础精神状态恢复的影响：' + num_str(1/player.sev(),l='**') + '\n对基础专注度的影响：' + num_str(1/player.sev(),l='**')
            $ sev_ad = '光是呼吸都会加剧你的头痛，在你出生那一刻就已经不配存在于这个世界上了。'
            $showtime += 0.05
            if player.severityRegarded > 1.0:
                $fun = red
            elif player.severityRegarded < 1.0:
                $fun = green
            else:
                $fun = str
            $showsev = "严重程度 " + fun(r2(player.severity * player.severityRegarded))
            if persistent.PreciseDisplayAbilities:
                $showsev += ' (' + str(player.severity) + ')'
            textbutton showsev:
                at trans_toRight(showtime)
                action [Hide("info"),Show(screen="info_use", pp=renpy.get_mouse_pos(), i=sev_info0+sev_info_details, a=sev_ad)]
                hovered Show(screen="info",i=sev_info0+sev_info_details, a=sev_ad)
                unhovered Hide("info")
                text_style "gameUI"
                hover_sound audio.cursor

            $ wor_info0 = '衡量工作和赚钱能力的指标。\n\n提升所赚的钱的同时也会提升除药物外的所有物品价格。\n\n基础工作能力：' + str(player.working) +'('+ num_str(player.workingRegarded, '+') + ')'
            $ wor_info_details = '\n\n基础工作类日程消耗率：'+ num_str(player.workConsumption) + '\n基础工作类日程恢复率：'+ num_str(player.workRecovery) + '\n基础工作类日程专注度：'+ num_str(player.workConcentration, '++')
            $ wor_ad = '你对于资本家们的价值所在。'
            $showtime += 0.05
            if player.workingRegarded > 1.0:
                $fun = green
            elif player.workingRegarded < 1.0:
                $fun = red
            else:
                $fun = str
            $showwor = "工作能力 " + fun(player.wor())
            if persistent.PreciseDisplayAbilities:
                $showwor += ' (' + str(player.working) + ')'
            textbutton showwor:
                at trans_toRight(showtime)
                action [Hide("info"),Show(screen="info_use", pp=renpy.get_mouse_pos(), i=wor_info0+wor_info_details, a=wor_ad)]
                hovered Show(screen="info",i=wor_info0+wor_info_details, a=wor_ad)
                unhovered Hide("info")
                text_style "gameUI"
                hover_sound audio.cursor
                

            $ phy_info0 = '衡量身体强壮度和坚韧性的指标。\n\n对所有精神状态相关的数值造成正面影响，也会降低睡眠消耗的精神状态。\n\n基础身体素质：'+str(player.physical) +'('+ num_str(player.physicalRegarded, '+') + ')'
            $ phy_info_details = '\n\n对基础精神状态消耗的影响：'+ num_str(player.phyCons(), rev=True,l='**') + '\n对基础精神状态恢复的影响：' + num_str(player.phyReco(),l='**') + '\n基础运动类日程消耗率：'+ num_str(player.sportConsumption) + '\n基础运动类日程恢复率：'+ num_str(player.sportRecovery) + '\n基础运动类日程专注度：'+ num_str(player.sportConcentration, '++')
            $ phy_ad = '虽然不具备把自己练到浑身都是肌肉的程度，但我的主治医师Pathos说运动可以缓解头疼，现在看来也确实是这样。'
            $showtime += 0.05
            if player.physicalRegarded > 1.0:
                $fun = green
            elif player.physicalRegarded < 1.0:
                $fun = red
            else:
                $fun = str

            $showphy = "身体素质 " + fun(player.phy())
            if persistent.PreciseDisplayAbilities:
                $showphy += ' (' + str(player.physical) + ')'

            textbutton showphy:
                at trans_toRight(showtime)
                action [Hide("info"),Show(screen="info_use", pp=renpy.get_mouse_pos(), i=phy_info0+phy_info_details, a=phy_ad)]
                hovered Show(screen="info",i=phy_info0+phy_info_details, a=phy_ad)
                unhovered Hide("info")
                text_style "gameUI"
                hover_sound audio.cursor

            $ wri_info0 = '衡量文字功底、文学欣赏水平和专注程度的指标。\n\n对专注度造成正面影响，满足需要更高水平的委托的要求，提升委托文稿的价值。\n\n基础写作技巧：'+str(player.writing) +'('+ num_str(player.writingRegarded, '+') + ')'
            $ wri_info_details = '\n\n日程专注度修正：' + num_str(player.wriConc(), '++') + '\n基础写作类日程消耗率：'+ num_str(player.writeConsumption) + '\n基础写作类日程恢复率：'+ num_str(player.writeRecovery) + '\n基础写作类日程专注度：'+ num_str(player.writeConcentration, '++')
            $ wri_ad = '写作几乎是我唯一的爱好了，把心里的痛苦写出来的感觉真的很棒。'

            $showtime += 0.05
            if player.writingRegarded > 1.0:
                $fun = green
            elif player.writingRegarded < 1.0:
                $fun = red
            else:
                $fun = str

            $showwri = "写作技巧 " + fun(player.wri())
            if persistent.PreciseDisplayAbilities:
                $showwri += ' (' + str(player.writing) + ')'
            
            textbutton showwri:
                at trans_toRight(showtime)
                action [Hide("info"),Show(screen="info_use", pp=renpy.get_mouse_pos(), i=wri_info0+wri_info_details, a=wri_ad)]
                hovered Show(screen="info",i=wri_info0+wri_info_details, a=wri_ad)
                unhovered Hide("info")
                text_style "gameUI"
                hover_sound audio.cursor


screen screen_dashboard_effects(player):
    style_prefix "gameUI"
    zorder 100
    $ effects = sliceArr(player.effects)
    $ del effects[0]
    frame:
        background None
        ypos 0.2
        xsize 500
        xalign 1.0
        viewport:
            draggable True
            mousewheel True
            ysize 530
            if len(player.effects)>24:
                scrollbars "vertical"
            vbox:
                xsize 455
                for i in effects:
                    $typename = type(i[0]).kind
                    $typei = effectKindInfo(typename, 'i')
                    $typea = effectKindInfo(typename, 'a')
                    textbutton typename text_style "gameL":
                        at trans_toLeft(0.2)
                        action [Show(screen="screen_effects", player=player), Hide("info")]
                        hovered Show(screen="info", i=typei, a=typea)
                        unhovered Hide("info")
                        xalign 1.0
                        hover_sound audio.cursor
                    vbox:
                        xalign 1.0
                        $l = len(i)
                        if type(i[0]).kind == '学识':
                            $col = 1
                        elif type(i[0]).kind == '药物反应':
                            $col = 2
                        else:
                            $col = 3
                        for j in range(int(l/col+1)):
                            
                            hbox:
                                xalign 1.0
                                for k in range(min(col, l-j*col)):
                                    $eff = i[j*col+k]

                                    $ite_pre = eff.getPrefixInfo()
                                    $ite_main = eff.getPrincipalInfo()
                                    $ite_suf = eff.getSuffixInfo()
                                    $stackinfo = '' if eff.stacks in (0,1) else '*' +str(eff.stacks)
                                    if eff.stacks == 0:
                                        $colorinfo = '{color=#b3b3b3}'
                                    elif eff.duration == 0 and type(eff).maxDuration!=0:
                                        $colorinfo = '{color=#F08080}'
                                    else:
                                        $colorinfo = ''
                                    if colorinfo != '':
                                        $stackinfo += '{/color}'

                                    textbutton colorinfo + type(eff).name + stackinfo  text_style "gameUI":
                                        #at trans_toLeft((j*col+k)*0.05+0.25)
                                        action [Show(screen="screen_effects", player=player), Hide("info3")]
                                        hovered Show(screen="info3", t=type(eff).name, i1=ite_pre, i2=ite_main+ite_suf, a2=type(eff).ad)
                                        unhovered Hide("info3")
                                        hover_sound audio.cursor