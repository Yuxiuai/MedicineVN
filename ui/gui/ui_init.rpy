transform screen_init_select_default:
    matrixcolor BrightnessMatrix(-0.15)
    parallel:
        matrixcolor BrightnessMatrix(-0.15)
    parallel:
        easein 0.5 yoffset 0
    parallel:
        easein 0.5 xoffset 0
    parallel:
        easein 0.5 alpha 1.0

    on hover:
        linear .25 matrixcolor BrightnessMatrix(0.0)
    on idle:
        linear .5 matrixcolor BrightnessMatrix(-0.15)

transform screen_init_select_move_to_left(distance):
    matrixcolor BrightnessMatrix(-0.15)
    parallel:
        easein .25 xoffset -distance
    parallel:
        linear .25 matrixcolor BrightnessMatrix(0.0)

transform screen_init_select_hide(distance):
    parallel:
        easein .25 yoffset 500
    parallel:
        easein .25 alpha 0

transform screen_init_select_label():
    xoffset -200
    easein .25 xoffset 0

transform screen_init_select_info():
    parallel:
        easein .5 xoffset -1450
    parallel:
        easein .25 alpha 1



screen screen_init_select():
    tag menu
    default selected = 0
    default unusedpoints = 10
    default wor = 0
    default phy = 0
    default wri = 0

    add persistent.main_menu_theme.bg

    add "gui/overlay/confirm.png"

    python:
        def getplayer(expr, args):
            p = Player()
            p.give_experience(expr, args)
            return p

        

    python:
        init_dict = ["选择主角出身", "平庸的社畜", "全职小说家", "自定义"]
        expr_dict = ["","wor", "wri", "cos"]
        info_dict = [
            "",
            "即便痛苦在你小时便就折磨着你，但你大学时仍然勤恳地学习着各种知识。\n即便你明白，自己无论怎么努力，也只能成为这个世界的一颗螺丝钉。\n\n{color=#ffff00}基础属性：{/color}\n无变化\n\n{color=#ffff00}特殊效果：{/color}\n你通过日程获得工作能力时，额外获得1点。",
            "你小时候的梦想便是出版一本自己的小说。\n除此之外，你因为无法忍受在持久性的头疼的情况下工作，辞掉了这份在他人眼中十分优越的工作。\n这样一来，你的收入来源基本上只剩下写网上的文章委托。\n你真的能够仅凭写作养活自己，直到自己的书出版的那一天吗？\n\n{color=#ffff00}基础属性：{/color}\n写作技巧 +0.3\n严重程度倍率 +30%\n运动类日程专注度 -20%\n\n{color=#ffff00}特殊效果：{/color}\n独特的序章剧情。\n可能会睡过头。\n较少的初始资金，较多的平台人气。\n获得灵感会恢复精神状态，但已有层数较高时效果会降低。\n无需上班，但每个月的15日需要支付等同于10倍药物价格的房租。\n获得小说原稿，解锁撰写小说日程，推进人物剧情后可以进行该日程，完成该小说后可专属结局。\n平台人气衰减速度降低50%，完成委托获得的报酬提升50%，且能获得平台人气，一段时间内不再流失粉丝，最大平台人气数量增加40000。",
            "自定义基础属性，不会获得特殊效果。",
        ]

    vbox:
        xcenter 0.5
        ycenter 0.5
        textbutton init_dict[selected]:
            text_style "white" 
            text_size 60 
            yoffset -30 
            xoffset 20
            at screen_init_select_label()

        hbox:
            imagebutton:
                idle Composite((360,770),(0, 0), "images/gui/opening/work_idle.webp",(0, 0), "images/gui/opening/work_info.webp")
                hover Composite((360,770),(0, 0), "images/gui/opening/work_hover.webp",(0, 0), "images/gui/opening/work_info.webp")
                if selected == 0:
                    action SetLocalVariable("selected", 1)
                    activate_sound audio.card1
                    at screen_init_select_default
                elif selected == 1:
                    action SetLocalVariable("selected", 0)
                    activate_sound audio.card2
                    at screen_init_select_move_to_left(0)
                else:
                    at screen_init_select_hide
                    
            imagebutton:
                idle Composite((360,770),(0, 0), "images/gui/opening/write_idle.webp",(0, 0), "images/gui/opening/write_info.webp")
                hover Composite((360,770),(0, 0), "images/gui/opening/write_hover.webp",(0, 0), "images/gui/opening/write_info.webp")
                
                if selected == 0:
                    action SetLocalVariable("selected", 2)
                    activate_sound audio.card1
                    at screen_init_select_default
                elif selected == 2:
                    action SetLocalVariable("selected", 0)
                    activate_sound audio.card2
                    at screen_init_select_move_to_left(370)
                else:
                    at screen_init_select_hide

            imagebutton idle "images/gui/opening/null.webp"

            imagebutton idle "images/gui/opening/null.webp"

            imagebutton idle "images/gui/opening/null.webp"

            #imagebutton:
            #    idle Composite((360,770),(0, 0), "images/gui/opening/other_idle.webp",(0, 0), "images/gui/opening/other_info.webp")
            #    hover Composite((360,770),(0, 0), "images/gui/opening/other_hover.webp",(0, 0), "images/gui/opening/other_info.webp")
            #    action NullAction()
            

            

            
            
                    
    if selected not in (0, -1):    
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
                    text_size 22

            imagebutton auto "images/gui/opening/back_%s.png":
                action SetLocalVariable("selected", 0)
                xalign 0.1
                yalign 0.95
                activate_sound audio.card2

            imagebutton auto "images/gui/opening/ok_%s.png":
                action ShowMenu("screen_diff_select", getplayer(expr_dict[selected], [wor, phy, wri]), 0)
                xalign 0.9
                yalign 0.95
                activate_sound audio.click1
    
    if selected == -1:    

        frame at screen_init_select_info:
            xsize 1300
            ysize 700
            xpos 1920
            ycenter 0.5
            yoffset 45
            background Frame("gui/style/grey_idle_background.png", tile=gui.frame_tile)

                
            
            vbox:
                spacing 40
                textbutton info_dict[selected]:
                    text_style "white" 
                    text_size 25

                frame:
                    background None
                    ysize 60
                    xsize 330

                    text '可用点数：%s' % (unusedpoints) style "white":
                        xsize 330
                        yalign 0.5

                frame:
                    background None
                    ysize 60
                    xsize 330

                    

                    frame:
                        background None
                        hbox:
                            spacing 100
                            if wor <= -0.05:
                                imagebutton idle "images/gui/none_w.png":
                                    action NullAction()
                                    xalign 1.0
                            else:
                                imagebutton idle "images/gui/minus_w.png":
                                    action SetLocalVariable("unusedpoints", unusedpoints+1),SetLocalVariable("wor", wor-0.01)
                                    activate_sound audio.cursor
                                    xalign 1.0

                            text '工作能力：%.2f' % (1.0 + wor) style "white":
                                xsize 330
                                yalign 0.5
                                
                            if unusedpoints <= 0:
                                imagebutton idle "images/gui/none_w.png":
                                    action NullAction()
                                    xalign 1.0
                            else:
                                imagebutton idle "images/gui/add_w.png":
                                    action SetLocalVariable("unusedpoints", unusedpoints-1),SetLocalVariable("wor", wor+0.01)
                                    activate_sound audio.cursor
                                    xalign 1.0

                            
                    null height 2

                
                frame:
                    background None
                    ysize 60
                    xsize 330
                    frame:
                        background None
                        hbox:
                            spacing 100

                            if phy <= -0.05:
                                imagebutton idle "images/gui/none_w.png":
                                    action NullAction()
                                    xalign 1.0
                            else:
                                imagebutton idle "images/gui/minus_w.png":
                                    action SetLocalVariable("unusedpoints", unusedpoints+1),SetLocalVariable("phy", phy-0.01)
                                    activate_sound audio.cursor
                                    xalign 1.0

                            text '身体素质：%.2f' % (1.0+phy) style "white":
                                xsize 330
                                yalign 0.5
                            
                            if unusedpoints <= 0:
                                imagebutton idle "images/gui/none_w.png":
                                    action NullAction()
                                    xalign 1.0
                            else:
                                imagebutton idle "images/gui/add_w.png":
                                    action SetLocalVariable("unusedpoints", unusedpoints-1),SetLocalVariable("phy", phy+0.01)
                                    activate_sound audio.cursor
                                    xalign 1.0

                            
                    null height 2

                frame:
                    background None
                    ysize 60
                    xsize 330
                    frame:
                        background None
                        hbox:
                            spacing 100

                            if wri <= -0.05:
                                imagebutton idle "images/gui/none_w.png":
                                    action NullAction()
                                    xalign 1.0
                            else:
                                imagebutton idle "images/gui/minus_w.png":
                                    action SetLocalVariable("unusedpoints", unusedpoints+1),SetLocalVariable("wri", wri-0.01)
                                    activate_sound audio.cursor
                                    xalign 1.0

                            text '写作技巧：%.2f' % (1.0+wri) style "white":
                                xsize 330
                                yalign 0.5
                            
                            if unusedpoints <= 0:
                                imagebutton idle "images/gui/none_w.png":
                                    action NullAction()
                                    xalign 1.0
                            else:
                                imagebutton idle "images/gui/add_w.png":
                                    action SetLocalVariable("unusedpoints", unusedpoints-1),SetLocalVariable("wri", wri+0.01)
                                    activate_sound audio.cursor
                                    xalign 1.0

                    null height 2

                null height 40

            imagebutton auto "images/gui/opening/back_%s.png":
                action SetLocalVariable("selected", 0)
                xalign 0.1
                yalign 0.95
                activate_sound audio.card2

            imagebutton auto "images/gui/opening/ok_%s.png":
                #if selected != 0:
                #    action Function(function_dict[selected], player), Return()
                #else:
                action ShowMenu("screen_diff_select", getplayer(expr_dict[selected], [wor, phy, wri]), 0)
                xalign 0.9
                yalign 0.95
                activate_sound audio.click1
        
    
    imagebutton auto "gui/exit_%s.png":
        xalign 0.95
        yalign 0.05
        action Return()
    
    key 'K_ESCAPE' action Hide("info"),Return()