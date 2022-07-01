label DefaultSport_beginning:
    if p.times==3:
        scene morningrun with fade
        "虽然还想睡懒觉，但是Pathos医生说晨跑对恢复很有作用……"
        "虽然这种程度的有氧运动并不能改变太多，但总有一天量变会引起质变……"
    elif p.times==7:
        scene afternoonrun with fade
        "“饭后百步走，活到九十九。”……可是我活那么大岁数有什么意义呢？"
        "为了病情恢复……还是多走走吧……"
    else:
        scene nightrun with fade
        "也确实不能下了班后就倒在床上，该走一走了。"
        "即便是随便散散步也比躺着强，大概吧……"
    "我深呼吸，准备在公寓门口的步行路散散步。"

    call Task_processing from _call_Task_processing
    $p.times+=1
    $DefaultSport.executeTask(p)

label DefaultSport_result_exce:
    if p.times==4:
        scene morningrun with fade
    elif p.times==8:
        scene afternoonrun with fade
    else:
        scene nightrun with fade
    $Notice.show()
    "在室外行走的感觉总比待在室内要好多了。"
    "今天的空气真清新啊……慢慢走在路上感觉什么疲劳都消失了。"
    "或许之后应该像那些老人一样选个环境好的地方散散步。"
    $p.times+=1
    jump TaskExecuting

label DefaultSport_result_good:
    if p.times==4:
        scene morningrun with fade
    elif p.times==8:
        scene afternoonrun with fade
    else:
        scene nightrun with fade
    $Notice.show()
    "像是去往一个未知的目的地一样。"
    "放松……至少从社畜的环境走出来了，走出来总是好的。"
    $p.times+=1
    jump TaskExecuting

label DefaultSport_result_norm:
    if p.times==4:
        scene morningrun with fade
    elif p.times==8:
        scene afternoonrun with fade
    else:
        scene nightrun with fade
    $Notice.show()
    "大概就是为了动一动。"
    "走路其实也很累，而且我应该有段时间不活动了，走完这段路就回去吧，脚底都变热了。"
    $p.times+=1
    jump TaskExecuting

label DefaultSport_result_bad:
    if p.times==4:
        scene morningrun with fade
    elif p.times==8:
        scene afternoonrun with fade
    else:
        scene nightrun with fade
    $Notice.show()
    "外面的汽车尾气味吹得我脑袋疼……我就不该出来……应该躺在床上的……"
    "或许根本就是走路这件事不适合我，应该交给那些更健壮的人，交给街上那些那些比我健康多少倍的人。"
    "真糟糕……"
    $p.times+=1
    jump TaskExecuting




label JoggingSport_beginning:
    if p.times==4:
        scene morningrun with fade
    elif p.times==8:
        scene afternoonrun with fade
    else:
        scene nightrun with fade
    "也许只是单纯散步还不够……至少需要一点小小的锻炼，我可不想变成什么熊什么猪啊。"
    call Task_processing from _call_Task_processing_1
    $p.times+=1
    $JoggingSport.executeTask(p)

label JoggingSport_result_exce:
    if p.times==4:
        scene morningrun with fade
    elif p.times==8:
        scene afternoonrun with fade
    else:
        scene nightrun with fade
    $Notice.show()
    "慢跑注重的是环境，刚好我家旁边有一个公园。"
    "哎呀，我都没注意过，这个时间段好像有很多大学生在跑步……"
    "好帅……这个……裆部好鼓……那个好壮……要是能被他按在床上……"
    "不对，我是来锻炼身体的！"
    $p.times+=1
    jump TaskExecuting

label JoggingSport_result_good:
    if p.times==4:
        scene morningrun with fade
    elif p.times==8:
        scene afternoonrun with fade
    else:
        scene nightrun with fade
    $Notice.show()
    "还算流畅地绕着公园跑了一圈，能感觉到身上的毛都因为出汗黏在一起了……"
    "回家美美地冲个凉——"
    $p.times+=1
    jump TaskExecuting

label JoggingSport_result_norm:
    if p.times==4:
        scene morningrun with fade
    elif p.times==8:
        scene afternoonrun with fade
    else:
        scene nightrun with fade
    $Notice.show()
    "上喘的感觉让我想起了高中的1000米……"
    "没想到现在的我也能慢悠悠地跑起来……不过身体真的很累啊……我需要休息一下，喘喘气……"
    $p.times+=1
    jump TaskExecuting

label JoggingSport_result_bad:
    if p.times==4:
        scene morningrun with fade
    elif p.times==8:
        scene afternoonrun with fade
    else:
        scene nightrun with fade
    $Notice.show()
    "嘶……扭到了脚……"
    "为什么会有人在跑道上放块砖头啊！"
    "脚好痛……慢慢走回去吧……"
    $p.times+=1
    jump TaskExecuting




label FastrunSport_beginning:
    if p.times==4:
        scene morningrun with fade
    elif p.times==8:
        scene afternoonrun with fade
    else:
        scene nightrun with fade
    "慢跑还是太无聊了，得稍微出点汗才行啊。"
    "还是快点跑好了。"
    call Task_processing from _call_Task_processing_2
    $p.times+=1
    $FastrunSport.executeTask(p)

label FastrunSport_result_exce:
    if p.times==4:
        scene morningrun with fade
    elif p.times==8:
        scene afternoonrun with fade
    else:
        scene nightrun with fade
    $Notice.show()
    "跑起来！跑起来！原来跑这么快也不赖嘛，吹在身上的风和平时完全不一样。"
    "简直能让人忘记任何压力，脑袋也不是那么痛了。"
    $p.times+=1
    jump TaskExecuting

label FastrunSport_result_good:
    if p.times==4:
        scene morningrun with fade
    elif p.times==8:
        scene afternoonrun with fade
    else:
        scene nightrun with fade
    $Notice.show()
    "还行……至少我不会被别人说是蜗牛……好像也没有人对于评价我这件事感兴趣……"
    "不过我速度还是挺快的嘛，虽然不知道有什么用处……但是建立信心总是好的！"
    $p.times+=1
    jump TaskExecuting

label FastrunSport_result_norm:
    if p.times==4:
        scene morningrun with fade
    elif p.times==8:
        scene afternoonrun with fade
    else:
        scene nightrun with fade
    $Notice.show()
    "这种速度感让我想起了高中的50米接力。"
    "太累了，感觉身上都是汗……得去洗澡了，感觉有什么不太妙的味道。"
    $p.times+=1
    jump TaskExecuting

label FastrunSport_result_bad:
    if p.times==4:
        scene morningrun with fade
    elif p.times==8:
        scene afternoonrun with fade
    else:
        scene nightrun with fade
    $Notice.show()
    "摔倒了！"
    "不是一般的痛，甚至膝盖都擦破了一些"
    "周围也没什么人能帮忙……看来得去买双氧水消消毒……"
    $p.times+=1
    jump TaskExecuting

label BadmintonClass_beginning:
    scene gym with fade
    "……"
    "像之前那样溜进来了。"
    scene court with dissolve
    "站队，点名，和记忆中的体育课完全一样，唯独不同的是我不会被点到名字。"
    "那么就好好观察老师的动作，认真听听都讲了些什么吧。"
    call Task_processing from _call_Task_processing_4
    $p.times+=1
    $BadmintonClass.executeTask(p)

label BadmintonClass_result_exce:
    scene court with fade
    $Notice.show()
    "不知道为什么总是很想快乐的打一次羽毛球。"
    "我或许是在羡慕这些大学生没有接受社会毒打？"
    "要认真练习了，得让Halluke注意到我才行。"
    jump halluke_plot_judge_1

label BadmintonClass_result_good:
    scene court with fade
    $Notice.show()
    "不知道为什么总是很想快乐的打一次羽毛球。"
    "我或许是在羡慕这些大学生没有接受社会毒打？"
    "要认真练习了，得让Halluke注意到我才行。"
    jump halluke_plot_judge_1

label BadmintonClass_result_norm:
    scene court with fade
    $Notice.show()
    "稍微有点打累了……"
    "普通的挥一挥球杆吧，对面的学生看起来也没什么精神的样子。"
    "不过能欣赏这些年轻大学生的肉体，也算是值了诶。"
    jump halluke_plot_judge_1

label BadmintonClass_result_bad:
    scene court with fade
    $Notice.show()
    "稍微有点打累了……"
    "普通的挥一挥球杆吧，对面的学生看起来也没什么精神的样子。"
    "不过能欣赏这些年轻大学生的肉体，也算是值了诶。"
    jump halluke_plot_judge_1


label StretchingSport_beginning:
    scene livingroom with fade
    "身上好酸……运动后还是要按正常运动流程做一下拉伸运动的。"
    "总之……开始吧。"
    "我把瑜伽垫从柜子深处拽出来，铺在客厅中间。"
    call Task_processing from _call_Task_processing_5
    $p.times+=1
    $StretchingSport.executeTask(p)

label StretchingSport_result_exce:
    scene livingroom with fade
    $Notice.show()
    "普通的运动后拉伸。"
    "很久以前，大概读书的时候才会有的活动，真的让人很怀念年轻的时候。"
    "大概连病都没有现在这么严重。"
    $p.times+=1
    jump TaskExecuting

label StretchingSport_result_good:
    scene livingroom with fade
    $Notice.show()
    "普通的运动后拉伸。"
    "很久以前，大概读书的时候才会有的活动，真的让人很怀念年轻的时候。"
    "大概连病都没有现在这么严重。"
    $p.times+=1
    jump TaskExecuting

label StretchingSport_result_norm:
    scene livingroom with fade
    $Notice.show()
    "我应该在床上躺着而不是在这里做拉伸……"
    "本来运动就浑身酸痛，现在感觉更难受了……"
    "好吧，有点夸张了，总之感觉舒服多了……"
    $p.times+=1
    jump TaskExecuting

label StretchingSport_result_bad:
    scene livingroom with fade
    $Notice.show()
    "我应该在床上躺着而不是在这里做拉伸……"
    "本来运动就浑身酸痛，现在感觉更难受了……"
    "好吧，有点夸张了，总之感觉舒服多了……"
    $p.times+=1
    jump TaskExecuting