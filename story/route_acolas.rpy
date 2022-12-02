label acolas_plot_judge:  # 羽毛球课程
    if persistent.nocharacterplot or p.aco_p == -1:
        $p.times+=1
        jump TaskExecuting
        
    #if p.hal_p > 6:
    #    scene court with fade
    #    "解散之后，acolas便和之前一样，冲到某个还没有被占用的球网边，随后看向我。"
    #    "那就和他一起打球打到下课吧？"
    #    $p.times+=1
    #    jump TaskExecuting
    if p.aco_p not in (7, 8, 12, 99):
        $jumplabel = 'acolas_route_' + str(p.aco_p)
        $renpy.jump(jumplabel)
    else:

        if p.aco_p == 8 and AcolasTask2 not in p.unlockedTasks:
            $AcolasTask2.unlock(p)
            $Message.new(p, 'Acolas', 'Acolas', '好消息！\n医生说我可能今天就可以出院了，你似乎还没来过我家吧？来玩一玩吧？周末的下午我有空哦。\n我家就在亚斯塔禄大街的恩多尔芬小区，54栋3312，到了楼下直接说我的名字就可以，服务生会带你上来的。\n除此之外我还想问你一些其他的东西，等你来了再和你说。', pos='a')
        $p.times+=1
        jump TaskExecuting





label acolas_route_0:
    $start_plot()
    stop music fadeout 5
    scene office with fade
    "我应该是从会议室里第一个出来的。"
    "马上就是心心念念的双休日时间了，也许我应该感到开心，但我现在的头疼状态也没法让我做什么有意思的事情。"
    "看来又得睡个两天觉补充补充精神了。"
    "马上就要到下班时间了，我回到自己的工位，整理桌子上的资料和文件。"
    "周围的同事在聊些当季明星和无聊的短视频内容。"
    "我瞟了一眼电脑显示屏的右下角，用拳头尖按压太阳穴。"
    "虽然说我对于办公室八卦总是没什么兴趣的。"
    "不过即便我不想听，我也不可能把自己的耳朵完全封死。"
    ol1"“新来的技术总监好帅啊——而且听说工作能力也超强！”"
    ol1"“我们部门的工作进度肯定远超其他部门啦！”"
    ol2"“是啊是啊，听说HR收到他要跳槽过来的消息，整个人都傻掉了！”"
    ol2"“马上就把之前那个啥也不会还总是摆架子的总监开了！”"
    ol1"“看他被打包踹回家的表情，实在是太爽啦！”"
    "…"
    "新的技术总监吗…"
    "可是这和我又有什么关系呢。"
    "讨论帅哥是那些女孩的事，我这种人要样貌没样貌，要钱没钱，一身病不说，还是个同性恋。"
    "总不可能出现那种天降好男友的剧情吧，比如什么，看到我就直接一见钟情，还当霸道总裁之类的…"
    "想想都觉得可笑。"
    "我单手按下电源键，将整理好的文件资料塞进文件夹里，丢进抽屉里之后离开我的工位。"
    "终于下班了。"
    "…"
    menu:
        "去楼梯（将无法触发人物剧情）" if replaying and p.aco_p>0 or not replaying:
            "走楼梯回去吧……"
            "公司的电梯总让我想起医院的电梯，似乎两个电梯是同一型号的。"
            "……"
            $end_plot()
            if replaying:
                jump afterreplay
            $p.aco_p = -1
            $p.times+=1
            jump TaskExecuting
                
        "去电梯" if replaying and p.aco_p==0 or not replaying:
            pass

    scene corridor with dissolve
    "如果他真的有能力带领我们，让项目进度更快的话，那也算是好事吧。"
    "我叹口气，打卡下班，来到电梯间。"
    "…"
    scene elevator with dissolve
    play music audio.acolas
    show acolas normal3_eyes phoneon earphone with dissolve
    "电梯里有一只稍高于我的灰狼。"
    "他正靠着电梯内部的右侧，看着手机。"
    "我抬头看了一眼他。"
    "他的目光注视着手中的智能手机，似乎对外界没有兴趣。"
    "两只上翘的耳朵被耳塞耳机堵住，连接至挂在他脖子上的挂脖式蓝牙耳机。"
    "并不像是在玩游戏，似乎只是在一页一页看着什么。"
    "他亮红色的眼球随着他拇指的翻动从上至下移动着，而后又回到上方。"
    "我没有意识到自己好像一直在盯着陌生人，他也没有注意到我正在看着他。"
    "…"
    "电梯到一楼了。"
    "我看向他，因为会觉得这种把自己封闭起来的人会比较自顾自地离开而很容易撞到别人。"
    show acolas phoneoff normal_eyes
    with dissolve
    "不过他在注意到电梯停止后，也看向我。"
    "怕和我撞到一起吗？"
    "我努力发挥自己仅有一丁点的随机应变能力，对他挤出一个微笑，虽然心里知道那一定很丑，希望没有吓到他。"
    "然后我快速地从电梯里走出来。"
    "…"
    stop music fadeout 5
    scene corridor with dissolve
    "我刚刚是不是有点反应过度了，明明直接走出来也不是不行啊…"
    "他会不会以为我被他吓到了才逃跑似的冲出去……"
    "……唉，我真是个笨蛋。"
    $end_plot()
    if p.aco_p == 0:
        $p.aco_p = 1
    if replaying:
        jump afterreplay
    $p.times+=1
    jump TaskExecuting

label acolas_route_1:
    $start_plot()
    stop music fadeout 5
    scene meeting with fade
    ar"“总之，在会议的最后，让我们来介绍一下新上任的技术总监Acolas。”"
    "目光正聚焦于桌下的手机上的小游戏界面的我在听到这个名字后抬起头来。"
    play music audio.acolas
    show acolas normal2_eyes
    with dissolve
    "诶，这个人好面熟啊。"
    show acolas normal_eyes surprised_eyebrow
    with dissolve
    "等等，这不就是上周五我遇到的那个……"
    "这套路可真是俗气，巧到言情小说都不会这样写吧。"
    "他似乎注意到我了。"
    "假装不认识他吧。"
    hide acolas with dissolve
    "我把目光转到其他同事身上。"
    "不出意外，那些女人看到这只又高又壮的种狼眼睛都直了。"
    "壮有什么用，反正也不会是我的，难道过一会这只灰狼就会自来熟地把他那鼓鼓的裆部贴在我屁股上吗？"
    "……"
    show acolas normal2_eyes at look
    with dissolve
    "我的目光再一次偷偷溜到灰狼的身上，不过这一次则稍稍偏下。"
    "……果然很大啊……"
    show acolas normal_eyes at look_
    "想什么呢？这种男人又不会是我的——"
    show acolas normal2_eyes
    "这只灰狼的名字是Acolas吧。"
    show acolas smile_mouth smile_eyebrow
    "Acolas在前面顺着Arnel的介绍讲着客套话，大概也就是什么“我会带领团队越来越好的”之类的。"
    "我对工作要是能有他一半精力旺盛，现在就不会天天只坐在这个位置了。"
    stop music fadeout 5
    scene office with fade
    "结束了。"
    "上周那几个女同事讨论的新总监也确实并非只是瞎说，在这次会议的最后他就登场了。"
    "他肯定就是上周五下班的时候，电梯里那只高个子戴耳机的灰狼。"
    "不过他已经忘了这事了也说不定。"
    "但总觉得怪怪的。"
    "…"
    play music audio.rareleisure
    "不管了，下班了，接下来又是美好的周末。"
    "我已经习惯这种临时突然挤进来的新任务了，生硬地破坏了我美好的周五下班放松计划。"
    "明明还有时间去吃点小吃，但做完剩下这点东西已经是两个小时之后了。"
    "我整理着自己桌子上的文件，把待机中的电脑关机。"
    "把散乱的文件排序后放进文件夹，桌子上已经用过的草稿纸一会丢进碎纸机里好了。"
    stop music
    show acolas at trans_toLeft()
    "我转头，突然发现有个高大的家伙就站在身后。"
    $ss('no_hat white glasses normal2_eyes scared_mouth scared_eyebrow em')
    s"“啊啊啊！…啊…是总监，你好…”"
    $sh()
    show acolas angry_eyes angry_eyebrow with dissolve
    "灰狼用他的红色瞳孔注视着我，相对于他的毛发较浅的眉毛则挤在一起。"
    "是…我犯了什么错误了吗……"
    "好强的…压迫感……"
    "我下意识地向后，但后面就是桌子了。"
    "他高于自己的身躯更是加重了这种压迫感…"
    show acolas normal3_eyes with dissolve
    "只见他终于挪开了视线，似乎在看周围。"
    "但现在这里应该只有我和他。"
    show acolas angry_eyes with dissolve
    "他伸出爪子。"
    "当我的身体感觉到来自于外界物体的触碰时，精神上并不相信这种情况居然在现实发生了。"
    "我的身体靠在桌沿，身后的两只爪子平铺在桌面上，支撑着身体。"
    "而他的爪腹则覆盖着我上衣胸前的部分。"
    "随后向下，到我的腹部。"
    play music audio.heartbeat
    show acolas smile_mouth with dissolve
    "我的毛发间开始分泌汗液。"
    "这，不会是要，被那个了吧。"
    "不，不行，现在还不能…"
    $Erection.add(p)
    "也许他比我还早知道我自己已经勃起了的这个事实，因为当他的爪子已经隔着裤子开始触摸我的裆部时。"
    "大脑一片空白的我才意识到自己早就在被他爪子抚摸身体的某个瞬间勃起了。"
    $ss('no_hat white glasses normal2_eyes scared_mouth scared_eyebrow blush sweat')
    s"“那个…我……”"
    $sh()
    "这种情况下要说什么，要怎么做，天哪…"
    "我的处男生涯终于要结束了吗？被一个刚刚才见过第一面的新来的总监强奸？"
    scene black
    "我只能闭上双眼。"
    "…"
    play music audio.acolas
    ac"“噗。”"
    ac"“哈哈哈哈。”"
    scene office with dissolve
    show acolas smile_mouth smile_eyebrow smile_eyes with dissolve
    "他突然向后一步，紧张的面容迅速转变为笑容。"
    "…到底是怎么回事啊！"
    ac"“那个，太好笑了，但，哈哈…好吧，也不是…”"
    "我都不知道我应该说什么。"
    "甚至我都不知道我现在应该想什么。"
    "愤怒？开心？希望被强奸？或者因为他没有继续进行而感到遗憾？"
    "我现在的表情一定很奇妙。"
    "再加上裆部那令人尴尬的奇妙勃起。"
    ac"“咳咳，好吧，对不起，用这种方式和你打招呼。”"
    ac"“我在刚刚的会议上看到你了，你的名字是…[p.name]吧。”"
    ac"“虽然介绍过了，但怕你当时没有专心，就重新介绍一下我自己吧。”"
    a"“我是Acolas，暂时是这个地方新来的技术总监，今后我们就一起工作了。”"
    "其实我仍然没有缓过来神，他主动抓过我的爪子，然后使劲摇晃起来。"
    "这种性骚扰一般的开场白也太奇怪了！他是不是也是这么对待上一个公司的其他员工，被嫌弃所以跳槽来这里了？"
    $ss('no_hat white glasses mood blush sweat')
    s"“呃…你好，Acolas。”"
    $ss('no_hat white glasses normal2_eyes angry_mouth angry_eyebrow')
    s"“下次，请不要这样…”"
    $sh()
    "妈的，为什么我的那东西还硬着。"
    show acolas surprised_eyebrow surprised_eyes with dissolve
    a"“啊…那个，对不起对不起，其实我不是这样的人啦，单纯是因为，我其实认识你的。”"
    $ss('no_hat white glasses surprised_eyes surprised_eyebrow')
    s"“认识我？”"
    $sh()
    "我深呼吸，转头继续整理自己的东西。"
    show acolas smile_mouth smile_eyebrow smile_eyes with dissolve
    a"“你是用Solitus作网名写作的吧，我也曾委托过你写东西。”"
    $ss('no_hat white glasses')
    s"“诶，是这样的吗？你委托了什么？”"
    $sh()
    "脑海里似乎并没有这样的一个委托人，或者说，毕竟我也接了很多委托了，也没法记住每一个。"
    show acolas surprised_eyebrow surprised_mouth with dissolve
    a"“大概是…那个那个…这个这个…”"
    $ss('no_hat white glasses normal2_eyes normal2_eyebrow sweat')
    s"“……”"
    $sh()
    show acolas smile_mouth smile_eyebrow smile_eyes with dissolve
    "操，是那个性癖很怪的那个家伙。"
    "但也是真的很有钱…"
    $ss('no_hat white glasses')
    s"“噢…大概明白了。”"
    $sh()
    if p.name=="Solitus":
        "也许这就是实名上网的坏处了。"
    else:
        "虽然很好奇他为什么通过一个网名就能联系到我，但想了想自己似乎也曾经在社交网站发过自己的照片和居住地之类的。"
        "如果关注了我应该也能认出来我才是。"
    "不过他的胆子也太大了，这么弄不怕认错人吗？"
    show acolas normal_eyebrow normal_eyes with dissolve
    a"“总之，我很喜欢你的作品，之后也会继续找你委托的。”"
    $ss('no_hat white glasses sweat')
    s"“好，谢谢夸奖。”"
    $sh()
    "我抬起头，对他做出一个微笑。"
    "虽然是挤出来的，但被他夸奖，其实心里也有一些小开心。"
    show acolas awkward_eyebrow awkward_mouth with dissolve
    a"“那么，我就先走了。”"
    a"“再见，Solitus。”"
    $ss('no_hat white glasses')
    s"“…”"
    $ss('no_hat white glasses smile_mouth normal2_eyes')
    s"“周一见。”"
    $sh()
    stop music fadeout 5
    hide acolas with dissolve
    "…"
    $Erection.clearByType(p)
    "他走了。"
    "我低头看着自己的裆部。"
    "它终于变成了非常平静的状态。"
    "我叹口气，在处理好最后一点东西之后，准备离开公司。"
    $end_plot()
    if p.aco_p == 1:
        $p.aco_p = 2
    if replaying:
        jump afterreplay
    $p.times+=1
    jump TaskExecuting




label acolas_route_2:
    $start_plot()
    stop music fadeout 5
    scene office with fade
    
    "会议室的灯光总是比本楼层的其他照明灯关得晚一些。"
    "总结，或者是讨论接下来的工作，之后的会议内容便是不需要我们这些普通的员工所参与了。"
    "本部门的工作区只剩我一人。"
    "虽然上周是由于一点工作上的小事情，但这周我是主动停留在这里的。"
    "我转头看向自己的工位。"
    "我很喜欢桌上有一些小东西，盆栽，金属摆件，或者可爱的小玩具，插上电就会左右晃之类的东西。"
    "每天离开之前我都会照顾他们，给盆栽里浇一点水，擦干净摆件上的灰尘等等。"
    "当然，工作相关的文件我也有好好整理就是。"
    "一个热爱做日程表的人永远不会是一个邋遢的人。"
    play music audio.acolas
    a"“等我多久了？”"
    show acolas smile_eyes smile_eyebrow smile_mouth with dissolve
    "我听到声音，转头看向身后的狼。"
    $ss('no_hat white glasses normal2_eyes')
    s"“也没多久。”"
    $sh()
    "他似乎稍微有些疲倦，但很明显，他在努力让自己不那么狼狈。"
    $ss('no_hat white glasses normal_eyes')
    s"“找我有什么事吗？”"
    $sh()
    show acolas normal2_eyes normal_eyebrow awkward_mouth with dissolve
    "其实当我昨天上写作平台的时候，看到他给我发了几条消息。"
    "大概是说，周五会议结束后等他一会。"
    "不过这个地方现在只有我们两个，难道他还想继续上周没干完的事？"
    "我撇撇嘴。"
    show acolas normal_eyes normal_eyebrow awkward_mouth with dissolve
    a"“那个…”"
    "他把公文包放在我的桌面上，靠在架子边。避开了我桌上的任何盆栽和摆件。"
    show acolas normal_eyes normal_eyebrow normal_mouth with dissolve
    a"“我回去想了很多，总觉得你可能会在意我那周五晚上对你做的事。”"
    a"“我想和你道个歉，当时的我有点太失礼了。”"
    show acolas normal3_eyes surprised_eyebrow normal_mouth with dissolve
    "他微低头，用爪子挠着他的头顶。"
    "他身后的尾巴正以较快的速度甩向一侧，停留半晌后又迅速地甩到另一侧去。"
    $ss('no_hat white glasses normal_eyes')
    s"“…我其实没有很在意。”"
    $ss('no_hat white glasses normal2_eyes smile_mouth')
    s"“被这样调戏的话，还在上学的时候就经常被室友这样逗弄了。”"
    show acolas normal3_eyes surprised_eyebrow normal_mouth with dissolve
    $ss('no_hat white glasses normal_eyes smile_mouth')
    s"“没什么事啦……”"
    $sh()
    "他的头比刚刚稍微抬高了一些，但为了看着我，仍然是低头的状态。"
    show acolas surprised_eyes surprised_eyebrow smile_mouth with dissolve
    a"“好。”"
    "他的嘴角快速弯曲成一个弧度。"
    show acolas normal3_eyes normal_eyebrow normal_mouth sweat with dissolve
    a"“如果我没和你道歉，会让我自己感觉有点焦虑。”"
    "他的眼神飘向一侧，然后又回到自己身上。"
    "这家伙在某种方面上还有些奇怪地固执呢。"
    show acolas smile_eyes smile_eyebrow smile_mouth no_sweat with dissolve
    a"“啊，心里没有负担的感觉真好啊。”"
    a"“就像把心脏挖出来，丢到外面让它自由地跑上一圈再回来。”"
    $ss('no_hat white glasses normal_eyes scared_mouth scared_eyebrow sweat')
    s"“真是……奇妙的比喻。”"
    $sh()
    stop music fadeout 5
    "我拽起椅子上我的小布包，准备离开这个地方回家去。"
    play sound audio.itemmed
    "我的药瓶突然从没有完全拉上的开口处掉出来。"
    "他似乎也注意到了。"
    show acolas normal_eyes normal_eyebrow awkward_mouth no_sweat with dissolve
    a"“那是什么？”"
    "我下身捡起瓶子。"
    $ss('no_hat white glasses normal2_eyes awkward_mouth normal2_eyebrow sweat')
    s"“补维c的，我有时候喜欢让嘴里有点酸味。”"
    $sh()
    "我并不想和别人坦白自己其实是个带病的异类这个事实。"
    show acolas normal2_eyes normal_eyebrow surprised_mouth sweat with dissolve
    a"“好吧。呃……其实我来找你肯定不只是来找你道歉的。”"
    $ss('no_hat white glasses normal2_eyes normal2_eyebrow sweat ques')
    s"“什么事啊？”"
    $sh()
    "我把药瓶塞进布包，确保拉锁拉到头了。"
    play music audio.allsfairinlove
    show acolas normal_eyes awkward_eyebrow smile_mouth sweat with dissolve
    a"“说起来，像你这样的独立写作者，还有编程的能力，没考虑过做个游戏什么的吗。”"
    "做游戏？我抬头看向他。"
    "这位技术总监倒是很有雅兴啊？不过我们也都这个岁数了，哪有什么精力去做大学生做的事呢。"
    $ss('no_hat white glasses normal_eyes sad_eyebrow scared_mouth')
    s"“…大学的时候确实有做过，花了一段时间，但是没什么人玩，一气之下就把项目都删了。”"
    $sh()
    "那时的我还真有毅力啊，顶着头疼——虽然没有现在那么疼——还能努力做出点东西来。"
    show acolas surprised_eyes surprised_eyebrow angry_mouth sweat with dissolve
    a"“哦？…那正好。”"
    "他突然靠近，以一种探求的目光注视着我的眼睛，仿佛要从我的脑壳里挖出点什么东西一样。"
    show acolas normal_eyes angry_eyebrow smile_mouth no_sweat with dissolve
    a"“要不要，加入我的游戏制作团队？和我做个游戏？就我们两个？”"
    "啊…这真的是一个上司会说出来的话吗？简直就像是你的高中班主任下课后不提作业，反而邀请你去他家里玩泥巴。"
    $ss('no_hat white glasses normal2_eyes awkward_eyebrow sad_mouth')
    s"“诶，我…”"
    $sh()
    "说真的，对于做游戏我倒还算有一点兴趣，但是…"
    "我的头疼病，在这种折磨下连完成每周的任务都十分艰难，真的还有额外的精力去陪他做游戏？"
    "我有些犹豫不决，但Acolas靠近到几乎要把自己压在桌子上。"
    show acolas angry_eyes angry_eyebrow angry_mouth sweat with dissolve
    a"“犹豫就会败北！”"
    a"“从你的眼中我已经看到了！你想和我做！”"
    show acolas angry_eyes angry_eyebrow angry_mouth sweat blush with dissolve
    a"“做——游戏！”"
    "他的身体越压越低，我能感觉到他那根柔软的阳具正压着我的小腹。"
    "他肯定是故意这么做的，想用美色诱惑我？呵呵！"
    $ss('no_hat white glasses closed_eyes angry_eyebrow angry_mouth mood')
    s"“不行哦——”"
    $sh()
    "我把手交叉，拦截在他即将亲到我脸上的他的脸的中间。"
    show acolas normal_eyes angry_eyebrow angry_mouth sweat no_blush with dissolve
    a"“即便是给我你的电话号也不行吗？”"
    $ss('no_hat white glasses normal_eyes normal_eyebrow angry_mouth sweat')
    s"“啊？这也能算作奖励？”"
    $sh()
    show acolas normal_eyes smile_eyebrow angry_mouth sweat no_blush with dissolve
    a"“那再加上——一顿火锅？”"
    $ss('no_hat white glasses sad_eyes normal_eyebrow angry_mouth sweat mood')
    s"“某宝上写程序的都没这么廉价！”"
    $sh()
    show acolas normal_eyes smile_eyebrow smile_mouth sweat blush with dissolve
    a"“那把我整个人借你一晚上～”"
    "在他说出这句话时，我能感觉到堆在我下腹上的他的那根东西向下移动，开始摩擦着我的那东西了。"
    "啊啊啊啊变态啊！虽然咱俩都是男同可这里还是公司啊！！"
    show acolas surprised_eyes awkward_eyebrow awkward_mouth sweat blush with dissolve
    $ss('no_hat white glasses angry_eyes normal_eyebrow angry_mouth anger blush mood')
    s"“我要你一晚上干什么啊！你个变态快爬啊！”"
    $sh()
    "似乎是戳到了他的痛处还是什么，他不再压在我的身上，回到站直的状态了。"
    "幸好他撤得早，自己的那话儿已经被他摩擦得快硬了。"
    show acolas normal_eyes normal_eyebrow normal_mouth sweat no_blush with dissolve
    a"“好嘛，怎么样才能让你同意呢？”"
    $ss('no_hat white glasses normal2_eyes normal_eyebrow awkward_mouth sweat')
    s"“我想知道…为什么非要选我？应该有很多人能力又强又很努力吧…”"
    $sh()
    "确实，这个才是最大的问题，我又没什么特别的，为什么他那么坚持？"
    $renpy.music.set_pause(True, channel='music')
    show acolas normal_eyes normal_eyebrow normal_mouth sweat no_blush with dissolve
    a"“因为…”"
    "难得看到这家伙扭捏起来。"
    show acolas normal_eyes normal_eyebrow normal_mouth sweat blush with dissolve
    a"“因为我……喜欢你。”"
    "这段声音波形经由他的声带发出，震动作为介质的空气，传播至我的鼓膜。"
    "接收到震动的听觉系统经过极为短暂的时间加工成电信号，通过钠离子和氯离子在神经细胞的进出的方式传播至最高中枢。"
    "最终在语言系统的帮助下被翻译成可以让我理解的实际的表达意义。"
    "身体第一个做出的操作便是控制全身的汗毛直立随后颤抖。"
    $ss('no_hat white glasses surprised_eyes surprised_eyebrow surprised_mouth sweat blush')
    s"“啊？…”"
    $sh()
    $renpy.music.set_pause(False, channel='music')
    show acolas normal_eyes normal_eyebrow angry_mouth no_sweat blush with dissolve
    a"“如果对你感兴趣的话，我觉得，促进感情最好的方式就是一起做事。”"
    show acolas normal_eyes awkward_eyebrow angry_mouth no_sweat blush with dissolve
    a"“同舟共济，互相帮助，一起向前，心心相印！”"
    $ss('no_hat white glasses angry_eyes angry_eyebrow angry_mouth sweat blush')
    s"“什么乱七八糟的东西！”"
    $sh()
    "可能是我的反射弧比地月距离还长的原因，脸颊这才开始变得发热。"
    "所以我终于也被人喜欢上了吗？还是这种有钱有能力有颜值的帅男人？"
    "怎么办怎么办，是该说“我每晚自慰都在意淫被你强奸的场面”还是“就现在快把你的大吊放进我的贝塔里”？"
    "不对啊我在想什么东西啊？"
    "我无意识地抓着头发，而他的神态则变得有些失落。"
    show acolas normal2_eyes normal_eyebrow normal_mouth sweat no_blush with dissolve
    a"“哎呦，吓到你了吧，我就说我的社交能力很差…”"
    "如果是平时，我一定能识破他这种行为有130\%的几率是在欲擒故纵。"
    "但脑内大量又无用的奇妙想法完全占据了可以思考的空间。"
    $ss('no_hat white glasses normal_eyes normal_eyebrow angry_mouth')
    s"“和你做游戏的话…我答应了！但是我有个条件。”"
    $sh()
    show acolas normal_eyes normal_eyebrow normal_mouth sweat no_blush with dissolve
    "好吧，谁让我没法拒绝这样一个完美的男人？"
    "不过做游戏肯定要花些精力的，如果还要忙太多工作的话我肯定会坚持不住的…"
    $ss('no_hat white glasses normal_eyes normal_eyebrow normal_mouth sweat')
    s"“就帮我做点我这边的工作好啦？对于你来说应该不难吧？”"
    $sh()
    show acolas surprised_eyes normal_eyebrow normal_mouth no_sweat blush with dissolve
    "他的眼神戏剧性地闪亮起来。"
    show acolas surprised_eyes awkward_eyebrow smile_mouth no_sweat blush with dissolve
    a"“就这么决定了！那待会我给你发我的某信号和手机号哦，我们先下班吧！”"
    stop music fadeout 5
    "他的尾巴摇来摇去的，像只被夸奖了的大狗一样。"
    "…"
    scene nightrun with fade
    "离开了公司。"
    "夏天的夜晚有些闷热。"
    "我看向身侧，路灯顶端的几何形灯罩中放射出温和的橘色光线，有几只看不清具体形状的飞虫围绕着光源转来转去。"
    "路边的绿化带上生着树木，看上去似乎已经活了几十年了。"
    "叶片被路灯也染上橘黄，颇有秋天的意味。"
    "远方漆黑的星空覆盖着这个世界的上空，但城市里并不能看到几颗星星。"
    "…他喜欢我…吗。"
    "我站定，深呼吸。"
    "如果是他陪自己一同下班，会是什么感觉呢？"
    "他会一边走一边开我的玩笑吗？或者在路上没人的时候突然索吻？"
    "一起看天空，看树叶，或者只是看着他。"
    "…"
    "为什么稍微有些难过呢？"
    "随之而来的便是折磨人的头痛。"
    $end_plot()
    if p.aco_p == 2:
        $p.aco_p = 3
    if replaying:
        jump afterreplay
    $p.times+=1
    jump TaskExecuting



label acolas_route_3:
    $ p.onOutside = True
    $start_plot()
    stop music fadeout 3
    scene hotpot with fade
    "我看着面前咕噜噜冒着泡的铜锅，把两只手放在蒸腾的白气中感受温度。"
    "透过白蒙蒙的水汽，我第一次看到了没有穿工作服的他。"
    play music audio.enjoymentoffood fadein 5
    show acolas vest necklace smile_mouth with dissolve
    "他穿着纯黑色微透的背心，加上偏灰的短裤，足底则是运动鞋。"
    "墨镜被他放在桌边，他的脖子上还挂着银白色的项链挂饰。"
    "平时的他在公司一直都是不变的工作服，但其实公司里并没有严格要求穿什么衣服。"
    "我在公司虽然也穿白衬衫，但只是因为不想显得太过突出罢了。"
    "裸露出来的臂膀结实而又健壮，很难想象那一身工作服下的他居然是这样的体型。"
    "也许他刚刚从健身房出来？我嗅了嗅，似乎并没有问到我想象中的汗味，只有火锅的辣油香。"
    "温暖的水汽带着热量穿过我的爪子，细密的小水珠在绒毛上聚成一团。"
    show acolas vest necklace angry_eyebrow smile_eyes smile_mouth with dissolve
    "我盯着铜锅中沸腾的红油翻腾，将我叫不出名字的软烂蔬菜从液体内部拽到表面，但却被便被对方用长筷子夹去，抢进他自己的酱料碗里。"
    "我抬头，看他一副得逞的样子。"
    "嗯…这种奇妙的感觉到底是什么呢。"
    "为什么我的心跳节奏变得混乱起来了？"
    "我摇摇头，虽然还想再吃点东西，不过好像也有点撑了。"
    "于是便把筷子放下，深吸一口气。"
    show acolas vest necklace smile_eyebrow normal_eyes smile2_mouth with dissolve
    a"“吃饱了吗？”"
    $ss('normal_eyes normal2_eyebrow')
    s"“如果不被人盯着的话，应该还能再吃点？”"
    $sh()
    show acolas vest necklace normal_eyebrow normal2_eyes surprised_mouth sweat with dissolve
    a"“谁看你啊，我才没看你。”"
    "我无意间笑了笑。"
    "但是我真的能够接受这一段新的恋情吗？"
    show acolas vest necklace normal_eyebrow normal_eyes surprised_mouth no_sweat with dissolve
    "我拿起筷子，在火锅里漫无目的地搅来搅去，试图捞出一块肉来。"
    "之前的我还想着试试谈恋爱，但真正遇到这种情况时，却让我有些不知所措。"
    "到底是哪里出了问题呢？"
    show acolas vest necklace normal_eyebrow normal2_eyes normal_mouth with dissolve
    a"“好吃吗？”"
    "我突然意识到我已经把筷子插进火锅汤里很久了，回过神来。"
    $ss('normal_eyes normal_eyebrow smile_mouth happy')
    s"“挺好吃的。”"
    $sh()
    show acolas vest necklace normal_eyebrow normal_eyes normal_mouth with dissolve
    a"“我经常来这家，每当我感觉特别疲惫的时候，就来点火锅吃。”"
    "我夹到一块香菇，放进碗里。"
    show acolas vest necklace normal_eyebrow normal3_eyes normal_mouth phoneon with dissolve
    a"“嗯…”"
    a"“感觉，吃火锅，最先想到的应该是辣和烫吧。”"
    show acolas vest necklace normal_eyebrow normal_eyes normal_mouth phoneoff with dissolve
    a"“说不定我就喜欢被这种辣口的感觉折磨，被火热的食物烫伤。”"
    a"“以这种方式来让自己好受点。”"
    "…什么？"
    show acolas vest necklace awkward_eyebrow awkward_eyes smile2_mouth no_phone with dissolve
    a"“噢，对不起，我自说自话了。”"
    show acolas vest necklace awkward_eyebrow awkward_eyes smile_mouth with dissolve
    a"“我去结账吧。”"
    $ss('normal_eyes normal2_eyebrow smile_mouth happy')
    s"“嗯…谢谢你请我吃饭。”"
    $sh()
    a"“不客气。”"
    "他起身，离开了桌子，随后便突然转头看向我。"
    show acolas vest necklace smile_eyebrow smile_eyes laugh_mouth with dissolve
    a"“还会有更多次的。”"
    hide acolas with dissolve
    stop music fadeout 5
    "我把沾了酱料稍稍变凉的香菇塞进嘴里。"
    "如果是空腹，可能会很好吃吧。"
    "但现在我已经很撑了，再好吃的肉到嘴里也只觉得油腻。"
    $ss('closed_eyes smile_eyebrow smile_mouth happy')
    s"“嗝——”"
    $sh()
    "这下是真的饱了。"
    "我把筷子横放在桌上，靠着椅背向后放松。"
    "他本身是邀请我来这里聊聊关于做游戏的事情的，但截止到现在都只像在约会一样。"
    "做游戏只是个幌子吗？还是他不好意思说呢…"
    "而且要是谈工作的话，怎么说也应该是在咖啡厅那样的地方吧…吃火锅更像是做完游戏的庆祝…"
    "Acolas回来了。"
    show acolas vest necklace normal_eyebrow smile_eyes normal_mouth with dissolve
    $ss('sad_eyes smile_eyebrow smile_mouth')
    s"“噢噢…没花费太多吧？”"
    $sh()
    show acolas vest necklace normal_eyebrow smile_eyes smile_mouth with dissolve
    a"“还好啦…”"
    "他挠挠头，坐回我对面。"
    "我还是不太相信，我真的对他那么有吸引力吗？他为什么会喜欢我呢？我们从刚认识到现在也才几周，难道只是因为我写过他的委托？"
    show acolas vest necklace normal_eyebrow normal3_eyes normal_mouth with dissolve
    a"“其实我不是很喜欢下班之后谈工作…什么的…”"
    show acolas vest necklace normal_eyebrow normal_eyes normal_mouth with dissolve
    a"“所以关于我想做的游戏，我就尽量简单地和你说好吧。”"
    $ss('normal2_eyes normal_eyebrow normal_mouth')
    s"“嗯…”"
    $sh()
    "是什么样的游戏呢？"
    play music audio.acolas
    show acolas vest necklace angry_eyebrow normal3_eyes normal_mouth with dissolve
    a"“我想做一款现代背景的游戏。”"
    a"“主角是个社畜，在现代社会努力工作，学习提升自己，最后赚很多钱的游戏，然后谈恋爱。你觉得如何？”"
    $ss('normal2_eyes normal_eyebrow normal_mouth ques')
    s"“只是赚钱恋爱吗？”"
    $sh()
    show acolas vest necklace angry_eyebrow normal_eyes awkward_mouth with dissolve
    a"“…嗯…其实我还没想好结局怎样写，但我确实挺想写一个工作相关的模拟经营类游戏。”"
    a"“分配每天的任务之类的…”"
    $ss('normal_eyes normal_eyebrow normal_mouth ques')
    s"“那岂不是每天都一样？”"
    $sh()
    show acolas vest necklace awkward_eyebrow awkward_eyes awkward_mouth with dissolve
    a"“是哦，那怎么办呢？”"
    $ss('surprised_eyes surprised_eyebrow normal_mouth em')
    s"“那就…每天都会出现不同的状态，遭遇不同的随机事件，需要分配不同的任务…你觉得如何？”"
    $sh()
    show acolas vest necklace surprised_eyebrow surprised_eyes awkward_mouth with dissolve
    a"“哦！…确实很有趣，不得不说你真的挺会做游戏的诶。”"
    $ss('normal_eyes normal_eyebrow smile_mouth')
    s"“小时候玩这种游戏比较多啦…”"
    $sh()
    show acolas vest necklace surprised_eyebrow surprised_eyes normal_mouth with dissolve
    a"“那结局该怎么写呢？”"
    $ss('normal2_eyes normal_eyebrow smile_mouth')
    s"“那就要看你想写的主角了。”"
    $sh()
    "我想到了曾经在某些论坛上看到的帖子。"
    $ss('normal_eyes normal_eyebrow normal_mouth')
    s"“给主角一个过去和未来，而且既然他是主角就一定得和别人不一样才行。”"
    $ss('sad_eyes normal_eyebrow normal_mouth')
    s"“不然大家都是社畜，上班的时候就已经很累了，玩游戏也要上班就太无聊了。”"
    $sh()
    show acolas vest necklace surprised_eyebrow smile_eyes smile_mouth with dissolve
    a"“[p.name]，你确实很会设计游戏，我就知道选你没错！”"
    "被他一夸我倒是突然有了热情。"
    stop music fadeout 5
    $ss('normal_eyes normal_eyebrow normal_mouth')
    s"“那么…如果他要比别人不同…”"
    $sh()
    "不同…哪里不同？…"
    "不同…我和别人就…不同…"
    "也许我可以…"
    $ss('normal2_eyes normal_eyebrow normal_mouth')
    s"“我突然有个点子。”"
    $sh()
    show acolas vest necklace surprised_eyebrow normal_eyes normal_mouth with dissolve
    a"“什么？”"
    "我深吸一口气。"
    play music audio.themedicine
    $ss('normal_eyes normal_eyebrow normal_mouth')
    s"“主角有一种头疼的怪病，需要购买昂贵的特殊药物治疗自己。”"
    s"“面对每天不同的情况，进行轻度或者重度工作以完成任务，用赚来的钱买药。”"
    $ss('normal2_eyes normal_eyebrow scared_mouth sweat')
    s"“如果没有药吃就游戏失败，如果主角因为频繁的工作头疼致死也算失败。”"
    s"“游戏的最后，主角努力赚钱还锻炼身体，从厌倦活着变得热爱生活，最后终于被医院治好！”"
    $ss('normal2_eyes normal_eyebrow smile_mouth no_sweat')
    s"“你觉得如何？”"
    $sh()
    show acolas vest necklace surprised_eyebrow surprised_eyes normal_mouth with dissolve
    "洋洋洒洒，我的想法从大脑的间隙中不停涌出，毕竟这就是我活到现在所真实经历的。"
    "他则会神地看着我，而后突然起身。"
    stop music fadeout 3
    show acolas vest necklace surprised_eyebrow surprised_eyes smile_mouth with dissolve
    a"“就这么做！”"
    show acolas vest necklace smile_eyebrow surprised_eyes laugh_mouth with dissolve
    a"“不愧是写小说的作家！这个想法确实很有趣啊！做成游戏也很适合，结局也很美丽！”"
    "这就是被肯定的感觉吗？"
    "至少我提出了这个想法，也许我再也不会质疑自己是否有资格和他共事了。"
    "我松了一口气。"
    play music audio.acolas fadein 3
    $ss('normal_eyes normal_eyebrow normal_mouth ques')
    s"“那么…我负责什么呢…？”"
    $sh()
    show acolas vest necklace smile_eyebrow smile_eyes smile_mouth with dissolve
    a"“嗯…其实我也偶尔写点东西啦，我觉得我们还是一起做同一个部分吧。”"
    a"“我们这两周先写游戏的底层程序代码，之后写剧情。”"
    show acolas vest necklace smile_eyebrow normal_eyes smile2_mouth with dissolve
    a"“这样一个小游戏的代码对你来说肯定不难吧？”"
    a"“你来搞定一部分代码，我去弄另一部分，然后再加上你的一些工作。”"
    "我点点头。"
    "游戏代码啊…看来今天晚上得查一查别人是怎么从头写起的了。"
    "他总是看起来很开心，至少对我一直笑着，但今天下午一定是他最开心的时候。"
    "我也很开心，也许是被认可的原因，也许是能与别人做一些有趣的东西，也许仅仅是因为他。"
    "这就是恋爱的感觉吧。"
    "我只觉得整个身体被什么东西填满了，轻飘飘的。"
    "我们以后说不定会有很多粉丝，再弄一些付费平台什么的…想想就很开心啊。"
    show acolas vest necklace smile_eyebrow normal2_eyes smile_mouth blush with dissolve
    a"“不要累到自己，我也会尽量做多一点帮你的。”"
    $ss('normal_eyes normal_eyebrow smile_mouth blush')
    s"“嗯…”"
    $sh()
    "我低头。"
    "被他关心了。"
    "真好啊。"
    "真想一直都这样开心啊，好像就连头也没那么疼了。"
    
    $end_plot()
    if p.aco_p == 3:
        $p.achievedGoal += r2(p.goal * 0.5)
        $AcolasItem2.add(p)
        $Notice.show()
        $AcolasTask1.unlock(p)
        $p.aco_p = 4
    if p.onOutside:
        $p.onOutside = False
    if replaying:
        jump afterreplay
    $p.times+=1
    jump TaskExecuting



label acolas_route_4:
    $start_plot()
    stop music fadeout 5
    scene office with fade
    "今天的会议结束得同样很晚。"
    "而我就像个马上要放学的中学生，在放学之前就把所有东西整理好。"
    "当然，明天又是新的假期，所以这种整理行为也倒是让人有些兴奋。"
    "…"
    "…Acolas，这周他才刚刚接手我们的项目，但他工作的时候总是让人觉得不太好接触。"
    "对代码的规范，一些效率的要求，还有技能的掌握要求都特别高。"
    "他也确实很厉害，懂得很多东西。"
    "同事们写不出来的东西，交给他就好。"
    "他写出来的东西总是优雅又规范，同时还特别有效率。"
    "听别人说他年纪轻轻就考取了软件专业的研究生，成绩还十分出色。"
    "就是这样一个别人家的孩子，居然就在我身边，真是不可思议。"
    "可是他私下却又是这样的。"
    "不过我的同事们并没有发现这一点，仍在午饭期间一边说些花痴的话一边乐得十分刺耳。"
    "我也不希望他们知道就是了。"
    "…"
    "同事们似乎已经习惯了我周五之前总要比他们更晚一点回去的行为，我大概也已经习惯多在这里待一会了。"
    "是的，我在等他。"
    "即便可以去他的办公室直接等他开完剩下的会，但是在我的工位边偷偷密会似乎变成了我们之间的某种仪式。"
    play music audio.acolas
    show acolas smile_eyebrow smile_eyes smile_mouth sweat with dissolve
    a"“嘿，[p.name]。”"
    "被他突然的说话声吓了一跳，我转头看向这只灰狼。"
    $ss('no_hat white glasses surprised_eyebrow normal2_eyes surprised_mouth')
    s"“啊，你来啦。”"
    $sh()
    show acolas surprised_eyebrow smile_eyes normal_mouth sweat with dissolve
    a"“那个，关于我们上周说要做的游戏…我定的计划是两周吧…”"
    $ss('no_hat white glasses normal_eyebrow normal2_eyes normal_mouth ques')
    s"“是啊，怎么了…”"
    $sh()
    "真正尝试去做一款这样数据量十分大的养成游戏确实很花精力…也许对于我来说两周也根本不够用，即便在工作量减轻的基础上。"
    show acolas surprised_eyebrow smile_eyes smile_mouth sweat with dissolve
    a"“不知道你有没有检查我们的网上代码仓库呢？”"
    $ss('no_hat white glasses scared_eyebrow normal2_eyes normal_mouth ques')
    s"“没有啊，不会是丢文件了吧…”"
    $sh()
    show acolas smile_eyebrow smile_eyes smile2_mouth blush with dissolve
    a"“其实我在今天中午午休无聊的时候，已经把所有的代码都写完了。”"
    $ss('no_hat white glasses surprised_eyebrow scared_eyes scared_mouth')
    s"“啊…”"
    $sh()
    "我呆住了。"
    "他确实很厉害，也很有能力，但这个速度…也太快了吧？"
    "那么多代码…那么多东西…他怎么就…"
    $ss('no_hat white glasses normal_eyebrow normal_eyes scared_mouth sweat')
    s"“这…这…这么快啊…那…辛苦了…”"
    $sh()
    show acolas smile_eyebrow angry_eyes surprised_mouth blush sweat with dissolve
    a"“其实没多少东西啦，而且我也在代码平台找到了差不多的游戏，借鉴一下…随随便便就写好了啦！”"
    "即便他这么说我还是不相信他真的能这么快，难道说他就是神？"
    $ss('no_hat white glasses normal_eyebrow normal2_eyes normal_mouth sweat')
    s"“啊…那…我们是要进行游戏的第二部分了吧？…”"
    $sh()
    show acolas smile_eyebrow angry_eyes normal_mouth no_blush sweat with dissolve
    a"“是这样，不过我打算先休息一周。找点时间测试一下我写的代码，然后再修一修。”"
    $ss('no_hat white glasses scared_eyebrow normal2_eyes normal_mouth ques')
    s"“测试不也挺累的吗，那也算休息？”"
    $sh()
    show acolas smile_eyebrow normal_eyes laugh_mouth sweat with dissolve
    a"“你不用担心我啦！自从做了这个游戏之后，我感觉年轻了好多啊，精力十足！休息的时候都在想测试用例怎么写呢。”"
    "…工作狂。"
    "这真的没问题吗？不过既然他一直说没问题的话…也不用多管闲事吧…"
    $ss('no_hat white glasses normal_eyebrow normal_eyes smile_mouth sweat')
    s"“好吧，那我就等你下周再听你和我讲讲怎么写文案咯？”"
    $sh()
    show acolas smile_eyebrow normal_eyes smile2_mouth no_sweat with dissolve
    a"“嗯。那我就先回去了。”"
    $ss('no_hat white glasses normal_eyebrow normal2_eyes smile_mouth blush')
    s"“下周见。”"
    $sh()
    stop music fadeout 5
    if p.aco_p == 4:
        $p.aco_p = 5
        if AcolasItem2.has(p):
            $AcolasItem2.get(p).remove(p)
    
    $end_plot()
    if replaying:
        jump afterreplay
    $p.times+=1
    jump TaskExecuting


label acolas_route_5:
    $ p.onOutside = True
    $start_plot()
    stop music fadeout 5
    scene acocafe with fade
    play music audio.enjoymentoffood fadein 3
    "今天会议结束得很早，于是在下班之后，就被这只灰狼强行拽到他的车上去了。"
    "他开车，载着我来到了这个地方。"
    "眼前的偏古典装修的店面顶端的木牌写着“COFFEE CAMPSITE”，门边便是一面分割成许多大正方形的玻璃窗，能从这里看到里面的靠窗座椅以及咖啡桌，还有旋转楼梯，以及一点点二楼的空间。"
    lady "“欢迎光临咖啡营地。”"
    "服务员开口，我点头示意便跟着Acolas往里走。"
    show acolas vest necklace normal_eyebrow normal_eyes smile_mouth phoneon with dissolve
    a"“我经常坐靠窗那个位置，虽然二楼也不错，但是信号很差。”"
    $ss('scared_eyebrow awkward_eyes smile_mouth')
    s"“那就这里吧。”"
    $sh()
    "Acolas似乎很喜欢找个地方约会的同时聊我和他之间的工作。"
    show acolas vest necklace normal_eyebrow normal3_eyes awkward_mouth phoneoff with dissolve
    a"“我已经提前点好单了。”"
    $ss('scared_eyebrow normal2_eyes normal_mouth')
    s"“点了什么？咖啡馆只能喝咖啡吧。”"
    $sh()
    show acolas vest necklace smile_eyebrow angry_eyes laugh_mouth no_phone with dissolve
    a"“哼哼，当然是各种甜点。”"
    show acolas vest necklace angry_eyebrow angry_eyes surprised_mouth with dissolve
    a"“如果你早上来的话，他们这里还供应早餐呢。”"
    "想起自己早餐不是吃点便宜面包糊弄一下，就是点外卖，此刻真是深知自身与别人之间的贫富差距。"
    show acolas vest necklace normal_eyebrow normal3_eyes normal_mouth phoneon with dissolve
    "Acolas坐在了我的对面，开始盯着他掌心的手机，似乎在看什么文章。"
    $ss('agony_eyebrow normal2_eyes smile_mouth')
    s"“那挺好的…”"
    $sh()
    "按照上次的情况来说，Acolas在吃过饭后才会开口谈工作，但现在我们的桌子上还没有任何东西端过来。"
    "而他也是一言不发。"
    "有些尴尬，他就只看手机？这还算是约会吗？……我还是说点什么吧。"
    $ss('sad_eyebrow normal_eyes smile_mouth')
    s"“那个，以前的总监，不知道你听没听别人说过。”"
    $sh()
    show acolas vest necklace normal_eyebrow normal_eyes normal_mouth phoneon with dissolve
    "他的视线从他的手机转向我。"
    $ss('awkward_eyebrow normal_eyes smile_mouth')
    s"“那家伙总是摆着个臭脸，让我们干这干那，他啥也不干，就算干也只是一点简单的活。”"
    $ss('angry_eyebrow awkward_eyes sad_mouth')
    s"“说实话，真不知道他是怎么当上总监的。”"
    $sh()
    show acolas vest necklace normal_eyebrow normal_eyes normal_mouth phoneoff
    "我呼气，不自觉地微笑着。"
    $ss('surprised_eyebrow normal2_eyes smile_mouth')
    s"“不过你来之后，总觉得有希望了。”"
    $ss('awkward_eyebrow normal2_eyes smile_mouth')
    show acolas vest necklace surprised_eyebrow normal_eyes surprised_mouth phoneoff with dissolve
    s"“仅仅只是一周的工作，就让我们几个意识到，你来之后，让我们的项目进展变得顺利又流畅。”"
    $ss('scared_eyebrow sad_eyes smile_mouth')
    show acolas vest necklace surprised_eyebrow surprised_eyes surprised_mouth phoneoff with dissolve
    s"“很感谢你，真的。”"
    $sh()
    "我看着他淡红色的瞳孔。"
    "平时的我并不会看着别人的眼睛，但只有看向他时我才没有那么紧张。"
    "他有些吃惊，又或者是惊讶，随后又变化成沉思的表情。"
    show acolas vest necklace surprised_eyebrow surprised_eyes normal_mouth no_phone with dissolve
    "他的眉头紧缩，之后很快舒张。"
    "沉默着，他突然松了一口气一般，叹气，然后终于抬起目光，与我交汇。"
    show acolas vest necklace surprised_eyebrow normal_eyes surprised_mouth sweat with dissolve
    a"“没什么，我只是做了我应该做的而已…”"
    $ss('normal2_eyebrow normal_eyes smile_mouth')
    s"“你真的帮了大忙。”"
    $sh()
    show acolas vest necklace surprised_eyebrow normal_eyes normal_mouth sweat blush with dissolve
    a"“搞得我怪难为情的，看着项目一点点完善，我也很开心。”"
    "他确实很开心，从他的表情就能看出来。"
    "他似乎并没有意料到我会和他道谢，所以才会那样吧。"
    "他看上去开心点了。不过他之前好像一直都很开心的样子来着啊？"
    hide acolas with dissolve
    "两杯咖啡被端上来，还有一盘慕斯蛋糕。"
    "突然想起自己在小的时候，每次路过蛋糕店都会盯着里面的大蛋糕，但因为家里太穷，能买一个小小的解馋就很不错了。"
    "即便工作之后，也舍不得买大蛋糕给自己吃，甚至小蛋糕都没再买给自己了。"
    "至少我眼前的这个蛋糕比我吃过的所有蛋糕都大。"
    "我用勺子挖了一块奶油，放进嘴里。"
    "不只是甜，奶油的味道，水果的味道，还有一丝巧克力的口感。"
    "…"
    "啊…"
    show acolas vest necklace smile_eyebrow surprised_eyes smile_mouth with dissolve
    a"“很好吃吧？”"
    $ss('normal2_eyebrow normal_eyes smile_mouth happy')
    s"“嗯。”"
    $sh()
    "我又挖了一勺，而他则对他的那杯咖啡更感兴趣。"
    show acolas vest necklace smile_eyebrow surprised_eyes laugh_mouth blush with dissolve
    a"“你喜欢就好，下次再多点一份吧。”"
    $ss('surprised_eyebrow surprised_eyes smile_mouth happy')
    s"“…啊…这肯定很贵吧…”"
    $sh()
    "这倒是突然让我想起价格的事了，即便每次都是他请我，但还是对价格好奇。"
    show acolas vest necklace surprised_eyebrow normal2_eyes smile2_mouth no_blush with dissolve
    a"“五六十吧，还好。”"
    "这么一块蛋糕五六十啊…够我吃两天的盒饭了…"
    $ss('scared_eyebrow sad_eyes smile_mouth')
    s"“…感谢你请我吃…小的来生肯定补上……”"
    $sh()
    show acolas vest necklace surprised_eyebrow normal_eyes smile_mouth with dissolve
    "我就着咖啡吃了一口，蛋糕的甜味中和了咖啡的苦，或者说这咖啡本来就没有我想的那么苦。"
    "大概是他没给我点苦的咖啡吧。"
    "这么想来，我突然感觉心在狂跳。"
    "…"
    stop music fadeout 5
    scene nightrun with fade
    "离开咖啡馆前，我和他的桌子上只剩下两个空杯子，和一个带着奶油渍的空瓷碟。"
    "他一边小口酌饮他的咖啡，一边和我交代完了接下来两周需要写的剧情，就像我和他在火锅店时那样。"
    "但这次我没有和他提出请他分摊我的工作这件事。"
    "毕竟他上一次已经分摊了我的工作，而且还一个人以极快的时间造成了两个人的工作。"
    "如果他这次还写得那么快，我还要他分摊工作的话，他的身体肯定吃不消的。"
    "伤脑筋，熬过接下来这两周就好了。"
    "如果他的游戏能做出来的话，我和他一定都会很开心吧。"
    "这款游戏就像是我和他的孩子一样，但…"
    "算了，我这次努力干活的话，我就不会那样想了…"
    $end_plot()
    if p.aco_p == 5:
        $p.aco_p = 6
        $AcolasItem3.add(p)
    if p.onOutside:
        $p.onOutside = False
    if replaying:
        jump afterreplay
    $p.times+=1
    jump TaskExecuting






label acolas_route_6:
    $start_plot()
    stop music fadeout 5
    scene meeting with fade
    "意外的是Acolas没有出席这周的会议，到底发生什么事了…"
    "今天上午的时候还有看到他，难道他今晚有事要做吗？"
    "…"
    scene office with fade
    "我看向窗户。"
    "安静的工作区内只有我。"
    "空调在其他人离开的时候就已经被关上了，闷热的环境让人觉得十分痛苦。"
    "尤其是这种寂寞的环境之中，那折磨人的头疼便会更甚。"
    "从内核持续向外辐射痛苦，整个大脑像是从内部被螺旋刀片打成浆糊。"
    "待会给他发某信问问他怎么回事吧…"
    $end_plot()
    if p.aco_p == 6:
        $Message.new(p, 'Acolas', 'Acolas', '在吗……\n我忘记和你说了，我因为最近着凉了，现在在医院输液，如果你想来的话，明后天的下午可以来市立医院看望我一下……\n我就在住院部的324号房间。')
        $p.aco_p = 7
    if replaying:
        jump afterreplay
    $p.times+=1
    jump TaskExecuting


label acolas_route_7:
    $ p.onOutside = True
    $start_plot()
    stop music fadeout 5
    scene hospital with fade
    "我来到了这里。"
    "A市市立医院，我们已经是老朋友了。"
    "但这次我并不是为了取药，而是为了别人。"
    scene hospital_corridor with dissolve
    "消毒水的气味就像扎根在鼻腔里一般令人犯呕，但医院作为汇集了整个城市的细菌病毒感染源的地方，他们不这么做也没什么别的办法了。"
    "我的脚踩在瓷砖地板上，即便我并没有用多大力气去走，但寂静的走廊像是将我的脚步声以回音的形式放大了数倍。"
    "我该对他说些什么？"
    "“怎么生病了？这两天没来公司我很担心你！”"
    "不不，这不就是想要他回去工作吗？难道在我心里他就只有工作的价值？"
    "“生病了就好好休息吧，不要再想公司的事了…”"
    "…也不对，难道他不知道要好好休息吗？"
    scene door with dissolve
    play music audio.lostinthought fadein 5
    "两侧的门的标识上的门牌号在我的前进中逐渐变大，他所在的324房就在前面了。"
    "我停在那间房门前。"
    "房门上没有玻璃，也没有什么洞之类的能让我看到里面。"
    "我抬起手，准备敲门，却又开始犹豫了。"
    "我应该作为什么身份来见他呢？"
    "他的同事？毕竟Arnel也不知道他得了什么病，只知道他请假了。不过既然都住院了，肯定不是什么感冒之类的小病吧？真的需要我来看望吗？"
    "…不对，我…我是他的恋人啊…他喜欢我…我也…喜欢他，那我来看他也是很正常的，毕竟我担心他…"
    "我敲了敲门。"
    "很难想象在如此现代化的城市中，住院部的内部还没有升级，仍然沿用了几十年前的老建筑。"
    "颇显老旧的瓷砖花纹，甚至门都是木头做的。"
    "半晌都没有回应。"
    "我试着推开门，很容易地推开了。"
    scene ward with dissolve
    "房间里有很多病床，但只有一张床被占用着，从被子中露着灰色的头，两只耳朵耷拉着的狼便是他。"
    "他闭着眼，躺在床上，连眼角也不像平时那样紧促着。"
    "是啊，他肯定喜欢比平常人做的更多吧？"
    "本来应该是我和他一起完成的游戏制作，却都被他做了不少，更别说他还包揽了不少我自己的工作，再加上他自己作为技术总监的任务。"
    "也许他以为自己能力出众，但这些工作还是压垮了他。"
    "我突然想，或许他平时可能只睡四五个小时，否则他现在怎么会睡得如此香？"
    "我关上门，看到从窗户吹进来的风，将让他身上的毛发吹得摇晃起来。"
    "睡觉不关窗会感冒的吧…"
    "我走到窗边，将打开的窗户关上。"
    "从这里也能看见医院院子内的风景，还有他们栽种在花坛上的花。"
    "我以前甚至都没注意过那些花。"
    "我晃晃脑袋。"
    "Acolas真的需要好好休息，即便我尽量轻手轻脚，但发出来的响声应该也能将他吵醒吧。"
    "但他还是睡着，像什么都没发生一样。"
    stop music fadeout 7
    "我走到床前，看着他的脸。"
    "这只灰狼作为一个雄性，不仅长相英俊，能够在雌性兽人中获得关注，还有出众的能力。"
    "而我算什么呢？他交付我的任务我都完不成，甚至还害他操劳过度，让他躺在病床上了，可能我真的不配做他的恋人吧。"
    "或许他在我第一次让他失望的时候，他就已经对我失去兴趣了，只不过他还想看我表现，或者碍于面子没说吧。"
    "但我…我已经无可自拔地爱上他了。"
    "我没法解释这种感觉，只是我…"
    "我深呼吸。"
    "强势的他终于不堪重负，躺在了这病床上。"
    "沉睡的他几乎是任人宰割了，因为现在我想对他做什么都行。"
    "我想，我想做什么呢？"
    "我站在他的床边，看着他，心跳逐渐加快。"
    "我拉下自己的裤子。"
    "没人在乎房间里是否有监控，也没人在乎他是否会醒来。"
    "我勃起的阳物就在自己的手中发热。"
    play music audio.masturbation
    "我的手握住顶端，揉搓挤压，看着龟状的头部钻出我的包皮，随后又随着我的动作收回。"
    "我这样摩擦着我的下体，为什么？"
    "我为什么要这样做，为什么在这个地方？"
    "Acolas…"
    "是欣赏这样的落差吗？强大的他，在我心里无可匹敌的他，现在躺在病床上，不能动，需要照顾，需要我为他关窗，需要我照顾他。"
    "我加快手上的动作，否则快感无法满足我迅速上升的渴求。"
    "我不让呻吟溢出唇齿，只是在嗓子内发出低吟。"
    stop music
    "精液被我的左手接住。"
    "如此以来，这代表着我们的关系更近一步了吗？"
    "我看着手中的乳白污渍，又看了看仍然睡着的他，随后闭眼，体会血液中流动的多巴胺。"
    "突然有一种，自己并不属于这里的分离感。"
    "我用纸擦干了手心，穿好了裤子，慌张地，仿佛有谁追赶着我一般地，逃离了这个地方。"
    $end_plot()
    if p.aco_p == 7:
        $Message.new(p, 'Acolas', 'Acolas', '我刚睡醒就看到你正好从我的病房里跑出去，我叫你你没听见……\n总之谢谢你来看我，我差不多下周就能出院了。', pos='b')
        $p.aco_p = 8
    if p.onOutside:
        $p.onOutside = False
    if replaying:
        jump afterreplay
    $p.times+=1
    jump TaskExecuting


label acolas_route_8:
    $start_plot()
    stop music fadeout 5
    scene acohall with fade
    "眼前这栋高等公寓和我自己租的房子相比简直是一个天一个地。"
    "只需要和前台服务生说一下自己是受他的邀请，他们便将表情从平淡转换为笑容，甚至给我端了一杯气泡水。"
    "我麻木地端着杯子随着他们的带领走进了电梯。"
    play music audio.infrequenttranquility fadein 5
    scene acomoun with dissolve
    "随着电梯一层层的慢慢升起，光线逐渐照射了进来，这是一座观光电梯。"
    "如果说什么地方能看到一个城市发展的景象，那么高空绝对是独一无二的选择。"
    "这栋公寓处在市中心旁边，在我们超过十八层之后，周围就再也没有建筑能遮挡我的视线了。"
    "放眼望去，拔地而起的建筑后是连绵的青色山脉，与天空的蓝连接，如同色盘中两种颜料混合成的渐变。"
    "如果Acolas在身边我大概会然后摇着他的手臂然后问他“你为什么这么有钱？”"
    "但就算这个按电梯的人不在这里，我可能也没有胆量和脸面那么做。"
    "今天晴空万里，希望Acolas的病能早点好起来。"
    "…"
    scene black with fade
    "到了Acolas的房间门前。"
    play sound audio.knocktable
    "我敲了敲门，听到屋内传来脚步声，在他开门后，我终于来到了他的家里。"
    scene black with dissolve
    play sound audio.door
    show acolas vest2 surprised_eyebrow normal_eyes smile2_mouth sweat with dissolve
    "Acolas在与我的视线交汇后，勉强挤出了个笑容。"
    "这对生病的他来说肯定十分艰难。"
    $ss('normal2_eyebrow normal2_eyes')
    s"“嘿…那个…你生病了…所以我来…看望你一下…”"
    $sh()
    show acolas vest2 surprised_eyebrow normal2_eyes smile_mouth with dissolve
    a"“感冒而已…不小心被风吹到了…进来吧。”"
    play sound audio.door
    scene acohome with dissolve
    "走进屋子里才意识到，自己居然是空手来拜访他的，如果看望别人生病的话，怎么说也应该买点苹果给他？"
    "但一想到他是有多么有钱，那苹果这种东西或许连他家里的垃圾桶都不配吃。"
    "他的客厅十分空旷，右侧便是能从三十一楼俯视风景的巨大落地窗。"
    "能看见穿过a市的河流，上方高架桥密集的车流。"
    "被树林填满的公园，还有其他偏低一点的房屋。"
    $ss('awkward_eyebrow awkward_mouth')
    s"“抱歉什么都没买给你…我…”"
    $sh()
    "我低头，突然瞄到客厅的角落，堆了一大堆花里胡哨的礼品盒和果篮。"
    show acolas vest2 awkward_eyebrow normal3_eyes awkward_mouth with dissolve
    a"“你也看到了，我其实不需要那些东西啦…”"
    show acolas vest2 smile_eyebrow smile_eyes smile2_mouth with dissolve
    a"“你能来我看我就很开心了。”"
    "我抬头。他不像平时那样意气风发了，眼角也罕见地出现了黑眼圈。"
    "不过Acolas的衣品似乎并不是很好，也许这就是他一直在公司穿工作服的原因吧，眼前的他这一身就像工地收发室的摇蒲扇大爷。"
    stop music fadeout 5
    $ss('surprised_eyebrow normal2_eyes sad_mouth sweat')
    s"“啊…啊…那个，我觉得你最好先去休息吧？至少躺在床上…而不是和我在客厅里…”"
    $sh()
    "突然意识到自己正在占用这位病人的休息时间，我轻推他的身体。"
    show acolas vest2 surprised_eyebrow normal_eyes normal_mouth with dissolve
    a"“你想来我的卧室？”"
    $ss('awkward_eyebrow sad_mouth scared_eyes sweat blush')
    s"“卧室！…不是，我就是觉得，生病了应该多休息！…我没想别的！”"
    $sh()
    show acolas vest2 smile_eyebrow normal_eyes laugh_mouth with dissolve
    a"“跟我来啦，带你看看我的卧室。”"
    "他看向我，牵着我的手。"
    "他的掌心很热，可能是因为他已经发烧了的原因。"
    $Erection.add(p)
    "我感觉自己硬了，不仅仅是因为他牵着我的手，更因为是要和他这样走进他的卧室。"
    "他能在公司对我做出那些事，要是和他在他的卧室独处…"
    "……"
    play sound audio.door
    scene acobed with dissolve
    "我跟着他来到了他的卧室。"
    "他的卧室很干净，不过如果是他的话，也正常。"
    "一个十分有逻辑性又很有能力的人的卧室就不可能乱七八糟的。"
    "除此之外，他的桌子上摆着很多我认不出人物的立牌，手办之类的东西，墙上挂着角色的挂画。"
    "我并没有看太多动漫或是漫画，看来我没法在这方面和他聊些什么…"
    "不过我可以问一问他的推荐。"
    show acolas vest2 surprised_eyebrow normal3_eyes surprised_mouth with dissolve
    a"“你对我的手办很感兴趣吗？喜欢哪个？”"
    play music audio.heartbeat fadein 5
    $ss('sweat blush')
    s"“只是随便看看…我其实没怎么接触过这些东西…”"
    $sh()
    show acolas vest2 normal_eyebrow normal_eyes laugh_mouth with dissolve
    "我只觉得心脏一直在以从未有过的速度跳动，血液深处的某种激素似乎在煽动着我去与眼前的人做些什么。"
    "头部毛发间的深处正分泌出汗液，我能感觉汗珠正随着重力向下坠落，打湿其所经过的路径，直到脸侧。"
    "甚至我的脸侧也因为这种感觉而变得火热起来。"
    "下体的鼓胀让人感到不适。"
    menu:
        "幻想他的裸体":
            "如果眼前的人脱掉衣服会是什么样的？"
            show acolas shorts2 with dissolve
            "他的腹肌摸起来如何？那久经锻炼的胸肌捏上去是否如棉花糖般柔软？他的……下面呢？"
            show acolas naked with dissolve
            "在他内裤之中的巨物一定很大，非常大。"
            show acolas naked erect at look
            "那东西一定散发着浓烈的雄性的气味，前列腺液积蓄在马眼上，已经做好进行交配之前的万全准备。"
            "我要脱掉裤子吗？然后再请求吮吸他的下体？毕竟他也是我的“同类”，应该会同意的吧？会吧？"
            "呼吸急促，我几乎思考不了，也没法专注于他在问什么。"
            show acolas vest2 soft at look_
            "我的幻想戛然而止，我再次回到了现实。"
        "丢掉这个想法":
            pass
        
    "我站在他的床边，而他则坐回他的床上。"
    "那张床看上去又大又软…如果我和他在这张床上…"
    "没错，我应该找个机会，我要和他……我已经幻想过很多次了……我必须……"
    $ss('scared_eyebrow normal2_eyes blush')
    s"“但是…那个…你最喜欢的动漫是什么…有机会的话我会去看看的！”"
    $sh()
    stop music
    show acolas vest2 angry_eyebrow normal_eyes normal_mouth with dissolve
    a"“其实，除此之外更重要的是，我更关心你的文案写的如何了。”"
    $Erection.clearByType(p)
    "我突然一惊，仿佛全身的血肉都收缩起来，连带那东西也一起萎掉了。"
    "就像开学前一天，你写好了所有作业，但突然想起有一本极多的作业一点没动的感觉。"
    "也许我说错了什么话？还是用错了词？还是在他们圈子里这样提问是有问题的？"
    $ss('sad_eyebrow normal2_eyes angry_mouth')
    s"“可是！可是你都病倒了，就先关心一下自己的病吧！…游戏什么的等你好了再弄不好吗？”"
    $sh()
    play music audio.lostinthought fadein 5
    show acolas vest2 angry_eyebrow smile_eyes awkward_mouth with dissolve
    a"“这么说就是和上次一样一点没写咯？”"
    $ss('scared_eyebrow agony_mouth sweat')
    s"“我上次也不是一点没写啊！这次我也写了一些但是…你再多给我一些时间吧，因为你生病所以我…”"
    $sh()
    show acolas vest2 angry_eyebrow smile_eyes angry_mouth with dissolve
    a"“就是因为我生病了你才更应该多写一点吧？我这么努力结果你就这样对待我？等着我把所有东西做完？”"
    $ss('surprised_eyebrow normal2_eyes angry_mouth sweat')
    s"“不是…我…我们真的可以慢慢来的，这又不是工作，更何况你还病倒了，我们就不能…”"
    $sh()
    show acolas vest2 frown_eyebrow closed_eyes normal_mouth with dissolve
    a"“不不不…这不是借口。”"
    show acolas vest2 angry_eyebrow normal_eyes normal_mouth with dissolve
    a"“你知道我为什么生病吗？你知道我没日没夜写代码是什么感觉吗？”"
    show acolas vest2 angry_eyebrow smile_eyes awkward_mouth with dissolve
    a"“我有几天一直到凌晨四点都没睡，写这个游戏写到天亮，写到头昏脑胀。”"
    show acolas vest2 angry_eyebrow smile_eyes angry_mouth with dissolve
    a"“而你呢？就算你能力不如我，也能帮我打打下手吧？那么长时间了居然一点有用的东西都没写出来。”"
    show acolas vest2 angry_eyebrow angry_eyes angry_mouth with dissolve
    a"“只有我一个人在干活。”"
    $ss('sad_eyebrow angry_mouth sweat')
    s"“不是…我…我努力了…可是真的没必要给我们的项目设置死线啊，有谁急着要玩我们的游戏吗？”"
    $sh()
    show acolas vest2 angry_eyebrow normal3_eyes angry_mouth sweat with dissolve
    a"“我真的很想快点做出来，你感觉不到吗。”"
    show acolas vest2 smile_eyebrow awkward_eyes angry_mouth sweat with dissolve
    a"“甚至我都猜到你会这样了，我在出院之后就已经把需要的文本都写得差不多了。”"
    show acolas vest2 normal_eyebrow normal3_eyes normal_mouth no_sweat with dissolve
    a"“本来我想着参考一下你写的东西完善一下，但你连文本都拿不出来，还是算了。”"
    $ss('sad_eyebrow normal2_eyes sad_mouth sweat')
    s"“…我…”"
    $sh()
    "我确实没有完成他给给予我的任务，而他不仅帮我完成了额外的工作，还经常请我吃饭。"
    "我怎么会这么没用。"
    show acolas vest2 frown_eyebrow closed_eyes angry_mouth no_sweat with dissolve
    "他突然开始剧烈咳嗽起来，像是要把肺吐出来一样。"
    $ss('scared_eyebrow scared_eyes scared_mouth')
    s"“Acolas！”"
    $sh()
    show acolas vest2 smile_eyebrow normal_eyes normal_mouth no_sweat with dissolve
    a"“你回去吧，我想一个人好好休息一会。”"
    $ss('sad_eyebrow sad_mouth tear')
    s"“我…对不起…我下次一定会…认真的…我一定…尽力…尽全部的力…”"
    $sh()
    show acolas vest2 smile_eyebrow normal2_eyes normal_mouth no_sweat with dissolve
    a"“别说了…回去吧，我没生你的气，我只想一个人呆一会，你不明白吗？”"
    "没生气是不可能的，但我也没理由再呆在这里了。"
    "他并没有看我。"
    stop music fadeout 5
    "我低头，离开了这个地方。"
    scene black with fade
    "…"
    "是我的错…吗？"

    $end_plot()
    if p.aco_p == 8:
        $AcolasTask2.lock(p)
        $AcolasTask1.lock(p)
        if AcolasItem3.has(p):
            $AcolasItem3.get(p).remove(p)
        $p.aco_p = 9
    if replaying:
        jump afterreplay
    $p.times+=1
    jump TaskExecuting



label acolas_route_9:
    $start_plot()
    stop music fadeout 5
    scene office with fade
    "一切都回到了起点。"
    "Acolas大概是真的对我失望透顶了吧。"
    "我连给他发个消息的勇气都没有，而他到了周五也仍然没能回到公司。"
    "他都已经累倒了，还要在病床上写东西。"
    "我不理解为什么他一定要如此卖力，在他这样既有名气又有地位还不愁吃喝的人的生命中，真的有什么事是重要的吗？"
    "…"
    "我望着工位上的一堆文件夹，抬头靠在工位上伸了个懒腰。"
    "我很喜欢听这种骨骼滑腔空隙间气泡炸裂的声音，就像把已经错位的骨头靠这种方式恢复成正常的形态。"
    "也是一种奖励——是你长期摧残这具身躯没有休息之后，骨骼之间的哀哭。"
    "代表你确实有在工作，在疲劳，在消磨生命。"
    "即便这些只是我的想象，但毕竟这样做总是非常爽。"
    "虽然每周会议大部分时间都在展示领导们的工作能力，外加提出一些增加工作难度的奇思妙想。"
    "但我并不算特别讨厌这种就算滑手机也不会被计较的会议。"
    "而在Acolas来之后，会议很明显变了另一种性质——内容大多变成了他展示自我的空间，他的想法又数不胜数。"
    "大家的工作变得忙碌，逐渐充实起来，我们所做的事变得更有意义。业绩越来越好，奖金也变多了一点。"
    "而他不在的会议，就像失去了主唱的摇滚乐队。"
    "会议重新变得陈词滥调，大家似乎都在等着那个侃侃而谈的背影，站在投影仪边指着柱状饼图。分析这周的公司财报和未来趋势。"
    "比起Acolas，现在上台的人明显力不从心——他们没法做出Acolas那种井井有条的规划，也不能满足所有参与者的期望。"
    "在座的各位看起来都昏昏欲睡，本来还站着的公司领导抬起了他的茶缸润了润嗓子，接着可谓是瘫倒一般滑倒在座位上面。"
    "眼睛左右扫视了我们一圈时候摆了摆手，终于说出了散会二字。"
    "杂乱的脚步声逐渐响起，我收起面前什么都没写的笔记随着人流回到了自己的工位上。"
    "我和他之间的关系，就结束在这里了吗？"
    "我突然想起大概两个月前，同一个位置，同一个时间段。"
    "我做着同样的事——在我整理这些剩下的文件时，那只活泼的狼就这样出现在我的身边。"
    "活泼…这个词现在也许不能用来形容他了。"
    "他变得憔悴，疲惫，甚至喜欢发火。"
    "到底是因为这就是他本来的样子，还是因为我没法让他满意？"
    "……"
    "果然我已经喜欢上他了啊，即便他那样对我，我还是在挂念着他。"
    "…"
    show acolas normal2_eyes with dissolve
    a"“嗨。”"
    "我回头。"
    "这就是我所期待的吗？我已经完全沉浸他对他的爱中了吗？这就是真正的爱吗？"
    "要求，支配，像藤蔓一样缠住我的双手双脚。"
    "我只是看着他，动弹不得。"
    show acolas surprised_eyebrow normal2_eyes with dissolve
    a"“对不起，当时对你那样。我只是，因为生病，有点控制不住。”"
    show acolas awkward_eyebrow smile_eyes with dissolve
    a"“我刚刚才回公司，就来找你道歉了……”"
    show acolas surprised_eyebrow normal3_eyes with dissolve
    a"“我们一起做的游戏已经做好了demo，而且我已经发到独立游戏网站上了。”"
    show acolas surprised_eyebrow normal_eyes smile2_mouth with dissolve
    a"“没有你，我肯定做不出来。”"
    show acolas smile_eyebrow normal_eyes laugh_mouth with dissolve
    a"“谢谢你啊。”"
    "他的话像冲锋枪，我居然没法好好思考他到底想表达什么。"
    "我在这场游戏制作中付出了什么？我能付出什么？我付出的东西代表了什么？"
    "我在这场恋爱中得到了什么？他为什么要谢我？我做了什么？"
    $ss('white no_hat')
    s"“啊…好啊…恭喜你。”"
    $sh()
    "面对着痊愈的他，站在我面前的他，微笑着的他，用红色瞳孔直视着我的他，我能说些什么忤逆于他的话吗？"
    "他靠近了，他拥抱着我。"
    "这样的拥抱是我应得的吗？我值得他这样做吗？他为什么要这样做？"
    "拥抱会持续多久？我们会亲吻吗？我们接下来会做爱吗？"
    "我，为什么会想这么多呢？"
    show acolas smile_eyebrow smile_eyes smile_mouth with dissolve
    a"“除此之外，我想给你这个。”"
    "我才注意他的手上似乎握着什么东西。"
    show acolas surprised_eyebrow smile_eyes laugh_mouth with dissolve
    a"“这是…我的笔记本，用了很久。”"
    show acolas surprised_eyebrow normal3_eyes smile_mouth with dissolve
    a"“里面是我大学到现在记录的很多的东西，一些面试的技巧，一些常用的框架的基本入门之类的，虽然现在可能有些技术已经过时了，但其实大多数还算有用。”"
    show acolas surprised_eyebrow normal3_eyes smile2_mouth with dissolve
    a"“除此之外，后面还有关于这个游戏代码和背景设计。”"
    show acolas normal_eyebrow normal3_eyes normal_mouth with dissolve
    a"“很抱歉我包揽了所有的工作，却还要说你不努力。游戏已经做完了，如果有机会的话，我一定不会再这样push你去做什么事情了。”"
    show acolas normal_eyebrow normal_eyes normal_mouth sweat blush with dissolve
    a"“抱歉…真的抱歉…”"
    if p.aco_p == 9:
        $AcolasItem1.add(p)
        $Notice.show()
    "他把笔记本强塞进我的手里，本子确实看上去很旧了，而且似乎经常在被翻动的样子。"
    show acolas awkward_eyebrow normal_eyes laugh_mouth sweat no_blush with dissolve
    a"“可要好好利用！如果你变得更厉害一点的话……工作速度就会更快一点了。”"
    "…"
    "说到底其实还是希望我能快点做好事情啊。"
    "我并不是不求上进，但如果是他说出这样的话…"
    $ss('white no_hat normal2_eyes smile_mouth')
    s"“谢谢你的笔记本，我一定会看的。”"
    $sh()
    "我自己都不相信自己——他的任务我已经完成失败很多次了，读书这件事，也许我也会失败吧。"
    show acolas normal_eyebrow normal_eyes smile2_mouth no_sweat no_blush with dissolve
    a"“那么，下周一我就正式上班了，你也早点回去休息吧。”"
    $ss('white no_hat')
    s"“嗯。”"
    $sh()
    hide acolas with dissolve
    "他招了招手，离开了我的视线。"
    "我低头看着手中的笔记本，迷失感愈发严重。"

    $end_plot()
    if p.aco_p == 9:
        $p.aco_p = 10
    if replaying:
        jump afterreplay
    $p.times+=1
    jump TaskExecuting


label acolas_route_10:
    $start_plot()
    stop music fadeout 5
    scene meeting with fade
    "面对Acolas上午发来的发布游戏的网址，我竟没有勇气点开。"
    "他说他在游戏结束后的制作人列表中的主创，编程和文案上都写了我的名字，但我实际上几乎什么都没做，或者说就算做了也没有放进游戏中。"
    "这是一种恩惠？还是一种侮辱？也许还能算一种把柄。"
    "想一想，如果哪天他说：要不是我把你放进制作人列表里，你会被别人知道吗？你会实现你自己的梦想吗？……之类的，我要怎么回答？"
    "而且如果玩过的人在社群中提问，我在这个游戏中做了什么样的贡献，那Acolas要怎么回答他呢？"
    "算了，只要我不去关心那些事，我就不用考虑这样的问题。"
    "这场制作游戏的风波已经平定下来了，我的人生也回到了平常。"
    "但是，与之前不同的是……"
    "Acolas没再和我一起吃过饭了——之前的他就算在中午午休，也会偶尔来我这边转悠，或者在工作的时候，躲在某些地方像高中班主任一样监视着我。"
    "虽然我并不讨厌，但是每次看到他的时候都会吓一跳，之后他便也会久违地放下他平时严肃的表情，对我笑一笑。"
    "然而，经过了这么多的事情后，我们现在的关系到底算什么呢？"
    "…"
    scene office with fade
    "会议结束了，那只灰狼重回舞台，但是很明显，他的状态远不如从前。"
    "结束后，他吩咐我把这几周他不在的时候，质量不佳或者无人完善的工作整理一下发给他。"
    "此刻那装有他所需要的数据的小小的机械设备正在我的口袋中静静地躺着。"
    "为什么我不直接用软件传给他？我只是借这个机会和他单独见个面而已。"
    "我深吸一口气。"
    "之前的我甚至会期待看到他，而现在，就连去找他说说话都让我觉得十分紧张。"
    "如他所言，他的病也许真的好起来了，也让我毫不意外地，他这一整周都把自己埋在办公室里。"
    "我突然想，如果他的病没那么快好就好了。"
    "但如果他没能从床上下来，那我们的关系肯定也是在一直冷战吧。"
    "空荡荡的某信聊天窗口，空荡荡的桌子，没有主心骨的会议室……"
    "我的视线重回桌面。"
    "Acolas的笔记本正摆放在我桌上放文件的铁架中。"
    "我抬起马克杯，将最后一口深褐色的液体灌进口中——也许我不该这么做，毕竟已经下班了，但总比倒掉好。"
    "……"
    "去他的办公室要不要敲门？要不要去洗手间整理一下我的毛发？我们明明是恋人啊，真的需要这样吗？"
    "我们真的是恋人吗？"
    "我抬起手，嗅了嗅自己的手臂，暂时没有闻到什么令人作呕的低等人气味。"
    "这样过去就行吧。"
    scene acodoor with dissolve
    play sound audio.knocktable
    "我敲了敲门，在听到他短而快的回应后才推开门。"
    play sound audio.door
    scene acooffice with dissolve
    "这好像是我第一次来过他的办公室，之前都是他来找我——可能因为他下班比我早？"
    show acolas with dissolve
    "灰狼正低着头，翻看着堆在他办公桌上的一堆纸质资料，甚至在地上也堆着一堆纸质资料。"
    "除了他写字的声音，他的电脑也发出白噪音般嗡嗡的风扇声。"
    "我没有说话，我也不敢说话，被打断思绪的感觉并不好。"
    "可既然我已经敲了门，那他也被迫分心了，这样想，罪恶感就少了很多。"
    "他翻阅的文件的速度很快，他手中的圆珠笔快速地在文件底部熟练地签上名字，然后把签好的文件放在另一堆文件顶端。"
    "经常和电脑打交道的我大概都没怎么用过笔了，更不要说这样的纸质阅读对我来说还是稍微有一些难受……"
    "我该等他弄完这些吗？还是现在就开口比较好？毕竟我打破了他独处的局面，想必我还是尽快交付完工作就离开比较好？"
    "我靠近他的桌子，将u盘放在他的桌上被文件堆围起来的一块比较开阔的地区。"
    $ss('white no_hat awkward_eyebrow sweat')
    s"“这个是，这几周的总结，还有一些其他的东西…请过目…”"
    $sh()
    show acolas normal3_eyes with dissolve
    a"“嗯，辛苦，没什么事就出去吧。”"
    "我倒是突然很火大，是啊，他是我的上司，他可以这样，但他更是我的恋人啊？难道工作比我还重要？"
    "虽然我这样说也很幼稚，可他和我之间的这种莫名的距离感又是闹哪样？"
    $ss('white no_hat angry_eyebrow normal2_eyes sad_mouth mood')
    s"“Acolas，你才刚刚把身体养好，现在这样高强度工作又会把身体弄垮的。”"
    $sh()
    play music audio.concretejungle
    show acolas normal_eyes with dissolve
    a"“是吗？那工作的事谁来弄？我住院了这么久，这些本来由我负责的东西堆了这么多，我现在不弄完之后只会更多。”"
    show acolas angry_eyebrow normal_eyes with dissolve
    a"“我们是车轮，是螺丝钉，是零件，流水线上来了一个任务你就要做，这就是我们的生活。”"
    show acolas angry_eyebrow normal3_eyes with dissolve
    a"“希望你不要像个小孩子一样吵来吵去的，分配给你的工作永远是部门里最少的。你已经够悠闲的了，还在有空余的时间在这里和我聊天。”"
    "他几乎是一边在文件上写来写去，一边和我说话。"
    "我知道，从他口中说出来的话十分伤人，我应该生气愤怒的，我也应该再也不管他的。"
    "但他需要我的帮助。"
    play music audio.solitus
    $ss('white no_hat agony_eyebrow normal_eyes normal_mouth')
    s"“你别想唬我，我又不是没了解过部门里其他人的每周工作量，更别说有时候我还得分担他们做不完的工作。”"
    $ss('white no_hat agony_eyebrow awkward_eyes normal_mouth')
    s"“…我已经从同事那边听说了，是你自己接下这么多任务给你自己的。”"
    show acolas surprised_eyebrow normal_eyes with dissolve
    $ss('white no_hat sad_eyebrow normal2_eyes agony_mouth')
    s"“你只是为自己的报复性工作找了个借口而已，然后再去伤关心你的人的心来惩罚自己，这样行不通的。”"
    $sh()
    "他没有看我，也没有回应，他只是继续在文件上写一些什么，然后再放到别的地方。"
    "只有他写字的声音，以及他的电脑发出的白噪音般嗡嗡的风扇声。"
    show acolas normal_eyebrow closed_eyes with dissolve
    a"“…呼，至少让我把我向上面要求的这些工作做完好吗？”"
    stop music fadeout 5
    $ss('white no_hat awkward_eyebrow normal2_eyes smile_mouth')
    s"“我来帮你做吧。”"
    $sh()
    "我这样说了，但我心里真的没底我是否能做完这些工作。"
    show acolas surprised_eyebrow surprised_eyes with dissolve
    "但就在我说出这句话后，他的手突然停下，而后看向我。"
    show acolas awkward_eyebrow surprised_eyes laugh_mouth with dissolve
    "他居然笑了，但并不是感谢我帮他做事的笑，更像是嘲讽。"
    show acolas awkward_eyebrow surprised_eyes angry_mouth with dissolve
    a"“我之前交付给你的任务，你一个都没完成，你还指望我安心把任务交给你处理吗？”"
    $ss('white no_hat angry_eyebrow scared_eyes normal_mouth sweat')
    s"“可…Acolas，我关心你啊！”"
    $sh()
    show acolas angry_eyebrow awkward_eyes normal_mouth with dissolve
    a"“嘴上说说谁都会。如果你真的关心我，那我也不会因为要做的事太多而住院，现在也不需要这样工作。”"
    $ss('white no_hat normal2_eyes')
    s"“可是……”"
    $ss('white no_hat normal_eyes sweat')
    s"“…”"
    $sh()
    "我能说什么呢？"
    "房间再次回归沉默，只剩下呜呜的风扇声，还有他写字的声音。"
    scene acodoor with dissolve
    "我离开了他的办公室。"
    "也许，真的全都是我的错吧。"

    $end_plot()
    if p.aco_p == 10:
        $p.aco_p = 11
    if replaying:
        jump afterreplay
    $p.times+=1
    jump TaskExecuting



label acolas_route_11:
    $start_plot()
    stop music fadeout 5
    scene meeting with fade
    "Acolas没来会议，就像他从来都没有来过会议一样。"
    "我和他的情况也逆转了——从他来找我，到我去他的办公室找他。"
    "我不明白我为什么要来找他，也许在他眼里，我和他的感情即将破裂，但在这个公司里，除了我还有谁关心他呢？"
    "即便上周已经被他嘲笑了一番，却还是在下班后来到了他的办公室门前。"
    scene acodoor with dissolve
    "我靠近他的办公室，心脏便狂跳，像是要破开我肋骨的牢笼一般。"
    "即便已经做好伤心的准备。"
    play sound audio.knocktable
    "我敲了敲门。"
    play sound audio.knocktable
    "咚…咚……"
    "没有回应。"
    "或许他实在是太忙了吧，甚至听不见我敲门的声音。"
    "也可能是他知道是我，只是不想开门。"
    menu:
        "直接推门进入他的办公室（可能会让他十分不满）" if (not replaying and (p.route == 'a' or not p.route)) or (replaying and p.aco_p != 98 and p.aco_p != 99):
            menu:
                "真的吗？即便会让这条线完全失败哦？即便你可能无法和他永远在一起哦？"
                "推门":
                    pass
                "离开":
                    jump acolas_route_11_1
                
        "离开（反正现在和他也没什么想说的）" if not replaying or (replaying and p.aco_p != 98 and p.aco_p != 99):
            jump acolas_route_11_1
    
    play sound audio.door
    "我推开门，于是便被眼前的景象惊住了。"
    scene black
    "仍然启动着的电风扇倒在地上，朝着斜上方旋转着扇叶。纸质文件像鸡窝的羽毛一样散落的满地都是，显示屏的屏幕倒扣在桌子上，键盘也丢在地上。"
    "而Acolas则头朝下地趴在地上，一动不动。"
    "…"
    scene black
    call screen cfreeze(3)
    "头疼，头真的很疼。"
    "为什么，为什么他就是不肯！…"
    "…"
    scene hospital_corridor_night with fade
    "医院的消毒水味。"
    "我每呼吸一口，仿佛便有一瓶开封的消毒水顶着我的鼻孔往里灌，让这些液体倒流进的我呼吸道中，之后再让它们填满我的每一粒肺泡，直到爆炸。"
    "急诊室的门打开了。"
    show acolas closed_eyes with dissolve
    "Acoals试图朝我这边走，却差点摔倒。"
    "他的气色和以前完全不能比了，毛发也肉眼可见地毛糙干燥起来。"
    "我应该抱紧他？还是安慰他？还是训斥他？"
    "训斥他没有听我的话，仍然朝着把自己弄死的目标努力？"
    show acolas frown_eyebrow with dissolve
    "他来到我的面前，身高比我高出十几公分的他向下看着我。"
    show acolas frown_eyebrow smile_mouth with dissolve
    "他微笑着。"
    show acolas frown_eyebrow normal2_eyes laugh_mouth with dissolve
    a"“谢谢你救了我，医生说我不用住院了，在家休息一段时间就行。”"
    a"“我…”"
    play sound audio.slap
    show acolas surprised_eyebrow surprised_eyes sad_mouth with dissolve
    "清脆的响声从我的手和他的脸处传来。"
    "我的手心因为这次攻击而火辣辣的疼，想必被我打过的他的脸也是如此地疼。"
    "他呆住了，他没意识到我会扇他巴掌。"
    "沉默，沉默，如同我和他是这座医院的大厅的中心，大厅内的所有人匆忙地在我和他的身边来往，而我和他像是透明的，凝滞的。"
    play sound audio.slap
    show acolas frown_eyebrow normal_eyes normal_mouth with dissolve
    "我又扇了他一巴掌，在同一位置。"
    show acolas frown_eyebrow sad_eyes normal_mouth with dissolve
    "他低头，什么也没说。"
    show acolas frown_eyebrow sad_eyes normal_mouth tear with dissolve
    "他哭了。"
    "…"
    scene incar with fade
    "出租车的引擎声，雨点打击窗户的滴答声。"
    "外面什么时候下雨了？"
    "我和他坐在出租车的后座位，大概连司机也察觉到了我和他之间的特殊情况，试图搭话也只是张开了嘴便又收回去。"
    show acolas normal_eyebrow sad_eyes normal_mouth with dissolve
    a"“[p.name]，什么不做的感觉是什么样的。”"
    $ss('white no_hat scared_eyebrow normal2_eyes smile_mouth')
    s"“坐在院子里，感觉无聊了就去附近的孩子玩，不想的话就在房间里睡一整天，或者看漫画书，小说之类的。”"
    $sh()
    show acolas normal_eyebrow closed_eyes normal_mouth with dissolve
    a"“我小时候住的很高，没有院子，也没有那么多朋友。”"
    show acolas frown_eyebrow normal_eyes normal_mouth with dissolve
    a"“只要一有时间，就是无穷无尽的补课班，有学习方面的，也有才艺方面的…虽然我现在几乎忘记怎么弹钢琴了，但我甚至有个钢琴证书。”"
    $ss('white no_hat agony_eyebrow normal_eyes scared_mouth')
    s"“…”"
    $sh()
    "城市中的孩子比我们乡下长大的要痛苦的多啊。"
    show acolas frown_eyebrow sad_eyes normal_mouth with dissolve
    a"“…我们的游戏出现了很多问题，程序漏洞，数值不平衡，文案错误，剧情逻辑不自洽。”"
    a"“为了在自己喜欢的圈子尽快实现自己的个人价值，让更多人认识我，并喜欢我做的游戏，我十分急切地想得到他们的关注。”"
    show acolas normal_eyebrow sad_eyes normal_mouth with dissolve
    a"“我知道，在现实的我已经绝对地实现了我的价值，我很有钱，还在城市里最贵的小区里买了高层公寓。”"
    a"“或许我比很多人强，但这还不够。”"
    show acolas frown_eyebrow normal_eyes smile2_mouth with dissolve
    a"“没人会在我们网上交友的时候说自己是什么什么地方的总监吧？也不会说自己很有钱，或者几岁就买了车买了房子之类的？”"
    show acolas frown_eyebrow sad_eyes smile2_mouth with dissolve
    a"“我自以为能力足够，可以很快完成游戏的制作。”"
    show acolas frown_eyebrow sad_eyes angry_mouth with dissolve
    a"“但现在的结果就是，像山一样高的抱怨和差评堆在那里，铺天盖地。”"
    show acolas frown_eyebrow sad_eyes normal_mouth with dissolve
    a"“再加上我自己的报复性工作，这些东西一点一点把我压垮了。”"
    show acolas frown_eyebrow normal_eyes normal_mouth with dissolve
    a"“我不想和别人说这些，因为我希望自己在别人眼中是那种，十分可靠，能力极强的人。”"
    show acolas frown_eyebrow closed_eyes normal_mouth with dissolve
    a"“但是，[p.name]，我只说给你听，好吗？”"
    $ss('white no_hat agony_eyebrow normal2_eyes normal_mouth')
    s"“…”"
    $sh()
    "他深呼吸。"
    show acolas sad_eyebrow sad_eyes normal_mouth with dissolve
    a"“我真的很累，很累，很累，很累……”"
    show acolas sad_eyebrow closed_eyes normal_mouth with dissolve
    "他的身体突然瘫软下来，靠在我的身上，深呼一口气。"
    $ss('white no_hat smile_eyebrow normal2_eyes smile_mouth')
    s"“你早该这样的。”"
    $ss('white no_hat smile_eyebrow normal_eyes smile_mouth')
    s"“明天打电话推掉工作吧，或者慢慢来也可以。”"
    $ss('white no_hat scared_eyebrow normal2_eyes smile_mouth')
    s"“如果你再那样的话，也许我就见不到你了。”"
    $sh()
    show acolas sad_eyebrow normal_eyes normal_mouth sweat with dissolve
    a"“抱歉，我真的，再也不会了。”"
    $ss('white no_hat angry_eyebrow angry_eyes smile_mouth')
    s"“那这个周末，你可不要偷偷工作哦？”"
    $sh()
    show acolas frown_eyebrow normal_eyes normal3_mouth sweat with dissolve
    a"“那游戏的事…”"
    $ss('white no_hat smile_eyebrow smile_eyes smile_mouth')
    s"“去他妈的bug，我们想什么时候修就什么时候修，我们想什么时候写就什么时候写。”"
    $ss('white no_hat smile_eyebrow smile_eyes angry_mouth')
    s"“反正我们是老板，你急什么哦…”"
    $sh()
    a"“真的吗？…我其实还蛮担心游戏的风评…”"
    $ss('white no_hat sad_eyebrow sad_eyes smile_mouth')
    s"“难道还能比现在更差吗？…”"
    $sh()
    show acolas awkward_eyebrow sad_eyes smile2_mouth sweat with dissolve
    a"“嘛…”"
    $ss('white no_hat normal2_eyebrow normal2_eyes smile_mouth')
    s"“他们会理解的，至少这段时间，多放松一下吧。”"
    $ss('white no_hat surprised_eyebrow normal2_eyes smile_mouth')
    s"“做游戏只是消遣的行为，无聊的时候再去修bug吧？”"
    $sh()
    show acolas awkward_eyebrow normal_eyes smile2_mouth no_sweat with dissolve
    a"“听你的。”"
    "希望如此吧，我再也不希望在下一次进他办公室的时候，再看到倒地不起的他了。"
    "……也许我在这段感情中，终于做了一件正确的事。"
    $end_plot()
    if p.aco_p == 11:
        $p.aco_p = 12
        $p.route = 'a'
    if replaying:
        jump afterreplay
    $p.times+=1
    jump TaskExecuting


label acolas_route_11_1:
    $start_plot()
    "算了，还是等下次再找他吧。"
    "也许他只是今天太忙了，我的贸然进入肯定会打扰他的。"
    scene office with dissolve
    "也许等周末的时候约他出来吃点什么？毕竟总是他请我吃饭，我都没请他吃过什么……"
    "等晚点问问他想吃什么吧。"
    $end_plot()
    if p.aco_p == 11:
        $p.aco_p = 98
        $Achievement107.achieve()
        if p.hal_p == 99:
            $Achievement301.achieve()
        $Notice.show()
    if replaying:
        jump afterreplay
    $p.times+=1
    jump TaskExecuting


label acolas_route_12:
    $start_plot()
    $p.onOutside = True
    scene black with fade
    stop music fadeout 5
    $p.stime(8,33)
    "“知名轮船酒店德里莫号将停泊于A市，于本周末，登船享受一日住店，绕海域一圈，甲板开放，房间整洁，享受美妙海上风光。”"
    "这段广告我已经可以倒背如流了，A市的汽车广播，地铁广告，甚至刷短视频的时候跳出来的广告都是这个。"
    "这样的酒店的价格也必然十分恐怖，我是做梦都没想到，自己能从那家伙手里得到船票。"
    "虽然他总是抓我摸鱼，不过还是挺看中我的嘛。"
    "说真的，要不是Acolas对这种邮轮没什么兴趣，可能他自己也会来这里的。"
    play music audio.thedeldrimor fadein 5
    scene deldrimor1 with dissolve
    $p.stime(35)
    "…"
    show acolas vest necklace smile_mouth with dissolve
    "他走在我的前面，我像个跟屁虫一样在他的身后倒腾着我的两只腿。"
    "出了地铁之后，A市港口便就在眼前了。"
    "湿润的海风还带着股咸味，灰狼抬头望向远处，同我一起看着不远处的港口。"
    "德里莫号如同一座海上的高楼，从港口建筑之后露出头来。"
    "即便住在临海的港口城市，我也没有太多机会去看看海之类的，倒不如说我根本就对这种本质上只是更巨大的水库来说没什么兴趣。"
    $p.stime(36)
    "但是毕竟机会难得，而且实际来到这里，感觉还不错。"
    "…"
    scene deldrimor2 with dissolve
    $p.stime(37)
    "德里莫号有趣的一点是，在几乎所有交通业务都被数字化的今天，仍然保留着最古老又别致的方法——船票。"
    "我将两张船票交给验票人员，在进行安检后，便让我和Acolas通行了。"
    unk"“好好享受——”"
    scene deldrimor3 with dissolve
    $p.stime(38)
    "…"
    "登船，在船内踩着楼梯抵达我和他的房间。"
    "通道狭窄又阴暗，但当我们找到船票上的房间时，在进到房间后，内部便明亮起来了。"
    scene deldrimor4 with dissolve
    $p.stime(44)
    "房间里有一张宽敞的双人床，白色的被子上印有德里莫的Logo，床头柜上摆着花瓶。"
    "但最重要的是，在正对着门的前方，安置着一面巨大的玻璃窗。"
    "玻璃窗由三片纵高窄宽的矩形玻璃片以梯形向外突出的方式连接而成，能看见暗蓝的天空上堆积着碎云，偏亮一点的视野终点的地平线，之后便是朦胧气雾之下的海蓝色。"
    "贴心地，紧挨着玻璃窗的则是一张小桌，大概可以坐在上面喝杯茶之类的。"
    "Acolas把他的背包放在桌子上，随后便抱着两臂，像评价师那样打量着整个房间。"
    $ss("normal2_eyes")
    s"“你觉得怎么样？”"
    $sh()
    "我把背包放在他的包旁边，将外衣脱掉，放在椅背上。"
    show acolas vest necklace awkward_eyebrow with dissolve
    $p.stime(45)
    a"“看样子内饰并不值这个价格，但也能接受。毕竟也有名气的价格在内…”"
    show acolas vest necklace frown_eyebrow with dissolve
    a"“…一静下来我就在想工作和我们在做的游戏的事，早该系统性地对游戏做一次单元测试的，不然就不会出这么多问题…”"
    $ss("awkward_eyebrow awkward_eyes awkward_mouth sweat")
    s"“说好了，来这里就给我认真放松啊…别再想工作的事了。”"
    $sh()
    "担忧的情绪攀上心思，但毕竟是他，如果真的放松下来就不是他了。"
    show acolas vest necklace smile_eyebrow smile_eyes smile_mouth with dissolve
    a"“听你的。”"
    $p.stime(9, 11)
    stop music fadeout 5
    scene black with fade
    "…"
    "离船航行还有一段时间，这段时间便是我和他无人打扰的时间。"
    "我一直在等待这个。"
    "清洗用于交合的体内空间总是艰难且让人疲倦的，但在迎接美妙的事物时，总要作出一点牺牲。"
    "我的视线透过玻璃，再回到室内的他，此时那只灰狼正拽着那两三层厚的窗帘拉到中间，将本就昏暗的屋内加深成夜的颜色，若不是我知道现在是正午，大概要以为现在已经是傍晚。"
    "而我则面对着他坐在靠窗户较近那边的床边，等待着他的精心布局。"
    "帘子顶端转轮的声音嗡嗡，厚窗帘隔绝了窗户的一切光源，仅留下帘子下方露出来的一条亮线，让它通过漫反射，提供室内唯一的光源，也让我能看见他，看见彼此。"
    "他是什么样的人呢，很多时候我并不能摸透他。"
    $p.stime(12)
    "他有时候很欢乐，带来搞笑的氛围，工作时又是那么严肃认真，而现在的他则离开了那扇窗，缓慢地走近有我在的柔软床榻。"
    "从他的双目绽放而出的血红，那份独属于掠食者的颜色，正紧盯着我。"
    "即便我和他带着几乎是同一族的血脉，此刻我也是他的猎物。"
    "我心甘情愿。"
    "他靠近了，透过暗淡的底光，我能看见那只灰狼的壮硕体型。"
    "是啊，他住的地方开门转个弯就是健身房，经常跑步的我估计也是跑不过他。"
    "我伸手，触摸他的腰部，触感首先是顺滑但带点湿润的毛发，而后是排列在他腹部的肌肉，刚刚洗完澡的他身上带着海盐和柑橘的香味。"
    "他也伸出手，触摸着我的脸。"
    $p.stime(13)
    "谁都没有说话，自他从浴室中回到我和他共存的空间时，就像说好了那样一般。"
    "继续，向前推进吧。"
    "唇齿交接，这就是我一直渴望着的和他的接吻啊。"
    "他很主动，我也并不懂得如何掌控局面，只得任他破坏，搅动。"
    "浅浅的吻在他的掌控之下以某种节奏向前突破，我的口被强迫张开更大来容纳他的占据，牙床或是唾液腺，大概没有什么地方没有被他的舌头蹂躏过的了。"
    "稍显仓促的我试图吞下交缠之中他的唾液，但却迎来他更加让我无法招架的攻势——唾液从我他的嘴角流出，打湿了嘴角的毛发。"
    "我没有注意到的是，他正用一只手解着我的睡衣，另一只手则拦在我的背后，配合着他逐渐下压的身体将我本来向上的上半身，压制到已经快贴近床面了。"
    "于是我跟随着他的意愿躺下，这吻是在让人享受，每一寸被分配了感觉系统的黏膜都被温柔地爱抚到。"
    "我很享受，但熟练的他会把和我的吻当作某段可以留存的记忆，还是因为经历过太多而转眼便就忘却呢。"
    "他看着我，用手触摸着我短裤下的阳物。"
    $p.stime(14)
    "我已经十分坚挺了——拜这个吻所赐——同时感觉顶端也变得十分湿润。"
    "他缓慢地拉下我的短裤，露出我今天精心挑选的四角内裤——我并不喜欢穿其他被称之为情趣内衣的内裤，但现在穿的这个也是我最喜欢的那件。"
    "我看得到，我欲望的体现正颤抖着，用它的液体染湿我心爱的内裤。"
    "随着他的拉拽，我的东西就这么露出来了。"
    "也许会有些难为情，但明明做爱更让人难为情才是。"
    "他用一只手扶着我发红的狼根，用嘴含上龟头。"
    $p.stime(15)
    "我受不了这样的刺激，下意识喘息出声后差点射出来，幸好我手淫比较多，相对于普通的处男来说还是比较持久的。"
    "他的舌头一开始便就聚焦于龟头边缘的冠状沟内，挤压舔舐着敏感的沟回。"
    "我的脚爪下意识地紧抓着空气，被爱抚着的东西更是每时每刻都在向我请求释放。"
    "但我不能，我至少要撑到他舔累之前——在他对口交失去兴趣那一刻，用他想要的东西回馈给他，我也能获得最久的美妙体验。"
    "在他将我的肉棒吞咽得更深时，我的思绪却总是没法集中。"
    "也许我需要完完全全地记清楚这场性爱带来的每一分体验，每一次感官的兴奋，每一滴流溢而出的体液。"
    "我知道，他总是被焦虑和压力困扰。"
    $p.stime(16)
    "除了用毒品抢劫脑内的多巴胺银行，或者自残来欺骗脑内啡分泌，仅剩下的也就是生育所带来的系统奖励了吧。"
    "那些性爱带来的快感让他暂时忘记焦虑，才能让同样属于普通生命的他在变态般的完美主义和自虐般压榨自身动力系统的行为中得以喘息吧。"
    "现在如此熟练的他在过去应该也是这样为别人口交过很多次了。"
    "他也这样抚摸别人，也让别人把精液射进他嘴里。"
    "我能想象。"
    "但我会觉得难过吗，会觉得占有欲无法得到满足吗？"
    "那都是小孩子才会担心的事。"
    "…"
    $p.stime(17)
    "我射了，我没法坚持下去了。"
    "虽然这个比喻有点恶心，但感觉就像憋了整整一天的小便，慌慌张张跑到厕所，对着小便池疯狂输出直到弹夹打空的感觉。"
    "我感觉我都要把蛋蛋射空了…"
    "我大喘着气，大概是恶趣味，我很喜欢看别人吞下自己的精液。"
    $p.stime(18)
    "他也确实这样做了，我看到他嘴边还溢出了一点，于是我起身，和他再一次接吻，这次是我主动，清理自己造成的混乱。"
    "舔过他的嘴角，再一点点清理品味带着自己遗传物质的浊液。"
    "而他也抚上我的身躯，将手伸到我的后方。"
    "…"
    scene deldrimor5 with fade
    $p.stime(10, 22)
    "刚刚来的时候，外面还是晴天，但等船慢慢开始航行的时候却突然下起雨来了。"
    "爱欲过后，便是沉寂。"
    "这个时候很适合来一根烟才对，但Acolas并没有抽烟的习惯，我对那种冒着烟雾的东西也没兴趣。"
    "我没想过我和他的第一次交合来得竟如此晚，或许他第一次来我的工位对我恶作剧的时候，我就该乖乖对他抬起屁股？"
    "而且也没想过，无论是他阳物的进出，或是带着生殖信息的种子流入我的体内，其实也并没有我想得那样快乐。"
    "仅仅只是因为所谓的贤者时间吗？"
    $p.stime(23)
    scene deldrimor7 with dissolve
    "我转头看着窗户，听海浪呼啸的声音，还有雨滴拍打玻璃窗和铁质船体的叮叮咚咚声响。"
    "很明显，我们已经驶离A市的港口了，现在只能从地平线处看到一点点小小的建筑顶端。"
    show acolas naked normal3_eyes phoneon with dissolve
    "Acolas的头靠着枕头，并非完全躺着，他只是看着他的手机，白色的光十分刺眼。"
    "我侧躺着紧贴着他，明显高于自己体温的热量从他的身体传递至我。"
    "这就是谈恋爱的感觉吗？这就是我一直在追求着的东西吗？"
    "很热，很温暖。"
    "我感到开心吗？"
    $p.stime(24)
    show acolas naked frown_eyebrow normal_eyes no_phone with dissolve
    "我翻个面，爬上他的身体，夺走他的手机。"
    $ss("naked no_hat normal2_eyes")
    s"“现在和我在一起，还有那种焦虑感吗？”"
    $sh()
    $p.stime(25)
    "他看样子不想回答这个问题，试图拿回手机。"
    "不过毕竟他有如此强壮的肌肉，从我这种体弱多病的废物手里拿回手机肯定也不是什么难事。"
    "但他在看我仍然不想给他手机时，则很轻松地一把抓回他的手机，按下电源键放在一边。"
    "虽然便看他闭眼深呼吸起来。"
    show acolas naked awkward_eyebrow sad_eyes with dissolve
    a"“没那么多了。”"
    $p.stime(26)
    $ss("naked no_hat agony_eyebrow normal_eyes")
    s"“虽然我道歉了你应该也不会听，抱歉我一直都没做好你交代给我的事。”"
    $sh()
    show acolas naked surprised_eyebrow normal_eyes smile2_mouth with dissolve
    a"“哼哼，是你说的不要在这边想工作的事。”"
    "好吧，看来我不该说这些的。"
    "我只能听见海潮撞击船舱的声音，还有发动机引擎震动发出的嗡嗡声。"
    "片刻宁静之后，他才开口。"
    $p.stime(27)
    play music audio.deldrimorsroom fadein 5
    show acolas naked normal_eyebrow normal_eyes normal_mouth with dissolve
    a"“我仔细分析了一下，为什么我那么想去快一点做完那款游戏。”"
    a"“不只是想要得到关注和认可，应该也有关于在意的事情没做完，就会让我十分难受的原因吧。”"
    show acolas naked angry_eyebrow sad_eyes normal_mouth with dissolve
    a"“说不出来到底是难受什么，就是浑身不舒服的感觉。”"
    a"“任务就在身边，就想赶快做完。”"
    show acolas naked awkward_eyebrow normal_eyes normal_mouth with dissolve
    a"“学生时代的我也很喜欢在放学之前把作业写完，就算没留也会预测着写。”"
    a"“即便我需要占用其他课的时间，但我就算不听课也要把时间留给写作业。”"
    $p.stime(28)
    a"“毕竟写完了就可以做自己想做的事了…我也知道这种思维是错的，现实只会是做完一部分后就会有更多的出现，但我已经没法控制自己不去做事了。”"
    $ss("naked no_hat scared_eyebrow normal2_eyes")
    s"“所以你才经常赶在我前面完成我的任务，最后甚至累倒了。”"
    $sh()
    show acolas naked awkward_eyebrow sad_eyes normal_mouth with dissolve
    a"“大概吧…”"
    $p.stime(29)
    show acolas naked normal_eyebrow smile_eyes normal_mouth with dissolve
    a"“你当时总是说，不要设置死线什么的，但生活中很多东西都没有死线，难道就一直拖延着吗…”"
    a"“比如读想读的书，学想学的知识，还有离结束明明很远或者根本就没有结束日期的任务…”"
    show acolas naked frown_eyebrow normal3_eyes normal_mouth with dissolve
    a"“我看到那些书架上没有读完的书，就会觉得很焦虑…我还有那么多的事情要做，但我却总觉得无力。”"
    show acolas naked frown_eyebrow normal_eyes normal_mouth with dissolve
    a"“你明白那种感觉吗？…”"
    $p.stime(30)
    "说实话，我不太能理解，虽然我也会想把事情都快快做好，但还是经常拖延很久。"
    $ss("naked no_hat scared_eyebrow normal2_eyes")
    s"“大概明白。”"
    "我看着他。"
    $ss("naked no_hat agony_eyebrow normal2_eyes")
    s"“但是，只有休息好了才能做你想做的事，把身体搞垮了该怎么做。”"
    $sh()
    "我知道我所说的话和多喝热水没什么区别，难道他不懂这些吗？可我还能说什么帮助他呢？"
    show acolas naked normal_eyebrow closed_eyes normal_mouth with dissolve
    a"“这正是我所害怕的。”"
    "他闭上眼睛。"
    $p.stime(31)
    show acolas naked normal_eyebrow normal_eyes normal_mouth with dissolve
    a"“如果我在没有完成所有我想做的事情，学会想学的东西之前死去。”"
    a"“那该有多糟。”"
    show acolas naked normal_eyebrow normal3_eyes normal_mouth with dissolve
    a"“就像打游戏，辛辛苦苦收集的装备，练的等级，只是一点小小的失误，整个存档就不复存在。”"
    $ss("naked no_hat sad_eyebrow sad_eyes")
    s"“所以其实是…害怕死亡…？”"
    $sh()
    $p.stime(32)
    show acolas naked normal_eyebrow normal_eyes normal_mouth with dissolve
    a"“不，我不怕，我应该能稳稳地接住死亡，如果他就要来找我的话。”"
    show acolas naked normal_eyebrow sad_eyes normal_mouth with dissolve
    a"“但那必须是我已经做完了所有的事，得到了很多人的认可和喜爱，做了很多能够流传或者仅仅只是停顿于历史中一小段的时间的作品。”"
    a"“那个时候之后，我应该就能坦然地接受死亡。”"
    "我思考。他的眼神少有地黯淡。"
    $ss("naked no_hat agony_eyebrow normal_eyes")
    s"“我明白了，就像你会在死线前很早就疯狂追赶进度，你也无意识地想赶在死亡很久之前就努力做完一生要做的事。”"
    s"“但是活着不只是你的愿望和梦想，你的工作，或者我和你的游戏。”"
    show acolas naked surprised_eyebrow surprised_eyes normal_mouth with dissolve
    $ss("naked no_hat scared_eyebrow normal2_eyes")
    s"“那些间隔也是活着的一部分。”"
    $p.stime(33)
    s"“就像我们现在正在做的事一样。”"
    $ss("naked no_hat scared_eyebrow normal2_eyes smile_mouth")
    s"“享受这些间隔，不也挺好的吗…”"
    s"“而且你死了，对你来说所有事物也没有意义了，就算没做完你想做的事，你也没有能力去遗憾了。”"
    "我向前坐起，缩短和他之间的距离。"
    $ss("naked no_hat scared_eyebrow normal2_eyes angry_mouth")
    s"“其实你就是害怕死亡，只不过你和别人不一样，人家是想在死前享受，而你是想做一些事。”"
    $ss("naked no_hat scared_eyebrow closed_eyes normal_mouth")
    s"“但是死掉了，其实也解脱了，什么事…都没意义了，所以顺其自然就好。”"
    $sh()
    $p.stime(34)
    show acolas naked normal_eyebrow sad_eyes normal_mouth with dissolve
    a"“…你说的话我会好好思考的。”"
    stop music fadeout 5
    "他闭眼，随后便是他温热的唇吻上来。"
    "我很惊讶，我甚至不奢望他能对我有好感。"
    "我迎合着他的亲吻，雨仍然没有要停下来的迹象，像是要持续至永远一般。"
    "…"
    $end_plot()
    if replaying:
        jump afterreplay
    if p.aco_p == 12:
        $p.aco_p = 13
    $ p.newDay()
    $ p.stime()
    $ Save.save(p)
    $ Notice.add('存档已保存！')
    $ Notice.show()
    call loading from _call_loading_9
    jump acolas_route_13


label acolas_route_13:
    $start_plot()
    if p.mental < 5:
        $p.mental = 30.0
    show screen screen_dashboard(p)
    $p.onOutside = True
    scene deldrimor4 with fade
    "汽笛声和穿过玻璃的阳光将我唤醒。"
    "在醒来的刹那我突然意识到，这次的起床并没有闹钟参与，也没有头疼的折磨。"
    "也许是我睡得很香？在和Acolas相拥入眠一夜之后？"
    "无论如何，我今早不打算吃药了，即便这是个冒险的行为，但如果头疼突然爬上脑壳的话，再吃应该也来得及。"
    "…"
    $p.stime(8, 43)
    scene deldrimor10 with dissolve
    play music audio.deldrimorsdeck fadein 5
    "甲板上聚集了很多人。"
    "下了一晚上雨，也该放晴了。"
    "我和他来到甲板的栏杆边，将身体的重量倚靠于栏杆上。"
    "稍微有一点冷的海风，带着咸味，除此之外便是海鸥的叫声。"
    "可惜我没带手撕面包这种东西喂给它们吃，但看周围的人似乎早有准备。"
    "他们从自带的面包中撕下一块举高，于是那些飞翔的生物便控制他们的速度，缓慢降落至面包附近的同时还要跟上邮轮的速度。"
    "看上去就像悬浮在空中一样。"
    "我在想，如果我抬手一抓，是不是就抓到海鸥了。"
    $p.stime(44)
    scene deldrimor9 with dissolve
    "Acolas则在看着大海，我顺着他的方向看去，在地平线处，已经能够看到陆地和较高的建筑群了。"
    "这场邮轮之行就快结束了，他看上去有些忧愁。"
    show acolas vest necklace smile_eyebrow normal_eyes normal_mouth with dissolve
    a"“[p.name]害怕被抛弃吗？”"
    "他突然开口。"
    "我稍微有些惊讶，他为什么突然会有这样的想法。"
    show acolas vest necklace normal_eyebrow sad_eyes normal_mouth with dissolve
    a"“那种，没有人需要你，没有人觉得你有什么用处，大家都唾弃你，还有人夺走你的心血和作品，发表出来后受他人敬仰。”"
    "…"
    $p.stime(45)
    $ss("scared_eyebrow normal_eyes normal_mouth")
    s"“是，这很可怕。”"
    $sh()
    show acolas vest necklace normal_eyebrow normal2_eyes normal_mouth with dissolve
    a"“如果我要是变成那个样子，可能就没有什么信心完成自己的想法了。”"
    $ss("smile_eyebrow smile_eyes scared_mouth")
    s"“但是大家都喜欢你，大家都敬佩你的能力，你也为我们，尤其是我，做了很多。”"
    $ss("agony_eyebrow smile_eyes normal_mouth")
    s"“你害怕被抛弃吗？所以Acolas才会那样努力吧。”"
    s"“努力到身心俱疲，在生病的时候责备自己没法完成自己想做的事，甚至责备别人，要求别人也和你一同努力到极限。”"
    "我看向他。"
    $p.stime(46)
    $ss("normal_eyebrow normal_eyes smile_mouth")
    s"“希望你能稍微停下来速度，像这样好好休息一会…”"
    $sh()
    show acolas vest necklace surprised_eyebrow normal3_eyes normal_mouth with dissolve
    a"“如果我停下了…那你们…”"
    "他似乎想说什么，但还是以叹息中断了自己的发言。"
    show acolas vest necklace surprised_eyebrow sad_eyes normal_mouth with dissolve
    a"“唉…”"
    $p.stime(47)
    show acolas vest necklace smile_eyebrow smile_eyes sad_mouth with dissolve
    a"“我感觉我真是个差劲的人，在我身边肯定很累，很有压力吧。”"
    $ss("normal_eyebrow normal_eyes normal_mouth")
    s"“是啊，我也从来没否认过，但没关系，我会陪着你的，直到你变成更好的自己…”"
    $ss("normal2_eyebrow normal2_eyes smile_mouth")
    s"“我们…还有很长的时间呢…”"
    $sh()
    $p.stime(48)
    show acolas vest necklace frown_eyebrow smile_eyes smile_mouth with dissolve
    "Acolas转身看向我，以极快的速度吻了一下我的脸颊。"
    stop music fadeout 5
    "…"
    $p.stime(10, 30)
    scene subway with fade
    "地铁内人很多，大多也都是和我们一起离船的游客。"
    "我和他在这样的公共场合旁若无人地牵手。"
    "虽然我没法忽视其他人异样的眼光，但我更不想中断和他掌心相拥的温热。"
    "或许曾经的我并没有走进他的心，我和他的所作所为仅仅是为了消遣——体验爱与被爱的感觉。"
    "而现在，我确信，随着我与他的互相了解，这份感情一定会越来越深。"
    "…"
    "Acolas突然转头过来。"
    show acolas vest necklace normal_eyebrow normal2_eyes normal_mouth with dissolve
    a"“[p.name]，我决定了。”"
    show acolas vest necklace frown_eyebrow smile_eyes smile_mouth with dissolve
    a"“下周五我就准备辞职。”"
    $ss("surprised_eyebrow surprised_eyes scared_mouth")
    s"“啊？真的？”"
    $sh()
    $p.stime(31)
    "我不敢相信，这个一直试图以工作的形式实现自身价值的疯子居然会说出这种话？"
    show acolas vest necklace smile_eyebrow smile_eyes laugh_mouth with dissolve
    a"“真的。”"
    show acolas vest necklace smile_eyebrow smile_eyes smile2_mouth with dissolve
    a"“我想通了，也许职场压力确实大了点，或者仅仅是因为我自己无意识地放纵自己的报复性工作欲，给自己的压力太多了…”"
    show acolas vest necklace awkward_eyebrow smile_eyes surprised_mouth with dissolve
    a"“当总监这段时间我攒了很多钱，就算不够…不是还有你嘛——”"
    $ss("sad_eyebrow awkward_eyes smile_mouth")
    s"“哎呀…那你在家里呆爽了，偶尔帮我分摊下工作也挺好的…”"
    $sh()
    $p.stime(32)
    show acolas vest necklace sad_eyebrow normal_eyes sad_mouth blush with dissolve
    a"“是你让我学会放松的，怎么又突然反悔～”"
    $ss("angry_eyebrow normal2_eyes angry_mouth")
    s"“你这家伙！”"
    $sh()
    show acolas vest necklace smile_eyebrow smile_eyes laugh_mouth blush with dissolve
    "我不再理他，拿出来手机准备刷一会莓博。"
    "等这周结束，他辞职了，我的病应该也好了。"
    $p.stime(33)
    "之后的人生，会变成什么样呢？"
    $end_plot()
    if p.aco_p == 13:
        $p.aco_p = 14
    if replaying:
        jump afterreplay
    $p.times+=1
    $p.onOutside = False
    jump dayEnd

label acolas_route_98:
    $start_plot()
    stop music fadeout 5
    scene meeting with fade
    "Acolas并没有出席这周的会议，取而代之的则是一个新的技术总监。"
    "他居然离职了吗？甚至没和我说过一声……"
    "但是为什么他短信也没有回复过我，打电话也是无人接听，就这样不声不响地消失了……"
    scene office with dissolve
    "也许他已经离开了这个城市吧，或者他再也忍受不了这样焦虑的人生……"
    "好啦，该想想这周末该做点什么了……"
    $end_plot()
    if p.aco_p == 98:
        $p.aco_p = 99
    if replaying:
        jump afterreplay
    $p.times+=1
    jump TaskExecuting