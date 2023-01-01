label halluke_plot_judge_1:  # 羽毛球课程
    if persistent.nocharacterplot or p.hal_p == -1:
        $p.times+=1
        jump TaskExecuting
        
    if p.hal_p > 6:
        scene court with fade
        "解散之后，Halluke便和之前一样，冲到某个还没有被占用的球网边，随后看向我。"
        "那就和他一起打球打到下课吧？"
        $p.times+=1
        jump TaskExecuting

    $jumplabel = 'halluke_route_' + str(p.hal_p)
    $renpy.jump(jumplabel)


label halluke_plot_judge_2:  # 和Halluke打羽毛球
    if persistent.nocharacterplot:
        $p.times+=1
        jump TaskExecuting
    
    if p.hal_p > 9:
        scene court with fade
        "每周一次的羽毛球场约会，但自从在和他确定了关系后就变得和之前不太一样了。"
        "单单说自己是想为了练球才来的是不可能的，但每次击球之前，都能看到他望向这边的十分火热的眼神。"
        "甚至刚才还说出了“没接到球就要和我亲一次”这种奇怪的话……"
        "我知道这本来就是热恋中的情侣会做的事啦……但我总觉得有些……不太自在？"
        "可能我还需要时间吧……明明之前的我也是这样厚脸皮的啊……"
        "到底是哪里不对劲呢……"
        $p.times+=1
        jump TaskExecuting

    $jumplabel = 'halluke_route_' + str(p.hal_p)
    $renpy.jump(jumplabel)


label halluke_route_0:
    $start_plot()
    scene court with fade
    play music audio.badmintonclass fadein 5
    teac"“本次课的内容要讲的差不多就是这些了。”"
    teac"“那么，接下来的活动则是自我练习。”"
    teac"“单人一组，把球丢向空中，然后用手里的球拍击打掉下来的球。”"
    teac"“循环这个过程，练习你们对于接球的熟练度，熟悉了之后，看到球飞过来，基本上不需要思考就能打回去。”"
    teac"“有能力的也可以自己练习，不要什么都不做就好。”"
    teac"“解散。”"
    "…"
    "结束了。"
    "两个球网中间的空位放置了一个纸壳箱，里面都是残破的旧球。"
    "可以随意使用，也可以用自己的好球。"
    "无论如何，小时候还是玩过羽毛球的，但现在还是按照老师的教育程序来吧。"
    "我靠近旧球箱，半蹲下身子在箱子里翻找还算完整的球。"
    "大多数仅仅是羽毛掉了的程度，也有整个的一圈羽毛都掉下来的球。"
    "终于在偏底部的位置找到了一个完整的球。"
    "看上去也仅仅只是旧了一些，羽毛和头部都是完整的。"
    "好，就这样开始练习吧。"
    "…"
    "不对，那个孩子去哪里了。"
    "虽然说孩子，但也应该只比我小几岁而已。"
    "我拿着旧球，眼神扫视身侧开始练习的学生。"
    "…嗯？"
    "居然不在？"
    "记忆中那个小家伙应该站在队里的，怎么解散了就不见了。"
    "不会是偷偷溜掉了吧。"
    menu:
        "继续在前方球场寻找":
            "看他的样子应该不会是会逃课的人。"
            "继续找找好了。"
            "……"
            "好像确实不在……果然是那种不可貌相的家伙吗？"
            scene court_ with dissolve
            pass
        "去厕所看看":
            "应该是上厕所去了吧……"
            scene toilet with dissolve
            "我来到一侧的洗手间，走进男厕。"
            "在顺便解决了排泄的需求后，发现这里似乎并没有其他人。"
            "……那他到底去哪了？"
            scene court
            "……我离开洗手间，回到球场。"
            "……"
            scene court_ with dissolve
            pass
        "观察其他班级的球场":
            scene court_ with dissolve
            "这里的球网基本上都被占用了，也许他去其他的地方玩了。"
            "我转身看向身后。"
            "上次来上课的时候我都没有注意，原来一整个羽毛球场并不都是给我们这个老师负责的班级的。"
            "而是平分给这三个班级的。"

            pass
    show halluke smile_eyes smile_mouth smile_eyebrow
    with dissolve
    "我眯起眼睛，突然发现那个小家伙正站在其他班级的球网处，和另一些人打球。"
    "他看起来很熟练，也很享受。"
    show halluke angry_eyes
    "即便身材相对于其他人来说较小，但爆发力完全不差于他的对手。"
    "当他挥拍击打飞过来的羽毛球时，从他的方向传来一声富有弹性而又清脆的响声。"
    show halluke normal_eyes
    "这证明他的力道正好，球拍击球的位置也完全正确。"
    "反正在我手里是从来没有发出过那样的响声。"
    show halluke shy_eyes
    "我甚至还会在击球的时候，不小心让球碰到球拍的外圈…"
    "他真的很厉害，不是吗？"
    scene court_window with dissolve
    "我把球收起来，朝着靠近他的体育馆窗户边移动，假装自己需要拿东西。"
    scene court_ with dissolve
    show halluke smile_eyes smile_mouth smile_eyebrow sweat
    with dissolve
    "再背靠窗台，拿出手机，装作在看什么东西的模样。"
    "他并没有注意到我，仍然在和也许是他朋友的人们打球。"
    "平时面无表情的他在打球的时候明显舒缓很多，情绪的表露也明显了不少。"
    show halluke angry_eyes
    "比如没有接到球会不太开心，对面没有接到则会自信地微笑，而后快速变回原来的表情。"
    "这种感情流露对于普通人来说并不稀有，但在他身上就十分特别。"
    "虽然我才认识他一天半，但很明显，羽毛球应该是他生命中少有的，能够让他非常享受的事情之一。"
    "我在做什么？虽然现在在做的并不是什么合乎道理的行为，但…"
    show halluke angry_eyes smile_mouth angry_eyebrow at look_1
    "我注视着手机屏幕上那只白熊的动作。"
    "从场地一侧快速移动到另一侧，或者漂亮地把对方的扣杀打回去。"
    "穿着运动鞋的脚踝露出白色袜子的边缘，上身短袖也经常因他的快速移动而翻飞，衣服下的肉体就这样短暂地裸露出来。"
    "稍微有些色情的黑色护膝，还有极短的黑色短裤……"
    show halluke smile_eyes
    "我快速按下手机下侧的快门键，于是带着他的打球动作和美好肉体的照片就这么被我偷偷塞进相册里了。"
    "我咽下口腔内多余的口水，享受背德感和偷窃带来的兴奋。"
    "…"
    stop music
    play sound audio.finishclass
    show halluke angry_eyes normal_mouth angry_eyebrow at look_
    "下课了。"
    "我没想到会这么快，在看了一眼手机的时间之后才发现，已经偷拍他半个小时了。"
    "不过他非常投入，完全不知道这只鬼鬼祟祟的沙漠狼在干什么。"
    hide halluke
    with dissolve
    "我打开手机相册，今天拍的照片的缩略图居然都已经超过一个屏幕了。"
    "虽然自我练习时间里我什么都没干，不过仅仅是接球这种事情…对于我来说估计也不用…补练。"
    scene court_window with dissolve
    show halluke with dissolve
    "我整理好窗台上自己的东西，转头看到那只白熊在摆弄另一个窗台上他的浴筐。"
    "他看起来很认真地确定着里面的东西，时而拿出手机看一会。"
    show halluke angry_eyes
    "现在也许是个不错的搭讪时机，但…还是算了！"
    "我甚至都不知道他的名字叫啥。"
    "…这样好了。"
    "下次点名的时候，注意一下他的名字好了。"
    "我跟随着其他人的路线，朝着羽毛球馆的大门前行。"
    if p.hal_p == 0:
        $p.hal_p = 1
    $end_plot()
    if replaying:
        jump afterreplay
    $p.times+=1
    scene nightrun with fade
    $p.onOutside = True
    "准备回去了。"
    scene black with dissolve
    "……"
    play sound unlocking
    $pause(0.5)
    play sound audio.button
    scene livingroom
    $p.onOutside = False
    jump TaskExecuting



label halluke_route_1:
    $start_plot()
    scene court with fade
    play music audio.badmintonclass fadein 5
    "今天的课程讲解了和挥拍有关的动作。"
    "挥拍的技巧也是很重要的，合适的握拍角度，击球力度，方法都联系到能否持久战斗。"
    "就像我，也许并不是我体质太差，我一直都觉得自己挥起拍一点都不轻盈，很容易就累了。"
    "反过来看，那些似乎擅长击球的人则就很轻盈又准确地击回球。"
    "就像现在的课程，老师所演示的那样。"
    "我和其他学生在球网的两侧站成几排，看着中间的老师做演示。"
    "虽然讲得很专业，但总是没法想象要怎么弄…"
    teac"“那么，大概就是我刚刚讲的那些。”"
    teac"“来一位学生和我演示一下。”"
    "老师看向两侧。"
    "我身边的几个男学生似乎很兴奋，似乎在怂恿一只带着头带的鬣狗。"
    "那只鬣狗单爪握着球拍，而另一爪子则对着其他几个学生挥动。"
    "老师似乎也注意到了他，将浮动的视线固定于那个站在学生中靠前位置的鬣狗。"
    scene court_ with dissolve
    "我没有看那个被迫自告奋勇的家伙，而是将目光往右移动。"
    "那只相对于其他雄性兽人学生要矮很多的白熊和同他一般高的雌性们站在一起。"
    "他也随着其他人看向鬣狗，似乎并没有想要出来演示的想法。"
    teac"“那就你了，看你似乎很有想法啊，你去网的那一边吧。”"
    scene court with dissolve
    "我将目光重新转移到鬣狗身上，他将球网撩起，俯身通过来到网的另一边。"
    "老师从地上捡起一枚羽毛球，挥动球拍将球击向另一边。"
    play sound audio.badminton
    "动作利落而精准，声音充满弹性的力量。"
    "…"
    "啊，鬣狗似乎有点心急，没有接到球。"
    "他捡起地上的球，试图发球。"
    "…"
    "呃，球掉在了地上，他没打到。"
    "应该是太紧张了吧，再加上还有这么多人看着他。"
    play sound audio.badminton
    "他再一次发球，虽然成功了，但当老师再一次以完全标准而又充满美观的动作打回羽毛球时，鬣狗再一次落空了。"
    "这球我上我也能接。"
    "鬣狗似乎很尴尬，看向我身边刚刚对着他起哄的学生们。"
    ha"“老师，我可以吗？”"
    scene court_ with dissolve
    show halluke at trans_toRight()
    "我转向声音的来源。"
    "那只白熊低声对着老师开口。"
    scene court with dissolve
    "鬣狗应该是刚刚偷偷回去了，在老师点过头后，他从球网的一侧绕过去，来到了刚刚鬣狗的位置。"
    "是的，一场势均力敌的战斗。"
    play sound audio.badminton
    "我看着羽毛球在空中流畅地往返，从一侧飞到另一侧，又以几乎相同的轨迹飞回。"
    play sound audio.badminton
    "也许其他人也和我想得一样，他确实是非常厉害。"
    show halluke angry_eyebrow angry_eyes normal_mouth
    with dissolve
    play sound audio.badminton
    "那只白熊的眼神每到战斗时都如同从灰烬中燃起了火焰一般。"
    play sound audio.badminton
    "黑色的瞳孔注视着空中的羽毛球，即便矮小也能瞬间从场的一侧移动到另一侧。"
    show halluke opened_mouth
    with dissolve
    "帅气，又可爱。"
    "要不是老师不许上课用手机，我应该早就拿起手机拍照了。"
    "…"
    "最后是老师结的尾。"
    play sound audio.badminton
    "当球飞过来时，他的球拍一转，将球的冲击力量以一种技巧性的方法化解。"
    show halluke smile_eyebrow smile_eyes smile_mouth
    with dissolve
    "那球便就停留在他的拍上，然后掉落在他的另一只爪子上。"
    teac"“不错，这位同学很厉害。”"
    teac"“想必应该是本来就很擅长的。”"
    show halluke normal_eyebrow normal_eyes
    with dissolve
    ha"“…嗯……”"
    teac"“你的名字是…”"
    "我的耳朵无意识地抖动。"
    h"“Halluke。”"
    "…"
    stop music
    play sound audio.finishclass
    "下课了。"
    teac"“我会给你加分的，Halluke同学。”"
    teac"“那么，这节课就到这里，希望大家空余时间自己多多练习。”"
    teac"“下课！”"
    hide halluke with dissolve
    "…"
    "解散了。"
    "所以他的名字是，Halluke。"
    scene court_window with dissolve
    "我回到窗台，整理着自己的东西。"
    show halluke with dissolve
    "还和之前一样，他似乎并没有因为老师的表扬而高兴多少。"
    "他和我一样，在窗台整理他的浴筐。"
    "…"
    "过去搭讪吗？用什么话题？"
    "“你刚刚好厉害！”，还是“你之前就学过吗？能不能教教我？”…"
    "不，都太蠢了。"
    "……"
    show halluke angry_eyes
    "我抬头，他似乎要离开了。"
    "好吧，也许，也许下一次。"
    "我叹气，离开羽毛球场。"
    if p.hal_p == 1:
        $p.hal_p = 2
    $end_plot()
    if replaying:
        jump afterreplay
    $p.times+=1
    scene nightrun with fade
    $p.onOutside = True
    "准备回去了。"
    scene black with dissolve
    "……"
    play sound unlocking
    $pause(0.5)
    play sound audio.button
    scene livingroom
    $p.onOutside = False
    jump TaskExecuting


label halluke_route_2:
    $start_plot()
    scene court with fade
    play music audio.badmintonclass fadein 5
    "今天的课程结束了。"
    "老师讲解过后便是自由练习时间，发球和接球，两两一组。"
    "我看着队列溃散开来，学生们结群走向空处，边笑边聊，询问和邀伴。"
    "和上周一样，那个孩子仍然在和老师的演示中表现出色，仍然在球场的另一侧，和其他人打着球。"
    "而我在干什么？"
    "我这个无法融入的外来者，杵在人群中，危险地暴露在空旷的原野上。"
    "找不到一同练习的学生，也没有事情可做。"
    scene court_window with dissolve
    "我捏了捏球拍把，感受到了手中的重量，然后有节奏地晃动着球拍走向窗台边，用一种懒散自在的姿态。"
    "…"
    "我把球拍往墙上一靠，整个人搭在窗台上，猛力地吸气。膨胀的胸膛撑起了白短袖。"
    "呼气从口中逸出，而膈肌欲升不升。"
    "我抬起空闲出来的爪子，攥成拳头，用食指突出的关节挤压太阳穴。"
    "在指节的按压下，晕眩感终于被镇压了回去。"
    "白色的身影在我眼角略过，如同救命稻草般把我的注意力从人群中牵了过去。"
    "我叹气。"
    "那，就继续上次那样吧。"
    scene court with fade
    show halluke angry_eyes sweat with dissolve
    "我拿起手机，尽量让自己看起来像是个不训练偷刷莓博的人，屏幕里的画面从单调的橙黄色塑胶地板逐渐开始浮现出他的身影。"
    "我就靠在离他最近的窗台边。"
    "抬高，降低，手上细微的动作都能让镜头内的角度发生大变。"
    "指尖轻触拍照键，白熊便与挥着牌的他交错开，永远地凝固在了我的屏幕上。"
    "没有闪光灯，没有快门声，侧后边也没有人。"
    "那个年轻的大学生运动的身姿就这样拍摄进了我的手机中。"
    "今天天气相对于昨天来说更热，但他的短裤却总是比别人的更短一些。"
    "从可以看出肌肉形状的小腿到露出大半的大腿。"
    "白色运动鞋，脚踝露出恰到好处长度的双黑色条纹的白袜。"
    $Erection.add(p)
    "右腿还缠着护膝。"
    show halluke smile_eyes smile_mouth sweat with dissolve
    "他接球。他跳动。他发球。他手撑着膝盖。他跑去捡球。他张着嘴喘气。他翻起衣服下摆。他对着同组得意地笑。"
    "当他将另一侧对手的扣杀完美地化解后击回，赢得一分。"
    "每时每刻都不一样，都过去而不再回来了。至少此刻的他全都属于我，哪个时刻都不能错失，哪个他都不能少。"
    "是的，这些都在我的手机里。"
    "都在里面。"
    "…"
    "在意识到自己的身体某处发生了某些让人脸红的变化后，我摁掉屏幕，把手机滑进裤袋，快步穿过羽毛球场，来到另一侧的洗手间。"
    scene toilet with dissolve
    stop music fadeout 5
    "…"
    "……"
    "我打开靠里的隔间，疲惫地半瘫坐在马桶上，下巴抵着的胸膛中，心跳声在疯狂地回荡。"
    "感觉自己刚才就如同一个半夜在家里处理尸体的凶手，突然就传来了门铃声。"
    scene black with fade
    "…"
    "所以我来做什么，当然是。"
    "我用手扯下短裤，好让我挺立的狼根呼吸一下外面的空气。"
    "这坨红色的柱子就这么不受控制地在裤裆里充血，逼迫它的主人来照顾他。"
    "虽然说对不起也是没有意义的，毕竟手机里有这么多关于他的照片的我早就是完完全全的罪人了。"
    "借用一下从他身上反射进我手机镜头时留下的彩色图像又有何不可呢？"
    "我用手握住我的阳具，温热，同时完全坚硬。"
    play music audio.masturbation
    "这不同于自己在床上时强迫它立起来时勉勉强强抵达半硬的情况，现在已经完全是100\%充血，就像一艘火箭。"
    "另一只手掏出手机，解锁，然后点开相册，隐藏相册。"
    "于是那个拥有五六十张图片的隐藏文件夹便在我面前展露出它的内容了。"
    "全都是，全部都是他。"
    "那只，叫Halluke的白熊。"
    "我的眼睛扫过偷拍而来的影像，目光在他的脸，身体，腿和裆部之间游走。"
    "露出腼腆的笑容的他和我接吻时会害羞得连舌头都不敢伸出来吗？"
    "胸部是否柔软，乳头是否美味？"
    "脚爪，小腿，大腿…"
    "当我的舌头舔过他敏感的穴口时他会作何表情，发出什么声音？"
    "他的下体是大还是小？敏感到仅仅是摩擦便可射精？是否量大而又美味？"
    "而当我胯下这根阳物进到他的体内时…"
    "…"
    stop music
    play sound audio.door
    "意料之外的脚步声响起，有人来上厕所了。"
    "先暂停一下好了…"
    scene toilet with dissolve
    "我咧开一个不算大的门缝，把眼球从中探出去。"
    show halluke with dissolve
    "便看到白熊站定在左斜方的小便池前。"
    show halluke normalpee with dissolve
    "他把运动短裤轻轻往下一拉，白色绒毛和红色茎柱的交界处就刺入了我的视界。"
    "我看着眼前被白毛包裹着的小家伙，正用爪子扶着柔软的粉色阳物，对着便池排放出尿液。"
    "我屏住呼吸，想听清尿液冲刷在小便池壁上发出的水声，但是什么也没有。"
    show halluke normalpee angry_eyes with dissolve
    "他那手上的动作像是甩了下阳具上的残尿，像每个男人结束排泄一样。"
    show halluke normal with dissolve
    "而后他便在洗手池那里冲了下手便走了，只有我硬挺着鸡巴独自呆在隔间里喘气。"
    $Erection.get(p).end(p)
    scene black with fade
    "…"
    "我扯下张纸巾，苦大仇深地擦干净糊了我一手的精液。"
    scene toilet with dissolve
    "只觉全身疲倦的我从隔间踱了出来，某种可以称之为满足的情绪浮现在脑中，但……"
    scene black
    "我箭步冲回隔间，脑仁如同果冻般在脑壳里面打转，自始至终都存在的尿骚味终于打破了极限。"
    "……"
    "流质涌向了喉管，我忍不住对着马桶呕吐了起来。"
    "…"
    $Pleasure.clearByType(p)
    if p.hal_p == 2:
        $p.hal_p = 3
    $end_plot()
    if replaying:
        jump afterreplay
    $p.times+=1
    scene nightrun with fade
    $p.onOutside = True
    "准备回去了。"
    scene black with dissolve
    "……"
    play sound unlocking
    $pause(0.5)
    play sound audio.button
    scene livingroom
    $p.onOutside = False
    jump TaskExecuting



label halluke_route_3:
    $start_plot()
    scene court with fade
    play music audio.badmintonclass fadein 5
    "这周仍然是击球训练。"
    "仍然是毫无进度的单向追求，仍然是毫无变化的球场。"
    "说实话，最初我到底是因为什么才来到这里的…"
    "明明是想着锻炼身体，可在遇到了那个家伙之后，每次来上课脑袋里就都是他了…"
    "健康的运动和合口味的大学生，本来应该是双份的快乐，怎么会变成这样…"
    "现在的我完全从试图虚心学习羽毛球的社畜变成了偷拍大学生的变态男。"
    "再加上厕所手冲男这一称号，怎么事情就变得这么让人难过呢！"
    "不行，我一定，这周要，和他说话。"
    "场内充盈着男人的气味和淡淡的胶皮味。"
    "和往常一样，几乎所有的球网都被占用了。"
    "羽毛球被球拍击中的富有弹性的闷响，运动鞋踩着塑胶地板的跑步声，交谈还有大喘气的声音。"
    "即便是不运动，单纯来到这里也算是享受了。"
    "那家伙，是叫Halluke的吧，他现在又在哪里打球呢？"
    "我向后看。"
    scene court_ with fade
    "从左到右扫视，再望向后方更远的场地。"
    "…"
    "不应该啊。"
    "经常和他打球的几个熟面孔之中突然多出来一个，顶替他的四人组正平分于我左后方最近的球网两侧。"
    "然后开始打起球来了。"
    "虽然也都是穿着“暴露”的大学生们，但不知怎地并不太能勾起我的什么想法。"
    "可能是我偷拍他拍习惯了，一个相册里放各种人的偷拍似乎也有点对不起Halluke。"
    "…虽然本来偷拍就已经是对不起他了。"
    "但，问题是，这只小熊仔去哪里了。"
    "这才刚刚解散，不会又去上厕所了？"
    scene black
    "我的脑海中突然浮现出上周的事情。"
    "…"
    "呼。"
    scene court with fade
    "不过，既然看不到他，我应该也能专心训练了吧。"
    "果然男人都是害人精。"
    "…"
    "A市大学的羽毛球场并不算大，甚至娇小得可爱。"
    "只容纳了12个球网，每三个网并排在一起，一共四个横排。"
    "有趣的是平时都是三个班上课。"
    "很多情况下在中间上课的班级会霸占六个网，而两侧上课的班级能用的网只有他们的二分之一。"
    "也怪我第一次来就选了最靠南的一侧，也凑巧正好和那只白熊呆在同一个队里。"
    "我挤进球网两侧的人群中。"
    "由于分配不均，三个老师似乎也不太关心这件事。"
    "所以Halluke和他的朋友们也经常去比较舒服的中间区域打球，几乎可以平均分给中间班级的上课人数。"
    "也就是说，最多的情况也只会是四个人用同一个网。"
    "再看看我们，一个网一侧就可能有五六个人个人用，一个球打过来，一群人接。"
    "不过好消息是，这群学生有很多都不是比较喜欢运动的样子，随着时间推移，会有很多人都去窗台边上坐着偷懒。"
    "玩手机，或者单纯坐在那里不想训练。"
    "这也给了我们也勉强组成二对二双打的可能性。"
    "…"
    scene court with fade
    "流汗，深呼吸。"
    "压低重心，将注意力集中在球上。"
    "我握紧手中的球拍，运用那位老师教导的方法。"
    play sound audio.badminton
    "用力挥动，把拍甩出去，随后收力，让球拍在左侧停稳。"
    "恢复预备状态。"
    "…"
    "不错。"
    "这样的练习很棒，我能感觉到自己的短袖内部变得潮湿粘腻。"
    "虽然被汗水浸润的感觉并不太差，但还是清爽干净一点更好。"
    play sound audio.badminton
    "我站在球网一侧，将对面打来的球击回。"
    "对面也完全被我挑起了兴趣，即便球网两侧不只有我和那位学生，但我和他几乎是旁若无人地在进行单打比赛。"
    "…"
    scene court_ with fade
    "这场小型比赛以我的扣杀结尾。"
    "毕竟我也是有一点羽毛球基础的，刚刚我只是故意用比较容易的方式朝着他的方向打球，但总得找个时间结束这场练习赛。"
    "不出所料地，他没有接上我的扣杀，那个羽毛球便高速擦着他的脸侧飞过，掉到了他后方的地面上。"
    "他捡起球，似乎还想和我继续打。"
    "我笑着挥挥手示意结束，毕竟应该也快下课了，手臂也开始有些疲累。"
    "就在我打算去窗台把自己的球拍装回背包里时，我转头。"
    stop music fadeout 4
    scene court_window with dissolve
    show halluke normal2_eyes awkward_eyebrow with dissolve
    "那只白熊正靠在窗台边上，面朝着我的方向观看。"
    "这是我和他的第一次视线交汇。"
    "…"
    "我的脚步也停止了，对视持续了大概一秒。"
    "我该做点什么？"
    show halluke normal_eyes normal_eyebrow with dissolve
    "他的动作很快，低头，然后从裤兜里掏出手机，开始盯着荧光屏用手指按来按去。"
    "而我呢，在他宣告离开对视之后，也再次把交给自己的行动指令恢复成刚刚要做的事。"
    hide halluke with dissolve
    "但，我的脑袋便如同盖上锅盖煮面条一样，泡沫伴随沸腾声从锅和盖子的缝隙中疯狂涌出。"
    "此时的我该抱着什么样的情绪？"
    "偷拍他然后对着他小便自慰的背德感？被陌生人盯着的困惑感？还是尴尬？"
    "这算是我和他之间的进步吗？"
    "我，我以后还要不要偷拍他呢？我手机里的照片该怎么处理，要是某天被他看到了会怎样？"
    play sound audio.finishclass
    "下课铃让我从思绪中回归现实。"
    "我快速收拾好东西，下意识地转头看向右侧。"
    "白熊并没有像往常一样，在那个位置收拾他的浴筐。"
    "……"
    "回家吧。"
    if p.hal_p == 3:
        $p.hal_p = 4
    $end_plot()
    if replaying:
        jump afterreplay
    $p.times+=1
    scene nightrun with fade
    $p.onOutside = True
    "我的心跳得很快，而我却不明白为什么。"
    scene black with dissolve
    "……"
    play sound unlocking
    $pause(0.5)
    play sound audio.button
    scene livingroom
    $p.onOutside = False
    jump TaskExecuting



label halluke_route_4:
    $start_plot()
    scene court with fade
    stop music fadeout 5

    "我们不只一次对视，擦肩而过。"
    show halluke angry_eyes with dissolve
    "他从我身边走过，我从他的身边走过。"
    "我没有再用手机偷拍他了，但我们仍然只像是两个完全没有关联的陌生人一样。"
    "没有说过话，没有开口，没有任何交流。"
    "如果还是难以理解的话，就像是。"
    "你走在路上，突然看到一个路人，和你的朋友很像，于是你下意识地将目光多放在他身上几秒。"
    show halluke normal2_eyes awkward_eyebrow
    "而他则意识到你的注视，将视线挪到你这边来。"
    "你俩对视，但并没有停止行走。"
    "在擦肩而过前，你不再看他，因为你发现你并不认识他，而他也不认识你，所以不再看你。"
    "你俩擦肩而过，似乎刚刚什么都没有发生过。"
    show halluke normal_eyes normal_eyebrow
    "就是这种奇妙的感觉，若是陌生人还好，但因为你和他已经算是“认识”了，这样的行为就显得让人觉得莫名地不舒服。"
    "我拿起球拍，每周都来打球的生活我应该已经厌倦了。"
    "也许下周就不来了，我也确信我应该是没什么希望和一个直男搭讪。"
    "我拿着球，看向球网对面的人。"
    "是他，那个叫Halluke的白熊。"
    show halluke normal2_eyes
    "他正站在我球网的另一侧，以一个合适的理由看着我——等待我的发球。"
    play music audio.meaninglessemotion fadein 4
    show halluke angry_eyes
    "我该感到开心吗？或者是我应该有什么感觉？"
    "就像是，虽然你和他不认识，但你每天每夜都用他的照片缓解欲望。"
    "你享受着这样的平衡，但却被他打断了。"
    "不知所措感，大概是这样吧。"
    "我回忆起课上说过的发球姿势。"
    show halluke normal2_eyes
    "左脚在前，右脚在后，右手持拍向右后侧举起，左手夹住球，举在胸腹部。"
    "我松开手，让羽毛球随重力掉落，我的重心也由右脚转移至左脚，将正好坠落到偏下一点的位置的球以球拍拍面打出。"
    play sound audio.badminton
    show halluke awkward_eyebrow
    "羽毛球在空中拉起一道弧线——不含任何技巧，单纯是为了让他接到而这样击球的。"
    play sound audio.badminton
    show halluke normal2_eyes smile_mouth normal_eyebrow
    "而他却很有攻击性，将球以一种较为快速的角度回击，球此时的轨迹则是直线，径直朝着我的右侧场飞来。"
    "快速反应是运动员最需要掌握的能力，我快速迈步，先右脚越过去，再是左脚，来稳住身体。"
    "同时右手握拍，扭转力度回击。"
    play sound audio.badminton
    show halluke normal_eyes normal_mouth normal_eyebrow
    "从右手手腕传来了震动感和击球声。"
    "球再一次飞向高空，随后向他的场内偏后的位置飞去。"
    show halluke awkward_eyebrow opened_mouth
    "如果他要接这个球，就一定要向后移动，凭他的力气，我估计他应该会把球打到离球网较近的位置。"
    "这样我就可以用较小的力度，来让球落在他那边靠近球网的前半场，他必须以极快的速度意识到到这一情况，再赶回来接球。"
    "可那就已经晚了。"
    "看来还是我技高一筹。"
    "…"
    show halluke normal2_eyes smile_mouth angry_eyebrow
    "球落到了地上。"
    "落到了…"
    "我的地上。"
    "他并没有跑到后面接球，而是一跃而起，在中场接到了我发出的远球，随后用一记扣杀，让羽毛球以高速越过球网来到我的场地。"
    "如果我此时也在中场，是有机会接到这个球的。"
    "但我没有，因为此时的我由于计划，提前来到了球网边等待他从他的后半场击过来的球。"
    "是我输了。"
    show halluke normal2_eyes smile_mouth smile_eyebrow
    "胜利者的脸上自然地流溢着笑容，但作为输家的我却有些伤心。"
    "并不是因为我输掉了，就算我赢了，也真的会让我由衷地感到有趣吗？"
    "明明终于有机会和他一起打球，为什么我开心不起来？"
    "我弯腰捡起球，继续对着球网另一侧的他发球。"
    scene court with fade
    stop music
    play sound audio.finishclass
    "下课了。"
    "我将飞来的球卸力，让他回到我的手中。"
    show halluke angry_eyes with dissolve
    "我看了网对面的他一眼。"
    "到他似乎只是低着头，往我的这边靠近。"
    "终于有机会和他说话了吗…要说些什么呢？"
    "我还在思考，于是看他就这么来到我的身边，与我擦肩而过，去找他的浴筐了。"
    hide halluke with dissolve
    "…"
    "我大概明白了。"
    "我，其实对他来说什么也算不上吧，只是一个随处可见的大学生而已。"
    "那些意外的对视，单打训练，也只是普通人会对陌生人做的很正常的事而已。"
    "在认清楚自己在他心里的地位后，这种狠狠地被抽耳光的感觉就浮上来了。"
    "无论是对着裆部看，对偷拍来的照片发泄欲望，偷窥小便自慰之类的，这些事情都是建立在我对他只有欲望这方面的需求上才有的。"
    "但我已经见到他好多次了，有一个月了吧？"
    "当产生一些其他的情愫后，再回望那些行为，却皆是如此的不堪。"
    "这种本来是单纯想和他上床的欲望，到底是什么时候变成了想认识他，想了解他，想拥抱他的欲望的呢。"
    "…"
    "即便我再喜欢他，我所做的一切对他来说也几乎没有意义，我永远也没法走进他的生活中。"
    "永远都只能是个局外人。"
    "停止幻想吧。"
    "我叹口气。"
    "几乎是瞬间，仿佛握着手中球拍的力量都遗失了。"
    "也许下周不会再来了。"
    "是时候做好脱离和他的关系的思想准备了，也防止未来的自己继续折磨自己。"
    "……"
    if p.hal_p == 4:
        $p.hal_p = 5
    $end_plot()
    if replaying:
        jump afterreplay
    $p.times+=1
    scene nightrun with fade
    $p.onOutside = True
    "准备回家了……"
    scene black with dissolve
    "……"
    play sound unlocking
    $pause(0.5)
    play sound audio.button
    scene livingroom
    $p.onOutside = False
    jump TaskExecuting



label halluke_route_5:
    $start_plot()
    scene court with fade
    stop music fadeout 5
    "还是下定决心再次来到这里了。"
    "呼吸，呼吸。"
    "稳定情绪。"
    "只要情绪稳定了，脑袋就没那么痛了。"
    "也许是因为做事要有始有终，也许是因为到这里应该可以学到更多的运动技巧，总之因为某些原因，我还是说服了自己来到这里。"
    "但我只是感觉很疲惫。"
    "课上的训练逐渐变得越来越多，虽然刚开课的时候老师也带着做热身训练，不过运动强度并不算大。"
    "但现在已经入夏了，外面的空气都是热的，更别说只能靠开窗开门通风的羽毛球场馆。"
    "再加上强度直线上升的准备运动，每次做完这好几十次的反复跳跃后，整个大腿都变软了。"
    "宝贵的周末…这样的天气里的我应该躺在空调房里咬冰棍，而不是在这里把自己腿跳到残废。"
    "唉。"
    "我站在队伍靠后的位置，这样偶尔偷懒也不会被老师发现。"
    show halluke with dissolve
    "而Halluke在我的左手边，站在第一排。"
    "我能看到他裤子的屁股那里露出来的一小股尾巴。"
    "白色的绒球。"
    "……真想捏捏啊。"
    "…"
    "我突然意识到自己又开始产生一些不必要的想法，便不再看他，把精神专注在老师的口令上。"
    "…"
    scene court_ with fade
    "终于结束了…"
    "做完准备运动后腿已经不想动了，但紧接着准备运动的又是羽毛球的挥拍和接球动作练习。"
    "熬到了自由活动时间的我坐在长凳上，用包里的毛巾擦去额头上的汗液。"
    "是不是没吃饱午饭啊，感觉要低血糖晕过去一样迷糊…"
    play music audio.halluke
    show halluke normal_eyes with dissolve
    "我抬头，却发现那只白熊正在我的身边。"
    "他一手拿着看上去就十分专业的球拍，另一手按压着他自己的肩膀。"
    show halluke normal2_eyes with dissolve
    "眼神则与抬起头来的我对接。"
    "我有些呆住。"
    "即便我已经看过他生殖器的样貌和打球时偶然露出的小腹，以远或近在不同角度偷拍过他，但和他对视这么久却是第一次。"
    "我看着他的眼睛，仅仅是看着他的眼睛就让我心跳加快。"
    "我控制着自己的目光向下挪到他的胸部裆部或者是脚踝之类的什么地方，仅仅是回应着他的目光与他对视。"
    "多好笑，上周刚刚黯淡下来的好感，仅仅是片刻的对视就让我完全重燃起来，甚至还引起我那么多的想法。"
    "我和他就这样对视了许久。"
    "他好像有什么话要说，但一直没有开口。"
    "现在正是最好的时机，最好的第一次开口的时机。"
    $ss('normal2_eyes')
    s"“来打球吗？”"
    $sh()
    show halluke awkward_eyes with dissolve
    "我起身，对着他说出了我和他之间的第一句话。"
    "不包含任何多余的情感，完全隐藏了我的激动，喜欢，欲望，以及一大堆乱七八糟的东西。"
    "虽然很突然，但是也许这种自来熟的打招呼方式应该也是最能够让他接受的吧…"
    show halluke normal_eyes sweat with dissolve
    "当这几个字真真切切从我口中说出，以声音的形式传递到这个世界，传递到他的耳中，同时也传递到我的耳中这一刻。"
    "我莫名想起了名为《创世纪》中的创造亚当一画中的上帝和亚当的手指对接。"
    "我从未想过对喜欢的人说话时，内心是如此心惊胆战，小心翼翼的。"
    "他听到我的声音，转头看向我。"
    show halluke awkward_eyes awkward_eyebrow with dissolve
    "他微张口，几乎就要说出来话了，但是还是什么都没说出来。"
    $ss('awkward_mouth sweat')
    s"“嗨，那个就是……要不要打羽毛球？……就，和我打……”"
    $sh()
    "有点尴尬。"
    "我感觉我的毛发里正在流出汗来。"
    show halluke normal_eyes awkward_eyebrow blush with dissolve
    h"“…行啊。”"
    "应该是他刚刚没听清我说什么吧。"
    show halluke normal2_eyes normal_eyebrow blush with dissolve
    "他点头。"
    "看来成功了。"
    "明明是他先来盯着我想要约我打球吧，怎么突然变成我先开口了。"
    "总之万事开头难，我已经和他说过第一句话了，接下来再怎么搭讪也不会被当成奇怪的人了吧？"
    "他回头看着羽毛球场地，我随着他的视线也看到了位于角落的一个没有人使用的球网。"
    show halluke smile_mouth shy_eyes normal_eyebrow no_blush with dissolve
    "他转头来看着我，似乎在等我拿球拍。"
    "我转身下意识看了看阳台，突然想起自己好像把球拍随手丢地上了。"
    "嗯…"
    "我捡起球拍，跟着他往那个球网移动。"
    "距离那个地方还有一段路程，接下来就是要发挥我主观能动性的时候了。"
    $ss('normal2_eyes blush smile_mouth')
    s"“你打的很厉害。”"
    $sh()
    "非常无聊的一句搭讪，看起来就像是那种没话找话的无聊客套。"
    "但我真的觉得他打的很厉害，但要是说得太过热情太过仰慕，效果还不如这个。"
    show halluke opened_mouth awkward_eyes awkward_eyebrow with dissolve
    "他迅速转过头。"
    show halluke smile_mouth normal_eyes awkward_eyebrow blush with dissolve
    h"“…谢谢。”"
    "他又转过去，对着他的球拍了。"
    "不过仅仅是这不到一秒的时间，还是被我看到了他脸上下意识要笑出来的样子。"
    "真是单纯可爱的孩子啊。"
    "我跟在他后面，如此贴近他让我眼中他的身高变得十分矮。"
    "真想抱抱他呢，但就算是直男间的搞怪，现在也不是时候。"
    "总之，我和他终于迈出了第一步。"
    "就算没法做爱人，只是和他做朋友的话也让人满足。"
    show halluke smile_mouth normal_eyes normal_eyebrow no_blush with dissolve
    "他已经站到球网的另一边了，而我则展开架势，准备接从他那边发来的球……"
    "……"
    stop music fadeout 5
    if p.hal_p == 5:
        $p.hal_p = 6
    $end_plot()
    if replaying:
        jump afterreplay
    $p.times+=1
    scene nightrun with fade
    $p.onOutside = True
    "准备回家了……"
    scene black with dissolve
    "……"
    play sound unlocking
    $pause(0.5)
    play sound audio.button
    scene livingroom
    $p.onOutside = False
    jump TaskExecuting


label halluke_route_6:
    $start_plot()
    scene court_window with fade
    stop music fadeout 5
    "很难相信这周我又来到这里了，"
    "不过时间真快啊，我已经来这里上课快两个月了。"
    "期间但也是学到了一些有用的知识，至少不会再随便地挥来挥去了。"
    "体育馆内仍然吵吵嚷嚷，不过似乎在说结课的事情。"
    "…"
    "我凑近了些听。"
    "大概应该是还有三四周的样子就要结课了，到时候会考试，丢球接球什么的。"
    "反正我不是学生，到时候在一边摸鱼就好了吧…"
    "我坐在窗户附近的长凳上，把球拍立在墙边，"
    "自由活动时间也快过半了，应该快有空下来的球网了，"
    "Halluke运气还不错，刚解散就已经占据了一个球网的位置，现在他还在和他的朋友们打球。"
    "这几位实力似乎都很厉害的样子，小白熊愿意和我打还真是委屈他了…"
    "算了，玩会手机吧等他吧。"
    "…"
    scene court_window with fade
    "当我刷完莓博上的新博文后，突然发现他们已经结束了。"
    "最开始还是双打，现在已经变成单打了。"
    show halluke smile_mouth with dissolve
    "Halluke一个人挑战他们三个，仍然充满干劲的样子。"
    "…诶…真好啊。"
    "不过要是前几周的我，现在已经凑到附近开始偷拍了吧。"
    "…"
    show halluke angry_eyebrow angry_eyes angry_mouth with dissolve
    "嗯哼？"
    "他们似乎不再打了，相对于其他几人较矮的Halluke仍然拿着球拍，嘴里似乎在说什么。"
    show halluke normal_eyebrow angry_eyes sweat normal_mouth with dissolve
    "但其他人回应了他的话之后就跑到靠近他们那边的长凳上休息了。"
    "Halluke也只能把球拍放在一边。"
    "哎呀，现在是不是应该我登场，像白马王子一样邀请他打球？"
    "噢…等等…"
    "他在做什么？"
    "我看着那只白熊。"
    hide halluke with dissolve
    "此时的他突然坐在窗台附近的空地上，似乎在想什么事。"
    "随后便开始进行俄罗斯转体，收回伸长的腿成三角形，两只手握在一起，随着上身转动将手带到身体的两侧。"
    "而后是卷腹，随后又是平板支撑。"
    "好厉害啊，虽然…"
    "现在仍然是上课时间，他身边的球网还有人打球呢，居然不会感觉尴尬吗？"
    "不过说实话，从外表上看他似乎又矮又软绵绵的，不过也能看到从短袖袖口中露出来的手臂也带着肌肉形状。"
    "这也是他能够接住我打得很偏的球——从场的一侧跑到另一侧，也能发出速度很快的扣杀的原因吧。"
    "想必他的衣服下肯定也是一具充满力量感的身体吧。"
    "…"
    play sound audio.finishclass
    scene court_window with dissolve
    "下课铃响了。"
    "看来我就这么一直看着他锻炼一直到了下课。"
    "本来还想叫他再打一会球，不过…"
    "…"
    play music audio.halluke fadein 5
    show halluke with dissolve
    $ss('normal2_eyes smile_mouth happy')
    s"“嗨。”"
    $sh()
    show halluke normal2_eyes with dissolve
    "我靠近他，他还是像往常一样，弄他的浴筐。"
    "在听到我的声音后也转过头来。"
    show halluke angry_eyes with dissolve
    "他的眼神仍然带着点困惑，不过很快就明亮起来。"
    show halluke normal_eyes with dissolve
    "想必是在回忆我到底是谁这件事上想了半天。"
    $ss('normal_eyes smile_mouth mood')
    s"“啊，记不清我是谁的话，我是上周课下课前和你打了一会球的那个…”"
    $sh()
    show halluke normal2_eyes with dissolve
    h"“噢…”"
    "他盯着我，尴尬的感觉上来了…"
    $ss('surprised_eyes surprised_eyebrow smile_mouth sweat')
    s"“诶，你刚刚打球打的好厉害啊…”"
    $sh()
    "…我要说什么来着？…"
    show halluke normal_eyes sweat with dissolve
    h"“嗯…谢谢……”"
    show halluke normal2_eyes with dissolve
    "他微微低头，但很快又恢复直勾勾的对视。"
    "天呐…他不会说别的话吗？"
    "啊，想起来了，我是想多和他见几面的…"
    $ss('sweat')
    s"“那个，你平时会自己练球吗？我听说这里的羽毛球场不上课的时候也开放，也不用交场地费。”"
    $sh()
    show halluke normal_eyes sweat with dissolve
    h"“不会…”"
    show halluke normal2_eyes with dissolve
    "他看起来有点匆忙，又有些慌张，是急着回去还是也觉得尴尬想快点说完？"
    "他似应该是那种不太擅长交流的人吧，不过到了球网边，又像变了个人似的…"
    "打赢了会笑得很可爱，咧开嘴笑，输了又会有些气馁，对着空气挥两下拍像是出气…"
    $ss('normal2_eyes normal2_eyebrow smile_mouth blush')
    s"“我的意思是，那…要不要，来一起打球？”"
    $sh()
    show halluke awkward_eyebrow awkward_eyes opened_mouth no_sweat with dissolve
    "他似乎有些惊讶，我注意到他的瞳孔正微微放大。"
    $ss('normal2_eyes normal2_eyebrow smile_mouth blush')
    show halluke awkward_eyebrow awkward_eyes normal_mouth with dissolve
    s"“周末来这里打球，怎么样？”"
    $sh()
    show halluke normal_eyebrow normal_eyes sweat with dissolve
    h"“……”"
    show halluke normal2_eyes with dissolve
    $ss('normal_eyes normal_eyebrow blush')
    s"“你那个时候应该没有课吧…”"
    $sh()
    show halluke normal_eyes with dissolve
    h"“…没有…”"
    $ss('normal2_eyes normal2_eyebrow smile_mouth blush')
    s"“那要来吗？”"
    $sh()
    show halluke smile_eyebrow normal2_eyes smile_mouth with dissolve
    h"“唔，好。”"
    "他似乎变得很紧张，也许我不该拦住他的。"
    "不过来都来了，还是把话说清楚吧。"
    $ss('awkward_eyes awkward_eyebrow smile_mouth mood blush')
    s"“我都没说什么时候，你就同意了？”"
    $sh()
    show halluke awkward_eyebrow awkward_eyes opened_mouth blush sweat with dissolve
    h"“我…我……”"
    "他似乎更紧张了。"
    show halluke awkward_eyebrow normal_eyes opened_mouth blush sweat
    "于是这样一个比我大约矮二十公分的可爱学生，就这样站在我面前不知所措。"
    "真想趁他现在这个状态把他扒了衣服猛干。"
    "不过这里是球场，还是算了。"
    $ss('awkward_eyes awkward_eyebrow scared_mouth mood blush')
    s"“好吧，对不起，我可能说话有点……那个，总之！”"
    $ss('normal_eyes normal_eyebrow scared_mouth no_mood blush')
    s"“加我的某信，快下课了就不耽误你了，晚点联系我就好。”"
    $sh()
    "我掏出手机，给他展示了有自己信息的二维码。"
    "这样他就可以通过某信找到我了。"
    show halluke normal_eyebrow normal2_eyes normal_mouth blush no_sweat with dissolve
    "他似乎缓和了一点，拿出了手机。"
    "我看着他握着手机的小爪子在微微颤抖，控制着手机屏幕进入扫码。"
    show halluke shy_eyes smile_mouth blush with dissolve
    h"“这样…可以吗…”"
    $ss('normal2_eyes normal2_eyebrow smile_mouth blush')
    s"“嗯，一会手机上聊哦。”"
    $sh()
    "我对他招了招手。"
    "他也招了招手，随后快速便跑到窗台附近。"
    show halluke normal_eyes normal_eyebrow normal_mouth blush with dissolve
    "当我快要离开场地的时候，他还没有离开。"
    "而是聚精会神地盯着手机。"
    "……"
    stop music fadeout 5
    if p.hal_p == 6:
        $Message.new(p, 'Halluke', 'Halluke', '你好，我的名字是Halluke，如你所见，我在和新认识的朋友说话的时候很容易紧张，有时候连话都说不出来，并不是因为我故意想这样的……总之对不起，可能和我说话这件事让你觉得很困惑吧。\n周日下午，怎么样？我会在体育馆等你的。', h=16, m=50)
        $HallukeTask1.unlock(p)
        $p.hal_p = 7
    $end_plot()
    if replaying:
        jump afterreplay
    $p.times+=1
    scene nightrun with fade
    $p.onOutside = True
    "准备回家了……"
    scene black with dissolve
    "……"
    play sound unlocking
    $pause(0.5)
    play sound audio.button
    scene livingroom
    $p.onOutside = False
    jump TaskExecuting


label halluke_route_7:
    $start_plot()
    scene court with fade
    play music audio.brightanticipations fadein 5
    show halluke smile_mouth sweat with dissolve
    "也许可以称之为一场特别的约会。"
    "虽然我已经快累倒了，这小家伙看上去还和刚进体育馆那时候差不多，仅仅只是脑门上多了点汗而已。"
    $ss('scared_eyebrow sad_eyes sad_mouth sweat mood')
    s"“抱歉，抱歉，让我休息下吧…”"
    $sh()
    "我已经没力气接下他这一发球了，索性把球拍丢在一边，直接躺在地上。"
    show halluke awkward_eyebrow normal_mouth with dissolve
    "…浑身酸痛，如果可以，我感觉我几乎能直接在羽毛球场地睡着。"
    "我只是坐在地上大口喘气。"
    show halluke normal_eyebrow normal2_eyes normal_mouth with dissolve
    "他从球网的边缘走过，来到我的场地，轻而易举地用球排将地上的球以一种我永远学不会的方式，让球像粘在他的拍上一样从地上被抬起。"
    "我用双手反支撑着自己，看向走进窗边的小白熊，只见他从背包里掏出一瓶水和一个运动水壶，朝着我的方向走来。"
    show halluke smile_mouth with dissolve
    h"“口渴了就喝吧。”"
    show halluke smile_mouth at sit
    "他走到我的身边，也坐在地板上。"
    "先是把矿泉水瓶放在了我的旁边，接着又打开那个运动水壶自己喝着。"
    $ss('sad_mouth sweat blush')
    s"“…好贴心啊，知道我没带水来…”"
    $sh()
    show halluke normal2_eyes with dissolve
    "我拿起塑料瓶，拧开盖子就往嘴里倒。"
    "…从没感觉过自己有这么渴，只是遵从基于本能的吞咽动作，一瓶没开封的水就这么被我一口气喝光了。"
    show halluke normal_eyes with dissolve
    "随后便是继续喘气，只不过喝了水之后，感觉舒服多了。"
    $ss('normal2_eyebrow normal2_eyes smile_mouth sweat blush')
    s"“谢啦，Halluke。”"
    $sh()
    show halluke awkward_eyebrow shy_eyes opened_mouth at near
    "我翻滚到他的腿边，脑袋躺在地上看着他。"
    "他的口微张，咬着运动水壶的壶嘴。能看到他的脖颈处扩张又收紧做吞咽动作，有水从他嘴边漏出来，形成略带点色情意味的嘴角水渍。"
    "这样近距离观察可比偷拍好多了，我甚至能闻到他身上淡淡的汗味。"
    "他知道我正看着他，但他此刻在想什么呢？"
    "只要我做更越界的直男，那么尴尬的就不是我。"
    "也许他在想，自己不能那么敏感，仅仅是被看而已，没必要大惊小怪的。"
    show halluke blush normal_eyes normal_mouth with dissolve
    "或者是我的目光让他有点不自在，但为了礼貌还是假装不在意。"
    "无论如何，他只是在喝水而已，脸却变得微微红润起来。"
    "真是太可爱了。"
    "他终于喝完了，把运动水壶放在旁边，开始喘气，同时故意避开我的视线。"
    "即便我的头已经贴在了他的大腿边。"
    show halluke blush normal2_eyes at near_
    h"“…休息好了没…”"
    $ss('smile_eyebrow smile_eyes scared_mouth blush')
    s"“没有噢，还是好累啊。”"
    $sh()
    h"“…”"
    show halluke angry_eyes angry_eyebrow angry_mouth with dissolve
    h"“那我去找别人打。”"
    $ss('surprised_eyebrow smile_eyes awkward_mouth mood')
    s"“别别别，我已经休息好了！”"
    $sh()
    "我直接从地上蹦起来。"
    show halluke blush normal_eyes normal_eyebrow smile_mouth with dissolve
    "Halluke的嘴角微微上扬，从旁边捡起他自己的球拍。"
    h"“说说而已啦…来吧。”"
    show halluke angry_eyes angry_eyebrow smile_mouth with dissolve
    "我把脑门上的汗擦下去，重新让仿佛碎成几百节的身体动起来。"
    "毕竟是我邀请他来的，现在，现在还不能临阵脱逃啊！"
    "加油啊！你可以的！"
    "我扭了扭胳膊，重新捡起球拍，架起准备接球的姿势。"
    "…"
    stop music fadeout 4


    if p.hal_p == 7:
        $p.hal_p = 8
    $end_plot()
    if replaying:
        jump afterreplay
    $p.times+=1
    scene nightrun with fade
    $p.onOutside = True
    "准备回家了……"
    scene black with dissolve
    "……"
    play sound unlocking
    $pause(0.5)
    play sound audio.button
    scene livingroom
    $p.onOutside = False
    jump TaskExecuting




label halluke_route_8:
    $start_plot()
    scene court with fade
    play music audio.brightanticipations fadein 5
    "中场休息时间。"
    "有时候我真的觉得这个小家伙的精力是无限的。"
    show halluke sweat with dissolve
    "我接过他递过来的矿泉水，继续将大量的透明液体灌进嘴里。"
    "再次将一整瓶矿泉水咽下肚后，我下意识地发出舒适的喘气。"
    $ss('normal2_eyes')
    s"“Halluke。”"
    $sh()
    show halluke normal2_eyes sweat with dissolve
    h"“嗯？”"
    "这只坐在地上缓慢喝水的小熊在听到我的声音后转过头来。"
    $ss('normal2_eyes scared_mouth ques')
    s"“突然想问……为什么你能打这么久还不累呢？”"
    $sh()
    show halluke awkward_eyebrow angry_eyes no_sweat with dissolve
    h"“…身体好…吧……”"
    $ss('normal2_eyes smile_mouth')
    s"“有多好？”"
    $sh()
    show halluke normal_eyebrow normal2_eyes with dissolve
    "当我随口说出来这句话的时候，才意识到自己好像说错了什么。"
    "或者说是说对了什么…"
    "我借势靠近他，试图用手抓他的运动短袖想要向上拉。"
    show halluke awkward_eyebrow angry_eyes sweat with dissolve
    "不过经常打球的人就是反应比较快啊，在我伸出手的一瞬间就向后躲开了我的手，还顺便把他的水壶盖上盖子了。"
    "我还不甘心，怎么能错过如此机会。"
    "我继续向他的身体进攻，本坐在地上的我像抓逃走的小猫一样朝着他的方向扑。"
    "即便他左躲右躲，我还是抓到了他短袖的一角。"
    "假装自己是直男是每个南通的必修课，我想我现在的表现完全可以给我发最佳直男奖了。"
    "越厚脸皮，越觉得自己做的事没什么，就越能揩到更多的油。"
    "此时的他正坐在地上背靠着球网栏杆，而我的双腿则拦在他伸直的双腿两边，支撑着我比他高了不少的身体跪坐在他的身体上方。"
    $ss('angry_eyebrow angry_mouth')
    s"“给我康康！”"
    $sh()
    show halluke awkward_eyebrow normal_eyes opened_mouth sweat belly with dissolve
    "抓着他短袖一角的我的手向上扯，于是他的腹部光景便尽数收入我眼中了。"
    "他的腹肌并不算明显，甚至可以说是十分可爱的大小，但也并非没有。"
    "哎呀，我做的是不是有点过火了？"
    show halluke awkward_eyebrow angry_eyes angry_mouth no_blush with dissolve
    "我本想摸一下，但他似乎只是紧紧地盯着我的…下腹？"
    $ss('agony_eyebrow closed_eyes angry_mouth sweat em')
    s"“嗷！”"
    $sh()
    show halluke smile_eyebrow angry_eyes smile_mouth normal with dissolve
    "一股剧痛从蛋蛋处传来，我感觉整个人都飞了起来。"
    $ss('awkward_eyebrow normal2_eyes awkward_mouth sweat mood')
    s"“呜呜呜呜…下手好重…”"
    $sh()
    "不对，应该是下腿。"
    "在地上疼到打滚的我如此想着，这可比头疼疼多了啊！"
    "只见Halluke坐在刚刚的地方，只不过他的膝盖立了起来。"
    "想必他就是用那带着护膝的膝盖给我来了一下爆蛋攻击吧…"
    show halluke normal_mouth with dissolve
    h"“哼…”"
    stop music
    play sound audio.drop
    "不过突然好像传来什么东西掉在地上的声音。"
    "我回头，Halluke已经起身，但他的护膝却掉在地上了。"
    $ss('scared_mouth ques')
    s"“怎么了？坏了吗？”"
    $sh()
    "感到疼痛缓解了的我不再打滚。"
    show halluke awkward_eyebrow awkward_eyes normal_mouth with dissolve
    h"“…带子断了…”"
    "不会是刚好因为踢了我那一下才直接给弄断了吧？我的蛋蛋有这么硬吗…"
    show halluke awkward_eyebrow angry_eyes normal_mouth with dissolve
    h"“我去丢掉。”"
    $ss('scared_mouth normal2_eyes')
    s"“等等，只是断了带子而已，换上新的还能用吧。”"
    $sh()
    "他捡起护膝。"
    show halluke normal_eyebrow normal2_eyes with dissolve
    h"“买个新的不就好了？”"
    "我迅速起身。"
    $ss('scared_eyebrow sad_eyes angry_mouth sweat')
    s"“啊……那个……”"
    $sh()
    play music audio.heartbeat
    "终于可以对着他的贴身物品打手冲了吗？"
    "虽然我的大脑不擅长即时反应，但我只能努力想个借口拿到这东西……"
    menu:
        "虽然我的大脑不擅长即时反应，但我只能努力想个借口拿到这东西……{fast}"
        "现场帮他修好":
            $ss('scared_eyebrow angry_mouth sweat')
            s"“很容易修的！就，把那里的带子重新穿回卡扣……”"
            $sh()
            show halluke awkward_eyebrow angry_eyes normal_mouth with dissolve
            h"“感觉挺麻烦的……还是丢了吧，都用了很久了……”"
            "看来这招不行……"
            $ss('scared_eyebrow normal2_eyes sad_mouth sweat')
            s"“那就送给我吧？可以给我吗？…我挺早就想要买个护膝了……这个旧的就给我吧！我修一下还能用！”"
        "说自己也想买护膝":
            $ss('scared_eyebrow normal2_eyes sad_mouth sweat')
            s"“就是……我挺早就想要买个护膝了……然后，那这个旧的就给我吧！我修一下还能用！”"
        "说想要他的贴身物品拿来自慰":
            $ss('scared_eyebrow normal2_eyes sad_mouth sweat blush')
            s"“就是……其实我想用你的护膝……”"
            $sh()
            "什么啊！我怎么能说这种话！"
            $ss('scared_eyebrow normal2_eyes angry_mouth sweat')
            s"“就是……我挺早就想要买个护膝了……然后，那这个旧的就给我吧！我修一下还能用！”"
        
    $sh()
    show halluke awkward_eyebrow angry_eyes normal_mouth with dissolve
    h"“可是…”"
    show halluke normal_eyebrow normal2_eyes with dissolve
    $ss('angry_eyebrow angry_eyes smile_mouth sweat blush')
    s"“别可是了，给我就好啦…”"
    $sh()
    stop music
    "我从他手里抢过护膝，他似乎也没有要抢回去的意思。"
    show halluke awkward_eyebrow awkward_eyes with dissolve
    h"“呃……”"
    "他看我的眼神十分微妙。"
    "这时我才感觉到，手中这一美妙的护膝是有多么地沉重。"
    play music audio.brightanticipations fadein 4
    show halluke normal_eyebrow normal2_eyes with dissolve
    h"“那……休息够了吗…”"
    $ss('normal2_eyebrow normal2_eyes smile_mouth')
    s"“嗯嗯…”"
    $sh()
    show halluke smile_mouth with dissolve
    "我喘口气。虽然裆部还在隐隐作痛，但和我的头疼一比也不算什么了。"
    "我将抢来的旧护膝放进背包里，拿起球拍准备继续战斗。"
    "…"
    stop music fadeout 4

    if p.hal_p == 8:
        $HallukeItem1.add(p)
        $p.hal_p = 9
    $end_plot()
    if replaying:
        jump afterreplay
    $p.times+=1
    scene nightrun with fade
    $p.onOutside = True
    "准备回家了……"
    scene black with dissolve
    "……"
    play sound unlocking
    $pause(0.5)
    play sound audio.button
    scene livingroom
    $p.onOutside = False
    jump TaskExecuting



label halluke_route_9:
    stop music
    $start_plot()
    scene yaxuefensi with fade
    "Halluke用单手握着筷子在黑色的碗中搅动，用筷子尖挑起一簇粉丝抬到空中，不紧不慢地朝着上面吹气，随后再送进他的口中。"
    "或许他并没有注意到我正在看着他，因为他的瞳孔此时向下，看着放在他腿上的手机。"
    "有时候我看着他一开一合的嘴唇，会很想和他接吻。"
    "但既然我已经走到了这里，也应该做好喜欢一个直男的觉悟——是偷偷摸摸这样观望，或是再也忍受不了做朋友，最后被当成怪物，从此断绝关系。"
    "但，如果是他的话…"
    "他仍然不紧不慢地把浸湿褐色汤汁的粉丝咬进嘴里，而我却突然没什么食欲，只想看着他。"
    "如果是他的话，应该也能接受…吧……"
    "也许有一天我该和他坦白，也许我……"
    play music audio.halluke fadein 5
    show halluke smile_eyebrow angry_eyes with dissolve
    h"“你不吃吗？”"
    "意识到自己正在对着桌上的凉拌鸭肠发呆的我因他的声音突然回过神来。"
    $ss()
    s"“稍微有点烫，我晾一会。”"
    $sh()
    show halluke normal_eyebrow normal_eyes with dissolve
    h"“…哦…”"
    "然后他就继续开吃了。"
    "这里是位于A大门口附近的一家鸭血粉丝店，经济实惠也好吃，但是人气似乎并不是很高。"
    "即便如此，在我听说他也很喜欢来这家店的时候，也是十分地惊讶。"
    "所以今天打完羽毛球后就来这里吃晚饭了。"
    $ss('normal2_eyebrow normal2_eyes smile_mouth')
    s"“突然好奇Halluke平时打完球会做些什么呢？”"
    $sh()
    show halluke normal2_eyes with dissolve
    "并不是我想刻意搭讪，只不过嘴边突然冒出来这句话。"
    h"“…学习，或者睡觉吧…”"
    $ss('sad_eyebrow normal2_eyes')
    s"“哦…”"
    $sh()
    show halluke normal_eyebrow normal_eyes with dissolve
    "我将筷子插进有些坨了的鸭血粉丝碗里搅了搅，把方方正正的鸭血块戳碎。"
    "其实仔细想想，哪会有朋友主动要陪着他打球，还带他一起吃晚饭的…也许他已经知道我喜欢他这件事了？"
    "我眼前的小白熊正捧着碗喝汤，而我还没怎么吃。"
    "…我和他的未来，会是什么样的呢…"
    show halluke awkward_eyebrow normal2_eyes with dissolve
    h"“还不吃吗？”"
    "Halluke看着我。"
    "似乎这是他第一次主动关心我。"
    "我明白这可能只是朋友间的随便聊聊，但是这也算一种…表达他是在意着我的！"
    "这让我感到有些害羞。"
    $ss('sad_eyebrow normal2_eyes blush')
    s"“没什么…就是……想和你……做比较好的朋友…”"
    $sh()
    "我到底在说什么啊………"
    show halluke awkward_eyebrow awkward_eyes with dissolve
    h"“啊…”"
    "他突然沉默了，似乎在思考我说的话，我甚至能听到从他脑袋里传出来的齿轮运作声…开玩笑的。"
    show halluke normal_eyebrow angry_eyes with dissolve
    h"“说真的…我其实只有你一个朋友。”"
    h"“其他人，也就仅仅只是认识的关系。”"
    $ss('sad_eyebrow normal2_eyes scared_mouth')
    s"“这样吗…我看你也经常和别人有说有笑的？”"
    $sh()
    show halluke awkward_eyebrow awkward_eyes with dissolve
    "他低着头，"
    h"“和你在一起我不会感觉很紧张。”"
    h"“我挺害怕和别人说话的，但是跟你说话，感觉能…说得比以前多一点……”"
    "这算赞赏吗？还是肯定？我现在应该说什么？"
    show halluke normal_eyebrow normal2_eyes with dissolve
    h"“然而我还不知道你的名字，我们好像都没有好好自我介绍过吧。”"
    show halluke smile_mouth with dissolve
    h"“叫我Halluke吧。”"
    "啊……糟了，虽然已经和他打球这么多次了，我之前偷偷知道了他的名字，忘了他还不知道我叫什么。"
    "平时完全都是靠眼神交流的。"
    $ss()
    s"“……我，我的名字是……”"
    $ss('smile_mouth normal2_eyes')
    s"“[p.name]。”"
    $sh()
    show halluke awkward_eyebrow awkward_eyes with dissolve
    h"“好。”"
    "虽然花了很长时间，但我们现在已经能像朋友那样正常聊天了。"
    "也许我应该更勇敢点才行，至少先把脑子里那些无用的顾虑先清除掉。"
    "我晃晃脑袋，低头用筷子夹起一大坨粉丝塞进嘴里。"
    "…"
    scene foodstand with dissolve
    "即便已经接近秋天，A市的气温还是居高不下。"
    "看来吃鸭血粉丝不是一个好主意，在三两口吞下热汤之后，现在已经是满身汗的状态了。"
    show halluke sweat with dissolve
    "Halluke看上去也有些热的样子。"
    "路边有冰淇淋摊。"
    $ss('smile_eyes smile_eyebrow smile_mouth sweat')
    s"“Halluke，要吃冰淇淋吗？”"
    $sh()
    show halluke smile_eyes awkward_eyebrow sweat with dissolve
    h"“啊…可以啊。”"
    "我带着他靠近冰淇淋摊。摊主笑着接待我们。"
    $ss('normal2_eyebrow normal_eyes smile_mouth happy')
    s"“草莓还是奶油？”"
    $sh()
    "我看向身边这只小白熊，他却面带紧张地回看向我。"
    show halluke normal_eyes cry_eyebrow sweat with dissolve
    h"“草莓…奶油…啊…你帮我选吧，我其实都行。”"
    "这家伙不会有选择困难症吧？不过口味问题还需要选择吗？"
    $ss('normal2_eyes scared_eyebrow')
    s"“嗯？喜欢什么就吃什么，也不是我能帮你决定的呀…”"
    $sh()
    show halluke angry_eyes cry_eyebrow angry_mouth sweat with dissolve
    h"“…啊……”"
    "三人此时陷入了诡异的沉默之中。"
    "大概是过去了几十秒后，身边的人才说出他想要草莓口味的。"
    show halluke cry_mouth with dissolve
    h"“那我要一个草莓的。”"
    $ss('normal2_eyebrow normal_eyes smile_mouth')
    s"“我要个奶油的。”"
    $sh()
    "摊主对这段似乎是在耽误他做生意一样的延迟回复也没有厌烦的样子，随后便熟练地用冰淇淋机打出两个甜筒。"
    show halluke normal_mouth with dissolve
    "我提前付了钱，所以现在也能空出手来把甜筒递给Halluke。"
    show halluke normal_eyes normal_eyebrow normal_mouth sweat with dissolve
    h"“…谢了…”"
    $ss('normal2_eyes normal2_eyebrow smile_mouth blush')
    s"“两块钱而已啦，请你吃的…”"
    $sh()
    show halluke angry_eyes normal_eyebrow normal_mouth with dissolve
    "熊用两只手握着冰淇淋，小口地咬着粉红色的冰淇淋顶，但他的表情却十分复杂，并不像是开心，更像是思考着什么。"
    "不过我也不想多问，可能是太热了的原因吧。"
    stop music fadeout 4
    if p.hal_p == 9:
        $p.hal_p = 10
    $end_plot()
    if replaying:
        jump afterreplay
    $p.times+=1
    scene nightrun with fade
    $p.onOutside = True
    scene black with dissolve
    "……"
    play sound unlocking
    $pause(0.5)
    play sound audio.button
    scene livingroom
    $p.onOutside = False
    jump TaskExecuting


label halluke_route_11:
    $start_plot()
    $BadmintonClass.lock(p)
    scene ingym with fade
    stop music fadeout 5
    $p.stime(18,20)
    "……"
    "我推开体育馆的玻璃门。"
    "和往常的周末一样，来使用场馆的学生把这里围得水泄不通。"
    "即便天已经黑了，还是有很多学生在门口转悠。"
    "我记得，他有时候会拎着拍兴致冲冲地往人堆里挤，完全不怕他那小个头在人堆里被那些急着抢位置的学生挤爆了。"
    "有时候就跟在我后面，我来推开人群，来让我和他一起进去。"
    "可是，明明前些日子还是一起打球的好队友，怎么会突然这样呢？"
    "…我继续向前，越过面向校外人员的登记台，径直往楼道里走。"
    "塑胶和男人汗臭的味道在高温之下让人十分不适。"
    "我还记起，刚见到他的时候，手机里对着他偷拍的情景。"
    "但努力了这么多，也在一起打球这么久，凭什么…"
    scene court with fade
    "我走进位于二楼的羽毛球场馆。"
    $p.stime(18,25)
    $ss('sad_eyebrow angry_eyes angry_mouth anger')
    s"“Halluke！”"
    $sh()
    
    show halluke awkward_eyebrow awkward_eyes cry_mouth sweat with dissolve
    "即便他身在离门最远的球网。但在我喊出他名字的时候还是突然愣了一下。"
    "我能看到朝他飞去的球落在了地上。"
    show halluke normal_eyebrow angry_eyes normal_mouth no_sweat with dissolve
    "他看向这边，如同凝固了一般。"
    "他身边的人似乎在和他说什么，转而又看向我的方向。"
    "我并不在乎别人的目光，我只是朝着他去。"
    "我能感觉到一股底气，一股具有侵占性的情绪，一股火热。"
    "这些东西支撑着我的身体，让我前进。"
    "成为我愤怒的来源，成为我的力量。"
    show halluke normal_eyebrow normal_eyes normal_mouth with dissolve
    "这段距离只有大约二十几米远。"
    "我能感觉到，看向我的人越来越多。"
    "我应该羞愧吗？正常人会这样做吗？"
    "打开大门，大吼一声，目中无人地从别人的球网两侧径直穿过。"
    "不，那都不重要了。"
    show halluke cry_eyes with dissolve
    "我走近了他。"
    "他长得不高，但我和他越是靠近，这种跨度就越明显。"
    "他正站在我面前，也许是不敢，才看向一侧。"
    "我该做什么？"
    "骂他，为他删自己的好友，为他毁掉了这一脆弱的关系，为我和他的人生轨迹从此永远都无法再度相交。"
    "我抬手，抓住了他的衣领。"
    play music audio.meaninglessemotion
    show halluke angry_eyes with dissolve
    h"“对不起，如果你生气了，就揍我吧。”"
    show halluke tear with dissolve
    h"“然后…就不要再来了。”"
    "是啊，发泄愤怒吧，发泄愤怒吧。"
    "我能感觉到肌肉充血的火热，还有激动带来的血压上升感。"
    "我的心在疯狂跳动。"
    "我松开了抓着他领子的手。"
    show halluke normal_eyes with dissolve
    "他似乎想说什么。"
    "但我不想给他任何机会。"
    "我弯腰，用悬他胸前的那只手抓住他的脖颈，强行将他的下颚上抬。"
    "而我则贴上他的嘴唇，与他干涩的唇接吻。"
    "他在挣扎。"
    show halluke closed_eyes with dissolve
    "我的手没有松开，另一只手扶住他的后脑，朝着自己的方向按压。"
    "同时努力撬开他齿，让温热的舌相互交融。"
    "他要逃跑。"
    show halluke closed_eyes blush cry_mouth with dissolve
    "我的手更紧了，简直像是要把他整个人压进自己口中。"
    "我们就这样，在陌生人，在他的朋友面前接吻。"
    show halluke angry_eyebrow angry_eyes angry_mouth with dissolve
    "他努力挣脱了我。"
    "我呼吸。"
    "面对着他大口地呼吸。"
    "口中仍残留着他的余味。"
    $ss('sad_mouth agony_eyebrow blush')
    s"“这就是，我从你身上想要的全部。”"
    $ss('normal_mouth normal_eyebrow blush')
    s"“我已经满足了，你不会再看到我了。”"
    $sh()
    show halluke awkward_eyebrow cry_mouth no_tear with dissolve
    "…"
    "是的。"
    "从一开始就是，我只是个凭胯下的东西来偷拍他的罪犯。"
    "陪他打球，我也只能做这种事。"
    "他不擅长交流，说话又总是需要思考一会。"
    "他是一个，我永远没法染指，没法把深夜里对着他照片的幻想实现的人。"
    "但我打破了规定。"
    "无论他喜欢异性还是同性，厌恶或者喜欢，我觉得这就是我所渴望达到的真实了，之后要发生什么也与我无关了。"
    "该离开了。"
    "…"
    show halluke cry_eyebrow normal_eyes opened_mouth with dissolve
    h"“别走。”"
    show halluke angry_eyebrow normal_eyes cry_mouth tear with dissolve
    h"“你以为这样对我做了这种事，就可以这么走掉吗。”"
    "我停下了脚步，回头看着他。"
    "至少是此刻，我还有勇气抵抗周围人的围观和异样眼光。"
    stop music fadeout 5
    "他把地上的球拍和零散的东西收拾起来，随后抓着我的手腕，牵着我的身体朝着大门方向离开。"
    $p.stime(18,40)
    scene gym_night with dissolve
    "他一直也没有抬头看过我一眼，就这样，我们离开了这座体育馆。"
    "即便外面的空气比场馆内的胶皮味好多了，但我还是没什么心情。"
    "没想到他第一次牵我手的情形居然是这样的。"
    "他就这样扯着我的手，一直把我拉到了学校外的马路边。"
    "我们一直都没有互相开口，仅仅只是在路边站着。"
    "他要做什么？"
    "我看向他，却只能看见他的后脑勺而已。"
    "我不敢多说。"
    "这场特别的牵手持续了几分钟，我就像个喝多了酒寻衅滋事的犯人，而这位矮我二十多公分的警察狠狠地抓着我的手，仿佛下一秒我就要逃跑。"
    "直到一辆出租车停在我们两个面前，他的抬高并摇摆着的另一只手也随着车子的熄火而放下。"
    show halluke angry_eyes tear with dissolve
    "他终于回头看向我了。"
    "但他的表情，我没法看出任何东西。"
    $p.stime(18,45)
    hide halluke with dissolve
    "…"
    "他打开车门，上了前座，也终于放开了我的手，警察终于解开了我的临时镣铐。"
    "那么也代表，我可以趁现在就此逃离这个地方，从此再也不来到这个大学附近，就像他所希望的那样。"
    "但是，我不想这样，也许他真的有什么话要说。"
    "于是我上了车。"
    scene incar with dissolve
    "…"
    play sound audio.cardoorclose
    "我关上车门。"
    "也许Halluke早就提前在手机上写好了目的地地址，或许司机会读心，只是从上车一直到现在，两人，包括司机在的三个人里，都没有人说话。"
    "我只听到从车窗缝隙里流进来的风声，还有引擎发动中的声音。"
    "车里的汽油味让我感到眩晕，我只好按下车门上的按钮，让玻璃完全降下来。"
    "在冷风的吹拂下，我终于安静下来了。"
    "如果让我现在去亲他，都不用在体育场，就算跑到只有我和他在的地方，我也没那个勇气。"
    "…也许那就是愤怒的力量吧，由我幻想出来的背叛而形成的怒火。"
    "但，Halluke到底想让我做什么呢？"
    "也许只有下车之后才能知道了。"
    "当我从内心的意识低语中脱离，重新回到现实世界时，我发现车子正在减速，而窗外是一栋公寓。"
    "…"
    "Halluke从车上下去了，那我也下车吧。"
    play sound audio.cardooropen
    "我把车门拉开，从车上出来。"
    scene haloutside with dissolve
    "…"
    $p.stime(19,00)
    show halluke angry_eyes at darken(-0.7) with dissolve
    "出租车走了，黑暗的小区里，只有我和Halluke两人。"
    "我看着他，他看着我。"
    "他的表情已经不再像当时那样崩溃，或者可以称之为崩溃的表情。"
    show halluke normal2_eyes with dissolve
    "他向我伸出手。"
    "那我能怎么办呢，我只能握住他的手，仅此而已。"
    "…"
    "这次他抓着我的手不再那么用力，而且也不是抓着手腕，而是普通的牵手。"
    "……"
    scene black with dissolve
    "他正在我的前面，拉着我一步一步趴着这栋旧公寓的楼梯。"
    "他没有说话，我也没有说话。"
    "他只是牵着我一直往前，我也一直往前，跟着他的脚步。"
    "楼梯间只有我和他的脚步声。"
    "直到我和他停在4楼的楼梯口。"
    "他对着左侧的门，掏出钥匙开始解锁。"
    "…"
    play sound unlocking
    "所以…他带我，来到了他的家里？"
    "…要我见他的父母？还是什么？他家里是什么情况？"
    "不不…我还没有准备好，如果我见到他的父母应该说点什么？我是他的同学？室友？可他什么专业我都不清楚！"
    "…"
    play sound audio.button
    show halluke angry_eyes with dissolve
    h"“进来吧，家里只有我一个人。”"
    $ss('sweat')
    s"“…噢……”"
    $sh()
    "这是他离开学校后说的第一句话，他也真的猜到了我现在正在担心什么。"
    "我越过门槛，走进了他的家里。"
    $p.stime(19,10)
    scene halhome with dissolve
    "…"
    "他的家里十分简单，能从客厅直接看到厨房和卧室的门，而且面积看起来也十分小。"
    "不过总体上比较整洁，也没有什么奇怪的味道，和外界的下水道气味完全隔绝了。"
    show halluke angry_eyes with dissolve
    $ss('normal2_eyes')
    s"“带我来这里，是要做什么？”"
    $sh()
    show halluke normal_eyes with dissolve
    h"“我……我有很多话想和你说，真的。”"
    $ss('sad_eyebrow surprised_mouth surprised_eyes')
    s"“我在听。”"
    $sh()
    show halluke angry_eyes with dissolve
    h"“……”"
    play music audio.halluke
    show halluke normal_eyes with dissolve
    h"“如果你那样对我的话，肯定也说明你也是同性恋了。”"
    h"“我一直以来担心的事也终于平静下来了……”"
    show halluke angry_eyes with dissolve
    h"“总之，谢谢你愿意跟着当时脑袋乱成一锅浆糊的我回到我自己的家，在这里我能感到舒服点，也能让我更放松说出来我想说的话…”"
    h"“我……先从我自己开始说起吧。”"
    show halluke normal_eyes with dissolve
    h"“像我这样的大学生应该住在寝室吧？但我却住在外面。”"
    h"“因为我的家里人觉得，寝室里的人会带坏我，直接就带着我办了走读的手续，让我在学校附近租了个小单间。”"
    h"“初中高中都是如此，家里甚至禁止我和学校里的人打交道，经常作为考试第一名的我，他们认为我没必要和别人交流什么。”"
    h"“为我好，为我好，可我现在面对陌生人连你好都不知道怎么说。”"
    show halluke angry_eyebrow angry_eyes with dissolve
    "愤懑在他脸上浮现，但很快就转化为无奈。"
    show halluke normal_eyebrow normal_eyes with dissolve
    h"“但我其实也已经习惯了，没人关心我的想法，也没人注意我在做什么，不需要我做决定，就算我做决定也没人会听。"
    h"“也许是那样的环境，没什么人和我说话，我也不会表达自己的想法。”"
    h"“你肯定也在大学宿舍呆过吧，大家除非有什么共同爱好或者其他的联系，其他情况下基本上应该只和自己寝室的室友玩得好才对。”"
    h"“像我这种又不在寝室又不懂的交朋友的，就完全没人可说话。”"
    show halluke angry_eyes with dissolve
    h"“就算和别人打羽毛球的时候也是，他们在和我打完羽毛球之后也就和自己的朋友离开了。”"
    h"“我打得好，对面输了不愿意，我打的差的话，对面可能就不会选我了。”"
    h"“我很喜欢打羽毛球，这让我看起来不像个被永久沉默的怪物，即便很难掌控技术，能和他们在运动的时候小说几句话我就很开心了。”"
    h"“但并没有那么多学生真的喜欢羽毛球，只是因为这个运动简单不累又好拿学分而已，我和他们也没有在课外的时候打过。”"
    show halluke normal_eyes with dissolve
    h"“后来我遇见了你。”"
    h"“…你也很厉害，但我最初单纯只是觉得你和他们一样。”"
    show halluke angry_eyes with dissolve
    h"“但你，在学校的时候有在主动想找我打对吧，我还不至于这个都察觉不到。”"
    h"“之后甚至主动和我聊天……我真的很惊讶，但我不敢做出太大的动作，也不知道该和你说什么来让你经常陪我玩……”"
    show halluke normal_eyes smile_mouth with dissolve
    h"“后来你甚至和我约在课后练球，我真的很……开心。”"
    show halluke angry_eyes normal_mouth with dissolve
    h"“从来没人这样关注我。”"
    h"“但是自从和你打了很多次之后，我开始害怕了。”"
    h"“虽然我也可以和同学打，但是总是没有和你打的那种感觉。”"
    show halluke normal_eyes smile_mouth with dissolve
    h"“你会关心我，不会故意打难为我的球，还逗我开心，和我闹来闹去的。”"
    h"“还有打完球之后一起出去吃的东西。”"
    h"“我都记着，我都很感激。”"
    show halluke angry_eyes with dissolve
    h"“但是就是这种…细腻的东西，让我喜欢上你了，但也让我开始怀疑自己…”"
    h"“因为我从来没有这样活过，这让我感到恐惧。”"
    h"“从没有人这样关心我，我怕我会完全依赖上你。”"
    show halluke tear with dissolve
    h"“但我根本不了解你这位根本不属于我们学校的人是什么来头。”"
    h"“在这门课程结束之后，我们便失去了能够一起沟通的东西，说不定你就再也不会来到这个体育馆了，我们也再也没机会一起打球了。”"
    h"“也许你只是个喜欢找厉害的人打球的家伙，对我的喜欢完全没兴趣。”"
    h"“也许你想和我做朋友的直男，但总有一天你会发现我的取向，然后离开我。”"
    show halluke normal_eyes with dissolve
    h"“我已经无法自拔地沉浸在这种能被人关照的日子了，如果让我回到过去我一定会崩溃的，我再也找不到像你一样在乎我的人了。”"
    show halluke cry_eyebrow normal_eyes with dissolve
    h"“但……既然我已经习惯没人在乎我的日子了，如果无论如何结局都让人无法接受，还不如现在就结束这一切，也许会让我好受一点……”"
    show halluke cry_eyes with dissolve
    h"“也不用担心，自己真的有一天直面着你离开我时，会不会直接崩溃………”"
    "我不知道该回答他什么，只是拥抱着他。"
    "我听到了几声啜泣。"
    $ss('normal2_eyes')
    s"“别怕，真的。”"
    $sh()
    "那几个字，即便已经在脑袋里重复了千万次，却还是说不出来。"
    $ss()
    s"“我…我们已经是最好的朋友了，什么话都可以和我说。”"
    $p.stime(19,15)
    $sh()
    show halluke angry_eyebrow smile_eyes with dissolve
    "我还是没能说出来那几个字，但他却将头转了过来。"
    "这次是他主动亲吻上来。"
    "我感到一阵混乱，仅仅只是被他主导。"
    "但亲吻仅仅只是贴上嘴唇后便松开。"
    show halluke angry_eyes normal_mouth with dissolve
    h"“…你肯定会觉得我很轻浮，很随便吧。”"
    h"“你只是和我打过几次球，上过几次课，和我聊聊天，我就喜欢上你了，甚至还要这样亲你。”"
    show halluke normal_eyebrow normal_eyes smile_mouth blush with dissolve
    h"“但我真的太喜欢你了……我们不能在一起吗？”"
    h"“虽然我们仅仅只是打过几次羽毛球的关系，但当我的生活简直就是一团乱麻的时候，无论是多么微小的光照进来，都让我感动不已。”"
    "我，被表白了吗？"
    "现在脑子里一锅浆糊的人是我了。"
    "在我第一次凭着欲望对着这只小我几岁的大学生拿出手机偷拍时，会不会想到几个月后他正紧抓着我想要得到我的爱？"
    show halluke angry_eyes normal_mouth with dissolve
    $p.stime(19,20)
    h"“同性恋还是异性恋根本不重要，只是从来没人像你这样关心我。”"
    h"“我一开始也害怕你做的只是朋友应该做的事而已，我也害怕你没法接受我已经喜欢上你了这个事情。”"
    show halluke cry_eyebrow smile_mouth with dissolve
    h"“……我的喜欢真的很廉价，即便你只做了朋友应该做的。”"
    show halluke normal_mouth with dissolve
    h"“我的话都说完了，如果你现在想走的话，就走吧。”"
    menu:
        "同意他的表白" if (not replaying and (p.route == 'h' or not p.route)) or (replaying and p.hal_p != 99):
            "也许我应该更慎重点才对，毕竟我并不确定自己是否已经爱上他了。"
            "他已经歇斯底里了，说出来的想法也必然只是一时之言。"
            "也许他的过去充斥着悲惨，但这一切与我何干，怜悯还是什么样的感情都不能被称之为爱的。"
            "也许……也许我……"
            "我晃晃脑袋。"
            "算了，冲！"
            $ss()
            s"“Halluke。”"
            $sh()
            show halluke awkward_eyebrow with dissolve
            "我转头看向他。"
            $ss('normal2_eyes')
            s"“我……我也喜欢你。”"
            show halluke opened_mouth with dissolve
            s"“比你喜欢我还要喜欢你，没说谎。”"
            $ss('normal_eyes smile_mouth blush')
            show halluke smile_mouth with dissolve
            s"“从在羽毛球场第一次见到你的时候就喜欢你，喜欢你打羽毛球时的专注和敏捷。”"
            s"“喜欢你第一次和我说话的时候支支吾吾的可爱模样，喜欢你在打赢了球之后，脸上突然闪现的短暂笑容。”"
            show halluke angry_eyes normal_eyebrow with dissolve
            $ss('normal2_eyebrow normal2_eyes smile_mouth happy')
            s"“也喜欢后来的你，在接受了我之后，把藏在心里的痛苦和焦虑说出口的你。”"
            $sh()
            show halluke cry_eyes cry_eyebrow with dissolve
            "当我说完这些话之后，只觉脸上有团火在烧。"
            "即便这些话仅仅只是我片刻想出来的，但我不知道这样的说辞能否获取他的信任。"
            "大概我还没有完全爱上他，但如果我了拒绝他，就再也遇不到像他这样无论是体型还是外貌都如此符合我口味的人了。"
            "……无论如何，先答应好了，也许以后我会逐渐爱上他的。"
            "他朝我伸出双臂。"
            "于是我便和他拥抱着。"
            if p.hal_p == 11:
                $p.hal_p = 12
        "离开" if not replaying or (replaying and p.hal_p == 99):
            "也许我应该更慎重点才对，毕竟我并不确定自己是否已经爱上他了。"
            "他已经歇斯底里了，说出来的想法也必然只是一时之言。"
            "也许他的过去充斥着悲惨，但这一切与我何干，怜悯还是什么样的感情都不能被称之为爱的。"
            "也许……也许我……"
            "我晃晃脑袋。"
            $ss()
            s"“抱歉。”"
            #s"“大概我们大家都该冷静一下，也许，也许我还没法接受……这段感情……”"
            s"“也许我还没法接受……这段感情……”"
            $ss('angry_eyebrow scared_eyes smile_mouth')
            s"“因为我是一个钢铁直男。”"
            $ss('normal2_eyes sad_mouth')
            show halluke shy_eyes awkward_eyebrow no_blush with dissolve
            $sh()
            "也许这才是最好的选择，就像他所做出来的那个选择一样。"
            "我们的关系本就建立在欲望之上，也许等过一段时间，我就对他失去兴趣了。"
            "那还不如现在就结束这段感情。"
            show halluke cry_eyes cry_eyebrow with dissolve
            "我转身，没有胆量看他的脸。"
            "屋内的寂静氛围似要将我碾碎。"
            "我背对着他打开门，离开了他的家。"
            if p.hal_p == 11:
                $p.hal_p = 99
                $Achievement106.achieve()
                if p.aco_p >= 98:
                    $Achievement301.achieve()
                $HallukeTask1.lock(p)
                $Notice.show()
    
    if not replaying:
        $p.stime(19,50)
    scene black with dissolve
    stop music fadeout 5
    if p.hal_p == 12 or (replaying and p.hal_p != 99):
        $p.route = 'h'
        "离开之后，我重新加回了他的好友。"
        "也就是说，我终于有了一个男朋友。"
        "我本应该开心才是，但我总有一种莫名的疑虑，也许那些表白只是我的冲动之言。"
        "我并没有我说得那么喜欢他，我真真切切地欺骗了他。"
        "……"
        "也许我应该更慎重点才对，毕竟我并不确定自己是否已经爱上他了。"
        "他已经歇斯底里了，说出来的想法也必然只是一时之言。"
        "也许……也许我……"
        "可为什么，[p.name]，你明明那么喜欢他，甚至对着他的身体自慰，可现在为何会这样？"
        "我低着头朝着家的方向移动。"
        "大概只是我们的关系发展太波折太迅速太陡峭了吧。"
        "他喜欢我也明明只是因为我为他做过其他人没有为他做过的事吧？"
        "我靠近他也只是为了满足窥淫欲和低俗的意淫。"
        "我们的关系本就建立在欲望之上，也许等过一段时间，我就对他失去兴趣了。"
        "我们在一起，真的能够幸福吗？"
        "我走进自己居住的公寓小区。"
        "头开始痛起来了，以后再想吧。"
    if p.hal_p == 99:
        "一切都如同已死去那般安静。"
        "我只能听见我的脚步声。"
        "当我离开他所居住的小区后，我只是感到某种我无法表达的感觉。"
        "这种感觉像是释然，又像是空虚。"
        "我看到天空中仿佛有星辰落下，有嘶哑的鸟叫声流过思绪。"
        play sound audio.suicide
        "而后，我便听到了远处有什么东西沉重地砸落在地上的声音。"
        "……"
        "不，这一切都和我没关系。"
        "和我没关系。"
    "……"
    if not replaying:
        $p.stime()
        $p.times+=2
    $end_plot()
    if replaying:
        jump afterreplay
    
    if p.hal_p == 12:
        $Message.new(p, 'Halluke', 'Halluke', '那么既然你已经来过我家了，之后你想来玩也可以啦。因为羽毛球课已经结课了，所以那个时候我没课，如果你想来找我玩，就周六下午来吧。', h=20, m=51)
        $HallukeTask2.unlock(p)

    play sound unlocking
    $pause(0.5)
    play sound audio.button
    scene livingroom
    $p.onOutside = False
    jump TaskExecuting


label halluke_route_12:
    $start_plot()
    scene bedroom with fade
    stop music fadeout 5
    "我有些困倦。"
    "刚刚射过精的身体再加上拉着窗帘的卧室都让困意加倍努力抑制着精神，催促我去睡觉。"
    "但我还不想，或者说我正勉强维持着自己的精神不让自己睡着。"
    "…"
    "我的怀中是裸体的Halluke，他正蜷缩在我的怀中，闭眼发出均匀且舒缓的呼吸声。"
    "我柔软的阳物此时此刻正贴在他毛茸茸的臀上，几分钟前它还挺立着，反复来往于我怀中这个小家伙的后门。"
    "…"
    play music audio.concretejungle
    "当我再一次来到他家时，便忍不住抱着他的身体试图交配，可他并不感到反感，甚至看上去还很期待。"
    "甚至他在我来之前就已经洗干净后面了。"
    "我们…已经互相是男朋友的关系了啊。"
    "…"
    "现在我只能听见呼吸声，钟表秒针移动的齿轮传动声，还有偶尔的鸟叫。"
    "于是，在经历了十几周后，我终于“如愿以偿”地和这位曾经让我对着他照片发泄过很多次的，被当时的我称为直男的大学生做爱了。"
    "曾经的我只想将这一偷拍环节称之为死前生活的一点小小的刺激行为，以及施法材料的获取方式。"
    "谁能想到一两个月前我还在对着他意淫，两周前我还在担心我和他能不能做好朋友。"
    "现在就已经睡到了。"
    "只是我越来越感到某种…虚无感。"
    "可能这就是拥有一切之后产生的无趣？"
    "无论是偷拍还是对着他自慰，都是极为热烈的。"
    "但到了现在，却只能感到无聊，孤独和空虚。"
    "…"
    "所以一路走来到现在，我到底在追求什么？"
    "难道只是为了能像现在一样，拥有了能将精液排进别人的直肠里的条件，这样就可以不用自己动手自慰，还可以得意地和别人说“我不是处男”了吗？"
    "我到底是抱着怎样的想法去接近他的？"
    "是仰慕？是喜爱？是欲望？"
    "我只是在追求一个可以做爱的对象吗？"
    "我做这一切，是有意义的吗？"
    "也许他喜欢我，但他的喜欢对于我来说又有什么意义呢？"
    "…"
    "毕竟，这段感情本就来自生理上的欲望，而非真正的喜欢吧。"
    "…"
    stop music
    show halluke naked no_glasses angry_eyes with dissolve
    h"“在想什么？”"
    "我似乎已经盯着乳白色的粗糙墙面有一会了，在听到他的声音时才回过神来。"
    "他似乎也是才睡醒的样子，没有戴他的圆眼镜。"
    $ss("naked no_hat mood")
    s"“…没什么…就是…”"
    $sh()
    "当我说出“就是”的时候我就后悔了，但既然都说了，还是不要找借口掩盖过去。"
    $ss("naked no_hat normal2_eyebrow normal2_eyes")
    s"“Halluke喜欢我什么？”"
    $sh()
    show halluke awkward_eyebrow shy_eyes with dissolve
    "也许问问他这个问题，我也许能得到某些灵感，这样就能像他喜欢我一样喜欢上他了吧…"
    "他的腿在被窝里本来正动来动去，在听到我问出这个问题的时候突然停止了。"
    show halluke normal_eyebrow normal_eyes with dissolve
    "随后他坐起身，思考了片刻。"
    play music audio.halluke fadein 5
    show halluke smile_mouth with dissolve
    h"“你记得几周前你带我出去吃鸭血粉丝吗？在吃完准备回学校的时候你请我吃冰淇淋。”"
    show halluke angry_eyes normal_mouth with dissolve
    h"“我…当时有点震惊。”"
    "这不就是普通地吃一次冰淇淋吗？"
    show halluke normal_eyes smile_mouth with dissolve
    h"“当然不是因为你请我吃，是因为你问我想要什么口味的冰淇淋。”"
    show halluke normal_mouth with dissolve
    h"“你知道的，我的很多事情都是被家里人完全决定的，但甚至就连吃什么味的冰淇淋也是。”"
    h"“他们吃冰淇淋的时候从来不问我喜欢吃什么，递给我的永远都是白色的甜筒。”"
    show halluke angry_eyes with dissolve
    h"“‘草莓味的都是色素，吃了脑子就不好使了。’”"
    show halluke normal_eyes smile_mouth with dissolve
    h"“虽然我吃过草莓，也自己买过草莓味的冰淇淋，但这是第一次，有人问我想吃什么味的冰淇淋。”"
    show halluke closed_eyes normal_mouth with dissolve
    h"“就…可能你不会在乎这种事，但是那天晚上我在家里哭了一晚上。”"
    show halluke cry_eyes with dissolve
    h"“我觉得自己人生没价值，因为没什么事是自己决定的，自己过的人生根本没有自己的想法和痕迹。”"
    h"“就像一个木偶一样，只需要被家里人指挥而已，甚至连冰淇淋的口味都没法决定。”"
    show halluke normal_eyes smile_mouth with dissolve
    h"“…谢谢你当时让我选择，如果你先点口味的话，那我可能就习惯性地吃你点的口味了。”"
    "我不知道该说什么，只是突然想起了自己的父母。"
    "即便我不喜欢他们，但我实际上要比身边这位幸运得多。"
    "我也起身，坐在床上面对着他。"
    $ss("naked no_hat normal2_eyebrow normal2_eyes")
    s"“想开点，你已经离开他们了，就有很多事已经都可以自己选择了。”"
    $ss("naked no_hat smile_eyebrow smile_eyes")
    s"“就像，就像以后，Halluke之后想做什么职业？”"
    $sh()
    show halluke awkward_eyebrow normal2_eyes normal_mouth with dissolve
    h"“…唉…？”"
    show halluke angry_eyes with dissolve
    h"“问题大概就是这样了，可能我想过以后要做什么吧…但一直以来我都决定不了什么，可能也完全没有规划人生的能力吧。”"
    h"“就算我有，说出来的话也没有意义，没有作用。”"
    show halluke normal_eyebrow normal2_eyes with dissolve
    h"“如果你把木偶的绳子切断，即便它有翅膀。也没法飞起来，只会掉到地上，运气差的话可能直接就摔碎了。”"
    h"“我已经没法为自己做决定了，肯定还是看家里人要我做什么，我就去做什么。”"
    show halluke normal_eyes with dissolve
    h"“[p.name]的职业和大学肯定是自己选的吧？”"
    h"“我什么都选择不了，就算考第一也很无聊，生活也没有意义。”"
    show halluke angry_eyes with dissolve
    h"“不知道我是怎么坚持到现在的。”"
    h"“很好笑的是，我家里人一直都不知道我打羽毛球，要是他们知道了肯定又要说我净做些没用的事。”"
    "如果我被这样对待的话，一定会觉得生命充满了煎熬吧，想想就很想直接从二十几层楼上跳下去。"
    $ss("naked no_hat normal2_eyes")
    s"“恰恰相反，你没注意到吗，是你自己选择了羽毛球。”"
    show halluke awkward_eyebrow normal2_eyes normal_mouth with dissolve
    s"“一开始我刚看到你的时候，对你的印象大概是，打羽毛球会笑的很开心，一不打了就变成臭脸了。”"
    s"“羽毛球是你自己选择的，认识我也是你自己选择的，甚至之后一系列的东西都是你选择的。”"
    $ss("naked no_hat smile_mouth")
    s"“你家里人要是知道你和我这样的同性恋在一起，岂不是要疯掉？”"
    $sh()
    show halluke normal_eyebrow normal_eyes smile_mouth with dissolve
    "他笑出声来了。"
    $ss("naked no_hat")
    s"“至少和你的家里人聊一下，让他们不要什么事都帮你定夺。就算他们不同意，山高皇帝远，你在这里做什么他们也不知道呀。”"
    s"“何必给自己打造一个空气笼子呢？”"
    $sh()
    show halluke angry_eyes normal_mouth with dissolve
    h"“…是啊…但…但我还是害怕…做不好…”"
    $ss("naked no_hat normal2_eyes")
    s"“你已经成年了，内心深处一定是想过自己的人生的，不要害怕作出选择，也不要依赖别人作出选择。”"
    $ss("naked no_hat smile_eyes")
    s"“再者你的生活并不是没有意义的，虽然像你说的，学业或者啥都是家里人替你做的决定，但至少过程是你自己走过来的呀。”"
    $ss("naked no_hat smile_mouth")
    show halluke normal2_eyes with dissolve
    s"“你走过的路都是属于你自己的，都是你存在过的印记，这都是你的存在意义所在。”"
    $sh()
    show halluke cry_eyes with dissolve
    h"“[p.name]…我…”"
    "在我安慰他的这段时间里，他的情绪就逐渐开始不稳定了。"
    "确实，对于他这样的人，要重新破坏所有家人强加给他的观念，再重塑新的世界观，一定很不容易吧。"
    "那么，接下来我该做什么呢？"
    "我抱住他，即便我其实对安慰他并没有什么太大的兴趣，只是他需要有人听他说话，需要有人陪他。而非我主动去做。"
    $ss("naked no_hat")
    s"“接下来的路还有很远，但我会陪你继续，我会帮你的，不要害怕。”"
    $sh()
    show halluke angry_eyebrow shy_eyes smile_mouth blush with dissolve
    h"“嗯。”"
    "他并没有我想象中地那么脆弱，或者说我的想法就不对，如果他在这样的家中坚持到现在，说明他应有一颗十分坚韧的心才能挺到现在。"
    "如果我也能有他那样热爱生活就好了，也不至于每个睡不着的深夜都对着窗台和垂手可得的无痛死亡恍惚出神。"
    stop music fadeout 4
    "…"
    scene bedroom with fade
    "我突然意识到自己好像没那么困了。"
    "他起床去上厕所了，卧室里只有裸体的我。"
    "…"
    play music audio.impendingdeath
    "那么，我成功地安抚了他，解决了他的问题，很明显他开心多了，但我内心却有种奇怪的感觉。"
    "如果要我称呼这种感情的话，更像是……不耐烦，但是必须要做的工作一般。"
    "我们互相付出了这么多时间，他从我这里得到了“爱”，而我也从他那里得到了我一直梦寐以求的他的身体。"
    "但我却感觉不到快乐，或者说幸福……"
    "我只是这样安慰着他，保护着他，陪伴着他，我为什么要这样做呢，只是因为他向我“求救”了吗？只是因为，这些事只有我一人能做吗？"
    "是啊，如果我离开了，没有了我的陪伴，他一定会十分难过吧。"
    "但我并没有在这段关系中获得任何慰藉，甚至只有疲惫。"
    "我感觉他正吮吸着我的陪伴和精力。与此同时，如果是敏感的他……要是我说错话的话，肯定会发生很不好的事吧？"
    "……作为他的救命稻草，我是应该和他陈述自己其实骗了他，没有爱上他，还是保持现状，为了一个和我无关的人能够活得舒服一点而输出精力和共情呢？"
    "他对我的爱正随着我对感情上的安抚和付出快速生长着，但我对他的爱却如同荒地一般。"
    "……甚至连新鲜感的加成也没有了。"
    "做爱原来是那样地让人疲倦，完全没有自慰方便舒服。"
    "心底有个声音一直呼唤着对爱情的渴望，逼迫我做与他相关的事情。"
    "周六的羽毛球课，周日的私下约会，有时候我突然会感到不对劲……我为什么要做这些事，我明明只是觉得他长得很可爱而已，我为什么要……"
    "……当时的我还绞尽脑汁想认识他，也许是和他在一起能让我感觉开心吧？"
    "但那种开心，和看帅哥很开心应该是一样的吧？"
    "……"
    "我已经和他在一起了，为什么我还是感觉孤独？"
    "为什么我没能爱上他？"
    "…"
    "我突然听到齿轮转动的声音。"
    "呼吸声。"
    "齿轮转动声。"
    "心跳声。"
    "……"
    "我到底在哪里？"
    stop music fadeout 5
    if p.hal_p == 12:
        $p.hal_p = 13
    $end_plot()
    if replaying:
        jump afterreplay
    $p.times+=1
    $HallukeTask2.lock(p)
    scene black with dissolve
    "……"
    play sound unlocking
    $pause(0.5)
    play sound audio.button
    scene livingroom
    $p.onOutside = False
    jump TaskExecuting


label halluke_route_13:
    $start_plot()
    $p.onOutside = True
    scene black with fade
    stop music fadeout 5
    $p.stime(8,33)
    "“知名轮船酒店德里莫号将停泊于A市，于本周末，登船享受一日住店，绕海域一圈，甲板开放，房间整洁，享受美妙海上风光。”"
    "这段广告我已经可以倒背如流了，A市的汽车广播，地铁广告，甚至刷短视频的时候跳出来的广告都是这个。"
    "这样的酒店的价格也必然十分恐怖，我是做梦都没想到，自己能从那家伙手里得到船票。"
    "虽然他总是抓我摸鱼，不过还是挺看中我的嘛。"
    "……"
    "和他在一起多留下一点回忆的话，应该也能让我喜欢上他吧。"
    "…"
    play music audio.thedeldrimor fadein 5
    scene deldrimor1 with dissolve
    $p.stime(35)
    "…"
    "我能感觉到他正拽着我的背包带，跟着我的步子前进，人多的地铁让他感觉很不舒服。"
    "出了地铁之后，A市港口便就在眼前了。"
    "湿润的海风还带着股咸味，那只小白熊便从我身后绕到一边来，同我一起看着不远处的港口。"
    "德里莫号如同一座海上的高楼，颇有泰坦尼克号的感觉。"
    "即便住在临海的港口城市，我也没有太多机会去看看海之类的，倒不如说我根本就对这种本质上只是更巨大的水库来说没什么兴趣。"
    show halluke shirt smile_mouth with dissolve
    $p.stime(36)
    "不过Halluke嘛…他倒是挺开心的，甚至还为此穿了套新衣服。"
    "他并不是那种喜欢出去乱逛的人，但只要是我陪他，他也十分愿意和我一起……"
    scene deldrimor2 with dissolve
    $p.stime(37)
    "…"
    "德里莫号有趣的一点是，在几乎所有交通业务都被数字化的今天，仍然保留着最古老又别致的方法——船票。"
    "我将两张船票交给验票人员，在进行安检后，便让我和Halluke通行了。"
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
    "Halluke把背包放在桌子上，然后把他自己整个人面朝下丢到床上。"
    $ss("ship cap normal2_eyes")
    s"“你觉得怎么样？”"
    $sh()
    "我把背包也放在桌子上，搭着他的白色背包，将外衣脱掉，放在椅背上。"
    show halluke shirt smile_eyes smile_mouth with dissolve
    "而他在听到我和他搭话之后，也坐起身来，拍了拍身上的灰尘。"
    h"“挺好的，感觉很舒服诶…”"
    $p.stime(45)
    show halluke shirt normal_eyes normal_mouth with dissolve
    h"“好久没出门到这么远的地方了，感觉真的好紧张…”"
    show halluke shirt shy_eyes smile_mouth with dissolve
    h"“不过到了这里，只有我和你，也就不那么紧张了…”"
    "我也靠近床边，趴在他的身边，用爪子抚摸着他头顶的毛发。"
    "他似乎很享受，两只没有脱鞋子的脚悬在床边晃悠。"
    "离船航行还有一段时间，先在这里休息一下吧。"
    scene deldrimor5 with fade
    $p.stime(9, 11)
    "…"
    "刚刚来的时候，外面还是晴天，但等船慢慢开始航行的时候却突然下起雨来了。"
    "Halluke似乎为不能出门吹吹风这件事有点难过，仅仅只是靠在窗户边上看着波澜的海。"
    "我们已经驶离A市的港口了，现在只能从地平线处看到一点点小小的建筑顶端。"
    $ss("ship cap normal2_eyes")
    s"“不开心吗？”"
    $p.stime(12)
    $sh()
    show halluke shirt awkward_eyebrow angry_eyes normal_mouth with dissolve
    h"“有点遗憾吧，好不容易来到这种地方，却又遇上下雨。”"
    scene deldrimor6 with dissolve
    "我转头看着窗户，听海浪呼啸的声音，还有雨滴拍打玻璃窗和铁质船体的叮叮咚咚声响。"
    "面对着有些忧伤的他，我应该安慰一下吗？作为他的男朋友？"
    scene deldrimor7 with dissolve
    "我从身后抱住他，将头搭到他的肩膀上。"
    $p.stime(13)
    show halluke shirt angry_eyes smile_mouth with dissolve
    h"“谢啦…”"
    show halluke shirt shy_eyes smile_mouth with dissolve
    h"“说真的，这样也挺好的。”"
    "他看着我。"
    h"“平静，安详。”"
    show halluke at near
    $p.stime(14)
    "我用吻部蹭了蹭他的脸颊，毛绒绒的。"
    "这就是谈恋爱的感觉吗？这就是我一直在追求着的东西吗？"
    "我感到开心吗？"
    "为什么我总是觉得好像差点什么…"
    stop music fadeout 5
    show halluke shirt awkward_eyebrow awkward_eyes normal_mouth
    $p.stime(15)
    h"“[p.name]？”"
    "他好像叫了好几次我的名字，而我才刚刚回过神来。"
    $ss("ship cap normal2_eyes")
    s"“噢噢…嗯…怎么了？”"
    $sh()
    "他微笑着，眯起眼睛来，转身试图挣脱我。"
    show halluke shirt angry_eyes smile_mouth at look_
    "于是我不再将身体压向他，让他自由活动。"
    "他看了看大海，又将视线挪到我身上。"
    show halluke no_glasses closed_eyes with dissolve
    "然后摘下了他的眼镜。"
    show halluke shirt angry_eyes smile_mouth with dissolve
    h"“很少有人喜欢听我的话，也很少有人能让我放下心来和他说话。”"
    $p.stime(16)
    $ss("ship cap normal2_eyes")
    s"“怎么突然说这个？”"
    $sh()
    show halluke normal_mouth with dissolve
    h"“…嗯…”"
    "外面的天阴蒙蒙的。房间内也并不同早上那般明亮了。"
    play music audio.deldrimorsroom fadein 5
    h"“我小时候，觉得眼镜很酷。”"
    $p.stime(17)
    h"“但是我表哥和我说，如果戴眼镜的话，和别人打架，对方只需要把你的眼镜打掉，你就没办法了。”"
    show halluke awkward_eyes with dissolve
    h"“我的表哥…他去很远的地方上大学了，现在也没和我有联系了。”"
    h"“我后来上了小学，初中，高中。”"
    h"“和别人不同的是，我的视力非常好，从来不需要戴眼镜。”"
    h"“每次测试都是最优秀的视力。”"
    $p.stime(18) 
    show halluke normal_eyes smile_mouth with dissolve
    h"“那时的我就想，我可不要戴眼镜。”"
    h"“要随身带着眼镜盒，要保护好，冬天会起雾，而且戴着眼镜，耳朵鼻子都很难受。”"
    show halluke normal_mouth with dissolve
    h"“但是，最后我还是戴了。”"
    "他拿出背包里的眼镜盒，打开，从里面拿出眼镜布。"
    "而后拿起眼镜，对着镜片吹口气，再用眼镜布一点一点摩擦着镜片。"
    show halluke glasses
    "带他擦拭结束过后，又将眼镜戴在了脸上。"
    h"“当我发现自己视力的疯狂下降之后，我害怕了。”"
    $p.stime(19)
    show halluke angry_eyes with dissolve
    h"“我害怕自己将会不得不为我的生活戴上枷锁，我害怕镜片会越来越厚，最后就连镜片都救不了我了。”"
    h"“我会变成一个瞎子，从此留给我的只有黑暗。”"
    h"“我害怕这些不痛，但是真实地增加了活下去的难度的残疾。”"
    h"“手，腿，视觉，听觉，味觉，说话…”"
    show halluke awkward_eyebrow normal_eyes smile_mouth with dissolve
    h"“如果我一旦失去了其中的一个，可能我都不会再有勇气或者意志活下去吧。”"
    h"“就像越过围墙的王子，拥有过却再剥夺就太痛苦了。”"
    $p.stime(20)
    show halluke normal_eyebrow angry_eyes normal_mouth with dissolve
    h"“这样没法完全体会到活着的美好的生命，还有什么存在的必要呢。”"
    $ss('ship cap')
    s"“…”"
    s"“就像时常复发的口腔溃疡，鼻塞，嗓子疼这种…”"
    $sh()
    show halluke normal_eyes smile_mouth with dissolve
    h"“没错…但倒不至于让我活不下去，我知道有一天会治得好，只是过程也让人感到痛苦。”"
    h"“更像是没法治疗的慢性病…”"
    $p.stime(21)
    $ss("ship cap normal2_eyes smile_mouth")
    s"“…”"
    s"“假如，你从小时候开始就得了一种病，会让你每天每时每刻都会头痛，医生也治不好的那种，你需要每天都吃药…你会怎么做？”"
    $sh()
    "他眨了眨眼。"
    show halluke angry_eyes with dissolve
    h"“大概，我会感到很郁闷吧，也可能会想不开…”"
    h"“但应该也比变瞎或者什么都听不见好，能感觉到活着的美妙之处，而不是被剥夺了作为生命的功能…”"
    scene deldrimor6 with dissolve
    "他转过身去，看着朦胧的海。"
    $p.stime(22)
    "雨仍然没有要停下来的迹象，像是要持续至永远一般。"
    "…"
    "我爱上他了吗？爱上了，还是没有？"
    scene deldrimor7 with dissolve
    show halluke shirt angry_eyes smile_mouth with dissolve
    $p.stime(23)
    h"“你想去外面吗？”"
    "他的话再次把我拉回现实，这次我没有让他重复好几遍才清醒。"
    "看来他还没感觉到我其实心不在焉吧。"
    h"“我们可以找工作人员借一把伞，然后我们去甲板呆一会，如何？”"
    stop music fadeout 5
    $ss("ship cap normal2_eyes smile_mouth")
    s"“好啊，听你的。”"
    $sh()
    play music audio.deldrimorsdeck fadein 5
    $p.stime(35)
    scene deldrimor8 with fade
    "…"
    "我的手中是颇有古典气息的带弯钩的长柄伞，而他则在伞下和我一同行走。"
    "雨滴落在漆黑的伞面而发出连续的砰的敲打声，他的鼻子在呼吸的时候会轻微地颤动。"
    "积水的甲板，湿润的空气。"
    "雨中的大海，灰压压的，有种自然之神君临此处的感觉。"
    "我和他移动到甲板的边缘，靠近铁质的栏杆。"
    "我们被无限的深灰包围着，海浪，水声，以及引擎之类的东西发出的持续的轰隆声。"
    "甲板上只有我和他。"
    $p.stime(36)
    show halluke shirt angry_eyes with dissolve
    h"“说实话，我没想过自己真的可以找到一个让我无话不谈的人。”"
    h"“我以为我口中的一字一句都要永远地烂在我的思绪里了。”"
    $ss("ship cap normal2_eyes smile_mouth")
    s"“我记得，我刚认识你不久的时候，你支支吾吾地回答我说的话的样子。”"
    $sh()
    "他也随我的视线看向大海。"
    $p.stime(37)
    show halluke angry_eyes smile_mouth with dissolve
    h"“是啊，我以为我只能在别人面前那个样子了。”"
    h"“谢谢你，在你身边说话，我一点都不感觉紧张。”"
    $ss("ship cap smile_mouth")
    s"“挺好的。”"
    $sh()
    "我们只是看着海。"
    $p.stime(38)
    "雨还没停，落在栏杆上，落在伞上，落在甲板上。"
    show halluke awkward_eyebrow normal_eyes smile_mouth with dissolve
    h"“把心里的话都说出来感觉真的很好。”"
    show halluke angry_eyes smile_mouth with dissolve
    h"“但是如果没有你，把很多东西都憋在心里的我，肯定要比现在痛苦得多。”"
    h"“真的，很感激…嘿嘿。”"
    "我摸了摸他的头。"
    $p.stime(39)
    show halluke normal_eyebrow normal2_eyes normal_mouth with dissolve
    h"“[p.name]。”"
    $ss('ship cap')
    s"“什么？”"
    $sh()
    show halluke awkward_eyebrow angry_eyes normal_mouth with dissolve
    $p.stime(40)
    h"“你觉得，自己存在的意义是为了什么？或者说，为什么要活着？”"
    "这个问题倒是把我难住了，我到底是为什么活着呢？"
    "我转头看向大海。"
    "也许我想死。"
    "现在从这里跳下去就可以死了，死了之后就可以解脱了，死了之后也不用工作，也不用买药，也不用忍受头疼。"
    "但我为什么坚持到了现在？"
    $p.stime(41)
    show halluke normal_eyebrow angry_eyes normal_mouth with dissolve
    h"“…其实我也不想活着了。”"
    h"“活着太无聊了。”"
    show halluke normal2_eyes smile_mouth with dissolve
    h"“话说，[p.name]在大学的时候是什么专业？”"
    "我思考了下。"
    "我回忆起小时候自己想当作家，想写各种各样的文字，但高中的作文只能拿到中等偏下的成绩。"
    "于是我高中的时候决定做个老师，又喜欢理科，想着做个化学老师之类的。"
    $p.stime(42)
    "但是为什么阴差阳错地，把志愿填成了软工呢。"
    $ss('ship cap')
    s"“软件工程。”"
    $sh()
    show halluke angry_eyes normal_mouth with dissolve
    h"“我是计算机，父母硬给我填的。”"
    show halluke normal2_eyes with dissolve
    $p.stime(43)
    h"“不知道[p.name]是不是有在做软件相关的工作，但我认为，我应该不会从事计算机方面的职业吧。”"
    show halluke angry_eyes normal_mouth with dissolve
    h"“那我这个大学还有什么意义呢。”"
    h"“我对未来要做什么也没有想法，每次想到都觉得十分迷茫，”"
    h"“我没什么朋友，也没人关心我，在这个城市的家里只有我一个人。”"
    $p.stime(44)
    h"“羽毛球，也许我没那么喜欢羽毛球罢了，只是因为别的都不适合我。”"
    "我转头看向他，他的眼睛也远望着大海。"
    show halluke closed_eyes normal_mouth with dissolve
    h"“这样的生活真是又无趣，又失败。”"
    show halluke smile_eyes smile_mouth with dissolve
    h"“但是我遇到了你。”"
    show halluke angry_eyes normal_mouth with dissolve
    $p.stime(45)
    h"“我之前读过一本书，书里按照人存在的意义将人归纳为四种。”"
    h"“活在自己眼中的人，活在身边熟人眼中的人，活在大众眼中的人，活在特定一个人眼中的人。”"
    show halluke smile_eyes smile_mouth with dissolve
    h"“如果我死了，[p.name]也会很难过吧？”"
    $p.stime(46)
    $ss("ship cap normal2_eyes")
    s"“但是如果仅仅只是为了别人而活，那还有什么意义？”"
    $ss("ship cap normal2_eyes smile_mouth")
    s"“不如我们两个肩并肩一起跳海吧？那还算有趣一点。”"
    $sh()
    $p.stime(47)
    "虽然我这么说，但我不知道我是否真正有这样的勇气。"
    show halluke angry_eyes normal_mouth with dissolve
    h"“并非是为了别人而活，而是一种……留恋？”"
    h"“世间仍然有在乎我的人，也有我在乎的人，以这为理由，那就足够了。”"
    h"“和你在一起的时间里，要比我曾经经历过的时光都美好。”"
    show halluke smile_mouth with dissolve
    $p.stime(48)
    h"“所以[p.name]可不要不小心死掉噢。”"
    "我笑笑。"
    "他并不知道我的病，即便他作为我的男朋友有权知道，但我还是打算继续隐瞒。"
    "总会有一天，我的病就算药物也没法拯救。"
    "到那个时候，我就该离开这里了吧。"
    $p.stime(49)
    "雨还在下，但我们都没有继续再说话。"
    "…"
    stop music fadeout 5
    $end_plot()
    if replaying:
        jump afterreplay
    if p.hal_p == 13:
        $p.hal_p = 14
    $ p.newDay()
    $ p.stime()
    $ Save.save(p)
    $ Notice.add('存档已保存！')
    $ Notice.show()
    call loading from _call_loading_10
    jump halluke_route_14


label halluke_route_14:
    $start_plot()
    if p.mental < 5:
        $p.mental = 30.0
    show screen screen_dashboard(p)
    $p.onOutside = True
    scene deldrimor4 with fade
    "汽笛声和穿过玻璃的阳光将我唤醒。"
    "在醒来的刹那我突然意识到，这次的起床并没有闹钟参与，也没有头疼的折磨。"
    "无论如何，我今早不打算吃药了，即便这是个冒险的行为，但如果头疼突然爬上脑壳的话，再吃应该也来得及。"
    "…"
    play music audio.meaninglessemotion fadein 5
    scene black with fade
    $p.stime(8, 43)
    "我们一起来到上层船舱的餐厅吃过早饭后，本想再去甲板上看看风景，但船已经靠岸，同时因为转晴的天气，甲板上几乎挤满了人。"
    "还是算了。"
    scene deldrimor6 with fade
    $p.stime(9, 55)
    "我们回到自己的房间，在我拒绝了他还想再来一发的请求后，他还是紧紧抱着我，将他的爪子放进我的内裤里抚摸着我半硬不硬的阳物，带着微红的脸颊用鼻子顶着我的耳朵。"
    "也许叫他来这里并不是一件正确的事，他比从前更粘人了，更加依赖我了，甚至看我的眼神都变了。"
    "他的世界，也许只剩下我了。"
    "而我也不再考虑如何让自己爱上他，我只想逃避这份感情。"
    "…"
    $p.stime(10, 30)
    scene subway with fade
    "回家途中，我和他上了地铁。"
    "他和我坐在一起，即便我们一句话没说，但他甚至仅仅只是一直盯着我，以这种方式消磨时间。"
    "幸好地铁很快就开到他要下车的地铁站了。"
    "即便如此，我们仍就像真正的情侣那样，牵手，对视，聊天，告别。"
    "但，伪装自己的心去做这些事，真的消耗了我特别多的精力。"
    $p.stime(31)
    "我叹口气，仿佛卸下了千斤重的担子一样向后倒在地铁座位的椅背上。"
    "我掏出手机，准备翻翻莓博消磨时间，不知为何却点开了图片应用。"
    "几乎是轻车熟路地，我解锁了特殊权限并进入了隐藏文件夹，里面都是Halluke打球的照片，都来源于我的偷拍。"
    "有的清晰，有的模糊，有的还裁掉了其他路人，用来方便手冲。"
    "现在的我面对着这些照片是什么心情呢？"
    $p.stime(32)
    "而曾经的我又是抱着怎样的心态拍摄，又怀着怎样的歹念对着这些正常人来看只是普通的照片自慰的呢？"
    "我心里有些复杂，更多的是不知道该怎么结束这一切的疑问。"
    "…"
    play sound audio.getmedicine
    $p.stime(33)
    "手机突然传出一阵提示音。"
    "我很快就发现，这是一个我好久都没点开过的社交应用的特殊提示音。"
    "虽然说是社交，但大家基本上都把它当作约炮的应用。"
    $p.stime(34)
    "我点开那个应用，显示出来的则是一个和Halluke相比更加矮小更加可爱的小狼兽人发来的信息。"
    "我突然感到一阵混乱的情绪。"
    "抱着仅仅是好奇的态度，我点开了信息。"
    
    stop music
    scene bedroom with fade
    $p.stime(16, 55)
    "…"
    "我感觉快乐吗？"
    "或许是的。"
    "当我把那种小狗一样可爱的家伙抱起来侵犯时，某种特殊，十分稀有又让人完全痴迷的感觉填满了我的大脑。"
    "我突然回忆起几个月前，我在A大体育馆对着小便的Halluke自慰，清理完自己自慰产生的精液后没多久，突然对着马桶呕吐起来的事。"
    if p.hal_p == 14:
        $p.hal_p = 15
    $end_plot()
    if replaying:
        jump afterreplay
    $p.onOutside = False
    jump dayEnd



label Halluke_hidden_plot1:
    stop music fadeout 3
    "我真的有必要这样做吗？"
    "我的拇指悬停在手机荧幕之上，如果我按下去，讯息便会以我无法计量的速度传输到基站，随后我的上司的手机便会接收到转发而来的电波。"
    "为什么我这么紧张呢，以前不也是经常和他请假吗，可这次却…"
    "我按下了通话按钮。"
    "随后手机便开始发出等待接通的嘟声。"
    "我深呼吸，脑中将破碎的词句快速拼接成可用的借口，按理说我不应该如此慌乱的，果然还是因为加班请假…"
    "电话接通了。"
    ar"“喂？[p.name]？什么事？”"
    $ss('glasses white no_hat normal2_eyebrow smile_eyes awkward_mouth sweat')
    s"“我，我要请假…”"
    $sh()
    ar"“为什么请假？今天老板宁愿付给你们这些人三倍的加班费也要让你们所有人加班，你不知道这件事有多重要吗？”"
    ar"“你要是请假回去睡觉，就去给CEO打电话吧，我做不了主。”"
    $ss('glasses white no_hat normal_eyebrow smile_eyes agony_mouth sweat')
    s"“…我，我是为了一件很重要很重要的事。”"
    $sh()
    "不，这句话不在我所构思的借口之中，难道我必须临场发挥了吗？"
    "意外的是，在我说出这句话之后，电话里的声音停下了，他只是叹了口气。"
    ar"“你说吧。”"
    $ss('glasses white no_hat scared_eyebrow sad_eyes sad_mouth sweat')
    s"“因为…因为我的恋人…她…今天是她…很重要的日子…我必须…去…”"
    $sh()
    ar"“恋人？你还有女朋友了？”"
    $ss('glasses white no_hat surprised_eyebrow surprised_eyes surprised_mouth sweat')
    s"“…对…她今天…比赛，我要去场上…给她加油。”"
    $ss('glasses white no_hat sad_eyebrow sad_eyes angry_mouth sweat')    
    s"“我每周都去，如果我这周不去她肯定…”"
    $sh()
    ar"“…好了，我听够了。”"
    play music audio.debilitatinganxiety
    ar"“你要不要看看你自己编得都是些什么乱七八糟的，把我当小孩耍？”"
    "恐惧令四肢的血液抽回心脏。"
    $ss('glasses white no_hat sad_eyebrow closed_eyes angry_mouth sweat')   
    s"“我…抱歉，但我…必须……”"
    $sh()
    stop music
    ar"“不过…我有没说不给你假吗？”"
    ar"“…请假的事我去处理，工资的事就算了。你给我记住了，这件事情之后再让我抓到你睡觉…你就完蛋了。”"
    "什么？他居然…同意了吗？"
    $ss('glasses white no_hat smile_eyebrow surprised_eyes smile_mouth no_sweat happy tear')   
    s"“啊啊！…谢谢主管！我…我以后一定！…一定努力工作！…”"
    $sh()
    play sound audio.interruption
    "他挂断了电话。"
    $routineMusic(p)
    "刀子嘴豆腐心…至少在我印象里，我每次请假，虽然他嘴上一直在骂我，实际上也没有哪次是不允许我离开的。"
    "我突然有点感动，是因为我为了他，为了我所爱的人，做了一些我平时不敢去做的事吗？"
    "这种心中的澎湃感，是因为我正在做着正确的事吗？"
    scene workarea with fade  
    $p.onVacation = True
    $p.stime(55)
    $p.hal_p = 50
    $p.checkTask()
    $routineMusic(p)
    "我离开公司，回到了家中。"
    "等吃过午饭之后就像之前那样去球场帮他吧。"
    
    jump end_call

label Halluke_hidden_plot2:
    stop music fadeout 3
    scene court with fade
    "我终于来到了这里。"
    "这不是我第一次来，也不会是最后一次。"
    show halluke with dissolve
    "Halluke正在羽毛球场的角落拿着球拍，对着墙壁发球，再将球击回。"
    show halluke awkward_eyebrow normal2_eyes opened_mouth with dissolve
    "几乎在我看到他之后的片刻，他就像感知到了我的存在一般，快速地转过头来，看向我。"
    "我能看到他的眼睛都亮了起来。"
    "…"
    scene court_ with dissolve
    "就这样，我和他坐在球场的休息侧的长凳上等待体育老师的叫号，同时观察着其他人的考试内容。"
    "其实就是一人在球网一侧发球，而考试人则需要将球击回发球人的半场，同时还要打得足够远，还不能出界。"
    "乍一看好像还有难度，但想必体育应该不会给太低的分数，所以放宽心态就好。"
    "更别说我身边的人那么擅长羽毛球，这种考试如鱼得水啦。"
    show halluke normal_eyebrow cry_eyes normal_mouth with dissolve
    "我无意识地转头看向他，他却看上去十分紧张，眼神紧盯着体育馆的地面，身体微微颤抖着。"
    $ss('scared_eyebrow normal2_eyes normal_mouth sweat')
    s"“发生什么事了？”"
    $ss('scared_eyebrow normal2_eyes agony_mouth sweat')
    s"“考试要鼓起劲来啊。”"
    $sh()
    show halluke normal_eyebrow angry_eyes cry_mouth with dissolve
    h"“…没事。”"
    "他抬头看向我，像是在努力对着我做出一个微笑。"
    "我有点担心，是因为家里的事吗？"
    "…"
    scene court with fade
    "考试开始了。"
    "我站在他的球网对侧，一共有五个球，我朝着他丢出球，就像我们平时在课上训练的那样。"
    play sound audio.badminton
    "他击到了球，我抬头，白色的羽毛球越过球网，像拖着尾迹的彗星。"
    teac"“出界。”"
    "老师的声音让我一惊。"
    "是我丢球丢的不够好吗？"
    "我注视着球网对面的Halluke的眼睛，他明显十分紧张。"
    "不…这样不行…"
    "我再次丢出接下来的几发球。"
    play sound audio.badminton
    teac"“没接到球。”"
    play sound audio.badminton
    teac"“没过网。”"
    play sound audio.badminton
    teac"“出界。”"
    play sound audio.badminton
    teac"“出界！”"
    "…"
    "我不敢看同学们异样的眼光，仿佛那个正在考试的人是我。"
    "我和他离开了球网边。"
    scene court_ with dissolve
    "估计Halluke的体育课期末成绩要垫底了，但他的平时分一定能确保他及格的。"
    "我和他离开球场，他看上去有些沮丧，本就不愿意说话的他更是一言不发。"
    $ss('sad_eyebrow normal2_eyes normal_mouth')
    s"“没关系，不用担心的，你这几节课表现得都那么好，而且也都出勤了，老师不会为难你的。”"
    $sh()
    "他的状态更差了，只是一直低着头往前走，或许是在听到我的声音后才停下，随后转头看向我。"
    play music audio.debilitatinganxiety fadein 3
    show halluke cry_eyebrow angry_eyes angry_mouth with dissolve
    h"“…你…走吧…”"
    show halluke cry_eyebrow angry_eyes opened_mouth tear with dissolve
    h"“…然后…不要来找我了…”"
    show halluke angry_eyebrow shy_eyes opened_mouth with dissolve
    h"“都…都是你…都是你害的…都是你！…”"
    "他的手抓住我胸口的短袖。"
    "我能解释什么呢？"
    "是我的角度不对？力度？方向？可我们之前在课上的时候就是这样练习的啊？"
    $ss('surprised_eyebrow scared_eyes scared_mouth sweat')
    s"“我…”"
    $sh()
    hide halluke with dissolve
    "还没来得及解释，他便松开了手，朝着球场出口的方向跑走了。"
    "…"
    "我该生气吗？为了来他这里，我宁愿抛下一大笔加班费，抛下同事额外包揽我的工作，该卖了Arnel一个大人情。"
    "明明是他自己太紧张，自己发挥失常，怎么能怪到我头上？"
    "果然是撒泼成性的小孩子，幼稚得可笑。"
    "我居然还为了他来到这里。"
    "…"
    "唉。"
    "Halluke他，考试失利成那样，一定很伤心吧。"
    "所以他才会这样。"
    "…"
    "我转头，刚刚我们所在的球网边还在进行着别人的考试。"
    "那两个我不认识的人配合得十分出彩，几乎每一球都拿到了满分。"
    "我叹气，离开了羽毛球场。"
    $p.hal_p = 51
    $p.times+=1
    scene nightrun with fade
    $p.onOutside = True
    "意料之中，我被他删除了好友。"
    "这样的话，无论是要我向他道歉，补偿他，或者做一切只求他原谅的事都没可能了。"
    "羽毛球课已经结束了，我不知道他在哪一班，也不知道他是哪一届的。"
    "也许因为这次考试，他可能再也不会打羽毛球了。"
    "都是因为我。"
    "因为我。"
    $p.times+=1
    stop music fadeout 3
    $HallukeTask1.lock(p)
    $HallukeTask2.lock(p)
    $Achievement505.achieve()
    scene black with dissolve
    "……"
    play sound unlocking
    $pause(0.5)
    play sound audio.button
    scene livingroom
    $p.onOutside = False
    jump TaskExecuting



