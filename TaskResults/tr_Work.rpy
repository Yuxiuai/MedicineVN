label DefaultWork_beginning:
    scene office with fade
    if p.times<5:
        "开始进行今天的工作吧。"
        "我深呼吸，按压自己工位桌上电脑的电源键。"
    else:
        "午餐时间过得好快……"
        "继续下午的工作……"
        "我揉了下疲惫的眼睛，将睡眠中的电脑打开。"
    call Task_processing from _call_Task_processing_11
    $p.times+=1
    $DefaultWork.executeTask(p)

label DefaultWork_result_exce:
    scene office with fade
    $Notice.show()
    "好像一不小心解决了当前项目之前程序员埋下的隐患！"
    "这周的会议我肯定要被表扬了。"
    "嘿嘿，这就是得意的感觉吗！"
    $p.times+=1
    jump TaskExecuting

label DefaultWork_result_good:
    scene office with fade
    $Notice.show()
    "虽然今天工作很繁重，不过也算是按时完成了。"
    "不愧是我。"
    $p.times+=1
    jump TaskExecuting

label DefaultWork_result_norm:
    scene office with fade
    $Notice.show()
    "今天的代码写得很顺手，完成任务后还有时间摸会鱼。"
    "考虑考虑把之前没补完的番看一看好了。"
    $p.times+=1
    jump TaskExecuting

label DefaultWork_result_bad:
    scene office with fade
    $Notice.show()
    "……似乎平稳地混过去了，今天似乎没什么比较难的工作的样子。"
    "要是每天都这么轻松就好了……"
    $p.times+=1
    jump TaskExecuting


label LoafingWork_beginning:
    scene office with fade
    if p.times<5:
        "头有点痛得厉害，还是先不要那么努力工作好了。"
        "还是先弄一些工作之外的事好了……"
    else:
        "吃完午饭之后就好困哦，不想上班……"
        "做点什么好呢？"
    menu:
        "趴在桌子上休息":
            $p.retval = 'sleep'
        "做些搬东西的杂活" if p.canSport >= 0:
            $p.retval = 'phy'
        "看会网络小说" if p.canRead >= 0:
            $p.retval = 'wri'
        "阅读携带的书籍" if p.canRead >= 0 and list(filter(lambda x: type(x).kind == '书本' and type(x).__name__ not in p.itemcd, p.items)) != []:
            $p.retval = 'read'
    $p.times+=1
    $LoafingWork.executeTask(p)

label LoafingWork_result_exce:
    scene office with fade
    $Notice.show()
    "好像一不小心解决了当前项目之前程序员埋下的隐患！"
    "这周的会议我肯定要被表扬了。"
    "嘿嘿，这就是得意的感觉吗！"
    $p.times+=1
    jump TaskExecuting

label LoafingWork_result_good:
    scene office with fade
    $Notice.show()
    "虽然今天工作很繁重，不过也算是按时完成了。"
    "不愧是我。"
    $p.times+=1
    jump TaskExecuting

label LoafingWork_result_norm:
    scene office with fade
    $Notice.show()
    "今天的代码写得很顺手，完成任务后还有时间摸会鱼。"
    "考虑考虑把之前没补完的番看一看好了。"
    $p.times+=1
    jump TaskExecuting

label LoafingWork_result_bad:
    scene office with fade
    $Notice.show()
    "……似乎平稳地混过去了，今天似乎没什么比较难的工作的样子。"
    "要是每天都这么轻松就好了……"
    $p.times+=1
    jump TaskExecuting




label OvertimeWork_beginning:
    scene workarea with fade
    "工作还有一点没有完成，还是不要拖到下次上班好了。"
    "……要集中精神了，不能让头疼干扰我。"
    call Task_processing from _call_Task_processing_12
    $p.times+=1
    $OvertimeWork.executeTask(p)

label OvertimeWork_result_exce:
    scene workarea with fade
    $Notice.show()
    "……并没有剩太多很难的任务，还算轻松搞定了。"
    "不过没有主管盯着倒是蛮舒服的……总之该休息了！"
    $p.times+=1
    jump TaskExecuting

label OvertimeWork_result_good:
    scene workarea with fade
    $Notice.show()
    "还不赖，虽然堆到休息时间才做工，不过该完成的都做完了……"
    "我这么勤奋什么时候给我涨工资呢？"
    $p.times+=1
    jump TaskExecuting

label OvertimeWork_result_norm:
    scene workarea with fade
    $Notice.show()
    "感觉比在公司里工作还要简单……"
    "毕竟可以躺在床上办公……困了就睡……"
    $p.times+=1
    jump TaskExecuting

label OvertimeWork_result_bad:
    scene workarea with fade
    $Notice.show()
    "……头好疼，好想吐，我不行了……"
    "还是拖到下次上班时候做好了。"
    $p.times+=1
    jump TaskExecuting





label SnapWork_beginning:
    scene office with fade
    "困死了，我得先稍微小睡一会……"
    call Task_processing from _call_Task_processing_13
    $p.times+=1
    $SnapWork.executeTask(p)

label SnapWork_result_exce:
    scene office with fade
    $Notice.show()
    "在主管来巡查之前居然奇迹般地自然醒了……"
    "我睡得差不多了，还是假装在努力工作好了……"
    $p.times+=1
    jump TaskExecuting

label SnapWork_result_good:
    scene office with fade
    $Notice.show()
    "用手臂枕着睡觉好难过……"
    "买个颈枕这件事要尽快提上日程了……"
    $p.times+=1
    jump TaskExecuting

label SnapWork_result_norm:
    scene office with fade
    $Notice.show()
    "同事敲键盘的声音真是催眠……"
    "主管居然没注意到我睡着了吗？这家伙肯定也在摸鱼打游戏吧——"
    $p.times+=1
    jump TaskExecuting

label SnapWork_result_bad:
    scene office with fade
    $Notice.show()
    ar"“[p.name]！”"
    "白狼的声音在办公室里回荡着"
    ar"“下次在让我看见你睡觉！我就把你调到流水线去做十二个点的活！”"
    ar"“现在！给我工作！”"
    ar"“其他人也是！”"
    "该死……今天运气好差。"
    "被吵醒后太阳穴内的血管好像要炸开般地疼，看来今天要提前吃药了……"
    $p.times+=1
    jump TaskExecuting



label FocusWork_beginning:
    scene office with fade
    "不行，最近摸鱼太多了，不努努力这周工资肯定要泡汤了……"
    "就算头疼也稍稍忍耐下吧，希望明天的新闻不会是某社畜暴死电脑桌前……"
    call Task_processing from _call_Task_processing_14
    $p.times+=1
    $FocusWork.executeTask(p)

label FocusWork_result_exce:
    scene office with fade
    $Notice.show()
    s"“你没import那个什么numpy的包，肯定报什么都没找到的错呀……”"
    "这家伙真的是大学毕业来的吗……这还要我教……"
    "看来他弄完他自己负责那段，算了算我们这次工作已经完成平时的两倍进度了，而且也没有让我太头疼……"
    "周末去外面转转买点好吃的犒劳一下自己吧——"
    $p.times+=1
    jump TaskExecuting

label FocusWork_result_good:
    scene office with fade
    $Notice.show()
    "我轻车熟路地用快捷键关闭编译器和电脑，把没喝完的咖啡倒进垃圾桶里。"
    "至少这次工作之后应该有一段时间没有密集的工作了。"
    "还好不算太难，至少能在ddl之前做完。"
    $p.times+=1
    jump TaskExecuting

label FocusWork_result_norm:
    scene office with fade
    $Notice.show()
    "普通的社畜时光……"
    "头好疼……下班之后我要狠狠地睡他个十小时……"
    $p.times+=1
    jump TaskExecuting

label FocusWork_result_bad:
    scene office with fade
    $Notice.show()
    "感觉很不好！麻烦太多了！需求分析那边的到底在干什么啊，出这么多需求是想累死谁！"
    "胃疼……而且头也疼……"
    "我 以 后 再 也 不 想 这 样 工 作 了 ！"
    $p.times+=1
    jump TaskExecuting


label MeetingWork_beginning:
    scene meeting with fade
    "参加了每周一次的会议。"
    "会议上概括了一周以来的进度变化和公司成长，制定了下一阶段的工作目标。"
    "虽然大多与我无关，但稍微听听也对工作有好处就是。"
    "我把电脑包里的商务本拿出来，摆在会议室自己座位的桌上…"
    call Task_processing from _call_Task_processing_15
    $p.times+=1
    $MeetingWork.executeTask(p)

label MeetingWork_result_exce:
    scene meeting with fade
    $Notice.show()
    "在讲了些每次会议都会说的客套话后，在表扬阶段居然难得地提到了我们！"
    "我们部门上周的工作完成的很好，连天天摸鱼睡觉的我都被表扬了……"
    "好高兴啊，是不是该奖励自己吃一顿火锅？"
    if p.aco_p > 0:
        "或许应该叫上Acolas。"
    $p.times+=1
    jump acolas_plot_judge

label MeetingWork_result_good:
    scene meeting with fade
    $Notice.show()
    "这次会议提到的点似乎挺重要的。"
    "得记点笔记，或许之后的工作用得到。"
    $p.times+=1
    jump acolas_plot_judge

label MeetingWork_result_norm:
    scene meeting with fade
    $Notice.show()
    "就只是一周的总结而已，没什么特别的。"
    "看起来本周也没发生什么特殊的事情，下班之后应该做些什么呢……"
    $p.times+=1
    jump acolas_plot_judge

label MeetingWork_result_bad:
    scene meeting with fade
    $Notice.show()
    "非常无聊的内容……"
    "唉，他怎么又在讲企业创立的故事了……然后就是画大饼……"
    "讲这些有什么用呢，不如给我涨点工资。"
    "还是先想想周末去哪儿玩好了……"
    $p.times+=1
    jump acolas_plot_judge
