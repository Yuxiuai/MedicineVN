init python:
    def toattrsD(attrs):
        d = {}
        for i in attrs:
            d[i[0]] = 0
        return d


    dic_attrs = {
        'solitus':solitus_attrs,
        'pathos':pathos_attrs,
        'halluke':halluke_attrs,
        'acolas':acolas_attrs,
        'destot':destot_attrs,
        'arnel':arnel_attrs,
    }

    dic_ads = {
        'solitus': toattrsD(solitus_attrs),
        'pathos': toattrsD(pathos_attrs),
        'halluke': toattrsD(halluke_attrs),
        'acolas': toattrsD(acolas_attrs),
        'destot': toattrsD(destot_attrs),
        'arnel': toattrsD(arnel_attrs),
    }

default screen_phone_camera_cached = False

screen screen_phone_camera(player):


    #predict False
    style_prefix "gameUI"
    zorder 600
    
    python:

        sol_i = _('存有我自己照片的文件夹')
        sol_a = _('……虽然我倒是偶尔会搞几张自拍给别人看啦。')
        pa_i = _('存有Pathos私密照片的隐藏文件夹')
        pa_a = _('原来白大褂下面的是……色情的双丁！？')
        aco_i = _('存有Acolas私密照片的隐藏文件夹')
        aco_a = _('果然……这鼓胀的裆部之下……硬起来肯定有20cm多吧？')
        hal_i = _('存有Halluke私密照片的隐藏文件夹')
        hal_a = _('居然拍到了尿尿的场景……也太色了！')
        des_i = _('存有Destot私密照片的隐藏文件夹')
        des_a = _('现在的他只有一张剪影而已。')
        arn_i = _('存有Arnel私密照片的隐藏文件夹')
        arn_a = _('现在的他只有一张剪影而已。')

        dep_i = _('存有？？？私密照片的隐藏文件夹\n（当前版本尚未开放）')
        dep_a = _('……')


        
    
    frame:
        
        if phone_page == 3 and not screen_phone_camera_cached:
            at app_inner_show(0, -65)
        elif not screen_phone_camera_cached:
            at app_inner_hide(0, -65)
        

        
        background None
        xcenter 0.5
        ycenter 0.5
        yoffset -10
        
        use barrier('', 0)

        add "gui/phone/wallpaper/camera.webp":
            xcenter 0.5

        text "角色立绘" xpos 0.92 xanchor 1.0 ypos 0.085 size 40 style "phonew"


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
                        if 'solituspics' in persistent.unlocked_items or config.developer:
                            frame:
                                background None
                                xsize 530
                                ysize 176
                                imagebutton idle 'gui/phone/camera/1.jpg':
                                    action Hide("info"),SetVariable("phone_hide", True),Show(screen="screen_phone_camera_show", who="solitus", player=player), SetVariable("phone_hide", True)
                                    hovered Show(screen="info", i=sol_i, a=sol_a)
                                    unhovered Hide("info")
                                    at app_transform
                                    
                                text "Solitus":
                                    style "phonew"
                                    xfill True
                                    yalign 1.0
                                    size 35
                                    xpos 0.02
                        
                        if 'pathospics' in persistent.unlocked_items or config.developer:
                            frame:
                                background None
                                xsize 530
                                ysize 176
                                imagebutton idle 'gui/phone/camera/2.jpg':
                                    action Hide("info"),SetVariable("phone_hide", True),Show(screen="screen_phone_camera_show", who="pathos", player=player), SetVariable("phone_hide", True)
                                    hovered Show(screen="info", i=pa_i, a=pa_a)
                                    unhovered Hide("info")
                                    at app_transform
                                    
                                text "Pathos":
                                    style "phonew"
                                    xfill True
                                    yalign 1.0
                                    size 35
                                    xpos 0.02
                        
                        if 'acolaspics' in persistent.unlocked_items or config.developer:
                            frame:
                                background None
                                xsize 530
                                ysize 176
                                imagebutton idle 'gui/phone/camera/3.jpg':
                                    action Hide("info"),SetVariable("phone_hide", True),Show(screen="screen_phone_camera_show", who="acolas", player=player), SetVariable("phone_hide", True)
                                    hovered Show(screen="info", i=aco_i, a=aco_a)
                                    unhovered Hide("info")
                                    at app_transform
                                    
                                text "Acolas":
                                    style "phonew"
                                    xfill True
                                    yalign 1.0
                                    size 35
                                    xpos 0.02
                        
                        if 'hallukepics' in persistent.unlocked_items or config.developer:
                            frame:
                                background None
                                xsize 530
                                ysize 176
                                imagebutton idle 'gui/phone/camera/4.jpg':
                                    action Hide("info"),SetVariable("phone_hide", True),Show(screen="screen_phone_camera_show", who="halluke", player=player), SetVariable("phone_hide", True)
                                    hovered Show(screen="info", i=hal_i, a=hal_a)
                                    unhovered Hide("info")
                                    at app_transform
                                    
                                text "Halluke":
                                    style "phonew"
                                    xfill True
                                    yalign 1.0
                                    size 35
                                    xpos 0.02
                        
                        if 'destotpics' in persistent.unlocked_items or config.developer:
                            frame:
                                background None
                                xsize 530
                                ysize 176
                                imagebutton idle 'gui/phone/camera/6.jpg':
                                    action Hide("info"),SetVariable("phone_hide", True),Show(screen="screen_phone_camera_show", who="destot", player=player), SetVariable("phone_hide", True)
                                    hovered Show(screen="info", i=des_i, a=des_a)
                                    unhovered Hide("info")
                                    at app_transform
                                    
                                text "Destot":
                                    style "phonew"
                                    xfill True
                                    yalign 1.0
                                    size 35
                                    xpos 0.02

                        if 'arnelpics' in persistent.unlocked_items or config.developer:
                            frame:
                                background None
                                xsize 530
                                ysize 176
                                imagebutton idle 'gui/phone/camera/7.jpg':
                                    action Hide("info"),SetVariable("phone_hide", True),Show(screen="screen_phone_camera_show", who="arnel", player=player), SetVariable("phone_hide", True)
                                    hovered Show(screen="info", i=arn_i, a=arn_a)
                                    unhovered Hide("info")
                                    at app_transform
                                    
                                text "Arnel":
                                    style "phonew"
                                    xfill True
                                    yalign 1.0
                                    size 35
                                    xpos 0.02
                    

                        null height 300
                                


        frame:
            background None
            xpos 0.03
            ypos 0.06
            imagebutton auto "gui/phone/backw_%s.png":
                action SetVariable("screen_phone_camera_cached", False), SetVariable("phone_page", 0), Hide("info")
                hover_sound audio.cursor
            

                
    
    key 'K_ESCAPE' action SetVariable("screen_phone_camera_cached", False), SetVariable("phone_page", 0), Hide("info")

























screen screen_phone_camera_show(player, who='pathos'):
    
    default hiding = False
    default bg = -1
    default attrs = dic_attrs[who]
    default attrsD = dic_ads[who].copy()
    if who == 'solitus':
        default at_list = [truecenter]
    else:
        default at_list = []


    python:
        def export(name, attrs, attrsD):
            if name == 'solitus':
                code = "ss('"
            else:
                code = "show " + name + " "
            for attr in attrs:
                ad = attrsD[attr[0]]

                if ad == 0:
                    continue
                code += attr[2][ad][1]
                code += ' '
            
            if name == 'solitus':
                code += "')"
            else:
                code += "with dissolve"

            pygame_sdl2.scrap.put(pygame_sdl2.SCRAP_TEXT, code.encode("utf-8"))
            showNotice(["已导出代码：", code])

        

        renpy.transition(Dissolve(0.2), layer='headimage')
        if renpy.get_screen("confirm"):
            renpy.transition(None, layer='headimage')
            renpy.scene("headimage")

        

    #tag gamegui
    modal True
    style_prefix "gameUI"
    zorder 600
    frame:
        xfill True
        yfill True
        if bg != -1:
            background ALLBGS[bg]
        else:
            background None
    if not hiding:
        frame:
            at trans_toRight()
            style "translucent_frame"
            yfill True
            xsize 400
            

            frame:
                background None

                text who.capitalize():
                    style 'phonew'
                    xalign 0.9
                    yalign 0.0
                    size 40

            
                viewport:
                    ypos 0.05
                    mousewheel True
                    draggable True
                    scrollbars "vertical"
                    vbox:
                        frame:
                            background None
                            vbox:
                                xfill True 

                                textbutton '{size=-5}背景{/size}' text_style "white":
                                    action NullAction()
                                    xfill True
                                    activate_sound audio.cursor
                                    xoffset -8
                                frame:

                                    background None
                                    ysize 60
                                    textbutton "随机背景（%s / %s）" % (bg+1, LENALLBGS) text_style "white":
                                        action SetLocalVariable("bg", rd(0, LENALLBGS)-1)
                                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                                        xfill True
                                        yfill True
                                        text_size 20
                                        activate_sound audio.cursor
                                frame:

                                    background None
                                    ysize 60
                                    textbutton "前一个背景" text_style "white":
                                        if bg == 0:
                                            action SetLocalVariable("bg", LENALLBGS-1)
                                        elif bg == -1:
                                            action SetLocalVariable("bg", 0)
                                        else:
                                            action SetLocalVariable("bg", bg-1)
                                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                                        xfill True
                                        yfill True
                                        text_size 20
                                        activate_sound audio.cursor
                                frame:

                                    background None
                                    ysize 60
                                    textbutton "后一个背景" text_style "white":
                                        if bg == LENALLBGS-1:
                                            action SetLocalVariable("bg", 0)
                                        elif bg == -1:
                                            action SetLocalVariable("bg", 0)
                                        else:
                                            action SetLocalVariable("bg", bg+1)
                                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                                        xfill True
                                        yfill True
                                        text_size 20
                                        activate_sound audio.cursor

                                frame:

                                    background None
                                    ysize 60
                                    textbutton "隐藏ui" text_style "white":
                                        action SetLocalVariable("hiding", True)
                                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                                        xfill True
                                        yfill True
                                        text_size 20
                                        activate_sound audio.cursor
                                if config.developer:
                                    frame:

                                        background None
                                        ysize 60
                                        textbutton "导出代码" text_style "white":
                                            action Function(export, who, attrs, attrsD)
                                            background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                                            xfill True
                                            yfill True
                                            text_size 20
                                            activate_sound audio.cursor

                                textbutton '{size=-5}细节{/size}' text_style "white":
                                    action NullAction()
                                    xfill True
                                    activate_sound audio.cursor
                                    xoffset -8

                                use screen_phone_camera_show_inner(player, who, attrs, attrsD, at_list)

            
            imagebutton auto "gui/phone/back__%s.png":
                action [Hide("screen_phone_camera_show"),Hide("info"), SetVariable("phone_hide", False), SetVariable("screen_phone_camera_cached", True) ,Function(renpy.hide, who, 'headimage')]
                hover_sound audio.cursor

        key 'K_ESCAPE' action [Hide("screen_phone_camera_show"),Hide("info"), SetVariable("phone_hide", False), SetVariable("screen_phone_camera_cached", True) ,Function(renpy.hide, who, 'headimage')]
    else:
        button:
            xfill True
            yfill True
            action SetLocalVariable("hiding", False)

    if not renpy.showing(who, layer='headimage'):
        #界面打开后再显示 防止卡顿过久
        timer 0.15 action Function(renpy.show, who, at_list=at_list, layer='headimage', zorder=0)


screen screen_phone_camera_show_inner(player, name, attrs, attrsD, at_list=[]):

    for i in attrs:


        frame:

            background None
            ysize 60
            textbutton i[0] text_style 'white':
                action [Show(screen='screen_phone_camera_show_inner_select', i=i, attrsD=attrsD, name=name, at_list=at_list)]
                background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                xfill True
                yfill True
                text_size 20
                activate_sound audio.cursor

            text i[2][attrsD[i[0]]][0] style 'white':
                xalign 0.975
                size 20
                #yoffset -5
                #yalign 0.5

    null height 10
    textbutton ''

screen screen_phone_camera_show_inner_select(i, attrsD, name, at_list):
    use barrier(screen="screen_phone_camera_show_inner_select",tr=None)
    style_prefix "info"
    zorder 2002
    default pp = renpy.get_mouse_pos()
    $ p = pp
    if p[0] < 1500:
        $ xc = 0.0
        $ trans = trans_toLeft
    else:
        $ xc = 1.0
        $ trans = trans_toRight
    $ xc = 0.0 if p[0] < 1500 else 1.0
    $ yc = 0.0 if p[1] < 540 else 1.0
    frame:
        pos pp
        padding (15, 15)
        xanchor xc
        yanchor yc
        xsize 300
        at trans()
        has vbox


        for j in range(len(i[2])):
            frame:
                background None
                ysize 50
                $attrname = i[2][j][0]
                textbutton attrname text_style "white":
                    action [Function(renpy.show, name+' '+i[2][j][1], at_list=at_list, layer='headimage', zorder=0), SetDict(attrsD, i[0], j)]
                    background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                    xfill True
                    activate_sound audio.cursor
                if attrsD[i[0]] == j:
                    add "gui/right_.png":
                        xalign 0.975
                        yalign 0.5
            null height 2
