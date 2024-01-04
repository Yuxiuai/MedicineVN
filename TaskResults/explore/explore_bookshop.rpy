label explore_bookshop:
    scene library with fade
    if p.times<11:
        "我推开了Ascalon书店的大玻璃门。"
        "前台本还在玩手机的白色老虎因为我的开门动作而抬起头来，随后便对我露出个微笑。"
        "不知道怎么回应他，只是对他点了点头。"
        "……随便看看吧。"
        jump explore_bookshop_choice
    else:
        "我推开了Ascalon书店的大玻璃门。"
        "已经很晚了，买完书就尽快离开好了……"
        jump explore_bookshop_buy
    
        
    

label explore_bookshop_choice:
    menu:
        "做些什么？"
        "买书":
            "买些新书吧。"
            jump explore_bookshop_buy
        "去阅读区" if p.times<11:
            jump explore_bookshop_rest
        "回去":
            zaster"“下次再来哦。”"
            $ss('normal2_eyebrow')
            s"“嗯。”"
            $ss('normal2_eyes')
            s"“那个……”"
            $ss('normal2_eyes smile_mouth')
            s"“下次见。”"
            $sh()
            "在对话里额外添加一些无关紧要的客套话就是我唯一能够尝试的聊天手段了，但很明显这并不会让他注意到我……"
            "或者说，我们之间好像总是隔着什么……"
            "……"
            "该回去了。"
            jump GoOutside_result

label explore_bookshop_buy:
    $temp = p.money
    call screen screen_explore_buybook(p)
    if p.times<11:
        if temp > p.money:
            zaster"“一共是这些钱哦，请保管好书籍——”"
        else:
            "没什么特别感兴趣的……过段时间再来看看好了。"

        jump explore_bookshop_choice
    else:
        "……"
        "不知道这么晚了还能不能打到车，总之得快点离开了。"
        jump GoOutside_result

label explore_bookshop_rest:
    $p.times+=1
    $BookstoreBuff.add(p)
    $Notice.show()
    $p.onOutside = False
    jump after_executing_task_label


label explore_bookshop_end:
    "差不多该回去了……"
    $BookstoreBuff.clearByType(p)
    jump before_operate_screen_label

screen screen_explore_buybook(player):
    #tag gamegui
    use barrier(screen="screen_explore_buybook", mode=0)

    python:
        allbooks = list(filter(lambda x: x.kind=='书籍', ALLITEMS))
        items = list(filter(lambda x: x not in [type(x) for x in list(filter(lambda x: x.kind=='书籍', p.items))], allbooks))
        items.sort(key=lambda x: x.id)

    #modal True
    zorder 200
    drag:
        xcenter 0.5
        ycenter 0.48
        frame:
            at trans_toRight()
            style "translucent_frame"
            xsize 700
            ysize 800
            vbox:
                frame:
                    background None
                    yalign 0.001
                    textbutton '{size=+10}购买书籍{/size}':
                        text_style "gameUI"
                        xoffset -5
                        yoffset -5
                        action NullAction()

                    imagebutton auto "gui/exit_%s.png":
                        xalign 1.0
                        action [Hide("screen_explore_buybook"), Return()]

                    frame:
                        background None
                        ysize 700
                        xsize 650
                        ypos 60
                        xpos 25

                        viewport:
                            mousewheel True
                            draggable True
                            scrollbars "vertical"
                            vbox:
                                $professBooks = [ProfessionalBookWorking, ProfessionalBookWriting, ProfessionalBookSeverity]

                                use screen_buylist(player, professBooks, p=0.4, d=20, n='专业类书籍')

                                null height 10

                                use screen_buylist(player, items, p=0.85, d=40, n='未收藏的书籍')

                                if Achievement306.has():
                                    null height 10

                                    use screen_buylist(player, [CactusCheat], p=2, d=40, n='其他书籍')
                                

                                null height 30
                                textbutton ''
                    