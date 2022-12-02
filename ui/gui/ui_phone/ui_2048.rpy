init python:
    score = 0

    def game2048_geticon(num):
        return "gui/phone/2048/" + str(num) + ".png"

    def game2048_newgame(blocks):
        global score
        if score > persistent.highestscore2048:
            persistent.highestscore2048 = score 
        score = 0
        for i in blocks:
            blocks[i] = 0
        game2048_newblock(blocks)

    def game2048_newblock(blocks):
        emptyblocks = list(filter(lambda x: blocks[x]==0, blocks))
        if emptyblocks != []:
            blocks[rcd(emptyblocks)] = rcd((2,2,2,2,4))
        else:
            if score > persistent.highestscore2048:
                persistent.highestscore2048 = score 

    game2048_d = {
        'up':(-1,0),
        'down':(1,0),
        'left':(0,-1),
        'right':(0,1)
    }

    def game2048_getnext(str,to):
        move = game2048_d[to]
        next_block = "%s%s" % (chr(ord(str[0]) + move[0]), chr(ord(str[1]) + move[1]))

        if len(next_block)==2 and next_block in '41121314223243344':
            return next_block
        else:
            return -1

        
    def game2048_moveable(i, blocks, fun):
        if fun(i) == -1:
            return False
        elif blocks[fun(i)] != 0 or blocks[i] != blocks[fun(i)]:
            return False
        else:
            return True

    def game2048_move(blocks, to):
        global score
        fun = lambda x:game2048_getnext(x,to)
        moveableblocks = []
        while True:
            temp_blocks = dcp(blocks)
            for i in blocks:
                if blocks[i] != 0 and fun(i) != -1:
                    moveableblocks.append(i)
            for i in moveableblocks:
                if blocks[fun(i)] == 0:
                    blocks[fun(i)] = blocks[i]
                    blocks[i] = 0
                elif blocks[i] == blocks[fun(i)]:
                    blocks[fun(i)] *= 2
                    score += blocks[fun(i)]
                    blocks[i] = 0
            if temp_blocks == blocks:
                break

        game2048_newblock(blocks)

screen screen_phone_bg_y():
    modal True
    style_prefix "gameUI"
    zorder 100
    
    frame:
        background None
        xcenter 0.5
        ycenter 0.5
        ysize 750
        xsize 400
        
        add "gui/phone/2048/phone_yellow.png":
            xcenter 0.51
            ycenter 0.46

screen screen_phone_2048(player):
    #tag gamegui
    modal True
    style_prefix "gameUI"
    zorder 100
    #use screen_phone_bg_y 
    frame:
        at trans_app(-150, 50)
        background None
        xcenter 0.5
        ycenter 0.5
        ysize 750
        xsize 400
        
        add "gui/phone/2048/phone_yellow.png":
            xcenter 0.51
            ycenter 0.46

        frame:
            
            background None
            xalign 0.5
            yalign 0.55
            ysize 750
            xsize 400

            #add "gui/phone/2048/phone_yellow.png":
            #    xcenter 0.5
            #    ycenter 0.45
            add "gui/phone/2048/gameback.png":
                xcenter 0.5
                ycenter 0.45

            default blocks = {
                '11':0,
                '12':0,
                '13':0,
                '14':0,

                '21':0,
                '22':0,
                '23':0,
                '24':0,

                '31':0,
                '32':0,
                '33':0,
                '34':0,

                '41':0,
                '42':0,
                '43':0,
                '44':0
            }

            $global score




            frame:
                ypos 165
                xpos 5
                background None
                vbox:
                    spacing 2
                    hbox:
                        spacing 2
                        for i in ('11', '12', '13', '14'):
                            $icon = game2048_geticon(blocks[i])
                            imagebutton idle icon:
                                action NullAction()

                    hbox:
                        spacing 2
                        for i in ('21', '22', '23', '24'):
                            $icon = game2048_geticon(blocks[i])
                            imagebutton idle icon:
                                action NullAction()

                    hbox:
                        spacing 2
                        for i in ('31', '32', '33', '34'):
                            $icon = game2048_geticon(blocks[i])
                            imagebutton idle icon:
                                action NullAction()

                    hbox:
                        spacing 2
                        for i in ('41', '42', '43', '44'):
                            $icon = game2048_geticon(blocks[i])
                            imagebutton idle icon:
                                action NullAction()

            frame:
                background None
                xalign 0.835
                yalign 0.12
                xsize 105
                $info = '曾获得的最高分：' + str(persistent.highestscore2048)
                $ad = '真的有人会玩游戏里的游戏吗？'
                textbutton str(score):#str(blocks['score']):
                    xalign 0.5
                    action [Hide("info"),Show(screen="info_use", pp=renpy.get_mouse_pos(), i=info, a=ad)]
                    hovered Show(screen="info", i=info, a=ad)
                    unhovered Hide("info")
                    style "white"

            frame:
                background None
                ypos 0.73
                textbutton "{color=000000}{size=-10}{font=SourceHanSansLite.ttf}R键开始游戏，方向键操作。":
                    action NullAction()


            frame:
                background None
                xpos 0.8
                ypos 0.83
                imagebutton auto "gui/phone/back_%s.png":
                    action [Hide("screen_phone_2048"),Hide("info"),Show(screen="screen_phone", player=player)]
                    hover_sound audio.cursor

    if not renpy.variant("pc"):
        frame:
            background None
            xcenter 0.7
            ycenter 0.6
            vbox:
                hbox:
                    xalign 0.5
                    imagebutton auto "gui/phone/2048/w_%s.png":
                        action Function(game2048_move, blocks, 'up')
                        activate_sound audio.sfx2048
    
                hbox:
                    imagebutton auto "gui/phone/2048/a_%s.png":
                        action Function(game2048_move, blocks, 'left')
                        activate_sound audio.sfx2048

                    imagebutton auto "gui/phone/2048/s_%s.png":
                        action Function(game2048_move, blocks, 'down')
                        activate_sound audio.sfx2048

                    imagebutton auto "gui/phone/2048/d_%s.png":
                        action Function(game2048_move, blocks, 'right')
                        activate_sound audio.sfx2048
        frame:
            background None
            xcenter 0.7
            ycenter 0.3

            imagebutton auto "gui/phone/2048/r_%s.png":
                action Function(game2048_newgame, blocks)
                activate_sound audio.sfx2048


    key "K_UP" action [Function(game2048_move, blocks, 'up'), Function(play_audio, audio.sfx2048)]
    key "K_DOWN" action [Function(game2048_move, blocks, 'down'), Function(play_audio, audio.sfx2048)]
    key "K_RIGHT" action [Function(game2048_move, blocks, 'right'), Function(play_audio, audio.sfx2048)]
    key "K_LEFT" action [Function(game2048_move, blocks, 'left'), Function(play_audio, audio.sfx2048)]
    key 'r' action [Function(game2048_newgame, blocks), Function(play_audio, audio.sfx2048)]
    key 'K_ESCAPE' action [Hide("screen_phone_2048"),Hide("info"),Show(screen="screen_phone", player=player)]