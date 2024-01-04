screen screen_dashboard(player):
    
    zorder 500

    if not renpy.get_screen("screen_phone_camera_show"):
        use screen_dashboard_calendar(player)
        use screen_dashboard_medicine(player)
        use screen_dashboard_severity(player)
        use screen_dashboard_abilities(player)
        use screen_dashboard_effects(player)


screen screen_dashboard_calendar(player):
    style_prefix "gameUI"
    zorder 500
    $ weekday = weekdayFormat(player.today)
    $ cons = player.aggravationConsumption()
    $ info = _('\n消耗倍率：') + num_str(player.deteriorateConsumption, rev = True)
    $ info2 = _('\n过夜预计消耗的精神状态约为：') + str(cons)
    $ ad = _('时间正在一刻不停地流逝，无可避免的死亡正在前方等待，而悔恨和不甘正在堆积。')
    if player.finalStageDays > -1:
        $ ad = _("即将抵达的死亡。")

    vbox:
        xpos 0.02
        ypos 0.02
        $showHour=player.st()[0]
        $showMin=player.st()[1]
        $weather=type(player.effects[0])
        $wea_name = weather.name
        $wea_info = weather.info
        $wea_ad = weather.ad
        if player.cured > 0:
            $ poz = _('？？？')
        elif player.onOutside:
            $ poz = _('在外面')
        elif player.onVacation:
            $ poz = _('在家中')
        else:
            $ poz = _('在公司')
        
        if config.developer:
            $ poz += _('\n时间段：%s') % player.times

        

        $wea_t = _('本日天气为：') + wea_name
        if player.finalStageDays > -1:
            textbutton _("废墟下的第[player.finalStageDays]天")xalign 0.0:
                at trans_Down(0.2)
                #action Function(allE, player=player)
                action [Hide("info3"),Show(screen="info3_use", pp=renpy.get_mouse_pos(), t=wea_t, i1=wea_info, a1=wea_ad, i2=info2+info, a2=ad)]
                hovered Show(screen="info3",t=wea_t, i1=wea_info, a1=wea_ad, i2=info2+info, a2=ad)
                unhovered Hide("info3")
                text_style "gameUI"
                hover_sound audio.cursor
        else:
            $showing = _("[player.mon]月[player.day]日  第[player.week]周  [wea_name]\n[weekday]  [showHour]:[showMin]  [poz]")
            if _preferences.language == 'english':
                $eng_month = {1:'Jan.', 2:'Feb.', 3:'Mar.', 4:'Apr.', 5:'May', 6:'Jun.', 7:'Jul', 8:'Aug.', 9:'Sept.', 10:'Oct.', 11:'Nov.', 12:'Dec.'}
                $eng_day = {1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}
                if player.mon in eng_month:
                    $showmonth = eng_month[player.mon]
                else:
                    $showmonh = '???'
                if player.today in eng_day:
                    $showday = eng_day[player.mon]
                else:
                    $showday = '???'
                $showing = _("[player.day]  [showmonth]  Week [player.week]  [wea_name]\n[showday]  [showHour]:[showMin]  [poz!t]")
            textbutton showing xalign 0.0:
                at trans_Down(0.2)
                #action Function(allE, player=player)
                action [Hide("info3"),Show(screen="info3_use", pp=renpy.get_mouse_pos(), t=wea_t, i1=wea_info, a1=wea_ad, i2=info2+info, a2=ad)]
                hovered Show(screen="info3",t=wea_t, i1=wea_info, a1=wea_ad, i2=info2+info, a2=ad)
                unhovered Hide("info3")
                text_style "gameUI"
                hover_sound audio.cursor



screen screen_dashboard_medicine(player):
    style_prefix "gameUI"
    zorder 500
    $ hasMed = False
    $ tim = 0.2
    $ drugReco = int(player.basicRecovery * player.drugRecovery * 100)
    $ quickuse_info = _('点击可快捷使用。')
    vbox:
        xalign 0.98
        yalign 0.02
        
        if MedicineA.has(player):
            $tim += 0.05
            $ hasMed = True
            $ info1 = MedicineA.getinfo(player) + quickuse_info
            $ ad1 = MedicineA.ad
            textbutton str(MedicineA.get(player).amounts) + _("    药物{font=arial.ttf}α{/font}"):
                at med_menu(tim)
                if not Despair.has(p):
                    if persistent.actionquickly:
                        action Function(quickUse, item=MedicineA, player=player), Hide("info")
                    else:
                        action [Show(screen="info_confirm",text=_('使用'),act=[Function(quickUse, item=MedicineA, player=player), Hide("info")],i=info1,a=ad1, width=401,pp=renpy.get_mouse_pos()), Hide("info")]
                        
                else:
                    action NullAction()
                hovered Show(screen="info",i=info1,a=ad1,width=401)
                unhovered Hide("info")
                text_style "meda_text"
                xalign 1.0

                if not Despair.has(p):
                    activate_sound audio.itemmed
                else:
                    activate_sound audio.error
                    

        if MedicineB.has(player):
            $tim += 0.05
            $ hasMed = True
            $ info2 = MedicineB.getinfo(player) + quickuse_info
            $ ad2 = MedicineB.ad
            textbutton str(MedicineB.get(player).amounts) + _("    药物{font=arial.ttf}β{/font}"):
                at med_menu(tim)
                if not Despair.has(p):
                    if persistent.actionquickly:
                        action Function(quickUse, item=MedicineB, player=player), Hide("info")
                    else:
                        action [Show(screen="info_confirm",text=_('使用'),act=[Function(quickUse, item=MedicineB, player=player), Hide("info")],i=info2,a=ad2, width=401,pp=renpy.get_mouse_pos()), Hide("info")]
                else:
                    action NullAction()
                hovered Show(screen="info",i=info2,a=ad2,width=401)
                unhovered Hide("info")
                text_style "medb_text"
                xalign 1.0
                if not Despair.has(p):
                    activate_sound audio.itemmed
                else:
                    activate_sound audio.error

        if MedicineC.has(player):
            $tim += 0.05
            $ hasMed = True
            $ info3 = MedicineC.getinfo(player) + quickuse_info
            $ ad3 = MedicineC.ad
            textbutton str(MedicineC.get(player).amounts) + _("    药物{font=arial.ttf}γ{/font}"):
                at med_menu(tim)
                if not Despair.has(p):
                    if persistent.actionquickly:
                        action Function(quickUse, item=MedicineC, player=player), Hide("info")
                    else:
                        action [Show(screen="info_confirm",text=_('使用'),act=[Function(quickUse, item=MedicineC, player=player), Hide("info")],i=info3,a=ad3, width=401,pp=renpy.get_mouse_pos()), Hide("info")]
                else:
                    action NullAction()
                hovered Show(screen="info",i=info3,a=ad3,width=401)
                unhovered Hide("info")
                text_style "medc_text"
                xalign 1.0
                if not Despair.has(p):
                    activate_sound audio.itemmed
                else:
                    activate_sound audio.error

        if MedicineD.has(player):
            $ hasMed = True
            $tim += 0.05
            $ ad4 = MedicineD.ad
            textbutton str(MedicineD.get(player).amounts) + _("    药物{font=arial.ttf}δ{/font}"):
                at med_menu(tim)
                if persistent.actionquickly:
                    action Function(quickUse, item=MedicineD, player=player), Hide("info")
                else:
                    action [Show(screen="info_confirm",width=401,text=_('使用'),act=[Function(quickUse, item=MedicineD, player=player), Hide("info")], i=MedicineD.getinfo(player) + quickuse_info,a=ad4, pp=renpy.get_mouse_pos()), Hide("info")]
                hovered Show(screen="info",width=401,i=MedicineD.getinfo(player) + quickuse_info,a=ad4)
                unhovered Hide("info")
                text_style "medd_text"
                xalign 1.0
                hover_sound audio.itemmed

        if not hasMed:
            textbutton _("你已经没有药了。"):
                at trans_toLeft(tim)
                action NullAction()
                text_style "gameUI"
                xalign 1.0




screen screen_dashboard_severity(player):
    style_prefix "gameUI"
    python:
        info0 = _('衡量当前对疼痛忍耐度的重要指标。\n\n耗费精力时会消耗，做一些休息的事时则会恢复。\n当早晨起床无法使用药物将自身的精神状态提升至大于0的精神状态时，游戏结束。')
        info1 = _('\n\n基础精神状态消耗倍率：') + num_str(Task.getConsScale(player),rev=True)
        info2 = _('\n基础精神状态恢复倍率：') + num_str(Task.getRecoScale(player))
        ad = _('你天生罹患的偏头痛似乎没有办法治愈，药效随着时间流逝正在减弱。\n如果你没有在疼痛突破防线之前咽下药物，那么也许你便再也没有机会见到第二天的太阳了。')
        p2men = ''
        if config.developer and player.p2:
            p2men = _('<') + str(player.p2.mental) + _('><') + str(Despair.getstack(player.p2))+ _('>')
        if BookUndeadEffect.has(player) and player.mental <= 0:
            player.mental = 10

    zorder 500
    vbox:
        xcenter 0.5
        ypos 0.02
        
        textbutton _("精神状态\n") + r2s(player.mental) + p2men:
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
    zorder 500
    vbox:
        xpos 0.02
        ypos 0.13

        vbox:
            label _("基础") text_style "gameL":
                at trans_toRight(0.2)
            $ info = _('今日种子：') + str(player.seed)# + _('\n当前Safe指数：') + str(player.safe)
            $ info1 = _('\n\n专注度可以使日程的获得更好结果的概率上升。\n\n基础专注度修正：') + num_str(Task.getConcScale(player), '++')
            $ info2 = _('\n\n使用食物和药物的恢复效率。\n\n基础食物恢复效率：%s\n最终食物恢复效率：%s') % (num_str(1-player.fooduse*0.005), num_str(player.useFoodScale()))
            $ info3 = _('\n药物恢复效率：') + num_str(player.useDrugScale())
            if player.name == 'Solitus':
                $ad = _('我的名字，非常适合我。')
            else:
                $ad = _('别人称呼我的方式，即便我并不喜欢这个名字。')
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
                $ info_money = _('我没有钱了，我只能努力工作然后祈祷自己会不在这个期间被公司开除。')
            elif player.money > 1000 and meds > 0:
                $ info_money = _('我已经买过这周要吃的药了，这些空闲的钱应该能让我美美过上一周。')
            elif player.money < 1500 and meds == 0:
                $ info_money = _('这些钱……足够我买药吗？')
            elif player.money < 3000 and meds == 0:
                $ info_money = _('呼，我喜欢发工资的感觉，但这些钱马上就会被购买药物的开销消耗殆尽。')
            elif player.money > player.price * 8:
                $ info_money = _('也许这次我可以不用把所有的钱拿来买药。')
            else:
                $ info_money = _('这些钱能买些什么呢……')
            $showtime += 0.05
            textbutton _("所持金钱 ") + str(player.money):
                at trans_toRight(showtime)
                action [Hide("info"),Show(screen="info_use", pp=renpy.get_mouse_pos(), i=_('购买药物和其他能够保障生存的东西。'), a=info_money)]
                hovered Show(screen="info",i=_('购买药物和其他能够保障生存的东西。'), a=info_money)
                unhovered Hide("info")
                text_style "gameUI"
                hover_sound audio.cursor
            $showtime += 0.05
            textbutton _("药物价格 ") + str(player.price):
                at trans_toRight(showtime)
                action [Hide("info"),Show(screen="info_use", pp=renpy.get_mouse_pos(), i=_('下周药价涨价幅度：') + str(player.priceIncrease) + '%', a=_('努力赚钱，要么就被疯涨的药价压倒。'))]
                hovered Show(screen="info", i=_('下周药价涨价幅度：') + str(player.priceIncrease) + '%', a=_('努力赚钱，要么就被疯涨的药价压倒。'))
                unhovered Hide("info")
                text_style "gameUI"
                hover_sound audio.cursor
            $showtime += 0.05
            $paid_info, wages_info = player.calWorkPaid()
            $paid_info = _('\n\n预计获得收入：') + str(paid_info)
            $wages_info = _('\n预计下周工资：') + str(wages_info)
            $w_info = _('每周在发过工资后都会根据工作能力和上周的工作完成度加薪。') + paid_info + wages_info
            $w_a = _('偶尔我也想着，如果我再也不需要买药的话，那这些钱够我吃多少好吃的，玩多少好玩的呢？')
            if player.experience != 'wri':
                textbutton _("本周工资 ") + str(player.wages):
                    at trans_toRight(showtime)
                    action [Hide("info"),Show(screen="info_use", pp=renpy.get_mouse_pos(), i=w_info, a=w_a)]
                    hovered Show(screen="info",i=w_info,a=w_a)
                    unhovered Hide("info")
                    text_style "gameUI"
                    hover_sound audio.cursor
            
            #textbutton _("工作目标 ") + str(player.goal):
            #    action NullAction()
            #    hovered Show(screen="info", i=_('工作速度加成：') + str(int((player.workSpeed-1) * 100)) + '%', a=_('就算我再努力工作，估计也是在这个小破职位，永远也不会升职。'))
            #    unhovered Hide("info")
            #    text_style "gameUI"  # 判定升职后修改
            
            $per = player.achievedGoal/player.goal
            if per == 0:
                $ info_acg = _('又是新的一周，看看这周我要被分配哪些工作……')
            elif per < 0.3 and player.today < 3:
                $ info_acg = _('这周才刚开始我就累了。')
            elif per < 0.4 and player.today < 5:
                $ info_acg = _('完了，这绝对做不完了……')
            elif per < 0.9 and player.today < 5:
                $ info_acg = _('糟糕……我是不是摸鱼摸太多了……不会做不完工作吧……')
            elif per >= 1 and player.today < 5:
                $ info_acg = _('这周也是勉强糊弄过去了，总之发工资前都可以狂摸鱼啦！')
            else:
                $ info_acg = _('偶尔回头看看自己做的工作，也很有成就感就是了……')
            $showtime += 0.05
            $info_goal = _('如果在周五之前没有达到100%以上，只会获得一半的每周工资。\n如果超过了120%，则会获得更多的工资和加薪。')
            $showgoal = _("工作进度 ") + str(int(per*100)) + '%'
            if persistent.PreciseDisplayGoal:
                $showgoal = _("工作进度 ") + str(player.achievedGoal) + ' / ' + str(player.goal) + " (" + str(int(per*100)) + '%)'
            if player.experience != 'wri':
                textbutton showgoal:
                    at trans_toRight(showtime)
                    action [Hide("info"),Show(screen="info_use",i=info_goal, a=info_acg,pp=renpy.get_mouse_pos())]
                    hovered Show(screen="info",i=info_goal, a=info_acg)
                    unhovered Hide("info")
                    text_style "gameUI"
                    hover_sound audio.cursor

            if player.experience == 'wri' and WriterItem1.has(p):
                textbutton '小说进度 ' + str(WriterItem1.get(p).progress) + '%':
                    at trans_toRight(showtime)
                    action [Hide("info"),Show(screen="info_use",i="独属于你自己的小说的撰写进度。\n提升小说进度需要消耗回忆片段进行撰写小说日程，而进行人物剧情可以获得若干人物片段。", a="为什么要……这么做呢……",pp=renpy.get_mouse_pos())]
                    hovered Show(screen="info",i="独属于你自己的小说的撰写进度。\n提升小说进度需要消耗回忆片段进行撰写小说日程，而进行人物剧情可以获得若干人物片段。", a="为什么要……这么做呢……")
                    unhovered Hide("info")
                    text_style "gameUI"
                    hover_sound audio.cursor

            if player.popularity < 5000:
                $ info_po = _('这辈子都没想过我这个只会写点黄文的家伙也有人喜欢……')
            elif player.popularity < 10000:
                $ info_po = _('诶……意外有很多人喜欢我呢……我不会就此成名出书吧——好吧，我至少应该先不死……')
            elif player.popularity < 40000:
                $ info_po = _('居然已经有这么多粉丝了吗……')
            elif player.popularity >= 40000:
                $ info_po = _('已经有这么多人喜欢我写的作品了……我真的很感动，不为了我，也为了认可我文章的人继续活着。')
            $showtime += 0.05
            $info_por = _('平台人气会提升每早在平台上收到打赏的概率和金额，也有一定概率流失人气。\n\n写作后产生的已完成的文稿，写作时消耗的{color=#ffff00}灵感{/color}越多，上传文稿获得的粉丝越多。\n\n{color=#ff0000}上传的文稿消耗的灵感较低时会掉粉！{/color}\n\n当前粉丝下限为1000，上限为'+str(p.maxpopularity)+'。')
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

            $ sev_info0 = _('衡量病情是否严重的重要指标。\n\n严重程度会对所有日程的精神状态消耗、恢复和专注度造成负面影响，也会提升睡眠消耗的精神状态。\n\n基础严重程度：') + str(player.severity) +'('+ num_str(max(player.severityRegarded, 0.2), '+', rev=True) + ')'
            $ sev_info_details  = _('\n\n精神状态消耗修正：') + num_str(player.sev(),l='**', rev=True) + _('\n精神状态恢复修正：') + num_str(1/player.sev(),l='**') + _('\n专注度修正：') + num_str(1/player.sev(),l='**')
            $ sev_ad = _('光是呼吸都会加剧你的头痛，在你出生那一刻就已经不配存在于这个世界上了。') if player.sev() != 0.01 else _('你再也不用受头疼的折磨了，可代价是什么？')
            $showtime += 0.05
            if player.severityRegarded > 1.0:
                $fun = red
            elif player.severityRegarded < 1.0:
                $fun = green
            else:
                $fun = str
            $showsev = _("严重程度 ") + fun(r2(player.sev()))
            if persistent.PreciseDisplayAbilities:
                $showsev += ' (%s)' % r2(player.severity)
            textbutton showsev:
                at trans_toRight(showtime)
                action [Hide("info"),Show(screen="info_use", pp=renpy.get_mouse_pos(), i=sev_info0+sev_info_details, a=sev_ad)]
                hovered Show(screen="info",i=sev_info0+sev_info_details, a=sev_ad)
                unhovered Hide("info")
                text_style "gameUI"
                hover_sound audio.cursor

            $ wor_info0 = _('你的利用价值所在。\n\n提升工作完成的工作量以及工作的专注度。\n\n基础工作能力：') + str(player.working) +'('+ num_str(player.workingRegarded, '+') + ')'
            $ wor_info_details = _('\n\n额外工作速度：') + str(int((player.workSpeed-1) * 100)) + _('%\n工作类日程专注度修正：') + num_str(15 * player.wor() - 20, '++')
            $ wor_info_details += _('\n\n当你通过日程获取工作能力时会根据加成提升更多的能力点数。\n工作能力获取加成：%s') % num_str(int(player.workingGain*100), '++', '')
            $ wor_ad = _('几乎是我唯一的稳定赚钱方式，我一定不能丢掉这份工作。')
            $showtime += 0.05
            if player.workingRegarded > 1.0:
                $fun = green
            elif player.workingRegarded < 1.0:
                $fun = red
            else:
                $fun = str
            $showwor = _("工作能力 ") + fun(player.wor())
            if persistent.PreciseDisplayAbilities:
                $showwor += ' (%s)' % r2(player.working)
            if p.experience != 'wri':
                textbutton showwor:
                    at trans_toRight(showtime)
                    action [Hide("info"),Show(screen="info_use", pp=renpy.get_mouse_pos(), i=wor_info0+wor_info_details, a=wor_ad)]
                    hovered Show(screen="info",i=wor_info0+wor_info_details, a=wor_ad)
                    unhovered Hide("info")
                    text_style "gameUI"
                    hover_sound audio.cursor
                

            $ phy_info0 = _('衡量身体强壮度和坚韧性的指标。\n\n对所有精神状态相关的数值造成正面影响，也会降低睡眠消耗的精神状态。\n\n基础身体素质：%s(%s)') % (player.physical, num_str(player.physicalRegarded, '+'))
            if p.phy() < 3:
                $ phy_info_details = _('\n\n精神状态消耗修正：%s\n精神状态恢复修正：%s\n运动类日程专注度修正：%s') % (num_str(player.phyCons(), rev=True,l='**'), num_str(player.phyReco(),l='**'), num_str(20 * player.phy() - 30, '++'))
            else:
                $ phy_info_details = _('\n\n精神状态消耗修正：%s（最大值）\n精神状态恢复修正：%s（最大值）\n运动类日程专注度修正：%s') % (num_str(player.phyCons(), rev=True,l='**'), num_str(player.phyReco(),l='**'), num_str(20 * player.phy() - 30, '++'))
            $ phy_info_details += _('\n\n当你通过日程获取身体素质时会根据加成提升更多的能力点数。\n身体素质获取加成：%s') % num_str(int(player.physicalGain*100), '++', '')
            $ phy_ad = _('虽然没法把自己练到浑身都是肌肉的程度，但我的主治医师Pathos说运动可以缓解头疼，现在看来也确实是这样。')
            $showtime += 0.05
            if player.physicalRegarded > 1.0:
                $fun = green
            elif player.physicalRegarded < 1.0:
                $fun = red
            else:
                $fun = str

            $showphy = _("身体素质 ") + fun(player.phy())
            if persistent.PreciseDisplayAbilities:
                $showphy += ' (%s)' % r2(player.physical)

            textbutton showphy:
                at trans_toRight(showtime)
                action [Hide("info"),Show(screen="info_use", pp=renpy.get_mouse_pos(), i=phy_info0+phy_info_details, a=phy_ad)]
                hovered Show(screen="info",i=phy_info0+phy_info_details, a=phy_ad)
                unhovered Hide("info")
                text_style "gameUI"
                hover_sound audio.cursor

            $ wri_info0 = _('衡量文字功底、文学欣赏水平和专注程度的指标。\n\n对专注度造成正面影响，满足需要更高水平的委托的要求，提升委托文稿的价值。\n\n基础写作技巧：')+str(player.writing) +'('+ num_str(player.writingRegarded, '+') + ')'
            if p.wri() < 3:
                $ wri_info_details = _('\n\n专注度修正：') + num_str(player.wriConc(), '++')+ _('\n写作类日程专注度修正：') + num_str(7 * player.wri() - 10, '++')
            else:
                $ wri_info_details = _('\n\n专注度修正：') + num_str(player.wriConc(), '++') + _('（最大值）\n写作类日程专注度修正：') + num_str(7 * player.wri() - 10, '++')
            $ wri_info_details += _('\n\n当你通过日程获取写作能力时会根据加成提升更多的能力点数。\n写作能力获取加成：%s') % num_str(int(player.writingGain*100), '++', '')
            $ wri_ad = _('写作几乎是我唯一的爱好了，把心里的痛苦写出来的感觉真的很棒。')

            $showtime += 0.05
            if player.writingRegarded > 1.0:
                $fun = green
            elif player.writingRegarded < 1.0:
                $fun = red
            else:
                $fun = str

            $showwri = _("写作技巧 ") + fun(player.wri())
            if persistent.PreciseDisplayAbilities:
                $showwri += ' (%s)' % r2(player.writing)
            
            textbutton showwri:
                at trans_toRight(showtime)
                action [Hide("info"),Show(screen="info_use", pp=renpy.get_mouse_pos(), i=wri_info0+wri_info_details, a=wri_ad)]
                hovered Show(screen="info",i=wri_info0+wri_info_details, a=wri_ad)
                unhovered Hide("info")
                text_style "gameUI"
                hover_sound audio.cursor


screen screen_dashboard_effects(player):
    style_prefix "gameUI"
    zorder 400
    python:
        if len(player.effects) >=50:
            Achievement310.achieve()
            Achievement.show()
        if LifeIsColorless.has(player):
            effects = [[LifeIsColorless.get(p)]]
        else:
            effects = sliceArr(player.effects)
            del effects[0]
        
    frame:
        background None
        ypos 0.2
        xsize 550
        xalign 1.0
        modal False
        at trans_toLeft(0.2)
        viewport:
            #draggable True
            mousewheel True
            ysize 530
            xinitial 1.0
            scrollbars "vertical"
            vbox:
                xsize 500
                for i in effects:
                    $typename = i[0].kind
                    $typei = effectKindInfo(typename, 'i')
                    $typea = effectKindInfo(typename, 'a')
                    textbutton '{size=-10}'+typename+'{/size}' text_style "gameL":
                        action NullAction()
                        xalign 1.0
                        ysize 20
                        hover_sound audio.cursor
                        
                    vbox:
                        xalign 1.0
                        
                        python:
                            l = len(i)
                            if type(i[0]).kind == '学识':
                                col = 1
                            elif type(i[0]).kind == '药物反应':
                                col = 2
                            else:
                                col = 3
                        for j in range(int(l/col+1)):
                            
                            hbox:
                                box_wrap True
                                xalign 1.0
                                for k in range(min(col, l-j*col)):
                                    python:
                                        eff = i[j*col+k]

                                        stackinfo = '' if eff.stacks in (0,1) else '*' +str(eff.stacks)
                                        if eff.stacks == 0:
                                            colorinfo = _('{color=#b3b3b3}{s}')
                                        elif eff.duration == 1 and eff.maxDuration!=1:
                                            colorinfo = _('{color=#F08080}')
                                        else:
                                            colorinfo = ''
                                        if colorinfo != '':
                                            stackinfo += _('{/color}')
                                    if not eff.hide:
                                        textbutton colorinfo + eff.name + stackinfo  text_style "gameUI":
                                            #at trans_toLeft((j*col+k)*0.05+0.25)
                                            if not LifeIsColorless.has(player):
                                                action [Show(screen="screen_effects", player=player), Hide("info_e")]

                                            else:
                                                action NullAction()
                                            hovered Show(screen="info_e", eff=eff)
                                            unhovered Hide("info_e")
                                            hover_sound audio.cursor

