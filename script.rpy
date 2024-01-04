transform newplayer_show:
    xalign 0.5
    yalign 0.5
    matrixcolor SepiaMatrix()

screen newplayer_warning:
    $info = "本游戏正在测试中，可能会出现各种意想不到的报错或BUG，包括但不限于{u}无法触发剧情{/u}，{u}存档崩坏{/u}，{u}进度归零等情况{/u}，如果发现报错请在频道反馈，{u}点击忽略错误可能会引发更多错误！{/u}\n"
    $info += "本游戏仅作为个人学习用，请勿用作他用，请在下载之后的24小时内删除游戏。"
    $info += "禁止私自发布、外传、搬运本游戏，本游戏为免费游戏，禁止通过该游戏牟利，如果您是通过某种渠道购买该游戏，很可能已经上当受骗。\n"
    $info += "在游戏的游玩过程中可能会出现恐怖，色彩突然变换等情况，不适合容易受到干扰，对心理暗示感到不适，患有光敏性癫痫以及有心脏病的玩家。\n"
    $info += "本游戏仅发布于{u}itch.io游戏主页{/u}以及QQ频道{u}Endorphins酒馆{/u}，除此之外皆为非法发布，{u}因非官方人员非法发布的游戏副本受到的损失请自行承担。{/u}\n"
    $info += "本游戏为限制级，包含{u}露骨的限制级描写，血腥暴力，以及精神疾病等{/u}，除此之外还含有{u}同性爱，兽人，meta元素等敏感元素{/u}。\n如果您未满18岁或者对这些元素感到不适，请{u}退出游戏。{/u}\n"
    $info += "本游戏包含的时间，地点，人物，事件，故事及其他内容均为虚构，与真实人物或事件无关。如有雷同，纯属巧合。\n"
    $info += "游戏可能并{u}不包含你想要的剧情和结局{/u}，也{u}不存在温馨欢愉的剧情{/u}。"
    $info += "以上以及此段提示仅会出现一次，如果您确定自己已经熟读以上内容准确无误，同时能够接受所提到的元素并已成年，\n请点击右下角的图标进入游戏，否则请关闭游戏，{u}游玩游戏导致的精神损失等一切后果请自行承担。{/u}\n"
        
    frame at screen_init_select_info:
        xsize 1300
        ysize 700
        xpos 1920
        ycenter 0.5
        yoffset 45
        background Frame("gui/style/grey_idle_background.png", tile=gui.frame_tile)
        
        vbox:
            text info:
                style "white" 
                size 25

        imagebutton auto "images/gui/opening/ok_%s.png":
            action Return()
            xalign 0.9
            yalign 0.95
            activate_sound audio.click1
    
    use menu_labelname('警告')

screen newplayer_warning_android:
    $info = "因为游戏本质上是带有模拟经营要素的视觉小说，使用鼠标能更加轻松地操作，以及一些演出效果专为电脑平台设计，在安卓平台上没法完全还原，有能力请一定使用电脑游玩。\n"
    $info += "请不要将游戏放置于后台，这极大概率会导致{u}游戏报错{/u}，甚至{u}坏档{/u}。\n"
    $info += "当你在游玩剧情的过程中闪退，可能是因为加载立绘用时较久，让安卓系统误认为游戏卡死然后退出，并非是BUG。\n"
    $info += "如果频繁出现闪退情况，请在设置中点开{u}禁用主角立绘{/u}的选项，这可能有助于减少闪退的出现概率。\n"
    $info += "如果你执意要在手机平台上游玩该游戏，请记得备份存档以防万一。\n"
        
    frame at screen_init_select_info:
        xsize 1300
        ysize 700
        xpos 1920
        ycenter 0.5
        yoffset 45
        background Frame("gui/style/grey_idle_background.png", tile=gui.frame_tile)
        
        vbox:
            text info:
                style "white" 
                size 40

        imagebutton auto "images/gui/opening/ok_%s.png":
            action Return()
            xalign 0.9
            yalign 0.95
            activate_sound audio.click1
    
    use menu_labelname('安卓玩家须知')

label splashscreen:
    $renpy.sound.stop(channel="chara_voice")
    $renpy.hide('blackmask', layer='mask')
    $sh()
    
    $Saver.savecheck()
    $Achievement.check()

    scene black
    $ p=None
    $ replaying = False

    $ _game_menu_screen = None
    $ quick_menu=False
    $ _confirm_quit=False
    $ renpy.block_rollback()
    $ _skipping = False

    if persistent.newplayer:
        scene suicide at newplayer_show with dissolve
        call screen newplayer_warning
        $ persistent.newplayer = False
        if renpy.android:
            call screen newplayer_warning_android
        scene black with fade
        $pause(0.5)

    play music audio.themedicine

    if not persistent.nosplash:
        show splash
        $ renpy.pause(delay=6,hard=True)
    
    $ _game_menu_screen = "screen_gamemenu"
    $ quick_menu=True
    $ _confirm_quit=True
    $ renpy.block_rollback()
    $ _skipping = True

    

    return

label start:
    $replaying = False
    $_game_menu_screen = "screen_gamemenu"
    $p.player_default()
    if config.developer:
        menu:
            "跳过开局？"
            "周一":
                $ p.newDay()
                $ p.newDay()
                $ p.newDay()

                $ MedicineA.add(p, 10)
                $ Notice.clear()
                $ p.onOutside = False
                
                $ p.mental = 100
                $ Saver.save(p)

                $ p.times = 2
                $ p.onVacation = False
                if p.experience == 'wri':
                    $ p.onVacation = True

                show screen screen_dashboard(p)

                jump before_operate_screen_label
            "周六":
                $ p.newDay()
                $ p.newDay()
                $ p.newDay()

                $ MedicineA.add(p, 10)
                $ Notice.clear()

                $ p.today = 6
                $ p.day = 7
                $ p.mental = 100
                $ p.onOutside = False
                $ Saver.save(p)

                $ p.times = 2
                $ p.onVacation = True
                
                
                
                show screen screen_dashboard(p)

                jump before_operate_screen_label
            "不了":
                pass
            
    jump day0


label bookdont:
    $clearscreens()
    $ sh()
    $ _confirm_quit = False
    $ _game_menu_screen = None
    $ _skipping = False
    $ quick_menu = False
    stop music
    scene bs
    $Achievement303.achieve()
    $renpy.pause()
    $renpy.quit()


label to_the_title:
    $renpy.hide('blackmask', layer='mask')
    $renpy.sound.stop(channel="chara_voice")
    $sh()
    $clearscreens()
    $ sh()
    play music audio.themedicine

    $ _confirm_quit = False
    $ _game_menu_screen = None
    $ _skipping = False
    $ quick_menu = False
    $ replaying = False

    if not persistent.nosplash:
        scene black with fade
        show splash
        $ renpy.pause(delay=6,hard=True)
    

    $ quick_menu = True
    $ _skipping = True
    $ _confirm_quit = True
    $ _game_menu_screen = "screen_gamemenu"
    return


label afterload:

    $ config.rollback_enabled = False
    $ replaying = False
    $clearscreens()
    call loading from _call_loading_3
    #$routine_music(p)
    if Despair.has(p):
        jump despair_wakeup
    if p.hal_p == 15 or p.aco_p == 14:
        if p.experience == 'wri':
            jump writer_before_earthquake
        jump before_earthquake
    if p.hal_p == 14 and p.today == 7:
        jump halluke_route_14
    if p.aco_p == 13 and p.today == 7:
        jump acolas_route_13
    if p.dep_p == 8:
        jump depline_route_8
    if p.week==0 and p.day==29:
        if p.experience == 'wri':
            jump writer_day0
        jump day0
    elif p.week==0 and p.day==30:
        if p.experience == 'wri':
            jump writer_wakeup_pro
        jump wakeup_pro
    elif p.week==0 and p.day==1:
        if p.experience == 'wri':
            jump writer_wakeup_pro
        jump wakeup_pro
    elif p.week==1 and p.day==2:
        if p.experience == 'wri':
            jump writer_wakeup_pro
        jump wakeup_pro
    else:
        jump wakeup


screen test_():
    default x = 1
    frame:
        #background None
        xcenter 0.5
        ycenter 0.5
    
        text str(x)
        use test__(x)

screen test__(x):
    textbutton '+':
        action SetScreenVariable("x", x+1)
