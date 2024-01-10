image wallpaper_1 = 'images/gui/phone/wallpaper/1.webp'
image wallpaper_2 = 'images/gui/phone/wallpaper/2.webp'
image wallpaper_3 = 'images/gui/phone/wallpaper/3.webp'
image wallpaper_4 = 'images/gui/phone/wallpaper/4.webp'
image wallpaper_5 = 'images/gui/phone/wallpaper/5.webp'
image wallpaper_aco = 'images/gui/phone/wallpaper/aco.webp'
image wallpaper_hal = 'images/gui/phone/wallpaper/hal.webp'
image wallpaper_des = 'images/gui/phone/wallpaper/des.webp'
image wallpaper_ruin = 'images/gui/phone/wallpaper/ruin.webp'
image wallpaper_se = 'images/gui/phone/wallpaper/se.webp'
image wallpaper_te = 'images/gui/phone/wallpaper/te.webp'
image wallpaper_we = 'images/gui/phone/wallpaper/we.webp'
image wallpaper_ce = 'images/gui/phone/wallpaper/ce.webp'
image wallpaper_toy = 'images/gui/phone/wallpaper/toy.webp'

init python:
    def get_frame(player):
        return "gui/phone/frame.png"





default phone_defaulted = False
default phone_cached_app = None
default phone_page = 0

transform pickup_phone_transform():
    on show:
        yoffset 1200
        easein 0.4 yoffset 0
    on hide:
        easein 0.3 yoffset 1200

transform app_transform():
    
    on idle:
        easein 0.2 matrixcolor IdentityMatrix()
    on hover:
        easein 0.2 matrixcolor BrightnessMatrix(0.1)

transform app_appear(x, y, wait):
    xoffset y
    yoffset -x
    alpha 0.0
    wait
    parallel:
        easein 0.5 alpha 1.0
    parallel:
        easein 0.5 xoffset 0
    parallel:
        easein 0.5 yoffset 0

transform app_close():
    parallel:
        easein 0.2 alpha 0.0
    parallel:
        easein 0.1 xoffset 50
    parallel:
        easein 0.1 yoffset -50

transform app_inner_show(x, y):
    xoffset x
    yoffset y
    zoom 0.0
    parallel:
        easeout 0.4 zoom 1.0
    parallel:
        easeout 0.4 xoffset 0
    parallel:
        easeout 0.4 yoffset 0

transform app_inner_hide(x, y):
    parallel:
        easeout 0.2 zoom 0.0
    parallel:
        easeout 0.2 xoffset x
    parallel:
        easeout 0.2 yoffset y

transform app_inner_undefaulted(x, y):
    zoom 0.0




screen screen_phone_app_null():
    frame:
        xsize 95
        ysize 110
        background None
        add "gui/phone/icons/null.png":
            xcenter 0.5
        
        text '':
            xcenter 0.5
            yalign 1.0
            yoffset 1
            size 17
            style "phone"

screen screen_phone_app(player, name, icon, page, x, y, i, a):
    frame:
        if phone_defaulted:
            at app_appear(x, y, 0)
        else:
            at app_appear(x, y, 0.3)
        xsize 95
        ysize 110
        background None
        imagebutton idle "gui/phone/icons/"+icon+".png":
            action SetVariable("phone_page", page), SetVariable("phone_cached_app", icon), Hide("info")
            activate_sound audio.cursor
            hovered Show(screen="info", i=i, a=a)
            unhovered Hide("info")
            xcenter 0.5
            at app_transform
        
        text name:
            xcenter 0.5
            yalign 1.0
            yoffset 1
            size 17
            style "phone"

screen screen_phone_header(player):
    frame:
        background None
        ysize 30
        xsize 582
        yoffset 4
        
        $showHour=player.st()[0]
        $showMin=player.st()[1]
        $battary = max(1, 100-int((int(showHour)*60+int(showMin)-420)*100/950))

        text "[showHour]:[showMin]" size 25 style "phone" yalign 0.5
        
        bar:
            value battary
            range 100
            ysize 25
            xsize 45
            xpos 0.795
            yalign 0.5
            
            if battary > 66:
                at colorize('#00ec0c')
            elif battary > 33:
                at colorize('#ecd400')
            else:
                at colorize('#f10000')
        
        frame:
            ysize 25
            xsize 50
            xpos 0.795
            yalign 0.5
            background Frame("gui/phone/battary_frame.png", 2, 2, 4, 2, True)

        text "[battary]%" size 25 xpos 0.89 yalign 0.5 style "phone"

        text "電" size 30 xpos 0.735 yalign 0.5 style "phone"

default phone_hide = False



screen screen_phone(player):
    #tag gamegui
    modal True
    style_prefix "gameUI"
    zorder 600
    
    if not phone_hide:
        frame at pickup_phone_transform:
            
            background None
            xalign 0.5
            ypos 0.1
            ysize 1300
            xsize 582

            
            use screen_phone_desktop(player)

            if phone_page == 1 or phone_cached_app == '2048':
                use screen_phone_2048(player)

            if phone_page == 2 or phone_cached_app == 'levi':
                use screen_phone_levi(player)

            if phone_page == 3 or phone_cached_app == 'camera':
                use screen_phone_camera(player)

            if phone_page == 4 or phone_cached_app == 'video':
                use screen_phone_video(player)

            if phone_page == 5 or phone_cached_app == 'gallery':
                use screen_phone_gallery(player)

            if phone_page == 6 or phone_cached_app == 'calc':
                use screen_phone_calc(player)

            if phone_page == 7 or phone_cached_app == 'write':
                use screen_phone_write(player)

            if phone_page == 8 or phone_cached_app == 'note':
                use screen_phone_note(player)

            if phone_page == 9 or phone_cached_app == 'food':
                use screen_phone_food(player)

            if phone_page == 10 or phone_cached_app == 'music':
                use screen_phone_music(player)

            if phone_page == 11 or phone_cached_app == 'call':
                use screen_phone_call(player)

            if phone_page == 12 or phone_cached_app == 'message' or phone_cached_app == 'new':
                use screen_phone_message(player)

            if phone_page == 13 or phone_cached_app == 'wallpaper':
                use screen_phone_wallpaper(player)

            if phone_page == 14 or phone_cached_app == 'browser':
                use screen_phone_browser(player)
            
            if phone_page == 15 or phone_cached_app == 'cheat':
                use screen_phone_cheat(player)

            if phone_page == 99 or phone_cached_app == 'weather':
                use screen_phone_weather(player)
                


            use screen_phone_header(player)


            add "gui/phone/frame.png":
                xalign 0.5
                ypos -8

        $phone_defaulted = True

        if phone_page == 0:
            timer 0.5 action SetVariable("phone_cached_app", None)
            key 'K_ESCAPE' action Hide("info"),SetVariable("phone_defaulted", False),SetVariable("phone_cached_app", None),Hide("screen_phone")
        

screen screen_phone_desktop(player):
    
    add player.phone_wallpaper xcenter 0.5 yoffset -2 

    $weather=player.effects[0].name
    $weekday = weekdayFormat(player.today)


    $showHour=player.st()[0]
    $showMin=player.st()[1]

    text "[showHour]:[showMin]" size 100 xalign 0.08 yalign 0.15 style "phone"
    textbutton "[weather]" text_size 30 xpos 0.95 yalign 0.15 xanchor 1.0 xoffset 10 text_style "phone" action SetVariable("phone_page", 99), SetVariable("phone_cached_app", 'weather'), Hide("info")
    text "[player.mon]月[player.day]日 [weekday]" size 30 xpos 0.95 yalign 0.185 xanchor 1.0 style "phone"



    frame:
        ypos .3
        background None
        xcenter 0.5
        hbox:
            spacing 15
            use screen_phone_app_null
            use screen_phone_app_null
            use screen_phone_app_null
            use screen_phone_app_null
            if persistent.sponsor or config.developer:
                use screen_phone_app(player, '神秘应用', "cheat", 15, 0, -50, _('赞助者模式菜单，可以刷取道具和状态。'), _('不内置作者本人的色图。'))
            else:
                use screen_phone_app_null
                


    frame:
        ypos .4
        background None
        xcenter 0.5
        hbox:
            spacing 15
            use screen_phone_app(player, '2048', "2048", 1, 25, 50, _('经典的小游戏2048。'), _('关于我平时摸鱼的时候都在干什么。'))
            use screen_phone_app(player, '电子宠物', 'levi', 2, 25, 25, _('曾经是掌控世界的海神！现在是……你的电子宠物利维坦。'), _('主角换了新手机，所以我们把这位可爱的海神放进了这里。'))
            use screen_phone_app(player, '相机', 'camera', 3, 25, 0, _('查看角色立绘。'), _('偷拍婆的隐藏文件夹……等等，这拍的也太多了，还这么全面？'))
            use screen_phone_app(player, '视频', 'video', 4, 25, -25, _('回顾人物剧情。'), _('缅怀某个叫做网课的东西。'))
            use screen_phone_app(player, '相册', 'gallery', 5, 25, -50, _('欣赏游戏CG。'), _('一般我们都会管这个叫“画廊”，不过那听起来也太高贵了。'))

    frame:
        ypos .5
        background None
        xcenter 0.5
        hbox:
            spacing 15
            use screen_phone_app(player, '计算器', "calc", 6, 50, 50, _('用于计算的计算器。'), _('嗯……谁会在一个游戏里玩计算器呢？'))
            use screen_phone_app(player, '写作平台', 'write', 7, 50, 25, _('通过接委托，完成委托或上传随笔来获得人气和报酬。\n接取的委托在所持物品中。'), _('什么时候写东西也像画画那样来钱快粉丝涨的也快就好了……'))
            use screen_phone_app(player, '统计', 'note', 8, 50, 0, _('统计各种数据。\n\n数据更新带有延迟，如数据无变化可以通过再次进入的方式刷新界面，也可以等待下一回合自动刷新。\n全局数据仅在每日存档时更新，重新游玩数据也会继续记录。'), _('谁不喜欢统计数据呢？'))
            if player.experience == 'wri':
                use screen_phone_app(player, '外卖', 'food', 9, 50, -25, _('购买多种多样的食物。'), _('相对于自己做饭，还是点外卖吧……'))
            else:
                use screen_phone_app(player, '外卖', 'food', 9, 50, -25, _('购买多种多样的食物。'), _('如果中午不点外卖的话我就会去吃免费的工作餐，其他时候的话就饿着也没事。'))
            use screen_phone_app(player, '音乐', 'music', 10, 50, -50, _('欣赏游戏音乐。'), _('感觉……你药音乐不如你城……'))

    frame:
        ypos 0.63
        background None
        xcenter 0.5
        hbox:
            spacing 15
            use screen_phone_app(player, '通话', "call", 11, 75, 50, _('和你的朋友打个电话聊聊天吧。'), _('谁会直接和！送外卖的店家！打电话！啊！'))
            if Message.hasNewMes(player):
                use screen_phone_app(player, '某信', 'new', 12, 75, 25, _('有新消息了。'), _('“永远爱你”\n“啊对对”'))
            else:
                use screen_phone_app(player, '某信', 'message', 12, 75, 25, _('和已经添加手机号的朋友聊天。'), _('“永远爱你”\n“啊对对”'))
            use screen_phone_app(player, '壁纸', 'wallpaper', 13, 75, 0, _('更换桌面壁纸。'), _('不能换成大尺度照片么？'))
            use screen_phone_app(player, '图鉴', 'browser', 14, 75, -25, _('查看已获得过的道具和状态。'), _('百度亿下，你就知道。'))
            
        
            frame:
                if phone_defaulted:
                    at app_appear(75, -50, 0)
                else:
                    at app_appear(75, -50, 0.3)
                xsize 95
                ysize 110
                background None
                imagebutton idle "gui/phone/icons/shutdown.png":
                    action [SetVariable("phone_defaulted", False),SetVariable("phone_cached_app", None),Hide("screen_phone"),Hide("info")]
                    activate_sound audio.cursor
                    hovered Show(screen="info", i=_('是时候做点有用的事了。'), a=_('关掉，关掉，一定要关掉！'))
                    unhovered Hide("info")
                    xcenter 0.5
                    at app_transform
                
                text '关闭':
                    xcenter 0.5
                    yalign 1.0
                    size 18
                    style "phone"
