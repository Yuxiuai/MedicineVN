screen ctc(arg=None):
    zorder 100
    add "gui/ctc.png" xalign 0.93 yalign 0.96 at ctc_bob


screen barrier(screen, mode=1):
    if mode == 0:
        button:
            xfill True
            yfill True
            action NullAction()
    else:
        button:
            xfill True
            yfill True
            action Hide(screen)



screen freeze(time=None): #show screen freeze(5)
    modal True
    zorder 50
    if persistent.nowaiting == True:
        $time=0.1
    timer time:
        action Hide(screen="freeze")

    button:
        xfill True
        yfill True
        action NullAction()

screen cfreeze(time=None): #call screen freeze(5)
    modal True
    zorder 50
    if persistent.nowaiting == True:
        $time=0.1
    timer time:
        action Return()

    button:
        xfill True
        yfill True
        action NullAction()



label hide_all_screens:
    hide screen screen_dashboard
    hide screen screen_dashboard_calendar
    hide screen screen_dashboard_medicine
    hide screen screen_dashboard_severity
    hide screen screen_dashboard_abilities
    hide screen screen_dashboard_effects
    hide screen screen_effects
    hide screen screen_index
    hide screen screen_items
    hide screen screen_map
    hide screen screen_notify
    hide screen screen_phone
    hide screen screen_tasks
    hide screen info
    hide screen info2
    hide screen info3
    return

label hide_all_info:
    hide screen info
    hide screen info2
    hide screen info3
    return