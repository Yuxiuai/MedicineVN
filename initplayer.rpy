screen screen_initplayer(player):
    #modal True
    zorder 200
    drag:
        xcenter 0.503
        ycenter 0.48
        frame:
            at trans_toRight()
            style "translucent_frame"
            xsize 1200
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
                            textbutton '{size=+10}创建人物{/size}':
                                xoffset -15
                                yoffset -10
                                text_style "gameUI"                                      
                    frame:
                        #xoffset -10
                        background None
                        ysize 500
                        xsize 380
                        ypos 60
                        xpos 10
                        use player_show(player)
                        
                        

                frame:
                    background None
                    xsize 400
                    ysize 800

                    
                    
                    frame:
                        background None
                        textbutton '{size=+10}所持金钱：%s{/size}' % player.money:
                            xoffset -25
                            yoffset -10
                            text_style "gameUI" 
                    
                    frame:
                        background None
                        ysize 660
                        xsize 400
                        ypos 60
                        xpos -15
                        viewport:
                            mousewheel True
                            draggable True
                            scrollbars "vertical"
                            use shop_show(player)

                frame:
                    background None
                    xsize 400
                    ysize 800
                    
                    frame:
                        background None
                        textbutton '{size=+10}已有道具{/size}':
                            xoffset -25
                            yoffset -10
                            text_style "gameUI" 

                        imagebutton idle 'gui/help.png':
                            action Show(screen='info_use', i=_('这是一个加点界面，初次进行游戏或者对这个功能不感兴趣的，可以直接点击下方的开始游戏，对游戏并无太大影响。\n\n这个界面允许你随意调整默认的初始道具，以及角色的初始点数，你可以在左下角免费重随基础能力点数、花50元购得1点基础能力点数、在右侧花钱购买道具，或是卖出你不需要的初始道具。\n这里的道具比外面要稍微贵一些，购买时请考虑清除自己是否急需。\n\n{color=#ff0000}你不应该在这里花光你的所有钱，除非你知道自己在做什么！{/color}'))
                            hovered Show(screen='info', i=_('帮助'), a='点击查看有关该界面的介绍。')
                            unhovered Hide('info')
                            
                            activate_sound audio.cursor
                            xalign 0.95
                            yalign 0.0
                            yoffset -5
                    
                    frame:
                        background None
                        ysize 660
                        xsize 400
                        ypos 60
                        xpos -15
                        viewport:
                            mousewheel True
                            draggable True
                            scrollbars "vertical"
                            use inventory_show(player)

            frame:
                #xoffset -10
                background None
                ysize 40

            if player.money >= 0:
                textbutton '{size=+5}开始游戏{/size}' text_style "white":    
                    action [Hide("screen_initplayer",transition=dissolve),Hide("info"),Hide("info3"),Return()]
                    activate_sound audio.cursor  
                    idle_background None
                    hover_background Frame("gui/style/grey_hover_background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                    xfill True
                    text_xalign 0.5
                    xalign 0.5
                    yalign 0.98
            else:
                textbutton '{size=+5}你的钱不够{/size}' text_style "white":    
                    action NullAction()
                    activate_sound audio.error
                    xfill True
                    text_xalign 0.5
                    xalign 0.5
                    yalign 0.98




define initplayer_goods = {

        DrugIbuprofen: 10.0,
        DrugColdrex: 30.0,
        DrugHypnotic: 20.0,

        Cola: 80.0,
        StreetFood9: 45.0,
        StreetFood10: 45.0,
        SexyPic: 50.0,

        BookDefault: 180.0,
        AMaverickLion: 180.0,
        BookWri: 180.0,
        BookPhysPun: 180.0,
        BookWor: 180.0,

        ProfessionalBookWorking: 90.0,
        ProfessionalBookWriting: 90.0,
        ProfessionalBookSeverity: 90.0,
        
    }

screen shop_show(player):

    python:
        def buy(player, item, money):
            player.money -= money
            item.add(player)


    vbox:
        
        for item in sorted(initplayer_goods.keys(), key=lambda x: initplayer_goods[x]):
            if item.isUnique and not item.has(player) or not item.isUnique:
                frame:
                    background None
                    #ysize 60
                    xsize 370

                    frame:
                        background None
                        ysize 40

                        $ite_name = item.name
                        $ite_main = item.info
                        $ite_ad = item.ad
                        if ite_ad is None:
                            $ite_ad = ''

                        textbutton item.name text_style "white":
                            background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            if renpy.variant("pc"):
                                action [Hide("info"),Function(buy, player, item, initplayer_goods[item])]
                            else:
                                action [Hide("info"),Show(screen="info_confirm", act=Function(buy, player, item, initplayer_goods[item]) ,text='购入', pp=renpy.get_mouse_pos(), t=ite_name, i=ite_main, a=ite_ad)]
                            hovered [Show(screen="info", t=ite_name, i=ite_main, a=ite_ad)]
                            unhovered Hide("info")
                            xsize 370
                            text_size 20
                            activate_sound audio.cursor
                        
                        textbutton '￥%s' % str(initplayer_goods[item]) text_style "white":
                            action NullAction()
                            text_size 20
                            xalign 0.9
                            


screen inventory_show(player):

    python:
        def withdraw(player, item, money):
            player.money += money
            item.sub(player)


    vbox:
        
        for item in player.items:
            frame:
                background None
                #ysize 60
                xsize 370

                frame:
                    background None
                    ysize 40

                    $ite_name = item.name
                    $ite_main = item.info
                    $ite_ad = item.ad
                    if ite_ad is None:
                        $ite_ad = ''
                        
                    textbutton item.name text_style "white":
                        background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                        if renpy.variant("pc"):
                            action [Hide("info"),Function(withdraw, player, item, initplayer_goods[type(item)])]
                        else:
                            action [Hide("info"),Show(screen="info_confirm", act=Function(withdraw, player, item, initplayer_goods[type(item)]) ,text='卖出', pp=renpy.get_mouse_pos(), t=ite_name, i=ite_main, a=ite_ad)]
                        hovered [Show(screen="info", t=ite_name, i=ite_main, a=ite_ad)]
                        unhovered Hide("info")
                                    
                                    
                        xsize 370
                        text_size 20
                        activate_sound audio.cursor
                    
                    textbutton str(item.amounts) text_style "white":
                        action NullAction()
                        text_size 20
                        xalign 0.9



screen player_show(player):
    default point = 0
    python:
        def random_ability(player, point):
            player.working = rd(90, 110) * 0.01
            player.physical = rd(90, 110) * 0.01
            player.writing = rd(90, 110) * 0.01
            player.severity = rd(90, 110) * 0.01
            player.money += point * 50

        def buy_ability(player, ability, mode='+'):
            if mode == '+':
                setattr(player, ability, getattr(player, ability)+0.01)
            else:
                setattr(player, ability, getattr(player, ability)-0.01)
            player.money -= 50

        def extra_points(player):
            return int(int(player.working*100) + int(player.physical*100) + int(player.writing*100) - int(player.severity*100) - 200)

    vbox:
        xsize 460

        frame:
            background None
            ysize 100
            xsize 330
            frame:
                background None
                textbutton '{size=+10}%s{/size}      {size=-5}\n选择游戏难度：{/size}' % (player.name) text_style "white":
                    action NullAction()
                    xsize 330
                     
            null height 2


        frame:
            background None
            ysize 50
            xsize 300
            xoffset 10
            textbutton _("简单") text_style 'white':
                action [Function(GameDifficulty1.add, player),Hide("diff_select"),Hide('info')]
                hovered Show(screen='info', i=_('游戏难度：简单\n\n勾选此项后，将游戏难度设置为简单。\n在此难度下，大幅度降低精神状态的消耗，并大幅度提高精神状态的恢复。\n同时，允许随意改变日程，可以直接阅读书籍，不会获得酸痛和药物依赖效果，灵感将在一天结束后自动转化为写作素材。'),width=600)
                unhovered Hide('info')
                background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor
            if GameDifficulty1.has(player):
                imagebutton idle "gui/right_.png":
                    xalign 1.0
                    yalign 0.5

        frame:
            background None
            ysize 50
            xsize 300
            xoffset 10
            textbutton _("一般") text_style 'white':
                action [Function(GameDifficulty3.add, player),Hide("diff_select"),Hide('info')]
                hovered Show(screen='info', i=_('游戏难度：一般\n\n勾选此项后，将游戏难度设置为一般。'),width=600)
                unhovered Hide('info')
                background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor
            if GameDifficulty3.has(player):
                imagebutton idle "gui/right_.png":
                    xalign 1.0
                    yalign 0.5

        frame:
            background None
            ysize 50
            xsize 300
            xoffset 10
            textbutton _("硬核") text_style 'white':
                action [Function(GameDifficulty5.add, player),Hide("diff_select"),Hide('info')]
                hovered Show(screen='info', i=_('游戏难度：硬核\n\n勾选此项后，将游戏难度设置为硬核。\n在此难度下，提升更多精神状态的消耗，睡眠消耗的精神状态并降低精神状态的恢复。'),width=600)
                unhovered Hide('info')
                background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                xfill True
                activate_sound audio.cursor
            if GameDifficulty5.has(player):
                imagebutton idle "gui/right_.png":
                    xalign 1.0
                    yalign 0.5

        null height 20

        frame:
            background None
            ysize 60
            xsize 330
            frame:
                background None
                textbutton '额外随机点数：%s\n付费属性点数：%s' % (extra_points(player)-point, point) text_style "white":
                    action NullAction()
                    xsize 330

                imagebutton auto 'gui/rand_%s.png':
                    action Function(random_ability, player, point), SetLocalVariable("point", 0)
                    hovered Show(screen='info', i='进行一次随机分配属性，并重置购点花费的金钱。')
                    unhovered Hide('info')
                    
                    activate_sound audio.cursor
                    xalign 1.0
                    yoffset 10
                     
            null height 2

        null height 30

        frame:
            background None
            ysize 60
            xsize 330
            frame:
                background None
                textbutton '严重程度：%s' % player.severity text_style "white":
                    action NullAction()
                    xsize 330
                    yalign 0.5
                                     
            null height 2

        frame:
            background None
            ysize 60
            xsize 330
            frame:
                background None
                textbutton '工作能力：%s' % player.working text_style "white":
                    action NullAction()
                    xsize 330
                    yalign 0.5
                
                imagebutton idle "images/gui/add_w.png":
                    action Function(buy_ability, player, 'working'), SetLocalVariable("point", point+1), Hide('info')
                    hovered Show(screen='info', i='花费50元获得1点工作能力。\n\n工作能力能够提升工作完成的工作量以及工作时的专注度。\n\n{color=#FF4500}工作能力较低时无法完成每周的工作任务。{/color}')
                    unhovered Hide('info')
                    activate_sound audio.cursor
                    xalign 1.0

                     
            null height 2

        
        frame:
            background None
            ysize 60
            xsize 330
            frame:
                background None
                textbutton '身体素质：%s' % player.physical text_style "white":
                    action NullAction()
                    xsize 330
                    yalign 0.5
                
                imagebutton idle "images/gui/add_w.png":
                    action Function(buy_ability, player, 'physical'), SetLocalVariable("point", point+1), Hide('info')
                    hovered Show(screen='info', i='花费50元获得1点身体素质。\n\n身体素质能对所有精神状态相关的数值造成正面影响，也会降低睡眠消耗的精神状态。\n\n{color=#FF4500}身体素质较低时难以在游戏中存活。{/color}')
                    unhovered Hide('info')
                    activate_sound audio.cursor
                    xalign 1.0

                     
            null height 2

        frame:
            background None
            ysize 60
            xsize 330
            frame:
                background None
                textbutton '写作技巧：%s' % player.writing text_style "white":
                    action NullAction()
                    xsize 330
                    yalign 0.5
                
                imagebutton idle "images/gui/add_w.png":
                    action Function(buy_ability, player, 'writing'), SetLocalVariable("point", point+1), Hide('info')
                    hovered Show(screen='info', i='花费50元获得1点写作技巧。\n\n写作技巧能对日程的整体专注度造成正面影响，满足需要更高水平的委托的要求，提升委托文稿的价值。\n\n{color=#FF4500}写作技巧较低时进行日程将会获得较差的结果。{/color}')
                    unhovered Hide('info')
                    activate_sound audio.cursor
                    xalign 1.0

            null height 2

        null height 40

