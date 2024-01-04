transform screen_name_up():
    yoffset 500
    alpha 0.0
    0.5
    parallel:
        easein 0.75 yoffset 50
    parallel:
        easein 0.75 alpha 1.0

transform screen_name_down():
    yoffset -500
    alpha 0.0
    0.5
    parallel:
        easein 0.75 yoffset -50
    parallel:
        easein 0.75 alpha 1.0

transform screen_init_select_label():
    xoffset -200
    easein .25 xoffset 0

transform screen_name_select_info():
    parallel:
        easein .5 xoffset -1150
    parallel:
        easein .25 alpha 1


init python:
    name_dict = {
            "Solitus":"“真正的名字。”",
            "Pathos":"“……”\n“这个名字已经被我占用了。”\n“还是换一个吧。”",
            "帕索斯":"“……”\n“这个名字已经被我占用了。”\n“还是换一个吧。”",
            "pathos":"“……”\n“这个名字已经被我占用了。”\n“还是换一个吧。”",
            "Decay":"“……”\n“那是我的名字，幼崽。”",
            "德凯":"“……”\n“那是我的名字，幼崽。”",
            "decay":"“……”\n“那是我的名字，幼崽。”",
            "Arnel":"“……”\n“没门。”",
            "阿诺尔":"“……”\n“没门。”",
            "arnel":"“……”\n“没门。”",
            "Serote":"“……”\n“我想，你可以试试其他的名字。”",
            "赛罗特":"“……”\n“我想，你可以试试其他的名字。”",
            "serote":"“……”\n“我想，你可以试试其他的名字。”",
            "Halifax":"“……”\n“啊，我觉得应该不太行……？”",
            "Lenton":"“……”\n“啊，我觉得应该不太行……？”",
            "Lentonicus":"“……”\n“啊，我觉得应该不太行……？”",
            "哈利法":"“……”\n“啊，我觉得应该不太行……？”",
            "伦托":"“……”\n“啊，我觉得应该不太行……？”",
            "伦托尼科斯":"“……”\n“啊，我觉得应该不太行……？”",
            "halifax":"“……”\n“啊，我觉得应该不太行……？”",
            "lenton":"“……”\n“啊，我觉得应该不太行……？”",
            "lentonicus":"“……”\n“啊，我觉得应该不太行……？”",
            "Creefo":"“……”\n“哈哈哈哈哈哈——”\n“不行。”",
            "Augustus":"“……”\n“哈哈哈哈哈哈——”\n“不行。”",
            "克雷弗":"“……”\n“哈哈哈哈哈哈——”\n“不行。”",
            "奥古斯都":"“……”\n“哈哈哈哈哈哈——”\n“不行。”",
            "creefo":"“……”\n“哈哈哈哈哈哈——”\n“不行。”",
            "augustus":"“……”\n“哈哈哈哈哈哈——”\n“不行。”",
            "Deci":"“……”\n“不行。”",
            "德西":"“……”\n“不行。”",
            "deci":"“……”\n“不行。”",
            "dc":"“……”\n“不行。”",
            "Dc":"“……”\n“不行。”",
            "Yuxiu":"“……”\n“你好像有那个什么大病。”",
            "聿修":"“……”\n“你好像有那个什么大病。”",
            "玉秀":"“……”\n“你好像有那个什么大病。”",
            "于秀爱":"“……”\n“你好像有那个什么大病。”",
            "yuxiu":"“……”\n“你好像有那个什么大病。”",
            "yx":"“……”\n“你好像有那个什么大病。”",
            "聿修i":"“……”\n“你好像有那个什么大病。”",
            "yxi":"“……”\n“你好像有那个什么大病。”",
            "Inufuto":"“你以后不许看立绘。”",
            "inufuto":"“你以后不许看立绘。”",
            "电狗":"“你以后不许看立绘。”",
            "点购":"“你以后不许看立绘。”",
            "电子幽灵犬":"“你以后不许看立绘。”",
            "电鬼狗":"“你以后不许看立绘。”",
            "电电":"“你以后不许看立绘。”",
            "点点":"“你以后不许看立绘。”",
            "diangou":"“你以后不许看立绘。”",
            "Halluke":"“……”\n“什么……？”",
            "哈卢克":"“……”\n“什么……？”",
            "halluke":"“……”\n“什么……？”",
            "Depline":"“……”\n“那还真是巧呢？”",
            "德普林":"“……”\n“那还真是巧呢？”",
            "depline":"“……”\n“那还真是巧呢？”",
            "赤松":"“……”\n“那还真是巧呢？”",
            "Akamatsu":"“……”\n“那还真是巧呢？”",
            "赤松Akamatsu":"“……”\n“那还真是巧呢？”",
            "Acolas":"“……”\n“当然——{w}不行！”",
            "阿克拉斯":"“……”\n“当然——{w}不行！”",
            "acolas":"“……”\n“当然——{w}不行！”",
            "德斯托特":"“是前辈也不行！”",
            "Destot":"“是前辈也不行！”",
        }

screen screen_name_select(player):
    tag menu
    if renpy.android:
        default nameinfo = "那么，请告诉我该如何称呼你。\n{size=-4}（手机用户可以复制中文再粘贴。）{/size}"
    else:
        default nameinfo = "那么，请告诉我该如何称呼你。"
    default name = persistent.beforename
    default okflag = False
    default info = ''
    default tempname = ''
    $ playerinfo = '你。\n'
    add persistent.main_menu_theme.bg

    add "gui/overlay/confirm.png"


        

    python:
        

        def getnameinfo(name):
            
            if name in name_dict:
                return name_dict[name]
            if len(name) == 0:
                return "真正的名字。"
            if name.isdecimal():
                return "看样子你很喜欢数字。"
            if len(set(name)) == 1:
                return "非常高效的名字。"
            if name == 'a':
                return '好吧，如果你真的喜欢这个名字的话。'
            if name in ('abc', 'abcd', 'abcde'):
                return '非常有创造性。'
            if name in ('sb', '啥比', '傻逼'):
                return '……嗯，如果你愿意称自己为这个名字的话。'
            if name in ('name', 'Name', '名字'):
                return '是的，这是一个……名字。'
            if len(name) == 1:
                return "真是简短的名字。"
            if len(name) == 2:
                return "简短而不失优雅。"
            if len(name) == 3:
                return "嗯……这是个不错的名字。"
            if len(name) == 20:
                return "是的，这是最长的名字了，你应该去写一本小说。"
            return "十分优秀的名字。"
        
        def getnameok(name):
            if name == "Solitus":
                return True
            if name in name_dict:
                return False
            return True

        if player.experience == 'wor':
            initpic = "images/gui/opening/work_%s.webp"
            playerinfo += '作为一个普通、庸常、且随处可见的都市人，'
        elif player.experience == 'wri':
            initpic = "images/gui/opening/write_%s.webp"
            playerinfo += '作为一位全职作家，离开了公司，'
        elif player.experience == 'cos':
            initpic = "images/gui/opening/cos_%s.webp"
            playerinfo += '不被定义的你，'

        if GameDifficulty1.has(player):
            diffpic = "images/gui/opening/1_%s.webp"
            playerinfo += '行走于惬意的{color=#ff9900}旅途{/color}之中……'
        elif GameDifficulty2.has(player):
            diffpic = "images/gui/opening/2_%s.webp"
            playerinfo += '走在{color=#7FFF00}轻松{/color}愉快的道路之上……'
        elif GameDifficulty3.has(player):
            diffpic = "images/gui/opening/3_%s.webp"
            playerinfo += '投身于{color=#87CEEB}平凡{/color}的生活……'
        elif GameDifficulty4.has(player):
            diffpic = "images/gui/opening/4_%s.webp"
            playerinfo += '即将体会{color=#FF0000}艰辛{/color}的路途……'
        elif GameDifficulty5.has(player):
            diffpic = "images/gui/opening/5_%s.webp"
            playerinfo += '来到了{color=#c000da}地狱{/color}。'



    vbox:
        xalign 0.05
        ycenter 0.5
        textbutton "最后一步":
            text_style "white" 
            text_size 60 
            yoffset -30 
            xoffset 20
            at screen_init_select_label
        hbox:
            imagebutton auto initpic:
                action NullAction()
                activate_sound audio.card2
                at screen_name_up
            imagebutton auto diffpic:
                action NullAction()
                activate_sound audio.card2
                xoffset -100
                at screen_name_down
                    
    frame at screen_name_select_info:
        xsize 1100
        ysize 700
        xpos 1920
        ycenter 0.5
        yoffset 45
        background Frame("gui/style/grey_idle_background.png", tile=gui.frame_tile)
        
        vbox:
            textbutton playerinfo:
                text_style "white" 
                text_size 25

            null height 15

            textbutton nameinfo:
                text_style "white" 
                text_size 25

            null height 15

            input:
                length 20
                exclude "\"\'[]{}%$@?!#^&*\(\)"
                value ScreenVariableInputValue("name")
                style "white"
                size 40
                copypaste True
                xoffset 10

        if name in ("Leviathan", "利维坦", "海神","leviathan"):
            $renpy.quit()

        if okflag and getnameok(name) and tempname == name:
            imagebutton auto "images/gui/opening/ok_%s.png":
                action Function(setattr, player, "name", name), SetVariable("p", player), Start()
                xalign 0.9
                yalign 0.95
                activate_sound audio.click1

        else:
            if renpy.android:
                $nameinfo = "那么，请告诉我该如何称呼你。\n{size=-4}（手机用户可以复制中文再粘贴。）{/size}"
            else:
                $nameinfo = "那么，请告诉我该如何称呼你。"
            $okflag = False
            imagebutton auto "images/gui/opening/test_%s.png":
                if len(name) == 0:
                    action SetLocalVariable("name", "Solitus"), SetLocalVariable("tempname", "Solitus"), SetLocalVariable("nameinfo", getnameinfo("Solitus")), SetLocalVariable("okflag", True)
                else:
                    action SetLocalVariable("tempname", name), SetLocalVariable("nameinfo", getnameinfo(name)), SetLocalVariable("okflag", getnameok(name))
                xalign 0.9
                yalign 0.95
                activate_sound audio.click1

    
        
    
    imagebutton auto "gui/exit_%s.png":
        xalign 0.95
        yalign 0.05
        action Return()
    
    key 'K_ESCAPE' action Hide("info"),Return()










    


screen screen_rename(player):


    if renpy.android:
        default nameinfo = "输入你想修改的名字。\n{size=-4}（手机用户可以复制中文再粘贴。）{/size}"
    else:
        default nameinfo = "输入你想修改的名字。"
    default name = player.name
    default okflag = False
    default info = ''
    default tempname = ''   
    default badname = False  

    python:
                
        def getnameok(name):
            if name == "Solitus":
                return True
            if name in name_dict:
                return False
            return True

        def rename(player, name):
            if not FishingItem1.has(player):
                showNotice(['你没有命名牌！'])
                return
            FishingItem1.get(player).sub(player)
            oldname = player.name
            player.name = name
            for name in player.messages:
                for mes in player.messages[name]:
                    if mes.fro == oldname:
                        mes.fro = player.name


    style_prefix "transparent"


    frame at tdissolve:
        xalign .5
        yalign .5
        padding (60, 40)
        background '#0000004f'

        has vbox:
            xalign .5
            yalign .5
            spacing 45

        label "请输入要修改的名字。":
            style "confirm_prompt"
            xalign 0.5

        if okflag:
            label "{size=-3}{color=#00ff00}这是一个可用的名字。{/size}{/color}":
                style "confirm_prompt"
                xalign 0.5
        elif not getnameok(name) and tempname == name:
            label "{size=-3}{color=#ff0000}这个名字不可用。{/size}{/color}":
                style "confirm_prompt"
                xalign 0.5

        input:
            length 20
            exclude "\"\'[]{}%$@?!#^&*\(\)"
            value ScreenVariableInputValue("name")
            style "white"
            size 40
            copypaste True
            xoffset 10

        if name in ("Leviathan", "利维坦", "海神","leviathan"):
            $renpy.quit()

        hbox:
            xalign 0.5
            spacing 150



            if okflag and getnameok(name) and tempname == name:
                textbutton _("{size=-3}确定{/size}"):
                    action Function(rename, player, name),Hide("screen_rename",transition=dissolve)
                    xalign 0.9
                    yalign 0.95
                    activate_sound audio.click1

            else:
                $okflag = False
                textbutton _("{size=-3}检查{/size}"):
                    if len(name) == 0:
                        action SetLocalVariable("name", "Solitus"), SetLocalVariable("tempname", "Solitus"), SetLocalVariable("okflag", True)
                    else:
                        action SetLocalVariable("tempname", name), SetLocalVariable("okflag", getnameok(name))
                    xalign 0.9
                    yalign 0.95
                    activate_sound audio.click1

            textbutton _("{size=-3}取消{/size}") action Hide("screen_rename",transition=dissolve)


    key "game_menu" action Hide("screen_rename",transition=dissolve)