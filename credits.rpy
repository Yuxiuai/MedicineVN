
#####################################################################################
#鸣谢
#####################################################################################

define CREDITS_SIZE = 3500
define CREDITS_TIME = 30

transform credits_scroll(speed):
    ypos 800
    linear speed ypos (CREDITS_SIZE * -1)

screen credits():
    style_prefix "credits"

    add "#000"

    frame at credits_scroll(CREDITS_TIME):
        background None
        xalign 0.5

        vbox:

            label "{color=#ffffff}{size=+30}{font=C.ttf}药：绝望的解决手段" xalign 0.5
            label "{color=#ffffff}{size=+20}{font=C.ttf}The Remedy of Sheer Desperation" xalign 0.5

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

            #null height 150

            #label "{color=#ffffff}翻译" xalign 0.0
            #label "{color=#ffffff}Translator" xalign 0.0

            #null height 25

            #label "{color=#ffffff}聿修" xalign 1.0

            null height 150

            label "{color=#ffffff}测试" xalign 0.0
            label "{color=#ffffff}Test Engineers" xalign 0.0

            null height 25

            label "{color=#ffffff}ELiK" xalign 1.0
            label "{color=#ffffff}Aster" xalign 1.0
            label "{color=#ffffff}罗瞑Roming" xalign 1.0
            label "{color=#ffffff}BZQDTCYY" xalign 1.0

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

            null height 1000

            label "{color=#ffffff}{size=+30}感谢游玩！" xalign 0.5
            label "{color=#ffffff}{size=+20}Thanks for Playing!" xalign 0.5

            null height 100

            label "{color=#ffffff}2022/x/xx version 0.4.2" xalign 0.5


    timer CREDITS_TIME+5 action Return()
    key "button_select" action Confirm("是否跳过？", Return())

label credits:
    $ quick_menu = False
    play music audio.credits fadein 3
    call screen credits
    stop music fadeout 3
    scene black with dissolve
    $ renpy.pause(delay=3,hard=True)
    $ quick_menu = True
    jump to_the_title