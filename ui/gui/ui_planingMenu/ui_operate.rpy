screen screen_operate(player):
    zorder 300

    python:
        def time_forward(p):
            p.times += 1

        def geticon(player, item):
            if not type(item) in player.itemcd:
                return item.icon()
            cd = player.itemcd[type(item)]
            return Composite((75, 75), (0, 0), item.icon(), (0, 0), 'gui/items/cooldown.png', (0, 0),Fixed(Text(str(cd), size=30,xcenter=0.5, ycenter=0.5)))

    if not renpy.get_screen("screen_phone_camera_show"):
        $renpy.sound.stop(channel="chara_voice")
        hbox:
            xpos 0.05
            ypos 0.85

            spacing 50
            if player.cured < 0 and not Despair.has(p):
                imagebutton auto "gui/menu/phone_%s.png":
                    at trans_Up()
                    action [Show(screen="screen_phone", player=player), Hide("info")]
                    hovered Show(screen="info", i=_('打开手机。\n你可以用它来进行不需要消耗回合的事件，打电话给你喜欢的人，点个外卖，或是在手机的接稿平台上查看每日更新的委托。'), a=_('“真的有不用手机刷短视频和玩手游的人吗？”……\n没错，就是在下。'))
                    unhovered Hide("info")
                    
                    activate_sound audio.opearte_phone
            imagebutton auto "gui/menu/schedule_%s.png":
                at trans_Up()
                action [Show(screen="screen_tasks", player=player), Hide("info")]
                hovered Show(screen="info", i=_('安排日程\n安排你接下来一整天要做的事，没有全部安排完则无法进行到下一时间段。'), a=_('可以忍受上司的批评，但是不能忍受突发事件导致的日程计划修改！'))
                unhovered Hide("info")
                
                activate_sound audio.opearte_task
            if not Despair.has(p):
                imagebutton auto "gui/menu/box_%s.png":
                    at trans_Up()
                    action [Show(screen="screen_items", player=player), Hide("info")]
                    hovered Show(screen="info", i=_('库存\n检查你所持有的物品，使用或是丢弃。'), a=_('虽然能看到很多东西但这并不代表我会把所有的东西都随身携带着！总之你懂就好……'))
                    unhovered Hide("info")
                    
                    activate_sound audio.opearte_inventory
            else:
                imagebutton auto "gui/menu/medicine_%s.png":
                    at trans_Up()
                    action [Hide("info"), Jump("despairusemed")]
                    hovered Show(screen="info", i=_('服用药物\n你的药物。'), a=_('这些东西本应属于你，只属于你。'))
                    unhovered Hide("info")
                    
                    activate_sound audio.itemmed

            if player.cured < 0 and not Despair.has(p):
                imagebutton auto "gui/menu/effinfo_%s.png":
                    at trans_Up()
                    action [Show(screen="screen_effects", player=player), Hide("info")]

                    
                    hovered Show(screen="info", i=_('角色效果\n检查你此时拥有的各种效果和详细信息。'), a=_('呵呵，不看BUFF就让我狂上班的人连第一周都活不过去。'))
                    unhovered Hide("info")
                    
                    
            imagebutton auto "gui/menu/settings_%s.png":
                at trans_Up()
                action [ShowMenu(screen='screen_gamemenu',player=player), Hide("info")]
                hovered Show(screen="info", i=_('菜单\n打开游戏菜单。'), a=_('30xx年可以已经可以穿越时空了……于是我们……\n噢，等等，我们的游戏背景才发展到21世纪吗！？'))
                unhovered Hide("info")
                
            frame:
                background None
                yoffset 10
                xoffset 10
                

                hbox:
                    spacing 5
                    $stari = list(filter(lambda x: x.star, player.items))
                    for i in range(min(10, len(stari))):
                        $item = stari[i]
                        frame:
                            background None
                            xsize 80
                            ysize 80
                            imagebutton idle geticon(player, item):
                                action Function(ui_itemUse, item=item, player=player)
                                hovered Show(screen="info", i=_('快速使用%s。' % item.name))
                                unhovered Hide("info")
                                activate_sound audio.cursor
                                at trans_Up(i*0.05)
                            if item.amounts > 1:
                                text str(item.amounts) size 25 at trans_Up(i*0.05)

                    if not persistent.forbidnostarquickitem and len(stari) < 10:
                        python:
                    
                            otheri = list(filter(lambda x: not x.blocked and x.maxCd != -1 and type(x) not in p.itemcd and x not in list(filter(lambda x: x.star, p.items)) and x.kind not in ('书籍', '专业类书籍'), p.items))
                            if len(otheri) > 1:
                                for i in range(len(otheri)-1, 0, -1):
                                    if type(otheri[i-1]) == type(otheri[i]):
                                        del otheri[i]

                        for i in range(min(10-len(stari), len(otheri))):
                            $item = otheri[i]
                            frame:
                                background None
                                xsize 80
                                ysize 80
                                imagebutton idle geticon(player, item):
                                    action Function(ui_itemUse, item=item, player=player)
                                    hovered Show(screen="info", i=_('快速使用%s。' % item.name))
                                    unhovered Hide("info")
                                    activate_sound audio.cursor
                                    at trans_Up(i*0.05)
                                if item.amounts > 1:
                                    text str(item.amounts) size 25 at trans_Up(i*0.05)
        if CafeBuff.has(player):
            hbox:
                xpos 0.95
                ypos 0.725
                spacing 50
                xalign 1.0
                imagebutton auto "gui/menu/home_%s.png":
                    at trans_toLeft()
                    action Hide("info"), Jump("explore_shop_5_end")
                    hovered Show(screen="info", i=_('离开咖啡馆。'), a='在醒时的世界，和在梦中一样。')
                    unhovered Hide("info")

                imagebutton auto "gui/menu/shop_%s.png":
                    at trans_toLeft()
                    
                    action ShowMenu(screen="screen_explore_buycoffee", player=player, _transition=dissolve),Hide('info')
                    hovered Show(screen="info", i=_('购买咖啡。'), a='存在意义不大……但书店有的东西我们也得有。')
                    unhovered Hide("info")

        elif BookstoreBuff.has(player):
            hbox:
                xpos 0.95
                ypos 0.725
                spacing 50
                xanchor 1.0

                imagebutton auto "gui/menu/home_%s.png":
                    at trans_toLeft()
                    action Hide("info"), Jump("explore_bookshop_end")
                    hovered Show(screen="info", i=_('离开书店。'), a='在醒时的世界，和在梦中一样。')
                    unhovered Hide("info")

                imagebutton auto "gui/menu/shop_%s.png":
                    at trans_toLeft()
                    action ShowMenu(screen="screen_explore_buybook", player=player, _transition=dissolve),Hide('info')
                    hovered Show(screen="info", i=_('购买书籍。'), a='买书->获得新鲜感->速读->买书……你以为我会让你这么做么！')
                    unhovered Hide("info")
            
        elif player.cured < 0 and not Despair.has(p):
            hbox:
                xpos 0.9
                ypos 0.725
                imagebutton auto "gui/menu/explore_%s.png":
                    at trans_toLeft()
                    action Show(screen="screen_map", player=player, transition=dissolve)
                    hovered Show(screen="info", i=_('地图\n检查A市你所居住的城区地图。'), a=_('到达世界最高城A市！太美丽了A市……\n哎呀这不于老师吗？\n再看看远处的社畜沙漠狼吧家人们……'))
                    unhovered Hide("info")
        
        if player.cured < 0 and not Despair.has(p):
            hbox:
                xpos 0.05
                ypos 0.725
                imagebutton auto "gui/menu/warn_%s.png":
                    at trans_toRight()
                    action Show(screen="screen_journal", player=player, transition=dissolve)
                    hovered Show(screen="info", i=_('待办事项\n记录了本周要做的事情。'), a=_('为总是忘记推剧情的宝贝们添加的新东西。'))
                    unhovered Hide("info")
                    activate_sound audio.opearte_journal
                    

        hbox:
            xpos 0.9
            ypos 0.85
            if player.hal_p == 11 and player.today==6 and player.times == 10 and not SteamerTicket.has(player) and player.messages['Halluke'][-1].seen != None and player.cured==-1:
                imagebutton auto "gui/menu/edit_%s.png":
                    at trans_toLeft()
                    action Function(showNotice, [_('还没有给Halluke发消息。')])
                    hovered Show(screen="info", i=_('还没有给Halluke发消息。'))
                    unhovered Hide("info")
                    activate_sound audio.error

            elif player.isScheduled():
                imagebutton auto "gui/menu/edit_%s.png":
                    at trans_toLeft()
                    action Function(showNotice, [_('还未完成日程的安排！')])
                    hovered Show(screen="info", i=_('尚未安排完本日的日程\n点击左下方第二个图标安排你的本日日程。'), a=_('说真的，就不能给我一点单纯发呆的时间吗？'))
                    unhovered Hide("info")
                    activate_sound audio.error

            elif Message.hasNewMes(player):

                imagebutton auto "gui/menu/edit_%s.png":
                    at trans_toLeft()
                    action Function(showNotice, [_('某信中还有未读的信息！')])
                    hovered Show(screen="info", i=_('点击手机图标里的某信，检查其他人给你发来的新信息。'), a=_('就是高冷不想回不行？'))
                    unhovered Hide("info")
                    activate_sound audio.error

            else:
                imagebutton auto "gui/menu/done_%s.png":
                    at trans_toLeft()
                    action [Hide("screen_operate"),Function(time_forward, p), Return(None),Hide("info")]
                    hovered Show(screen="info", i=_('已安排完日程\n点击图标结束规划并开始按照顺序完成日程。'), a=_('可能日程表对我来说就是有种魔力吧，写在上面的东西就必须一点一点地完成……'))
                    unhovered Hide("info")
                    activate_sound audio.cursor
        if player.week == 1 and player.today==1 and player.times==2:
            if not player.uihelp:
                python:
                    def func(player):
                        player.uihelp = True
                add "images/gui/uihelp.png" at uihelp_trans1
                button:
                    xfill True
                    yfill True
                    action Function(func, player)
            elif renpy.showing("images/gui/uihelp.png"):
                add "images/gui/uihelp.png" at uihelp_trans2

        if player.hal_p == 11 and player.today==6 and player.times == 10 and not SteamerTicket.has(p) and player.messages['Halluke'][-1].seen != None and player.cured==-1 and player.finalStageDays==-1:
            key 'K_SPACE' action Function(showNotice, [_('还没有给Halluke发消息。')])
        elif player.isScheduled():
            key 'K_SPACE' action Function(showNotice, [_('还未完成日程的安排！')])
        elif Message.hasNewMes(player):
            key 'K_SPACE' action Function(showNotice, [_('某信中还有未读的信息！')])
        else:
            key 'K_SPACE' action [Hide("screen_operate"),Function(time_forward, p), Return(None),Hide("info")]

        if player.hal_p == 11 and player.today==6 and player.times == 10 and not SteamerTicket.has(p) and player.messages['Halluke'][-1].seen != None and player.cured==-1 and player.finalStageDays==-1:
            key 'K_LCTRL' action Function(showNotice, [_('还没有给Halluke发消息。')])
        elif player.isScheduled():
            key 'K_LCTRL' action Function(showNotice, [_('还未完成日程的安排！')])
        elif Message.hasNewMes(player):
            key 'K_LCTRL' action Function(showNotice, [_('某信中还有未读的信息！')])
        else:
            key 'K_LCTRL' action [Hide("screen_operate"),Function(time_forward, p), Return(None),Hide("info")]

transform uihelp_trans1:
    alpha 0.0
    0.2
    easein 1.0 alpha 1.0

transform uihelp_trans2:
    alpha 1.0
    easein 1.0 alpha 0.0