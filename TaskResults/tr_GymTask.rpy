label gym_injured:
    "啊啊啊啊……"
    "居然受伤了……"
    "不是一般的痛，开始流血了……"
    "还是尽快回家去休息好了……"
    $p.times+=1
    jump TaskExecuting


label GymSport_beginning:
    if Injured.has(p):
        scene bedroom with fade
        "受伤了……还是不去健身房好了……"
        $p.times+=2
        jump TaskExecuting
    else:
        scene gymsport with fade
        "嗯……绝对不是为了看那些壮男的肌肉才下决定来这里的。"
        "我将灌满水的运动水壶放在窗边。"
        "那么，开始准备制定健身计划吧。"
        call screen screen_gymtasks(p)
        "……"
        "计划完毕。"
        call Task_processing from _call_Task_processing_3
        $p.times+=1
        $GymTask.executeTask(p)


label gym_result:
    $temp = rd(1,3)
    if temp == 1:
        jump GymSport_result_exce
    elif temp == 2:
        jump GymSport_result_good
    elif temp == 3:
        jump GymSport_result_norm

label GymSport_result_exce:
    scene gymsport with fade
    $Notify.show()
    "虽然来的次数不多，但身体很快就适应了这种氛围，是好事啊。"
    "这可比平时随便跑跑锻炼的质量好太多了，以后也经常来好了。"
    $p.times+=1
    jump TaskExecuting

label GymSport_result_good:
    scene gymsport with fade
    $Notify.show()
    "要问我买健身卡是为了什么呢！"
    "肯定不是单纯想健身，当然是为了看满身肌肉的帅哥的啊——"
    "虽然很辛苦啦……从来没有这样强度的身体锻炼，不过看着帅哥心里总会好受一些……"
    $p.times+=1
    jump TaskExecuting

label GymSport_result_norm:
    scene gymsport with fade
    $Notify.show()
    "举哑铃真的好累，手都要断了……"
    "而且从家里到这边要坐好久的车，要不是贪那几块办卡便宜的钱我就去家门口那家了，然后还要听教练的限制食物摄取……"
    "唉，钱都花了，不是抱怨的时候，继续练习吧。"
    $p.times+=1
    jump TaskExecuting
