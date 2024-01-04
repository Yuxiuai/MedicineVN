screen screen_report(player):
    #tag gamegui

    #modal True
    zorder 600

    frame:
        xcenter 0.503
        ycenter 0.48
        at trans_toRight()
        style "translucent_frame"
        xsize 800
        ysize 800
        hbox:

            frame:
                background None
                xsize 400
                ysize 800
                frame:
                    background None
                    text _('{size=+10}身体情况报告{/size}'):
                        xoffset -5
                        style "white"

                    

                frame:
                    #xoffset -10
                    background None
                    ysize 700
                    xsize 750
                    ypos 60
                    xpos 10
                    use screen_report_list(player)
                frame:
                    #xoffset -10
                    background None
                    ysize 700
                    xsize 750
                    ypos 60
                    xpos 10
                    use screen_report_score(player)

            frame:
                background None
                xsize 400
                ysize 800
                

                imagebutton auto "gui/exit_%s.png":
                    xalign 0.98
                    action [Hide("screen_report",transition=dissolve),Hide("info"),Hide("info3"), Return()]
                    activate_sound audio.cursor


screen screen_report_list(player):
    python:
        player = Achievement.pretreatment(player)
        avares = 0
        for i in player.medinfo:
            avares += player.medinfo[i].res
        temp = avares / max(1, len(player.medinfo))
    frame:
        xfill True
        background None
        vbox:
            xalign 0.0
            text '计分项' style "white" size 25
            null height 10
            text '基础' style "white" size 18
            if p.experience != 'wri':
                text '工作能力：'style "white" xoffset 5 size 20
            text '身体素质：'style "white" xoffset 5 size 20
            text '写作技巧：'style "white" xoffset 5 size 20
            text '严重程度：'style "white" xoffset 5 size 20

            text '平台人气：'style "white" xoffset 5 size 20
            text '食物恢复效果：'style "white" xoffset 5 size 20

            text '平均药物抗性：'style "white" xoffset 5 size 20
            if GameDifficulty5.has(player):
                text '难度' style "white" size 18
                text '地狱：' style "white" xoffset 5 size 20
                

        vbox:
            xalign 0.78
            text '有效值' style "white" size 25 xalign 0.5
            null height 10
            text '' style "white" size 18
            if p.experience != 'wri':
                text '%s' % player.wor() style "white" xoffset 5 size 20 xalign 0.5
            text '%s' % player.phy() style "white" xoffset 5 size 20 xalign 0.5
            text '%s' % player.wri() style "white" xoffset 5 size 20 xalign 0.5
            text '%s' % player.sev() style "white" xoffset 5 size 20 xalign 0.5

            text '%s' % player.popularity style "white" xoffset 5 size 20 xalign 0.5
            text '%s%s' % (r2((1-player.fooduse*0.005)*100), '%') style "white" xoffset 5 size 20 xalign 0.5

            text '%s%s' % (r2(100-temp), '%') style "white" xoffset 5 size 20 xalign 0.5
            if GameDifficulty5.has(player):
                text '' style "white" size 18
                text '' style "white" xoffset 5 size 20 xalign 0.5
        vbox:
            xalign 0.98
            text '得分' style "white" size 25 xalign 0.5
            null height 10
            text '' style "white" size 18
            if p.experience != 'wri':
                text '+%s' % int(player.wor()*1000) style "white" xoffset 5 size 20 xalign 0.5
                text '+%s' % int(player.phy()*1250) style "white" xoffset 5 size 20 xalign 0.5
                text '+%s' % int(player.wri()*1250) style "white" xoffset 5 size 20 xalign 0.5
            else:
                text '+%s' % int(player.phy()*1750) style "white" xoffset 5 size 20 xalign 0.5
                text '+%s' % int(player.wri()*1750) style "white" xoffset 5 size 20 xalign 0.5
            text '-%s' % int(player.sev()*2000) style "white" xoffset 5 size 20 xalign 0.5

            text '+%s' % int(player.popularity*0.1) style "white" xoffset 5 size 20 xalign 0.5
            text '-%s' % int(player.fooduse*10) style "white" xoffset 5 size 20 xalign 0.5

            text '-%s' % int(temp*10) style "white" xoffset 5 size 20 xalign 0.5
            if GameDifficulty5.has(player):
                text '' style "white" size 18
                text '+100%' style "white" xoffset 5 size 20 xalign 0.5



screen screen_report_score(player):
    $score = int(Achievement.calScore(player))
    frame:
        xfill True
        background None
        
        vbox:
            xalign 0.0
            yalign 1.0
            text '总分：' style "white" size 35
            null height 10
            text '最终分数：' style "white" size 35
            null height 10
        
        vbox:
            xalign 0.98
            yalign 1.0
            text '%s' % score style "white" size 35 xalign 1.0
            null height 10
            text '%s' % int(score/max(1, player.week)) style "white" size 35 xalign 1.0
            null height 10