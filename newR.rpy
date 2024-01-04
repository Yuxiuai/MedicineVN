##########################################################
##                起床和吃药
##
##########################################################

label wakeup:
    stop music
    $ screen_phone_write_page = 0
    $ screen_phone_write_inputwords = ''
    $ screen_phone_camera_cached = False
    $ screen_phone_message_send = ''
    $ screen_phone_message_page = 0
    $ phone_defaulted = False
    $ phone_cached_app = None
    $ phone_page = 0


    $p.onOutside = False
    $ quick_menu = False
    $ _game_menu_screen = None
    $ renpy.block_rollback()
    $ blackmask(p)

    if GameDifficulty5.has(p):
        if Debilitated.has(p):
            jump hardcorebe1
        if Decadent.has(p):
            jump hardcorebe2
        if Deterioration.has(p):
            jump hardcorebe3



    scene black
    if not persistent.nomedicine:
        if p.experience != 'wri':
            play music audio.alarm
        $renpy.show('blurred', at_list=[blurr_concentration(p)])
    $ quick_menu = True
    $ _game_menu_screen = "screen_gamemenu"
    jump alarmCircle

label alarmCircle:
    if Novice.has(p):
        $Novice.get(p).afterSleepAction(p)
    $ renpy.block_rollback()
    if persistent.nomedicine:
        stop music
        show screen screen_dashboard(p)
        jump before_go_out
    if p.experience == 'wri':
        if rra(p, 10):
            $p.times = 3
        menu:
            "起床" if True:
                stop music
                if HotelBuff.has(p):
                    scene location_hotel at setcolor with dissolve
                else:
                    scene bedroom at setcolor with dissolve
                $renpy.show('blurred', at_list=[blurr_concentration(p)])
                show screen screen_dashboard(p)
                pass
            "不起床" if True:
                scene black with fade
                if p.times == 0:
                    $p.times = 3
                else:
                    $p.times = 8
                $ pause(2)
                jump alarmCircle

    else:
        menu:
            "关闭闹钟" if True:
                stop music
                play sound audio.button
                if HotelBuff.has(p):
                    scene location_hotel at setcolor with dissolve
                else:
                    scene bedroom at setcolor with dissolve
                $renpy.show('blurred', at_list=[blurr_concentration(p)])
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
                scene cupboard at setcolor with dissolve
                call screen screen_useMed(p)
                if HotelBuff.has(p):
                    scene location_hotel at setcolor with dissolve
                else:
                    scene bedroom at setcolor with dissolve
                $renpy.show('blurred', at_list=[blurr_concentration(p)])
                if p.mental != temp:
                    if p.cured<21:
                        "我拿起桌边早就提前盛好水的玻璃杯，将药瓶中的药物吞下。"
                        "……"
                elif True:
                    jump dontusemed
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
            
        "尝试回忆美好的事情" if p.mental <= 0 and Novice.has(p):
            $step = r2((80 - p.mental) / 7)
            "这样做真的有用么？"
            $p.gain_mental(step)
            $Notice.show()
            $blackmask(p)
            $blackmask(p)
            "你深呼吸，试图压住随着痛苦飞速提升的心率。"
            $p.gain_mental(step)
            $Notice.show()
            $blackmask(p)
            "“你必须坚持，你还有很多事情没做完……”"
            $p.gain_mental(step)
            $Notice.show()
            $blackmask(p)
            "这就是你必须活下去的原因吗？"
            $p.gain_mental(step)
            $Notice.show()
            $blackmask(p)
            "……哈——呼——"
            $p.gain_mental(step)
            $Notice.show()
            $blackmask(p)
            "……这点痛苦……还没法打败我。"
            $p.gain_mental(step)
            $Notice.show()
            $blackmask(p)
            "不值一提……"
            $p.gain_mental(step)
            $Notice.show()
            $blackmask(p)
            "可是，我为什么要……如此坚持活下去……"
            $p.gain_mental(80.0 - p.mental)
            $Notice.show()
            $blackmask(p)
            "明明马上就要解脱了……"
            $Novice.clearByType(p)
            jump before_go_out
            

        "努力回忆温蔼的过去" if p.mental <= 0 and AMaverickLionEffect.has(p):
            $step = r2((AMaverickLionEffect.get(p).m - p.mental) / 7)
            "好疼，只剩下疼。"
            $p.gain_mental(step)
            $Notice.show()
            $blackmask(p)
            "你想吼叫出声，但在这空荡的房间中并没有谁能救你。"
            $p.gain_mental(step)
            $Notice.show()
            $blackmask(p)
            "解脱么？要去解脱么？想要让痛苦消逝殆尽么？"
            $p.gain_mental(step)
            $Notice.show()
            $blackmask(p)
            "想想美好的曾经，小时的你掉进了水库里，没有一个朋友敢去救你。"
            $p.gain_mental(step)
            $Notice.show()
            $blackmask(p)
            "在你的肺灌满水之前，你从水库里挣扎着爬了出来。"
            $p.gain_mental(step)
            $Notice.show()
            $blackmask(p)
            "那时的你会想到未来意图轻生的现在么？"
            $p.gain_mental(step)
            $Notice.show()
            $blackmask(p)
            "你必须坚持……"
            $p.gain_mental(AMaverickLionEffect.get(p).m - p.mental)
            $Notice.show()
            $blackmask(p)
            "不……现在还不是时候……我还有没做完的事……"
            $AMaverickLionEffect.clearByType(p)
            jump before_go_out
            

    if p.mental < 0:
        if p.cured<21:
            "不……不行，头还是很痛……"
        jump medicineTake
    elif True:
        if p.cured<21:
            "也许好点了。"
        jump before_go_out

label dontusemed:
    if p.mental < 0:
        if p.cured>=21:
            jump CuredBE
        jump ending1
    elif True:
        jump before_go_out

##########################################################
##                日常
##
##########################################################

label before_go_out:
    
    if p.experience == 'wri' and p.today == 1 and p.week == 1:
        "……"
        "我睁眼。"
        "并不美好的一天又开始了。"
        "手里的钱也不太够了，如果我还想活到周六的话，就得尽快写点委托了。"

    if HotelBuff.has(p):
        jump hotel_event


    # 钓鱼测试 ####################


    if p.experience == 'wri' and not GoFishing.isUnlocked(p):
        jump fish_event
    elif p.today == 6 and not GoFishing.isUnlocked(p):
        jump fish_event
    
    ###############################

    if p.cured >= 21:
        $ renpy.say(None, countdown(p))

    if p.cured >= 84:
        jump curedRoutine

    if p.hal_p == 11 and p.today == 6 and p.cured < 0 and not SteamerTicket.has(p) and p.experience != 'wri':
        jump work_overtime_h

    if p.today == 1 and p.week == 2 and p.experience != 'wri':
        call solitus_route_3 from _call_solitus_route_3
    else:
        scene bathroom at setcolor with fade
        $routine_narrator(p, _("洗漱……"))

    if p.today in (1, 2, 3, 4, 5) and WeatherTornado.has(p) and not SteamerTicket.has(p):
        jump tornado_event

    if SteamerTicket.has(p) and p.today == 6:
        jump prepare_for_surgery_1_1
    
    elif p.week == 15 and p.today == 6 and p.cured == -1 and not persistent.nocharacterplot:
        jump prepare_for_surgery_2_1

    
    if p.dep_p == 3:
        $Message.new(p, 'Depline', 'Depline', '这周末再出来玩玩吧，我还会去你那边，不过这次就我们两个好了！具体时间是周日下午左右哦，集合地点就在商店街的宾馆吧？', p.st()[0], p.st()[1], True,'',True)
    

    if p.today in (1, 2, 3, 4 ,5) and p.experience != 'wri':
        scene livingroom at setcolor with fade
        $renpy.show('blurred', at_list=[blurr_concentration(p)])

        if p.mental < 40:
            $ routine_narrator(p, _("凭什么我要一直坚持到现在啊……好想死啊……"))
        elif p.mental > 100:
            $routine_narrator(p, _("早上吃点什么呢……还是到了公司再点外卖吧……"))
        else:
            $routine_narrator(p, _("准备上班了。"))

        if type(p.effects[0]) == WeatherSmog and Mask.has(p):
            "今天好像有很重的雾霾啊……带上口罩吧。"
            $Mask.get(p).use(p)

        scene morningrun at setcolor with fade
        $ renpy.show('blurred', at_list=[blurr_concentration(p)])

        $ p.onOutside = True
        $ p.times += 1

        if p.mental < 40:
            $ routine_narrator(p, _("只觉得浑身都很疲惫，这样的我肯定撑不到下班吧。"))
        elif p.mental > 100:
            $routine_narrator(p, _("这个时间……应该不会迟到吧……"))
        else:
            $ routine_narrator(p, _("上班途中……"))
        
        jump before_go_office
        
        

    else:
        $ p.times += 2

        $ beforemusic=renpy.music.get_playing()

        jump before_operate_screen_label

label before_operate_screen_label:  ## 回到这里
    $ routine_bg(p)
    $ routine_music(p)
    if p.times == 2:
        
        python:
            if p.hal_p in (12, 13) and not persistent.noannoyhalluke:
                if not p.messages['Halluke']:
                    whats = []
                    for i in range(ra(p, 3, 5)):
                        whats.append(rca(p, ret_mes_halluke_mad['random']))
                    whats.append(rca(p, ret_mes_halluke_mad['1']))
                    Message.new_s(p, 'Halluke', 'Halluke', whats, seen=False, chachong=False)
                elif p.messages['Halluke'][-1].fro == 'Halluke':
                    Message.new(p, 'Halluke', 'Halluke', '昨晚的消息……为什么没回复？', seen=False, h='7', m=str(rd(0, 49)), chachong=False)
                else:
                    whats = []
                    for i in range(ra(p, 3, 5)):
                        whats.append(rca(p, ret_mes_halluke_mad['random']))
                    whats.append(rca(p, ret_mes_halluke_mad['1']))
                    Message.new_s(p, 'Halluke', 'Halluke', whats, seen=False, chachong=False)
            if (p.des_p == 3 or p.des_p == 4 and rra(p, 50)) and not p.onVacation:
                temp = rca(p, [ToastFood, CoffeeFood, StreetFood5, StreetFood6, StreetFood7, SaladFood, Cola, Strawberry])
                temp.add(p)
                    
                if temp == ToastFood:
                    Message.new(p, 'Destot', 'Destot', '前辈，看你不太愿意吃早餐，请你吃吐司啦，要努力工作哦！', chachong=False, pos='')
                elif temp in (CoffeeFood, StreetFood5, StreetFood6, StreetFood7):
                    Message.new(p, 'Destot', 'Destot', '前辈，我今天路过咖啡店，顺便给你带了一杯！放你桌子上了！', chachong=False, pos='')
                elif temp == SaladFood:
                    Message.new(p, 'Destot', 'Destot', '前辈，不要总吃太油腻的东西了，偶尔也来试试我最喜欢吃的沙拉吧！', chachong=False, pos='')
                elif temp == Cola:
                    Message.new(p, 'Destot', 'Destot', '前辈，来一瓶可乐不，感觉比咖啡还提神！', chachong=False, pos='')
                else:
                    Message.new(p, 'Destot', 'Destot', '前辈，猜猜看我今天看到什么了，这草莓又大又红还那么便宜，快吃啦！', chachong=False, pos='')


        if p.onVacation:
            if p.mental < 40:
                $ routine_narrator(p, _("……今天还是在床上一直躺着好了……"))
            elif p.mental > 100:
                $routine_narrator(p, _("我听到了鸟叫声……今天有点想出去散散步呢。"))
            else:
                $routine_narrator(p, _("该准备计划一下今天要做的事了。"))
            $ p.beforeSchedule()
            if p.dep_p == 1:
                jump depline_route_1
            
        else:
            if p.mental < 40:
                $ routine_narrator(p, _("头好疼啊，我今天能撑到下班吗……"))
            elif p.mental > 100:
                $routine_narrator(p, _("一天的工作开始了，调整好自己的状态吧。"))
            else:
                $routine_narrator(p, _("打完卡了，该准备计划一下今天要做的事了。"))
            $ p.beforeSchedule()
            jump morning_plot_label_office
        
    elif p.times == 5:
        python:
            if p.hal_p in (12, 13) and not persistent.noannoyhalluke:
                if not p.messages['Halluke']:
                    whats = []
                    for i in range(ra(p, 3, 5)):
                        whats.append(rca(p, ret_mes_halluke_mad['random']))
                    whats.append(rca(p, ret_mes_halluke_mad['2']))
                    Message.new_s(p, 'Halluke', 'Halluke', whats, seen=False, chachong=False)
                elif p.messages['Halluke'][-1].fro == 'Halluke':
                    Message.new(p, 'Halluke', 'Halluke', rca(p, ret_mes_halluke_mad['upset']), seen=False, chachong=False)
                else:
                    whats = []
                    for i in range(ra(p, 3, 5)):
                        whats.append(rca(p, ret_mes_halluke_mad['random']))
                    whats.append(rca(p, ret_mes_halluke_mad['2']))
                    Message.new_s(p, 'Halluke', 'Halluke', whats, seen=False, chachong=False)
            if (p.des_p == 3 or p.des_p == 4 and rra(p, 50)) and not p.onVacation:
                if p.today == 4:
                    BurgerFood.add(p)
                    Message.new(p, 'Destot', 'Destot', '前辈，今天是疯狂星期四，请你吃汉堡啦！', chachong=False, pos='')
                else:
                    temp = rca(p, [PizzaFood, BurgerFood, BreadFood, Strawberry])
                    temp.add(p)
                    
                    if temp == PizzaFood:
                        Message.new(p, 'Destot', 'Destot', '前辈，之前一直想吃一点意餐，今天吃点披萨吧，已经放在你桌子上了！', chachong=False, pos='')
                    elif temp == BurgerFood:
                        Message.new(p, 'Destot', 'Destot', '前辈，今天汉堡店有活动哦，汉堡放在你桌子上了！', chachong=False, pos='')
                    elif temp == BreadFood:
                        Message.new(p, 'Destot', 'Destot', '前辈，这个面包又便宜又好吃，还让我想起一些有趣的东西……总之放你桌子上了！', chachong=False, pos='')
                    else:
                        Message.new(p, 'Destot', 'Destot', '前辈，猜猜看我今天看到什么了，这草莓又大又红还那么便宜，快吃啦！', chachong=False, pos='')
                
                

        if p.onVacation:
            if not p.hasSchedule:
                $ p.beforeSchedule()
                $ routine_narrator(p, _("睡过头了……中午才起床也太颓废了……"))
            if p.mental < 40:
                $ routine_narrator(p, _("困死了，有种休息不够的感觉……"))
            elif p.mental > 100:
                $routine_narrator(p, _("有点饿了，中午想吃点甜的呢……"))
            else:
                $routine_narrator(p, _("午饭时间……今天吃点什么好呢……"))
            
        else:
            if p.des_p == 3 and p.today == 5:
                jump destot_route_3
            if p.mental < 40:
                $ routine_narrator(p, _("头晕……想吐……根本没什么胃口吃饭……"))
            elif p.mental > 100:
                $routine_narrator(p, _("上午的工作好像也没有很多……总之吃午饭吧。"))
            else:
                $routine_narrator(p, _("上午的工作做完了，差不多该点个外卖吃午饭了。"))

    elif p.times == 6:
        if p.onVacation:
            if p.mental < 40:
                $ routine_narrator(p, _("小睡一会……"))
            elif p.mental > 100:
                $routine_narrator(p, _("晚点应该出门逛逛……先准备一下吧……"))
            else:
                $routine_narrator(p, _("稍微刷一会手机再做下午的事情吧……"))
        else:
            if p.mental < 40:
                $ routine_narrator(p, _("希望下午没有什么破事，头已经快炸了……"))
            elif p.mental > 100:
                $routine_narrator(p, _("还有几个小时就下班了，至少现在还没有感觉很吃力……"))
            else:
                $routine_narrator(p, _("午休结束了……"))
        $p.times += 1
        jump after_operate_screen_label
    elif p.times == 9:
        if p.onOutside:
            $routine_narrator(p, _("……"))
            $ p.times+=1
            jump before_operate_screen_label

        elif p.onVacation:
            if p.mental < 40:
                if p.experience == 'wri':
                    $ routine_narrator(p, _("啊……头好疼……"))
                else:
                    $ routine_narrator(p, _("看来放假也没法让我的头疼轻一些……"))
            elif p.mental > 100:
                $routine_narrator(p, _("放假的时间总是很短暂……"))
            else:
                $routine_narrator(p, _("稍微有点累了……该找个时间躺一会……"))

            $ p.times+=1
            jump before_operate_screen_label
            
        else:
            if p.mental < 40:
                $ routine_narrator(p, _("终于结束了……希望我不会死在回家的路上……"))
            elif p.mental > 100:
                $routine_narrator(p, _("下班下班，回家爽摸鱼咯——"))
            else:
                $routine_narrator(p, _("准备下班了……"))
            $ p.times+=1
            $ p.onOutside = True
            if WeatherSmog.has(p):
                $WeatherSmog.get(p).check(p)
            jump before_operate_screen_label

            

    elif p.times == 10:
        python:
            if p.hal_p in (12, 13) and not persistent.noannoyhalluke:
                if not p.messages['Halluke']:
                    whats = []
                    for i in range(ra(p, 3, 5)):
                        whats.append(rca(p, ret_mes_halluke_mad['random']))
                    whats.append(rca(p, ret_mes_halluke_mad['3']))
                    Message.new_s(p, 'Halluke', 'Halluke', whats, seen=False, chachong=False)
                elif p.messages['Halluke'][-1].fro == 'Halluke':
                    Message.new(p, 'Halluke', 'Halluke', rca(p, ret_mes_halluke_mad['upset']), seen=False, chachong=False)
                else:
                    whats = []
                    for i in range(ra(p, 3, 5)):
                        whats.append(rca(p, ret_mes_halluke_mad['random']))
                    whats.append(rca(p, ret_mes_halluke_mad['3']))
                    Message.new_s(p, 'Halluke', 'Halluke', whats, seen=False, chachong=False)
            
            if p.aco_p == 8 and p.today == 5 and AcolasTask2 not in p.unlockedTasks:
                AcolasTask2.unlock(p)
                Message.new(p, 'Acolas', 'Acolas', '好消息！\n我刚刚出院，你似乎还没来过我家吧？来玩一玩吧？周六的下午我有空哦。\n我家就在亚斯塔禄大街的恩多尔芬小区，54栋3112，到了楼下直接说我的名字就可以，服务生会带你上来的。\n除此之外我还想问你一些其他的东西，等你来了再和你说。', h=16, m=rd(0, 59), pos='')
            if p.des_p == 2 and p.today == 5 and DestotTask1 not in p.unlockedTasks:
                DestotWork.lock(p)
                DestotTask1.unlock(p)
                Message.new(p, 'Destot', 'Destot', '前辈！太棒了！我的考核过了哦！现在公司那边已经和我签协议了，等我毕业了就可以来这里上班了！总之这周日晚上有时间吗！来和我一起出来吃点东西庆祝一下吧！', h=16, m=rd(0, 59), pos='')
            if p.des_p == 4 and p.today == 5 and DestotTask2 not in p.unlockedTasks:
                DestotTask2.unlock(p)
                Message.new(p, 'Destot', 'Destot', '前辈，周日中午有时间吗？我想请你来我家里一下，有些事情想和你说……', h=16, m=rd(0, 59), pos='')
            elif not p.des_noodles and rra(p, 20) and p.des_p in (3, 4):
                PackOfInstantNoodles.add(p)
                Message.new(p, 'Destot', 'Destot', '前辈，我从Arnel那边问到了你的地址，买的一箱泡面已经送过去了，如果晚上太饿的话就算吃点泡面也比饿着肚子睡觉强！', h=16, m=rd(0, 59), pos='')
                p.des_noodles = True
            
            

        if p.onVacation and not p.onOutside:
            if not p.hasSchedule:
                $ routine_narrator(p, _("一觉睡到晚上……真不愧是我。"))
                $ p.beforeSchedule()
            if p.mental < 40:
                $ routine_narrator(p, _("我现在只想躺在床上……"))
            elif p.mental > 100:
                $routine_narrator(p, _("或许我应该出门走一走？或者看点什么小说之类的？"))
            else:
                $routine_narrator(p, _("好了，该准备做晚上要做的事了。"))
            
        else:


            if p.mental < 40:
                $ routine_narrator(p, _("再坚持一会……马上就到家了……"))
            elif p.mental > 100:
                $ routine_narrator(p, _("啊……终于快到家了……"))
            else:
                $ routine_narrator(p, _("……"))

            
            scene black with dissolve
            $ routine_narrator(p, _("……"))

            play sound unlocking
            $ pause(0.5)
            play sound audio.button

            $ p.onOutside = False
            $ p.onVacation = True

            $ routine_bg(p)
            $ routine_music(p)

            if p.mental < 40:
                $ routine_narrator(p, _("嘶啊……头快疼死了……"))
            elif p.mental > 100:
                $ routine_narrator(p, _("回到家里总是让我心情很好……"))
            else:
                $ routine_narrator(p, _("到家了。"))
            $ routine_narrator(p, _("……总之该准备做晚上要做的事了。"))

        if p.hal_p == 11 and p.today == 6 and p.cured < 0:
            if p.experience != 'wri':
                $ routine_narrator(p, _("给Halluke发个消息，看看他怎么样了吧。"))
            else:
                $ routine_narrator(p, _("糟糕……忘记去羽毛球场了……给Halluke发个消息，看看他怎么样了吧。"))
        
        if p.experience == 'wri' and not SteamerTicket.has(p) and WriterItem2.has(p):
            if p.hal_p == 13:
                jump give_ticket_writer_h


    elif p.times >= 13:
        python:
            if p.hal_p in (12, 13) and not Message.hasNewMes(p) and not persistent.noannoyhalluke:
                hmess = len(list(filter(lambda x: x.fro == 'Halluke' and x.day == p.day, p.messages['Halluke'])))
                pmess = len(list(filter(lambda x: x.fro != 'Halluke' and x.day == p.day, p.messages['Halluke'])))
                uniquemess = len(set([x.what for x in list(filter(lambda x: x.fro != 'Halluke' and x.day == p.day, p.messages['Halluke']))]))

                if p.plan[1] == HallukeTask2:
                    p.hal_noreply = 0
                    Message.new_s(p, 'Halluke', 'Halluke', ['我一个人在家里好孤独啊……谢谢你来陪我玩……', '啊……做梦都在想的场景居然真的实现了……', '要是能和你在一起同居该有多幸福啊？'], seen=False, chachong=False)           
                elif p.plan[2] == HallukeTask1:
                    p.hal_noreply = 0
                    Message.new_s(p, 'Halluke', 'Halluke', ['今晚表现不错哦……要不是场馆晚上关门我想和你打一整宿！', '真没开玩笑！好喜欢和你一起打球啊……', '明晚你还会来的对吧？'], seen=False, chachong=False)          
                elif pmess == 0:
                    Message.new_s(p, 'Halluke', 'Halluke', ['为什么……为什么你一天都没回我消息？', '如果讨厌我的话，那我就去死吧，反正没有你喜欢，我活着也没什么意义。'], seen=False, chachong=False)
                    p.hal_p = 99
                    HallukeTask1.lock(p)
                    HallukeTask2.lock(p)
                    p.route = None
                    Achievement150.achieve()
                    if p.aco_p >= 98:
                        Achievement301.achieve()
                elif uniquemess == 1 and pmess > 1:
                    Message.new_s(p, 'Halluke', 'Halluke', ['为什么你一直用重复的话回复我？我对你来说一点也不重要对吗？','我知道了，你也就和他们一样把我当成累赘了是吧，你们都这样……就连你也这样……', '我活着还有什么意义……'], seen=False, chachong=False)
                    p.hal_p = 99
                    HallukeTask1.lock(p)
                    HallukeTask2.lock(p)
                    p.route = None
                    Achievement150.achieve()
                    if p.aco_p >= 98:
                        Achievement301.achieve()
                elif hmess >= pmess + 3:
                    if pmess-uniquemess:
                        Message.new_s(p, 'Halluke', 'Halluke', ['有那么忙吗……？我今天给你发了%s条信息，而你就回了%s条，甚至还有%s条是重复的……' % (hmess, pmess, pmess-uniquemess+1),'所以……其实你并不喜欢我……是吗？连我的消息都不怎么回……'], seen=False, chachong=False)
                    else:
                        Message.new_s(p, 'Halluke', 'Halluke', ['有那么忙吗……？我今天给你发了%s条信息，而你就回了%s条？' % (hmess, pmess),'所以……其实你并不喜欢我……是吗？连我的消息都不怎么回……'], seen=False, chachong=False)
                    p.hal_noreply += 1
                    p.hal_achievement451_able = False
                elif hmess <= pmess - 3:
                    if pmess-uniquemess:
                        Message.new_s(p, 'Halluke', 'Halluke', ['什么意思啊……我今天给你发了%s条信息，但你却只给我回了%s条，甚至还有%s条是重复的……' % (hmess, pmess, pmess-uniquemess+1), '都是些敷衍的句子……你当我看不出来么……'], seen=False, chachong=False)
                    else:
                        Message.new_s(p, 'Halluke', 'Halluke', ['什么意思啊……我今天给你发了%s条信息，但你却只给我回了%s条……' % (hmess, pmess), '都是些敷衍的句子……你当我看不出来么……'], seen=False, chachong=False)
                    
                    p.hal_noreply += 1
                    p.hal_achievement451_able = False
                elif p.plan[2] != HallukeTask1:
                    Message.new_s(p, 'Halluke', 'Halluke', ['今晚没来和我打羽毛球吗……我在体育馆等了你一晚上……', '好寂寞……我一个人……一直都是我一个人……', '但没关系，我知道你今天下午肯定是有事才没来的吧？','对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧对吧？','你明天会来的吧？','会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧会吧？'], seen=False, chachong=False)
                    p.hal_noreply += 1
                    p.hal_achievement451_able = False
                else:
                    p.hal_noreply = 0
                    whats = []
                    for i in range(ra(p, 3, 5)):
                        whats.append(rca(p, ret_mes_halluke_mad['random']))
                    whats.append(rca(p, ret_mes_halluke_mad['4']))
                    Message.new_s(p, 'Halluke', 'Halluke', whats, seen=False, chachong=False)

                
                if p.hal_noreply == 2:
                    Message.new_s(p, 'Halluke', 'Halluke', ['只是……只是希望你回个消息而已……', '看不到你的回复让我有一种像是窒息一样的感觉……好难受……','活着……好累……这样会让你想安慰我吗……'], seen=False, chachong=False)
                elif p.hal_noreply >= 3:
                    Message.new_s(p, 'Halluke', 'Halluke', ['前天是这样，昨天也是这样……今天也是……', '我好难过啊……难过得快要死了……我好痛苦……怎么办怎么办……', '对你来说我的一切是否都没有意义？'], seen=False, chachong=False)
                    p.hal_p = 99
                    p.route = None
                    HallukeTask1.lock(p)
                    HallukeTask2.lock(p)
                    Achievement150.achieve()
                    if p.aco_p >= 98:
                        Achievement301.achieve()
                    
                    
                

        if p.mental < 40:
            $ routine_narrator(p, _("床……头疼药……安眠药……我真的能够活过今晚吗……"))
        elif p.mental > 100:
            $routine_narrator(p, _("像现在这样头不是很痛就很好……如果我的病被治好了，我会不会更开心呢？"))
        else:
            $routine_narrator(p, _("一天又快结束了，早点休息吧。")) 
    

    jump operate_screen_label

label before_go_office:
    $temp = ra(p, 1, 100) if p.week >1 else -1
    if p.cured != -1:
        pass
    elif temp in (1, 2, 3):
        scene morningrun with fade
        if not Injured.has(p):
            $Injured.add(p)
            play sound audio.bone
            "啊！……扭到脚了……好痛啊……"
            "希望今天不会再有坏运气的事情发生了……"
        else:
            $rec = r2(30 * f())
            $Notice.add(_('降低了%s点精神状态。') % rec)
            "本就受伤了还要来上班，我为什么不请个假呢……"
            "腿真的痛死了。"

    elif temp in (4, 5, 6, 7):
        scene morningrun with fade
        "刷新闻的时候看到了行业相关的职业现状，很多年轻人都找不到工作……"
        $MentProb.add(p)
        "如果我没有那么努力，会不会被烧鱿鱼呢……"

    elif temp in (8,9,10,11):
        scene morningrun with fade
        "路边的桃花都开了，闻起来好香啊……"
        if PhysProb.has(p):
            $PhysProb.subByType(p)
            "太阳也很暖和……感觉也没那么累了……"
        else:
            $MentRezB.add(p)
            "等赚到足够钱了就出去旅游吧，去一个有很多花的地方。"

    elif 12 <= temp < 25:
        $rl = list(p.visitedStore)
        if 5 in rl:
            $rl.extend([5]*len(rl))
        $temp = rca(p, rl)
        if temp == 2:
            scene store with fade
            "路过了零食店，要去看看么？"
            menu:
                "路过了零食店，要去看看么？"
                "进去看看":
                    $temp = p.money
                    call screen screen_explore_store(p)
                    if p.money==temp:
                        "没啥东西，走了。"
                    else:
                        "收获满满……"
                "还是赶紧上班吧":
                    pass
            
                
            
        elif temp == 3:
            scene foodstand with dissolve
            "路过了一个小吃摊，买点么？"
            menu:
                "路过了零食店，要去看看么？"
                "进去看看":
                    $temp = p.money
                    call screen screen_explore_buystreetfood(p)
                    if p.money==temp:
                        "没啥想吃的，还是算了。"
                    else:
                        "买了好多东西……回去再吃吧。"
                "还是赶紧上班吧":
                    pass
        elif temp == 4:
            scene giftshop with fade
            menu:
                "路过一家礼品店，要看看么？"
                "进去看看":
                    $temp = p.money
                    call screen screen_explore_buystreetgift(p)
                    if p.money==temp:
                        "没好东西，不买了。"
                    else:
                        "这个东西还挺好的……回去放在我桌子上……"
                "还是赶紧上班吧":
                    pass
        elif temp == 5:
            scene cafe with fade
            menu:
                "路过一家咖啡店，要看看么？"
                "进去看看":
                    "我没有理由拒绝。"
                    $temp = p.money
                    call screen screen_explore_buycoffee(p)
                    if p.money==temp:
                        "算了，都太贵了。"
                    else:
                        "今晚加班的时候喝……"
                "还是赶紧上班吧":
                    pass
        elif temp == 6:
            scene flowershop with fade
            menu:
                "路过一家花店，要看看么？"
                "进去看看":
                    $temp = p.money
                    call screen screen_explore_buystreetflower(p)
                    if p.money==temp:
                        "没好东西，不买了。"
                    else:
                        "这朵花好看……回去放在我桌子上的花瓶里养着……"
                "还是赶紧上班吧":
                    pass
        elif temp == 7:
            scene store with fade
            menu:
                "路过一家工具店，要看看么？"
                "进去看看":
                    $temp = p.money
                    call screen screen_explore_store2(p)
                    if p.money==temp:
                        "没啥东西，走了。"
                    else:
                        "收获满满……"
                "还是赶紧上班吧":
                    pass
        elif temp == 8:
            scene store with fade
            menu:
                "路过一家文体用品店，要看看么？"
                "进去看看":
                    $temp = p.money
                    call screen screen_explore_store3(p)
                    if p.money==temp:
                        "没啥东西，走了。"
                    else:
                        "收获满满……"
                "还是赶紧上班吧":
                    pass


    $ p.onOutside = False
    $ p.onVacation = False
    if WeatherSmog.has(p):
        $WeatherSmog.get(p).check(p)

    $ p.times += 1

    $ beforemusic=renpy.music.get_playing()

    jump before_operate_screen_label


label morning_plot_label_office:
    if p.cured != -1:
        jump operate_screen_label
    if p.dep_p == 1:
        jump depline_route_1
    if p.today == 1 and not SteamerTicket.has(p):
        if p.hal_p == 13:
            jump give_ticket_h
        elif p.aco_p == 12:
            jump give_ticket_a
        elif p.week == 4 and p.des_p == 1:
            jump destot_route_1

    if p.today not in (6,7) and p.des_p == 5:
        jump destot_route_5
    if p.week == 3 and (p.today == 5 or p.today == rra(p, 50)) and p.des_p == 0:
        jump destot_route_0
  
            



        #'''
        #elif temp == 4:
        #    "今天的太阳好舒服啊……"
        #    "如果我没有那么努力，会不会被烧鱿鱼呢……"
        #    jump operate_screen_label
        #
        #elif temp == 5:
        #    "刷新闻的时候看到了行业相关的职业现状，很多年轻人都找不到工作……"
        #    $MentProb.add(p)
        #    "如果我没有那么努力，会不会被烧鱿鱼呢……"
        #    jump operate_screen_label
        #'''
    jump operate_screen_label

label operate_screen_label:
    if not replaying and not calling:  #  防止打电话或者回顾剧情回来之后npc快速回复信息
        $ Message.allret(p)
        $ p.checkTask()

    if replaying:
        $replaying = False
        $phone_defaulted = True
        #$phone_cached_app = 'video'
        $phone_page = 4
        $routine_music(p)
        show screen screen_phone(p)
    
    if calling:
        $calling = False
        $phone_defaulted = True
        #$phone_cached_app = 'call'
        $phone_page = 11
        $routine_music(p)
        show screen screen_phone(p)

    show screen screen_objects(p)
    call screen screen_operate(p)
    hide screen info
    hide screen info2
    hide screen info3

    if p.times in (3, 7, 11, 14):
        jump after_operate_screen_label
    else:
        jump before_operate_screen_label

label after_operate_screen_label:
    if p.hal_p == 11 and p.today == 6 and p.times == 11 and p.cured < 0:
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
        $p.onOutside = True
        jump halluke_route_11

    jump executing_task_label


label executing_task_label:
    $ p.stime()
    
    if p.times == 14:
        jump before_sleep
    $donextplan(p)

label after_executing_task_label:
    if p.times >= 14:
        if HotelBuff.has(p):
            scene location_hotel at setcolor with dissolve
        else:
            scene bedroom at setcolor with dissolve
        "好困……得尽快睡觉了。"
        jump dayEnd
    if p.cured<0:
        $tt = p.get_task_time()
        if tt == 2:
            if p.plan[0] != p.plan[1]:
                $ Inspiration.add(p)

        elif tt == -1:
            if p.plan[1] != p.plan[2] and p.plan[2] != WriteDownInspiration:
                $ Inspiration.add(p)
        
        $p.levi_hunger = max(0, p.levi_hunger-ra(p, 5, 20))
        $p.levi_joy = max(0, p.levi_joy-ra(p, 5, 20))

        if p.onVacation:
            if rra(p, 60):
                $ MentRezB.add(p)
        $nextweather = p.newMorningWeather(True)
        if WeatherThunder.has(p) or WeatherRainy.has(p):
            $nextweather = WeatherThunderRain
        if (GameDifficulty4.has(p) or GameDifficulty5.has(p)) and not nextweather.has(p) and rra(p, 10):
            $Notice.add('天气似乎逐渐从%s变化为%s了……' % (p.effects[0].name, nextweather.name))
            $nextweather.add(p)
    
    jump before_operate_screen_label




label before_sleep:  # 触发部分剧情
    if p.cured < 0 and SteamerTicket.has(p) and p.today == 1 and not persistent.nocharacterplot:
        jump prepare_for_surgery_1

    elif p.cured < 0 and p.week == 15 and p.today == 1 and not persistent.nocharacterplot:
        jump prepare_for_surgery_2

    elif p.cured == 6:
        jump curedroute_phone_1

    elif p.cured == 13:
        jump curedroute_phone_2

    elif p.cured == 20:
        jump curedroute_phone_3

    elif p.cured == 27:
        jump curedroute_phone_4

    else:
        jump before_dayend




label before_dayend:
    if HotelBuff.has(p):
        scene location_hotel at setcolor with dissolve
    else:
        scene bedroom at setcolor with dissolve
    stop music fadeout 5
    $renpy.show('blurred', at_list=[blurr_concentration(p)])
    if not p.cured<21:
        "……"
        jump dayEnd
    

    if not p.s8 and p.week >= 2 and p.cured==-1 and p.finalStageDays==-1 and not True in [x.kind == '食物' for x in p.itemcd]:
        jump solitus_route_8
    
    
    if GameDifficulty4.has(p) or GameDifficulty5.has(p):
        jump before_sleep_task


    "该睡觉了。"
    jump dayEnd

label before_sleep_task:
    "睡觉之前还有一点时间，做点什么好呢……"
    $before_sleep_extratask = None
    menu:
        "放松一下":
            $before_sleep_extratask = 'phys'  # 恢复精神状态5~15 如果有过劳 50%概率消除1层过劳 30%概率降低1点严重 20%概率获得1层体魄
        "整理思绪":
            $before_sleep_extratask = 'ment'  # 恢复精神状态5~10 如果有焦虑 50%概率消除1层焦虑 30%概率降低1点严重 20%概率使灵感的持续时间+1
        "熬夜":
            $before_sleep_extratask = 'task'  # 进行一个在家才能做的日程 暂时获得20%的严重度和40%精神状态消耗提升，60%的精神状态恢复降低 提升2点严重 
            $Notice.show()
        "阅读书籍" if p.canRead >= 0 and list(filter(lambda x: x.kind in ('书籍', '专业类书籍') and type(x) not in p.itemcd, p.items)) != []:
            $before_sleep_extratask = 'read'  # 阅读一半书籍 33%提升1点严重 33%无变化 33%降低1点严重
        "打手冲" if Erection.has(p):
            $before_sleep_extratask = 'mast'  # 恢复精神状态10~25 降低1点严重 移除勃起
    if before_sleep_extratask == 'task':
        $Stayuplate.add(p)
        if p.plan[3].checkAvailable(p, p.today, 3) != True:
            $p.plan[3] = NoTask
        call screen screen_tasks_extra(p)
        $donextplan(p)
    else:
        if before_sleep_extratask == 'read':
            $renpy.call_screen(_screen_name="screen_tr_readingbook", player=p, nums=1)
            
        call Task_processing from _call_Task_processing_42
        python:
            p.stime(ra(p, 22, 23), ra(p, 30, 59))
            if before_sleep_extratask == 'phys':
                reco = r2(ra(p, 5, 15) * Task().getRecoScale(p))
                p.gain_mental(reco)
                if rra(p, 50) and PhysProb.has(p):
                    PhysProb.clearByType(p)
                    Notice.add(_('移除了1层过劳！'))
                elif rra(p, 40):
                    Physique.add(p)
                    Notice.add(_('获得了1层体魄！'))
                else:
                    p.gain_abi(-0.01, 'sev')
            elif before_sleep_extratask == 'ment':
                reco = r2(ra(p, 5, 10) * Task().getRecoScale(p))
                p.gain_mental(reco)
                if rra(p, 50) and MentProb.has(p):
                    MentProb.clearByType(p)
                    Notice.add(_('移除了1层焦虑！'))
                elif rra(p, 40) and Inspiration.has(p):
                    Inspiration.get(p).duration += 1
                    Notice.add(_('灵感的持续时间提升了1天！'))
                else:
                    p.gain_abi(-0.01, 'sev')
            elif before_sleep_extratask == 'mast':
                reco = r2(ra(p, 5, 10) * Task().getRecoScale(p))
                p.gain_mental(reco)
                p.gain_abi(-0.01, 'sev')
                Erection.clearByType(p)
                
            else:
                
                for book, allo in p.retval:
                    book.readBook(p, allo)
                    
    $Notice.show()
    if HotelBuff.has(p):
        scene location_hotel at setcolor with dissolve
    else:
        scene bedroom at setcolor with dissolve
    if before_sleep_extratask == 'mast':
        "……呼……"
    "好困……得尽快睡觉了。"
    jump dayEnd



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

    if GameDifficulty1.has(p):
        scene black with dissolve
        $clearscreens()
        call screen gd1_jumpday(p)
        $ p.mental = 100
    else:
        $ p.newDay()
    $ Saver.save(p)
    $ Notice.add(_('存档已保存！'))
    call loading from _call_loading_1
    $ Notice.show()
    if p.hal_p == 15 or p.aco_p == 14 and p.cured < 0:
        if p.experience == 'wri':
            jump writer_before_earthquake
        jump before_earthquake
    jump wakeup


screen screen_useMed(player):

    if MedicineA.has(player):
        imagebutton idle 'gui/object/mshadow.png':
            at med_bottle_shadow

            xcenter 0.22
            ycenter 0.55
            focus_mask None
        
        imagebutton idle 'gui/object/ma.png':
            at med_bottle

            if persistent.actionquickly:
                action Hide("info"),Function(quickUse, item=MedicineA, player=player)
            else:
                action [Show(screen="info_confirm",text=_('使用'),act=[Function(quickUse, item=MedicineA, player=player), Hide("info"), Return()],i=MedicineA.getinfo(player) + '\n点击使用。',width=600, a=MedicineA.ad, pp=renpy.get_mouse_pos()), Hide("info")]
            hovered Show(screen="info",i=MedicineA.getinfo(player) + '\n点击使用。',width=600, a=MedicineA.ad)
            unhovered Hide("info")
            #text_style "meda_text"
            #xalign 1.0
            hover_sound audio.itemmed
            activate_sound audio.itemmed
            xcenter 0.22
            ycenter 0.55
            focus_mask None
    
    if MedicineB.has(player):
        imagebutton idle 'gui/object/mshadow.png':
            at med_bottle_shadow

            xcenter 0.28
            ycenter 0.55
            focus_mask None

        imagebutton idle 'gui/object/mb.png':
            at med_bottle
            
            if persistent.actionquickly:
                action Hide("info"),Function(quickUse, item=MedicineB, player=player)
            else:
                action [Show(screen="info_confirm",text=_('使用'),act=[Function(quickUse, item=MedicineB, player=player), Hide("info"), Return()],i=MedicineB.getinfo(player) + '\n点击使用。',width=600, a=MedicineB.ad, pp=renpy.get_mouse_pos()), Hide("info")]
            hovered Show(screen="info",i=MedicineB.getinfo(player) + '\n点击使用。',width=600, a=MedicineB.ad)
            unhovered Hide("info")
            #text_style "meda_text"
            #xalign 1.0
            hover_sound audio.itemmed
            activate_sound audio.itemmed
            xcenter 0.28
            ycenter 0.55
            focus_mask None

    if MedicineC.has(player):

        imagebutton idle 'gui/object/mshadow.png':
            at med_bottle_shadow

            xcenter 0.34
            ycenter 0.55
            focus_mask None

        imagebutton idle 'gui/object/mc.png':
            at med_bottle

            if persistent.actionquickly:
                action Hide("info"),Function(quickUse, item=MedicineC, player=player)
            else:
                action [Show(screen="info_confirm",text=_('使用'),act=[Function(quickUse, item=MedicineC, player=player), Hide("info"), Return()],i=MedicineC.getinfo(player) + '\n点击使用。',width=600, a=MedicineC.ad, pp=renpy.get_mouse_pos()), Hide("info")]
            hovered Show(screen="info",i=MedicineC.getinfo(player) + '\n点击使用。',width=600, a=MedicineC.ad)
            unhovered Hide("info")
            #text_style "meda_text"
            #xalign 1.0
            hover_sound audio.itemmed
            activate_sound audio.itemmed
            xcenter 0.34
            ycenter 0.55
            focus_mask None
    
    if MedicineD.has(player):
        
        imagebutton idle 'gui/object/mshadow.png':
            at med_bottle_shadow

            xcenter 0.7
            ycenter 0.55
            focus_mask None

        imagebutton idle 'gui/object/md.png':
            at med_bottle
            
            if persistent.actionquickly:
                action Hide("info"),Function(quickUse, item=MedicineD, player=player)
            else:
                action [Show(screen="info_confirm",text=_('使用'),act=[Function(quickUse, item=MedicineD, player=player), Hide("info"), Return()],i=MedicineD.getinfo(player) + '\n点击使用。',width=401, a=MedicineD.ad, pp=renpy.get_mouse_pos()), Hide("info")]
            hovered Show(screen="info",i=MedicineD.getinfo(player) + '\n点击使用。',width=401, a=MedicineD.ad)
            unhovered Hide("info")
            #text_style "meda_text"
            #xalign 1.0
            hover_sound audio.itemmed
            activate_sound audio.itemmed
            xcenter 0.7
            ycenter 0.55
            focus_mask None
    
    
    imagebutton auto "gui/menu/home_%s.png":
        at trans_toLeft()
        action Hide("info"), Return()
        unhovered Hide("info")
        hovered Show(screen="info", i=_('不吃药。'), a=_('……'), width=100)
        activate_sound audio.cursor
        xpos 0.9
        ypos 0.85



label curedRoutine:
    show screen screen_dashboard(p)
    $ routine_music(p)
    $ p.times = curedsettime(p.times)
    if p.cured >= 105:
        jump ce
    if p.times == 3:
        $ p.beforeSchedule()

        $ p.physical = p.physical - p.physical*0.05
        $ p.writing = p.writing - p.writing*0.05
        $ p.popularity = max(1000, p.writing - p.popularity*0.05)
        
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




screen gd1_jumpday(player):
    default day = 1
    python:
        def getp(p, day):
            for i in range(day):
                p.dateChange()
            return p

        def setp(p, day):
            p.newDay(day)

        pp = dcp(player)
    
    
    $pp = getp(pp, day)
    textbutton "时间快进":
        text_style "white" 
        text_size 60 
        xoffset 30
        yoffset 30
        at screen_init_select_label()

    
    frame:
        yfill True
        xfill True
        xcenter 0.5
        ycenter 0.4
        hbox:
            xalign 0.5
            frame:
                yfill True
                xsize 600
                background None
                $weekday = weekdayFormat(player.today)
                vbox:
                    xalign 0.5
                    yalign 0.5
                    text "[player.mon]月[player.day]日" size 150 xalign 0.08 yalign 0.15 style "phone"
                    text "第[player.week]周 [weekday]" size 60 xpos 0.95 yalign 0.185 xanchor 1.0 style "phone"

            null width 150

            add 'gui/gd1/to.png' yalign 0.5

            null width 150

            frame:
                yfill True
                xsize 600
                background None
                $weekday = weekdayFormat(pp.today)
                vbox:
                    xalign 0.5
                    yalign 0.5
                    text "[pp.mon]月[pp.day]日" size 150 xalign 0.08 yalign 0.15 style "phone"
                    text "第[pp.week]周 [weekday]" size 60 xpos 0.95 yalign 0.185 xanchor 1.0 style "phone"
        
        hbox:
            xalign 0.5
            yalign 0.9
            spacing 300
            
            imagebutton idle 'gui/gd1/minus.png':
                
                if day > 1:
                    action SetLocalVariable("day", day-1)
                else:
                    action SetLocalVariable("day", 7)
                activate_sound audio.cursor
                at app_transform

            imagebutton idle 'gui/gd1/ok.png':
                action Function(setp, player, day), Return()
                at app_transform

            imagebutton idle 'gui/gd1/plus.png':
                
                if day < 7:
                    action SetLocalVariable("day", day+1)
                else:
                    action SetLocalVariable("day", 1)
                activate_sound audio.cursor
                at app_transform


            

