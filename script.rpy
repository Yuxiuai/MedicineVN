label splashscreen:
    $renpy.sound.stop(channel="chara_voice")
    $renpy.hide('blackmask', layer='mask')
    $sh()
    scene black
    $ p=None
    $ replaying = False

    $ _game_menu_screen = None
    $ quick_menu=False
    $ _confirm_quit=False
    $ renpy.block_rollback()
    $ _skipping = False

    if persistent.newplayer:
        "本游戏正在测试中，可能会出现各种意想不到的报错或BUG，包括但不限于无法触发剧情，存档崩坏，进度归零等情况，请做好心理准备或等待稳定版发布。"
        "禁止私自发布、外传、搬运等，本游戏为免费游戏，禁止通过该游戏牟利，如果您是通过某种渠道购买该游戏，可能已经上当受骗。"
        "本游戏仅发布于{color=#fbff00}{a=https://yuxiu.itch.io/medicine}itch.io游戏主页{/a}{/color}以及QQ频道{color=#fbff00}{a=https://pd.qq.com/s/f83b8nyks}Endorphins酒馆{/a}{/color}，除此之外皆为非法发布。"
        "本游戏不适合容易受到干扰，对心理暗示感到不适的玩家。"
        "本游戏包含限制级内容，除此之外还含有同性爱，兽人等。\n如果您未满18岁或者对这些元素感到不适，请退出游戏。"
        "本游戏在电脑平台上的某些效果更好，如果可以请尽量使用电脑游玩。"
        "本游戏包含的时间，地点，人物，事件，故事及其他内容均为虚构，与真实人物或事件无关。如有雷同，纯属巧合。"
        "以上以及此段提示仅会出现一次，如果您确定自己已经熟读以上内容准确无误，同时能够接受所提到的元素并已成年，\n请点击“我同意”以进入游戏，否则请关闭游戏。"
        menu:
            "以上以及此段提示仅会出现一次，如果您确定自己已经熟读以上内容准确无误，同时能够接受所提到的元素并已成年，\n请点击“我同意”以进入游戏，否则请关闭游戏。{fast}"
            "我同意":
                $ persistent.newplayer = False

    play music audio.themedicine

    if not persistent.nosplash:
        show splash
        $ renpy.pause(delay=6,hard=True)

    $ _game_menu_screen = "save"
    $ quick_menu=True
    $ _confirm_quit=True
    $ renpy.block_rollback()
    $ _skipping = True

    $Save.savecheck()

    return

label start:
    $ config.rollback_enabled = False
    $ _game_menu_screen = None
    $ p = None
    $ Save.clear()
    stop music fadeout 5
    "…"
    "……"
    "………"
    play music audio.nameyourself
    jump nameYourself

label nameYourself:
    $ mc=renpy.input(_("你的名字是？"), length=10, default=persistent.beforename, exclude="\"\'[]{}%$@?!#^&*\(\)")
    if not mc:
        $ mc="Solitus"
        "你的名字是Solitus，确定吗？"
        jump acceptedName
    if mc=="Solitus":
        "“真正的名字。”"
        jump acceptedName
    elif mc=="Pathos" or mc=="帕索斯" or mc=="pathos":
        "“……”"
        "“这个名字已经被我占用了。”"
        "“还是换一个吧。”"
        jump notAcceptedName
    elif mc=="Decay" or mc=="德凯" or mc=="decay":
        "“……”"
        "“那是我的名字，幼崽。”"
        jump notAcceptedName
    elif mc=="Arnel" or mc=="阿诺尔" or mc=="arnel":
        "“……”"
        "“没门。”"
        jump notAcceptedName
    elif mc=="Serote" or mc=="赛罗特" or mc=="serote":
        "“……”"
        "“我想，你可以试试其他的名字。”"
        jump notAcceptedName
    elif mc=="Halifax" or mc=="Lenton" or mc=="Lentonicus" or mc=="哈利法" or mc=="伦托" or mc=="伦托尼科斯"or mc=="halifax"or mc=="lenton"or mc=="lentonicus":
        "“……”"
        "“啊，我觉得应该不太行……？”"
        jump notAcceptedName
    elif mc=="Creefo" or mc=="Augustus" or mc=="克雷弗" or mc=="奥古斯都"or mc=="creefo"or mc=="augustus":
        "“……”"
        "“哈哈哈哈哈哈——”"
        "“不行。”"
        jump notAcceptedName
    elif mc=="Deci" or mc=="德西"or mc=="deci"or mc=="dc"or mc=="Dc":
        "“……”"
        "“不行。”"
        jump notAcceptedName
    elif mc=="Leviathan" or mc=="利维坦" or mc=="海神"or mc=="leviathan":
        python:
            raise Exception('你不应该起这个名字的。')
        jump acceptedName
    elif mc=="Yuxiu" or mc=="聿修" or mc=="玉秀" or mc=="于秀爱"or mc=="yuxiu"or mc=="yx" or mc=="聿修i":
        "“……”"
        "“你好像有那个什么大病。”"
        jump notAcceptedName
    elif mc=="Halluke" or mc=="哈卢克" or mc=="halluke":
        "“……”"
        "“什么……？”"
        jump notAcceptedName
    elif mc=="Depline" or mc=="德普林" or mc=="depline"or mc=="赤松"or mc=="Akamatsu"or mc=="赤松Akamatsu":
        "“……”"
        "“我其实不喜欢有人和我重名？”"
        jump notAcceptedName
    elif mc=="Acolas" or mc=="阿克拉斯" or mc=="acolas":
        "“……”"
        "“当然——{w}不行！”"
        jump notAcceptedName
    elif True:
        "你的名字是[mc]，确定吗？"
        jump acceptedName

label notAcceptedName:
    menu:
        "取消" if True:
            jump nameYourself

label acceptedName:
    menu:
        "确定" if True:
            jump initplayer
        "取消" if True:
            jump nameYourself

label initplayer:
    $ replaying = False
    $ persistent.beforename = mc
    $ p = Player(name=mc)
    $ WeatherSunny.add(p)
    $ DrugHypnotic.add(p, 5)
    $ DrugColdrex.add(p, 5)
    #$ DrugVitamin.add(p, 2)
    $ Cola.add(p, 3)
    $ SexyPic.add(p, 2)
    $ StreetFood10.add(p, 2)

    $ BookDefault.add(p)
    $ AMaverickLion.add(p)
    $ ProfessionalBookWorking.add(p, 2)
    $ GameDifficulty3.add(p)
    $ Novice.add(p)
    
    
    call screen screen_initplayer(p)
    $ _game_menu_screen = "preferences"

    if persistent.lastend == 'ne':
        $Sticker59.add(p)
        $persistent.lastend = None
    if persistent.lastend == 'te':
        $AppleJuiceSticker.add(p)
        $persistent.lastend = None
    if persistent.lastend == 'ce':
        $ExaminationReport.add(p)
        $persistent.lastend = None

    $ Save.save(p)
    $ Notice.clear()

    jump day0


label to_the_title:
    $renpy.hide('blackmask', layer='mask')
    $renpy.sound.stop(channel="chara_voice")
    $sh()
    call hide_all_screens from _call_hide_all_screens
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
    $ _game_menu_screen = "save"
    return

label testStart:
    $ replaying = False
    $ config.rollback_enabled = False
    $ p = None
    $ Save.clear()
    $ p = Player(name='Solitus')
    $ WeatherSunny.add(p)
    $ DrugHypnotic.add(p, 5)
    $ DrugColdrex.add(p, 5)
    #$ DrugVitamin.add(p, 2)
    $ Cola.add(p, 3)
    $ SexyPic.add(p, 2)
    $ StreetFood10.add(p, 2)
    $ GameDifficulty3.add(p)

    $ BookDefault.add(p)
    $ AMaverickLion.add(p)
    $ ProfessionalBookWorking.add(p, 2)


    $ p.newDay()
    $ p.newDay()
    $ p.newDay()
    $ MedicineA.add(p, 10)
    $ p.mental = 10.0
    $ Novice.add(p)
    $ p.onOutside = False

    $ Save.save(p)
    $ Notice.clear()

    jump wakeup


label test:
    "测试"
    call loading from _call_loading_7
    jump test


label halluke_sprite_test:
    show workarea
    play music audio.halluke
    hide halluke
    '彬彬' "“啊——再喝——”"
    show halluke smile_eyes smile_eyebrow smile_mouth at sprite_appear
    with dissolve
    h "“开玩笑，我超勇的好不好——”"
    show halluke awkward_eyes awkward_eyebrow opened_mouth blush
    with dissolve
    h "“杰哥……你有好多a片哦……”"
    show halluke pants awkward_eyes awkward_eyebrow normal_mouth blush
    with dissolve
    h "“杰哥……这……这什么啊……”"
    show halluke naked angry_eyes angry_eyebrow opened_mouth blush
    with dissolve
    h "“杰哥不要啦！”"
    call loading from _call_loading_2
    jump loop

label acolas_sprite_test:
    show afternoonrun
    play music audio.acolas
    "有一个人前来买瓜。"
    show acolas at sprite_appear
    with dissolve
    a "“哥们儿，这瓜多少钱一斤呐？”"
    show acolas surprised_eyes surprised_eyebrow surprised_mouth blush
    with dissolve
    a "“What's up，这瓜皮子是金子做的，还是瓜粒子是金子做的？”"
    show acolas pants awkward_eyes awkward_eyebrow normal_mouth sweat
    with dissolve
    a "“你这瓜要熟我肯定要啊。那它要是不熟怎么办呀？”"
    show acolas naked angry_eyes angry_eyebrow opened_mouth blush sweat anger
    with dissolve
    a "“你这哪够十五斤哪？你这称有问题啊！”"
    call loading from _call_loading
    jump loop

label bookdont:
    call hide_all_screens from _call_hide_all_screens_2
    $ sh()
    $ _confirm_quit = False
    $ _game_menu_screen = None
    $ _skipping = False
    $ quick_menu = False
    stop music
    scene bs
    $Achievement303.achieve()
    $Achievement.show()
    $renpy.pause()
    $renpy.quit()