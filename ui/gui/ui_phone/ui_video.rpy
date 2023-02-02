screen screen_phone_video_address(player):
    #tag gamegui
    modal True
    style_prefix "gameUI"
    zorder 600
    

    frame:
        at trans_app(70, 50)
        background None
        xalign 0.5
        yalign 0.5
        ysize 750
        xsize 400

        add "gui/phone/address/address.png":
            xcenter 0.51
            ycenter 0.46

        frame:
            ypos 90
            background None
            vbox:
                spacing 2

                frame:
                    ysize 75
                    xfill True
                    background None
                    $sol_i = _('个人剧情')
                    $sol_a = _('《社畜福瑞重度头疼》')
                    imagebutton idle "gui/phone/address/Solitus.png":
                        action [Hide("info"),Hide("screen_phone_video_address"),Show(screen="screen_phone_video_show",who='solitus', player=player)]
                        hovered Show(screen="info", i=sol_i, a=sol_a)
                        unhovered Hide("info")  
                        background Frame("gui/style/white_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                        activate_sound audio.cursor
                        xfill True
                        yalign 0.5
                    textbutton "Solitus":
                        xpos 0.25
                        hover_sound audio.cursor
                        text_style "white"
                        yalign 0.5
                            
                null height 2
                if p.sol_p > 0 or Achievement400.has() or Achievement402.has():
                    frame:
                        ysize 75
                        xfill True
                        background None
                        $pa_i = _('和Pathos曾发生过的故事')
                        $pa_a = _('《从小白鼠到感情PUA》')
                        imagebutton idle "gui/phone/address/Pathos.png":
                            action [Hide("info"),Hide("screen_phone_video_address"),Show(screen="screen_phone_video_show",who='pathos', player=player)]
                            hovered Show(screen="info", i=pa_i, a=pa_a)
                            unhovered Hide("info")  
                            background Frame("gui/style/white_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            activate_sound audio.cursor
                            xfill True
                            yalign 0.5
                        textbutton "Pathos":
                            xpos 0.25
                            hover_sound audio.cursor
                            text_style "white"
                            yalign 0.5
                                
                    null height 2
                if p.aco_p > 0 or Achievement501.has():
                    frame:  
                        ysize 75
                        xfill True
                        background None
                        $aco_i = _('和Acolas曾发生过的故事')
                        $aco_a = _('《霸道总裁爱上我》')
                        imagebutton idle "gui/phone/address/Acolas.png":
                            action [Hide("info"),Hide("screen_phone_video_address"),Show(screen="screen_phone_video_show",who='acolas', player=player)]
                            hovered Show(screen="info", i=aco_i, a=aco_a)
                            unhovered Hide("info")  
                            background Frame("gui/style/white_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            activate_sound audio.cursor
                            xfill True
                            yalign 0.5
                        textbutton "Acolas":
                            xpos 0.25
                            hover_sound audio.cursor
                            text_style "white"
                            yalign 0.5

                    null height 2
                if p.hal_p > 0 or Achievement502.has():
                    frame:
                        ysize 75
                        xfill True
                        background None
                        $hal_i = _('和Halluke曾发生过的故事')
                        $hal_a = _('《社恐之间的交流》')
                        imagebutton idle "gui/phone/address/Halluke.png":
                            action [Hide("info"),Hide("screen_phone_video_address"),Show(screen="screen_phone_video_show",who='halluke', player=player)]
                            hovered Show(screen="info", i=hal_i, a=hal_a)
                            unhovered Hide("info")  
                            background Frame("gui/style/white_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            activate_sound audio.cursor
                            xfill True
                            yalign 0.5
                        textbutton "Halluke":
                            xpos 0.25
                            hover_sound audio.cursor
                            text_style "white"
                            yalign 0.5

                    null height 2

                if False:
                    frame:
                        ysize 75
                        xfill True
                        background None
                        $dep_i = _('和？？？曾发生过的故事\n（当前版本尚未开放）')
                        $dep_a = _('……')
                        imagebutton idle "gui/phone/address/Depline.png":
                            #action [Hide("info"),Hide("screen_phone_video_address"),Show(screen="screen_phone_video_show",who='depline', player=player)]
                            action NullAction()
                            hovered Show(screen="info", i=dep_i, a=dep_a)
                            unhovered Hide("info")  
                            background Frame("gui/style/white_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            activate_sound audio.cursor
                            xfill True
                            yalign 0.5
                        textbutton "？？？":
                            xpos 0.25
                            hover_sound audio.cursor
                            text_style "white"
                            yalign 0.5



        frame:
            background None
            xpos 0.8
            ypos 0.83
            imagebutton auto "gui/phone/back_%s.png":
                action [Hide("screen_phone_video_address"),Hide("info"),Show(screen="screen_phone", player=player)]
                hover_sound audio.cursor

    key 'K_ESCAPE' action [Hide("screen_phone_video_address"),Hide("info"),Show(screen="screen_phone", player=player)]



        
screen screen_phone_video_show(player, who='pathos'):

    default d_routes = {
        'pathos':[_('解锁第二种药物'), _('解锁第三种药物')],
        'halluke':[_('初次偷拍'),_('Halluke的能力展示'),_('厕所自慰'),_('初次留下印象'),_('自我怀疑'),
            _('初次开口'),_('周末约球'),_('特别的约会'),_('获得护膝'),_('粉丝店的思考'),'',
            _('体育馆的亲吻与诉苦'),_('对一切失去兴趣'),_('与Halluke的轮渡酒店之一'),_('与Halluke的轮渡酒店之二')],
        'acolas':[_('电梯偶遇'),_('性骚扰式自我介绍'),_('道歉与游戏项目'),_('火锅店与第一次项目'),_('结束第一次项目'),
        _('咖啡营地与第二次项目'),_('缺席会议的Acolas'),_('医院看望'),_('Acolas的公寓与结束第二次项目'),_('游戏发布与获得旧笔记'),
        _('Acolas的办公室'),_('报复性工作的Acolas'),_('与Acolas的轮渡酒店之一'),_('与Acolas的轮渡酒店之二')],
    }

    #tag gamegui
    modal True
    style_prefix "gameUI"
    zorder 600
    frame:
        at trans_Down()
        background None
        xalign 0.5
        yalign 0.5
        ysize 750
        xsize 430
        frame:
            background Frame("gui/style/white_hover_background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
            ypos 0.05
            xpos 0.05
            xsize 380
            text _("以下为已解锁的相关剧情：") style "white"

        frame:
            background None
    
            viewport:
                ypos 0.15
                ysize 530
                mousewheel True
                draggable True
                scrollbars "vertical"
                yinitial 0.01
                if who != 'solitus':
                    use screen_phone_videos(player, who, d_routes[who])
                else:
                    use screen_phone_videos_sol(player)
        

        frame:
            background None
            xpos 0.8
            ypos 0.83
            imagebutton auto "gui/phone/back_%s.png":
                action [Hide("screen_phone_video_show"),Hide("info"),Show(screen="screen_phone_video_address", player=player)]
                hover_sound audio.cursor

    key 'K_ESCAPE' action [Hide("screen_phone_video_show"),Hide("info"),Show(screen="screen_phone_video_address", player=player)]







screen video_slot(player, routename, labelname):
    frame:
        ysize 70
        xsize 340
        xpos 15
        background Frame("gui/style/transparent.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
        hbox:
            imagebutton idle "gui/phone/video.png":
                yalign 0.5
                xalign 0.05
                background Frame("gui/style/white_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)

            textbutton routename text_style "white":
                action [SetVariable("replaying", True), SetVariable("replaying_times", player.times), Hide("screen_phone_video_show"),Hide("screen_phone_bg"),Function(renpy.hide_screen,"screen_dashboard"), Jump(labelname)]
                background Frame("gui/style/white_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                xfill True
                yfill True
                activate_sound audio.cursor
            
    null height 2






screen screen_phone_videos(player, who, routes):
    frame:
        background None
        vbox:
            xsize 330
            for i in range(len(routes)): 
                $labelname = who + _('_route_') + str(i)
                if renpy.has_label(labelname):
                    if renpy.seen_label(labelname):
                        use video_slot(player, routes[i], labelname)
            null height 10
            textbutton ''


screen screen_phone_videos_sol(player):

    default routes = [_('第一天'), _('第二天'), _('第三天'), _('焦虑与疲倦'), _('咽喉的燃烧感'), _('以创作发泄焦虑'), _('梦醒时分'), _('劳累'), _('饥饿感'), _('关于自慰')]
    default endings = {
        Achievement100:[_('我已经站在你世界的\n顶端了'), 'ending0'], 
        Achievement101:[_('世间泰坦仅允我喘息'), 'ending1'], 
        Achievement102:[_('深陷其足下泥泞'), 'ending2'], 
        Achievement103:[_('肉与肉与肉与肉的豪\n华盛宴'), 'earthquakeBE'], 
        Achievement104:[_('不能重启的我们只能\n前进'), 'despairBE'], 
        Achievement105:[_('我们的神灵从未向这\n里看过一眼'), 'CuredBE'], 
        Achievement400:[_('为了能够让你学会如\n何去爱'), 'ne'], 
        Achievement401:[_('如果能成为你就好了'), 'te'], 
        Achievement402:[_('我已经一无所有'), 'CE']}

    frame:
        background None
        vbox:
            xsize 370

            for i in range(len(routes)): 
                $labelname = 'solitus_route_' + str(i)
                if renpy.has_label(labelname):
                    if renpy.seen_label(labelname):
                        use video_slot(player, routes[i], labelname)
            
            for i in list(endings.keys()): 
                if i.has():
                    use video_slot(player, endings[i][0], endings[i][1])
                        

            null height 10
            textbutton ''
