screen screen_journal(player):
    
    python:
        notes = ['note']

        if 'decaypics' in persistent.unlocked_items or config.developer:
            notes.append('note_dk')
        if 'pathospics' in persistent.unlocked_items or config.developer:
            notes.append('note_pa')

        if 'acolaspics' in persistent.unlocked_items or config.developer:
            notes.append('note_aco')

        if 'hallukepics' in persistent.unlocked_items or config.developer:
            notes.append('note_hal')
        if 'deplinepics' in persistent.unlocked_items or config.developer:
            notes.append('note_dep')
        if 'destotpics' in persistent.unlocked_items or config.developer:
            notes.append('note_des')
        if 'arnelpics' in persistent.unlocked_items or config.developer:
            notes.append('note_ar')

    default shownote = rcs(player, notes)

    #tag gamegui
    #modal True
    zorder 550
    frame:
        at trans_toRight()
        style "translucent_frame"
        background "images/gui/menu/note/%s.png" % shownote
        xsize 1000
        ysize 800
        xcenter 0.5
        ycenter 0.48
        vbox:
            frame:
                background None
                yalign 0.001
                textbutton '{size=+10}待办事项{/size}':
                    text_style "handwrite"
                    xoffset 5
                    yoffset -5
                    action NullAction()
                    text_size 50

                frame:
                    background None
                    ysize 680
                    xsize 980
                    xpos 10
                    ypos 90

                    use screen_journal_inner(player)
    button:
        xfill True
        yfill True
        action Hide("screen_journal",transition=dissolve)

    key 'K_ESCAPE' action [Hide("screen_journal",transition=dissolve),Hide("info")]



screen screen_journal_inner(player):
    
    vbox:

        

        text '{u}周五：{/u}' style 'handwrite'
        if player.today in (6, 7):
            text ' - {s}购买药物（外出→医院→二楼）' style 'handwrite'
        else:
            text ' - 购买药物（外出→医院→二楼）' style 'handwrite'
        if player.aco_p not in (7, 8, 12, 99) and player.experience != 'wri':
            if player.today in (6, 7) or (player.today == 5 and player.times>=9):
                text '    {u}下午：{/u}\n     - {s}参加公司的周研讨会（参与周研讨会）' style 'handwrite'
            else:
                text '    {u}下午：{/u}\n     - 参加公司的周研讨会（参与周研讨会）' style 'handwrite'
        
        
        text '\n{u}周六：{/u}' style 'handwrite'
        $nothing6 = True
        if player.aco_p == 12 and SteamerTicket.has(player):
            text ' - {color=#ff0000}和Acolas一起去游轮酒店{/color}' style 'handwrite'
        if player.hal_p == 13 and SteamerTicket.has(player):
            text ' - {color=#ff0000}和Halluke一起去游轮酒店{/color}' style 'handwrite'
        if player.aco_p == 7:
            if player.today == 7:
                text ' - {s}去医院探望Acolas（外出→医院→住院部）' style 'handwrite'
            else:
                text ' - 去医院探望Acolas（外出→医院→住院部）' style 'handwrite'
            $nothing6 = False
        if player.aco_p == 8:
            if player.today ==7 or (player.today == 6 and player.times>=9):
                text '    {u}下午：{/u}\n     - {s}去Acolas家里，地址是……XX小区XX单元……（去Acolas家）' style 'handwrite'
            else:
                text '    {u}下午：{/u}\n     - 去Acolas家里，地址是……XX小区XX单元……（去Acolas家）' style 'handwrite'
            $nothing6 = False
        if player.hal_p == 50:
            if player.today ==7 or (player.today == 6 and player.times>=9):
                text '    {u}下午：{/u}\n     - {s}去体育馆帮Halluke发球（羽毛球课程）' style 'handwrite'
            else:
                text '    {u}下午：{/u}\n     - 去体育馆帮Halluke发球（羽毛球课程）' style 'handwrite'
            $nothing6 = False
        if player.hal_p == 11:
            if player.today ==7 or (player.today == 6 and player.times>=9):
                text '    {u}下午：{/u}\n     - {s}去体育馆帮Halluke发球（羽毛球课程）' style 'handwrite'
            else:
                text '    {u}下午：{/u}\n     - 去体育馆帮Halluke发球（羽毛球课程）' style 'handwrite'
            $nothing6 = False
        if player.hal_p == 12:
            if player.today ==7 or (player.today == 6 and player.times>=9):
                text '    {u}下午：{/u}\n     - {s}去Halluke家里，地址是……XX小区XX单元……（去Halluke家）' style 'handwrite'
            else:
                text '    {u}下午：{/u}\n     - 去Halluke家里，地址是……XX小区XX单元……（去Halluke家）' style 'handwrite'
            $nothing6 = False
        
        if player.hal_p < 7:
            if player.today ==7 or (player.today == 6 and player.times>=9):
                text '    {u}下午：{/u}\n     - {s}去体育馆参加羽毛球课程（羽毛球课程）' style 'handwrite'
            else:
                text '    {u}下午：{/u}\n     - 去体育馆参加羽毛球课程（羽毛球课程）' style 'handwrite'
            if not BadmintonRacket.has(player):
                text '         - {color=#ff0000}需要购买新的羽毛球拍……（外出→商店街→文体商店）{/color}' style 'handwrite'
            $nothing6 = False

        if player.dep_p==7:
            if player.today ==7 and (player.today == 6 and player.times>=11):
                text '    {u}晚上：{/u}\n     - {s}和Depline庆祝生日（外出→商店街→宾馆）' style 'handwrite'
            else:
                text '    {u}晚上：{/u}\n     - 和Depline庆祝生日（外出→商店街→宾馆）' style 'handwrite'
            $nothing7 = False

        if nothing6:
            text '    暂无事项……' style 'handwrite'

        text '\n{u}周日：{/u}' style 'handwrite'
        $nothing7 = True
        if player.aco_p == 7:
            text ' - 去医院探望Acolas（外出→医院→住院部）' style 'handwrite'
            $nothing7 = False
        if player.dep_p == 2:
            if player.today ==7 and player.times>=5:
                text '    {u}上午：{/u}\n     - {s}去商场和赤松面基（和赤松面基）' style 'handwrite'
            else:
                text '    {u}上午：{/u}\n     - 去商场和赤松面基（和赤松面基）' style 'handwrite'
            $nothing7 = False
        if player.dep_p in (3, 4, 5, 6):
            if player.today ==7 and player.times>=5:
                text '    {u}上午：{/u}\n     - {s}和Depline一起出门（外出→商店街→宾馆）' style 'handwrite'
            else:
                text '    {u}上午：{/u}\n     - 和Depline一起出门（外出→商店街→宾馆）' style 'handwrite'
            $nothing7 = False
        
        if player.hal_p in (7, 8, 9):
            if player.today ==7 and player.times>=9:
                text '    {u}下午：{/u}\n     - {s}去体育馆陪Halluke打羽毛球（和Halluke打羽毛球）' style 'handwrite'
            else:
                text '    {u}下午：{/u}\n     - 去体育馆陪Halluke打羽毛球（和Halluke打羽毛球）' style 'handwrite'
            $nothing7 = False
        if player.des_p==4:
            if player.today ==7 and player.times>=9:
                text '    {u}下午：{/u}\n     - {s}去Destot家里，地址是……XX小区XX单元……（去Destot家）' style 'handwrite'
            else:
                text '    {u}下午：{/u}\n     - 去Destot家里，地址是……XX小区XX单元……（去Destot家）' style 'handwrite'
            $nothing6 = False
        if player.des_p==2:
            if player.today ==7 and player.times>=11:
                text '    {u}晚上：{/u}\n     - {s}和Destot一起出门（和Destot外出）' style 'handwrite'
            else:
                text '    {u}晚上：{/u}\n     - 和Destot一起出门（和Destot外出）' style 'handwrite'
            $nothing7 = False
        
        
        if nothing7:
            text '    暂无事项……' style 'handwrite'
        

        
        $others = [
            WriterItem1.has(player), 
            any([x.has(player) for x in (AcolasItem2, AcolasItem3, AcolasItem4)]), 
            player.hal_p in (12, 13), 
            player.dep_p == 9, 
            player.dep_p == 10,
        ]
        if any(others):
            text '\n其他：' style 'handwrite'
        if others[0]:
            text ' - 完成小说（撰写小说）' style 'handwrite'
        if others[1]:
            text ' - 帮Acolas做他的游戏项目（完成Acolas的项目）' style 'handwrite'
        if others[2]:
            text ' - 保持Halluke情绪稳定……（小心地回复消息）' style 'handwrite'
        if others[3]:
            text ' - Depline去了哪里……' style 'handwrite'
        if others[4]:
            text ' - 阿斯卡隆书店要倒闭了……' style 'handwrite'

        text '\n治疗进度：' style 'handwrite'
        if player.sol_p == 0:
            if player.week >= 4:
                text '    {color=#3fff05}{u}这周五：{/u}{/color}\n     - 去找Pathos医生复诊（外出→医院→四楼）' style 'handwrite'
            else:
                text '    {u}第四周后的周五：{/u}\n     - 去找Pathos医生复诊（外出→医院→四楼）' style 'handwrite'
                
        elif player.sol_p in (1, 2):
            if player.week >= 8:
                text '    {color=#3fff05}{u}这周五：{/u}{/color}\n     - 去找Pathos医生复诊（外出→医院→四楼）' style 'handwrite'
            else:
                text '    {u}第八周后的周五：{/u}\n     - 去找Pathos医生复诊（外出→医院→四楼）' style 'handwrite'

        elif player.sol_p in (3, 4):
            if player.week >= 12:
                text '    {color=#3fff05}{u}这周五：{/u}{/color}\n     - 去找Pathos医生复诊（外出→医院→四楼）' style 'handwrite'
            else:
                text '    {u}第十二周后的周五：{/u}\n     - 去找Pathos医生复诊（外出→医院→四楼）' style 'handwrite'
        else:
            text ' - 等待手术通知……' style 'handwrite'