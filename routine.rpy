label wakeup:
    $ quick_menu = False
    $ _game_menu_screen = None
    $ renpy.block_rollback()
    scene black
    if not persistent.nomedicine:
        play music audio.alarm
        if not persistent.quickAlarm:
            $ pause(2)
        scene bedroom at setcolor with dissolve
        if p.cured >= 84:
            show blurred:
                alpha (1-(-0.048 * p.cured + 5))
    $ quick_menu = True
    $ _game_menu_screen = "save"
    jump alarmCircle

label alarmCircle:
    if Novice.has(p):
        $Novice.get(p).afterSleepAction(p)
    $ renpy.block_rollback()
    if persistent.nomedicine:
        stop music
        show screen screen_dashboard(p)
        jump beforeCircle
    if not persistent.quickAlarm:
        $ pause(2)
    menu:
        "关闭闹钟" if True:
            stop music
            play sound audio.button
            scene bedroom at setcolor with fade
            if p.cured >= 84:
                show blurred:
                    alpha (1-(-0.048 * p.cured + 5))
            show screen screen_dashboard(p)
            pass
        "不理会" if True:
            scene black with fade
            $ pause(2)
            jump alarmCircle
    $ pause(2)
    jump medicineTake

label medicineTake:
    menu:
        "吃药":
            if p.meds() >0:
                $ temp = p.mental
                call screen screen_useMed(p)
                if p.mental != temp:
                    if p.cured<21:
                        "我拿起桌边早就提前盛好水的玻璃杯，将药瓶中的药物吞下。"
                        "……"
                elif True:
                    jump dontusemed_pro
            elif p.mental>0:
                if p.cured<21:
                    "已经没有药了吗？"
                    "我看着空瓶。"
                if p.today == 5:
                    if p.cured<21:
                        "今天就可以买更多的了。"
                        "妈的，凭什么我活着就得这么难受。"
                elif True:
                    if p.cured<21:
                        "……好吧，马上就到周五了，冷静，冷静，只要少工作多休息就行……"
            else:
                if p.cured>=21:
                    jump CuredBE
                jump ending2
        "不吃药":
            jump dontusemed

    if p.mental < 0:
        if p.cured<21:
            "不……不行，头还是很痛……"
        jump medicineTake
    elif True:
        if p.cured<21:
            "也许好点了。"
        jump beforeCircle

label dontusemed:
    if p.mental < 0:
        if p.cured>=21:
            jump CuredBE
        jump ending1
    elif True:
        jump beforeCircle

label beforeCircle:
    if p.cured >= 21:
        $ renpy.say(None, countdown(p))

    if p.cured >= 84:
        jump curedRoutine

    if p.today == 1 and p.week == 2:
        call solitus_route_3 from _call_solitus_route_3
    else:
        scene bathroom at setcolor with fade
        "洗漱……"

    if p.hal_p == 11 and p.today == 6:
        scene livingroom with fade
        "本以为能睡个好觉，妈的，突然被要求加班，什么情况啊那么急，就不能等周一再弄？我真是日了Halifax这个臭傻逼。"
        "这啥卵老板我真服了。"
        "噢……今天好像是Halluke体育考试啊……"
        "给他发个消息告诉他一声吧……"
        $ Message.new(p, p.name, 'Halluke','……我一直没胆量和你说明这件事，怕你知道我不是学校学生就对我敬而远之了。\n你说得对，我确实不是大学生，我已经工作1年了，就在H公司。\n总之我想和你说，今天老板突然要求我们加班，可能没法去帮你发球了。\n\n抱歉，祝考试顺利。',seen=True)
        "左手还在刷牙，我用右手快速打字给他发了消息。"
        "……"
        "点击发送，这样应该会好一点吧……"
        "噢！要迟到了……我得赶快出门了……"
        scene morningrun with fade
        $ p.onOutside = True
        $ p.times = 1
        "……"
        $ p.onOutside = False
        $ p.onVacation = False
    elif p.today in (1, 2, 3, 4 ,5) and not WeatherTornado.has(p):
        scene livingroom at setcolor with fade
        if p.cured >= 84:
            show blurred:
                alpha (1-(-0.048 * p.cured + 5))
        "……"
        if p.cured<21:
            "准备上班了。"
        scene morningrun at setcolor with fade
        if p.cured >= 84:
            show blurred:
                alpha (1-(-0.048 * p.cured + 5))
        $ p.onOutside = True
        $ p.times = 1
        if p.cured<21:
            "上班……"
        "……"
        $ p.onOutside = False
        $ p.onVacation = False
    else:
        scene workarea at setcolor with fade
        if WeatherTornado.has(p):
            "看来今天有台风过境啊……那应该就不用上班了……"
            $ per = p.achievedGoal/p.goal
            if per <= 60:
                "我还有好多工作没完成呢……得在家里加班了……"
            elif per < 80:
                "还剩些工作没做，在家里一边摸鱼一边做完好了……"
            else:
                "好耶！工作都弄完了，可以在家里狂摸鱼咯——"

    jump dayCircle


label dayCircle:
    $ renpy.block_rollback()
    
    $ p.times = 2


    if p.onVacation == False:
        if rrs(p, 5):
            scene office_ at setcolor with fade
        else:
            scene office at setcolor with fade
        if p.cured >= 84:
            show blurred:
                alpha (1-(-0.048 * p.cured + 5))
        $routineMusic(p)
        if p.hal_p == 13 and p.today == 1 and p.cured == -1:
            "当我刚坐在工位的椅子上准备打开电脑时，突然听到了有什么人在我身后故意咳嗽的声音。"
            "我回头看，是管理着这个部门的主管Arnel。"
            "白狼斟酌了一下，看上去十分别扭的样子。"
            $ SteamerTicket.add(p, 2)
            $ Notice.show()
            ar "“这是……嗯，这是这周六的游轮酒店船票…我去参加招标会给的赠礼。送你两张！别多话，别问我为什么送你，就这样。”"
            "我瞪大了眼睛，但是白狼却躲闪着我的目光，稍显急切地把两张船票拍在我的桌子上后便匆匆离开。"
            "我手忙脚乱的把手机连同船票一起放到桌子上，当我想道谢的时候，Arnel已经跑开了。"
            "…"
            "什么游轮啊？"
            "我拿起桌子上的船票，一搭眼便看到了德里莫游轮公司的logo。"
            "我去，这…这么珍贵的东西？就送我了？"
            "…"
            "德里莫游轮是最近停靠在A市附近的世界知名的豪华游轮酒店。"
            "曾经是交通工具的它现在变成了酒店，在各大海域运行，让游客欣赏海景。"
            "价格十分昂贵的同时也有完美的服务和绝佳的口碑。"
            "我从没想过自己有朝一日能去那样的酒店住宿一天…"
            "太牛逼了！"

            "呼…不过还是要冷静下来。"
            "Halluke…如果我带他去游轮上玩一天的话，应该会让他很开心吧。"
            "多出去玩的话……我到那个时候，应该也会逐渐喜欢上他吧…"
            "到时候在甲板上喂海鸥，在房间里和他独处…"
            "应该会很开心吧。"
            "那就邀请他好了。"
            if rrs(p, 5):
                scene office_ at setcolor with fade
            else:
                scene office at setcolor with fade
        elif p.aco_p == 12 and p.today == 1 and p.cured == -1:
            "当我刚坐在工位的椅子上准备打开电脑时，突然听到了有什么人在我身后故意咳嗽的声音。"
            "我回头看，是管理着这个部门的主管Arnel。"
            "白狼斟酌了一下，看上去十分别扭的样子。"
            $ SteamerTicket.add(p, 2)
            $ Notice.show()
            ar "“这是……嗯，这是这周六的游轮酒店船票…我去参加招标会给的赠礼。送你两张！别多话，别问我为什么送你，就这样。”"
            "我瞪大了眼睛，但是白狼却躲闪着我的目光，稍显急切地把两张船票拍在我的桌子上后便匆匆离开。"
            "我手忙脚乱的把手机连同船票一起放到桌子上，当我想道谢的时候，Arnel已经跑开了。"
            "…"
            "什么游轮啊？"
            "我拿起桌子上的船票，一搭眼便看到了德里莫游轮公司的logo。"
            "我去，这…这么珍贵的东西？就送我了？"
            "…"
            "德里莫游轮是最近停靠在A市附近的世界知名的豪华游轮酒店。"
            "曾经是交通工具的它现在变成了酒店，在各大海域运行，让游客欣赏海景。"
            "价格十分昂贵的同时也有完美的服务和绝佳的口碑。"
            "我从没想过自己有朝一日能去那样的酒店住宿一天…"
            "太牛逼了！"

            "呼…不过还是要冷静下来。"
            "Acolas…如果我带他去游轮上玩一天的话，应该会让他暂时脱离工作的事，好好放松吧。"
            "这家伙……居然真的把自己工作到差点死掉了……"
            "到时候在甲板上喂海鸥，在房间里和他独处…"
            "应该会很开心吧。"
            "那就邀请他好了。"
            if rrs(p, 5):
                scene office_ at setcolor with fade
            else:
                scene office at setcolor with fade
        if p.cured<21:
            "打完卡了，该准备计划一下今天要做的事了。"
    elif True:
        $routineMusic(p)

        if p.cured<21:
            "难得的假期，该准备计划一下今天要做的事了。"
    $ beforemusic=renpy.music.get_playing()
    $ p.beforeSchedule()
    show screen screen_dashboard(p)
    if SteamerTicket.has(p) and p.today == 6:
        stop music fadeout 5
        "呼，虽然我不是什么喜欢拖延的人，但终于到了周六，也该做一下决定了。"
        "去游轮酒店的的机会难得，而手术什么时候都能做，但我又何尝不想快点摆脱头疼呢？"
        "如果去游轮的话，我给Pathos打电话把手术推到下周；如果去做手术的话，就把票再还给Arnel，让他去送给别人好了。"
        "怎么办呢……"
        $ SteamerTicket.get(p).sub(p, 2)
        menu:
            "准备去医院做手术" if True:
                if Achievement402.has():
                    menu:
                        "是否直接抵达已经完成过的内容？"
                        "治愈线坏结局":
                            $p.cured = 0
                            jump CuredBE
                        "治愈线普通结局":
                            python:
                                for i in range(105 - p.cured):
                                    p.newDay()
                            $p.cured = 105
                            jump CE
                        "不需要":
                            pass
                        
                $p.onOutside = True
                jump CureEndingBeginning
            "和Halluke去游轮酒店" if p.route == 'h':
                $p.onOutside = True
                jump halluke_route_13
            "和Acolas去游轮酒店" if p.route == 'a':
                $p.onOutside = True
                jump acolas_route_12
    
    elif p.week == 15 and p.today == 6 and p.cured == -1 and not persistent.nocharacterplot :
        stop music fadeout 5
        "呼，终于，我的病要被治好了。"
        "我从未想过自己有一日真的能摆脱如此病痛，甚至不用额外花一分钱。"
        "我一直没有放弃，坚持到现在，都是完全值得的。"
        "那么，准备一下自己，去医院吧。"
        menu:
            "准备去医院做手术" if True:
                jump CureEndingBeginning

    jump TaskExecuting

label TaskExecuting:
    $ routineMusic(p)
    if p.times == 2:
        $ Message.allret(p)
        call screen screen_index(p)
        hide screen info
        hide screen info2
        hide screen info3
        if replaying == True:
            $renpy.jump(replaying_labelname)

        $ p.times+=1
        jump TaskExecuting
    elif p.times == 3:
        $ p.stime()
        if BookRiskEffect.has(p):
            $ constemp = p.mental
        $doplan(p, 0)
    elif p.times == 5:
        
        if BookRiskEffect.has(p) and constemp > p.mental:
            $ BookRiskEffect.cons += constemp - p.mental
            $ BookRiskEffect.renewInfo()
        if p.onVacation:
            scene workarea at setcolor with fade
            if p.cured >= 84:
                show blurred:
                    alpha (1-(-0.048 * p.cured + 5))
            if rra(p, 60):
                if p.cured<0:
                    $ MentRezB.add(p)
        elif True:
            if rrs(p, 5):
                scene office_ at setcolor with fade
            else:
                scene office at setcolor with fade
            if p.cured >= 84:
                show blurred:
                    alpha (1-(-0.048 * p.cured + 5))
        if p.cured<21:
            "上午的工作做完了，差不多该点个外卖吃午饭了。"
        $ Message.allret(p)
        call screen screen_index(p)
        hide screen info
        hide screen info2
        hide screen info3
        if replaying == True:
            $renpy.jump(replaying_labelname)
        $ p.times+=1
        jump TaskExecuting
    elif p.times == 6:
        if p.cured<21:
            "午休结束了……"
        $ p.times+=1
        jump TaskExecuting
    elif p.times == 7:
        if BookRiskEffect.has(p):
            $ constemp = p.mental
        $doplan(p, 1)
    elif p.times == 9:
        
        if BookRiskEffect.has(p) and constemp > p.mental:
            $ BookRiskEffect.cons += constemp - p.mental
            $ BookRiskEffect.renewInfo()
        if p.plan[1] != p.plan[0]:
            if p.cured<0:
                $ Inspiration.add(p)
        if p.onVacation == True:
            if rra(p, 60):
                if p.cured<0:
                    $ MentRezB.add(p)
            scene workarea at setcolor with fade
            if p.cured >= 84:
                show blurred:
                    alpha (1-(-0.048 * p.cured + 5))
            if p.cured<21:
                "有点累了，稍微摸会鱼吧……"
            $ p.times+=1
            scene workarea at setcolor with fade
            if p.cured >= 84:
                show blurred:
                    alpha (1-(-0.048 * p.cured + 5))
            if p.cured<21:
                "好了，该准备做晚上要做的事了。"
            $ Message.allret(p)
            call screen screen_index(p)
            hide screen info
            hide screen info2
            hide screen info3
            if replaying == True:
                $renpy.jump(replaying_labelname)
            $ p.times+=1
            jump TaskExecuting
        elif True:
            if rrs(p, 5):
                scene office_ at setcolor with fade
            else:
                scene office at setcolor with fade
            if p.cured >= 84:
                show blurred:
                    alpha (1-(-0.048 * p.cured + 5))
            if p.cured<21:
                "准备下班了……"
            $ p.times+=1
        jump TaskExecuting
    elif p.times == 10:
        if p.hal_p == 11 and p.today == 6:
            scene nightrun at setcolor with fade
            if p.cured >= 84:
                show blurred:
                    alpha (1-(-0.048 * p.cured + 5))
            $ p.onOutside = True
            "下班途中……"
            $ p.times+=1
            scene black with dissolve
            "……"
            play sound unlocking
            $ pause(0.5)
            play sound audio.button
            scene livingroom at setcolor
            if p.cured >= 84:
                show blurred:
                    alpha (1-(-0.048 * p.cured + 5))
            $ p.onOutside = False
            $ p.onVacation = True
            "终于下班了，给Halluke发个消息，看看他怎么样了吧。"
        elif p.onVacation == False:
            scene nightrun at setcolor with fade
            if p.cured >= 84:
                show blurred:
                    alpha (1-(-0.048 * p.cured + 5))
            $ p.onOutside = True
            if p.cured<21:
                "下班途中……"
            $ p.times+=1
            scene black with dissolve
            "……"
            play sound unlocking
            $ pause(0.5)
            play sound audio.button
            scene livingroom at setcolor
            if p.cured >= 84:
                show blurred:
                    alpha (1-(-0.048 * p.cured + 5))
            $ p.onOutside = False
            $ p.onVacation = True
            if p.cured<21:
                "终于到家了。"
                "该准备一下晚上要做的事了。"
        elif True:
            $ p.times+=1
            jump TaskExecuting
        $ Message.allret(p)
        call screen screen_index(p)
        hide screen info
        hide screen info2
        hide screen info3
        if replaying == True:
            $replaying_times = 9
            $renpy.jump(replaying_labelname)
        if p.hal_p in (11, 13) and p.today == 6:
            "我……被Halluke删了好友？"
            "不会吧……为什么？"
            "仅仅是因为我没去和他考试？"
            "可……但……这到底是为什么？"
            "我重新添加为好友，得到的却只有红色的拒绝。"
            "……"
            "某种挫败感交杂着怒火冲上大脑。"
            "所以我做了这么多，结果却是这样的么？"
            "我还没鼓起勇气先说再见，就先被他这种什么也不用担心，什么也不用顾虑的家伙删了？"
            "现在还有时间，我必须去找他问个清楚。"
            jump halluke_route_11
        jump TaskExecuting
    elif p.times == 11:
        if BookRiskEffect.has(p):
            $ constemp = p.mental
        $doplan(p, 2)





    elif p.times == 13:
        
        if BookRiskEffect.has(p) and constemp > p.mental:
            $ BookRiskEffect.cons += constemp - p.mental
            $ BookRiskEffect.renewInfo()
        if p.plan[2] != p.plan[1]:
            if p.cured<00:
                $ Inspiration.add(p)
        if p.today in (6, 7):
            if rra(p, 60):
                if p.cured<0:
                    $ MentRezB.add(p)
        scene livingroom at setcolor with fade
        if p.cured >= 84:
            show blurred:
                alpha (1-(-0.048 * p.cured + 5))



        if p.cured == 6:
            if 7 <= p.hal_p <= 13:
                play music audio.phonering
                menu:
                    "接电话" if True:
                        stop music
                "……"
                h "“嗨…我是Halluke…想打羽毛球吗？这周末…”"
                $ ss('no_hat bleak_eyes')
                s "“不了。”"
                $ sh()
                h "“啊……那……什么……”"
                $ ss('no_hat bleak_eyes')
                s "“……如果没事的话就挂了吧，我很累。”"
                $ sh()
                h "“哦……嗯……”"
                "我挂断电话。"
                "我突然意识到自己之前应该不会对他说这样的话的，但为什么直接就说出口了呢。"
                "他邀请我……我应该是……开心或者不开心……"
                "但我脑袋里只是空荡荡的，什么东西都没有。"
                "……有点奇怪，但是这对我来说有什么意义呢。"
            
            elif 3 <= p.aco_p <= 13:
                play music audio.phonering
                menu:
                    "接电话" if True:
                        stop music
                "……"
                a "“我是Acolas，这两天有时间在下班后和我吃点什么吗？”"
                $ ss('no_hat bleak_eyes')
                s "“不了。”"
                $ sh()
                a "“啊……那……什么……”"
                $ ss('no_hat bleak_eyes')
                s "“……如果没事的话就挂了吧，我很累。”"
                $ sh()
                a "“哦……嗯……”"
                "我挂断电话。"
                "我突然意识到自己之前应该不会对他说这样的话的，但为什么直接就说出口了呢。"
                "他邀请我……我应该是……开心或者不开心……"
                "但我脑袋里只是空荡荡的，什么东西都没有。"
                "……有点奇怪，但是这对我来说有什么意义呢。"

        if p.cured == 13:
            if 10 <= p.hal_p <= 13:
                play music audio.phonering
                menu:
                    "接电话" if True:
                        stop music
                h "“嗨……[p.name]……明天想去吃鸭血粉丝吗，我拿到了这学期的奖学金，可以请你一顿！”"
                h "“怎么样！出来玩嘛我好久没见到你了——”"
                $ ss('no_hat bleak_eyes')
                s "“不了。”"
                $ sh()
                h "“那你带我去小吃街转转嘛，带我吃你喜欢吃的东西？”"
                $ ss('no_hat bleak_eyes')
                s "“没兴趣。”"
                $ sh()
                h "“……所以，你是出了什么事吗？有事情可以和我说，别看我只是大学生，但我能帮的都会尽量做的。”"
                $ ss('no_hat bleak_eyes angry_eyebrow')
                s "“停下。”"
                $ sh()
                h "“抱歉，我只是想……”"
                "我挂断电话。"
                "……"
                "我好像很久没到上班路上之外的地方了，记得之前还经常外出瞎逛，现在想想真是无聊。"
                "我宁愿躺在床上。"
        
            elif 10 <= p.aco_p <= 13:
                play music audio.phonering
                menu:
                    "接电话" if True:
                        stop music
                "……"
                a "“Acolas，抱歉，这段时间对你说了一些伤人的话，可能我最近工作太累了……”"
                a "“那个……要不要来我家聊聊游戏的事？”"
                $ ss('no_hat bleak_eyes')
                s "“不了。”"
                $ sh()
                a "“那我们去看电影怎么样？听说最近新上了一部……？”"
                $ ss('no_hat bleak_eyes')
                s "“没兴趣。”"
                $ sh()
                a "“……所以，你是出了什么事吗？我知道我真的做错了很多事，但是至少给我弥补的机会……”"
                $ ss('no_hat bleak_eyes angry_eyebrow')
                s "“停下。”"
                $ sh()
                a "“抱歉，我只是想……”"
                "我挂断电话。"
                "……"
                "我好像很久没到上班路上之外的地方了，记得之前还经常外出瞎逛，现在想想真是无聊。"
                "我宁愿躺在床上。"

        if p.cured == 20:
            if 11 <= p.hal_p <= 13:
                play music audio.phonering
                menu:
                    "接电话" if True:
                        stop music
                h "“那个，[p.name]？是你吧？”"
                $ ss('no_hat bleak_eyes')
                s "“是。”"
                $ sh()
                h "“不知道这个时间给你打电话有没有打扰到你，但你一直没回我消息…真的没事吧？”"
                $ ss('no_hat bleak_eyes')
                s "“没事。”"
                $ sh()
                h "“噢，好吧。”"
                "我挂断电话，目光瞟了一眼某信上的十多个红点标志。"
                "…"
                "翻了翻，基本上都是些无聊的垃圾对话，还有一些生活琐事…"
                "这种事为什么要给我发…有什么意义吗？"
            
            elif 11 <= p.aco_p <= 13:
                play music audio.phonering
                menu:
                    "接电话" if True:
                        stop music
                "……"
                a "“[p.name]？最近如何，有没有好好工作啊……哦，应该是好好休息！”"
                $ ss('no_hat bleak_eyes')
                s "“有。”"
                $ sh()
                a "“不知道这个时间给你打电话有没有打扰到你，但你一直没回我消息…真的没事吧？”"
                $ ss('no_hat bleak_eyes')
                s "“没事。”"
                $ sh()
                a "“噢，好吧。”"
                "我挂断电话，目光瞟了一眼某信上的十多个红点标志。"
                "…"
                "翻了翻，基本上都是些无聊的垃圾对话，还有一些生活琐事…"
                "这种事为什么要给我发…有什么意义吗？"

        if p.cured == 27:
            if 11 <= p.hal_p <= 13:
                play music audio.phonering
                menu:
                    "接电话" if True:
                        stop music
                h "“那个…我有点担心你，你之前不是这样的…？”"
                $ ss('no_hat bleak_eyes angry_eyebrow')
                s "“我最近真的很忙，我也不想出门，我只想下班了之后就回床上倒着，你听明白了没有？”"
                $ sh()
                "我挂断电话。"

                play music audio.phonering
                menu:
                    "接电话" if True:
                        stop music

                h "“[p.name]…我知道你其实讨厌我对吧…我…”"
                "我挂断电话。"

                play music audio.phonering
                menu:
                    "接电话" if True:
                        stop music

                h "“既然如此为什么当时还要拯救我？”"
                "我挂断电话。"

                play music audio.phonering
                menu:
                    "接电话" if True:
                        stop music

                h "“我死了，你就开心了，不是吗？”"
                "我挂断电话。"
            elif 11 <= p.aco_p <= 13:
                play music audio.phonering
                menu:
                    "接电话" if True:
                        stop music
                a "“你已经很久没来开会了，到底出了什么事？我看不到你出席总是让我很紧张。”"
                $ ss('no_hat bleak_eyes angry_eyebrow')
                s "“没出什么事，我只是不想去而已，公司也没有规定必须要去听周会，你能不能不要烦我了？”"
                $ sh()
                "我挂断电话。"

                play music audio.phonering
                menu:
                    "接电话" if True:
                        stop music

                a "“[p.name]…对不起……我…”"
                "我挂断电话。"

                play music audio.phonering
                menu:
                    "接电话" if True:
                        stop music

                a "“都怪我，求你原谅我……”"
                "我挂断电话。"

                play music audio.phonering
                menu:
                    "接电话" if True:
                        stop music

                "从电话中只有呜咽声和他模糊得听不出音节的话。"
                "我挂断电话。"


        if p.cured < 0 and SteamerTicket.has(p) and p.today == 1:
            play music audio.phonering
            menu:
                "接电话" if True:
                    stop music
            "……"
            play music audio.solitus fadein 5
            pathos "“噢，晚上好，[p.name]先生。”"
            pathos "“感谢你这几个月对于这些尚未上市的药物进行测试，看样子它们的效果良好，而且也让我们清楚你的病的具体病因。”"
            pathos "“这周六的上午就可以来医院准备做手术了，作为第一个患上这种新病的人，我们决定把你的这种病称为S型综合征，同时免除手术费用。”"
            pathos "“毕竟你买药也都花了不少钱了吧，现在再让你那么多出来你应该也拿不出。”"
            pathos "“怎么样，是不是对我感恩戴德了？是不是想和我疯狂说谢谢？”"
            $ ss("surprised_eyebrow surprised_eyes")
            s "“啊…”"
            $ sh()
            "可以说我被这个突如其来的喜讯冲昏了头。"
            "那么，折磨了我二十多年的头疼终于要在这周五画上等号了吗？"
            "这种感觉很微妙，我是不是应该兴奋得上蹿下跳呢？"
            "但我为什么感觉没那么开心？或者说，我总觉得有什么不好的事就要发生了？"
            $ ss()
            s "“我…”"
            $ sh()
            pathos "“打住，我知道你肯定很开心，开心到疯，但你可以和你的好朋友说，而不是我。因为我现在要睡觉了，拜～”"
            play sound audio.interruption
            "电话断了。"
            "…这人，怎么那么屑啊。"
            if p.route == 'h':
                "可是，周六还要和Halluke去德里莫号玩一个双休日呢…"
                "是把手术往后推，还是放弃去豪华轮船上和Halluke看海的机会？"
            elif p.route == 'a':
                "可是，周六还要和Acolas去德里莫号玩一个双休日呢…"
                "是把手术往后推，还是放弃去豪华轮船上和Acolas看海的机会？"
            "…周六再说吧。"
            scene livingroom at setcolor with fade
        elif p.cured < 0 and p.week == 15 and p.today == 1 and not persistent.nocharacterplot:
            play music audio.phonering
            menu:
                "接电话" if True:
                    stop music
            "……"
            play music audio.solitus fadein 5
            pathos "“噢，晚上好，[p.name]先生。”"
            pathos "“感谢你这几个月对于这些尚未上市的药物进行测试，看样子它们的效果良好，而且也让我们清楚你的病的具体病因。”"
            pathos "“这周六的上午就可以来医院准备做手术了，作为第一个患上这种新病的人，我们决定把你的这种病称为S型综合征，同时免除手术费用。”"
            pathos "“毕竟你买药也都花了不少钱了吧，现在再让你那么多出来你应该也拿不出。”"
            pathos "“怎么样，是不是对我感恩戴德了？是不是想和我疯狂说谢谢？”"
            $ ss("surprised_eyebrow surprised_eyes")
            s "“啊…”"
            $ sh()
            "可以说我被这个突如其来的喜讯冲昏了头。"
            "那么，折磨了我二十多年的头疼终于要在这周五画上等号了吗？"
            "这种感觉很微妙，我是不是应该兴奋得上蹿下跳呢？"
            "但我为什么感觉没那么开心？或者说，我总觉得有什么不好的事就要发生了？"
            $ ss()
            s "“我…”"
            $ sh()
            pathos "“打住，我知道你肯定很开心，开心到疯，但你可以和你的好朋友说，而不是我。因为我现在要睡觉了，拜～”"
            play sound audio.interruption
            "电话断了。"
            "按理来说这种程度的通知仅仅只是通过电话来吗？"
            "而我在听到了这个消息之后，是应该狂喜才对吗？"
            "还是说现在的我一时没有晃过神来？"
            "我……我终于不用再头疼了？对吗？"
            "不用每天听着嘈杂的闹钟在半夜起来吃药，不用精打细算工资花钱买药，也可以自由自在出去乱逛不受头疼困扰，也不用在工作的时候害怕自己一个不小心就挂掉！"
            "啊！——"
            "我只感觉心脏跳动的速度正以指数级别上升，我有多久没有这么开心了？"
            "呼吸，呼吸。"
            "我突然想起小时候玩的一款手机游戏，在活动期间刷副本有极低的概率获得一件免费的角色时装，同时还会触发全服公告，说某人获得了这件时装。"
            "那时的我在百无聊赖的一次次刷本中丧失了耐心，但当那件时装图标出现在战利品栏中，16岁的我便在家长的房间里大呼小叫，上蹿下跳。"
            "现在的我和那个时候的我相比哪个更加开心呢？但当我想上蹿下跳抒发一下兴奋时，突然意识到，这间公寓里只有我一个人而已。"
            "倒也没什么动力了。"
            "……无论如何，我仍然很开心就是了。"
            "还剩几天，这段时间就多休息休息，少工作，让自己顺畅地活到周末吧。"
            scene livingroom at setcolor with fade


        if p.cured<21:
            "一天又快结束了，睡觉之前做些什么呢？"
        $ Message.allret(p)
        call screen screen_index(p)
        hide screen info
        hide screen info2
        hide screen info3
        if replaying == True:
            $renpy.jump(replaying_labelname)
        $ p.times+=1
        jump TaskExecuting
    elif p.times == 14:
        scene bedroom at setcolor with fade
        if p.cured >= 84:
            show blurred:
                alpha (1-(-0.048 * p.cured + 5))
        if p.cured<21:
            if not p.s8 and p.week >= 2:
                $temp = True
                python:
                    for i in p.itemcd:
                        if i.kind == '食物':
                            temp = False
                if temp:
                    jump solitus_route_8
                else:
                    "该睡觉了。"
            else:
                "该睡觉了。"
            
        elif True:
            "……"
        jump dayEnd
    elif True:
        "游戏时间发生错误！现在时间为[p.times]！"
        return

label dayEnd:
    if p.cured == 21:
        $ p.severity = 0.5
        $ LifeIsColorless.add(p)
    if p.cured == 42:
        $ p.severity = 0.3
    if p.cured == 63:
        $ p.severity = 0.2
    if p.cured == 84:
        $ p.severity = 0.1
    $ p.newDay()
    $ Save.save(p)
    $ Notice.add('存档已保存！')
    $ Notice.show()
    call loading from _call_loading_1
    if p.hal_p == 15 or p.aco_p == 14:
        jump before_earthquake
    jump wakeup


screen screen_useMed(player):

    use barrier(screen="screen_useMed", mode=0)

    $ items = list(filter(lambda x: type(x).kind=='实验药物' and not x.broken, player.items))


    zorder 200

    drag:
        xcenter 0.5
        ycenter 0.48
        has frame:
            at trans_toRight()
            style "translucent_frame"
            xsize 700
            ysize 800
        vbox:
            frame:
                background None
                yalign 0.001
                textbutton '{size=+10}使用药物{/size}':
                    text_style "gameUI"
                    xoffset -5
                    yoffset -5
                    action NullAction()

                imagebutton auto "gui/exit_%s.png":
                    xalign 1.0
                    action [Hide("screen_useMed_confirm"), Return(None)]

                frame:
                    background None
                    ysize 640
                    xsize 700
                    ypos 60
                    xpos 15

                    has viewport:
                        mousewheel True
                        draggable True
                    use screen_useMed_show(player, items)

screen screen_useMed_show(player, items):
    vbox:
        xsize 640
        $ typename = '实验药物'
        $ typei = itemKindInfo('实验药物', 'i')
        $ typea = itemKindInfo('实验药物', 'a')
        hbox:
            textbutton '{size=-5}'+typename+'{/size}' text_style "white":
                action NullAction()
                hovered Show(screen="info", i=typei, a=typea)
                unhovered Hide("info")
                xfill True
                xalign 1.0
                activate_sound audio.cursor


        vbox:

            for ite in items:
                frame:
                    background None
                    ysize 60
                    xfill True
                    $ ite_name = type(ite).name
                    $ ite_pre = ite.getPrefixInfo(player)
                    $ ite_main = ite.getPrincipalInfo() + type(ite).getBenefit(player)
                    $ ite_suf = ite.getSuffixInfo()

                    frame:
                        background None
                        textbutton ite_name text_style "white":
                            action [Hide("info"),Show(screen="info_confirm", text='使用', act=Function(ui_itemUse, item=ite, player=player),r=True, pp=renpy.get_mouse_pos(), t=ite_name, i=ite_pre+'\n'+ite_main+ite_suf, a=type(ite).ad)]
                            hovered [Show(screen="info", t=ite_name, i=ite_pre+'\n'+ite_main+ite_suf, a=type(ite).ad)]
                            unhovered Hide("info")
                            background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)
                            activate_sound audio.cursor
                            xfill True

                    null height 2
        null height 30
        textbutton ''


label curedRoutine:
    show screen screen_dashboard(p)
    $ p.times = curedsettime(p.times)
    if p.cured == 105:
        jump CE
    if p.times == 3:
        $ p.beforeSchedule()
        
        $ gt = CuredTask.gt()
        menu:
            "工作" if p.today in (1, 2, 3, 4, 5) and p.cured < 98:
                $ Stat.record(p,CuredWork)
                jump CuredWork_beginning
            "休息" if p.today in (6, 7) and p.cured < 98:
                $ Stat.record(p,CuredRest)
                jump CuredRest_beginning
            "[gt]" if p.today in (1, 2, 3, 4, 5) and p.cured >= 98:
                $ Stat.record(p,CuredWork)
                jump CuredWork_beginning
            "[gt]" if p.today in (6, 7) and p.cured >= 98:
                $ Stat.record(p,CuredRest)
                jump CuredRest_beginning
            "放弃" if p.cured >= 91:
                jump CuredBE

    if p.times == 7:
        $ gt = CuredTask.gt()
        menu:
            "工作" if p.today in (1, 2, 3, 4, 5) and p.cured < 98:
                $ Stat.record(p,CuredWork)
                jump CuredWork_beginning
            "休息" if p.today in (6, 7) and p.cured < 98:
                $ Stat.record(p,CuredRest)
                jump CuredRest_beginning
            "[gt]" if p.today in (1, 2, 3, 4, 5) and p.cured >= 98:
                $ Stat.record(p,CuredWork)
                jump CuredWork_beginning
            "[gt]" if p.today in (6, 7) and p.cured >= 98:
                $ Stat.record(p,CuredRest)
                jump CuredRest_beginning
            "放弃" if p.cured >= 91:
                jump CuredBE

    if p.times == 11:
        $ gt = CuredTask.gt()
        menu:
            "休息" if p.today in (1, 2, 3, 4, 6, 7) and p.cured < 98:
                $ Stat.record(p,CuredRest)
                jump CuredRest_beginning
            "买药" if p.today == 5 and p.cured < 98:
                $ Stat.record(p,CuredHosp)
                jump CuredHosp_beginning
            "[gt]" if p.today in (1, 2, 3, 4, 6, 7) and p.cured >= 98:
                $ Stat.record(p,CuredRest)
                jump CuredRest_beginning
            "[gt]" if p.today == 5 and p.cured >= 98:
                $ Stat.record(p,CuredHosp)
                jump CuredHosp_beginning
            "放弃" if p.cured >= 91:
                jump CuredBE
    jump dayEnd