label gym_injured:
    "啊啊啊啊……"
    "居然受伤了……"
    "不是一般的痛，开始流血了……"
    "还是尽快回家去休息好了……"
    $p.times+=1
    $ p.onOutside = False
    jump after_executing_task_label

label gym_nomoney:
    scene livingroom with fade
    "嗯……？"
    "手里的钱好像不太够的样子……"
    "我记得安排日程的时候明明有足够的钱……"
    "可能是买了什么小吃忘记了吧……"
    $p.times+=2
    $ p.onOutside = False
    jump after_executing_task_label

label GymSport_beginning:
    $ p.onOutside = True
    if Injured.has(p):
        scene bedroom with fade
        "受伤了……还是不去健身房好了……"
        $p.times+=2
        $ p.onOutside = False
        jump after_executing_task_label
    elif p.money < r2(0.4*p.price) and not GymTicket.has(p):
        jump gym_nomoney
    else:
        scene gymsport with fade
        "嗯……绝对不是为了看那些壮男的肌肉才下决定来这里的。"
        "我将灌满水的运动水壶放在窗边。"
        "那么，开始准备制定健身计划吧。"
        call screen screen_gymtasks(p)
        "……"
        "计划完毕。"
        $p.times+=1
        $GymTask.executeTask(p)


label gym_result:
    $GymSport.executeTask(p)
    $Notice.show()
    $temp = rd(1,3)
    if temp == 1:
        jump GymSport_result_exce
    elif temp == 2:
        jump GymSport_result_good
    elif temp == 3:
        jump GymSport_result_norm

label GymSport_result_exce:
    scene gymsport with fade
    "虽然来的次数不多，但身体很快就适应了这种氛围，是好事啊。"
    "这可比平时随便跑跑锻炼的质量好太多了，以后也经常来好了。"
    $p.times+=1
    $ p.onOutside = False
    jump after_executing_task_label

label GymSport_result_good:
    scene gymsport with fade
    "要问我买健身卡是为了什么呢！"
    "肯定不是单纯想健身，当然是为了看满身肌肉的帅哥的啊——"
    "虽然很辛苦啦……从来没有这样强度的身体锻炼，不过看着帅哥心里总会好受一些……"
    $p.times+=1
    $ p.onOutside = False
    jump after_executing_task_label

label GymSport_result_norm:
    scene gymsport with fade
    "举哑铃真的好累，手都要断了……"
    "而且从家里到这边要坐好久的车，要不是贪那几块办卡便宜的钱我就去家门口那家了，然后还要听教练的限制去控制食谱……"
    "唉，钱都花了，不是抱怨的时候，至少我已经流下了足够的汗水。"
    $p.times+=1
    $ p.onOutside = False
    jump after_executing_task_label
