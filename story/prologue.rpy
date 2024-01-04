label wakeup_pro:
    $quick_menu = False
    $_game_menu_screen = None
    
    scene black
    if not persistent.nomedicine:
        play music audio.alarm
        scene bedroom with dissolve
    $quick_menu = True

    jump alarmCircle_pro

label alarmCircle_pro:
    if persistent.nomedicine:
        stop music
        show screen screen_dashboard(p)
        jump beforeCircle_pro
    menu:
        "关闭闹钟":
            stop music
            play sound audio.button
            scene bedroom with fade
            show screen screen_dashboard(p)
        "不理会":
            scene black with fade
            $pause(2)
            jump alarmCircle_pro
    $pause(2)
    jump medicineTake_pro

label medicineTake_pro:
    menu:
        "吃药":
            if p.meds() >0:
                $temp = p.mental
                scene cupboard at setcolor with dissolve
                call screen screen_useMed(p)
                scene bedroom at setcolor with dissolve
                if p.mental != temp:
                    "我拿起桌边早就提前盛好水的玻璃杯，将药瓶中的药物吞下。"
                    "……"
                else:
                    jump dontusemed_pro
            elif p.mental>0:
                "已经没有药了吗？"
                "我看着空瓶。"
                if p.today == 5:
                    "今天就可以买更多的了。"
                    "妈的，凭什么我活着就得这么难受。"
                else:
                    "……好吧，马上就到周五了，冷静，冷静，只要少工作多休息就行……"
            else:
                jump ending2
        "不吃药":
            jump dontusemed_pro
        "坚持下去" if p.mental <= 0 and Novice.has(p):
            "……"
            $p.mental = 80.0
            $Novice.clearByType(p)
            jump beforeCircle_pro

    if p.mental < 0:
        "不……不行，头还是很痛……"
        jump medicineTake_pro
    else:
        "也许好点了。"
        jump beforeCircle_pro

label dontusemed_pro:
    if p.mental < 0:
        jump ending1
    else:
        jump beforeCircle_pro

label beforeCircle_pro:
    if p.week==0 and p.day==29:
        jump day0
    elif p.week==0 and p.day==30:
        jump solitus_route_1
    elif p.week==0 and p.day==1:
        jump solitus_route_2
    else:
        jump beforeDay


label day0:
    if p.experience == 'wri':
        jump writer_day0
    stop music fadeout 3
    scene black with dissolve
    "……"
    "“痛苦啊，你从未离开我那贫苦的心之火炉，”"
    "“比最为真挚的恋人更加多情。”"
    "“我知道在我迈向死亡的那一天，”"
    "“你会进到我的内心深处，”"
    "“与我并排躺下。”"
    "——弗朗西斯·雅姆《十四首祈祷诗其六》"
    "……"
    jump solitus_route_0


label solitus_route_0:
    $start_plot()
    play music audio.concretejungle
    scene city with fade
    if not replaying:
        show screen screen_dashboard_calendar(p)

    with dissolve
    "星期五。"
    "A市的街上总是没有什么太多的行人，大概是因为原来只是座港口小城的它突然被某人投资了大量的经费。"
    "原因是什么我们无从得知。"
    "大约是前几年，整个城市都充满了脚手架，曾经的低矮建筑都被蓝色的彩钢墙围起来，变成向外溢出沙土味的工地。"
    "而现在他们也大多建成了，把那个平静安宁的小城转化成了高楼林立的都市。"
    "小时候总羡慕电视画面里的摩天大楼，可当自己真的住上这里时，却并没有觉得多有趣了。"
    "就像他们说的比喻——钢铁森林。"
    "只剩下无情的经济流代替曾经的烟火气。"
    $p.stime(55)
    scene street with dissolve
    "而我是什么呢？"
    "我只是在这高速发展的社会中在地上爬行的败类，无法追上时代潮流的废物。"
    "作为一个普通的程序员，被人戏称为码农，天天做的也只是编写一份又一份无聊的，看着想吐的代码。"
    "曾经还在上大学时的我还能用有限的知识创造出有意思的文字游戏，还能靠着自己的能力稍微赚一点生活费。"
    "但这些对于我的人生，我的事业没有任何帮助。"
    "我的生活不会因为自己那些拿不到大众面前的小作品改变，那些东西也不会成为我能够写在简历上的东西。"
    "它们也吞噬了我的大学时光，我的时间都托付给制作一些不入流的游戏，导致成绩下降，毕业时也没有一个好看的成绩单。"
    "想着就让人难受。"
    "我抬头。"
    $p.stime(56)
    "世界之外存在着一颗不知能燃烧多久的火球，不停朝着我所在的位置投射光明与热量。"
    "如果我……也能成为谁的太阳就好了。"
    "用自己的能力——就算是燃烧自己，只要能做出好的游戏，写出好的文章，让别人看了开心，玩了觉得有趣，那就算是成功了。"
    "到时候也会有人像我看向太阳那样看向我吗？"
    "不……怎么可能呢……我连自己都照顾不好罢了。"
    "虽然病痛让我生不如死……但如果可以，我也好想体验那种被别人需要的感觉呢。"
    "要是能成为他人的太阳，就算{b}燃烧自己{/b}……"
    $p.stime(57)
    stop music
    scene black
    "我患有严重的先天性偏头痛。"
    "感谢当时的医生和我的父母，我从记事开始便就一直使用那种药物来缓解头疼。"
    "即便如此，小时候的我偶尔也有忘记吃药的经历。"
    "但其实也只是那种脑子里的血管鼓胀的感觉，夹杂着剧烈的无法描述的疼痛。"
    "还在我能够忍受的范围。"
    "但第二天醒来的时候，我在床边发现了被自己硬揪下来的毛发，还有在地上已经干掉的暗红色的血迹。"
    "我不敢照镜子，直到现在也是。"
    "同样地，我也没有再断过药。"
    "我家里摆着四五个闹钟，分散在出租房里的不同位置，确保我每天能按时起床，其中两个放在最显眼的桌边。"
    "而装着药的瓶子则矗立在两个闹钟中间，像一座纪念碑。"
    "就连医生也不知道，如果我吃药的间隔超过30个小时以上，我的身体会发生什么。"
    "而且普通的止疼药并没有效果，只有这种药效更加强力的处方药可以抑制。"
    "我甚至还被医院开了证明，否则带着这些白色的粉片连地铁都坐不了。"
    "但毕竟药也是毒。"
    "如果药一直保护我免受头疼，那么它就一定会{b}夺去{/b}属于我的某种东西。"
    "…"
    scene street with dissolve
    $p.stime(58)
    "星期五的下午总是让人觉得意外地安逸，但我并不只是在出门乱走。"
    "如果可以，我其实可以一直躺在床上吹空调来度过这个下午。"
    "但我需要做一些事。"
    "一些必须做的事。"
    "所以我准备去医院，即便医院现在还没法治好我，但他们会在每周五售卖我需要的药物。"
    "但是为什么是每周五？或者为什么其他时候不卖，我一概不知，也没有兴趣知道为什么。"
    "可能这就是我只能处于这个社会底层的原因吧。"
    "另外，我不知道我这种个性算不算自律，但我很喜欢在一天开始的时候计划自己接下来要做的事情。"
    "而且我很不喜欢被搅乱行程。"
    "我喜欢把我能做的事情分为一块一块的名为【日程】的东西，这样我就可以更方便地分配自己上午，下午和晚上要做的工作或者事。"
    "所以你应该也知道了，这周五的晚上我需要做的日程就是【外出】，然后去医院。"
    $p.times = 4
    $plantemp = p.plan
    $p.plan = [DefaultWork, MeetingWork, GoOutside, NoTask]
    "但这并不代表我晚上就只用来去医院，我在剩下的其他时间可以做一些其他的事，也许这就是我不能称我自己为完全自律的人。"
    show screen tutorial_screen_tasks(p)
    "这是我的日程表，不过它并不是“真实存在的”，这只是我脑中的一个想象。\n如日程表所示，每周五，我需要找个时间【外出】去医院买药，除非我今天请假，否则上午和下午我应该都在公司，我只能在下班之后的晚上才能买药。"
    "平时的我在工作日的时候，喜欢提前几分钟去公司，在工位上计划。而放假的话，则在我起床洗漱后开始。"
    hide screen tutorial_screen_tasks with dissolve
    $p.plan = plantemp
    $del plantemp
    "关于我的日程就说到这里好了……"
    scene hospital with dissolve
    $p.stime(16,0)
    "我来到了这里。"
    "A市市立医院。"
    "习惯性地对着门卫抬手而后便放下，因为我每周五都要取新的药，所以他已经对我的到来见怪不怪了。"
    "我不认识的生命们站立在医院门前的广场上。"
    "我也不想认识他们的经历，以及生命轨迹。"
    "能和医院有关联的普通人大多带着小或大的悲伤故事，如果把它们都塞进脑袋里，也许我有一天也会因为把脑浆溅在地上而被新闻报道吧。"
    "我穿过零散的人群，推开医院的旋转玻璃门。"
    $p.stime(1)
    scene hospital_corridor with dissolve
    "这里就像隔绝了外界一样凉爽，到底是空调的功劳，还是在这座建筑里离开人世的幽魂的聚集让这里寒冷异常呢？"
    "我不讨厌充斥在每条走廊的消毒水气味，那更像是人们恐惧的气味，这么想的话就很有趣。"
    "医学的发展也很有趣，生病的人们就应该淘汰掉，而不是像我一样，通过一些干巴巴的化学式变成的药物苟活。"
    "我叹气，走进电梯间。"
    scene elevator with dissolve
    "按下按钮，一间干净空旷的铁盒子便听我的指示在我面前打开。"
    "我经常会想象，如果这东西突然坏掉会怎样。"
    "我被困在人来人往的医院中的电梯里，几分钟，一小时，一天，一个月。"
    "为了活命不得不尝试到处都是的排泄物，直到最后吃掉自己的手臂和腿，互相啃食对方的肉最后皮包骨饿死。"
    "然后腐烂，干瘪，成为一具骨架，最终成为这座医院的一个传说。"
    "我总是在想，想一些没用的事情来消磨自己的人生。"
    "于是几乎是瞬间，我来到了四楼的脑科，会见每周五都会在此坐诊的我的主治医师。"
    $p.stime(2)
    play music audio.solitus
    scene consulting_room with dissolve
    show pathos at sprite_appear
    pathos"“不容乐观。”"
    show pathos angry_eyebrow angry_eyes saying
    pathos"“不幸的是，我们认为你的病症太过特殊，它似乎是因为…”"
    "那只黑色的雄狮一手高举黑色的X光片，另一手推着眼镜说着。"
    "我不在乎我的病理原因，我只知道我的病应该是无论如何都治不好了。"
    "我把头侧过去，望向窗外。"
    show pathos angry_eyebrow angry_eyes normal_mouth anger
    with dissolve
    pathos"“你有没有在听我说话？”"
    show pathos angry_eyebrow angry_eyes normal_mouth anger at near
    with dissolve
    "他从另一侧强行闯进我的视线中，挡住了窗子。"
    "纯黑色的狮子穿着一身白大褂，像是奶油蛋筒顶端插了一块巧克力。"
    "这种黑白的反差很有趣。"
    show pathos angry_eyebrow angry_eyes normal_mouth no_anger at near_
    with dissolve
    pathos"“记得每4周都来复诊，假设这周是第0周，那就是第4周和第8周的时候都各来一次，其他时候的周五我也在这里坐诊。”"
    show pathos awkward_eyebrow awkward_eyes angry_mouth
    with dissolve
    pathos"“至于第12周……先看你能不能活到那个时候吧？”"
    $ss('normal2_eyes sweat')
    s"“……”"
    $sh()
    show pathos angry_eyebrow angry_eyes normal_mouth no_anger
    with dissolve
    if not replaying:
        show screen screen_dashboard_severity(p)
    pathos"“药物能够显著恢复你的精神状态，也就是你的头疼程度，如果低于0，你肯定承受不住这种疼痛的。”"
    pathos"“工作，或者做一些消耗精力的事，以及睡觉到第二天都会消耗大量精神状态。”"
    pathos"“除此之外，药物还能维持你的严重程度水平，也就是你的病情严重程度。”"
    pathos"“严重程度越低，你的所有恢复效果就会越高，专注度也会变高，睡眠消耗以及其他消耗也会变低。”"
    pathos"“不要试图挑战不吃药的结果，如果你害怕就找个人帮你记。”"
    show pathos normal_eyebrow normal_eyes smile_mouth no_anger
    with dissolve
    pathos"“你这样俊俏的小伙子，应该有女朋友了吧，女孩子在这种事上比较细心，你可以让她提醒你。”"
    "我翻了个白眼。"
    $p.stime(3)
    show pathos angry_eyebrow awkward_eyes smile_mouth no_anger
    with dissolve
    "他并没有理会，而是拿起桌上的自动笔，快速地在他手中的单子上划出乱七八糟的线，随后潇洒地按压自动笔顶端，以清脆的咔嚓声结尾。"
    show pathos normal_eyebrow normal_eyes normal_mouth no_anger
    with dissolve
    pathos"“跟以前一样，你的药也准备好了。”"
    pathos"“虽然你已经吃了一段时间Alpha药了，但我还是要再重申一次。”"
    show pathos normal_eyebrow normal_eyes no_anger saying
    with dissolve
    pathos"“Alpha药的最佳使用时间是早上刚起床的时候，其他时候也不是不能用，但效果不如早上吃。”"
    "我稍微有些不耐烦了，于是起身准备夺走那张纸。"
    show pathos surprised_eyebrow surprised_eyes surprised_mouth sweat
    with dissolve
    "但他则把手向后一撤，我的爪子抓了个空。"
    $ss('angry_eyes angry_eyebrow sweat')
    s"“怎么？”"
    $sh()
    show pathos angry_eyebrow angry_eyes normal_mouth anger no_sweat
    with dissolve
    if renpy.get_skipping():
        $_skipping = False
        show pathos head
        pathos"“你是不是在快进，我的话有那么无聊吗？”"
        $_skipping = True
        show pathos no_head
    else:
        pathos"“我敢肯定你刚才没听我说话。”"
    $ss('sweat mood')
    s"“我现在听着呢，说重点。”"
    $sh()
    pathos"“那你听好了，我接下来要说的很重要。”"
    show pathos normal_eyebrow normal_eyes no_anger saying
    with dissolve
    pathos"“你的病情正在逐渐恶化。”"
    pathos"“你需要避免熬夜工作，打游戏等等，这会加剧你的头疼。”"
    $p.stime(4)
    pathos"“虽然你可以吃更多的药来缓解，但是当你把堤坝建得更高的时候，海啸也会越来越高。”"
    pathos"“药物没有明确规定使用时间，但你每天应该至少吃一片，你也可以适当多吃。”"
    show pathos angry_eyebrow angry_eyes anger saying
    with dissolve
    pathos"“另外还有非常非常重要的事！注意听！”"
    play sound audio.knocktable
    show pathos angry_eyebrow angry_eyes anger normal_mouth
    with dissolve
    "这只奶油冰淇淋狮子敲了敲桌子。"
    show pathos normal_eyebrow normal_eyes no_anger saying
    with dissolve
    pathos"“一口气吃很多药，或者只隔两三个小时吃，效果都不好！”"
    pathos"“你至少要等上一片在你体内的药都被肾代谢掉再吃！”"
    pathos"“比如，起床时吃的药下午可以再吃，上午吃的药，晚上睡前可以再吃，如果下午吃了药，晚上就不要再吃了！”"
    show pathos surprised_eyebrow surprised_eyes no_anger angry_mouth
    with dissolve
    pathos"“听明白了吗？”"
    show pathos surprised_eyebrow surprised_eyes smile_mouth
    with dissolve
    pathos"“我来考考你。”"
    menu:
        pathos"“如果早上起床的时候吃了药，至少什么时候可以吃第二片？”"
        "早上":
            show pathos angry_eyebrow angry_eyes anger awkward_mouth
            with dissolve
            pathos"“没错……没错你个大头鬼啊！”"
            pathos"“你这么吃早晚就没了，还不如现在直接从窗户里跳出去！”"
            show pathos angry_eyebrow angry_eyes anger opened_mouth
            with dissolve
            pathos"“一口气吃很多药，或者只隔两三个小时吃，效果都不好！”"
            pathos"“你至少要等上一片在你体内的药都被肾代谢掉再吃！”"
            show pathos angry_eyebrow angry_eyes anger normal_mouth
            with dissolve
            pathos"“比如，起床时吃的药下午可以再吃，上午吃的药，晚上睡前可以再吃，如果下午吃了药，晚上就不要再吃了！”"
            pathos"“听明白了吗？”"
            menu:
                "明白了":
                    pass
            pass
        "上午":
            show pathos angry_eyebrow angry_eyes awkward_mouth
            with dissolve
            pathos"“不对不对，这么点时间不够药物代谢的，你至少要下午再吃。”"
            show pathos angry_eyebrow angry_eyes opened_mouth
            with dissolve
            pathos"“下午！”"
            pass
        "下午":
            show pathos surprised_eyebrow surprised_eyes smile_mouth blush
            with dissolve
            pathos"“没错，看来你确实在听我说话。”"
            pass
        "晚上":
            show pathos surprised_eyebrow surprised_eyes sweat normal_mouth
            with dissolve
            pathos"“你不会是乱说一个时间跨度最久的时间吧？”"
            pathos"“到底有没有在听我说话啊？”"
            pathos"“算了，我就当你听了但是没听懂吧。”"
            pathos"“题目是至少，晚上吃当然可以，但是其实下午就可以吃第二片了。”"
            pass
    show pathos normal_eyebrow normal_eyes no_anger opened_mouth no_blush no_sweat
    with dissolve
    pathos"“总之，还有一个比较重要的事。”"
    show pathos normal_eyebrow normal_eyes no_anger saying no_blush no_sweat
    with dissolve
    pathos"“为了防止一些药物滥用方面的问题，就算你需要吃更多，我每周也不会提供给你更多数量的药。”"
    pathos"“药的保质期只有一周，逾期就不要再吃了。”"
    show pathos surprised_eyebrow surprised_eyes saying
    with dissolve
    pathos"“好消息是你可以试着多做运动，来让你的头疼稍微减轻，也可以让你少吃一点药。”"

    if not replaying:
        show screen screen_dashboard_abilities(p)
    pathos"“左侧的严重程度便是字面意思，代表你的疾病的严重程度，越多就代表你的头疼越严重，这也会影响整体的精神状态恢复等等，总之越低越好。”"
    pathos"“多做运动可以提升你的身体素质，来使你抵抗头疼的能力提升，抵消严重程度的反面效果。”"
    pathos"“其他的能力你自己检查一下就行，点击一下都会有详细说明的。”"
    show pathos awkward_eyebrow angry_eyes saying
    with dissolve
    if not replaying:
        show screen screen_dashboard_effects(p)
    pathos"“另外看你的黑眼圈，你肯定是{color=#ffff00}过劳{/color}了吧？”"
    pathos"“在你屏幕的右侧是你当前的效果栏，效果有很多种，有些是好的有些是坏的，像{color=#ffff00}过劳{/color}就是坏的。”"
    pathos"“层数较少时，持续时间结束不会有什么问题，代表你休息好了，而层数较高的话，持续时间结束就会让你{color=#ffff00}生病{/color}哦？到时候可就麻烦了。”"
    pathos"“放假的时候要多休息，产生一些与之对抗的效果，就能消除{color=#ffff00}过劳{/color}了。”"
    show pathos normal_eyebrow awkward_eyes saying
    with dissolve
    pathos"“还有很多和状态有关的知识，你可以用悬浮鼠标到状态上，如果是手机的话就长按，或者点开状态页面详细地查看，查看这个状态有什么具体的效果，能转化成什么。”"
    pathos"“具体还是需要你自己来学习，如果你不想动脑，点开右边的齿轮图标，也就是设置。”"
    pathos"“将难度调节到简单……虽然简单难度下会获得很多增益，但是也不代表你就无敌了，还是要找机会休息一下的。”"
    show pathos normal_eyebrow normal_eyes smile_mouth
    with dissolve
    pathos"“差不多就这些，如果你没听懂我说的什么或者还想再温习一下就点一下右边的左箭头图标，回退一下，或者点击历史图标。”"
    pathos"“走之前我会给你我的手机号，你可以在有需要的时候给我打电话，有什么问题我都会帮你解答。”"
    "我不清楚我是不是都记下了，但我确实有在听。"
    "但我应该记下来，这就是游戏规则，教我如何苟活在这个世界上的游戏规则。"
    show pathos angry_eyebrow normal_eyes normal_mouth
    with dissolve
    pathos"“我知道活下去很难，如何调整自己的身体，平衡自身的状态之类的，但别灰心，我相信你。”"
    pathos"“当你熟悉了这个世界的一切之后，活下去这件事对你来说就会像是玩过家家游戏一样简单。”"
    if replaying:
        jump afterreplay
    $showNotice(['已解锁新药物！{color=#fe6363}药物{font=arial.ttf}α{/font}{/color}！','可以在医院二楼的药房购买到该药物！'])
    play sound audio.getmedicine
    $p.stime(5)
    scene hospital_corridor with dissolve
    "我手中握着的是写有他字迹的诊断书。"
    "那么下一站便就是药房了。"
    scene hospital_corridor with fade
    nurse"“病人848662号，取药了。”"
    nurse"“需要多少？”"
    show screen screen_dashboard_medicine(p)
    $temp = p.money
    call screen screen_buyMed(p)
    
    

    $p.stime(16,6)
    if temp!=p.money:
        nurse"“给你药。”"
        nurse"“不要忘了下周五医院开门的时候再来取药，也就是上午，下午和晚上，其他时候没有供应。”"
        $ss('normal2_eyes')
        s"“嗯。”"
        $sh()
        "我怎么会忘，忘记了就只能乖乖去死了。"
        "我收下了药房护士递过来的药物，将它放进自己的随身斜挎包中。"
    else:
        nurse"“嗯？不买药？”"
        $ss('normal2_eyes')
        s"“……”"
        $ss('normal_eyes smile_mouth')
        s"“嗯。”"
        $sh()
        "算了，不买了。"
        "我受够了。"
        $Novice.clearByType(p)
        jump ending0
    stop music fadeout 4
    $p.stime(58)
    scene black with dissolve
    $PhysProb.clearByType(p)
    "…"
    "楼道的声控灯总是出问题，但电梯口到防盗门的距离并不远。"
    "我把手伸进斜挎包一侧的小袋，从里面摸出一串钥匙。"
    play sound unlocking
    "左旋，右旋，锁芯发出清脆的金属摩擦声。"
    "于是那门就被打开了。"
    play sound audio.button
    scene livingroom
    $p.onOutside = False
    "我关上门，然后摸开玄关的灯。"
    "光明让我能有机会喘息片刻，但我更喜欢在黑暗中工作。"
    "我脱下鞋，扯开衣服，把工作服丢在架子上。"
    "自己一个人住的好处是不用顾忌在家里穿什么，就像现在的我这样浑身上下只有一件小短裤。"
    "城市入春之后也有一个月了，行道旁也并非是光秃秃的深褐。"
    "现在就连从窗户进来的风也都是温暖且温柔的。"
    "……"
    $p.stime(17,0)
    "难得的假期，在床上趴到晚上好了。"
    $end_plot()
    scene black with dissolve
    $p.newDay()
    $Saver.save(p)
    $Notice.add('存档已保存！')
    $Notice.show()
    call loading from _call_loading_4 
    jump wakeup_pro

label solitus_route_1:
    $start_plot()
    if not replaying:
        $p.times = 2
        $p.stime(13,4)
        $p.onOutside = True
    scene street with fade
    if not replaying:
        show screen screen_dashboard(p)
    play music audio.concretejungle
    "星期六。"
    "虽然我并不是一个会说话的日历，但我其实挺喜欢在脑海里重复今天是放假的日子来着。"
    "A市大学就坐落于我所居住的公寓的附近，与她可以说算得上娇小可爱的校区连接着的是一家体育馆。"
    "虽然算是专属于大学生日常上课用的教室，但其实体育馆也并非是完全属于学校的。"
    "所以校外人员也可以从正门正大光明地进入场馆。"
    "虽然很早就有健身的想法，但自觉自己不是那种能够坚持下来高强度训练的人。"
    "立在路边代表行人通行的绿色指示灯看起来快要灭掉了，注意到这点后于是我便提着挎包踩着斑马线快速通过。"
    "现在仍然是春天，但身上已经开始有些燥热的感觉了。"
    "热风像泼过来的水，只不过把寒冷换成炎热。"
    "啊…"
    $p.stime(5)
    "如果有一天我也变得浑身肌肉，那会发生什么呢…"
    "至少找男朋友肯定轻松多了，就算我不好看，也可以被他们去头食用。"
    "我的视线落在一家文体商店的橱窗上。"

    "自小我就讨厌足球或是篮球。"
    "很多男生喜欢打篮球，仅仅是短暂的课间也要带着球出去，把自己弄得臭烘烘回来，搞得教室里乌烟瘴气的。"
    "我是不明白这种把球丢进高处的篮子里有什么好玩的，也许只是我不感兴趣吧。"
    $p.stime(6)
    "足球也是，初中的时候曾被飞来的足球径直打到头部，直接眼冒金星，差点晕过去。"
    "而高中自己跟着朋友玩的时候，也觉得跑不过他们，也没有太大的精力。"
    "这么说我不就什么都做不了了嘛…"
    "不过有一个我觉得可以尝试。"
    scene store with dissolve
    "我拉开玻璃门，扑面而来的冷风让我感觉自己像一条重新回到水中的鱼。"
    "空调拯救了全世界，太棒了。"
    "忽略店员的问候，我径直走向一侧挂着花花绿绿袋子的架子边。"
    "没错，我觉得也许羽毛球是最适合我的。"
    "不需要满场地乱跑，活动范围只有那半个场地。"
    "挥拍击球也不会消耗很大的力，也不会有危险。"
    "容易上手，但专精有难度。"
    "这太适合我了。"
    "这么想着，我挑了一副蓝色框的球拍。"
    $p.stime(7)
    if p.money < 160:
        "不过难受的是我已经把所有的钱都拿来买药了。"
        "不过我真的有必要把所有的钱都拿来买药吗？还是说我只是在自暴自弃地胡乱消费呢。"
        "以后再说吧，虽然也不知道自己会不会再来买了。"
    else:
        $BadmintonRacket.add(p)
        $p.money -= 160
        $Notice.show()
        if not replaying:
            "我掂量着手中的球拍，转头看了看其他的货物。"
            "随便看看吧。"
            call screen screen_explore_store3(p)
            $p.visitedStore.add(8)
        "我用手机扫码付过钱后，推开了玻璃门。"
        "现在我被刚刚拯救了自己的世界遗弃了。"
        "我望向对面的体育馆。"
        "即便有着想要立刻试试球拍的想法，但今天的温度实在有点高到离谱了。"
        "算了，以后有时间再去看看好了。"
    stop music fadeout 4
    $p.stime(21,40)
    $p.onOutside = False
    scene livingroom with fade
    "…"
    "所以这个周末的假期又过去一半了。"
    "明天就是周日，后天又是周一…"
    "啊…天哪…"
    "趴在床上的我把头埋进被子里。"
    "不对…不对…明天也不算放假，马上就是委托我写东西的委托人设置的截稿日了，而要写的东西还一点没动！"
    "天哪……不想活了……"
    $p.stime(41)
    "是的，我是一个写网络小说的三流写手，擅长写一些自己从来没经历过但在漫画上看过的成人场面。"
    "虽然来约稿的人不多，但也能为自己分担一些开销。"
    "我在床上滚来滚去。"
    "随后又停止翻滚，平躺着盯着天花板。"
    "好累…想死掉了…"
    "明明我今天好像也没做什么的样子…"
    "我转头，看着搭在桌边的装着羽毛球拍的袋子。"
    "现在突然有点后悔了，我这种人能走出屋子就已经达到我最大的运动量了。"
    "我真的能控制住想躺床的欲望跑那么远去练羽毛球吗…"
    "就像之前心血来潮买了健身房的会员卡但一直没去过，浪费了一大笔钱。"
    "唉…我真是废物。"
    $p.stime(42)
    "我继续翻滚，把自己丢到床边，一点一点滚到地上，再翻滚着到门口。"
    "起身关灯。"
    "晚安。"
    $end_plot()
    if replaying:
        jump afterreplay
    $p.newDay()
    $Saver.save(p)
    $Notice.add('存档已保存！')
    $Notice.show()
    call loading from _call_loading_5 
    jump wakeup_pro

label solitus_route_2:
    $start_plot()
    if not replaying:
        $p.times = 2
        $p.stime(13,10)
        $p.onOutside = True
    scene gym with fade
    if not replaying:
        show screen screen_dashboard(p)
    "于是我来到了这里。"
    "A大学的学费并不高，所以学校也不算富裕，从它仍然保持着几十年前的教学楼建筑风格和看着稍微有些破旧的宿舍楼就能看出。"
    "标志性的高层建筑还租给校外人员作写字楼，整个学校的大部分开阔空间也变成了停车位，用来收几块钱的停车费。"
    "我才毕业没几年，而且看上去也不是很显老，我还穿着网上学来的时尚搭配，应该不会被认出来吧。"
    "汗液在我的毛发间分泌，让被帽子覆盖的头顶有些潮热。"
    "为什么我这么狼狈，因为我刚刚才知道如果从体育馆的门进去要身份卡之类的东西，看来我只能装学生了……"
    "我继续步行靠近学校的大门，拿出手机装作忙碌的样子摆弄着屏幕，即便我似乎只是在桌面左右滑动。"
    "我的心脏开始在胸腔中疯狂颤动，似乎要掰开肋骨逃出来一样。"
    "…"
    $p.stime(11)
    "继续走，继续走，看手机不要看警卫…"
    "别拦下我……"
    "…………"
    "呼。"
    "我过来了。"
    "警卫并没有在意我，看来我和这群大学生比也没老到哪里去嘛。"
    "我收起手机，下意识加快步伐溜走。"
    "突然意识到现在自己不该这么快揭开自己的伪装的，不过幸好，警卫并没有发现。"
    "…"
    $p.stime(22)
    scene yard with dissolve
    "进到学校里就舒服多了。"
    "我在小广场中间站定，看着来往的学生。"
    "新生刚刚来到这里不久的样子，学生大多都顶着一张稚嫩的脸。"
    "真可爱啊…"
    "我快速扫视周围的雄性学生，先象征性地看一下脸，再把视线向下，挪到他们穿着短裤的微微鼓起的裆部。"
    "要我说，夏天最棒的就是看着穿短裤的大学男生了。"
    "能看到健壮的小腿，或者旺盛的腿毛，运动鞋脚踝处蔓延出来的白袜，或者仅仅是裸足穿着拖鞋！…一切的一切只要是穿着短裤就很色！…"
    "啊…为什么世界上的雄兽那么多，而没有一个是我的呢？"
    "什么时候我也能有一个穿着短裤的帅哥男友…"
    "操…我不能再像个变态一样看来看去了。"
    "我决定加快脚步，朝着羽毛球场的方向前进。"
    "…"
    $p.stime(23)
    scene court with dissolve
    "羽毛球场到了。"
    "是这座高大但明显非常新颖的综合体育馆的一楼。"
    "用一些小技术搞到了这所学校某个学院的课程表，这个时候大二的计算机院学生应该快上课了。"
    "我把背包放在窗台上，拿出我的球拍，看着逐渐从门口涌入的学生，准备等教师喊集合的时候再起身。"
    "我突然注意到在不远处的球网边，有一个白色的身影正在对着墙打球。"
    show halluke at trans_toRight()
    "他的圆耳朵随着挥拍的动作抖动着，看起来很专注。"
    "似乎是一只白熊啊。"
    $p.stime(24)
    show halluke at look
    "不过怎么会这么矮小，熊兽人通常来说不应该是高大健壮的类型吗？"
    "我把球拍放在窗台边，仔细打量那只白熊。"
    "看样子，完全只有一米六多一点的身高吧？身材也是保持在匀称之上一点点，看着也不是那种娇弱的样子，但也不是那种浑身肌肉的可怕家伙。"
    "倒不如说是那种很可爱的类型，短头发，圆眼镜，看着有些冷淡的样子呢。"
    show halluke at look_
    "唔呜，总盯着人家好像不太好。"
    hide halluke with dissolve
    "我看着某个脖子上挂着口哨的高大中年人朝着场中走去，我也拿着球拍靠近逐渐聚拢的人群。"
    scene black with dissolve
    "…"
    $p.stime(15,30)
    scene court with fade
    "随着体育老师的下课号令，我也跟着其他学生离开了队伍。"
    "他们有的直接离开了场地，有的则继续留在羽毛球场练习。"
    "我呼出一口气，幸好体育课的人比较多，就算没有被点到名字也没人注意。"
    "课上老师大致讲了一些基础的知识，以及接下来的课程需要带羽毛球拍这件事。"
    "看来大概是刚刚开课的呢。"
    scene court_window with dissolve
    show halluke at trans_toRight()
    "我拿着羽毛球拍来到窗台准备把拍子放进球拍袋里，突然发现课前那个矮矮的白熊就在我的左手边。"
    show halluke smile_eyes smile_mouth smile_eyebrow
    with dissolve
    "他看着放在窗台上的手提筐，从里面拿出手机摆弄。"
    $p.stime(31)
    "筐里面似乎是毛巾和一些洗浴用品，还有一双深灰色的塑料拖鞋。"
    "应该是打算打完球再去洗澡吧。"
    "虽然他的样子是我比较可以的类型，但既然都不认识，贸然搭讪应该不太好。"
    "我看着他的后脑勺，他的头发很短，耳朵上架着黑色的眼镜腿。"
    "我试着回想起点名的时候，他似乎也在同一个队伍里上课。"
    "嗯……"
    $p.stime(32)
    "既然在同一个班里，总会有机会的。"
    "哎呀，也不是同一个班，我明明已经不是大学生了。"
    "我回头，在他注意到我之前挪开视线，假装整理自己的东西。"
    "下次点名的时候，稍微注意一下好了。"
    scene court with dissolve
    "我还没有任何认识的人可以和我一起打，场地的羽毛球网似乎也都被占用了。"
    "如果找他的话…"
    $p.stime(33)
    "太害羞了啊，以后再说…"
    "我拿起装着球拍的袋子，踩着其他人的路线离开了场地。"
    scene black
    "…"
    play sound audio.button
    $p.stime(17,33)
    if not replaying:
        $p.onOutside = False
    scene livingroom
    "到家了。"
    "虽然现在还不是晚上，但我应该留给自己一点可供浪费的时间。"
    "看一看“莓博”上面关注的人发了什么。"
    scene meibo_1 with dissolve
    "…“莓博”是一个博客类型的社交网站，博主们可以发他们想发的东西，一些文字，或者是图片，或者是自己的画。"
    "然后别人可以通过评论来互动，也有转发之类的功能…"
    "我打开电脑，从收藏夹里点击“莓博”的网站图标。"
    "我关注了很多画师，因为我很羡慕会画画的人。"
    "而我只会一点点写作，还只能算是平庸的水平。"
    $p.stime(34)
    "大家从会说话开始就在学习写作，而画画不仅需要天分，还需要成倍的努力和道具。"
    "我没有那样的天赋，也没有那样的努力。"
    "我只能通过文字的方式，表达一些无聊的东西。"
    "我的双眼快速地扫过一张张熟悉画风的作品，在感到兴奋之余也不停点赞转发，希望能给他们带来一些新的人气。"
    "…"
    "我的目光停在一个陌生的id上。"
    $p.stime(35)
    scene meibo_2 with dissolve
    "这是一幅短漫，作者的名字并非在我的关注列表中，似乎是某个我已经关注了的画师转发的。"
    "我点进了他的主页。"
    "他的id是赤松Akamatsu，似乎是刚刚才在这个平台注册的账号，现在的他正把之前在其他平台的画搬运到这里。"
    "他画了很多简单的插图和短漫，基本上都关于两个固定的角色，似乎是狮子和狼的故事，演绎一些日常的琐事和有趣的灵感。"
    "画风也简单可爱，类似于简笔画，却又能看出底力所在。"
    $p.stime(36)
    "我保存了图片，同时点击了关注按钮。"
    "不错，期待他能画出更多的新作品。"
    "……"
    scene livingroom with dissolve
    $p.stime(18,44)
    "看了半天莓博，天色已经开始变暗了。"
    "明天就是工作日了，早点休息好了。"
    "我关上电脑，简单冲了个热水澡后上了床。"
    "不，谁会这么早睡觉？只是单纯想趴在床上浪费时间而已——"
    $end_plot()
    if replaying:
        jump afterreplay
    $p.newDay()
    $Saver.save(p)
    $Notice.add('存档已保存！')
    $Notice.show()
    call loading from _call_loading_6 
    jump wakeup_pro

label beforeDay:
    "……"
    if p.week == 1 and p.today == 1:
        "我抓起床边充电的手机，下意识按压侧边键打开手机。"
        "液晶屏幕正对着我的眼球放出刺目的光。"
        "我的视线注视着正中央的时刻数字，还有日期。"
        "又到周一了啊。"
    jump before_go_out