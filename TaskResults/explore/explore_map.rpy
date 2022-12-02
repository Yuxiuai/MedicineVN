screen screen_explore_map(player):
    #tag gamegui
    zorder 300
    frame:
        at map_appear
        background "imagemap/background.png"

        $info1 = "{size=+8}Ascalon书店{/size}\n到此处购买书籍，书籍可以在阅读类日程中的“阅读书籍”，或工作类日程的“偷懒”中使用。"
        $info11 = "\n\n{size=-5}可能探索到的地点或功能：\n    购买书籍{/size}"
        $ad1 = '什么莫兰书店，不认识！'
        imagebutton auto "imagemap/bookshop_%s.png":
            focus_mask True
            action [Hide("info"), Show(screen="info_confirm",text='去这里',act=[Hide("screen_explore_map"),Hide("info_confirm"),Return(),Jump("explore_bookshop")], pp=renpy.get_mouse_pos(),i=info1+info11, a=ad1)]
            hover_sound audio.cursor
            hovered Show("info",i=info1+info11, a=ad1)
            unhovered Hide("info")

        $info2 = "{size=+8}A市大学{/size}\n到此处听公开课或者发现一些有趣的东西，均衡提升能力。"
        $ad2 = 'Halluke在做什么呢……'
        $info22 = "\n\n{size=-5}可能探索到的地点或功能：\n    提升基础能力\n    兼职赚钱{/size}"
        imagebutton auto "imagemap/college_%s.png":
            focus_mask True
            action [Hide("info"), Show(screen="info_confirm",text='去这里',act=[Hide("screen_explore_map"),Hide("info_confirm"),Return(),Jump("explore_college")], pp=renpy.get_mouse_pos(),i=info2+info22, a=ad2)]
            hover_sound audio.cursor
            hovered Show("info",i=info2+info22, a=ad2)
            unhovered Hide("info")
        
        $info3 = "{size=+8}回家{/size}\n放弃外出探索，跳过这一回合。"
        $ad3 = '我的公寓，我很开心在这个城市能有属于我的一足之地。'
        $info33 = "\n\n{size=-5}可能探索到的地点或功能：\n    放弃探索{/size}"
        imagebutton auto "imagemap/home_%s.png":
            focus_mask True
            action [Hide("info"), Show(screen="info_confirm",text='去这里',act=[Hide("screen_explore_map"),Hide("info_confirm"),Return(),Jump("GoOutside_result")], pp=renpy.get_mouse_pos(),i=info3+info33, a=ad3)]
            hover_sound audio.cursor
            hovered Show("info",i=info3+info33, a=ad3)
            unhovered Hide("info")

        $info4 = "{size=+8}医院{/size}\n购买药物，或者治疗疾病。"
        $ad4 = '除了周五我一般都没有去医院的需求，除非是生病了……'
        $info44 = "\n\n{size=-5}可能探索到的地点或功能：\n    购买药物\n    治疗生病\n    治疗受伤"
        if p.sol_p == 0 and p.week >=4 and p.today == 5:
            $ info44 += red('\n    触发与Pathos的新剧情')
        elif p.sol_p == 2 and p.week >=8 and p.today == 5:
            $ info44 += red('\n    触发与Pathos的新剧情')
        if player.aco_p == 7:
            $ info44 += red('\n    触发与Acolas的新剧情')
        $ info44 += '{/size}'
        imagebutton auto "imagemap/hospital_%s.png":
            focus_mask True
            action [Hide("info"), Show(screen="info_confirm",text='去这里',act=[Hide("screen_explore_map"),Hide("info_confirm"),Return(),Jump("explore_hospital")], pp=renpy.get_mouse_pos(),i=info4+info44, a=ad4)]
            hover_sound audio.cursor
            hovered Show("info",i=info4+info44, a=ad4)
            unhovered Hide("info")

        $info5 = "{size=+8}Astaroth公园{/size}\n运动对身体有好处，对你的头疼也是，偶尔也能发现一些有趣的事情。"
        $ad5 = '听说这个公园有一股神秘力量，即便是再谨慎的人，也会在这个公园里丢钱包。'
        $info55 = "\n\n{size=-5}可能探索到的地点或功能：\n    提升身体素质\n    捡钱\n    丢钱\n    捡到物品{/size}"
        imagebutton auto "imagemap/park_%s.png":
            focus_mask True
            action [Hide("info"), Show(screen="info_confirm",text='去这里',act=[Hide("screen_explore_map"),Hide("info_confirm"),Return(),Jump("explore_park")], pp=renpy.get_mouse_pos(),i=info5+info55, a=ad5)]
            hover_sound audio.cursor
            hovered Show("info",i=info5+info55, a=ad5)
            unhovered Hide("info")

        $info6 = "{size=+8}商店街{/size}\n随机选一家店进去玩玩！花钱也是一种放松的手段。"
        $ad6 = '过度消费也是一种自残行为，但我留着那么多钱有什么用呢？'
        $info66 = "\n\n{size=-5}可能探索到的地点或功能：\n    夹娃娃机\n    杂货店\n    小吃街\n    礼品店\n    咖啡厅\n    花店{/size}"
        imagebutton auto "imagemap/ShoppingStreet_%s.png":
            focus_mask True
            action [Hide("info"), Show(screen="info_confirm",text='去这里',act=[Hide("screen_explore_map"),Hide("info_confirm"),Return(),Jump("explore_shop")], pp=renpy.get_mouse_pos(),i=info6+info66, a=ad6)]
            hover_sound audio.cursor
            hovered Show("info",i=info6+info66, a=ad6)
            unhovered Hide("info")

        $info7 = "{size=+8}文体中心{/size}\n这里的场馆大多需要购买门票才能进入，但是能收获更多。"
        $ad7 = '我其实还挺喜欢来这里转转的，就算花了钱也很值得。'
        $info77 = "\n\n{size=-5}可能探索到的地点或功能：\n    电影院\n    博物馆\n    游泳馆{/size}"
        imagebutton auto "imagemap/StylisticCenter_%s.png":
            focus_mask True
            action [Hide("info"), Show(screen="info_confirm",text='去这里',act=[Hide("screen_explore_map"),Hide("info_confirm"),Return(),Jump("explore_center")], pp=renpy.get_mouse_pos(),i=info7+info77, a=ad7)]
            hover_sound audio.cursor
            hovered Show("info",i=info7+info77, a=ad7)
            unhovered Hide("info")



    frame:
        at map_appear
        style "translucent_frame"
        xfill True
        ysize 75
        textbutton '{size=+5}A市B区平面图{/size}' text_style "white":
            action NullAction()
            ycenter 0.5
    
    hbox:
        at map_appear
        xpos 0.9
        ypos 0.85
        imagebutton auto "gui/menu/home_%s.png":
            at map_appear
            action [Hide("screen_explore_map"),Hide("info"),Return(),Jump("GoOutside_result")]
            unhovered Hide("info")
            hovered Show("info",i="放弃外出探索，跳过这一回合。")
            activate_sound audio.cursor
