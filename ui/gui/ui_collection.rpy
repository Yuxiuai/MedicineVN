init python:
    def get_ending_items():
        ending_items = [
            [Sticker59, Achievement400.has(), '普通结局'],
            [OldPic, Achievement401.has(), '真实结局'],
            [ExaminationReport, Achievement402.has(), '治愈结局'],
            [TransparentBottle, Achievement403.has(), '虚伪结局'],
            [TrainTicket, Achievement404.has(), '孤独结局'],
            [TheBook, Achievement405.has(), '作家结局'],
        ]
        return ending_items

transform selected_ending_item_transform():
    matrixcolor BrightnessMatrix(0.15)

transform ending_item_transform():
    xoffset -1000
    easein 1 xoffset 0

screen screen_collection_select(player):
    tag menu
    default collection_info = "你在收拾抽屉的时候翻出了一件特别的道具，它将会是……"
    add "images/gui/opening/bg2.webp"
    add "gui/overlay/confirm.png"

    default ending_items = get_ending_items()
    default locked = False
    default locked_info = '完成？？？结局后解锁。'

    frame at ending_item_transform:
        background None
        ysize 700
        xsize 650
        xpos 0.06
        ycenter 0.5
        yoffset 45
        vbox:
            spacing 30
            hbox:
                spacing 30
                for item in range(0, 3):
                    if ending_items[item][1]:
                        $icon = ending_items[item][0].icon()
                    else:
                        $icon = "images/gui/effects/unknown.png"
                    imagebutton idle icon:

                        if persistent.lastend == ending_items[item][0]:
                            action SetVariable("persistent.lastend", None), SetLocalVariable("locked", False)
                            at selected_ending_item_transform(), tzoom(2)
                        elif ending_items[item][1]:
                            action SetVariable("persistent.lastend", ending_items[item][0]), SetLocalVariable("locked", False)
                            at app_transform(), tzoom(2)
                        else:
                            action SetVariable("persistent.lastend", ending_items[item][0]), SetLocalVariable("locked", True), SetLocalVariable("locked_info", '完成%s结局后解锁。'%ending_items[item][2])
                            at app_transform(), tzoom(2)

                        activate_sound audio.card1
            hbox:
                spacing 30  
                for item in range(3, 6):
                    if ending_items[item][1]:
                        $icon = ending_items[item][0].icon()
                    else:
                        $icon = "images/gui/effects/unknown.png"
                    imagebutton idle icon:
                        
                        if persistent.lastend == ending_items[item][0]:
                            action SetVariable("persistent.lastend", None), SetLocalVariable("locked", False)
                            at selected_ending_item_transform(), tzoom(2)
                        elif ending_items[item][1]:
                            action SetVariable("persistent.lastend", ending_items[item][0]), SetLocalVariable("locked", False)
                            at app_transform(), tzoom(2)
                        else:
                            action SetVariable("persistent.lastend", ending_items[item][0]), SetLocalVariable("locked", True), SetLocalVariable("locked_info", '完成%s结局后解锁。'%ending_items[item][2])
                            at app_transform(), tzoom(2)

                        activate_sound audio.card1

                    
    frame at screen_name_select_info:
        xsize 1100
        ysize 700
        xpos 1920
        ycenter 0.5
        yoffset 45
        background Frame("gui/style/grey_idle_background.png", tile=gui.frame_tile)
        vbox:
            textbutton collection_info:
                text_style "white" 
                text_size 25

            python:
                if not persistent.lastend:
                    t_info = "不携带任何道具"
                    i_info = ""
                    a_info = ""
                elif locked:
                    t_info = "？？？"
                    i_info = locked_info
                    a_info = "？？？？？？？？？？？？？？？？？？？？？？？"
                else:
                    t_info = persistent.lastend.name
                    i_info = persistent.lastend.info
                    a_info = persistent.lastend.ad

            null height 20

            textbutton t_info:
                text_style "white" 
                text_size 50

            null height 20

            textbutton '{size=-2}' + i_info +'{/size}':
                text_style "white" 
                text_size 25
                
            null height 5

            textbutton '{i}' + a_info +'{/i}':
                text_style "white" 
                text_color "#d6d6d6"
                text_size 19



    
        if not locked:
            imagebutton auto "images/gui/opening/ok_%s.png":
                action ShowMenu("screen_name_select", player)
                xalign 0.9
                yalign 0.95
                activate_sound audio.click1

            
    imagebutton auto "gui/exit_%s.png":
        xalign 0.95
        yalign 0.05
        action Return()
    
    key 'K_ESCAPE' action Hide("info"),Return()



    frame at screen_init_select_label:
        background None
        xpos 0.05
        xsize 100
        ysize 200
        yoffset 20
        frame:
            yalign 0.5
            background None
            xsize 500
            text "收藏品" style "white" size 60