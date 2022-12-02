screen screen_phone_bg():
    modal True
    style_prefix "gameUI"
    zorder 100
    
    frame:
        at trans_Down()
        background None
        xcenter 0.5
        ycenter 0.5
        ysize 750
        xsize 400
        
        add "gui/phone/phone_desktop.png":
            xcenter 0.51
            ycenter 0.46

screen screen_phone_bg_():
    modal True
    style_prefix "gameUI"
    zorder 100
    
    frame:
        at trans_app
        background None
        xcenter 0.5
        ycenter 0.5
        ysize 750
        xsize 400
        
        add "gui/phone/phone_desktop_.png":
            xcenter 0.51
            ycenter 0.46


screen screen_phone(player):
    #tag gamegui
    modal True
    style_prefix "gameUI"
    zorder 100
    
    frame:
        at trans_Down()
        background None
        xcenter 0.5
        ycenter 0.5
        ysize 750
        xsize 400

        add "gui/phone/phone_desktopline.png":
            xcenter 0.5
            ycenter 0.45
        
        imagebutton idle "gui/phone/leviathan.png":
            action Function(CuteLeviathan)
            focus_mask True
            hovered Show(screen="info", i='普通的小猫咪壁纸，完全没有什么特别之处。', a='看什么看，你个三流程序员。')
            unhovered Hide("info") 
            xcenter 0.52
            ycenter 0.34

        frame:
            ypos .54
            background None
            xcenter 0.5
            hbox:
                spacing 40
                
                imagebutton auto "gui/phone/game_%s.png":
                    action [Hide("info"),Hide("screen_phone"),Show(screen="screen_phone_2048", player=player)]
                    hover_sound audio.cursor
                    hovered Show(screen="info", i='经典的小游戏2048。', a='关于Solitus平时摸鱼都在干什么。')
                    unhovered Hide("info")  

                imagebutton auto "gui/phone/camera_%s.png":
                    action [Hide("info"),Hide("screen_phone"),Show(screen="screen_phone_pic_address", player=player)]
                    hover_sound audio.cursor
                    hovered Show(screen="info", i='相机\n查看角色立绘。', a='偷拍婆的隐藏文件夹……等等，这拍的也太多了，还这么全面？')
                    unhovered Hide("info")   

                imagebutton auto "gui/phone/plot_%s.png":
                    action [Hide("info"),Hide("screen_phone"),Show(screen="screen_phone_video_address", player=player)]
                    hover_sound audio.cursor
                    hovered Show(screen="info", i='视频播放器\n回顾人物剧情。', a='缅怀某个叫做网课的东西。')
                    unhovered Hide("info")  

                imagebutton auto "gui/phone/pic_%s.png":
                    action NullAction()
                    hover_sound audio.cursor
                    hovered Show(screen="info", i='相册\n欣赏CG。\n\n（当前版本尚未开放，因为还没有CG，哈哈。）', a='一般我们都会管这个叫“画廊”，不过那听起来也太高贵了。')
                    unhovered Hide("info")  

        frame:
            ypos .67
            background None
            xcenter 0.5
            hbox:
                spacing 40
                imagebutton auto "gui/phone/write_%s.png":
                    action [Hide("info"),Hide("screen_phone"),Show(screen="screen_phone_commission", player=player)]
                    hover_sound audio.cursor
                    hovered Show(screen="info", i='写作平台\n通过接委托，完成委托或上传随笔来获得人气和报酬。\n接取的委托在所持物品中。', a='什么时候写东西也像画画那样来钱快粉丝涨的也快就好了……')
                    unhovered Hide("info")  
                imagebutton auto "gui/phone/note_%s.png":
                    #action [Hide("screen_phone"),Show(screen = "screen_phone_address", player = player, transition=dissolve)]
                    action [Hide("info"),ShowMenu(screen="screen_stat_local", player=player)]
                    hover_sound audio.cursor
                    hovered Show(screen="info", i='便笺\n统计各种数据。\n\n数据更新带有延迟，如数据无变化可以通过再次进入的方式刷新界面，也可以等待下一回合自动刷新。\n全局数据仅在每日存档时更新，重新游玩数据也会继续记录。', a='真的会有正常人事无巨细地把这些琐碎的经历都记下来吗？\n怎么可能会有呢~这些数据都是自动记录的~')
                    unhovered Hide("info") 
                imagebutton auto "gui/phone/ticket_%s.png":
                    action [Hide("info"),Hide("screen_phone"),Show(screen="screen_phone_food", player=player)]
                    hover_sound audio.cursor
                    hovered Show(screen="info", i='外卖平台\n购买用于在工作日午餐时间享用的食物。', a='不点外卖的话我就会去吃免费的工作餐。')
                    unhovered Hide("info") 
                imagebutton auto "gui/phone/music_%s.png":
                    action [Hide("info"),Hide("screen_phone"),Show(screen="screen_phone_music", player=player)]
                    hover_sound audio.cursor
                    hovered Show(screen="info", i='音乐播放器\n欣赏游戏音乐。', a='感觉……你药音乐不如你城……')
                    unhovered Hide("info")   
        frame:
            ypos .82
            background None
            xcenter 0.5
            hbox:
                spacing 40
                imagebutton auto "gui/phone/call_%s.png":
                    action [Hide("info"),Hide("screen_phone"),Show(screen = "screen_phone_address", player = player)]
                    hover_sound audio.cursor
                    hovered Show(screen="info", i='联系人\n和你的朋友打个电话聊聊天吧。', a='谁会直接和！送外卖的店家！打电话！啊！')
                    unhovered Hide("info")   
                $newmes = False
                
                if Message.hasNewMes(player):
                    imagebutton auto "gui/phone/new_%s.png":
                        action [Hide("info"),Hide("screen_phone"),Show(screen = "screen_phone_message_address", player = player)]
                        hover_sound audio.cursor
                        hovered Show(screen="info", i='某信\n有新消息了。', a='“永远爱你”\n“啊对对”')
                        unhovered Hide("info")  
                else:
                    imagebutton auto "gui/phone/message_%s.png":
                        action [Hide("info"),Hide("screen_phone"),Show(screen = "screen_phone_message_address", player = player)]
                        hover_sound audio.cursor
                        hovered Show(screen="info", i='某信\n和已经添加手机号的朋友聊天。', a='“永远爱你”\n“啊对对”')
                        unhovered Hide("info")   
                imagebutton auto "gui/phone/browser_%s.png":
                    action NullAction()
                    hover_sound audio.cursor
                    hovered Show(screen="info", i='浏览器\n（当前版本暂时不可用）', a='看会莓博吧，工作滚一边去。')
                    unhovered Hide("info")   
                imagebutton auto "gui/phone/shutdown_%s.png":
                    action [Hide("screen_phone",transition=dissolve),Hide("screen_phone_bg",transition=dissolve),Hide("info")]
                    hover_sound audio.cursor
                    hovered Show(screen="info", i='关机\n是时候做点有用的事了。', a='关掉，关掉，一定要关掉！')
                    unhovered Hide("info")  
    
    key 'K_ESCAPE' action [Hide("screen_phone",transition=dissolve),Hide("screen_phone_bg",transition=dissolve),Hide("info")]
    key 'q' action [Hide("screen_phone",transition=dissolve),Hide("screen_phone_bg",transition=dissolve),Hide("info")]
    key 'w' action [Hide("screen_phone",transition=dissolve),Hide("screen_phone_bg",transition=dissolve),Hide("info")]
    key 'e' action [Hide("screen_phone",transition=dissolve),Hide("screen_phone_bg",transition=dissolve),Hide("info")]
    key 'r' action [Hide("screen_phone",transition=dissolve),Hide("screen_phone_bg",transition=dissolve),Hide("info")]
