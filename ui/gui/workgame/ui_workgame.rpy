init -505:
    transform trans_workgame_dissolve(time):
        pause(time)
        alpha 1.0
        xanchor 0.5
        yanchor 0.5
        parallel:
            easein 0.5 rotate 360
        parallel:
            easein 0.5 zoom 0.001 alpha 0.0


screen ui_workgame(g):
    zorder 900
    predict False
    default poz = 960 - len(g.blocks) * 25
    default maxblocks = len(g.blocks)
    if g.blocks:
        #text '步数：%s' % (g.step) xcenter 0.5 ycenter 0.55
        text '点击方块即可消除与它相邻的同色方块！' style 'white' xcenter 0.5 ycenter 0.55
        vbox:
            xpos poz
            ypos 648
            
            hbox:
                for i, item in enumerate(g.blocks):
                    imagebutton auto item.icon:
                        action Function(g.touch, i), Function(g.end)
                        #activate_sound random_bubble()
                        if g.blocks[i].status == -1:
                            at trans_workgame_dissolve(g.transform(i))
                    
    if type(g.log[-1]) == Workgame_Win:
        timer g.log[-4].time + 0.5:
            action Return(g)


    


screen workgame_sayr(say_xp, say_yp, t='？'):
    zorder 100
    #$say_xp = rd(1000, 1100)
    #$say_yp = rd(100, 400)
    frame at trans_Up():
        background None
        xpos say_xp
        ypos say_yp
        add 'gui/game/sayr.png' at trans_Up()
        frame:
            background None
            padding (10, 0)
            xsize 170
            ysize 120
            text t style 'white' xalign 0.5
    timer 1.5 action Hide("workgame_sayr", Dissolve(1))

screen workgame_sayl(say_xp, say_yp, t="？"):
    zorder 100
    #$say_xp = rd(500, 700)
    #$say_yp = rd(75, 400)
    frame at trans_Up():
        background None
        xpos say_xp
        ypos say_yp
        add 'gui/game/sayl.png' at trans_Up()
        frame:
            background None
            padding (10, 0)
            xsize 170
            ysize 120
            text t style 'white' xalign 0.5
    timer 1.5 action Hide("workgame_sayl", Dissolve(1))

label workgame_test:
    stop music
    scene office with fade
    show destot with dissolve
    $g = Workgame()
    show screen workgame_sayr(rd(1000, 1100), rd(100, 400), '前辈……')
    show screen workgame_sayl(rd(500, 700), rd(75, 400), '我有一些问题……')
    call screen ui_workgame(g) with dissolve
    jump workgame_test




