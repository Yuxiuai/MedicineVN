transform screen_phone_calc_results_normal:
    zoom 0.7
    matrixcolor BrightnessMatrix(-0.2)

transform screen_phone_calc_results_active:
    matrixcolor BrightnessMatrix(-0.2)
    zoom 0.7
    parallel:
        easein 0.5 zoom 1.0
    parallel:
        easein 0.5 matrixcolor BrightnessMatrix(0)
    parallel:
        easein 0.5 yoffset 80
    


screen screen_phone_calc(player):
    default inputs = ''
    default results = ''

    python:
        def calculate(expression):
            if expression == '':
                return ''
            elif expression.endswith(('/', '*', '-', '+')):
                expression = expression[:-1]  # 去除末尾的运算符
            expression = expression.replace("%", "*0.01")
            expression = expression.replace("/", "*1.0/")
            try:
                resu = eval(expression)
            except:
                return '?'

            return eval(expression)




    predict False
    style_prefix "gameUI"
    zorder 600
    
    
    frame:
        
        if phone_page == 6:
            at app_inner_show(-220, 50)
        else:
            at app_inner_hide(-220, 50)

        
        background None
        xcenter 0.5
        ycenter 0.5
        yoffset -10
        
        use barrier('', 0)

        add "gui/phone/wallpaper/calc.webp":
            xcenter 0.5

        

        frame:
            
            background None
            xalign 0.5
            yalign 0.55
            ysize 1300
            xsize 582
            

            frame:
                background None
                xalign 1.0
                yanchor 1.0
                ypos 300
                xoffset -10
                vbox:
                    if results:
                        text results:
                            xalign 1.0
                            style 'phone'
                            size 80
                            at screen_phone_calc_results_active
                    else:
                        text str(calculate(inputs)):
                            xalign 1.0
                            style 'phone'
                            size 80
                            at screen_phone_calc_results_normal
                    text inputs:
                        xalign 1.0
                        style 'phone'
                        size 80




            frame:
                ypos 306
                xpos 3
                background None
                vbox:
                    hbox:
                        spacing 2
                        imagebutton idle "gui/phone/calc/00.png":
                            action SetLocalVariable("inputs", ''), SetLocalVariable("results", '')
                            at app_transform

                        imagebutton idle "gui/phone/calc/01.png":
                            if len(inputs) < 11:
                                action SetLocalVariable("inputs", inputs+'%'), SetLocalVariable("results", '')
                            at app_transform

                        imagebutton idle "gui/phone/calc/02.png":
                            action SetLocalVariable("inputs", inputs[:len(inputs)-1]), SetLocalVariable("results", '')
                            at app_transform

                        imagebutton idle "gui/phone/calc/03.png":
                            if len(inputs) < 11:
                                action SetLocalVariable("inputs", inputs+'/'), SetLocalVariable("results", '')
                            at app_transform


                                

                    hbox:
                        spacing 2
                        imagebutton idle "gui/phone/calc/10.png":
                            if len(inputs) < 11:
                                action SetLocalVariable("inputs", inputs+'7'), SetLocalVariable("results", '')
                            at app_transform

                        imagebutton idle "gui/phone/calc/11.png":
                            if len(inputs) < 11:
                                action SetLocalVariable("inputs", inputs+'8'), SetLocalVariable("results", '')
                            at app_transform

                        imagebutton idle "gui/phone/calc/12.png":
                            if len(inputs) < 11:
                                action SetLocalVariable("inputs", inputs+'9'), SetLocalVariable("results", '')
                            at app_transform

                        imagebutton idle "gui/phone/calc/13.png":
                            if len(inputs) < 11:
                                action SetLocalVariable("inputs", inputs+'*'), SetLocalVariable("results", '')
                            at app_transform
                                

                    hbox:
                        spacing 2
                        imagebutton idle "gui/phone/calc/20.png":
                            if len(inputs) < 11:
                                action SetLocalVariable("inputs", inputs+'4'), SetLocalVariable("results", '')
                            at app_transform

                        imagebutton idle "gui/phone/calc/21.png":
                            if len(inputs) < 11:
                                action SetLocalVariable("inputs", inputs+'5'), SetLocalVariable("results", '')
                            at app_transform

                        imagebutton idle "gui/phone/calc/22.png":
                            if len(inputs) < 11:
                                action SetLocalVariable("inputs", inputs+'6'), SetLocalVariable("results", '')
                            at app_transform

                        imagebutton idle "gui/phone/calc/23.png":
                            if len(inputs) < 11:
                                action SetLocalVariable("inputs", inputs+'-'), SetLocalVariable("results", '')
                            at app_transform
                                

                    hbox:
                        spacing 2
                        imagebutton idle "gui/phone/calc/30.png":
                            if len(inputs) < 11:
                                action SetLocalVariable("inputs", inputs+'1'), SetLocalVariable("results", '')
                            at app_transform

                        imagebutton idle "gui/phone/calc/31.png":
                            if len(inputs) < 11:
                                action SetLocalVariable("inputs", inputs+'2'), SetLocalVariable("results", '')
                            at app_transform

                        imagebutton idle "gui/phone/calc/32.png":
                            if len(inputs) < 11:
                                action SetLocalVariable("inputs", inputs+'3'), SetLocalVariable("results", '')
                            at app_transform

                        imagebutton idle "gui/phone/calc/33.png":
                            if len(inputs) < 11:
                                action SetLocalVariable("inputs", inputs+'+'), SetLocalVariable("results", '')
                            at app_transform

                    hbox:
                        spacing 2
                        imagebutton idle "gui/phone/calc/40.png":
                            if len(inputs) < 10:
                                action SetLocalVariable("inputs", inputs+'00'), SetLocalVariable("results", '')
                            at app_transform

                        imagebutton idle "gui/phone/calc/41.png":
                            if len(inputs) < 11:
                                action SetLocalVariable("inputs", inputs+'0'), SetLocalVariable("results", '')
                            at app_transform

                        imagebutton idle "gui/phone/calc/42.png":
                            if len(inputs) < 11:
                                action SetLocalVariable("inputs", inputs+'.'), SetLocalVariable("results", '')
                            at app_transform

                        imagebutton idle "gui/phone/calc/43.png":
                            action SetLocalVariable("inputs", ''), SetLocalVariable("results", str(calculate(inputs)))
                            at app_transform



            frame:
                background None
                xpos 0.03
                ypos 0.06
                imagebutton auto "gui/phone/back_%s.png":
                    action SetVariable("phone_page", 0), Hide("info")
                    hover_sound audio.cursor
            

                

    key 'K_ESCAPE' action SetVariable("phone_page", 0), Hide("info")