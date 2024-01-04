label GoOutside_beginning:
    play music audio.sliceoflife fadein 5
    if HotelBuff.has(p):
        scene location_hotel with fade
        "虽然我还是很想在这里一直躺着，但还是出去一下好了……"
    elif CafeBuff.has(p):
        scene location_cafe with fade
        "该离开这里了。"
        $CafeBuff.clearByType(p)
    elif BookstoreBuff.has(p):
        scene location_bookstore with fade 
        "该离开这里了。"
        $BookstoreBuff.clearByType(p)
    else:
        scene livingroom with fade
    
    "去哪里呢？"
    $ p.onOutside = True
    $p.times+=1
    call screen screen_map(p, True)

label GoOutside_result:
    if not Tired.has(p) and (GameDifficulty4.has(p) or GameDifficulty5.has(p)):
        
        menu:
            "是否继续前往另一个地点？"
            "是":
                $Tired.add(p)
                call screen screen_map(p, True)
            "放弃":
                pass
            
    $p.updateAfterTask(GoOutside)
    if rra(p, 50):
        $Novelty.add(p)
    if rra(p, 25):
        $PhysRezB.add(p)
    if rra(p, 33):
        $Relaxation.add(p)
    stop music fadeout 5
    
    if p.times==4:
        scene morningrun with fade
    elif p.times==8:
        scene afternoonrun with fade
    else:
        scene nightrun with fade
    "回去的路上……"
    $p.times+=1
    $ p.onOutside = False
    if WeatherSmog.has(p):
        $WeatherSmog.get(p).check(p)
    $Notice.show()
    jump after_executing_task_label
    #jump GoOutside_beginning












label TestTask_beginning:
    $p.times += 2
    $p.updateAfterTask(TestTask)
    jump after_executing_task_label


label HallukeTask1_beginning:
    $ p.onOutside = True
    scene court with fade
    "我把随身携带的东西放到窗台边。"
    "Halluke已经提前占据了一个球网的位置，此时他正像往常那样拎着球拍盯着我。"
    "准备一下就开始练习吧。"
    call Task_processing from _call_Task_processing_22
    
    $p.times+=1
    stop music fadeout 3
    $HallukeTask1.executeTask(p)

label HallukeTask1_result:
    scene court with fade
    $Notice.show()
    jump halluke_plot_judge_2


label HallukeTask2_beginning:
    $ p.onOutside = True
    $p.times+=1
    $HallukeTask2.executeTask(p)

label HallukeTask2_result:
    $Notice.show()
    jump halluke_route_12


label AcolasTask1_beginning:
    scene workarea at setcolor with fade
    if AcolasItem2.has(p):
        "我已经答应他要帮他做游戏了，而且他也帮我解决了不少的工作……"
        "那么现在就稍微花点时间了解一下该从哪里开始写吧……"
    elif AcolasItem3.has(p):
        if rd(0, 1) == 1:
            "深呼吸，你不是很会写东西吗？就算程序上没他厉害，至少你在剧情设计写作方面更强吧？"
            "但我为什么如此紧张呢……是仍然怕没完成他的请求从而焦虑？还是害怕自己被他抛弃？"
            "灵感……灵感……快想啊……"
        else:
            "我一定不能再让他失望了，我要尽全力才行。"
    elif AcolasItem4.has(p):
        "我不能让他失望我不能让他失望我不能让他失望我不能让他失望我不能让他失望我不能让他失望我不能让他失望我不能让他失望我不能让他失望我不能让他失望我不能让他失望我不能让他失望我不能让他失望我不能让他失望"
    call Task_processing from _call_Task_processing_23
    
    $p.times+=1
    stop music fadeout 3
    $AcolasTask1.executeTask(p)

label AcolasTask1_loop:
    scene workarea at setcolor with fade
    $Notice.show()
    menu:
        "继续做吗？"
        "继续":
            if int(p.st()[0]) == 6:
                "不……我不能再继续了……我需要睡眠……"
                jump AcolasTask1_result
            else:
                pass

        "停下":
            jump AcolasTask1_result

    if rd(0, 1) == 1:
        "深呼吸，你不是很会写东西吗？就算程序上没他厉害，至少你在剧情设计写作方面更强吧？"
        "但我为什么如此紧张呢……是仍然怕没完成他的请求从而焦虑？还是害怕自己被他抛弃？"
        "灵感……灵感……快想啊……"
    else:
        "我一定不能再让他失望了，我要尽全力才行。"
    call Task_processing from _call_Task_processing_24
    
    $p.stime(int(p.st()[0])+1, rd(1, 60))
    if int(p.st()[0])+1 > 23:
        $p.dateChange()
        $p.times = 12
        $p.stime(1, rd(1, 60))
        $p.staylate = True
    stop music fadeout 3
    $AcolasTask1.executeTask(p)


label AcolasTask2_loop:
    scene workarea at setcolor with fade
    $Notice.show()
    menu:
        "继续做吗？"
        "继续":
            pass
        "停下":
            menu:
                "继续做吗？{fast}"
                "继续":
                    pass
                "继续":
                    pass

    "我不能让他失望。"
    call Task_processing from _call_Task_processing_25
    
    $p.stime(int(p.st()[0])+1, rd(1, 60))
    if int(p.st()[0])+1 > 23:
        $p.dateChange()
        $p.times = 12
        $p.stime(1, rd(1, 60))
        $p.staylate = True
    stop music fadeout 3
    $AcolasTask1.executeTask(p)

label AcolasTask1_end:
    scene workarea with fade
    $Notice.show()
    "稍微熬下夜也不是不能做完……"
    "这样就不会让他失望了吧。"
    $p.times+=1
    if 5 <= int(p.st()[0]) < 15:
        "已经天亮了么……"
    jump after_executing_task_label

label AcolasTask1_result:
    scene workarea with fade
    $Notice.show()
    "头极度地疼。"
    "就到这里吧，我真的没法再进行下去了。"
    $p.times+=1
    jump after_executing_task_label

label AcolasTask2_beginning:
    $p.times+=1
    $AcolasTask2.executeTask(p)

label AcolasTask2_result:
    $Notice.show()
    jump acolas_route_8

label DestotTask1_beginning:
    $p.times+=1
    $DestotTask1.executeTask(p)

label DestotTask1_result:
    $Notice.show()
    jump destot_route_2

label DestotTask2_beginning:
    $p.times+=1
    $DestotTask2.executeTask(p)

label DestotTask2_result:
    $Notice.show()
    jump destot_route_4

label DeplineTask1_beginning:
    $p.times+=1
    $DeplineTask1.executeTask(p)
    $p.onOutside = True
    jump depline_route_2