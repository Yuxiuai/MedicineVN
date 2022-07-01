label load_lastweek():
    $p=dcp(persistent.SaverClass[2])
    jump afterload

label load_yesterday():
    $p=dcp(persistent.SaverClass[1])
    jump afterload

label load_today():
    $p=dcp(persistent.SaverClass[0])
    jump afterload


label afterload:
    python:
        for i in p.unlockedTasks:
            i.unlocked = True
        for i in p.lockedTasks:
            i.unlocked = False

    $config.rollback_enabled = False
    call hide_all_screens from _call_hide_all_screens_1
    call loading from _call_loading_3
    if p.week==0 and p.day==29:
        jump wakeup_pro
    elif p.week==0 and p.day==30:
        jump wakeup_pro
    elif p.week==0 and p.day==1:
        jump wakeup_pro
    elif p.week==1 and p.day==2:
        jump wakeup_pro
    else:
        jump wakeup