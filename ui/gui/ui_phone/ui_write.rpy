screen screen_phone_write(player):

    default page = 0
    predict False
    style_prefix "gameUI"
    zorder 600
    
    python:
        def getheight(comm):
            h = 110
            if comm.needWord == -1 and comm.needInspiration == -1 and comm.du == -1:
                return 135
            else:
                if comm.needWord != -1 :
                    h+=25
                if comm.needInspiration != -1 :
                    h+=25
                if comm.du != -1 :
                    h+=25
            return h

    frame:
        
        if phone_page == 7:
            at app_inner_show(-110, 50)
        else:
            at app_inner_hide(-110, 50)

        
        background None
        xcenter 0.5
        ycenter 0.5
        yoffset -10
        
        use barrier('', 0)

        add "gui/phone/wallpaper/message.webp":
            xcenter 0.5

        if page == 0:
            text "接取文稿" xpos 0.92 xanchor 1.0 ypos 0.085 size 40 style "foodname"

        elif page == 1:
            text "交付文稿" xpos 0.92 xanchor 1.0 ypos 0.085 size 40 style "foodname"

        elif page == 2:
            add "gui/phone/book.jpg" xoffset -11

        elif page == 3:
            text "帮助" xpos 0.92 xanchor 1.0 ypos 0.085 size 40 style "foodname"

            

        frame:
            
            background None
            xalign 0.5
            yalign 0.55
            ysize 1300
            xsize 582
        

            frame:
                ypos 150
                background None
                
                if page == 0:
                    frame:
                        background None
                        
                        vbox:
                            text "以下是今日向您推荐的委托：" style 'foodname' size 25 color "#383838"
                            frame:
                                background None
                                ypos 0.015
                                viewport:
                                    ysize 650
                                    xsize 550
                                    mousewheel True
                                    draggable True
                                    vbox:
                                        spacing 2
                                        for i in player.unacComm:
                                            hbox:
                                                $ys = getheight(i)
                                                frame:
                                                    background Frame("#f3af70")
                                                    xsize 460
                                                    ysize ys
                                                    vbox:
                                                        

                                                        text i.name:
                                                            style 'phonew'
                                                            size 30
                                                            
                                                        text "水平需求：" + str(i.require):
                                                            style 'phonew'
                                                            if i.require > player.writing_grade():
                                                                color "#ff2525"

                                                        text "提出价格：" + str(i.require*100*i.priceFluctuation) + "/千字":
                                                            style 'phonew'

                                                        text "需求：" style 'phonew'
                                                        if i.needWord == -1 and i.needInspiration == -1 and i.du == -1:
                                                            text " · 无需求" style 'phonew'
                                                        else:
                                                            if i.needWord != -1 :
                                                                text " · 字数需求：" + str(i.needWord) style 'phonew'
                                                            if i.needInspiration != -1 :
                                                                text " · 灵感需求：" + str(i.needInspiration) style 'phonew'
                                                            if i.du != -1 :
                                                                text " · 时间需求：" + str(i.du) style 'phonew'
                                                                

                                                frame:
                                                    yfill True
                                                    xsize 80
                                                    ysize ys
                                                    background Frame("#f3af70")
                                                    
                                                    
                                                    textbutton "×":
                                                        action Function(player.unacComm.remove, i), Function(showNotice, ["已删除委托：%s！"%i.name])
                                                        ysize ys/2
                                                        xfill True
                                                        at app_transform
                                                        yalign 0.0
                                                        background Frame("#e27919")
                                                        text_style 'phonew'
                                                        text_xalign 0.5
                                                        text_size 50
                                                        activate_sound audio.card1
                                                    
                                                    textbutton "+":
                                                        action Hide("info"),Function(player.receiveComm, comm=i), Function(showNotice, ["已接取委托：%s！"%i.name])
                                                        ysize ys/2-5
                                                        xfill True
                                                        at app_transform
                                                        yalign 1.0
                                                        background Frame("#e27919")
                                                        text_style 'phonew'
                                                        text_xalign 0.5
                                                        text_size 50
                                                        activate_sound audio.card2
                                        null height 100       

                        if persistent.sponsor or config.developer:
                            imagebutton auto "images/gui/reset_b_%s.png" action Function(player.refreshUnacComm) xalign 0.975
                                                    


                if page == 1:
                    frame:
                        background None
                        $ comms = list(filter(lambda x: type(x)==UnfinishedCommission or type(x)==FinishedCommission, player.items))
                        vbox:
                            if not comms:
                                text "您还没有接取任何委托。\n请先在接稿侧接取委托吧！" style 'foodname' size 25 color "#383838"
                            else:
                                text "以下是您已接取的委托：" style 'foodname' size 25 color "#383838"
                                frame:
                                    background None
                                    ypos 0.05
                                    viewport:
                                        ysize 650
                                        xsize 550
                                        mousewheel True
                                        draggable True
                                        vbox:
                                            spacing 2
                                            for i in comms:
                                                

                                                hbox:
                                                    $ys = getheight(i.comm)
                                                    if i.comm.freewheeling:
                                                        $ys = 15
                                                    frame:
                                                        background Frame("#f3af70")
                                                        xsize 460
                                                        ysize ys+110
                                                        vbox:
                                                            $price = i.comm.require*100*i.comm.priceFluctuation

                                                            text i.comm.name:
                                                                style 'phonew'
                                                                size 30
                                                                
                                                            if not i.comm.freewheeling:
                                                                text "水平需求：" + str(i.comm.require):
                                                                    style 'phonew'
                                                                    if i.comm.require > player.writing_grade():
                                                                        color "#ff2525"

                                                                text "提出价格：" + str(price) + "/千字":
                                                                    style 'phonew'

                                                                text "需求：" style 'phonew'
                                                                if i.comm.needWord == -1 and i.comm.needInspiration == -1 and i.comm.du == -1:
                                                                    text " · 无需求" style 'phonew'
                                                                else:
                                                                    if i.comm.needWord != -1 :
                                                                        text " · 字数需求：" + str(i.comm.needWord) style 'phonew'
                                                                    if i.comm.needInspiration != -1 :
                                                                        text " · 灵感需求：" + str(i.comm.needInspiration) style 'phonew'
                                                                    if i.comm.du != -1 :
                                                                        text " · 时间需求：" + str(i.comm.du) style 'phonew'

                                                            $cInfo = i.comm.contentInfo()
                                                            null height 10
                                                            text " > 平均写作技巧：" + str(cInfo[3]) style 'phonew'
                                                            text " > 已完成字数：" + str(cInfo[0]) style 'phonew'
                                                            if not i.comm.freewheeling:
                                                                text " > 文稿总价值：" + str(cInfo[1]) style 'phonew'
                                                            text " > 共消耗灵感：" + str(cInfo[2]) style 'phonew'
                                                            


                                                    frame:
                                                        yfill True
                                                        xsize 80
                                                        ysize ys+110
                                                        background Frame("#f3af70")
                                                        
                                                        
                                                        textbutton "×":
                                                            action Function(ui_itemQuit, item=i, player=player)
                                                            ysize ys/2+55
                                                            xfill True
                                                            at app_transform
                                                            yalign 0.0
                                                            background Frame("#e27919")
                                                            text_style 'phonew'
                                                            text_xalign 0.5
                                                            text_size 50
                                                            activate_sound audio.card1
                                                        
                                                        textbutton ">":
                                                            if type(i) == FinishedCommission:
                                                                if i.comm.freewheeling:
                                                                    action [Hide("comm_use"), Function(i.uploadToSocial, player=player)]
                                                                else:
                                                                    action [Hide("comm_use"), Function(i.getReward, player=player)]
                                                            else:
                                                                action Function(showNotice, ["委托还未完成！"])
                                                            ysize ys/2+45
                                                            xfill True
                                                            at app_transform
                                                            yalign 1.0
                                                            background Frame("#e27919")
                                                            text_style 'phonew'
                                                            text_xalign 0.5
                                                            text_size 50
                                                            activate_sound audio.card2
                                            null height 100  




                if page == 2:
                    frame:
                        background None
                        
                        frame:
                            background None
                            yalign 0.0
                            xanchor 1.0
                            xpos 0.98
                            yoffset -20
                            hbox:
                                spacing 10
                                text 'Solitus' style 'foodname' size 40 yalign 1.0
                                add "gui/phone/message/Solitus.png"

                        frame:
                            background None
                            yalign 0.1
                            $recentWri = 1.0
                            if player.recentCommWri:
                                $recentWri = sum(player.recentCommWri)*1.0/len(player.recentCommWri)

                            $recentIns = 10
                            if player.recentCommIns:
                                $recentIns = sum(player.recentCommIns)*1.0/len(player.recentCommIns)
                            
                            if recentIns < 10*recentWri:
                                $insbonus = recentIns - 50*recentWri
                            else:
                                $insbonus = recentIns - 10*recentWri
                            vbox:
                                null height 10
                                if len(player.recentCommWri) < 3:
                                    text '写作水平评价：' + '1.0' style 'phonew' size 40 color "#e27919"
                                    null height 10
                                    text '请再交稿' + str(3-len(player.recentCommWri)) +'篇以解锁更多评价。' style 'phonew' size 25 color "#383838"

                                else:
                                    null height 10
                                    text '写作水平评价：' + str(player.writing_grade()) style 'phonew' size 40 color "#e27919"
                                    null height 10
                                    text ' · 平均消耗灵感：' + r2s(recentIns) style 'phonew' size 30 color "#383838"
                                    text ' · 最低灵感阈值：' + r2s(10*recentWri) style 'phonew' size 30 color "#383838"
                                    if insbonus <= 0:
                                        $insbonus = '{color=#f00}0%{/color}'
                                    else:
                                        $insbonus = r2s(insbonus) + '%'
                                    text '    · 提升委托价格：+' + insbonus style 'phonew' size 30 color "#383838"
                                    text ' · 平台人气：' + str(player.popularity) style 'phonew' size 30 color "#383838"
                                    text '    · 提升委托价格：+' + r2s(player.popularity*1.0 / 1000) + '%' style 'phonew' size 30 color "#383838"
                                    text ' · 名誉分：' + str(player.writing_honor) style 'phonew' size 30 color "#383838"
                                    text '    · 影响委托价格：*' + str(max(player.writing_honor,10)) + '%' style 'phonew' size 30 color "#383838"
                                    null height 20
                                    $vb = player.writing_valuebouns()*100
                                    if vb == 0:
                                        $vb = '{color=#f00}'+str(vb)+'%{/color}'
                                    else:
                                        $vb = str(vb) + '%'
                                    text ' · 共计提升价格倍率：+' + vb style 'phonew' size 30 color "#e27919"

                                
                                vbox:
                                    null height 20
                                    text ' - 交付的委托数：' + str(player.doneComm) style 'phonew' size 30 color "#383838"
                                    text ' - 交付的随笔数：' + str(player.doneFree) style 'phonew' size 30 color "#383838"
                                    text ' - 委托总收入：' + str(player.gainCommPrice) style 'phonew' size 30 color "#383838"
                                    text ' - 打赏总收入：' + str(player.gainPopuPrice) style 'phonew' size 30 color "#383838"
                
                if page == 3:
                    frame:
                        background None
                        

                        frame:
                            background None
                            viewport:
                                ysize 700
                                xsize 550
                                mousewheel True
                                draggable True

                                vbox:
                                    text '什么是写作？' style 'phonew' size 25 color "#e27919"
                                    text ' - 写作可以为你带来大量的额外收入，而你只需要消耗平时无处释放的灵感即可。' style 'phonew' size 20 color "#383838"
                                    text '怎么写作？' style 'phonew' size 25 color "#e27919"
                                    text ' - 在左侧的接稿选项中挑选合适的委托，你可以观察报价来选择最高的委托，但要注意其需求。\n在接完稿后，选择一个时间段进行完成委托日程，即可进行委托的写作，一般来说一个日程就能达到字数要求，但有时候不能，再次对同一个委托进行完成委托日程即可。' style 'phonew' size 20 color "#383838"
                                    text '随笔写作是什么？' style 'phonew' size 25 color "#e27919"
                                    text ' - 你可以不接稿来写作，同样消耗灵感，以及一些特殊的状态，你可以在随笔写作日程中查看具体的状态。\n如果找不到这个日程，说明你暂时没有达到可以进行的要求，选择查看所有日程再寻找。\n但随笔写作的文稿在交稿后只能获得新的粉丝，粉丝越多，你收到的委托越多，报价越高。\n粉丝还会偶尔打赏你，粉丝越多，打赏的概率越高，金额越多。' style 'phonew' size 20 color "#383838"
                                    text '什么是写作水平评价？' style 'phonew' size 25 color "#e27919"
                                    text ' - 即最近三次交付的委托写作时你的写作技巧属性的平均值，你大概率会收到以这个评价为基准的水平需求的写作委托。' style 'phonew' size 20 color "#383838"
                                    text '如果我的写作水平评价低于委托的需求，可以接稿吗？' style 'phonew' size 25 color "#e27919"
                                    text ' - 可以，但如果在交稿时，写作委托时写作技巧低于需求，则会降低名誉分和收到的报酬。' style 'phonew' size 20 color "#383838"
                                    text '灵感的作用？' style 'phonew' size 25 color "#e27919"
                                    text ' - 交付委托时灵感越高则接下来受到的委托的报价会更高，除此之外有些委托还需要你达到灵感标准，如果消耗的灵感低于最低灵感阈值，则报价会大幅下降。' style 'phonew' size 20 color "#383838"
                                    text '名誉分是什么？' style 'phonew' size 25 color "#e27919"
                                    text ' - 交付委托时，写作文稿时你的写作技巧低于文稿的需求或进行限时委托但超时都会扣除名誉分，名誉分越低，委托报价越低。\n名誉分没有下限，但最低会让你的委托报价变为正常的10%。\n正常交付委托会恢复10点名誉分。' style 'phonew' size 20 color "#383838"
                                    



            hbox:
                ypos 0.7
                spacing 5
                xalign 0.5

                textbutton "接稿":
                    action SetLocalVariable('page', 0)
                    if page == 0:
                        background Frame("#f3af70")
                        activate_sound audio.error
                    else:
                        background Frame("#e27919")
                        at app_transform
                        activate_sound audio.click1
                    xsize 135
                    text_xalign 0.5
                    text_style "phonew"
                    text_size 35
                    

                textbutton "交稿":

                    action SetLocalVariable('page', 1)
                    if page == 1:
                        background Frame("#f3af70")
                        activate_sound audio.error
                    else:
                        background Frame("#e27919")
                        at app_transform
                        activate_sound audio.click1
                    xsize 135
                    text_xalign 0.5
                    text_style "phonew"
                    text_size 35

                textbutton "个人":
                    action SetLocalVariable('page', 2)
                    if page == 2:
                        background Frame("#f3af70")
                        activate_sound audio.error
                    else:
                        background Frame("#e27919")
                        at app_transform
                        activate_sound audio.click1
                    xsize 135
                    text_xalign 0.5
                    text_style "phonew"
                    text_size 35
            
                textbutton "帮助":
                    action SetLocalVariable('page', 3)
                    if page == 3:
                        background Frame("#f3af70")
                        activate_sound audio.error
                    else:
                        background Frame("#e27919")
                        at app_transform
                        activate_sound audio.click1
                    xsize 135
                    text_xalign 0.5
                    text_style "phonew"
                    text_size 35
                    
            frame:
                background None
                xpos 0.03
                ypos 0.06
                imagebutton auto "gui/phone/backw_%s.png":
                    action SetVariable("phone_page", 0), Hide("info")
                    hover_sound audio.cursor
            

                
    
    key 'K_ESCAPE' action SetVariable("phone_page", 0), Hide("info")