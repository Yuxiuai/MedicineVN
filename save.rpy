label load_lastweek():
    $Saver.load(Saver.lastweek)
    jump afterload

label load_yesterday():
    $Saver.load(Saver.yesterday)
    jump afterload

label load_today():
    $Saver.load(Saver.today)
    jump afterload


label afterload:
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