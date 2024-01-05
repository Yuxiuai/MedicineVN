default update_list = [
    ['0.5.31',['完全修复了实习生小游戏bug，删除了游戏中跳出来的对话框','未解锁的日程在未达成解锁条件时不会再显示日程名','待办事项中新增了购买球拍和周末坐船的事项','优化了手机中的相册功能，选项变为下拉框'],'23/12/29'],
    ['0.5.32',['将acolas，halluke的隐藏剧情以及偶遇pathos的剧情现在可以剧情回顾了，但可能需要重新进行一次才能回顾','更新了统计应用的样式，现在可以记录严重和三维的加减情况','熟鱼给予的降严重效果从质量*2变为质量-1.5','鱼线断掉的概率从1%+每秒*2.5%变为了0.5%+每秒*0.1','治愈生病的概率所有来源都大幅下调了，具体治愈率变化为：','    阴天：30->5','    感冒药：3^层数->2^层数','    良好的睡眠/良好的运动：15每层->2.5每层','    体魄：5每层->1每层','    呼吸训练：30->15','在主界面添加了更新公告','更换了Pathos的部分立绘','修复若干bug'],'24/01/05'],
]


screen screen_gamemenu_new():
    zorder 2001
    tag menu
    style_prefix "game_menu"

    if main_menu:
        add persistent.main_menu_theme.bg

    frame:
        bottom_padding 45
        top_padding 180
        background "gui/overlay/confirm.png"
        frame:
            background None
            xfill True

            viewport:
                yinitial 1.0
                scrollbars "vertical"
                mousewheel True
                draggable True
                #xfill True
                xsize 1800
                #side_yfill True
                use screen_gamemenu_new_inner(update_list)


    imagebutton auto "gui/exit_%s.png":
        xalign 0.95
        yalign 0.05
        action Return()

    use menu_labelname('更新历史')
        


screen screen_gamemenu_new_inner(hlist):
    frame:
        style_prefix "history"
        xfill True
        background None
        vbox:
            spacing 30
            for h in hlist:

                vbox:
                    text h[0]:
                        yalign 0.5
                        substitute False
                        size 30
                        xfill True
                    for i in h[1]:
                        text i:
                            yalign 0.5
                            substitute False
                            size 20
                            xfill True
                    text h[2]:
                        yalign 0.5
                        substitute False
                        size 15
                        xfill True

            if not hlist:
                text _("更新历史为空。")