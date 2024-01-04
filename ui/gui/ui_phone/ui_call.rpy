define screen_phone_call_i = {
    "Pathos": "总喜欢摆着臭脸的主治医师",
    "Acolas": "负责很多项目的技术总监",
    "Halluke": "就读于A市大学的白熊大学生",
    "Depline": "莓博上的大学生画师",
    "Destot": "我的实习生",
    "Arnel": "经常抓你偷懒睡觉的白狼部门主管，如果需要请假就给他打电话",
    "parents": "虽然你们很久都不通一次电话，但如果你手头很紧，也许可以和你的父母借一点钱",
}


screen screen_phone_call(player):


    predict False
    style_prefix "gameUI"
    zorder 600
    
    frame:
        
        if phone_page == 11:
            at app_inner_show(-220, 230)
        else:
            at app_inner_hide(-220, 230)

        
        background None
        xcenter 0.5
        ycenter 0.5
        yoffset -10
        
        use barrier('', 0)

        add "gui/phone/wallpaper/message.webp":
            xcenter 0.5


        frame:
            
            background None
            xalign 0.5
            yalign 0.55
            ysize 1300
            xsize 582
            



            frame:
                ypos 150
                background None
                vbox:
                    if player.sol_p>=0:
                        use screen_phone_call_friendbox(player, 'parents')
                        use screen_phone_call_friendbox(player, 'Pathos')
                    if player.experience!='wri':
                        use screen_phone_call_friendbox(player, 'Arnel')
                    if player.aco_p>2:
                        use screen_phone_call_friendbox(player, 'Acolas')
                    if player.hal_p>6 and player.hal_p != 51:
                        use screen_phone_call_friendbox(player, 'Halluke')
                    #if player.dep_p>10:
                    #    use screen_phone_call_friendbox(player, 'Pathos')
                    if player.des_p>=2:    
                        use screen_phone_call_friendbox(player, 'Destot')
                       

            frame:
                background None
                xpos 0.03
                ypos 0.06
                imagebutton auto "gui/phone/back_%s.png":
                    action SetVariable("phone_page", 0), Hide("info")
                    hover_sound audio.cursor
                 
        
        text "联系人" xpos 0.92 xanchor 1.0 ypos 0.085 size 40 style "foodname"

    key 'K_ESCAPE' action SetVariable("phone_page", 0), Hide("info")


screen screen_phone_call_friendbox(player, name):
    $showname = name
    if name == 'parents':
        $showname = '父母'
    frame:
        ysize 80
        xsize 550
        background None

        textbutton "[showname]":
            action Hide("screen_phone"), SetVariable("phone_page", 0), Hide("info") ,Jump("call_" + name)
            hovered Show(screen="info", i='给'+showname+'打电话。',a=screen_phone_call_i[name])
            unhovered Hide("info")  
            xfill True
            yfill True
            activate_sound audio.cursor
            background Frame("#f8f8f8")
            yalign 0.5
            text_style "foodname"
            text_size 40
            text_xoffset 5
            at screen_phone_message_friendbox_transform

        text ">" style "foodname" yalign 0.5 xalign 0.95 size 40
