transform sprite_appear():
    xoffset -100
    easein 0.2 xoffset 0

transform trans_toRight(wait = 0):
    xoffset -100
    alpha 0.0
    pause(wait)
    easein 0.2 xoffset 0 alpha 1

transform trans_toLeft(wait = 0):
    xoffset 100
    alpha 0.0
    pause(wait)
    easein 0.2 xoffset 0 alpha 1


transform trans_Down(wait = 0):
    yoffset -100
    alpha 0.0
    pause(wait)
    easein 0.2 yoffset 0 alpha 1

transform trans_Up(wait = 0):
    yoffset 100
    alpha 0.0
    pause(wait)
    easein 0.2 yoffset 0 alpha 1

transform med_menu(wait = 0):
    xoffset 100
    alpha 0.0
    pause(wait)
    easein 0.2 xoffset 0 alpha 1

    #on hover:
        #linear 0.2 xoffset -50
    #on idle:
        #linear 0.2 xoffset 0

transform screen_notify_appear(wait = 0):
    xoffset -100
    alpha 0.0 
    pause(wait)
    easein 0.2 xoffset 100 alpha 1.0
    linear 0.2 xoffset -40
    linear 0.05 xoffset 20
    linear 0.05 xoffset -10
    linear 0.1 xoffset 0  # 1
    pause(persistent.notifyDuration-1)
    easein 0.2 xoffset 50
    easein 0.2 xoffset -200 alpha 0
    #linear 0.1 xoffset 50
    #linear 0.15 xoffset 100
    #linear 0.05 xoffset -25
    #linear 0.05 xoffset 0

transform reverse():
    yzoom -1
        
transform ctc_bob:
    yoffset 0
    xoffset -60
    xanchor 0.5
    ease 1.6 yoffset -10
    ease 1.6 yoffset 0
    ease 1.6 yoffset -10
    ease 1.6 yoffset 0
    ease 1.6 yoffset -10
    ease 1.6 yoffset 0
    ease 0.8 xzoom -1
    ease 0.8 xzoom 1
    repeat

transform turn(x=-1):
    ease 0.5 xzoom x

transform near:
    parallel:
        ease 1 zoom 2
    parallel:
        ease 1 yoffset 800

transform look:
    parallel:
        ease 1 zoom 2
    parallel:
        ease 1 yoffset 800
        ease 4 yoffset 0
        ease 2 zoom 3
        #ease 4 yoffset 800

transform look_:
    parallel:
        ease 1 zoom 1
    parallel:
        ease 1 yoffset 0

transform look_1:
    parallel:
        ease 1 zoom 2
    parallel:
        ease 1 yoffset 800
        ease 4 yoffset 0
        #ease 4 yoffset 800
        repeat


transform near_:
    parallel:
        ease 1 zoom 1
    parallel:
        ease 1 yoffset 0


transform sit:
    parallel:
        ease 1 zoom 1.3
    parallel:
        ease 1 yoffset 250



transform trans_mainmenu(wait = 0):
    xoffset 100
    alpha 0.0
    pause(wait)
    easein 0.4 xoffset 0 alpha 1


transform alp:
    alpha 0.0

transform map_appear:
    xoffset 1000
    alpha 0.0
    easein 0.3 xoffset 0 alpha 1

transform trans_app(xo, yo):
    on show:
        zoom 0
        xoffset xo
        yoffset yo
        parallel:
            ease 0.25 xoffset 0
        parallel:
            ease 0.25 yoffset 0
        parallel:
            ease 0.25 zoom 1
        #parallel:
        #    ease 1 align (0.5, 0.5)
    on hide:
        parallel:
            ease 0.25 zoom 0
        parallel:
            ease 0.25 xoffset xo
        parallel:
            ease 0.25 yoffset yo

transform head_trans:
    on show:
        xoffset -100
        linear 0.2 xoffset 0
    on hide:
        xoffset 0
        ease 0.2 xoffset -100 xzoom 0.0



