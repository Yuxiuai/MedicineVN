label afterload:

    $ config.rollback_enabled = False
    call hide_all_screens from _call_hide_all_screens_1
    call loading from _call_loading_3
    $routineMusic(p)
    if Despair.has(p):
        jump despair_wakeup
    if p.hal_p == 14 and p.today == 7:
        jump halluke_route_14
    if p.hal_p == 13 and p.today == 7:
        jump acolas_route_13
    if p.week==0 and p.day==29:
        jump day0
    elif p.week==0 and p.day==30:
        jump wakeup_pro
    elif p.week==0 and p.day==1:
        jump wakeup_pro
    elif p.week==1 and p.day==2:
        jump wakeup_pro
    elif True:
        jump wakeup
