




define CREDITS_SIZE = 4300
define CREDITS_TIME = 28

transform credits_scroll(speed):
    ypos 900
    linear speed ypos (CREDITS_SIZE * -1)

screen credits():
    style_prefix "credits"

    add "#000"

    frame at credits_scroll(CREDITS_TIME):
        background None
        xalign 0.5

        has vbox

        null height 350

        label "{color=#ffffff}{size=+30}{font=C.ttf}药：绝望的解决手段" xalign 0.5
        label "{color=#ffffff}{size=+20}{font=C.ttf}Medicine: The Remedy of Sheer Desperation" xalign 0.5

        null height 500

        label "{color=#ffffff}主创" xalign 0.0
        label "{color=#ffffff}Producer" xalign 0.0

        null height 25

        label "{color=#ffffff}聿修" xalign 1.0

        null height 150

        label "{color=#ffffff}文案" xalign 0.0
        label "{color=#ffffff}Script Writers" xalign 0.0

        null height 25

        label "{color=#ffffff}聿修" xalign 1.0
        label "{color=#ffffff}Halifax" xalign 1.0

        null height 150

        label "{color=#ffffff}程序" xalign 0.0
        label "{color=#ffffff}Programer" xalign 0.0

        null height 25

        label "{color=#ffffff}聿修" xalign 1.0

        null height 150

        label "{color=#ffffff}画师" xalign 0.0
        label "{color=#ffffff}Sprite Artist" xalign 0.0

        null height 25

        label "{color=#ffffff}Inufuto" xalign 1.0
        label "{color=#ffffff}EmoFox" xalign 1.0
        
        null height 150

        label "{color=#ffffff}测试" xalign 0.0
        label "{color=#ffffff}Testing" xalign 0.0

        null height 25

        label "{color=#ffffff}ELiK\tAster\t罗瞑Roming" xalign 1.0
        label "{color=#ffffff}BZQDTCYY\tAcosluc\tL.catter" xalign 1.0
        label "{color=#ffffff}竹隐狴犴\t无忧可解？\tJanus" xalign 1.0
        label "{color=#ffffff}蕈影\tutcl雏灯\t-vicus\t白泽" xalign 1.0
        label "{color=#ffffff}Ylonw\t永远的wwk迷弟" xalign 1.0
        label "{color=#ffffff}以及为游戏提出过BUG的各位玩家" xalign 1.0

        null height 150

        label "{color=#ffffff}背景图片" xalign 0.0
        label "{color=#ffffff}BG Material" xalign 0.0

        null height 25

        label "{color=#ffffff}Unsplash" xalign 1.0
        label "{color=#ffffff}Pexels" xalign 1.0
        label "{color=#ffffff}FotoSketcher" xalign 1.0

        null height 150

        label "{color=#ffffff}背景音乐" xalign 0.0
        label "{color=#ffffff}BGM" xalign 0.0

        null height 25

        label "{color=#ffffff}FreePD" xalign 1.0

        null height 150

        label "{color=#ffffff}游戏音效" xalign 0.0
        label "{color=#ffffff}Sounds" xalign 0.0

        null height 25

        label "{color=#ffffff}Freesound" xalign 1.0
        label "{color=#ffffff}淘声网" xalign 1.0
        label "{color=#ffffff}耳聆网" xalign 1.0

        null height 150

        label "{color=#ffffff}特别感谢" xalign 0.0
        label "{color=#ffffff}Special Thanks" xalign 0.0

        null height 25

        label "{color=#ffffff}Endorphins频道全体成员" xalign 1.0
        label "{color=#ffffff}指路本游戏的频道" xalign 1.0
        label "{color=#ffffff}宣传这个游戏的玩家" xalign 1.0

        null height 25

        label "{color=#ffffff}还有你" xalign 1.0

        null height 1000

        label "{color=#ffffff}{size=+30}感谢游玩！" xalign 0.5
        label "{color=#ffffff}{size=+20}Thanks for Playing!" xalign 0.5

        null height 100

        label "{color=#ffffff}2023/5/20 version 0.4.16" xalign 0.5

        null height 1000


    timer CREDITS_TIME+5 action Return()
    key "button_select" action Confirm("是否跳过？", Return())

label credits:
    $ quick_menu = False
    $ clearscreens()
    if renpy.music.get_playing() in (None, audio.themedicine):
        play music audio.credits fadein 3
    call screen credits
    stop music fadeout 3
    $ quick_menu = True
    return
