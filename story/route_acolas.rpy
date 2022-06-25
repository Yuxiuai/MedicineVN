label acolas_plot_judge:
    if persistent.noplot:
        jump TaskExecuting
    if p.aco_p == 1:
        jump acolas_route_0
    elif p.aco_p == 3:
        jump acolas_route_1
    else:
        jump TaskExecuting


label acolas_route_0:
    $rollback_switch()
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
    $rollback_switch()
    if replaying:
        jump afterreplay
    jump TaskExecuting

label acolas_route_1:
    $rollback_switch()
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
    $rollback_switch()
    if replaying:
        jump afterreplay
    jump TaskExecuting