transform ui_save_choose_color:
    matrixcolor ColorizeMatrix('#000', '#fff')
    easein 0.5 matrixcolor ColorizeMatrix('#000', '#9500ff')


image save_ce:
    "gui/save/noise1.jpg"
    0.1
    "gui/save/noise2.jpg"
    0.1
    "gui/save/noise3.jpg"
    0.1
    "gui/save/noise4.jpg"
    0.1
    repeat


define newname = ''
screen screen_gamemenu_save(player=p):
    zorder 2001
    if persistent.savefile:
        default savei = len(persistent.savefile)-1
        default savej = len(persistent.savefile[savei])-1

        if savei >= len(persistent.savefile):
            $savei = len(persistent.savefile)-1
            $savej = len(persistent.savefile[savei])-1
    
    
    tag menu
    style_prefix "game_menu"

    add persistent.main_menu_theme.bg

    frame:
        bottom_padding 45
        top_padding 180
        background "gui/overlay/confirm.png"
        frame:
            background None
            xfill True
            xpos 0.125
            if not persistent.savefile:
                text "尚未拥有存档。" style "white"
            else:

                hbox:

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        #xfill True
                        xsize 700
                        #side_yfill True
                    
                        frame:
                            style_prefix "save"
                            xfill True
                            background None
                            vbox:
                                spacing 10
                                box_reverse True
                                for i in range(len(persistent.savefile)):
                                        
                                    vbox:
                                        box_reverse True
                                        spacing 10
                                        for j in range(len(persistent.savefile[i])):
                                            python:
                                                savep = persistent.savefile[i][j].p
                                                savename = _('空存档')
                                                if savep:
                                                    if savep.cured > -1:
                                                        savename = _('⎟手术后的第[savep.cured]天')
                                                    elif Despair.has(savep):
                                                        savename = _('⎟废墟下的第[savep.finalStageDays]天')
                                                    else:
                                                        weekday = weekdayFormat(savep.today)
                                                        savename = _('⎟第[savep.week]周⎟[weekday]')
                                                    

                                            frame:
                                                background None
                                                ysize 50
                                                $sn = persistent.savefile[i][j].name + savename
                                                if persistent.savefile[i][j].exception:
                                                    $sn = "{color=#ff0000}【已损坏】{/color}"+sn
                                                elif BookSevDownEffect_2.has(persistent.savefile[i][j].p):
                                                    $sn = "{color=#8433cc}【被诅咒】{/color}"+sn
                                                textbutton sn text_style 'white':
                                                    action SetLocalVariable("savei", i), SetLocalVariable("savej", j)
                                                    #elif not slot and not persistent.savefile[0]:
                                                    #    action Show(screen="info_use", i=_('至少先起一个名字。'), width=250)
                                                    #else:
                                                        #action Function(Saver.record_poz, mode)
                                                    if persistent.savefile[i][j] == persistent.savefile[savei][savej]:
                                                        background Frame("gui/style/grey_hover_background.png", tile=gui.frame_tile)
                                                        at ui_save_choose_color
                                                    else:
                                                        background Frame("gui/style/grey_[prefix_]background.png", tile=gui.frame_tile)
                                                    xfill True
                                                    ysize 50
                                                    activate_sound audio.card1
                                    python:
                                        expr_dict = {
                                            'wor': "平庸的社畜 ", 
                                            'wri': "全职小说家 ", 
                                            'cos': "平庸的社畜 ",
                                        }
                                    text expr_dict[persistent.savefile[i][j].p.experience]+persistent.savefile[i][0].p.name style "white":
                                        xfill True
                                        yoffset 5


                    
                    if persistent.savefile:
                        $choicesave = persistent.savefile[savei][savej]
                        python:
                            i_1 = choicesave.p.meds()
                            i_2 = str(int(choicesave.p.achievedGoal*100/choicesave.p.goal)) + '%'
                            if GameDifficulty1.has(choicesave.p):
                                diff = '{color=#ff9900}旅途{/color}'
                            elif GameDifficulty2.has(choicesave.p):
                                diff = '{color=#7FFF00}简单{/color}'
                            elif GameDifficulty3.has(choicesave.p):
                                diff = '{color=#87CEEB}一般{/color}'
                            elif GameDifficulty4.has(choicesave.p):
                                diff = '{color=#FF0000}硬核{/color}'
                            elif GameDifficulty5.has(choicesave.p):
                                diff = '{color=#c000da}地狱{/color}'
                            else:
                                diff = '？？？'

                            sev = choicesave.p.sev()
                            wor = choicesave.p.wor()
                            phy = choicesave.p.phy()
                            wri = choicesave.p.wri()
                            if choicesave.p.cured >= 21:
                                i1 = _('游戏难度：[diff]\n精神状态: [choicesave.p.mental]\n剩余药物: [i_1]\n所持金钱: [choicesave.p.money]\n严重程度: [sev]')
                            elif choicesave.p.experience == 'wri':
                                i1 = _('游戏难度：[diff]\n精神状态: [choicesave.p.mental]\n剩余药物: [i_1]\n所持金钱: [choicesave.p.money]\n平台人气: [choicesave.p.popularity]\n严重程度: [sev]\n工作能力: [wor]\n身体素质: [phy]\n写作技巧: [wri]')
                            else:
                                i1 = _('游戏难度：[diff]\n精神状态: [choicesave.p.mental]\n剩余药物: [i_1]\n所持金钱: [choicesave.p.money]\n工作进度: [i_2]\n严重程度: [sev]\n工作能力: [wor]\n身体素质: [phy]\n写作技巧: [wri]')
                            

                            if choicesave.p.cured >= 21:
                                
                                i2 = "{color=#9500ff}主线进度：[g]%{/color}\n"
                            else:
                                i2 = "{color=#9500ff}主线进度：" + str(int(choicesave.p.sol_p*100/5)) + '%{/color}\n'

                            if choicesave.p.cured == -1:
                                if 0 < choicesave.p.aco_p <= 14 and not choicesave.p.route or choicesave.p.route == 'a':
                                    if choicesave.p.route == 'a':
                                        i2 += "{color=#ff51cb}与Acolas进度：" + str(int(choicesave.p.aco_p*100/14)) + '%{/color}\n'
                                    else:
                                        i2 += "与Acolas进度：" + str(int(choicesave.p.aco_p*100/14)) + '%\n'
                                if 0 < choicesave.p.hal_p <= 15 and not choicesave.p.route or choicesave.p.route == 'h':
                                    if choicesave.p.route == 'h':
                                        i2 += "{color=#ff51cb}与Halluke进度：" + str(int(choicesave.p.hal_p*100/15)) + '%{/color}\n'
                                    else:
                                        i2 += "与Halluke进度：" + str(int(choicesave.p.hal_p*100/15)) + '%\n'

                            playtime_h = int(choicesave.p.playtime//60//60)
                            playtime_m = int((choicesave.p.playtime - playtime_h *60*60)//60)

                            
                            i2 += _('读取次数：[choicesave.p.restart]\n存档版本：[choicesave.p.version]\n游戏时间：[playtime_h]小时[playtime_m]分\n上次存档：[choicesave.p.savetime]\n建档时间：[choicesave.p.timestamp]')
                        
                        
                        default naming = False
                        default g = glitchtext(rd(1, 5))
                        $canload = True


                        frame:  #mainframe
                            background None
                            xsize 700
                            xoffset 10
                            frame:  #nameblock
                                ysize 80
                                background None
                                xoffset 10
                                hbox:
                                    spacing 5
                                    if choicesave.exception:
                                        $canload = False
                                        text "{color=#ff0000}【已损坏】{/color}"+choicesave.name style "white" size 40
                                        
                                    elif BookSevDownEffect_2.has(choicesave.p):
                                        $canload = False
                                        text "{color=#8433cc}【被诅咒】{/color}"+choicesave.name style "white" size 40

                                    elif not naming:
                                        text choicesave.name style "white" size 40
                                        imagebutton auto "gui/save/rename_%s.png":
                                            action SetVariable("newname", choicesave.name), SetLocalVariable("naming", True)
                                            yoffset 10
                                            xoffset 5
                                    else:
                                        input:
                                            length 20
                                            exclude "\"\'[]{}%$@?!#^&*\(\)"
                                            value VariableInputValue("newname")
                                            style "white"
                                            size 40
                                        imagebutton idle "gui/save/nameok.png":
                                            if newname:
                                                action Function(choicesave.rename, newname), SetLocalVariable("naming", False)
                                            else:
                                                action NullAction()
                                                activate_sound audio.error
                                            yoffset 10
                                            xoffset 5

                            
                            null height 30

                            frame: #save pic
                                background None
                                xfill True
                                xalign 1.0
                                xoffset 30
                                ypos 0.1
                                if choicesave.p.cured >= 21 or BookSevDownEffect_2.has(choicesave.p):
                                    add "save_ce" xcenter 0.42
                                elif choicesave.p.experience == 'wri':
                                    add "gui/save/rest.jpg" xcenter 0.42
                                elif choicesave.p.week <= 0:
                                    add "gui/save/street.jpg" xcenter 0.42
                                elif choicesave.p.today in (6, 7):
                                    add "gui/save/rest.jpg" xcenter 0.42
                                else:
                                    add "gui/save/work.jpg" xcenter 0.42

                            null height 20

                            frame:
                                background None
                                yanchor 1.0
                                ypos 0.88
                                xsize 400
                                xpos -0.02
                                text i1 style "white" text_align 0.0
                            frame:
                                xanchor 1.0
                                xpos 1.25
                                background None
                                xsize 600
                                yanchor 1.0
                                ypos 0.88
                                text i2 style "white" text_align 1.0

                            frame:
                                xsize 700
                                ysize 90
                                yalign 1.0
                                background None
                                imagebutton auto "gui/save/delete_%s.png":
                                    action Function(choicesave.delete), SetLocalVariable("savej", max(savej-1, 0))
                                    activate_sound audio.card2
                                    xalign 0.0

                                imagebutton auto "gui/save/download_%s.png":
                                    action Function(Saver.export, choicesave.p)
                                    activate_sound audio.click1
                                    xalign 0.45

                                imagebutton auto "gui/save/load_%s.png":
                                    if canload:
                                        action Function(Saver.load, choicesave.p)
                                    else:
                                        action NullAction()
                                        activate_sound audio.error
                                    xalign 0.9

                            if choicesave.p.cured >= 21:
                                timer 0.1 repeat True action SetLocalVariable("g", glitchtext(rd(1, 5)))
                        
    imagebutton auto "gui/add_%s.png":
        xalign 0.9
        yalign 0.05
        action Function(Saver.inport)
        activate_sound audio.getmedicine

    imagebutton auto "gui/exit_%s.png":
        xalign 0.95
        yalign 0.05
        if main_menu:
            action Return()
        else:
            action ShowMenu("screen_gamemenu", player)

    key 'K_ESCAPE' action Hide("info"),Return()
    key 'K_F1' action Hide("info"),Return()


    use menu_labelname('读取')
    