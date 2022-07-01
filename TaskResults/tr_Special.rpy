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
    stop music fadeout 5
    $p.times+=1
    scene livingroom with fade
    "回家了……"
    jump TaskExecuting
    #jump GoOutside_beginning


label HallukeTask1_beginning:
    scene court with fade
    "我把随身携带的东西放到窗台边。"
    "Halluke已经提前占据了一个球网的位置，此时他正拎着球拍盯着我。"
    "呼，没想到真的能在上课之外的时间见到他……总之，先陪他练习吧。"
    call Task_processing from _call_Task_processing_26
    $p.times+=1
    stop music fadeout 3
    $HallukeTask1.executeTask(p)

label HallukeTask1_result:
    scene court with fade
    $Notice.show()
    jump halluke_plot_judge_2


label HallukeTask2_beginning:
    $HallukeTask1.executeTask(p)

label HallukeTask2_result:
    $Notice.show()
    jump halluke_route_11