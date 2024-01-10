transform screen_diff_select_color_default:
    easein 1 matrixcolor ColorizeMatrix('#000', '#fff')

transform screen_diff_select_color_active(color):
    easein 2 matrixcolor ColorizeMatrix('#000', color)

screen screen_diff_select(player, mode=1):
    tag menu
    python:
        diff_dict = ["选择游戏难度", "{color=#ff9900}旅途{/color}", "{color=#7FFF00}简单{/color}", "{color=#87CEEB}一般{/color}", "{color=#FF0000}硬核{/color}", "{color=#c000da}地狱{/color}"]
        color_dict = [
            "", "#ff9900", "#7FFF00", "#87CEEB", "#FF0000", "#c000da"
        ]
        info_dict = [
            "",
            "你可以在一天开始时选择快进游戏至某天，并将精神状态恢复至100，适合只想快速浏览剧情的玩家。\n\n相对于一般难度，有以下内容不同：\n\n{color=#ffff00}包含了所有简单难度的额外内容。\n游戏结束时，不会记录通关分数和通关次数，下一次游戏也不会获得结局的特殊道具。\n\n{color=#ff0000}至少需要通关一次游戏才能选择此难度。\n仅在游戏开始时可选择该难度。\n切换为该难度之后，在该存档内无法再切换难度。{/color}",
            "不用关心大多数的游戏内容，适合只想观看剧情且还想简单体验一下养成内容的玩家。\n\n相对于一般难度，有以下内容不同：\n\n{color=#ffff00}可以随时更改已制定好的日程。\n所有基础能力属性的获取加成提升2点。\n不会获得酸痛和药物依赖效果。\n灵感将在一天结束后自动转化为写作素材。\n合理用药恢复严重程度的概率提升50%\n伤痕不再是永久状态，持续14天。{/color}\n\n难度可以随时切换。",
            "体验标准风格的本游戏，体验主角在生死边缘徘徊的痛苦和绝望，在游玩中逐渐了解这个游戏的各种玩法。\n\n{color=#7FFF00}推荐新玩家游玩该难度。{/color}\n\n难度可以随时切换。",
            "不建议还没有完全了解本游戏的玩家尝试，不过第四日程的存在让游戏的玩法发生了些许改变。\n如果你已经通关了一次游戏，那么可以试试这个难度。\n\n相对于一般难度，有以下内容不同：\n\n{color=#ffff00}允许在一天结束前进行额外的操作，其中包含进行本日的第四个日程。\n允许外出至两个地点。\n过劳和偏执会因为层数过高而转化，并非只在4层及以上时才转化。\n出现更多种类的天气，天气会随时间有概率变化。\n过夜提升的严重程度翻倍。\n当你进行日程时，有5%的概率获得突发头疼。\n食用食物有5%的概率获得腹痛。\n一天内没有食用正餐则大概率获得营养不良。\n外卖商品有10%的概率无法购买。{/color}\n\n难度可以随时切换。",
            "几乎无法完成的难度，能够选择该难度坚持到结局的只有寥寥数人。\n如果你想征服这个游戏，就来试试最高难度吧！\n\n相对于一般难度，有以下内容不同：\n\n{color=#ffff00}包含了所有硬核难度的额外内容。\n每完成一个日程后消耗1%~20%的当前精神状态。\n购买道具时提升20%的价格。\n过夜后工作能力，身体素质，写作技巧各有50%的概率失去1点。\n过夜后有概率失去1~10%的当前金钱。\n每周需要完成的工作目标提升4%*周数。\n过夜后有33%的概率提升随机一种已经使用过的药物的抗药性。\n过夜有33%概率流失1层体魄，有100%概率流失1层灵感。\n当你获得伤痕时，在第二天进入死亡结局。\n游玩全职小说家出身时，获得灵感不会恢复精神而是会消耗精神。{/color}\n\n{color=#ff0000}仅在游戏开始时可选择该难度。\n切换为该难度之后，在该存档内无法再切换难度。{/color}",
        ]
        function_dict = [
            '',
            lambda p: GameDifficulty1.add(p),
            lambda p: GameDifficulty2.add(p),
            lambda p: GameDifficulty3.add(p),
            lambda p: GameDifficulty4.add(p),
            lambda p: GameDifficulty5.add(p),
        ]


    if GameDifficulty1.has(player):
        default selected = 1
    elif GameDifficulty2.has(player):
        default selected = 2
    elif GameDifficulty3.has(player):
        default selected = 3
    elif GameDifficulty4.has(player):
        default selected = 4
    elif GameDifficulty5.has(player):
        default selected = 5
    else:
        default selected = 0

    imagebutton idle "images/gui/opening/bg.webp":
        if selected == 0:
            at screen_diff_select_color_default
        else:
            at screen_diff_select_color_active(color_dict[selected])
    vbox:
        xcenter 0.5
        ycenter 0.5
        textbutton diff_dict[selected]:
            text_style "white" 
            text_size 60 
            yoffset -30 
            xoffset 20
            at screen_init_select_label()

        hbox:
            imagebutton auto "images/gui/opening/1_%s.webp":
                if selected == 0:
                    action SetLocalVariable("selected", 1)
                    activate_sound audio.card1
                    at screen_init_select_default
                elif selected == 1:
                    action SetLocalVariable("selected", 0)
                    at screen_init_select_move_to_left(0)
                    activate_sound audio.card2
                else:
                    at screen_init_select_hide
            imagebutton auto "images/gui/opening/2_%s.webp":
                if selected == 0:
                    action SetLocalVariable("selected", 2)
                    activate_sound audio.card1
                    at screen_init_select_default
                elif selected == 2:
                    action SetLocalVariable("selected", 0)
                    at screen_init_select_move_to_left(370)
                    activate_sound audio.card2
                else:
                    at screen_init_select_hide
                    
            imagebutton auto "images/gui/opening/3_%s.webp":
                if selected == 0:
                    action SetLocalVariable("selected", 3)
                    activate_sound audio.card1
                    at screen_init_select_default
                elif selected == 3:
                    action SetLocalVariable("selected", 0)
                    at screen_init_select_move_to_left(730)
                    activate_sound audio.card2
                else:
                    at screen_init_select_hide

            imagebutton auto "images/gui/opening/4_%s.webp":
                if selected == 0:
                    action SetLocalVariable("selected", 4)
                    activate_sound audio.card1
                    at screen_init_select_default
                elif selected == 4:
                    action SetLocalVariable("selected", 0)
                    at screen_init_select_move_to_left(1090)
                    activate_sound audio.card2
                else:
                    at screen_init_select_hide

            imagebutton auto "images/gui/opening/5_%s.webp":
                if selected == 0:
                    action SetLocalVariable("selected", 5)
                    activate_sound audio.card1
                    at screen_init_select_default
                elif selected == 5:
                    action SetLocalVariable("selected", 0)
                    at screen_init_select_move_to_left(1440)
                    activate_sound audio.card2
                else:
                    at screen_init_select_hide
                    
    if selected != 0:    
        frame at screen_init_select_info:
            xsize 1300
            ysize 700
            xpos 1920
            ycenter 0.5
            yoffset 45
            background Frame("gui/style/grey_idle_background.png", tile=gui.frame_tile)

            vbox:
                textbutton info_dict[selected]:
                    text_style "white" 
                    text_size 25

            imagebutton auto "images/gui/opening/back_%s.png":
                action SetLocalVariable("selected", 0)
                xalign 0.1
                yalign 0.95
                activate_sound audio.card2

            $hasok = True
            if selected in (1, 5) and mode == 1:
                $hasok = False

            if GameDifficulty1.has(player) or GameDifficulty5.has(player):
                $hasok = False

            if hasok:
                imagebutton auto "images/gui/opening/ok_%s.png":
                    if mode != 1:
                        action Function(function_dict[selected], player), ShowMenu("screen_name_select", player)
                    elif selected != 0:
                        action Function(function_dict[selected], player), Return()
                    else:
                        action NullAction()
                    xalign 0.9
                    yalign 0.95
                    activate_sound audio.click1
    
    imagebutton auto "gui/exit_%s.png":
        xalign 0.95
        yalign 0.05
        if mode != 1:
            action Return()
        else:
            action ShowMenu("screen_gamemenu", player)
    key 'K_ESCAPE' action Hide("info"),Return()
