label afterreplay:
    $p.times = replaying_times
    $replaying = False
    show screen screen_dashboard(p)
    if p.times >= 10 or p.today in (6, 7):
        $ p.onOutside = False
        $ p.onVacation = True
        scene workarea with fade
    else:
        $ p.onOutside = False
        $ p.onVacation = False
        scene office with fade
    
    $routineMusic(p)
    jump TaskExecuting