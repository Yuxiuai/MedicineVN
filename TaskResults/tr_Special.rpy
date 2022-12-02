label GoOutside_beginning:
    scene livingroom with fade
    play music audio.sliceoflife fadein 5
    "去哪玩呢？"
    $p.times+=1
    call screen screen_explore_map(p)

label GoOutside_result:
    $p.updateAfterTask(GoOutside)
    if rra(p, 50):
        $Novelty.add(p)
    if rra(p, 25):
        $PhysRezB.add(p)
    if rra(p, 25):
        $Relaxation.add(p)
    stop music fadeout 5
    $p.times+=1
    scene livingroom with fade
    "回家了……"
    $Notice.show()
    jump TaskExecuting
    #jump GoOutside_beginning

label TestTask_beginning:
    $p.times += 2
    $p.updateAfterTask(TestTask)
    jump TaskExecuting


label HallukeTask1_beginning:
    scene court with fade
    "我把随身携带的东西放到窗台边。"
    "Halluke已经提前占据了一个球网的位置，此时他正像往常那样拎着球拍盯着我。"
    "准备一下就开始练习吧。"
    call Task_processing from _call_Task_processing_26
    $p.times+=1
    stop music fadeout 3
    $HallukeTask1.executeTask(p)

label HallukeTask1_result:
    scene court with fade
    $Notice.show()
    jump halluke_plot_judge_2


label HallukeTask2_beginning:
    $p.times+=1
    $HallukeTask2.executeTask(p)

label HallukeTask2_result:
    $Notice.show()
    jump halluke_route_12


label AcolasTask1_beginning:
    scene workarea with fade
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
        "我一定不能再让他失望了，我要尽全力才行。"
    call Task_processing from _call_Task_processing_33
    $p.times+=1
    stop music fadeout 3
    $AcolasTask1.executeTask(p)

label AcolasTask1_result:
    scene workarea with fade
    $Notice.show()
    "头极度地疼。"
    "就到这里吧，我真的没法再进行下去了。"
    $p.times+=1
    jump TaskExecuting

label AcolasTask2_beginning:
    $p.times+=1
    $AcolasTask2.executeTask(p)

label AcolasTask2_result:
    $Notice.show()
    jump acolas_route_8