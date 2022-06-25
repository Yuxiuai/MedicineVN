screen screen_index(player):
    #tag gamegui
    hbox:
        xpos 0.05
        ypos 0.85

        spacing 50
    
        imagebutton auto "gui/menu/phone_%s.png":
            at trans_Up()
            action [Show("screen_phone_bg"),Show(screen="screen_phone", player=player), Hide("info")]
            hovered Show(screen="info", i='打开手机。\n你可以用它来进行不需要消耗回合的事件，打电话给你喜欢的人，中午的时候点个外卖，或是在手机的接稿平台上查看每日更新的委托。', a='“真的有不用手机刷短视频和玩手游的人吗？”……\n没错，就是在下。')
            unhovered Hide("info")
            hover_sound audio.cursor
        if player.times == 2:
            imagebutton auto "gui/menu/schedule_%s.png":
                at trans_Up()
                action [Show(screen="screen_tasks", player=player), Hide("info")]
                hovered Show(screen="info", i='安排日程\n安排你接下来一整天要做的事，没有全部安排完则无法进行到下一时间段。', a='可以忍受上司的批评，但是不能忍受突发事件导致的日程计划修改！')
                unhovered Hide("info")
                hover_sound audio.cursor 
        imagebutton auto "gui/menu/box_%s.png":
            at trans_Up()
            action [Show(screen="screen_items", player=player), Hide("info")]
            hovered Show(screen="info", i='所持物品\n检查你所持有的物品，使用或是丢弃。', a='虽然能看到很多东西但这并不代表我会把所有的东西都随身携带着！总之你懂就好……')
            unhovered Hide("info")
            hover_sound audio.cursor
        imagebutton auto "gui/menu/effinfo_%s.png":
            at trans_Up()
            action [Show(screen="screen_effects", player=player), Hide("info")]
            hovered Show(screen="info", i='角色效果\n检查你此时拥有的各种效果和详细信息。', a='呵呵，不看BUFF就让我狂上班的人连第一周都活不过去。')
            unhovered Hide("info")
            hover_sound audio.cursor
        imagebutton auto "gui/menu/settings_%s.png":
            at trans_Up()
            action [ShowMenu(screen='preferences',player=player), Hide("info")]
            hovered Show(screen="info", i='设置\n可以在此处选择重新开始这一天，回到昨天或是回到上一周。', a='30xx年可以已经可以穿越时空了……于是我们……\n噢，等等，我们的游戏背景才发展到21世纪吗！？')
            unhovered Hide("info")
            hover_sound audio.cursor

    hbox:
        xpos 0.9
        ypos 0.725
        imagebutton auto "gui/menu/explore_%s.png":
            at trans_toLeft()
            action Show(screen="screen_map", player=player, transition=dissolve)
            hovered Show(screen="info", i='地图\n检查A市你所居住的城区地图。', a='到达世界最高城A市！太美丽了A市……\n哎呀这不于老师吗？\n再看看远处的社畜沙漠狼吧家人们……')
            unhovered Hide("info")
            hover_sound audio.cursor

    hbox:
        xpos 0.9
        ypos 0.85
        if p.hal_p == 11 and player.messages['Halluke'][-1].seen != None:
            imagebutton auto "gui/menu/edit_%s.png":
                at trans_toLeft()
                action Function(showNotify, ['还没有给Halluke发消息。'])
                hovered Show(screen="info", i='还没有给Halluke发消息。')
                unhovered Hide("info")
                activate_sound audio.error

        elif NoTask in player.plan:
            imagebutton auto "gui/menu/edit_%s.png":
                at trans_toLeft()
                action Function(showNotify, ['还未完成日程的安排！'])
                hovered Show(screen="info", i='尚未安排完本日的日程\n点击左下方第二个图标安排你的本日日程。', a='说真的，就不能给我一点单纯发呆的时间吗？')
                unhovered Hide("info")
                activate_sound audio.error

        else:
            imagebutton auto "gui/menu/done_%s.png":
                at trans_toLeft()
                action [Hide("screen_index"),Return(None),Hide("info")]
                hovered Show(screen="info", i='已安排完日程\n点击图标结束规划并开始按照顺序完成日程。', a='可能日程表对我来说就是有种魔力吧，写在上面的东西就必须一点一点地完成……')
                unhovered Hide("info")
                activate_sound audio.cursor
    
    key 'q' action [Show("screen_phone_bg"),Show(screen="screen_phone", player=player), Hide("info")]
    if player.times == 2:
        key 'w' action [Show(screen="screen_tasks", player=player), Hide("info")]
    key 'e' action [Show(screen="screen_items", player=player), Hide("info")]
    key 'r' action [Show(screen="screen_effects", player=player), Hide("info")]
    
    if NoTask in player.plan:
        key 'K_SPACE' action Function(showNotify, ['还未完成日程的安排！'])
    else:
        key 'K_SPACE' action [Hide("screen_index"),Return(None),Hide("info")]