screen Task_processing_screen(player): #show screen freeze(5)
    modal True
    zorder 50
    $time=r2(2/player.wor())
    if persistent.nowaiting == True:
        $time=0.1
    timer time:
        action Hide(screen="Task_processing_screen")

    button:
        xfill True
        yfill True
        action NullAction()

label Task_processing:
    show screen Task_processing_screen(p)
    "{cps=3}。。。。。。"
    return


label NoTask_beginning:
    "当你看到这条消息时说明日程分配出现了错误，请重新读档。"
    jump to_the_title