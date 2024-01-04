label destot_route_workgame:
    scene office with fade
    show destot with dissolve
    $workgame_object = Workgame()
    show screen workgame_sayr(rd(1000, 1100), rd(100, 400), '前辈……')
    show screen workgame_sayl(rd(500, 700), rd(75, 400), '我有一些问题……')
    call screen ui_workgame(workgame_object) with dissolve
    $p.updateAfterTask(DestotWork)
    $DestotWork.afterTaskResult(p)
    if workgame_object.step-workgame_object.chain < 2:
        $DestotWork.excePerf(p)
        jump DestotWork_result_exce
    elif workgame_object.step-workgame_object.chain in (3, 4):
        $DestotWork.goodPerf(p)
        jump DestotWork_result_good
    elif workgame_object.step-workgame_object.chain == 5:
        $DestotWork.normPerf(p)
        jump DestotWork_result_norm
    else:
        $DestotWork.badPerf(p)
        jump DestotWork_result_bad

label destot_route_workgame_loop:
    scene office with fade
    show destot with dissolve
    $workgame_object = Workgame()
    show screen workgame_sayr(rd(1000, 1100), rd(100, 400), '前辈……')
    show screen workgame_sayl(rd(500, 700), rd(75, 400), '我有一些问题……')
    call screen ui_workgame(workgame_object) with dissolve
    jump destot_route_workgame_loop

label destot_route_0:
    $start_plot()
    scene office with fade
    play music audio.phonering
    menu:
        "接电话" if True:
            stop music
    "……"
    ar"“喂，[p.name]，部门刚面了一个实习生，你来带吧。”"
    $ss('no_hat white glasses surprised_eyebrow surprised_eyes em')
    s"“啊…啊？”"
    $sh()
    "困得连大脑基础功能都还未开启的我在听到这一消息后突然清醒了起来。"
    "带实习生，为什么是我啊？不应该是资历更老的前辈来带吗？我这种天天上班睡觉的前辈，真的能带实习生么…"
    ar"“不是我们觉得你有多厉害，最近来了很多实习生，我们已经带不了那么多了，我自己还带了两个呢。”"
    $ss('no_hat white glasses awkward_eyebrow awkward_eyes')
    s"“真假，你不会骗我吧？”"
    $sh()
    "这只白狼嘴里说出来的话一个字都不能信，我都猜到了，肯定是他被负责带实习生，结果嫌麻烦就丢给我了。"
    ar"“咳咳，别胡说，实习生挺好的啊，可以把你自己的工作给他做一点之类的，你要真不喜欢我就让别人带。”"
    "啊？还有这好事？"
    "他这么说很明显就是知道我喜欢偷懒，才故意那么说的。"
    "不过实际上的情况反而是增多吧……毕竟我还要指导他，帮他做些什么之类的……"
    $ss('no_hat white glasses agony_eyebrow agony_mouth')
    s"“嗯…让我考虑一下…”"
    $sh()
    ar"“总之人家下周一就来上班了，你快点做决定，我还有事呢。”"
    "但带一个实习生肯定不可能像他说得那么简单，我肯定得变成他的专属答疑机器。"
    "想当初我毕业之后什么都不会，如果直接就让这样的实习生帮我干活，肯定是完全懵逼的状态吧。"
    "不过他说的也没错，其实我现在需要做的也没多难，要是同意了的话，给他点简单的事情做，我应该会轻松不少吧…"
    menu:
        "同意" if p.des_p != -1 and replaying or not replaying:
            if not replaying:
                $p.des_p = 1
            $ss('no_hat white glasses agony_mouth normal2_eyebrow normal2_eyes')
            s"“行吧，那你把他简历发我看看吧，不会是什么乱七八糟的摆烂学弟吧……”"
            $sh()
            ar"“应该不算差，拿过几次奖，简历发你了，自己去看。”"
            ar"“不指望你能把他培养成什么技术人才，你别把他养成和你一样天天偷懒的家伙就行。”"
            $ss('no_hat white glasses angry_eyes angry_eyebrow angry_mouth')
            s"“哎，我在你眼里就只会偷懒吗！”"
            $sh()
            "在我还在对着电话大叫的时候，代表通话中断的提示音已经响起。"
            "哎，真讨人厌。"
            "不过现在我突然开始后悔了，我干嘛要接下来这苦差事呢，一周要干的活也没那么多，我一个人快乐摸鱼不好么…"
            
        "拒绝" if p.des_p == -1 and replaying or not replaying:
            if not replaying:
                $p.des_p = -1
            "算了，感觉还是很麻烦的样子，我可不想当谁的贴身导师啊，况且谁知道这实习生是什么水平…"
            $ss('no_hat white glasses')
            s"“那个，我还是拒绝吧，感觉如果让实习生帮我做东西，不合格的话还是得我自己做…”"
            $sh()
            ar"“啊呀你这…”"
            $ss('no_hat white glasses normal2_eyebrow normal2_eyes smile_mouth')
            s"“好了没事我就先挂了，要开始干活了捏！”"
            $sh()
            "我挂断了电话，呼了一口气。"
            "不过为什么我现在突然觉得有点后悔，也许这是一个认识新的人的好机会呢……"
            "说不定他很帅，很可爱，愿意陪我出来玩呢？"
            "但后悔也没用了，我也没法让时间回到选择决定之前了，就这样吧。"
    $end_plot()
    if replaying:
        jump afterreplay
    jump operate_screen_label
        
    
    
    
label destot_route_1:
    $start_plot()
    scene office with fade
    stop music fadeout 5
    "每天早上不是头疼得要死就是困得要死。"
    "和普通人的是，大家都是睡觉补充精神，而我因为头疼，总是睡不太深。"
    "听说睡眠质量体现在大脑深睡眠的占比，但我的入睡情况一般是靠玩手机转移注意力，不让自己的头那么疼。"
    "玩到实在困得不行，才就着疲倦的势头睡着，第二天又匆匆醒来。"
    "不像其他人，躺在床上，安详地闭上眼，放空意识就睡得着。"
    "在极为安静的环境下，连蚊子振翅的声音都十分吵闹，如果我也那样做，头疼会让我更加痛苦的。"
    "…"
    show destot with dissolve
    "当我靠近自己的工位时，突然发现一个长耳朵的家伙站在我的桌子旁边，似乎十分紧张地看着附近。"
    "…嗯…他是谁呢…"
    "我半睁着眼，将他的外貌特征信息和我脑中的数据库做对比。"
    "是哪个同事来着…"
    "哦…等一下…今天，今天是周一。"
    "啊！"
    "我去。"
    "我又一次精神起来。"
    "他是，上周提到的实习生啊。"
    "啊，我把Arnel的信息屏蔽了，都忘记看他的简历了！"
    "我甩了甩脑袋，不顾东倒西歪的眼镜，我抽出手机点开Arnel的聊天窗口。"
    "余光里，那只小兔子似乎看到了我，随后快速地朝着我这里跑来。"
    "喂！你不要过来啊！我连他叫什么都不知道呢！"
    play music audio.destot
    destot"“你一定就是[p.name]前辈吧！Arnel主管给我看过你的照片了，说实话我觉得你比照片帅一点哦！”"
    $ss('no_hat white glasses surprised_eyebrow surprised_eyes')
    s"“啊…啊……是啊…我是…”"
    $sh()
    "我赶紧把手机揣回裤兜里，感觉脑门的毛发正疯狂渗出汗液。"
    destot"“你一定看过我的简历了，我的手机号和某信账号都在简历上，不过我还是再介绍一下自己吧！”"
    des"“我是Destot，现在就读于A市大学大四，专业是软件，梦想是成为很厉害的程序员！”"
    "他看上去十分有活力，既然他已经介绍自己了。那我假装看过他的简历就好了。"
    $ss('no_hat white glasses agony_mouth agony_eyebrow sad_eyes blush sweat')
    s"“啊…我是[p.name]…在这家公司上班…嗯…”"
    $sh()
    "怎么一到我介绍就磕磕巴巴的，不对…这不怪我啊，我根本没准备好！"
    "怎么办，我肯定在他眼里是个很差劲的人吧…想想办法…"
    $ss('no_hat white glasses awkward_eyebrow surprised_eyes')
    s"“啊…那个…”"
    $ss('no_hat white glasses sad_mouth normal2_eyes')
    s"“我其实资历也没有那么深，也就早你毕业两三年而已，也不算你的前辈吧，说不定基础知识还不如你…”"
    $ss('no_hat white glasses angry_eyebrow scared_eyes smile_mouth')
    s"“有什么公司和实习相关的问题我都会尽量回答的。”"
    $sh()
    des"“哦！那就太好了！我有好多好多问题想问你！”"
    "我抓了抓脑袋上的汗，但因为我的手不是面巾纸，除了让我的手毛也被汗打湿之外毫无作用，然而我的爪子里也早就被汗覆盖了。"
    "我把东西放在桌子上，坐回我的位置打开电脑。"
    "…"
    scene office with fade
    "这位新人确实有很多问题，虽然大多都是一些无聊的东西，比如工作累不累之类的。"
    "那肯定是累啊，还用问吗，要是轻松的话就是领导了。"
    show destot with dissolve
    des"“抱歉，问了很多问题，我总觉得前辈有种很亲切的感觉，就像是和同学聊天一样…”"
    $ss('no_hat white glasses awkward_eyebrow awkward_eyes awkward_mouth')
    s"“我就当你夸我年轻了…”"
    $sh()
    des"“其实我真的不是自来熟的人！只是觉得能和前辈你说很多…”"
    $ss('no_hat white glasses angry_mouth sweat')
    s"“那就别说那么多，有些问题太蠢了，你可以提一些实际的，有用的问题…”"
    $sh()
    "我确实对他的提问行为搞得有点不耐烦了。"
    des"“抱歉…”"
    des"“那么，我来上班具体需要做些什么呢…”"
    $ss('no_hat white glasses normal2_eyes normal2_eyebrow')
    s"“主管没和你说吗？”"
    $sh()
    des"“他跟我说问你。”"
    "哦…可能这就是他说的，可以分配实习生做一些工作…"
    $ss('no_hat white glasses awkward_mouth')
    s"“好吧，我先看看…”"
    $sh()
    "糟糕，我最近做的东西恰好都是比较难弄的工作，交给他来做真的可以么……"
    $ss('no_hat white glasses normal2_eyes')
    s"“……这周的话就算了，等你先学习一段时间再说。”"
    $sh()
    des"“诶，没关系吗？”"
    $DestotWork.unlock(p)
    $ss('no_hat white glasses')
    s"“过段时间再说吧，不过也不代表你来了什么也不用干，我会挑一些时间来教你一些现在我在做的东西的。”"
    $sh()
    des"“好的！那么我先回我自己的位置了，需要我的话就来找前辈您吧！”"
    $ss('no_hat white glasses normal2_eyes')
    s"“嗯。”"
    $sh()
    hide destot with dissolve
    stop music fadeout 5
    "那家伙离开了。"
    "糟了，跟这家伙聊天浪费了我好多时间，我得赶紧做计划了…"
    
    $end_plot()
    if replaying:
        jump afterreplay
    $p.des_p = 2
    jump operate_screen_label
    
label destot_route_2:
    $start_plot()
    scene destot_street1 with fade
    play music audio.destot fadein 5
    "我曾听说过夜晚的商业街人很多，但没想到这么多。"
    show destot with dissolve
    "我和这只稍微矮我一点的小兔子刚出地铁，过了一条马路，便来到了A市最有名的商业街。"
    "或许是周末的原因，或者是因为某些我不知道的节日，今晚的街道上充满了人，这还是我第一次体会到摩肩接踵这个成语的含义。"
    $ss('normal2_eyes normal2_eyebrow')
    s"“我们还是绕个道吧。”"
    $sh()
    "Destot的耳朵垂下，似乎也很苦恼，但要去往我们今晚的目的地并非只能走这条路。"
    "毕竟这条路是主要的步行街，各种小吃商店都分布在这条步行街的两侧，如果要去往街对面，那么只需要去旁边平行的街道就可以了。"
    des"“抱歉，其实我也有点想和前辈逛逛步行街的，但是人太多了…”"
    $ss('normal2_eyes normal2_eyebrow smile_mouth')
    s"“没关系啊，能和你出来走走就很好…”"
    $sh()
    des"“诶嘿嘿…”"
    scene destot_street2 with fade
    show destot with dissolve
    "来到没什么人的侧街，Destot很明显加快了速度。"
    "这只小兔子走在我前面，稍微有些急切的样子。"
    des"“之前想给你一点神秘感，那就现在就告诉你好了。”"
    des"“今晚要去的地方可是我最喜欢吃的一家自助，大一刚来到这里的时候就被推荐了，过来吃了几次。”"
    $ss('awkward_eyebrow sad_eyes agony_mouth blush')
    s"“嗯哼，价格也很贵吧…一说到要你请我吃反倒有点不好意思…”"
    $sh()
    "小兔子突然站住，眉头紧促起来看着我。"
    des"“哪有！我都说了是为了感谢前辈你的帮助啊！这周你帮我解决了很多问题！”"
    $ss('angry_mouth blush')
    s"“是嘛，其实还好啦…”"
    $sh()
    "我挠了挠头，虽然他提问的内容很多也是我一知半解的东西，基本上都是我们一起查资料和文档才解决的。"
    des"“况且就算没有，我也想请你吃点东西！因为我很喜欢你！…”"
    $ss('smile_eyebrow smile_eyes smile_mouth blush')
    s"“是嘛，有多喜欢我呢？”"
    $sh()
    "我并没有将他的喜欢放在心上，只是随便应付了他一句。"
    "不过其实有些奇妙的是，每次看到他我都会想起工作的事，让我感觉放松不下来，但这也不能怪他就是了。"
    des"“就，就很喜欢啊，反正很喜欢…不说这个了，我们马上就要到了！…”"
    scene destot_street3 with fade
    "前面就是拐角，连接着一条较繁华的马路。"
    "对比之下，之前的副街连灯光都有点昏暗起来了。"
    show destot with dissolve
    des"“我看看，右转之后应该就到了。”"
    "小兔子突然把手伸了出来。"
    des"“那个…要不要拉住我的手，前面人很多，我怕走散了…”"
    "我把手伸了出来，握住他的兔爪子。"
    "软蓬蓬的。"
    $ss('smile_eyebrow smile_eyes smile_mouth')
    s"“走吧？”"
    $sh()
    "但他并没有继续往前走，而是像是整个人冻在了那里一样，随后突然把手收了回去。"
    des"“我开玩笑的！走吧走吧！”"
    "嗯？前面确实人很多，按他这么说倒没什么问题啊，怎么会说开玩笑…"
    "于是我伸出手来，握住他已经垂在腰部的爪子，进入拥挤的人群。"
    "…"
    scene destot_waiting with fade
    "穿过人群，我们进去了一个建筑的二楼，不过似乎有很多人在排队等待用餐的样子。"
    "他去付了钱，随后从前台拿了号码，等待区的人很多，但幸好还有两个座位留给我们。"
    show destot with dissolve
    des"“…抱歉，我应该提前订好座位的，我没想到今晚人那么多…”"
    des"“现在手机也没电了，我还想着进到里面充电呢，这个地方连个插座都没有。”"
    $ss('normal2_eyebrow normal2_eyes')
    s"“你可以玩我的手机，不过我手机里只有很简单的小游戏。”"
    $sh()
    "我点开手机上的游戏图标。"
    des"“啊，我还没玩过这个游戏，是怎么玩的？”"
    $ss('surprised_eyebrow surprised_eyes surprised_mouth')
    s"“真的假的，这游戏不是很经典吗？”"
    $ss('normal_eyes normal_mouth normal2_eyebrow')
    s"“就是…用手滑动，两个相同的数字会合并成更大的数字，合出2048就算成功，不过还可以继续合出更大的数字…”"
    $sh()
    des"“看起来还挺有趣的？”"
    "我把手机给他，他便抱着我的手机开始滑来滑去。"
    "手机里还有一些没写完的委托，不过这个小兔子应该不会乱翻别人的东西吧？"
    "他的耳朵随着爪子的滑动支棱起来，过一会又慢悠悠的垂下去，似乎他的心思都会清晰地体现在耳朵上。"
    des"“前辈！你看我合出256了哦？虽然离终点还挺远，不过确实挺好玩的。”"
    "嘈杂的用餐声和大厅人员走动的声音似乎被思维拒之门外了，我突然意识到自己好像盯着他有一段时间了。"
    "…还没到我们吗？怎么这么多人…"
    "他的心思我大概是明白的，但是只是没法确定对方是不是真的喜欢自己。"
    "如果提前跟他说自己对他没兴趣，如果他就是这样会自然地对身边人过分热情的家伙，并不是只对我这样，岂不是很尴尬？"
    "我真的喜欢他吗？这句话也是问我自己的。"
    "他很可爱，看上去很努力，有点幼稚，有点天真…"
    unk"“9号！…9号顾客在吗！…”"
    "哦！到我们了。"
    "我突然回过神来，为什么最近的我总是有点恍惚呢。"
    "……"
    scene destot_bbq with fade
    "说是自助，大概是类似烤肉的那种店面，空气里充斥着肉类的油腻气味。"
    "虽然随便吃肉的说法是很诱人，但是拿菜加上烤制再吃下去往往要花很长时间。"
    "拖慢胃的消化时间，降低食欲，一餐吃下的食物其实和平时差不了多少。"
    "商家的一种手段，可以说性价比极低的一餐。"
    "可能大学生们更喜欢亲自动手烤制的快乐吧，这样也能说明为什么火锅更贵了，毕竟肉涮一涮就熟了。"
    show destot with dissolve
    "小兔子拿了些蔬菜和水果，不知道为什么他会喜欢这样的自助餐？蔬菜更新鲜一些吗？还是说仅仅是为了我才这么说…？"
    "我取了两杯酸梅汤，这东西很开胃，大概能让我们用餐过程中多吃一些。"
    "他小口的嗫饮着紫红色的饮料，我则拿着夹子在烤架上翻转他的菜叶，包上一些旁边烤好的肉放在他的盘子里。"
    "烤架有点特殊，整体是瓮形的，大概有一个矿泉水瓶那么高。"
    "表面有一些镂空的花纹，看不见里面是什么。"
    "有点像一个小炉子，顶端是四方格的烤架，不是那种电磁炉的平面。"
    "不过似乎应该也是电烤的，因为我没看到明火或者炭之类的东西。"
    "我们之间其实没有那么多的话题，我没能摸清他的爱好，他也没法搞懂我喜欢什么。"
    "所以这餐只能有一搭没一搭的和他聊聊工作上的一些见闻，不过看上去他更好奇我谈恋爱的经历。"
    "他确实吃得不多，或许他这种小家伙不该来吃自助的。"
    "只有我一直一趟一趟地取牛排，再孤零零地放在空无一物的烤架上，像等待作物成熟那样等待那东西变熟，直到我对一切肉类感到恶心。"
    des"“前辈觉得好吃吗？”"
    $ss('normal2_eyes')
    s"“…还好吧…”"
    $sh()
    "红色的带筋肉排变为深褐色，而我却毫无胃口，用桌上的大剪刀把肉剪成小块，趁着别人不注意，将肉塞进高烤架的镂空花纹里。"
    $ss('surprised_eyebrow')
    s"“我吃饱了，走吧。”"
    $sh()
    des"“嗯…”"
    "他的耳朵一直垂着，难道我让他觉得这顿饭不好吃吗？还是在想些什么东西呢？"
    $end_plot()
    if replaying:
        jump afterreplay
    $p.des_p = 3
    $DestotTask1.lock(p)
    $p.times += 1
    jump after_executing_task_label
    
    
    
label destot_route_3:
    $start_plot()
    stop music fadeout 5
    show office with dissolve
    "实习生大概是能给公司注入一些新鲜活力的唯一来源了。"
    show destot with dissolve
    "死气沉沉的办公室里，唯独那只长耳朵的小家伙在手忙脚乱地把稿子打印装订，倒是让我想起了我实习的那段时间…."
    "不过似乎我没有那么深刻的印象，虽然我能回忆起找第一份工作之前的焦虑，但入职没有多久就离开了那里。"
    "现在想来，很多东西都不太记得了，我为什么离开？当时做了些什么？甚至当时带我的前辈长什么样都不记得了。"
    "也许是记忆因为头疼老化了，说不定会提前得上痴呆症，忘掉所有东西。"
    "我和他的关系十分微妙，我知道他很有可能喜欢着我。"
    "虽然我表面上说喜欢和他出去吃点东西，或者逛逛街，但我又怎么不清楚，自己只是利用他的好意呢？"
    "明明不是恋人，明明根本就不喜欢他，却还是心安理得地接受他对我的示好。"
    "这真的没问题吗？"
    "但自他之前，我连一个能聊些什么的朋友都没有，每天只是面对着永远也不会变化的东西工作，然后上下班。"
    "我是在珍惜这份友谊所以才没有坦白自己并不喜欢他吗？"
    $ss('no_hat white glasses normal2_eyes normal2_eyebrow')
    s"“中午吃什么？”"
    $sh()
    "当我说出这句话的时候，是代表我真的想和他去吃东西，还是说我想让他承担今天的午饭，还是说我需要他的情感陪伴？"
    des"“先走走吧，顺便看看周围都有些什么。”"
    $ss('no_hat white glasses normal2_eyes normal2_eyebrow smile_mouth')
    s"“好。”"
    $sh()
    "…"
    scene street with fade
    play music audio.concretejungle
    "太阳光刺得我睁不开眼睛，可能是我在室内太久了吧。"
    "他在我的身侧走着，保持和我相同的步伐，分不清是我在跟着他还是他跟着我。"
    "我没在思考，只是下意识地去往一个地方。"
    "如果他想去什么地方，会突然停下来然后问我要不要往右拐吗？"
    "公司附近有很多小吃，虽然我没有吃过几家，但吃过的几家都已经和他一起去过了。"
    scene destot_storefront with dissolve
    "我突然想起，他刚来的时候，我跟他在公司楼下，朝着和现在的方向一样走路，跟他聊天。"
    "“这附近有很多好吃的，他家我之前很喜欢吃，还在他家办了卡，那家的烧烤味道很棒，对了，你吃过冷面没有？”"
    "…现在这些东西基本上也都吃过了。"
    $ss('no_hat white glasses surprised_eyebrow surprised_eyes surprised_mouth')
    s"“啊，什么时候新开了一家面馆啊，中午吃这家吧。”"
    $sh()
    des"“好啊。”"
    "他从来不会拒绝我，但拒绝我代表着什么呢？难道他害怕我吗？"
    "…"
    stop music fadeout 5
    scene destot_noodles with dissolve
    "两碗平平无奇的面条被服务员端上来，我们静静的将面吸入口中。"
    "这种诡异的安静似乎并不属于这个阳光开朗的实习生，但是他依然带着沉默，甚至眼睛都没有抬起来看我一眼。"
    "或许他有什么话想说的，或许是关于我的，或许是关于工作的，但是这么沉默的气氛属实并不是什么吃饭的好情况。"
    $ss('no_hat white glasses normal2_eyes')
    s"“你这周好像都在闷闷不乐的，怎么了吗？”"
    $sh()
    "将碗向前推了些，随着筷子在碗沿上的敲击声响起，我开启了一个看上去很不妙的话题。"
    "Destot像是咂了咂嘴，声音很轻，看上去有些愧疚，他的眼睛没有在看着我，我仅能听到一点气若游丝的声音。"
    des"“前辈…昨天我算了一下，大概之后不能请你经常吃东西了…”"
    "嗯…有关钱的问题？不过作为一个比他年长几岁的人经常蹭他的豪华晚餐确实让我有些面子挂不住。"
    "不过他愿意请我当然乐意赴宴，而他如果不愿意请那我也绝不会求着他。"
    $ss('no_hat white glasses')
    s"“我说过我可以回请…”"
    $sh()
    des"“这大概不用了，前辈。”"
    des"“等我家里人发生活费来就可以了，只是最近不太行而已…”"
    "Destot小心翼翼的说，他眼睛向上轻轻瞟了我一下，随后又低下头去，像是他欠我什么一样。"
    $ss('no_hat white glasses angry_eyebrow agony_mouth')
    s"“我不是说…不…我的意思是…算了…”"
    $sh()
    "他太过于小心，像是要藏住什么东西一样，虽然别人仅仅通过余光就能把他怀里珍藏的东西一眼看穿，但是总是让人不那么舒服。"
    $ss('no_hat white glasses awkward_eyebrow scared_eyes angry_mouth')
    s"“不行，你总是为我付出，我肯定会觉得不平衡的，这次我请你吃吧。”"
    $sh()
    "其实除此之外我们的开销偶尔还是由我承担的，比如打车的车费，饮料，或者街边小吃之类的。"
    "也许这样做能让他的情况更缓和一点，但相比于动辄几百的餐厅还是太少了。"
    "所以呢，为什么我要为他做这些？明明这些小钱对于他来说就是九牛一毛，你还这么做的原因只是为了让他更喜欢你吗？"
    "不，不…我在想什么呢？"
    "…"
    stop music fadeout 5
    scene street with fade
    "午餐吃完了。"
    "我们之间的话越来越少，能吃的新餐馆也越来越少，我们之间要走到尽头了吗？"
    "我记得之前有一次，我们吃过午饭在公园散步，一直在聊天，走了好几圈都没意识到，回去之后脚就拉伤了。"
    "我们之间越来越熟悉了吗？熟悉之后就会变成这样吗？"
    "到底为什么会这样呢？"
    scene destot_glassdoor with fade
    "我们走进公司的自动玻璃门，当有人靠近时，那扇玻璃门便会从中间打开。"
    "…以前好像一直是，他主动地在和我玩吧。"
    "主动和我出来玩，主动请我吃饭，主动和我找话题，而我一直都是被动地接受他的好意，连回报都是微不足道的。"
    "玻璃门会在有人来的时候主动打开，但如果玻璃门坏了或者没电了，就打不开了。"
    "也许，也许我得找个机会和他谈谈。"
    scene office with fade
    "如果和他说清楚自己对他的实际想法，不希望他再喜欢一个没有必要的人，他应该会好起来吧。"
    "会吗？"
    "我们之后还能一起玩了吗？"
    "但其实更深入地思考，我真的需要一个朋友吗？还是说我只是需要一个可以一直向我输出陪伴和好意的蠢货？"
    "如果要我拿出几百请他吃一顿，能让我感到开心或者值得吗？"
    "…也许不值得？"
    "我，真的把他当成我的朋友了吗？"
    "我，我真的这么自私吗？"
    "…"
    $end_plot()
    if replaying:
        jump afterreplay
    $p.des_p = 4
    jump operate_screen_label
    
    
label destot_route_4:
    $start_plot()
    stop music
    scene black with fade
    "我终究还是来到了这里。"
    "旧城区的老式楼房并没有配备电梯，七楼的高度让我想起了大学时电梯维修的情况，而我们的教室在十一楼。"
    "我有些喘不上来气，想站在门前缓一缓，让自己的状态好一些再进去。"
    "所以，为什么我会那么紧张呢，如果我敲一敲这扇门，我的人生会发生什么不同吗？"
    "他为什么要邀请我来他家呢，有什么事不能在公司或者手机上说呢？"
    "门后的是他的家人？宿友？是他的女朋友？还是男朋友？还是只有他一个人？"
    "我现在才发现，对于他我几乎完全不了解，他喜欢喝什么饮料，吃什么零食？"
    "完全不清楚。"
    "我的心脏不再因为我克服重力来到七层楼的高度而剧烈跳动，待它的频率像平时那样平缓之后，我才开始敲门。"
    play sound audio.door
    show destot with dissolve
    "门开了，他穿着一件灰色的短袖，我突然想起第一次见到他的模样，一个月过去了，一个人的神态真的会变化得如此之快吗？"
    "我不能理解他的表情，不像是单纯的微笑，似乎带了一点紧张。"
    des"“欢迎，快进来吧。”"
    scene destot_home with fade
    "客厅里有一张沙发，一张玻璃茶几，看上去刚刚擦过，但是正对着的电视机上似乎落了很多灰尘。"
    "毕竟是租的房子，不会有什么极具个性的地方，市面上似乎所有的出租中的房子应该都是这个布局。"
    "我扫视着房间的布局，而门右手边的部分就是厨房了。"
    "不过厨房的燃气灶上连个炒锅都没有，操作台上倒是有台微波炉，不过最显眼的应该是立在地上的一大箱方便面了。"
    $ss('normal2_eyes')
    s"“还不错，蛮整洁的。”"
    $sh()
    "我也不知道该说些什么，局面很快就陷入了尴尬之中。"
    show destot with dissolve
    des"“嗯…那个……来我的卧室吧，我想给你看一些东西。”"
    "我眨了眨眼，其实我更好奇他到底找我来想干什么，我其实对他家里有什么东西并不是很感兴趣。"
    "我跟着他往里走，客厅连接着面积不大的走廊，连接着三个门。"
    $ss('normal2_eyes surprised_eyebrow')
    s"“你有室友吗？”"
    $sh()
    des"“…没有，不过我在找合租的人了。”"
    des"“一开始还是觉得一个人住舒服点，不过再来一个也能分摊下房租吧。”"
    "他没看我，语调也有点低落。"
    $ss('normal2_eyebrow')
    s"“哦…”"
    $sh()
    "不知道该回复他什么，也许我当时真的应该再决绝一点，拒绝他的付出。"
    scene destot_bedroom with dissolve
    "他带我来到了最里面的房间。"
    "房间里只有一张普通的单人床，但是旁边的窗台上挤满了花盆。"
    scene destot_plant with dissolve
    play music audio.lithops
    "花盆里并不是花或者草什么的，更像是某种类似芦荟的植物？"
    des"“你知道有种植物叫多肉吗，这些就是，我还挺喜欢的，在这儿养了挺多的。”"
    des"“不知道为什么，就是蛮喜欢的。”"
    "我没有什么特别感兴趣的植物，大概只是因为本身就没有怎么有过栽培之类的经验吧。"
    des"“多肉很好养活，也不太需要水分，晒晒太阳就可以长得很好。”"
    des"“其实我是个很笨的人，养什么都活不成，唯独多肉活下来了。”"
    des"“关于多肉，我最喜欢的就是一种叫‘生石花’的品种。”"
    des"“看上去就像一块埋在土里的绿色石头一样。”"
    "他拿起一个小盆，生石花确实如他所言，像公园的踏脚石一样嵌在土里。"
    "有一些是从中间分为两半生长的，中间有一定的空隙，有些则是在分成两半之后，中间还有一个更小的部分的。"
    des"“你看它像一个石头，但是开花的时候是很漂亮很好看的哦，只不过现在还不是开花的时候。”"
    $ss('normal2_eyes')
    s"“这样啊。”"
    $sh()
    "这些流进我脑中的花卉知识并没有在我的脑海中留下什么印象。"
    des"“你喜欢生石花吗？生石花很有趣啊！”"
    des"“你知道生石花c188和c189有什么区别吗？生石花蜕皮的时候该怎么处理？…”"
    $ss('normal2_eyes surprised_eyebrow scared_mouth')
    s"“啊…我…”"
    $sh()
    "他在说些什么…"
    scene destot_bedroom with dissolve
    show destot with dissolve
    des"“啊…没什么，你应该是喜欢小动物的那种人吧？”"
    $ss('normal2_eyes surprised_eyebrow')
    s"“我偶尔也会养养仙人掌之类的，感觉其实差不多？…”"
    $sh()
    "他叹了口气。"
    scene destot_bedroom_d with dissolve
    show destot with dissolve
    "窗帘突然被拉上，厚重的帘子将窗子，有些雾蒙蒙的太阳光，以及他所有的生石花花盆全部隔离开，挡在后面。"
    des"“前辈，可以坐下吗，坐在我的床上？”"
    $ss('normal2_eyes')
    s"“为什么拉上窗帘？…”"
    $sh()
    "他没回答我，只是站在那里。"
    "我看不太清楚，他应该还是站在那里的。"
    "我坐下了，双腿微微分开，两只手放在两侧支撑着身体，他的床并没有多柔软。"
    "我听见了什么东西落地的声音，随后我便感觉胯间的裤子被他拉拽着往下扯，随后便是他的头挤了进来。"
    "我甚至没有设防，当我的阳具已经感觉到某种温暖又湿热的触感时，神志才反应过来。"
    $ss('scared_eyes surprised_eyebrow angry_mouth blush')
    s"“喂！你干嘛啊！”"
    $sh()
    "被他口腔包围的部分像是处于负压空间一样，我的下体被他紧紧吸附着，舌头的软滑触感出现在阳具每一寸肌肤感受器上。"
    if not replaying:
        $Erection.add(p)
        $Notice.show()
    "我下意识地夹紧双腿，这必然是毫无用处的，我的那东西顷刻间勃起，在他口中抽动着。"
    "爪子用力推着他的头，从爪间传来的柔软的毛发触感提醒了我到底有多久没有像刚见面时那样摸他的头了？"
    $ss('sad_eyebrow sad_mouth closed_eyes blush sweat')
    s"“哈…呼哈…”"
    $sh()
    "无可否认，这确实有点爽，不知道是快感还是紧张的氛围让我心跳加快。"
    "下体似乎马上就要泄出来，和膀胱涨满时急着小便的感觉一样。"
    "被自己的实习生口交是正确的吗？我能射吗？在他的嘴里射出来会是一件丢脸的事吗？为了不射而用力挣脱是正确的吗？"
    "他松口了，随后便是抽泣声。"
    "我没有射，但几乎是差一点就要射了的程度。"
    "那只小兔子抱着我，将他身体的分量依靠在我的身上。"
    des"“前辈…前辈…我…我喜欢你…求你…做我男朋友吧…”"
    $ss('surprised_eyebrow scared_eyes sad_mouth blush sweat')
    s"“…”"
    $sh()
    "我意料到了这种局面，但我没想到有这么快。"
    "随后便只有他抽泣的声音，我却不知道该怎么回复他。"
    "是啊，他请我吃的每一餐肯定不是闲钱太多了随便给我花着玩的。"
    if not replaying:
        $Erection.clearByType(p)
    "我接受了这些馈赠，是否代表着我默认了他的付出，而他也有理由期待着我给予他的回报呢？"
    $ss('sweat')
    s"“我…”"
    $sh()
    menu:
        "拒绝他":
            pass
        "拒绝他":
            pass
        "拒绝他":
            pass
    
    "我呼气。"
    "如果被拒绝了的话，第一次表白就失败的他。一定会很伤心吧。"
    $ss('normal2_eyes')
    s"“虽然我还没有谈过完整的恋爱，但我觉得，Destot……只是因为我在你身边，你才表白的吧？”"
    $sh()
    des"“不…我是考虑过很久的，我…我真很喜欢…真的真的……”"
    $temp = []
    jump destot_route_4_choices

label destot_route_4_choices:
    menu:
        "为什么喜欢我呢？" if 1 not in temp:
            $ss('sweat blush')
            s"“为什么喜欢我呢？”"
            $sh()
            des"“因为前辈很厉害，教我很多东西…”"
            "其实我也只是普通水平的程序员而已，还经常偷懒挨骂。"
            $temp.append(1)
            jump destot_route_4_choices
        "你知道我其实已经和别人谈恋爱了吗？" if 2 not in temp:
            $ss('normal2_eyes sweat blush')
            s"“你知道我其实已经和别人谈恋爱了吗？”"
            $sh()
            if 3 <=max(p.aco_p, p.hal_p, p.dep_p) <= 70:
                des"“…真的吗？…我不知道你已经有喜欢的人了，但是…”"
                des"“虽然有点懊恼，但还是想和你表达我的心情…”"
            elif max(p.aco_p, p.hal_p, p.dep_p) == p.hal_p:
                des"“…我知道，前辈会在周六去A大体育馆打羽毛球吧？那个时候你的手机状态不是wifi，我也是问别人才知道的。”"
                des"“虽然有点懊恼，但还是想和你表达我的心情…”"
            elif max(p.aco_p, p.hal_p, p.dep_p) == p.aco_p:
                des"“…我知道，是和技术总监吧，他在周五会议上经常看向你，你也总看着他，不是吗？”"
                des"“虽然有点懊恼，但还是想和你表达我的心情…”"
            $temp.append(2)
            jump destot_route_4_choices
        "你喜欢我哪里？" if 3 not in temp:
            $ss('sweat blush')
            s"“你喜欢我哪里？”"
            $sh()
            des"“我还记得…你会和我牵手，可能你没注意到，但我在握着你的手的时候，脸都是红的…”"
            des"“真的…真的很害羞，我还是第一次和别人牵手…也…很喜欢…”"
            "只是因为牵手吗？…我其实确实没有想太多，真的只是怕在人群里被挤散而已。"
            $temp.append(3)
            jump destot_route_4_choices
        "抱歉，拒绝了你。" if temp == [1,2,3]:
            $ss('sweat closed_eyes angry_eyebrow')
            s"“抱歉，我拒绝了你……”"
            $sh()
            des"“没什么，我早就预想到这个局面了……”"
            des"“甚至还跟玩了很久的朋友说这事，他就在电话里让我冲冲冲，虽然我自己都没底气。”"
            des"“其实前辈对我没感觉这件事，我早就知道了，只是觉得……可能有一点点可能……”"
            $temp.append(4)
            if p.des_score >= 100:
                jump destot_route_4_choices
            jump destot_route_4_after
        "我们之后还是朋友吗？" if temp == [1,2,3,4] and p.des_score >= 100:
            $ss('normal2_eyes smile_mouth')
            s"“我们之后还是朋友吗？”"
            $sh()
            des"“当然啊！”"
            des"“我们以后还是一起吃午饭，一起工作，一起散步。”"
            des"“以后，如果你反悔了的话，请你一定要告诉我，我会一直喜欢着你的。”"
            jump destot_route_4_after

        
label destot_route_4_after:
    $ss()
    s"“我拒绝你的原因是……”"
    $ss('normal2_eyes normal2_eyebrow')
    s"“Destot其实也不太了解我吧，同样我也不太了解你，一直以来我只把你当成我的朋友看待来着，抱歉。”"
    $sh()
    des"“…嗯…我也抱歉…”"
    $ss()
    s"“所以你在我没有拒绝的时候就流下眼泪了，应该早就猜到了不太可能会成功吧。”"
    $sh()
    des"“…”"
    "他没说话，但我突然才意识到他似乎早就没再哭了。"
    "我不知道他现在什么表情，也许并不好看。"
    "这段时间，因为喜欢我这件事，让他整个人都乱套了吧。"
    "明明知道自己没可能，但还是努力想让我过得好一些。"
    "这次表白也是想结束对我的暗恋和疑问，给自己一个确定的交代，再让自己回归正轨吧？"
    $ss()
    s"“……那么，我要离开了。”"
    $sh()
    des"“…再陪我一会吧？”"
    $ss()
    s"“不了。”"
    $sh()
    stop music fadeout 5
    scene destot_home with dissolve
    "我没再回头，离开了房间。"
    scene black with dissolve
    "穿上鞋子，离开了这间房子，关上了门。"
    play sound audio.doorslam
    "防盗门敲击门框的轰鸣声和锁芯回弹的碰撞声将我的大脑冲洗成空白，而后的沉寂让一切感觉都凭空重新复苏。"
    "该走了。"
    $Achievement550.achieve()
    if p.des_score >= 100:
        $Achievement551.achieve()
    $Achievement.show()
    $end_plot()
    if replaying:
        jump afterreplay
    $p.des_p = 5
    $DestotTask2.lock(p)
    $p.times += 1
    jump after_executing_task_label
    
    
    
label destot_route_5:
    $start_plot()
    "实习生没再来上班了，我也没有再打听过他。"
    "我一直没什么朋友，没了他的陪伴，总觉得很多东西都不一样了。"
    if p.des_score >= 100:
        "或许我不该拒绝他的，或许我应该用另一种说法，可是……"
    "不知道他还是不是仍然住在那个地方，但我也没有脸面去找他了。"
    "我清楚，对于他，我的心里并没有名为喜欢的情愫。"
    "但为什么，却还是感觉如此空虚。"
    $end_plot()
    if replaying:
        jump afterreplay
    $p.des_p = 99
    jump operate_screen_label