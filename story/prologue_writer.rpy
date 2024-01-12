label writer_wakeup_pro:
    $quick_menu = False
    $_game_menu_screen = None
    
    scene black
    $quick_menu = True

    jump writer_beforeCircle_pro

label writer_beforeCircle_pro:
    if p.week==0 and p.day==29:
        jump writer_day0
    elif p.week==0 and p.day==30:
        jump writer_day1
    elif p.week==0 and p.day==1:
        jump writer_day2
    else:
        jump wakeup

screen screen_dashboard_abilities_wri(player):
    style_prefix "gameUI"
    $showtime = 0.2
    zorder 500
    vbox:
        xpos 0.02
        ypos 0.13

        vbox:
            label _("基础") text_style "gameL":
                at trans_toRight(0.2)
            $ info = _('今日种子：') + str(player.seed)# + _('\n当前Safe指数：') + str(player.safe)
            $ info1 = _('\n\n专注度可以使日程的获得更好结果的概率上升。\n\n基础专注度修正：') + num_str(Task.getConcScale(player), '++')
            $ info2 = _('\n\n使用食物和药物的恢复效率。\n\n基础食物恢复效率：%s\n最终食物恢复效率：%s') % (num_str(1-player.fooduse*0.005), num_str(player.useFoodScale()))
            $ info3 = _('\n药物恢复效率：') + num_str(player.useDrugScale())
            if player.name == 'Solitus':
                $ad = _('我的名字，非常适合我。')
            else:
                $ad = _('别人称呼我的方式，即便我并不喜欢这个名字。')
            textbutton player.name:
                at trans_toRight(showtime)
                action [Hide("info"),Show(screen="info_use", pp=renpy.get_mouse_pos(), i=info+info1+info2+info3, a=ad)]
                hovered Show(screen="info", i=info+info1+info2+info3, a=ad)
                unhovered Hide("info")
                text_style "gameUI"
                hover_sound audio.cursor

        vbox:
            $showtime += 0.05
            label _("情况") text_style "gameL":
                at trans_toRight(showtime)
            $meds = player.meds()
            if player.money < 300:
                $ info_money = _('我没有钱了，我只能努力工作然后祈祷自己会不在这个期间被公司开除。')
            elif player.money > 1000 and meds > 0:
                $ info_money = _('我已经买过这周要吃的药了，这些空闲的钱应该能让我美美过上一周。')
            elif player.money < 1500 and meds == 0:
                $ info_money = _('这些钱……足够我买药吗？')
            elif player.money < 3000 and meds == 0:
                $ info_money = _('呼，我喜欢发工资的感觉，但这些钱马上就会被购买药物的开销消耗殆尽。')
            elif player.money > player.price * 8:
                $ info_money = _('也许这次我可以不用把所有的钱拿来买药。')
            else:
                $ info_money = _('这些钱能买些什么呢……')
            $showtime += 0.05
            textbutton _("所持金钱 ") + str(player.money):
                at trans_toRight(showtime)
                action [Hide("info"),Show(screen="info_use", pp=renpy.get_mouse_pos(), i=_('购买药物和其他能够保障生存的东西。'), a=info_money)]
                hovered Show(screen="info",i=_('购买药物和其他能够保障生存的东西。'), a=info_money)
                unhovered Hide("info")
                text_style "gameUI"
                hover_sound audio.cursor

label writer_day0:
    $start_plot()
    "……"
    play music audio.pw
    scene pw1 with dissolve
    "“当你长大后你想做什么？”"
    "还小的时候大人们总是这样问我，随后再摸摸我的头。"
    "我知道他们根本不在乎这件事，所以我也并没有说话。"
    "见我不发言，话题便又被转移到其他地方去，但始终还是客套话。"
    "譬如孩子长得好高，长得很漂亮，学习也很不错，然而客观事实来看，那些赞美不尽真实。"
    "这并没有什么错，那样的问题也很常见——或许他们可能真的有一丝一毫的好奇，好奇这个孩子以后会做什么。"
    "年轻的孩子就像园圃里的幼苗，谁也不知道它们想长成什么样，想以什么方式去成长。"
    "但他们预见到了，我会成为一个无时无刻不想着放弃生命以及一切的东西的人吗？"
    "…"
    scene pw2 with fade
    "高中的时候，老师组织了一场活动，要我们把自己之后的梦想写出来。"
    "我瞥了一眼四周，大家似乎都没什么想法。"
    "那时的我，头疼频率也只是一周一次的小打小闹，对生活也没那么失望和无力。"
    "就像一个孩子，但又不太像普通的孩子…"
    "我拿起圆珠笔，它不沉也不轻，在我的手心之中停驻。"
    "我该有一个什么样的愿望呢？"
    "…"
    scene pw3 with fade
    "我喜欢在晚自习里读些课外小说。"
    "最初大家只是因为不愿意听课，随后从书店购买的一些千汇万状的小说便在班级中传阅着。"
    "我也曾有幸看过几本。"
    "有些是夸大甚至编造动物的自然习性以描述一些离奇的故事的书，大多数人将其信以为真。"
    "有些是讲贫困封建社会下人民发生的苦难——我并不讨厌看，只是觉得“观赏”苦难实在有些冷漠。"
    "在战争频发的国家里不乏描写战士血气方刚酣畅淋漓地战斗的文字，也有描绘他们坚韧不拔的精神的文字。"
    "但是有一流派则会探讨因战争带来的死伤引发的对于生命的思考，风格大多阴沉悲伤，像是一层乌云，盖在上方。"
    "他们对死亡的看法十分通透，解构着死亡的含义。对“世事无常”的理解也更为深刻。"
    "并非我热爱悲伤的故事，这些故事也并非完全是纯粹的悲伤。"
    "实际上这些故事大多写着人的一些微小的片段，偶尔愉快但大多平凡，又将死亡和变故穿插得稀松平常，反映出人们对这些命运的安排无能为力的心态。"
    "我有时候好奇，那位作者所写的故事是否都是他所亲身经历又稍作艺术化处理的？"
    "我并没有方法可以联系到他，也许可能真的是这样的。"
    "…"
    scene pw2 with fade
    "你觉得自己和其他人不一样吗？"
    "你认为你的思想比别人更加通透，更加清晰。"
    "让我们回到那个问题，我在以后想做什么？"
    "如果我是小学生，在同龄人畅所欲言说科学家，宇航员一类时可能会说公司的高管。"
    "而我已经是中学生了，能够独立思考，意识到以自己的能力连踏进那样公司的玻璃门都不配。"
    "我的成绩并不优秀，甚至平庸至极，我不配许什么人上人的愿望。"
    "有人说梦想就是要高高地挂在空中，可是如果一想到自己的梦想是几乎没法完成的，那这个梦想存在的意义何在呢？"
    "梦想应该是像承诺那样吧，许下之后就一定要在未来努力达成…"
    "旁边的人已经开始动笔了，而我的愿望是…"
    "我想写一本属于自己的书。"
    stop music
    "…"
    play music audio.concretejungle
    scene office with fade
    "一周前，我辞掉了我的这份在他人眼里十分优渥的职业。"
    "我从独木桥走过，最后又放弃了那个位置。"
    "辞职的原因也很简单，只是因为害怕头疼。"
    "这不是很有趣吗？"
    scene bedroom with dissolve
    "明明本身就对生命没什么眷恋，不如用每周的工资随意挥霍，等到玩够了或者疼得实在受不了，就一跃而下。"
    "但为什么那一刻就突然想起了小时候的梦想呢，而且还想要把它实现，更是可笑至极。"
    "暂且不提能不能赚钱，可能连看的人都没有几个——谁会想看一个满脑子都是不想活了的人的自我拉扯啊。"
    "但是，不知道为什么，还是想去，试着做一做。"
    "就像是排在死前要做的一百件事清单的最后一项一样。"
    stop music
    "…"
    scene hospital_corridor
    nurse"“病人848662号，能听见吗？”"
    "我突然回过神来，我在这里傻站着多久了……"
    $ss('normal2_eyes')
    s"“抱歉，刚刚在想事情。”"
    $sh()
    "她看上去有些不耐烦了，低头不再看我，将笔尖抵向写字板。"
    nurse"“……都需要什么药？”"
    show screen screen_dashboard_medicine(p)
    show screen screen_dashboard_abilities_wri(p)
    $temp = p.money
    call screen screen_buyMed(p)
    
    hide screen screen_dashboard_medicine
    hide screen screen_dashboard_abilities_wri
    
    if temp!=p.money:
        "我收下了药房护士递过来的药物，将它放进自己的随身斜挎包中。"
        "没有存款，没有工作，飘忽不定的写作根本没法赚到几个钱，我下周该怎么办……"
        "我已经打算放弃了，或许我早该从楼顶上跳下去。"
    else:
        nurse"“嗯？不买药？”"
        "没有存款，没有工作，飘忽不定的写作根本没法赚到几个钱。"
        "我把今天的钱都花光了也买不够要吃的药。"
        "我放弃了。"
        $Novice.clearByType(p)
        jump ending0
    "……"
    scene black with dissolve
    "…"
    "楼道的声控灯总是出问题，但电梯口到防盗门的距离并不远。"
    "我把手伸进斜挎包一侧的小袋，从里面摸出一串钥匙。"
    play sound unlocking
    "左旋，右旋，锁芯发出清脆的金属摩擦声。"
    "于是那门就被打开了。"
    scene workarea with fade
    play sound audio.itempaper
    "只是外出买药的运动量就让我的身体坚持不下去了。"
    "或许我根本就写不完什么小说吧。"
    "就像个孩子，做什么决定都像孩子一样，完全不考虑自己能不能活下去。"
    "到底是因为傲慢，觉得车到山前必有路的侥幸，还是直觉的引导呢……"
    "我坐在桌前的扶手椅上，将整个身体的重心向后挪。"
    "桌上除了电脑，还有前几天买的纸质本。"
    "不知道为什么，我明明可以用电脑码字，为什么非要动手来写呢……"
    "或许是想起高中的自己，总在晚自习大写特写一些无聊的抑郁文学吧……"
    "当周围平静下来，静谧带来的惬意仅会存在一小会，随后脑内的阵痛便接替了所有的感觉。"
    "我调整呼吸，将纸质本打开。"
    "或许把精神专注到别的东西上，就不会那么疼吧……"
    "我从笔篓中抽出一支笔，拽下笔帽，像那个不耐烦的护士一样，将笔尖以一种熟悉的角度抵在纸上。"
    "我突然想起曾经读过的一首诗。"
    "握着笔的手移动着，滚珠旋转将墨汁涂到纸面之上……"
    scene black with fade
    "“痛苦啊，你从未离开我那贫苦的心之火炉。”"
    "“比最为真挚的恋人更加多情…”"
    "……"
    $end_plot()
    scene black with dissolve
    $p.newDay()
    $Saver.save(p)
    $Notice.add('存档已保存！')
    $Notice.show()
    call loading from _call_loading
    jump writer_wakeup_pro



label writer_day1:
    $start_plot()
    scene bedroom with dissolve
    "……"
    "有时候我只是躺在床上发呆。"
    "像现在这样。"
    "有一种奇妙的疲倦感束缚着我，缠绕着我的躯体。"
    "并不是懒惰，而是失去了动力。"
    "这种感觉是从何开始的呢……"
    "……"
    "我记得刚开始独居的时候，会觉得用锅做饭实在是太省钱了，但是后来发现虽然省钱，但是消耗的时间翻了好几倍。"
    "你需要起得很早来到早市——为了便宜又新鲜的食物——农户们在天刚亮时便准备摆摊，一直到七八点左右。"
    "下楼，纠结早餐吃点什么，油腻的还是干燥的，凉一点的还是热的，面食还是包子之类的。"
    "然后再纠结中午和晚上吃点什么，穿过拥挤的人流，又被脚步极慢的人挡住步伐。"
    "你的手里掂量着沉甸甸的蔬菜和肉——如果你只买一餐的量，可能会被摊贩鄙视。"
    "你上楼，放空自己直到再次体会到饥饿，然后处理食材，洗菜，去皮，腌肉，把所有调料都放进去。"
    "焯水，你撇去浮沫，又小心地把水倒掉，一滴开水在被倒进水槽之前先溅到了你的身上。"
    "温度立刻摧毁你皮肤外表的细胞，疼痛感如同针扎被传递。"
    "你应该像所有人那样无意识地叫出一声“啊”，但你的身边并没有任何存在，呻吟毫无作用，你已经习惯了封紧嘴唇。"
    "当你把肉下进锅里时，滋啦滋啦的声音和逸散的血肉香气并没有让你感到开心，而是让你突然意识到还没有煮饭。"
    "你停下火，又去洗米，把淘米水倒进水槽，你的衣服被弄得湿乎乎的。"
    "打开电饭锅开关，你又回来炒肉，但已经兴致全无了。"
    "以上所有的这些，也可以只用五分钟点一份外卖代替。"
    "消耗的不仅是时间，还有无人帮忙排解的忧伤，你会觉得一点挫折就能打倒你，仅仅只是忘记煮饭这件事就让你胃口全无。"
    "你没有人去说出这些痛苦，你没有朋友。"
    "你甚至还一直头疼。"
    "…"
    "如果…如果有个人能听我说话，能让我把心里想说的都告诉他。"
    "那种心中舒畅的感觉会重新出现吗？"
    "被热水烫到之后，我爱的人便会来到我身边安抚我；当我突然想起没有开电饭煲的时候，我的爱人早就已经煮好饭了。"
    "而我也能给他煮点简简单单的食物，看着他被一块热豆腐烫到嘴巴时表情时笑出声来。"
    "然而此刻空荡的房间中只有我的呼吸声存在。"
    "好想……让人陪我啊……"
    "我的死亡和恋人……哪一个先来呢？"
    "…我喜欢什么类型的呢，果然还是青春靓丽的大学生吧…"
    "大概也是为了弥补大学期间完全没谈过恋爱的缺失，那明天去附近的大学转转好了。"
    "……"
    $end_plot()
    scene black with dissolve
    $p.newDay()
    $Saver.save(p)
    $Notice.add('存档已保存！')
    $Notice.show()
    call loading from _call_loading_2
    jump writer_wakeup_pro

label writer_day2:
    $start_plot()
    scene gym with fade
    "我来到了A市大学。"
    "并不是因为我毕业于此，而是这里离我的家不远。"
    "门口似乎要刷学生卡，但当通过闸机的人变多时，最前面的人刷卡之后，后面的人直接跟着他就能进去。"
    "我尽量保持自然，假装自己是个出去遛弯回寝室的大学生。"
    "保安对于我这个社会闲散人员的潜入似乎并不感兴趣，并没有多看我一眼。"
    "…"
    scene yard with dissolve
    "我进来了，虽然还是感觉有点奇怪。"
    "虽然从来没有来到过这里，仅仅只是跟随心中的直觉的结果，却有一种奇妙的即视感，好像在什么地方见过这里。"
    "是在梦里？还是另一个平行世界的我选择了这所大学？"
    "我的目光掠过身侧谈笑有无的学生群，以审视的目光清点着雄性身上的隆起和裸露出来的皮肤。"
    "能让他们其中随便一个人出来做我男朋友都好啊…"
    "可我连跟他们搭讪的勇气都没有，更别说还要分辨他们是不是直男了。"
    "果然，找一个男朋友是很难的事啊…我还是去体育馆饱饱眼福算了。"
    "…"
    
    scene court with dissolve
    "一楼是羽毛球馆，正好坐下来休息一会，待个几分钟就去二楼的篮球馆吧。"
    "我穿过场馆，坐在窗侧的长椅上。"
    "羽毛球馆里人还挺多的，但基本上都是各打各的，几乎找不到两边没人的球网了。"
    "我压低身子，胳膊肘支着大腿，另一侧的掌心扶着自己的头。"
    "羽毛球看似是最轻松的球类，但实际上不仅要在球网一侧跑来跑去，还要以合适的力度挥拍。"
    "我看着离我最近的一只略高偏瘦的鬣狗兽人在他的场内挥拍，然而羽毛球就这么掉在了他的身边。"
    "我并不是说一定要找一个运动能力强的，只是感觉对于他，我没什么兴趣…"
    "我继续观察，略过和我性别相反的学生，视线再次转移到另一侧。"
    play music audio.badmintonclass
    show halluke angry_eyebrow at trans_toRight()
    "一只稍矮的白熊吸引了我的目光。"
    "他在他的场地上微分双腿，重心下压，以马步的姿态面对着球网另一侧。"
    "圆耳朵轻微抖动，仿佛千里外有一只蚊子的声音他都能听见。"
    play sound audio.badminton
    "当白色的羽毛球从上空飞驰而过，他的身高似乎完全不像是劣势，轻跳起身击回了那球，发出清脆的砰砰声。"
    play sound audio.badminton
    show halluke sweat with dissolve
    "对手似乎抓住了机会，将白熊打过来的球扣杀出他的场地，球不再以弧线飞行而是朝着斜下方直线飞驰。"
    show halluke belly with dissolve
    play sound audio.badminton
    "但白熊同样也已极快的速度将扣杀的球反扣回去。"
    show halluke normal smile_eyebrow smile_mouth with dissolve
    "球落在了地上，白熊赢了。"
    "但除此之外，我的目光则集中于他娇小的身躯所爆发出的力量，他向左跳跃，又向右踏步过去。"
    "他跳跃，他向后撤，他向上，向下，向左，向右挥拍。"
    "黑色的短袖随着他的动作飘动，露出带着薄肌的腹部。"
    show halluke normal smile_eyebrow opened_mouth with dissolve
    "汗水在他的毛发之间闪光，还有他获胜者的笑容，露出舌头与可爱的犬齿。"
    "真想把阴茎放进去啊，再反复插入拔出，直到溢满唾液，再拽下他那松垮的短裤，侵犯他的后庭，同时用手玩弄他的处男阴茎。"
    "想得我都硬了。"
    "嗯…我怎么会有如此龌龊的思想呢…"
    "但意淫无罪，我也应当享受这种思想带来的慰藉…"
    stop music fadeout 3
    play sound audio.finishclass
    "铃声打断了我的思想。"
    hide halluke with dissolve
    "散乱的学生逐渐聚集成各个方阵，我起身，准备离开羽毛球馆。"
    unk"“不上课吗，你哪个班级的？”"
    "我被吓了一跳，转头之后，似乎是个比我年长十几年的老师站在我的面前。"
    "一时间让我有点不知所措。"
    menu:
        "说自己身体不舒服":
            unk"“这样啊，那你先去和辅导员请假吧，对了，你是哪个班级的，叫什么？”"
            "我更加慌乱，不知道说什么，朝着体育馆的门跑走了。"
        "说自己其实是要上游泳课":
            unk"“不可能，现在就我们羽毛球馆在上课啊？”"
            "他抓住了我的手臂。"
            unk"“你哪个院的？把你们辅导员叫来…”"
            $ss('scared_eyebrow scared_eyes scared_mouth')
            s"“我…我…”"
            $sh()
            "我不敢看着他的眼睛，手臂被紧紧拽住无法逃脱，只感觉头部开始阵痛，随后扩散到全身…"
            scene black with dissolve
            "…"
            show screen freeze(3)
            pause
            $Achievement100_1.achieve()
            $Achievement.show()
            $Notice.show()
            "{color=#FF0000}Bad Ending ？\n——前面的区域，下辈子再来探索吧。{/color}"
            return
        "说自己只是打羽毛球的":
            unk"“哦，下次记得不要这个时候来用羽毛球馆了，我们要开始上课了。”"
            "我松了一口气，对他笑了笑，离开了体育馆。"
        "说自己只是想找厕所":
            unk"“早干什么去了，快去上课，你哪个班级的？”"
            "我颤颤巍巍，指着白熊那边的班级。"
            unk"“那快去吧。”"
            "我只能履行刚才说的话，朝着白熊的班级走。"
            "…"
            scene court with fade
            play sound audio.finishclass
            $p.gain_abi(0.02, 'phy', stat='剧情')
            $Notice.show()
            "下课铃响了…"
            "脑袋乱糟糟的，现在一想，刚才点名的时候居然没关注一下那只小白熊叫什么。"
            "下周这个时候要再来这里吗…"
            "课上大概也只是说了一些基础的东西，看样子应该刚开课不久。"
            "有些人没带羽毛球拍，但毕竟是第一节课，老师要求我们下次上课的时候必须要有一个{color=#ffe600}羽毛球拍{/color}。"
            "我记得商店街有一家文体商店，但我不记得是哪家了，有时间去看看吧…"
            "我叹气，离开了体育馆。"
        
    
    
    scene livingroom
    "到家了。"
    "没什么事做的话，就看会莓博好了……"
    scene meibo_1 with dissolve
    "…“莓博”是一个博客类型的社交网站，博主们可以发他们想发的东西，一些文字，或者是图片，或者是自己的画。"
    "然后别人可以通过评论来互动，也有转发之类的功能…"
    "我打开电脑，从收藏夹里点击“莓博”的网站图标。"
    "我关注了很多画师，因为我很羡慕会画画的人。"
    "而我只会一点点写作，还只能算是平庸的水平。"
    "大家从会说话开始就在学习写作，而画画不仅需要天分，还需要成倍的努力和道具。"
    "我没有那样的天赋，也没有那样的努力。"
    "我只能通过文字的方式，表达一些无聊的东西。"
    "我的双眼快速地扫过一张张熟悉画风的作品，在感到兴奋之余也不停点赞转发，希望能给他们带来一些新的人气。"
    "…"
    "我的目光停在一个陌生的id上。"
    scene meibo_2 with dissolve
    "这是一幅短漫，作者的名字并非在我的关注列表中，似乎是某个我已经关注了的画师转发的。"
    "我点进了他的主页。"
    "他的id是赤松Akamatsu，似乎是刚刚才在这个平台注册的账号，现在的他正把之前在其他平台的画搬运到这里。"
    "他画了很多简单的插图和短漫，基本上都关于两个固定的角色，似乎是狮子和狼的故事，演绎一些日常的琐事和有趣的灵感。"
    "画风也简单可爱，类似于简笔画，却又能看出底力所在。"
    "我保存了图片，同时点击了关注按钮。"
    "不错，期待他能画出更多的新作品。"
    "……"
    scene livingroom with dissolve
    "看了半天莓博，天色已经开始变暗了。"
    "明天就是周一了，但工作日的概念对于我来说并没有意义。"
    scene bedroom with dissolve
    "我关上电脑，简单冲了个热水澡后上了床。"
    "在下周六之前，我最好买一个{color=#ffe600}羽毛球拍{/color}，如果我还想去体育馆见见他的话。"
    $end_plot()
    scene black with dissolve
    $p.mental = 120
    $p.newDay()
    $Saver.save(p)
    $Notice.add('存档已保存！')
    $Notice.show()
    call loading from _call_loading_7
    jump writer_wakeup_pro

