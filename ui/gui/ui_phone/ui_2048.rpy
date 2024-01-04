init python:
    score = 0
    game2048_log = None

    def game2048_scoredefault():
        global score
        if score > persistent.highestscore2048:
            persistent.highestscore2048 = score 
        score = 0

    def game2048_geticon(num):
        if num > 524288:
            return "gui/phone/2048/999999.png"
        return "gui/phone/2048/%s.png" % num

    def game2048_newgame(blocks):
        global score
        for i in blocks:
            blocks[i] = 0
        game2048_scoredefault()
        game2048_newblock(blocks)

    def game2048_newblock(blocks):
        global score
        emptyblocks = list(filter(lambda x: blocks[x]==0, blocks))
        if emptyblocks != []:
            blocks[rcd(emptyblocks)] = rcd((2,2,2,2,4))
            #blocks[rcd(emptyblocks)] = 32
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
                elif blocks[i] == blocks[fun(i)] and blocks[fun(i)] <= 524288:
                    blocks[fun(i)] *= 2
                    if blocks[fun(i)] == 2048:
                        Achievement307.achieve()
                        Achievement.show()
                        Notice.show()
                    score += blocks[fun(i)]
                    blocks[i] = 0
            if temp_blocks == blocks:
                break

        game2048_newblock(blocks)


screen screen_phone_2048_block(b):
    imagebutton idle game2048_geticon(b):
        action NullAction()
 
screen screen_phone_2048(player):
    
    predict False
    style_prefix "gameUI"
    zorder 600
    
    frame:
        
        if phone_page == 1:
            at app_inner_show(-220, -65)
        else:
            at app_inner_hide(-220, -65)

        
        background None
        xcenter 0.5
        ycenter 0.5
        yoffset -10
        
        use barrier('', 0)

        add "gui/phone/wallpaper/2048.webp":
            xcenter 0.5

        

        frame:
            
            background None
            xalign 0.5
            yalign 0.55
            ysize 1300
            xsize 582

            #add "gui/phone/2048/phone_yellow.png":
            #    xcenter 0.5
            #    ycenter 0.45

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
                ypos 306
                xpos 3
                background None
                vbox:
                    spacing 2
                    hbox:
                        spacing 2
                        for i in ('11', '12', '13', '14'):
                            use screen_phone_2048_block(blocks[i])
                                

                    hbox:
                        spacing 2
                        for i in ('21', '22', '23', '24'):
                            use screen_phone_2048_block(blocks[i])
                                

                    hbox:
                        spacing 2
                        for i in ('31', '32', '33', '34'):
                            use screen_phone_2048_block(blocks[i])
                                

                    hbox:
                        spacing 2
                        for i in ('41', '42', '43', '44'):
                            use screen_phone_2048_block(blocks[i])
                                

            frame:
                background None
                xpos 0.805
                xanchor 0.5
                ypos 0.09
                xsize 200
                text str(max(persistent.highestscore2048, score)) xalign 0.5 style "white"
                

            frame:
                background None
                xpos 0.805
                xanchor 0.5
                ypos 0.174
                xsize 200
                text str(score) xalign 0.5 style "white"
                


            frame:
                background None
                xpos 0.03
                ypos 0.06
                imagebutton auto "gui/phone/back_%s.png":
                    action Function(game2048_scoredefault), SetVariable("phone_page", 0)
                    hover_sound audio.cursor

            if not renpy.variant("pc"):
                frame:
                    background None
                    xpos 1.5
                    ypos 0.45
                    xanchor 0.5
                    vbox:
                        spacing 40
                        hbox:
                            xalign 0.5
                            imagebutton auto "gui/phone/2048/w_%s.png":
                                action Function(game2048_move, blocks, 'up')
                                activate_sound audio.sfx2048
            
                        hbox:
                            spacing 40
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
                    xpos 1.5
                    ypos 0.1
                    xanchor 0.5

                    imagebutton auto "gui/phone/2048/r_%s.png":
                        action Function(game2048_newgame, blocks)
                        activate_sound audio.sfx2048

    key "K_UP" action [Function(game2048_move, blocks, 'up'), Function(play_audio, audio.sfx2048)]
    key "K_DOWN" action [Function(game2048_move, blocks, 'down'), Function(play_audio, audio.sfx2048)]
    key "K_RIGHT" action [Function(game2048_move, blocks, 'right'), Function(play_audio, audio.sfx2048)]
    key "K_LEFT" action [Function(game2048_move, blocks, 'left'), Function(play_audio, audio.sfx2048)]
    key 'r' action [Function(game2048_newgame, blocks), Function(play_audio, audio.sfx2048)]
    key 'K_ESCAPE' action Function(game2048_scoredefault),SetVariable("phone_page", 0)