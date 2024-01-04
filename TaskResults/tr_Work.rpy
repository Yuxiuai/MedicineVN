label DefaultWork_beginning:
    scene office with fade
    if p.times<5:
        "开始进行今天的工作吧。"
        "我深呼吸，按压自己工位桌上电脑的电源键。"
    else:
        "午餐时间过得好快……"
        "继续下午的工作……"
        "我揉了下疲惫的眼睛，将睡眠中的电脑打开。"
    call Task_processing from _call_Task_processing
    
    $p.times+=1
    $DefaultWork.executeTask(p)

label DefaultWork_result_exce:
    scene office with fade
    $Notice.show()
    "好像一不小心解决了当前项目之前程序员埋下的隐患！"
    "这周的会议我肯定要被表扬了。"
    "嘿嘿，这就是得意的感觉吗！"
    $p.times+=1
    jump after_executing_task_label

label DefaultWork_result_good:
    scene office with fade
    $Notice.show()
    "虽然今天工作很繁重，不过也算是按时完成了。"
    "不愧是我。"
    $p.times+=1
    jump after_executing_task_label

label DefaultWork_result_norm:
    scene office with fade
    $Notice.show()
    "今天的代码写得很顺手，完成任务后还有时间摸会鱼。"
    "考虑考虑把之前没补完的番看一看好了。"
    $p.times+=1
    jump after_executing_task_label

label DefaultWork_result_bad:
    scene office with fade
    $Notice.show()
    "……似乎平稳地混过去了，今天似乎没什么比较难的工作的样子。"
    "要是每天都这么轻松就好了……"
    $p.times+=1
    jump after_executing_task_label


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
        "阅读携带的书籍" if p.canRead >= 0 and list(filter(lambda x: x.kind in ('书籍', '专业类书籍') and type(x) not in p.itemcd, p.items)) != []:
            $nums = 1
            if MeetingReward5.has(p):
                $nums = 2
            
            $renpy.call_screen(_screen_name="screen_tr_readingbook", player=p,nums=nums)
    $p.times+=1
    $LoafingWork.executeTask(p)

label LoafingWork_result_exce:
    scene office with fade
    $Notice.show()
    "好像一不小心解决了当前项目之前程序员埋下的隐患！"
    "这周的会议我肯定要被表扬了。"
    "嘿嘿，这就是得意的感觉吗！"
    $p.times+=1
    jump after_executing_task_label

label LoafingWork_result_good:
    scene office with fade
    $Notice.show()
    "虽然今天工作很繁重，不过也算是按时完成了。"
    "不愧是我。"
    $p.times+=1
    jump after_executing_task_label

label LoafingWork_result_norm:
    scene office with fade
    $Notice.show()
    "今天的代码写得很顺手，完成任务后还有时间摸会鱼。"
    "考虑考虑把之前没补完的番看一看好了。"
    $p.times+=1
    jump after_executing_task_label

label LoafingWork_result_bad:
    scene office with fade
    $Notice.show()
    "……似乎平稳地混过去了，今天似乎没什么比较难的工作的样子。"
    "要是每天都这么轻松就好了……"
    $p.times+=1
    jump after_executing_task_label




label OvertimeWork_beginning:
    $routine_bg(p)
    "工作还有一点没有完成，还是不要拖到下次上班好了。"
    "……要集中精神了，不能让头疼干扰我。"
    call Task_processing from _call_Task_processing_1
    
    $p.times+=1
    $OvertimeWork.executeTask(p)

label OvertimeWork_result_exce:
    $routine_bg(p)
    $Notice.show()
    "……并没有剩太多很难的任务，还算轻松搞定了。"
    "不过没有主管盯着倒是蛮舒服的……总之该休息了！"
    $p.times+=1
    jump after_executing_task_label

label OvertimeWork_result_good:
    $routine_bg(p)
    $Notice.show()
    "还不赖，虽然堆到休息时间才做工，不过该完成的都做完了……"
    "我这么勤奋什么时候给我涨工资呢？"
    $p.times+=1
    jump after_executing_task_label

label OvertimeWork_result_norm:
    $routine_bg(p)
    $Notice.show()
    "感觉比在公司里工作还要简单……"
    "毕竟可以躺在床上办公……困了就睡……"
    $p.times+=1
    jump after_executing_task_label

label OvertimeWork_result_bad:
    $routine_bg(p)
    $Notice.show()
    "……头好疼，好想吐，我不行了……"
    "还是拖到下次上班时候做好了。"
    $p.times+=1
    jump after_executing_task_label













label CafeWork_beginning:
    $routine_bg(p)
    if CafeBuff.has(p):
        "这种地方倒是很适合办公，偶尔做做代码维护的工作试试看吧……"
    elif p.onVacation:
        "本来计划去咖啡馆做这个的，突然又懒得出去了，就在家里好了……"
    else:
        "工作做得差不多了，稍微维护一下代码好了……"

    "……呼……集中精神，不能让头疼干扰我。"
    call Task_processing from _call_Task_processing_32
    
    $p.times+=1
    $CafeWork.executeTask(p)

label CafeWork_result_exce:
    $routine_bg(p)
    $Notice.show()
    "好累……不过可以随手点一杯咖啡来喝。"
    "不过总体来看成果还算不错，希望他们能给我多涨些工资……"
    $p.times+=1
    jump after_executing_task_label

label CafeWork_result_good:
    $routine_bg(p)
    $Notice.show()
    "勉强完成了吧……"
    "这种工作还是应该留给那些更聪明的人来做……"
    $p.times+=1
    jump after_executing_task_label

label CafeWork_result_norm:
    $routine_bg(p)
    $Notice.show()
    "越写越乱，根本不知道从什么地方下手。"
    "十分吃力的工作，下次还是不要为了一点工资做这种事了……"
    $p.times+=1
    jump after_executing_task_label

label CafeWork_result_bad:
    $routine_bg(p)
    $Notice.show()
    "头好疼……啊啊啊啊……"
    "感觉甚至把已有的工作越搞越乱了……"
    "我再也不想做这种工作了……凭什么我要折磨自己呢。"
    $p.times+=1
    jump after_executing_task_label












label SnapWork_beginning:
    scene office with fade
    "困死了，我得先稍微小睡一会……"
    call Task_processing from _call_Task_processing_2
    
    $p.times+=1
    $SnapWork.executeTask(p)

label SnapWork_result_exce:
    scene office with fade
    $Notice.show()
    "在主管来巡查之前居然奇迹般地自然醒了……"
    "我睡得差不多了，还是假装在努力工作好了……"
    $p.times+=1
    jump after_executing_task_label

label SnapWork_result_good:
    scene office with fade
    $Notice.show()
    "用手臂枕着睡觉好难过……"
    "买个颈枕这件事要尽快提上日程了……"
    $p.times+=1
    jump after_executing_task_label

label SnapWork_result_norm:
    scene office with fade
    $Notice.show()
    "同事敲键盘的声音真是催眠……"
    "主管居然没注意到我睡着了吗？这家伙肯定也在摸鱼打游戏吧——"
    $p.times+=1
    jump after_executing_task_label

label SnapWork_result_bad:
    scene office with fade
    $Notice.show()
    show arnel with dissolve
    ar"“[p.name]！”"
    "白狼的声音在办公室里回荡着。"
    ar"“下次在让我看见你睡觉！我就把你调到流水线去做十二个点的活！”"
    ar"“现在！给我工作！”"
    ar"“其他人也是！”"
    hide arnel with dissolve
    "该死……今天运气好差。"
    "被吵醒后太阳穴内的血管好像要炸开般地疼，看来今天要提前吃药了……"
    $p.times+=1
    jump after_executing_task_label



label FocusWork_beginning:
    scene office with fade
    "不行，最近摸鱼太多了，不努努力这周工资肯定要泡汤了……"
    "就算头疼也稍稍忍耐下吧，希望明天的新闻不会是某社畜暴死电脑桌前……"
    call Task_processing from _call_Task_processing_3
    
    $p.times+=1
    $FocusWork.executeTask(p)

label FocusWork_result_exce:
    scene office with fade
    $Notice.show()
    $ss('glasses sweat mood white no_hat')
    s"“哎呀，你忘了给程序连接数据库了，这还能忘啊……”"
    $sh()
    "这家伙真的是大学毕业来的吗……"
    "站在他身边看着他弄完，算了算我们这次工作已经完成相对于平时的两倍进度了，而且也没有让我太头疼……"
    "周末去外面转转买点好吃的犒劳一下自己吧——"
    $p.times+=1
    jump after_executing_task_label

label FocusWork_result_good:
    scene office with fade
    $Notice.show()
    "我轻车熟路地用快捷键关闭编译器和电脑，把没喝完的咖啡倒进垃圾桶里。"
    "至少这次工作之后应该有一段时间没有密集的工作了。"
    "还好不算太难，至少能在ddl之前做完。"
    $p.times+=1
    jump after_executing_task_label

label FocusWork_result_norm:
    scene office with fade
    $Notice.show()
    "普通的社畜时光……"
    "头好疼……下班之后我要狠狠地睡他个十小时……"
    $p.times+=1
    jump after_executing_task_label

label FocusWork_result_bad:
    scene office with fade
    $Notice.show()
    "感觉很不好！麻烦太多了！需求分析那边的到底在干什么啊，出这么多需求是想累死谁！"
    "胃疼……而且头也疼……"
    "我 以 后 再 也 不 想 这 样 工 作 了 ！"
    $p.times+=1
    jump after_executing_task_label


label MeetingWork_beginning:
    scene meeting with fade
    "参加了每周一次的会议。"
    "会议上概括了一周以来的进度变化和公司成长，制定了下一阶段的工作目标。"
    "虽然大多与我无关，但稍微听听也对工作有好处就是。"
    "我把电脑包里的商务本拿出来，摆在会议室自己座位的桌上…"
    call Task_processing from _call_Task_processing_4
    
    $p.times+=1
    $MeetingWork.executeTask(p)

label MeetingWork_result_exce:
    scene meeting with fade
    $Notice.show()
    "在讲了些每次会议都会说的客套话后，在表扬阶段居然难得地提到了我们！"
    "我们部门上周的工作完成的很好，连天天摸鱼睡觉的我都被表扬了……"
    "好高兴啊，是不是该奖励自己吃一顿火锅？"
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


label DestotWork_beginning:
    scene office with fade
    "也确实应该找些时间教他一些东西了，总让他旁观我工作应该也学不到什么……"
    "唉，早知道我当时就不带什么实习生了……"
    call Task_processing from _call_Task_processing_21
    
    $p.times+=1
    $DestotWork.executeTask(p)

label DestotWork_result_exce:
    scene office with fade
    $Notice.show()
    show destot with dissolve
    $ss('glasses smile_eyes smile_mouth white no_hat')
    s"“我们比较通用的框架就是这样的，基本上要做的东西也不多，照葫芦画瓢就行了……”"
    $sh()
    des"“这样，我之前也学习过一些这个框架的内容，之前有一次课设就是这个，不过现在也忘得差不多了。”"
    des"“今晚下班之后得努力钻研一下！谢谢前辈指导！”"
    "不得不说他真的是蛮努力的啊，比摆烂的我有激情有精力多了。"
    "幸好他问的问题我还算了解，如果他变得更厉害了的话，应该就能帮我完成不少工作了吧……"
    $p.times+=1
    jump after_executing_task_label

label DestotWork_result_good:
    scene office with fade
    $Notice.show()
    show destot with dissolve
    $ss('glasses sweat smile_eyes smile_mouth white no_hat')
    s"“这些问题……这样……那样写就可以了。”"
    $sh()
    des"“原来是这样……我大概明白了！”"
    "还算比较普遍的问题吧，但是刚刚离开象牙塔的大学生不会遇到的东西。"
    "有时候我还在担心自己的能力是否足够，不过无论是什么能帮到他就太好了。"
    $p.times+=1
    jump after_executing_task_label

label DestotWork_result_norm:
    scene office with fade
    $Notice.show()
    show destot with dissolve
    $ss('glasses sweat white no_hat')
    s"“这些问题有些都可以查阅文档得到解答的，如果文档里没有那网上随便搜一搜肯定就有的。”"
    $sh()
    des"“抱歉……我会去看的！总问一些无聊问题也是我的缺点，我要努力改正！谢谢前辈指导！”"
    "虽然有些问题也确实是很无聊，但也有一些是我根本没了解的东西……"
    "让他去网上看看其他人的解法吧，总比学半吊子的我好。"
    $p.times+=1
    jump after_executing_task_label

label DestotWork_result_bad:
    scene office with fade
    $Notice.show()
    show destot with dissolve
    $ss('glasses sweat normal2_eyes awkward_mouth white no_hat')
    s"“这个……只要这样……”"
    $ss('glasses sweat normal_eyes awkward_eyebrow mood white no_hat')
    s"“诶，怎么会这样……”"
    $sh()
    des"“虽然有点冒犯不过，前辈你这样写不对，我之前学过这个的，应该要这样这样……”"
    "那只小兔子开始用我的电脑开始写代码，这下被他当老师了。"
    $ss('glasses sweat normal_eyes angry_eyebrow angry_mouth blush white no_hat')
    s"“这么简单的事情我会不知道吗？我……还不是为了考考你看看你能不能发现……”"
    $sh()
    des"“原来是这样！那我现在明白了！谢谢前辈指导！”"
    "不知道我为什么会下意识对他嘴硬，现在只觉得脸上有火在烧。"
    "好羞耻，但是也算学到了新东西吧。"
    $p.times+=1
    jump after_executing_task_label