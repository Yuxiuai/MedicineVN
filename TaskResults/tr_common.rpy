screen Task_processing_screen(player): #show screen freeze(5)
    modal True
    zorder 50
    python:
        if persistent.nowaiting:
            time = 0.1
        else:
            time = 2
    timer time:
        action Hide(screen="Task_processing_screen")

    button:
        xfill True
        yfill True
        action NullAction()

label Task_processing:
    $_game_menu_screen = None
    show screen Task_processing_screen(p)
    if persistent.nowaiting:
        "。。。。。。{fast}{nw}"
    else:
        "{cps=4}。。。。。。{nw}"
    $_game_menu_screen = 'preferences'
    return


label NoTask_beginning:
    "当你看到这条消息时说明日程分配出现了错误，请重新读档。"
    return

label moduleerror:
    "当你看到这条消息时说明你出现了模组问题，例如没有开启模组却使用了模组物品。"
    return