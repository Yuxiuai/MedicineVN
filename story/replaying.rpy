label afterreplay:
    $p.stime()
    if renpy.music.get_playing()!=beforemusic:
        play music beforemusic fadein 5
    if p.onVacation:
        scene workarea with fade
    else:
        scene office with fade
    jump TaskExecuting