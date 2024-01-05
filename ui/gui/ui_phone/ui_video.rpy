init python:
    def hasending(endings):
        for i in endings:
            if type(i) == list:
                for j in i:
                    if renpy.seen_label(j[0]) or persistent.unlockcharacterplot:
                        return True
        return False

screen screen_phone_video(player):

    predict False
    style_prefix "gameUI"
    zorder 600
    
    python:

        sol_i = _('个人剧情')
        sol_a = _('《社畜福瑞重度头疼》')
        pa_i = _('和Pathos曾发生过的故事')
        pa_a = _('《从小白鼠到PUA》')
        aco_i = _('和Acolas曾发生过的故事')
        aco_a = _('《霸道总裁爱上我》')
        hal_i = _('和Halluke曾发生过的故事')
        hal_a = _('《社恐之间的交流》')
        des_i = _('和Destot曾发生过的故事')
        des_a = _('《桌子底下怎么有奇怪的声音》')

        dep_i = _('和？？？曾发生过的故事\n（当前版本尚未开放）')
        dep_a = _('……')



        routes = {
            'solitus':[
                '序章',[
                    ["solitus_route_0", _('平庸的社畜：第一天')], 
                    ["solitus_route_1", _('平庸的社畜：第二天')], 
                    ["solitus_route_2", _('平庸的社畜：第三天')], 
                    ["writer_day0", _('全职小说家：第一天')], 
                    ["writer_day1", _('全职小说家：第二天')], 
                    ["writer_day2", _('全职小说家：第三天')], 
                ],

                '个人剧情',[
                    ["solitus_route_3", _('焦虑与疲倦')] , 
                    ["solitus_route_4", _('咽喉的燃烧感')] , 
                    ["solitus_route_5", _('以创作发泄焦虑')] , 
                    ["solitus_route_6", _('梦醒时分')] , 
                    ["solitus_route_7", _('劳累')] , 
                    ["solitus_route_8", _('饥饿感')] , 
                    ["solitus_route_9", _('关于自慰')] ,
                ],
                
            ],

            'pathos':[
                '主要剧情',[
                    ["pathos_route_0", _('解锁第二种药物')] , 
                    ["pathos_route_1", _('解锁第三种药物')] , 
                    ["pathos_route_2", _('签订手术知情书')] ,
                ],
                '其他',[
                    ["explore_center_3_hide", _('游泳馆的偶遇')], 
                ],

            ],

            'halluke':[
                '主要剧情',[
                    ["halluke_route_0", _('初次偷拍')] ,
                    ["halluke_route_1", _('Halluke的能力展示')] ,
                    ["halluke_route_2", _('厕所自慰')] ,
                    ["halluke_route_3", _('初次留下印象')] ,
                    ["halluke_route_4", _('自我怀疑')] ,
                    ["halluke_route_5", _('初次开口')] ,
                    ["halluke_route_6", _('周末约球')] ,
                    ["halluke_route_7", _('特别的约会')] ,
                    ["halluke_route_8", _('获得护膝')] ,
                    ["halluke_route_9", _('粉丝店的思考')] ,
                    ["halluke_route_11", _('体育馆的亲吻与诉苦')] ,
                    ["halluke_route_12", _('对一切失去兴趣')] ,
                    ["halluke_route_13", _('与Halluke的轮渡酒店之一')] ,
                    ["halluke_route_14", _('与Halluke的轮渡酒店之二')] ,
                ],
                '隐藏剧情',[
                    
                    ["Halluke_hidden_plot1", _('这一切仿佛从未发生')], 
                    
                ],

            ],

            'acolas':[
                '主要剧情',[
                    ["acolas_route_0", _('电梯偶遇')] ,
                    ["acolas_route_1", _('性骚扰式自我介绍')] ,
                    ["acolas_route_2", _('道歉与游戏项目')] ,
                    ["acolas_route_3", _('火锅与第一次项目')] ,
                    ["acolas_route_4", _('结束第一次项目')] ,
                    ["acolas_route_5", _('咖啡营地与第二次项目')] ,
                    ["acolas_route_6", _('缺席会议的Acolas')] ,
                    ["acolas_route_7", _('医院看望')] ,
                    ["acolas_route_8", _('Acolas的公寓与结束第二次项目')] ,
                    ["acolas_route_9", _('游戏发布与获得旧笔记')] ,
                    ["acolas_route_10", _('Acolas的办公室')] ,
                    ["acolas_route_11", _('Acolas的醒悟')] ,
                    ["acolas_route_12", _('与Acolas的轮渡酒店之一')] ,
                    ["acolas_route_13", _('与Acolas的轮渡酒店之二')] ,
                ],

                '隐藏剧情',[
                    ["Acolas_hidden_plot1", _('踏入乌托邦的大门')],
                ],

                '其他剧情',[
                    ["dream_acolas", _('入迷之梦')],
                ]

    
            ],

            'destot':[
                [
                    ["destot_route_0", _('新实习生')] ,
                    ["destot_route_1", _('实习生报道')] ,
                    ["destot_route_2", _('牵手与自助餐')] ,
                    ["destot_route_3", _('面馆与沉寂的氛围')] ,
                    ["destot_route_4", _('Destot的告白')] ,
                    ["destot_route_5", _('他已经离开了')],
                ],

    
            ],

        }

        endings = {
            'solitus':[
                [
                    ['ending0', _('BE0：我已经站在你世界的顶端了')], 
                    ['ending1', _('BE1：在我品尝爱或咖啡的苦涩之前')], 
                    ['ending2', _('BE2：用剪刀剪下连接着我的牵线')], 
                    ['earthquakeBE', _('BE3：肉与肉与肉与肉的豪华盛宴')], 
                    ['despairBE', _('BE4：不能重启的我们只能前进')], 
                    ['CuredBE', _('BE5：我们的神灵从未向这里看过一眼')], 
                    ['hardcorebe1', _('BE6：想象你依然存在（体弱）')], 
                    ['hardcorebe2', _('BE6：想象你依然存在（谵妄）')], 
                    ['hardcorebe3', _('BE6：想象你依然存在（衰退）')], 
                    ['ne', _('NE：为了能够让你学会如何去爱')], 
                    ['te', _('TE：如果能成为你就好了')], 
                    ['ce', _('CE：我已经一无所有')],
                    ['we', 'WE：融解'],
                ],
            ],
            'halluke':[
                [
                    ['fe_h', _('FE：我们活在一个没有生命的茧中')],
                    ['se_h', _('SE：存在')],
                ],
            ],
            'acolas':[
                [
                    ['fe_a', _('FE：我们活在一个没有生命的茧中')],
                    ['se_a', _('SE：存在')],
                ],
            ],
            'pathos':[],
            'destot':[],
        }


        
    
    frame:
        
        if phone_page == 4:
            at app_inner_show(110, -65)
        else:
            at app_inner_hide(110, -65)
        

        
        background None
        xcenter 0.5
        ycenter 0.5
        yoffset -10
        
        use barrier('', 0)

        add "gui/phone/wallpaper/camera.webp":
            xcenter 0.5

        text "剧情回顾" xpos 0.92 xanchor 1.0 ypos 0.085 size 40 style "phonew"

        frame:
            
            background None
            xalign 0.5
            ypos 150
            ysize 800
            xsize 582
            
            viewport:
                xcenter 0.5
                mousewheel True
                draggable True
                scrollbars "vertical"

                frame:
                    background None
                    xsize 540
                    

                    
                        

                    vbox:
                        spacing 20
                        if True:
                            vbox:
                                frame:
                                    background None
                                    xsize 530
                                    ysize 176
                                    imagebutton idle 'gui/phone/camera/1.jpg':
                                        action NullAction()
                                        hovered Show(screen="info", i=sol_i, a=sol_a)
                                        unhovered Hide("info")
                                        at app_transform
                                        
                                    text "Solitus":
                                        style "phonew"
                                        xfill True
                                        yalign 1.0
                                        size 35
                                        xpos 0.02
                                use screen_phone_videos(player, 'solitus', routes['solitus'], endings['solitus'])
                        
                        if hasending(routes['pathos']) or hasending(endings['pathos']):
                            vbox:
                                frame:
                                    background None
                                    xsize 530
                                    ysize 176
                                    imagebutton idle 'gui/phone/camera/2.jpg':
                                        action NullAction()
                                        hovered Show(screen="info", i=pa_i, a=pa_a)
                                        unhovered Hide("info")
                                        at app_transform
                                        
                                    text "Pathos":
                                        style "phonew"
                                        xfill True
                                        yalign 1.0
                                        size 35
                                        xpos 0.02
                                use screen_phone_videos(player, 'pathos', routes['pathos'], endings['pathos'])
                        
                        if hasending(routes['acolas']) or hasending(endings['acolas']):
                            vbox:
                                frame:
                                    background None
                                    xsize 530
                                    ysize 176
                                    imagebutton idle 'gui/phone/camera/3.jpg':
                                        action NullAction()
                                        hovered Show(screen="info", i=aco_i, a=aco_a)
                                        unhovered Hide("info")
                                        at app_transform
                                        
                                    text "Acolas":
                                        style "phonew"
                                        xfill True
                                        yalign 1.0
                                        size 35
                                        xpos 0.02
                                use screen_phone_videos(player, 'acolas', routes['acolas'], endings['acolas'])
                        
                        if hasending(routes['halluke']) or hasending(endings['halluke']):
                            vbox:
                                frame:
                                    background None
                                    xsize 530
                                    ysize 176
                                    imagebutton idle 'gui/phone/camera/4.jpg':
                                        action NullAction()
                                        hovered Show(screen="info", i=hal_i, a=hal_a)
                                        unhovered Hide("info")
                                        at app_transform
                                        
                                    text "Halluke":
                                        style "phonew"
                                        xfill True
                                        yalign 1.0
                                        size 35
                                        xpos 0.02
                                use screen_phone_videos(player, 'halluke', routes['halluke'], endings['halluke'])
                        
                        if hasending(routes['destot']) or hasending(endings['destot']):
                            vbox:
                                frame:
                                    background None
                                    xsize 530
                                    ysize 176
                                    imagebutton idle 'gui/phone/camera/6.jpg':
                                        action NullAction()
                                        hovered Show(screen="info", i=des_i, a=des_a)
                                        unhovered Hide("info")
                                        at app_transform
                                        
                                    text "Destot":
                                        style "phonew"
                                        xfill True
                                        yalign 1.0
                                        size 35
                                        xpos 0.02
                                use screen_phone_videos(player, 'destot', routes['destot'], endings['destot'])

                    

                        null height 300
                                


        frame:
            background None
            xpos 0.03
            ypos 0.06
            imagebutton auto "gui/phone/backw_%s.png":
                action SetVariable("phone_page", 0), Hide("info")
                hover_sound audio.cursor
            

                
    
    key 'K_ESCAPE' action SetVariable("phone_page", 0), Hide("info")







screen screen_phone_videos(player, who, routes, endings):

    frame:
        background None
        vbox:
            xfill True
            if hasending(routes):
                for i in routes:
                    if type(i) == list:
                        for j in i:
                            if renpy.seen_label(j[0]) or persistent.unlockcharacterplot:
                                use video_slot(player, j[1], j[0])
                    else:
                        text '{size=-5}%s{/size}'%i style "white":
                            xfill True


            if hasending(endings):
                text _('{size=-5}分支结局{/size}') style "white":
                    xfill True

                for i in endings:
                        
                    if type(i) == list:
                        for j in i:
                            if renpy.seen_label(j[0]) or persistent.unlockcharacterplot:
                                use video_slot(player, j[1], j[0])











screen video_slot(player, routename, labelname):
    frame:
        ysize 70
        xfill True
        background None
        textbutton routename text_style "white":
            action SetVariable("replaying", True), SetVariable("replaying_times", player.times), Hide("screen_phone"), SetVariable("phone_page", 0), Hide("info"), Function(renpy.hide_screen,"screen_dashboard"), Jump(labelname)
            background Frame("#494949")
            xfill True
            yfill True
            xalign 0.5
            activate_sound audio.cursor
            at app_transform
            
            
    null height 2

