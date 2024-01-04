label afterreplay:
    window hide
    $sh()
    $p.times = replaying_times
    $p.stime()
    $p.onShip = False
    show screen screen_dashboard(p)
    $routine_bg(p)
    $routine_music(p)
    jump operate_screen_label