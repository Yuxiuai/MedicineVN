screen screen_map(player, exploring=False):
    #tag gamegui
    zorder 900
    frame:
        at map_appear
        background "imagemap/background.webp"

        button:
            action NullAction()
            xfill True
            yfill True

        $info1 = _("{size=+8}Ascalon书店{/size}\n购买书籍。\n购买的书籍可以储存于道具栏中，通过“阅读书籍”等日程使用。")
        $info11 = _("\n\n{size=-5}可能探索到的地点或功能：\n    购买书籍{/size}")
        $ad1 = _('沙里淘金，壳里拾粒，水中萃血，皆需工夫。如果我买下足够多的书，总会发现些有趣的事情……')
        imagebutton auto "imagemap/bookshop_%s.webp":
            focus_mask True
            if not exploring:
                action [Hide("info"), Show(screen="info_use", pp=renpy.get_mouse_pos(),i=info1+info11, a=ad1)]
            else:
                if persistent.actionquickly:
                    action Hide("info"),Hide("screen_map"),Hide("info_confirm"),Return(),Jump("explore_bookshop")
                else:
                    action [Hide("info"), Show(screen="info_confirm",text='去这里',act=[Hide("screen_map"),Hide("info_confirm"),Return(),Jump("explore_bookshop")], pp=renpy.get_mouse_pos(),i=info1+info11, a=ad1)]
            hover_sound audio.cursor
            hovered Show("info",i=info1+info11, a=ad1)
            unhovered Hide("info")

        $info2 = _("{size=+8}A市大学{/size}\n到此处听公开课或者发现一些有趣的东西，均衡提升能力。")
        $ad2 = _('那小家伙在做什么呢……')
        $info22 = _("\n\n{size=-5}可能探索到的地点或功能：\n    提升基础能力\n    兼职赚钱{/size}")
        imagebutton auto "imagemap/college_%s.webp":
            focus_mask True
            if not exploring:
                action [Hide("info"), Show(screen="info_use", pp=renpy.get_mouse_pos(),i=info2+info22, a=ad2)]
            else:
                if persistent.actionquickly:
                    action Hide("info"),Hide("screen_map"),Hide("info_confirm"),Return(),Jump("explore_college")
                else:
                    action [Hide("info"), Show(screen="info_confirm",text='去这里',act=[Hide("screen_map"),Hide("info_confirm"),Return(),Jump("explore_college")], pp=renpy.get_mouse_pos(),i=info2+info22, a=ad2)]
            hover_sound audio.cursor
            hovered Show("info",i=info2+info22, a=ad2)
            unhovered Hide("info")
        
        $info3 = _("{size=+8}回家{/size}\n放弃外出探索，跳过这一回合。")
        $ad3 = _('我的公寓，我很开心在这个城市能有属于我的一足之地。')
        $info33 = _("\n\n{size=-5}可能探索到的地点或功能：\n    放弃探索{/size}")
        imagebutton auto "imagemap/home_%s.webp":
            focus_mask True
            if not exploring:
                action [Hide("info"), Show(screen="info_use", pp=renpy.get_mouse_pos(),i=info3+info33, a=ad3)]
            else:
                if persistent.actionquickly:
                    action Hide("info"),Hide("screen_map"),Hide("info_confirm"),Function(Tired.clearByType,player),Return(),Jump("GoOutside_result")
                else:
                    action [Hide("info"), Show(screen="info_confirm",text='去这里',act=[Hide("screen_map"),Hide("info_confirm"),Function(Tired.clearByType,player),Return(),Jump("GoOutside_result")], pp=renpy.get_mouse_pos(),i=info3+info33, a=ad3)]
            hover_sound audio.cursor
            hovered Show("info",i=info3+info33, a=ad3)
            unhovered Hide("info")

        $info4 = _("{size=+8}医院{/size}\n购买药物，或者治疗疾病。")
        $ad4 = _('除了周五我一般都没有去医院的需求，除非是生病了……')
        $info44 = _("\n\n{size=-5}可能探索到的地点或功能：\n    购买药物\n    治疗生病\n    治疗受伤{/size}")
        if p.sol_p == 0 and p.week >=4 and p.today == 5:
            $ info44 += red('{size=-5}\n    触发与Pathos的新剧情{/size}')
        elif p.sol_p == 2 and p.week >=8 and p.today == 5:
            $ info44 += red('{size=-5}\n    触发与Pathos的新剧情{/size}')
        elif p.sol_p == 4 and p.week >=12 and p.today == 5:
            $ info44 += red('{size=-5}\n    触发与Pathos的新剧情{/size}')
        if player.aco_p == 7 and p.today in (6, 7):
            $ info44 += red('{size=-5}\n    触发与Acolas的新剧情{/size}')
        imagebutton auto "imagemap/hospital_%s.webp":
            focus_mask True
            if not exploring:
                action [Hide("info"), Show(screen="info_use", pp=renpy.get_mouse_pos(),i=info4+info44, a=ad4)]
            else:
                if persistent.actionquickly:
                    action Hide("info"),Hide("screen_map"),Hide("info_confirm"),Return(),Jump("explore_hospital")
                else:
                    action [Hide("info"), Show(screen="info_confirm",text='去这里',act=[Hide("screen_map"),Hide("info_confirm"),Return(),Jump("explore_hospital")], pp=renpy.get_mouse_pos(),i=info4+info44, a=ad4)]
            hover_sound audio.cursor
            hovered Show("info",i=info4+info44, a=ad4)
            unhovered Hide("info")

        $info5 = _("{size=+8}Astaroth公园{/size}\n运动对身体有好处，对你的头疼也是，偶尔也能发现一些有趣的事情。")
        $ad5 = _('听说这个公园有一股神秘力量，即便是再谨慎的人，也会在这个公园里丢钱包。')
        $info55 = _("\n\n{size=-5}可能探索到的地点或功能：\n    提升身体素质\n    捡钱\n    丢钱\n    捡到物品{/size}")
        imagebutton auto "imagemap/park_%s.webp":
            focus_mask True
            if not exploring:
                action [Hide("info"), Show(screen="info_use", pp=renpy.get_mouse_pos(),i=info5+info55, a=ad5)]
            else:
                if persistent.actionquickly:
                    action Hide("info"),Hide("screen_map"),Hide("info_confirm"),Return(),Jump("explore_park")
                else:
                    action [Hide("info"), Show(screen="info_confirm",text='去这里',act=[Hide("screen_map"),Hide("info_confirm"),Return(),Jump("explore_park")], pp=renpy.get_mouse_pos(),i=info5+info55, a=ad5)]
            hover_sound audio.cursor
            hovered Show("info",i=info5+info55, a=ad5)
            unhovered Hide("info")

        $info6 = _("{size=+8}商店街{/size}\n随机选一家店进去玩玩！花钱也是一种放松的手段。")
        $ad6 = _('过度消费也是一种自残行为，但我留着那么多钱有什么用呢？')
        $info66 = _("\n\n{size=-5}点击查看商店街部分地图。{/size}")
        imagebutton auto "imagemap/ShoppingStreet_%s.webp":
            focus_mask True
            action [Hide("info"), Show(screen="screen_shopstreet_map", player=player, exploring=exploring)]
            hover_sound audio.cursor
            hovered Show("info",i=info6+info66, a=ad6)
            unhovered Hide("info")

        $info7 = _("{size=+8}文体中心{/size}\n这里的场馆大多需要购买门票才能进入，但是能收获更多。")
        $ad7 = _('我其实还挺喜欢来这里转转的，就算花了钱也很值得。')
        $info77 = _("\n\n{size=-5}可能探索到的地点或功能：\n    电影院\n    博物馆\n    游泳馆{/size}")
        imagebutton auto "imagemap/StylisticCenter_%s.webp":
            focus_mask True
            if not exploring:
                action [Hide("info"), Show(screen="info_use", pp=renpy.get_mouse_pos(),i=info7+info77, a=ad7)]
            else:
                if persistent.actionquickly:
                    action Hide("info"),Hide("screen_map"),Hide("info_confirm"),Return(),Jump("explore_center")
                else:
                    action [Hide("info"), Show(screen="info_confirm",text='去这里',act=[Hide("screen_map"),Hide("info_confirm"),Return(),Jump("explore_center")], pp=renpy.get_mouse_pos(),i=info7+info77, a=ad7)]
            hover_sound audio.cursor
            hovered Show("info",i=info7+info77, a=ad7)
            unhovered Hide("info")

    frame:
        at map_appear
        style "translucent_frame"
        xfill True
        ysize 75
        textbutton _('{size=+5}A市B区平面图{/size}') text_style "white":
            action NullAction()
            ycenter 0.5
    
    hbox:
        xpos 0.9
        ypos 0.85
        imagebutton auto "gui/menu/home_%s.png":
            at trans_toLeft()
            if not exploring:
                action Hide("screen_map", transition=dissolve),Hide("info")
                hovered Show(screen="info", i=_('关闭地图'), a=_('该继续安排日程了。'))
            else:
                action [Hide("screen_map"),Hide("info"),Function(Tired.clearByType,player),Return(),Jump("GoOutside_result")]
                hovered Show("info",i="放弃外出探索，跳过这一回合。")
            unhovered Hide("info")
            
            activate_sound audio.cursor

    key 'K_ESCAPE' action Hide("screen_map", transition=dissolve),Hide("info")




screen screen_shopstreet_map(player, exploring):
    #tag gamegui
    zorder 900
    frame:
        at map_appear
        background "imagemap/shopstreet/background.webp"

        button:
            action NullAction()
            xfill True
            yfill True

        $info1 = "{size=+8}宾馆{/size}"
        $info11 = "\n{size=-5}短暂休息或过夜{/size}"
        $ad1 = '一想到这里面每天晚上都有很多人在同时做爱，就十分不可思议。'
        imagebutton auto "imagemap/shopstreet/hotel_%s.webp":
            focus_mask True
            if not exploring:
                action [Hide("info"), Show(screen="info_use", pp=renpy.get_mouse_pos(),i=info1+info11, a=ad1)]
            else:
                if persistent.actionquickly:
                    action Hide("info"),Hide("screen_map"),Hide("screen_shopstreet_map"),Hide("info_confirm"),Return(),Jump("explore_hotel")
                else:
                    action [Hide("info"), Show(screen="info_confirm",text='去这里',act=[Hide("screen_map"),Hide("screen_shopstreet_map"),Hide("info_confirm"),Return(),Jump("explore_hotel")], pp=renpy.get_mouse_pos(),i=info1+info11, a=ad1)]
            action NullAction()
            hover_sound audio.cursor
            hovered Show("info",i=info1+info11, a=ad1)
            unhovered Hide("info")
            activate_sound audio.error

        $info2 = "{size=+8}花店{/size}" if 6 in p.visitedStore else '{size=+8}？？？{/size}'
        $ad2 = '你们知道吗，其实花朵是花的性器官！' if 6 in p.visitedStore else '？？？？？？？？？？？？'
        $info22 = "\n{size=-5}购买收藏品{/size}" if 6 in p.visitedStore else '\n{size=-5}还没去过这里，来这里逛一逛吧？{/size}'
        imagebutton auto "imagemap/shopstreet/flowershop_%s.webp":
            focus_mask True
            if not exploring:
                action [Hide("info"), Show(screen="info_use", pp=renpy.get_mouse_pos(),i=info2+info22, a=ad2)]
            else:
                if persistent.actionquickly:
                    action Hide("info"),Hide("screen_map"),Hide("screen_shopstreet_map"),Hide("info_confirm"),Return(),Jump("explore_shop_6")
                else:
                    action [Hide("info"), Show(screen="info_confirm",text='去这里',act=[Hide("screen_map"),Hide("screen_shopstreet_map"),Hide("info_confirm"),Return(),Jump("explore_shop_6")], pp=renpy.get_mouse_pos(),i=info2+info22, a=ad2)]
            hover_sound audio.cursor
            hovered Show("info",i=info2+info22, a=ad2)
            unhovered Hide("info")
        
        $info3 = "{size=+8}游戏厅{/size}" if 1 in p.visitedStore else '{size=+8}？？？{/size}'
        $ad3 = '不是我不喜欢打游戏，只是一激动，一失败，或者只是玩的久一些，头疼就会逼我放下游戏。' if 1 in p.visitedStore else '？？？？？？？？？？？？'
        $info33 = "\n{size=-5}夹娃娃{/size}" if 1 in p.visitedStore else '\n{size=-5}还没去过这里，来这里逛一逛吧？{/size}'
        imagebutton auto "imagemap/shopstreet/gameroom_%s.webp":
            focus_mask True
            if not exploring:
                action [Hide("info"), Show(screen="info_use", pp=renpy.get_mouse_pos(),i=info3+info33, a=ad3)]
            else:
                if persistent.actionquickly:
                    action Hide("info"),Hide("screen_map"),Hide("screen_shopstreet_map"),Hide("info_confirm"),Return(),Jump("explore_shop_1")
                else:
                    action [Hide("info"), Show(screen="info_confirm",text='去这里',act=[Hide("screen_map"),Hide("screen_shopstreet_map"),Hide("info_confirm"),Return(),Jump("explore_shop_1")], pp=renpy.get_mouse_pos(),i=info3+info33, a=ad3)]
            hover_sound audio.cursor
            hovered Show("info",i=info3+info33, a=ad3)
            unhovered Hide("info")

        $info4 = "{size=+8}零食店{/size}" if 2 in p.visitedStore else '{size=+8}？？？{/size}'
        $ad4 = '其实我更关心有没有快乐肥宅水卖。' if 2 in p.visitedStore else '？？？？？？？？？？？？'
        $info44 = "\n{size=-5}购买零食{/size}" if 2 in p.visitedStore else '\n{size=-5}还没去过这里，来这里逛一逛吧？{/size}'
        imagebutton auto "imagemap/shopstreet/snackshop_%s.webp":
            focus_mask True
            if not exploring:
                action [Hide("info"), Show(screen="info_use", pp=renpy.get_mouse_pos(),i=info4+info44, a=ad4)]
            else:
                if persistent.actionquickly:
                    action Hide("info"),Hide("screen_map"),Hide("screen_shopstreet_map"),Hide("info_confirm"),Return(),Jump("explore_shop_2")
                else:
                    action [Hide("info"), Show(screen="info_confirm",text='去这里',act=[Hide("screen_map"),Hide("screen_shopstreet_map"),Hide("info_confirm"),Return(),Jump("explore_shop_2")], pp=renpy.get_mouse_pos(),i=info4+info44, a=ad4)]
            hover_sound audio.cursor
            hovered Show("info",i=info4+info44, a=ad4)
            unhovered Hide("info")

        $info5 = "{size=+8}咖啡馆{/size}" if 5 in p.visitedStore else '{size=+8}？？？{/size}'
        $ad5 = '名为咖啡营地的小店，看上去消费水平十分高。' if 5 in p.visitedStore else '？？？？？？？？？？？？'
        $info55 = "\n{size=-5}购买咖啡{/size}" if 5 in p.visitedStore else '\n{size=-5}还没去过这里，来这里逛一逛吧？{/size}'
        imagebutton auto "imagemap/shopstreet/cafe_%s.webp":
            focus_mask True
            if not exploring:
                action [Hide("info"), Show(screen="info_use", pp=renpy.get_mouse_pos(),i=info5+info55, a=ad5)]
            else:
                if persistent.actionquickly:
                    action Hide("info"),Hide("screen_map"),Hide("screen_shopstreet_map"),Hide("info_confirm"),Return(),Jump("explore_shop_5")
                else:
                    action [Hide("info"), Show(screen="info_confirm",text='去这里',act=[Hide("screen_map"),Hide("screen_shopstreet_map"),Hide("info_confirm"),Return(),Jump("explore_shop_5")], pp=renpy.get_mouse_pos(),i=info5+info55, a=ad5)]
            hover_sound audio.cursor
            hovered Show("info",i=info5+info55, a=ad5)
            unhovered Hide("info")

        $info6 = "{size=+8}礼品店{/size}" if 4 in p.visitedStore else '{size=+8}？？？{/size}'
        $ad6 = '其实我很喜欢一些可爱的小摆件，买来之后像摆摊一样放在我的桌子上。' if 4 in p.visitedStore else '？？？？？？？？？？？？'
        $info66 = "\n{size=-5}购买收藏品{/size}" if 4 in p.visitedStore else '\n{size=-5}还没去过这里，来这里逛一逛吧？{/size}'
        imagebutton auto "imagemap/shopstreet/giftshop_%s.webp":
            focus_mask True
            if not exploring:
                action [Hide("info"), Show(screen="info_use", pp=renpy.get_mouse_pos(),i=info6+info66, a=ad6)]
            else:
                if persistent.actionquickly:
                    action Hide("info"),Hide("screen_map"),Hide("screen_shopstreet_map"),Hide("info_confirm"),Return(),Jump("explore_shop_4")
                else:
                    action [Hide("info"), Show(screen="info_confirm",text='去这里',act=[Hide("screen_map"),Hide("screen_shopstreet_map"),Hide("info_confirm"),Return(),Jump("explore_shop_4")], pp=renpy.get_mouse_pos(),i=info6+info66, a=ad6)]
            hover_sound audio.cursor
            hovered Show("info",i=info6+info66, a=ad6)
            unhovered Hide("info")

        $info7 = "{size=+8}工具店{/size}" if 7 in p.visitedStore else '{size=+8}？？？{/size}'
        $ad7 = '有什么有用的东西吗？' if 7 in p.visitedStore else '？？？？？？？？？？？？'
        $info77 = "\n{size=-5}购买工具{/size}" if 7 in p.visitedStore else '\n{size=-5}还没去过这里，来这里逛一逛吧？{/size}'
        imagebutton auto "imagemap/shopstreet/toolshop_%s.webp":
            focus_mask True
            if not exploring:
                action [Hide("info"), Show(screen="info_use", pp=renpy.get_mouse_pos(),i=info7+info77, a=ad7)]
            else:
                if persistent.actionquickly:
                    action Hide("info"),Hide("screen_map"),Hide("screen_shopstreet_map"),Hide("info_confirm"),Return(),Jump("explore_shop_7")
                else:
                    action [Hide("info"), Show(screen="info_confirm",text='去这里',act=[Hide("screen_map"),Hide("screen_shopstreet_map"),Hide("info_confirm"),Return(),Jump("explore_shop_7")], pp=renpy.get_mouse_pos(),i=info7+info77, a=ad7)]
            hover_sound audio.cursor
            hovered Show("info",i=info7+info77, a=ad7)
            unhovered Hide("info")

        $info8 = "{size=+8}小吃街{/size}" if 3 in p.visitedStore else '{size=+8}？？？{/size}'
        $ad8 = '该庆幸我的胃还没有出问题，不然真是死了算了。' if 3 in p.visitedStore else '？？？？？？？？？？？？'
        $info88 = "\n{size=-5}购买食物{/size}" if 3 in p.visitedStore else '\n{size=-5}还没去过这里，来这里逛一逛吧？{/size}'
        imagebutton auto "imagemap/shopstreet/food_%s.webp":
            focus_mask True
            if not exploring:
                action [Hide("info"), Show(screen="info_use", pp=renpy.get_mouse_pos(),i=info8+info88, a=ad8)]
            else:
                if persistent.actionquickly:
                    action Hide("info"),Hide("screen_map"),Hide("screen_shopstreet_map"),Hide("info_confirm"),Return(),Jump("explore_shop_3")
                else:
                    action [Hide("info"), Show(screen="info_confirm",text='去这里',act=[Hide("screen_map"),Hide("screen_shopstreet_map"),Hide("info_confirm"),Return(),Jump("explore_shop_3")], pp=renpy.get_mouse_pos(),i=info8+info88, a=ad8)]
            hover_sound audio.cursor
            hovered Show("info",i=info8+info88, a=ad8)
            unhovered Hide("info")

        
        $info9 = "{size=+8}文体商店{/size}" if 8 in p.visitedStore else '{size=+8}？？？{/size}'
        $ad9 = '小时候经常收集好看的本子，现在家里还有很多没有用完。' if 8 in p.visitedStore else '？？？？？？？？？？？？'
        $info99 = "\n{size=-5}购买收藏品{/size}" if 8 in p.visitedStore else '\n{size=-5}还没去过这里，来这里逛一逛吧？{/size}'
        imagebutton auto "imagemap/shopstreet/sportshop_%s.webp":
            focus_mask True
            if not exploring:
                action [Hide("info"), Show(screen="info_use", pp=renpy.get_mouse_pos(),i=info9+info99, a=ad9)]
            else:
                if persistent.actionquickly:
                    action Hide("info"),Hide("screen_map"),Hide("screen_shopstreet_map"),Hide("info_confirm"),Return(),Jump("explore_shop_8")
                else:
                    action [Hide("info"), Show(screen="info_confirm",text='去这里',act=[Hide("screen_map"),Hide("screen_shopstreet_map"),Hide("info_confirm"),Return(),Jump("explore_shop_8")], pp=renpy.get_mouse_pos(),i=info9+info99, a=ad9)]
            hover_sound audio.cursor
            hovered Show("info",i=info9+info99, a=ad9)
            unhovered Hide("info")



    frame:
        at map_appear
        style "translucent_frame"
        xfill True
        ysize 75
        textbutton '{size=+5}B区商店街{/size}' text_style "white":
            action NullAction()
            ycenter 0.5
    
    hbox:
        at map_appear
        xpos 0.9
        ypos 0.85
        imagebutton auto "gui/menu/home_%s.png":
            at map_appear
            action [Hide("screen_shopstreet_map",transition=dissolve),Hide("info")]
            unhovered Hide("info")
            hovered Show("info",i="离开商店街。")
            activate_sound audio.cursor
