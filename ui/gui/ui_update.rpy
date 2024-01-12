default update_list = [
    ['0.5.31',['完全修复了实习生小游戏bug，删除了游戏中跳出来的对话框','未解锁的日程在未达成解锁条件时不会再显示日程名','待办事项中新增了购买球拍和周末坐船的事项','优化了手机中的相册功能，选项变为下拉框'],'23/12/29'],
    ['0.5.32',['将acolas，halluke的隐藏剧情以及偶遇pathos的剧情现在可以剧情回顾了，但可能需要重新进行一次才能回顾','更新了统计应用的样式，现在可以记录严重和三维的加减情况','熟鱼给予的降严重效果从质量*2变为质量-1.5','鱼线断掉的概率从1%+每秒*2.5%变为了0.5%+每秒*0.1','治愈生病的概率所有来源都大幅下调了，具体治愈率变化为：','    阴天：30->5','    感冒药：3^层数->2^层数','    良好的睡眠/良好的运动：15每层->2.5每层','    体魄：5每层->1每层','    呼吸训练：30->15','在主界面添加了更新公告','更换了Pathos的部分立绘','修复若干bug'],'24/01/05'],
    ['0.5.33',['添加了存档导入导出功能，在存档列表下方多了一个下载按钮，点击即可复制存档的代码文件至剪贴板，存档列表右上角多了一个加号，它会读取你剪贴板的内容，如果你之前复制了其他人的存档，那么点击这里可以将存档导入进游戏中，你可以以这种方式分享你的存档，或是将出现bug的存档发到频道，来帮助解决bug','在赞助者模式下，委托界面多了一个按钮，允许你快速刷新委托，而在buff界面，点击查看也多出了一个移除buff的按钮','优化了读取本日和继续的逻辑，现在应该会正确读取本日存档','在赞助者模式下，不会再因为进行一些行为导致分数不被计入','修复若干bug'],'24/01/06'],
    ['0.5.34',['修复了过夜判定buff会额外多判定几次的bug','修复了不卖冰箱的bug','修复了地狱通关时产生的bug','调整了导出存档导出的代码，之前复制出的代码无法转移回存档，现在可以复制给其他人了','地狱过夜消耗的体魄概率变为33，灵感不变','弹珠机获取的灵感变为每次两个',],'24/01/07'],
    ['0.5.35',['修复了过夜判定buff概率出现报错的index out of range的bug','手机的最低电量为1','上调了涨工资增加的金额','增加书本《深沉之雨》，《实用百科全书》，《紫罗兰的洗礼》','《书》现在还会将严重倍率降低至1.0','《保持清醒的秘诀》每次工作会额外增加工作量从5%*最大工作量变为10%*最大工作量，同时会提示具体增加的数值。','《呼吸训练》现在会在治愈失败时提升一倍的治疗率。',],'24/01/10'],
    ['0.5.36',['增强了统计功能，现在可以查看到具体是哪些行动增加了精神状态或属性，需要从头记录新数据','重做了寻羊历险记，现在会在持续时间内自动选择更好的结果','重做了右丙氧芬，现在持续时间内不会刷出药物依赖','修复了一个bug，该bug导致指导Destot工作日程会提前结算日程结束时判定的效果',],'24/01/10'],

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