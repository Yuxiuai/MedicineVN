transform bright:
    matrixcolor BrightnessMatrix((persistent.brightvar-1.0))

transform sprite_test():
    zoom 0.45
    xcenter 0.5
    yalign 1.0

transform sprite_appear():
    matrixcolor SaturationMatrix(value=getcolor())
    xoffset -100
    easein 0.2 xoffset 0

transform trans_toRight(wait = 0):
    matrixcolor SaturationMatrix(value=getcolor())
    xoffset -100
    alpha 0.0
    pause(wait)
    easein 0.2 xoffset 0 alpha 1

transform trans_toLeft(wait = 0):
    matrixcolor SaturationMatrix(value=getcolor())
    xoffset 100
    alpha 0.0
    pause(wait)
    easein 0.2 xoffset 0 alpha 1


transform trans_Down(wait = 0):
    matrixcolor SaturationMatrix(value=getcolor())
    yoffset -100
    alpha 0.0
    pause(wait)
    easein 0.2 yoffset 0 alpha 1

transform trans_Up(wait = 0):
    matrixcolor SaturationMatrix(value=getcolor())
    yoffset 100
    alpha 0.0
    pause(wait)
    easein 0.2 yoffset 0 alpha 1

transform med_menu(wait = 0):
    matrixcolor SaturationMatrix(value=getcolor())
    xoffset 100
    alpha 0.0
    pause(wait)
    easein 0.2 xoffset 0 alpha 1

    #on hover:
        #linear 0.2 xoffset -50
    #on idle:
        #linear 0.2 xoffset 0

transform screen_notify_appear(wait = 0):
    matrixcolor SaturationMatrix(value=getcolor())
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

transform tdissolve(time=0.5):
    alpha 0.0
    linear time alpha 1.0

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

transform colorize(color):
    matrixcolor TintMatrix(color)


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


transform darken(val=-0.5):
    matrixcolor BrightnessMatrix(value=val)

transform nocolor:
    matrixcolor SaturationMatrix(value=0.0)


transform jumpscare:
    matrixcolor SaturationMatrix(value=0.0)
    #matrixcolor TintMatrix("#f00")
    zoom 3.5
    xalign 0.5
    yalign -1.0
    ease 0.5 yalign 0.35

transform jumpscare_p:
    parallel:
        easeout 0.3 zoom 4.5 yoffset 3000
    parallel:
        ease 0.025 xoffset 70
        ease 0.025 xoffset 110
        repeat
    #parallel:
    #    linear 0.35 zoom 4.0
    #parallel:
    #    linear 0.35 yoffset 2500

init python:
    def getcolor():
        if p:
            return p.color
        else:
            return 1.0
        

transform setcolor:
    matrixcolor SaturationMatrix(value=1.0 if not p else p.color)

transform headache_trans:
    parallel:
        xcenter 0.5
        ycenter 0.5
        easein 0.5 zoom 1.01
        easein 0.5 zoom 1.0
        0.5
        repeat
    parallel:
        easein 0.2 xoffset 1
        easeout 0.2 xoffset 0
        easein 0.2 xoffset -1
        repeat
    parallel:
        easein 0.2 yoffset 1
        easeout 0.2 yoffset 0
        easein 0.2 yoffset -1
        repeat

transform blurr_concentration(p):
    alpha (1-(-0.048 * p.cured + 5))

transform disso:
    alpha 0.0
    easein 0.2 alpha 1

transform toyduck:
    
    parallel:
        easein 0.2 xzoom 1.3
    parallel:
        easein 0.2 yzoom 0.8
    parallel:
        easein 0.2 yoffset 10

    block:
        parallel:
            easein 0.2 xzoom 1.0
        parallel:
            easein 0.2 yzoom 1.0
        parallel:
            easein 0.2 xoffset 0
        parallel:
            easein 0.2 yoffset 0

transform toyduck2:
    parallel:
        easein 0.2 xzoom 1.3
    parallel:
        easein 0.2 yzoom 0.8
    parallel:
        easein 0.2 yoffset 10
    

    block:
        parallel:
            easein 0.2 xzoom 1.0
        parallel:
            easein 0.2 yzoom 1.0
        parallel:
            easein 0.2 xoffset 0
        parallel:
            easein 0.2 yoffset 0

transform med_bottle():
    matrixcolor SaturationMatrix(value=getcolor())
    alpha 0.0
    easein 0.2 alpha 1
    
    on hover:
        easein 0.2 yoffset -50
    on idle:
        easein 0.2 yoffset 0

transform med_bottle_shadow():
    alpha 0.0
    easein 0.2 alpha 1

    on hover:
        easein 0.2 zoom 0.8
    on idle:
        easein 0.2 zoom 1.0

transform tzoom(z):
    zoom z