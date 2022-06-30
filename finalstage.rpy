init python:
    def to_the_final_stage(player):
        for i in range(len(player.effects) - 1, -1, -1):
            if player.effects[i].duration != -1:
                player.effects[i].clear(player)
        for i in range(len(player.items) - 1, -1, -1):
            player.items[i].remove(player)
        WeatherNone.add(player)
        Despair.add(player)

label earthquake:
    scene black
    stop music
    hide screen screen_dashboard
    play sound audio.earthquake
    call screen cfreeze(12)
    $to_the_final_stage(p)

    scene ruins
    "我睁眼。"
    show screen screen_dashboard(p)
    "……"