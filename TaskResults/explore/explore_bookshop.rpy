label explore_bookshop:
    scene library with fade
    "我推开了Ascalon书店的大玻璃门。"
    "前台本还在玩手机的白色老虎因为我的开门动作而抬起头来，随后便对我露出个微笑。"
    "真是可爱的小家伙。"
    "……"
    "买些新书吧。"
    $temp = p.money
    call screen screen_explore_buybook(p)
    python:
        allbooks = list(filter(lambda x: x.__base__==BookBase and not x.has(p), getSubclasses(Item)))
        if ProfessionalBookWorking in allbooks:
            allbooks.remove(ProfessionalBookWorking)
        if ProfessionalBookWriting in allbooks:
            allbooks.remove(ProfessionalBookWriting)
        if ProfessionalBookSeverity in allbooks:
            allbooks.remove(ProfessionalBookSeverity)
        if BookGameModule2 in allbooks and not GameModule2.has(p):
            allbooks.remove(BookGameModule2)
        if len(allbooks) == 0:
            Achievement302.achieve()
            Notice.show()
    if temp > p.money:
        zaster"一共是这些钱哦，请保管好书籍——"
    else:
        zaster"这就要走了吗，下次再来哦。"
    s"嗯。"
    s"那个……"
    s"下次见。"
    "在对话里额外添加一些无关紧要的客套话就是我唯一能够尝试的聊天手段了，但很明显这并不会让他注意到我……"
    "或者说，我们之间好像总是隔着什么……"
    "算了，该回去了。"
    jump GoOutside_result


screen screen_explore_buybook(player):
    #tag gamegui
    use barrier(screen="screen_explore_buybook", mode=0)

    python:
        allbooks = list(filter(lambda x: x.__base__==BookBase, getSubclasses(Item)))
        allbooks.remove(ProfessionalBookWorking)
        allbooks.remove(ProfessionalBookWriting)
        allbooks.remove(ProfessionalBookSeverity)
        if BookGameModule2 in allbooks and not GameModule2.has(p):
            allbooks.remove(BookGameModule2)

        items = list(filter(lambda x: x not in [type(x) for x in list(filter(lambda x: type(x).kind=='书本', p.items))], allbooks))
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
                            use screen_explore_buybook_show(player, items)
                    
screen screen_explore_buybook_show(player, items):
    vbox:
        $professBooks = [ProfessionalBookWorking, ProfessionalBookWriting, ProfessionalBookSeverity]

        use screen_buylist(player, professBooks, p=0.4, d=20, n='专业类书籍')

        null height 10

        use screen_buylist(player, items, p=0.85, d=40, n='未收藏的书本')

        null height 30
        textbutton ''