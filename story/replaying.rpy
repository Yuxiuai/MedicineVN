label afterreplay:
    $p.times = replaying_times
    $p.stime()
    $replaying = False
    show screen screen_dashboard(p)
    $routine_bg(p)
    $routine_music(p)
    jump operate_screen_label