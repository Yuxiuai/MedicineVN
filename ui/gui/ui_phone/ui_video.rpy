screen screen_phone_video_address(player):
    #tag gamegui
    modal True
    style_prefix "gameUI"
    zorder 100
    

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
                    $sol_i = '个人剧情'
                    $sol_a = '《社畜福瑞重度头疼》'
                    imagebutton idle "gui/phone/address/Solitus.png":
                        action [Hide("info"),Hide("screen_phone_video_address"),Show(screen="screen_phone_video_show",who='solitus', player=player)]
                        hovered Show(screen="info", i=sol_i, a=sol_a)
                        unhovered Hide("info")  
                        background Frame("gui/style/white_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                        activate_sound audio.cursor
                        xfill True
                        yalign 0.5
                    textbutton _("Solitus"):
                        xpos 0.25
                        hover_sound audio.cursor
                        text_style "white"
                        yalign 0.5
                            
                null height 2
                if p.sol_p > 0:
                    frame:
                        ysize 75
                        xfill True
                        background None
                        $pa_i = '和Pathos曾发生过的故事'
                        $pa_a = '《从小白鼠到感情PUA》'
                        imagebutton idle "gui/phone/address/Pathos.png":
                            action [Hide("info"),Hide("screen_phone_video_address"),Show(screen="screen_phone_video_show",who='pathos', player=player)]
                            hovered Show(screen="info", i=pa_i, a=pa_a)
                            unhovered Hide("info")  
                            background Frame("gui/style/white_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            activate_sound audio.cursor
                            xfill True
                            yalign 0.5
                        textbutton _("Pathos"):
                            xpos 0.25
                            hover_sound audio.cursor
                            text_style "white"
                            yalign 0.5
                                
                    null height 2
                if p.aco_p > 0:
                    frame:  
                        ysize 75
                        xfill True
                        background None
                        $aco_i = '和Acolas曾发生过的故事'
                        $aco_a = '《霸道总裁爱上我》'
                        imagebutton idle "gui/phone/address/Acolas.png":
                            action [Hide("info"),Hide("screen_phone_video_address"),Show(screen="screen_phone_video_show",who='acolas', player=player)]
                            hovered Show(screen="info", i=aco_i, a=aco_a)
                            unhovered Hide("info")  
                            background Frame("gui/style/white_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            activate_sound audio.cursor
                            xfill True
                            yalign 0.5
                        textbutton _("Acolas"):
                            xpos 0.25
                            hover_sound audio.cursor
                            text_style "white"
                            yalign 0.5

                    null height 2
                if p.hal_p > 0:
                    frame:
                        ysize 75
                        xfill True
                        background None
                        $hal_i = '和Halluke曾发生过的故事'
                        $hal_a = '《社恐之间的交流》'
                        imagebutton idle "gui/phone/address/Halluke.png":
                            action [Hide("info"),Hide("screen_phone_video_address"),Show(screen="screen_phone_video_show",who='halluke', player=player)]
                            hovered Show(screen="info", i=hal_i, a=hal_a)
                            unhovered Hide("info")  
                            background Frame("gui/style/white_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            activate_sound audio.cursor
                            xfill True
                            yalign 0.5
                        textbutton _("Halluke"):
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
                        $dep_i = '和？？？曾发生过的故事\n（当前版本尚未开放）'
                        $dep_a = '……'
                        imagebutton idle "gui/phone/address/Depline.png":
                            #action [Hide("info"),Hide("screen_phone_video_address"),Show(screen="screen_phone_video_show",who='depline', player=player)]
                            action NullAction()
                            hovered Show(screen="info", i=dep_i, a=dep_a)
                            unhovered Hide("info")  
                            background Frame("gui/style/white_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            activate_sound audio.cursor
                            xfill True
                            yalign 0.5
                        textbutton _("？？？"):
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
        'pathos':['解锁第二种药物', '解锁第三种药物'],
        'halluke':['初次偷拍','Halluke的能力展示','厕所自慰','初次留下印象','自我怀疑',
            '初次开口','周末约球','特别的约会','获得护膝','鸭血粉丝店的思考','',
            '体育馆的亲吻与诉苦','对一切失去兴趣','与Halluke的轮渡酒店之一','与Halluke的轮渡酒店之二'],
        'acolas':['电梯偶遇','性骚扰式自我介绍'],
    }

    #tag gamegui
    modal True
    style_prefix "gameUI"
    zorder 100
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
        xsize 335
        xpos 15
        background Frame("gui/style/transparent.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
        textbutton routename text_style "white":
            action [SetVariable("replaying", True), SetVariable("replaying_times", player.times), SetVariable("replaying_labelname", labelname), Hide("screen_phone_video_show"),Hide("screen_phone_bg"),Function(renpy.hide_screen,"screen_dashboard"), Return()]
            background Frame("gui/style/white_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
            xfill True
            yfill True
            text_xoffset 85
            activate_sound audio.cursor
        imagebutton idle "gui/phone/video.png":
            yalign 0.5
            xalign 0.05
    null height 2






screen screen_phone_videos(player, who, routes):
    frame:
        background None
        vbox:
            xsize 370
            for i in range(len(routes)): 
                $labelname = who + '_route_' + str(i)
                if renpy.has_label(labelname):
                    if renpy.seen_label(labelname):
                        use video_slot(player, routes[i], labelname)
            null height 10
            textbutton ''


screen screen_phone_videos_sol(player):

    default routes = ['第一天', '第二天', '第三天', '焦虑与疲倦', '咽喉的燃烧感', '以创作发泄焦虑', '梦醒时分', '劳累', '饥饿感']
    default endings = {
        Achievement100:['我已经站在你世界的\n顶端了', 'ending0'], 
        Achievement101:['世间泰坦仅允我喘息', 'ending1'], 
        Achievement102:['深陷其足下泥泞', 'ending2'], 
        Achievement103:['肉与肉与肉与肉的豪\n华盛宴', 'earthquakeBE'], 
        Achievement104:['不能重启的我们只能\n前进', 'despairBE'], 
        Achievement105:['我们的神灵从未向这\n里看过一眼', 'CuredBE'], 
        Achievement400:['为了能够让你学会如\n何去爱', 'ne'], 
        Achievement401:['如果能成为你就好了', 'te'], 
        Achievement402:['我已经一无所有', 'CE']}

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
