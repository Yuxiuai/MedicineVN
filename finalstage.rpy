init python:
    def to_the_final_stage(player):
        for i in range(len(player.effects) - 1, -1, -1):
            if player.effects[i].duration != -1:
                player.effects[i].clear(player)
        for i in range(len(player.items) - 1, -1, -1):
            if type(player.items[i]) not in (Sticker59, DrugFake):
                if player.items[i].kind == '实验药物' and not player.items[i].broken:
                    continue
                player.items[i].remove(player)
        
        if Sticker59.has(player):
            Sticker59.get(player).disableAction(player)
            
        player.p2 = Player()
        player.p2.mental = 100
        player.p2.newSeed()
        if player.route == 'h':
            player.p2.name = 'Halluke'
        if player.route == 'a':
            player.p2.name = 'Acolas'
        player.p2.drugRecovery = 1.5
        player.p2.deteriorateConsumption = 0.3
        player.p2.drugfake = False
        player.p2.effects.append(Despair())

        player.finalStageDays = 0
        player.plan = [NoTask, NoTask, NoTask]
        player.plancheck = [False, False, False]

        player.aco_p = -1
        player.hal_p = -1

        WeatherNone.add(player)
        if Despair.has(player):
            Despair.clearByType(player)
        Despair.add(player)


label writer_before_earthquake:
    $ renpy.block_rollback()
    stop music
    if p.mental < 5:
        $p.mental = 60.0
    scene black
    "……"
    scene bedroom with fade
    "我睁眼。"
    "吸进鼻腔的凌晨的空气有种孤独的潮湿感。"
    "天似乎刚刚亮，但我却十分清醒。"
    "意外地，头没有那么疼。"
    "……"
    "几个月过去了。"
    "我变了很多，非常多。"
    "我开始频繁读曾经不屑于读的书，写很多的委托。"
    "现在拥有了很多很多粉丝。"
    "我开始吃药，大量的药，各种不同的药，也从来没像以前那样忘记吃药，或是忘了买药。"
    "我试着探索这个城市，直到把每个地方能做什么，有什么东西卖都记得滚瓜烂熟。"
    "我甚至有了一比不小的积蓄。"
    "这是，怎么回事呢。"
    "在活着的这二十几年里，我有过如此自律努力的时候吗？"
    "甚至在面对人生最重要的考试的前几天，还在床上玩手机，和别人在网上用文字演绎交配的动作。"
    "为什么到了现在，就变了呢？"
    "是因为我不这样做就会“死”吗？"
    "我被什么超脱于我的存在控制了吗？受一位“木偶师”的操纵去做那些我从来都没动力去做的事吗？"
    "甚至我心里所想，口中所言都能被他听见吗？"
    "是这样吗？"
    "他现在正在看着我吗？"
    "我经常会这么想，想象自己就像是某个养成游戏的主角，被玩家操控着去做一些提升自己某些数值的事。"
    "想这些没什么意义，不过很有趣。"
    "那么，在经历了这一切后，我感到开心吗？"
    "我和我也许喜欢的人度过了一个“美妙”的周末，但我却完全感觉不出来有多开心。"
    "我想起小时候，有一个宣传得很美好的展会。"
    "一般来说，这样的展会都是开在大城市的，B市所在的省的省会还没有这么“现代”，展会能开在B市的省会城市是很罕见的事。"
    "即便价格也不高，但还是抵得上我好几天的餐费。"
    "当时的我为了这个展会攒了很多钱，但还是差一些入场费。"
    "我厚脸皮和家长要了入场费的钱，在展会开放的一大清早，孤身一人上了火车。"
    "展会去的人很少，展会场地也很小，大概一个高中教室的大小。"
    "也没什么活动，荧幕仿佛是一个仅用来做光源的摆设。"
    "晚上我便回去了。"
    "后悔吗？也许我应该后悔的，但是已经花掉的钱，后悔也不会再回来。"
    "思维回到现在。"
    "即便我没有为船票花钱，上船，和那位我并不爱的先生做爱，都没有让我觉得多值。"
    "…也许只是我把他当成了这艘轮渡酒店之旅的全部，至少我还看到了海。"
    "但我…绝对不会在和别人聊起这段时光的时候，把这场免费获得的奢华旅程标上美好回忆的标签。"
    "…"
    "我需要吃药吗？"
    "……"
    "我已经厌倦吃药了。"
    "也许是因为我马上就要从这种生活中解脱了吧。"
    "周末，只要到了周末就好了。"
    "一切都会好起来的，一切都会结束的。"
    "……"
    "但，他。"
    "我就不应该接触所谓的爱情的，我真正想要的到底是什么呢。"
    "为什么我得到了生命中的某个重要的存在，却开心不起来呢。"
    "我没想过这被世人歌颂的爱情乱七八糟像团乱麻，缠在我身上。"
    "痛苦永远都在继续。"
    "痛苦永远不会远离。"
    "我感到难以呼吸。"
    "……"
    "痛苦是艺术的食粮。"
    scene workarea with fade
    "……"
    "我拿出了那本小说原稿。"
    "将轮渡上的谈话，我的痛苦，我的疑问，我的孤独，还有现在的思考如若倾盆般倒入其中。"
    "我的笔飞速刻画下仅我自己能够理解的笔画，墨水如喷泉般溅出。"
    "……"
    "这就是，最后一章了。"
    $WriterItem5.add(p)
    $Notice.show()
    "我合上书，然后将笔丢进垃圾桶里。"
    "该启程了。"
    jump we


label before_earthquake:
    $ renpy.block_rollback()
    stop music
    if p.mental < 5:
        $p.mental = 60.0
    scene black
    "……"
    scene bedroom with fade
    "我睁眼。"
    "吸进鼻腔的凌晨的空气有种孤独的潮湿感。"
    "闹钟还没响，我也并不想知道现在是什么时候。"
    "但我十分清醒。"
    "现在是属于我的时间。"
    "用于思考的时间。"
    "意外地，头没有那么疼。"
    "思考，思考什么呢。"
    "几个月过去了。"
    "我变了很多，非常多。"
    "我工作越来越努力，我开始频繁写作，甚至还会经常出入健身房。"
    "我开始吃药，大量的药，各种不同的药，也从来没像以前那样忘记吃药，或是忘了买药。"
    "我试着探索这个城市，直到把每个地方能做什么，有什么东西卖都记得滚瓜烂熟。"
    "我甚至有了一比不小的积蓄。"
    "这是，怎么回事呢。"
    "在活着的这二十几年里，我有过如此自律努力的时候吗？"
    "甚至在面对人生最重要的考试的前几天，还在床上玩手机，和别人在网上用文字演绎交配的动作。"
    "为什么到了现在，就变了呢？"
    "是因为我不这样做就会“死”吗？"
    "我被什么超脱于我的存在控制了吗？受一位“木偶师”的操纵去做那些我从来都没动力去做的事吗？"
    "甚至我心里所想，口中所言都能被他听见吗？"
    "是这样吗？"
    "他现在正在看着我吗？"
    "我经常会这么想，想象自己就像是某个养成游戏的主角，被玩家操控着去做一些提升自己某些数值的事。"
    "想这些没什么意义，不过很有趣。"
    "那么，在经历了这一切后，我感到开心吗？"
    "我和我也许喜欢的人度过了一个“美妙”的周末，但我却完全感觉不出来有多开心。"
    "我想起小时候，有一个宣传得很美好的展会。"
    "一般来说，这样的展会都是开在大城市的，A市所在的省的省会还没有这么“现代”，展会能开在A市的省会城市是很罕见的事。"
    "即便价格也不高，但还是抵得上我好几天的餐费。"
    "当时的我为了这个展会攒了很多钱，但还是差一些入场费。"
    "我厚脸皮和家长要了入场费的钱，在展会开放的一大清早，孤身一人上了火车。"
    "展会去的人很少，展会场地也很小，大概一个高中教室的大小。"
    "也没什么活动，荧幕仿佛是一个仅用来做光源的摆设。"
    "晚上我便回去了。"
    "后悔吗？也许我应该后悔的，但是已经花掉的钱，后悔也不会再回来。"
    "思维回到现在。"
    "即便我没有为船票花钱，上船，和那位我并不爱的先生做爱，都没有让我觉得多值。"
    "…也许只是我把他当成了这艘轮渡酒店之旅的全部，至少我还看到了海。"
    "但我…绝对不会在和别人聊起这段时光的时候，把这场免费获得的奢华旅程标上美好回忆的标签。"
    "…"
    play music audio.alarm
    "闹钟响了…"
    stop music
    play sound audio.button
    "我已经厌倦关闹钟了。"
    "也厌倦了吃药。"
    "也许是因为我马上就要从这种生活中解脱了吧。"
    "周末，只要到了周末就好了。"
    "一切都会好起来的，一切都会结束的。"
    "……"
    "但，他。"
    "我就不应该接触所谓的爱情的，我真正想要的到底是什么呢。"
    "为什么我得到了生命中的某个重要的存在，却开心不起来呢。"
    "我没想过这被世人歌颂的爱情乱七八糟像团乱麻，缠在我身上。"
    "痛苦永远都在继续。"
    "痛苦永远不会远离。"
    "我感到难以呼吸。"
    "……"
    "起床洗漱吧。"
    scene livingroom with fade
    show screen screen_dashboard(p)
    "……"
    if p.route == 'h':
        scene morningrun with fade
        "我像往常那样离开小区，突然看到街边有一个格外显眼的红色的身影。"
        "他在对我招手。"
        show halluke shirt angry_eyebrow angry_eyes smile_mouth with dissolve
        h"“嘿！[p.name]！”"
        "Halluke？他怎么会在这里？"
        "他的出现让大脑稍微清醒了一点。"
        "我能清醒地意识到，我的大脑正在分泌些什么。"
        "惊喜，幸福，快乐，还是恐惧？"
        "我暂时没法识别那代表什么，我只是朝着他的方向走去。"
        "如果他没看见我的话，我一定会想假装没看见他那样快步溜过去的。"
        show halluke shirt normal_eyebrow angry_eyes normal_mouth with dissolve
        h"“我…我想了很多…”"
        show halluke shirt normal_eyebrow normal_eyes smile_mouth with dissolve
        h"“要不！我们同居吧！”"
        "啊…"
        "同居…"
        "我从没想过同居这件事。"
        "这代表着什么？更多的我不需要的陪伴？更多的千篇一律的性爱？"
        show halluke shirt awkward_eyebrow shy_eyes smile_mouth with dissolve
        h"“还有还有…我可以去你的公司里转转吗？今天上午我都没课哦！”"
        "我决定先把同居的事放在一边。"
        $ss("normal2_eyes scared_eyebrow ques")
        s"“那个，为什么要去我公司？”"
        $sh()
        show halluke shirt awkward_eyebrow shy_eyes opened_mouth with dissolve
        h"“不可以吗？我想看看未来的我的工作会是什么样的。”"
        $ss()
        s"“哦…”"
        $sh()
        show halluke shirt normal_eyebrow angry_eyes smile_mouth with dissolve
        h"“那我就当你同意同居了。”"
        $ss("normal2_eyes")
        s"“诶…”"
        $sh()
        show halluke shirt awkward_eyebrow normal_eyes normal_mouth with dissolve
        h"“我这边的租期快到了嘛…而且你也是租房子的吧？”"
        h"“我们一起付房租，可以一起省点钱嘛——”"
        show halluke shirt angry_eyebrow angry_eyes smile_mouth with dissolve
        h"“更重要的是！我们都是情侣啦，当然要同居啊！”"
        show halluke shirt angry_eyebrow angry_eyes cry_mouth blush with dissolve
        h"“你不在我身边的时候…我一直都在想你诶…想你想你想你…很想你…”"
        "这只小家伙张开双臂，像做捕食训练的幼崽，紧紧抱着我。"
        "…"
        "我能拒绝吗？我没有理由拒绝。"
        $ss("mood")
        s"“…好吧？…”"
        $sh()
        show halluke shirt awkward_eyebrow angry_eyes smile_mouth with dissolve
        h"“好耶！——”"
        "我尽力不让他看到我的表情。"
        "他就这样跟着我直到公司。"
    scene corridor with fade
    "打卡。"
    "好像，我似乎对一切“旧”的东西都厌倦了。"
    "没有头疼的世界是什么样的？"
    "它比学生时代的暑假还美丽吗？比发工资那天还幸福吗？"
    "这一切都结束了吗？"
    if p.route == 'h':
        show halluke shirt normal2_eyes normal_mouth with dissolve
        h"“[p.name]…？怎么了？…”"
    if p.route == 'a':
        show acolas normal_eyes smile_mouth with dissolve
        a"“早啊，[p.name]…需要我帮你泡杯咖啡吗？”"
        show acolas surprised_eyebrow awkward_mouth with dissolve
        a"“怎么了，你怎么一直盯着打卡机？”"

    "我意识到自己已经盯着打卡机几分钟了。"

    $ss("white glasses no_hat")
    s"“不…没什么…”"
    $sh()

    "我不该想这么多。"
    "至少我得撑过这周才行。"
    "即便我不头疼了，我也要工作啊。"
    "不能因为即将解脱而丢了工作。"
    scene office with fade
    if p.route == 'h':
        "Halluke跟着我进到了办公室内，同事们似乎对他这个陌生人不是很感兴趣，又或者可能是因为太早了，大家都昏昏欲睡吧。"
    if p.route == 'a':
        "Acolas拿着一袋速溶咖啡也踏进了办公室，那一会就用热水壶烧点开水泡杯咖啡吧。"
    "我摇了摇头。"
    "清醒一点。"
    "该计划一下今天要做的事了。"
    "…"
    play music audio.anxietyspreading
    "等等，计划什么呢。"
    "我能做什么？"
    "无非是点外卖吃饭，吃药，工作而已。"
    "这也值得我花时间去“计划”？"
    "…不，这不太对，我应该要计划的。"
    "我应该计划的。"
    "我，我应该把要做的事…从…一堆…能做的…日程中…选择出来？"
    "…我应该点击…“背包”？…“库存”？…"
    "手机…为什么我的手机…一直是这个…壁纸？…难道我一直没想过…换一个吗？"
    "我…"
    jump earthquake












label earthquake:
    scene black
    stop music
    $clearscreens()
    play sound audio.earthquake
    call screen cfreeze(12)
    $ to_the_final_stage(p)

    "它发生了。"
    "摇晃，摇晃。"
    "当我意识到脑内名为地震的名号终于出现之时，想要逃离已经晚了。"
    "我因震动摔倒在地，随后便是玻璃破碎，电火花声，尖叫，还有逃离的声音。"
    "这座钢铁丛林正在崩塌，而我几乎在离地几十米的高空之上。"
    "我会怎样？我会死吗？"
    "我身体下的水泥会塌陷吗？我头上的桌子会被落下来的水泥碎片压碎吗？"
    "空调的气味几乎是一瞬间就被灰尘味掩盖了，随之而来的还有刺鼻的血腥味。"
    "我不敢想象平时和我坐在同一个办公室的人的惨烈死状，但我至少可以挽救他。"

    if p.meds() == 0:
        jump earthquakeBE

    "世界还在摇动，我用尽全力把身边的摔倒的[p.p2.name]从门口的打卡机附近拽到相邻的我自己的桌子底下。"
    "也许…也许能撑一段时间？"

    "我注意到我的桌子底下放着备用的饮水机用的罐装水，而抽屉里应该还有公司之前发的当作午饭的吐司面包。"
    "看来口味刁一点也是好事，虽然这东西一点都不好吃，但至少抗饿。"
    "如果有这样的条件，那我们还能在被掩埋后存活一段时间来等待救援。"
    "…"
    "世界仍然没有停止摇动。{w}直到一块巨大的建筑碎块坠落在他的上方。"
    "幸运的是，坠落的水泥块被桌子和其他碎块卡住了，只发出一阵巨大的撞击声，没有压碎我们两个可怜虫的尸体。"
    "但。"
    if p.route == 'h':
        h"“[p.name]！…啊！…”"
        "从那碎块中延伸而出的半截断裂的钢筋，从趴在地上的白熊的背后径直穿透了他，在腰部突破而出，像大号图钉一样把他固定在地面上。"
    if p.route == 'a':
        a"“[p.name]！…啊！…”"
        "从那碎块中延伸而出的半截断裂的钢筋，从趴在地上的狼的背后径直穿透了他，在腰部突破而出，像大号图钉一样把他固定在地面上。"
    
    "不…不……不………！"
    "…"
    call screen cfreeze(3)
    scene ruins with fade
    "终于，世界不再摇动了。"
    "影视作品中人物面对超出承受能力的血腥或是灾难景象时都会表现得如同被定身一般，思维也停滞于那一刻。"
    "吓到瘫软？吓到定住？"
    "我不知道我是哪种情况，或许都有。"
    "我看着眼前的人的身体下方开始溢出血液。"
    "急救，急救！可现在谁能来救？"
    "我应该做什么？"
    "叫他的名字？摇晃他的身体保持他的清醒？还是把他当成食物来确保自己在接下来这几天不会饿死？"
    "他的呼吸十分急促，像溺水的人努力呼吸却无法获取氧气的样子。"
    "这代表他的肺被穿透了吗？"
    "不不不不…我…我得做点什么，我必须做些什么。"
    $ss("dirty no_hat scared_eyebrow scared_eyes scared_mouth")
    s"“[p.p2.name]，还…还能听到我说话吗？”"
    $sh()
    if p.route == 'h':

        h"“[p.name]…好疼……好疼…救我……我…我快死了…我…”"
        $ss("dirty no_hat agony_eyebrow normal_eyes")
        s"“冷静下来！…深呼吸…别怕…”"
        $ss("dirty no_hat agony_eyebrow sad_eyes")
        s"“你不会死的，马上就会有人来救我们出去…现在不要说话了…保存你的体力…”"
        $sh()

    if p.route == 'a':
        a"“啊啊啊啊…[p.name]…我…啊啊啊…[p.name]…”"
        $ss("dirty no_hat agony_eyebrow sad_eyes")
        s"“别说话，呼吸…呼吸…我们会没事的…我们会出去的…保存体力…撑下去…”"
        $sh()

    "我将手放到[p.p2.name]的额头上，他的呼吸随着我的言语似乎也变得平缓一些了。"
    "太好了，他没有死。而且钢筋似乎也没有破坏到他的要害…"
    "他…他肯定能活下来，如果这样的话…"
    "我从口袋中的药瓶里倒出来一粒药，再从桶装水里压一杯水，把混有药片的水倒进他的嘴里。"
    "一定…一定会有用的。"
    "我该庆幸身下这块地板没有塌陷，但也有可能同一楼层只有我所在的这个地方没有塌而已。"
    "但现在的情况我也没法确认，唯一知道的是我们被破碎的水泥碎块压埋了，以及他受了重伤。"
    "仅有微弱的呼气声占据了世界，剩下的则只有寂静，来自别人的呼喊声和求救声也没有了。"
    "此刻比刚才更加浓郁的血腥气让人忍不住反呕。"
    $ss("dirty no_hat sad_eyebrow")
    s"“……[p.p2.name]，还疼吗？”"
    $sh()
    "不知道给他吃的药有没有效果，但他仍然活着就是好事。"

    if p.route == 'h':
        h"“不太疼了…但还是…”"
        "他没看我，只是趴在地上，大概连抬头的力气都没有了。"

    if p.route == 'a':
        a"“好点了…但按理来说…我现在怎么还能说话…？”"
        a"“为什么，感觉…没那么…疼了…”"

    "即便我从来都不想和别人提起关于自己的缺陷这件事，但既然已经到了这个关头，还是讲清楚好了。"
    $ss("dirty no_hat sad_eyebrow")
    s"“我…在你的杯子里，放了药。”"
    s"“强效的止痛药。”"
    $sh()

    if p.route == 'h':
        h"“止痛药…也不会有…这么强的效果吧？…”"
    if p.route == 'a':
        a"“止痛药…也不会有…这么强的效果吧？…”"

    $ss("dirty no_hat sad_eyebrow")
    s"“其实…我有很严重的头疼，而且是从小到大一直在恶化的头疼病。”"
    $ss("dirty no_hat sad_eyebrow normal2_eyes")
    s"“自从我被诊断出来这样的情况，就开始吃药了。”"
    s"“几个月前，我的头疼加重到之前吃的头疼药都没法缓解的地步，才从医师手里弄来这种国外的强效止疼药。”"
    $ss("dirty no_hat sad_eyebrow closed_eyes")
    s"“抱歉，一直没和你说过这件事…我只是不想让我身边的人知道我的病，我不想被人当成是某些需要照顾的人。”"
    $ss("dirty no_hat sad_eyebrow normal_eyes")
    s"“为了救你，我必须这样做。”"
    $sh()

    "我期待从他们脸上看到什么情绪。"
    "惊讶，疑虑，困惑？"
    "但他们连开口说话都需要付出全力，甚至头都没法用自己的力量抬起来，我又怎么能期待他们给我做出什么反应呢。"
    "他们心里可能也很复杂吧，在知道了这种事情后？需要时间来消化？"
    "白痴，这种事其实也没什么好消化的吧。"

    if p.route == 'h':
        h"“是…这样啊…”"
        h"“抱歉…[p.name]。”"
        h"“不知道……现在感谢你…算不算晚……只不过我可能接下来就没机会说了……”"
        h"“我肯定马上就要死了……”"
        h"“现在才发现……死亡……一点都……不好啊……”"
        h"“[p.name]…我没法…理解你的痛苦…但你肯定…有过曾经和我一样的想法…”"
        h"“如果你…离开了这里…请一定要好好…活着。”"
        h"“在遇到你之前…我只觉得…人生…很无趣…”"
        h"“…如果你…坚持不下去了…也不要…想不开啊…”"
        h"“我想…我就是为了见到你…才存活到…现在的…”"
        h"“一定是…”"
        h"“我真的…很喜欢你…也很感谢你…”"
        h"“要活下去…”"

    if p.route == 'a':
        a"“…这样啊…”"
        a"“难怪…我偶尔会看到…你下班之后…就去医院的事…”"
        a"“…但你工作…那么努力…一定也是下了很大的…努力了吧…”"
        a"“我还逼你…做那些事…”"
        a"“抱歉…[p.name]。”"
        a"“其实我…从来都觉得…自己这么做…即便是错误的…”"
        a"“但还是觉得，做错事…是我的个性…”"
        a"“自私…也是我的个性…”"
        a"“…让你感到痛苦了吧…我知道的…但我一直不敢和你…道歉…”"
        a"“真是…对不起啊…”"
        a"“嘿嘿…都快死了…才想起来…和你道歉…不愧是我啊…”"
        a"“哎呀……虽然你的止痛药很厉害，但可能我还是会死……”"
        a"“我还有……很多东西没读完……很多事情没做过……现在就要死了……”"
        a"“倒是突然感觉……也不是很……难受嘛……多亏了你……”"
        a"“但是……你受伤没有我严重，你还有希望活下去。”"
        a"“……我很幸运……这辈子能遇到你……”"

    "我沉默着。"
    "我应该哭吗，在他说了这些感人的东西之后？"
    "像言情小说里的生死决别情节一样？"
    "我珍惜他吗？他的死会改变什么？会影响我什么？"
    play music audio.solitus
    $ss("dirty no_hat")
    s"“…我听到了。”"
    s"“但是，相信我。”"
    $ss("dirty no_hat sad_eyebrow")
    s"“如果药有作用，那么你就能活下去。”"
    s"“和我一起活下去。”"
    $ss("dirty no_hat sad_eyebrow sad_mouth")
    s"“别说那些话，你肯定能活下去的，明白吗？”"
    s"“救援马上就要来了…我们只需要等几个小时而已…”"
    $ss("dirty no_hat sad_eyebrow sad_mouth tear")
    s"“我们有水，有食物，有止痛药。”"
    s"“真的，真的，我们很有希望活下去的！”"
    s"“别放弃啊！”"
    $sh()
    "我也能说出如此慷慨激昂的话吗？"
    "说出这些话，就代表自己的行为能对得起内心的到的标准了吗？就能毫无愧疚地面对眼前的人的死亡了吗？"
    "我闭眼。"
    "脸上的眼泪，是什么时候流出来的？"
    "…"

    if Achievement400.has() or Achievement403.has():
        menu:
            "是否直接抵达已经完成过的内容？"
            "废墟线坏结局" if Achievement104.has():
                jump despairBE
            "废墟线普通结局" if Achievement400.has():
                jump ne
            "废墟线真实结局" if Achievement401.has():
                jump te
            "废墟线虚伪结局" if Achievement403.has():
                if p.route == 'h':
                    jump fe_h
                elif p.route == 'a':
                    jump fe_a
                else:
                    "出现错误。"
                    return
            "不需要":
                pass
            

    jump despair_dayend


label despair_execution:  
    $routine_music(p)
    if p.times <= 2:
        $renpy.sound.stop(channel="chara_voice")
        $p.plancheck = [False, False, False]
        call screen screen_operate(p)
        hide screen info
        hide screen info2
        hide screen info3
        $p.times = 3
        jump despair_execution
    elif p.times == 3:
        $donextplan(p)
    elif p.times == 5:
        scene ruins with fade
        "……头好疼……"
        "要不要吃点药……"
        call screen screen_operate(p)
        hide screen info
        hide screen info2
        hide screen info3
        scene ruins with fade
        "……下一件事。"
        jump despair_execution
    elif p.times == 6:
        $donextplan(p)
    elif p.times == 8:
        scene ruins with fade
        "……好疼……"
        "再不吃药……肯定要晕过去了……"
        call screen screen_operate(p)
        hide screen info
        hide screen info2
        hide screen info3
        scene ruins with fade
        "……呼……哈……呼……"
        jump despair_execution
    elif p.times == 9:
        $donextplan(p)
    elif p.times == 11:
        scene ruins with fade
        $Notice.show()
        "……又渴又饿，头还这么疼……我是不是快死了？……"
        "……不……还不能放弃……至少……"
        call screen screen_operate(p)
        hide screen info
        hide screen info2
        hide screen info3
        scene ruins with fade
        "……"
        "今天的救援仍然没有到来，也许我们已经被抛弃了吧，我们的生命对他们来说毫无价值。"
        "也许救援工作实在难以展开，或是幸存的希望都留给富人们了，而我们只是没用的垃圾吧。"
        "……接下来这段时间稍微休息一会吧……"
        stop music fadeout 4
        if p.mental <= 0:
            
            $clearscreens()
            jump despairBE
        jump despair_dayend

label despair_dayend:
    $ p.newDay()
    $ p.finalStageDays += 1
    if not p.p2.drugfake:
        $ Saver.save(p)
        $ Notice.add('存档已保存！')
        $ Notice.show()
    call loading from _call_loading_8
    if p.p2.drugfake:
        jump despair_end
    jump despair_wakeup

label despair_wakeup:
    "……"
    scene ruins
    "我睁眼。"
    show screen screen_dashboard(p)
    play music audio.drownedindespair 

    if p.meds() == 0:
        "人们如何定义睁眼？让光线重新照射进位于面部上放的两颗透光的玻璃状圆球里？"
        "睁眼和不睁眼似乎是一样的，我的眼前仍然是黑，几乎没有一丝光线透进来。"
        "我的新床——一大堆断裂的但还算得上平整的瓷砖地板——我的身体甚至已经习惯了这个新的卧室了。"
        "至少我的身体没有那么痛了。"
        "我的脑子已经没法思考了，或者说我无法支付思考所需要的能量，即便记录时间并不会对活下去带来什么作用，但我还是把它作为一份必要的支出。"
        "不过说真的，如果我没能获救，会不会有人打开我的脑壳来读取这些信息？"
        "…哼，大脑不是硬盘而是内存，如果断电了，信息应该也都没了吧。"
        "我想起小时候的我，随便头疼不及现在，但由于胃病之类的原因，就算饿了，也不会有饿的反应。"
        "所以每次我在忘记吃饭的时候，无法发出声音的饥饿就会为头疼添些柴火来督促我吃点东西。"
        "毕竟大脑消耗了身体中很大占比的能量啊，没有了能量，脑袋就会疼起来了。"
        "…真是的，这些胡思乱想不也要消耗能量吗。"
        "还是想一些有用的东西吧。"
        "如果我的感觉没问题的话…今天应该是在废墟下的第[p.finalStageDays]天了……"
        "之前购买的药物，现在应该全部变质了吧。"
        "…可我又能怎么办呢…"
        "难道就眼睁睁地把这些药都丢掉？"
        "虽然我从来都没试过在过期之后吃这些药，但…"
        "我还有其他的办法吗？"
        "因为无药可吃而死，或是因为过期中毒而死？"
        "…"
        "也许这只是Pathos为了盈利说出的谎言，哪有什么药保质期只有一周的？"
        "但可能这药就是特殊呢？…或是……"
        "管不了那么多了…"
        python:
            for i in p.items:
                if type(i) in (MedicineA, MedicineB, MedicineC) and i.broken:
                    i.du = -1
                    i.broken = False
    else:
        "大概是因为太困了所以睡着了吧。"

        "我每天都幻想，在闭上眼睛之后，我便会在家里的床上醒来，然后闭着眼睛逼迫着起床把发出尖锐声音的闹钟关掉。"
        "但这一切都不是梦，也永远不会发生。"
        "死亡每天都在逼近，饥饿令头疼更加狂躁。"
    "我将抽屉里的面包扯下一小块塞进嘴里。"

    if p.p2.mental <= 0:
        if p.route == 'h':
            "当我将面包塞进白熊的口中时，触碰到他的手时，却只感觉一阵冰冷。"
            "……"
        if p.route == 'a':
            "当我将面包塞进狼的口中时，触碰到他的手时，却只感觉一阵冰冷。"
            "……"
        $clearscreens()
        jump despairBE

    "然后再将面包撕下来给他一点。"
    "虽然他闭着眼睛，但每当我把手塞进他口中，都能感觉到微弱的温暖，和他将面包舔进口中的动作。"
    "……呼，还活着。"

    "那么，该计划一下今天要做的事了。"
    jump despair_execution


label DespairWaiting_beginning:
    scene ruins with fade
    $r = rd(1, 10)
    if r == 1:
        "这种情况下只能保存体力等待救援……"
    if r == 2:
        "……到底还要等多久呢。"
    if r == 3:
        "又渴又饿……抽屉里应该还有昨天剩下的面包……但现在还不是吃的时候。"
    if r == 4:
        "……饮水机里的水已经不多了，虽然很渴，但还能忍受。"
    if r == 5:
        "……突然觉得好困……但现在睡过去，是不是就再也没机会醒来了？"
    if r == 6:
        "……血腥味让人难以呼吸，同事们应该被砸死不少吧……但现在还不是最难熬的时候，过段时间应该就会变成腐臭味……"
    if r == 7:
        "活着，为什么要活着……曾经自己不是总向往着用死亡来结束痛苦吗？可为什么现在还坚持着呢？"
    if r == 8:
        if p.route == 'h':
            h"“[p.name]……我好疼……”"
            $ss("dirty no_hat")
            s"“……深呼吸，疼的话……再等一会，就吃药，好吗？”"
            $sh()
            h"“嗯……”"
            "到底什么时候能够结束呢……"
        if p.route == 'a':
            a"“[p.name]……再给我吃一片吧……”"
            $ss("dirty no_hat")
            s"“……深呼吸，马上就吃药，好吗？”"
            $sh()
            a"“嗯……”"
            "到底什么时候能够结束呢……"
    if r == 9:
        if p.route == 'h':
            h"“[p.name]……我好困……”"
            $ss("dirty no_hat scared_eyebrow")
            s"“不能睡……睡着了……一切都结束了……”"
            $sh()
            h"“好……”"
            "到底什么时候能够结束呢……"
        if p.route == 'a':
            a"“[p.name]……好累……”"
            $ss("dirty no_hat scared_eyebrow")
            s"“不能睡……睡着了……一切都结束了……”"
            $sh()
            a"“好……”"
            "到底什么时候能够结束呢……"
    if r == 10:
        if p.route == 'h':
            $ss("dirty no_hat normal2_eyes")
            s"“Halluke，还醒着吗？”"
            $sh()
            h"“[p.name]……”"
            $ss("dirty no_hat")
            s"“坚持下去，如果我们活着出去，我就……”"
            $sh()
            "就怎样呢？也许我没有爱上他，但至少，我不想让他死去。"
            "自己是不是已经习惯有他在身边的感觉了呢？"
            h"“我突然想起……和你一起……吃冰淇淋的时候了……”"
            h"“所以你也……要撑下去……”"
            $ss("dirty no_hat normal_eyes tear")
            s"“……"
            $sh()
            "我只是有点难过，但我说不出来为什么难过。"
            "是想到他的死，还是我的死？"
        if p.route == 'a':
            s"“Acolas，还醒着吗？”"
            $sh()
            a"“[p.name]……”"
            $ss("dirty no_hat")
            s"“坚持下去，如果我们活着出去，我就……”"
            $sh()
            "就怎样呢？也许我没有爱上他，但至少，我不想让他死去。"
            "自己是不是已经习惯有他在身边的感觉了呢？"
            a"“我现在开始怀念起……之前和你在办公室打闹的时候了……”"
            $ss("dirty no_hat normal_eyes tear")
            s"“……"
            $sh()
            "我只是有点难过，但我说不出来为什么难过。"
            "是想到他的死，还是我的死？"
        
    call Task_processing from _call_Task_processing_15
    
    $p.times+=1
    $DespairWaiting.executeTask(p)

label DespairWaiting_result:
    scene ruins with fade
    $Notice.show()
    "闭眼休息了一会，我的疼痛尚可缓解，但他的疼痛只能靠药恢复。"
    "药瓶还在口袋中，还可以再撑一段时间。"
    $p.times+=1
    jump despair_execution


label DespairObserve_beginning:
    scene ruins with fade
    "我该检查一下他的状态。"
    "也许我曾经希望永远都不再见到他，但至少现在，我想让他活下去。"
    call Task_processing from _call_Task_processing_16
    
    $p.times+=1
    $DespairObserve.executeTask(p)

label DespairObserve_result:
    scene ruins with fade
    $Notice.show()
    $r = rd(1, 7)
    if r == 1:
        "虽然[p.p2.name]的血止住了，但他的状态还是不太好的样子。"
    if r == 2:
        "也许我该给他喝点水，他的嘴唇已经干裂出血了。"
    if r == 3:
        "面包……该给他吃吗？他可能快撑不住了？"
    if r == 4:
        "他已经意识不清了。"
    if r == 5:
        "看样子仍然活着，但他似乎并不想说话。"
    if r == 6:
        "他说自己还能撑一会。"
    if r == 7:
        "也许……也许他正痛苦着吧？也许……也许该放弃？……"
    if p.p2:
        $temp = Despair.getstack(p.p2)
        if temp>=4:
            $Despair.get(p.p2).sub(p.p2, int(temp/2))
            $temp = Despair.getstack(p.p2)
        "*[p.p2.name]当前的精神状态为[p.p2.mental]，绝望等级为[temp]*"
        
    else:
        "系统错误！"
    $p.times+=1
    jump despair_execution


label DespairDistribute_beginning:
    scene ruins with fade
    if p.meds() == 1:
        jump lastMed
    "是时候给他吃药了……"
    if p.finalStageDays >= 4:
        "拜托……药一定要管用啊……"
    menu:
        "[MedicineA.name]" if MedicineA.has(p):
            $MedicineA.get(p).sub(p)
            $MedicineA.add(p.p2)
            $MedicineA.get(p.p2).use(p.p2)
            call Task_processing from _call_Task_processing_17
            
            $p.times+=1
            scene ruins with fade
            $Notice.show()
            "用我的马克杯给他倒了一杯水，这样也能给他补充点水分。"
            if p.route == 'h':
                h"“……咕……”"
            if p.route == 'a':
                a"“……咕……”"
                
            "虽然他看上去还是没什么精神，但应该有效吧……"
        "[MedicineB.name]" if MedicineB.has(p):
            $MedicineB.get(p).sub(p)
            $MedicineB.add(p.p2)
            $MedicineB.get(p.p2).use(p.p2)
            call Task_processing from _call_Task_processing_18
            
            $p.times+=1
            scene ruins with fade
            $Notice.show()
            "用我的马克杯给他倒了一杯水，这样也能给他补充点水分。"
            if p.route == 'h':
                h"“……唔……”"
            if p.route == 'a':
                a"“……唔……”"
            "虽然他看上去还是没什么精神，但应该有效吧……"
        "[MedicineC.name]" if MedicineC.has(p):
            $MedicineC.get(p).sub(p)
            $MedicineC.add(p.p2)
            $MedicineC.get(p.p2).use(p.p2)
            call Task_processing from _call_Task_processing_19
            
            $p.times+=1
            scene ruins with fade
            $Notice.show()
            "用我的马克杯给他倒了一杯水，这样也能给他补充点水分。"
            if p.route == 'h':
                h"“……呃嗯……”"
            if p.route == 'a':
                a"“……呃嗯……”"
            "虽然他看上去还是没什么精神，但应该有效吧……"
        "安慰剂" if DrugFake.has(p):
            jump after_drugfake
        "算了。" if any((MedicineA.has(p), MedicineB.has(p), MedicineC.has(p))):
            "不……还是下次吧……他……肯定能坚持下来。"
            $p.times+=1
            pass
        "我已经没有药了。" if not any((MedicineA.has(p), MedicineB.has(p), MedicineC.has(p))):
            "……"
            $p.times+=1
            pass
    
    $DespairDistribute.executeTask(p)

label DespairDistribute_result:
    $Notice.show()
    $p.times+=1
    jump despair_execution

label despairusemed:
    scene ruins with fade
    if p.meds() == 1:
        jump lastMed
    "我……我撑不住了……头……快要炸开了……"
    menu:
        "[MedicineA.name]" if MedicineA.has(p):
            $MedicineA.get(p).use(p)
            "……很快就会好起来的。"

        "[MedicineB.name]" if MedicineB.has(p):
            $MedicineB.get(p).use(p)
            "……很快就会好起来的。"

        "[MedicineC.name]" if MedicineC.has(p):
            $MedicineC.get(p).use(p)
            "……很快就会好起来的。"

        "还可以忍一忍。" if any((MedicineA.has(p), MedicineB.has(p), MedicineC.has(p))):
            "……我……还能撑一会……"

        "我已经没有药了。" if not any((MedicineA.has(p), MedicineB.has(p), MedicineC.has(p))):
            "……"

    jump despair_execution



label after_drugfake:
    play music audio.thelastmedicine fadein 5
    $p.p2.drugfake = True
    "……"
    "这只是合理的药物调节程序。"
    "我提醒着自己。"
    "你并没有做错什么，那些医生也是这样欺骗他们的病人的。"
    "痛苦…痛苦也只是幻觉而已。"
    "他会活着的。"
    "他会活着的，对吗？"
    "保存体力，保存体力。"
    "思考和呼吸都会加速生命的燃烧。"
    "怀疑，思考，惦念，怜悯都是不必要的，没有任何东西比生命重要。"
    "但我却不能停止这些字句从大脑布满褶皱的缝隙中流出，不能关闭回忆的画面在意识中的形成，如同挽留河水般无力。"
    "第一堂课便是生命的教育。"
    "生命是珍贵的，生命是无法再获得的，生命是只有一次的。"
    if p.route == 'h':
        s"“Halluke……你睡着了吗？”"
    elif p.route == 'a':
        s"“Acolas……你睡着了吗？”"
    "我低声。"
    if p.route == 'h':
        h"“…还没。”"
    elif p.route == 'a':
        a"“…还没。”"
    
    "我的生命是宝贵的，我的存在是宝贵的，我…"
    "为了我…"
    "但我赌上了他的性命。"
    "…"
    "饥饿感让精神变得飘渺，我能听到死神的脚步声，似乎就在几米外。"
    "我发誓，我发誓，我再也不会欺骗他了，只有这一次，我祈求上天，让他活过今晚…"
    if p.route == 'h':
        s"“Halluke……你还醒着吗？”"
    elif p.route == 'a':
        s"“Acolas……你还醒着吗？”"
    "我低声。"
    if p.route == 'h':
        h"“…嗯。”"
    elif p.route == 'a':
        a"“…嗯。”"
    "我的呼吸紊乱了，也许一直都是紊乱的。"
    if p.route == 'h':
        s"“Halluke，求你，答应我。”"
    elif p.route == 'a':
        s"“Acolas，求你，答应我。”"
    s"“活过今晚就好……真的，明早就会有人救我们了。”"
    if p.route == 'h':
        h"“…”"
        h"“我答应你……”"
    elif p.route == 'a':
        a"“…”"
        a"“……会的。”"
    
    "他的声音如此轻微。"
    "也许我不该继续打扰他了。"
    "不会这么巧的，不会这么巧。"
    "他已经坚持了很久了，不是吗。"
    "现在我能把剩下的药给他吃吗？"
    "不…我不能…药太少了…如果……"
    "如果我再努力一点，如果我买多一点药，如果…"
    "那他就不会…我们就不会是这样的场面…"
    "为什么…为什么事情会变成这样…"
    "我想哭，但我不能流泪。"
    "水，能量。"
    "我们就像芦苇。"
    if p.route == 'h':
        h"“[p.name]？”"
    elif p.route == 'a':
        a"“[p.name]？”"
    
    s"“我……我还醒着……怎么了……”"
    "黑暗，潮湿，寂静。"
    "我分辨不出现在到底是什么时候。"
    "但我很困，我不确定，我到底是困了，还是大限将至。"
    "我能睡吗？"
    if p.route == 'h':
        s"“Halluke？”"
        h"“……”"
        s"“Halluke！”"
    elif p.route == 'a':
        s"“Acolas？”"
        a"“……”"
        s"“Acolas！”"
    "…"
    "没有回应。"
    "…"
    jump despair_dayend

screen lastmedchoice():
    default t2 = glitchtext(rd(20, 40))
    default t3 = glitchtext(rd(20, 40))
    style_prefix "choice"

    vbox:
        button:
            action Jump('lastMed_to')
            text t2 xalign 0.5
            hovered SetLocalVariable('t2', '留给对方')
            unhovered SetLocalVariable('t2', glitchtext(rd(20, 40)))
            
                
        button:
            action Jump('lastMed_me')
            text t3 xalign 0.5
            hovered SetLocalVariable('t3', '留给自己')
            unhovered SetLocalVariable('t3', glitchtext(rd(20, 40)))
        
    window:
        text '你的手中紧握着最后一粒药。' xpos 402 ypos 75
    use quickmenu(p)



label lastMed:
    #stop music fadeout 5
    "这一刻还是到来了，不得不面对，没法逃避。"
    "小时候每次坐长途汽车的时候，坐得烦了就会想，我躺在地上撒泼，求助家长，说我放弃了我忍受不住了，我就可以瞬间回到家里，不用受苦。"
    "多有趣的想法。"
    "不过我现在却一直都没有那种想法，甚至我连后悔也没有。"
    "假如我今天请假了，难道我就不会受到这样的痛苦了吗？"
    "情况会更糟也说不定，至少我现在还活着，而另一个在家里的平行世界的我已经被天花板压成酱了。"
    "只能往前走，不能后退，不能退出，不能求饶。"
    "即便面对的是无声的终结。"
    "也许，也许马上，我就能听到救援的声音了，马上，马上就会有光线透过缝隙，像水穿过缝隙流进来，这样我就可以不用做选择了。"
    "但没有。"
    "一些都和几天前没有区别。"
    "不，有区别，至少我曾经还能听见呼救声，说话声，哀嚎声，哭泣声，硬物敲击铁管的声音，呼吸声。"
    "最后呼吸声也没有了，除了我眼前的人。"
    "…我眼前的人。"
    "他，已经不是以前的他的模样了。"
    "就像被钉在十字架上，就像一座沉默的雕塑。"
    "我看着手中的仅剩一粒的药。"
    "我应该留给他吗？…把活下去的希望交给正常人，而不是一个头疼的病治了几年都没有治好的废物？"
    "不，他被钢筋捅穿了，即便他坚持到了现在，但谁能保证他不会随时死掉？就算他活下来了，肯定也会变成残疾…变得…不正常？"
    play music audio.thelastmedicine
    show screen freeze(5)
    "{cps=1}和我一样？{/cps}"
    if renpy.variant("pc"):
        call screen lastmedchoice
    else:
        menu:
            "你的手中紧握着最后一粒药。"
            "留给对方。":
                jump lastMed_to
            "留给对方。":
                jump lastMed_to
            "留给自己。":
                jump lastMed_me
            "留给对方。":
                jump lastMed_to
            "留给自己。":
                jump lastMed_me
            "留给自己。":
                jump lastMed_me
            "留给自己。":
                jump lastMed_me
            "留给对方。":
                jump lastMed_to

label lastMed_to:
    "……"
    $ss("dirty no_hat")
    s"“嘿。”"
    $sh()
    "我听到了，十分勉强地，他的呼吸声比以前大了一点，以此来回应我的呼唤。"
    $ss("dirty no_hat normal2_eyes sad_eyebrow")
    s"“张开嘴……来吃药吧。”"
    $sh()
    "我突然意识到，这种奇妙的反差。"
    "曾经我对于他这种正常人来说是虚弱的，痛苦的，必须靠吃药和精打细算地使用自己的大脑。"
    "但现在，情况似乎反过来了。"
    "我可以说话，因为我至少还能比较放肆地滥用仅剩的能量，但他却只能用呼吸的力度回应我。"
    if p.route == 'h':


        h"“[p.name]…”"
        "我突然听到他的声音。"
        "我很久没听到他叫我了。"
        $ss("dirty no_hat normal_eyes sad_eyebrow")
        s"“嗯？…不要说话了，这样会消耗能量的。”"
        $sh()
        h"“…[p.name]。”"
        "我蠕动身体，和往常一样，用饮水机，往纸杯里滴水。"
        h"“不要。”"
        $ss("dirty no_hat normal2_eyes scared_eyebrow")
        s"“什么？”"
        $sh()
        h"“我…我不需要。”"
        $ss("dirty no_hat normal2_eyes sad_eyebrow")
        s"“…”"
        $sh()
        h"“…之前的你，在给我吃药之前……”"
        h"“不会那么…犹豫…”"
        h"“我知道…已经…只剩…最后一粒了吧？”"
        "我沉默。"
        h"“果然……我还是想活下去啊……抱歉……”"
        h"“但是……想和你……一起……”"
        h"“我到现在还有意识……多谢了你……”"
        h"“所以……我肯定……也能撑下去……”"
        h"“我们…一人…一半。”"
        h"“这样…你也有机会…活下去……！”"
        "一人一半…吗…"
        $ss("dirty no_hat sad_eyebrow sad_eyes")
        s"“…”"
        $sh()
        h"“和你在一起的时光…是我活着最珍贵的记忆。”"
        h"“一直被家里人…控制的我，第一次有人愿意…听我说话…尊重我的想法…”"
        h"“也许我后来…对你造成困扰了吧…”"
        h"“抱歉…我太喜欢你了…没有想过你…也需要喘口气的时间…”"
        h"“如果我们…能活下来的话…我发誓…我会慢慢来的…”"
        h"“我其实…知道的…那个时候…你对我没有之前…那么…兴奋了…”"
        h"“肯定也…有点反感我了…我不怪你…是我自己的原因…”"
        h"“但你…还是把…药…分给我…”"
        h"“…啊…好想和你…再打一次羽毛球啊…”"
        h"“我们一定会…活下来的…肯定会的…”"
        $ss("dirty no_hat sad_eyebrow tear sad_mouth")
        s"“…”"
        $sh()
        "我沉默。"
        "我只是沉默。"
        "液体从我眼角流溢，但即便是泪水，在废墟之下也是绝对宝贵的。"
        "但我宁愿让它流淌，让它挥霍。"
        $ss("dirty no_hat sad_eyebrow closed_eyes tear")
        s"“Halluke…”"
        $ss("dirty no_hat sad_eyebrow normal_eyes tear")
        s"“求你了…不要死啊……”"
        $sh()
        "我把药掰开，将另一半塞进了他的口中。"
        "……"
        jump despair_end
    
    if p.route == 'a':
        a"“[p.name]…”"
        "我突然听到他的声音。"
        "我很久没听到他叫我了。"
        $ss("dirty no_hat normal_eyes sad_eyebrow")
        s"“嗯？…不要说话了，这样会消耗能量的。”"
        $sh()
        a"“…[p.name]。”"
        "我蠕动身体，和往常一样，用饮水机，往纸杯里滴水。"
        a"“不要。”"
        $ss("dirty no_hat normal2_eyes scared_eyebrow")
        s"“什么？”"
        $sh()
        a"“我…我不需要。”"
        $ss("dirty no_hat normal2_eyes sad_eyebrow")
        s"“…”"
        $sh()
        a"“…之前的你，在给我吃药之前…”"
        a"“不会那么…犹豫吧…”"
        a"“我知道…已经…只剩…最后一粒了吧？”"
        "我沉默。"
        a"“说真的……我…已经…没法坚持下去了…”"
        a"“我…我放弃了…”"
        a"“对不起，[p.name]…但我……”"
        a"“这不是…吃不吃药的问题…我…我感觉自己…应该…挺不过…今晚了…”"
        a"“其实我……早就该死了……但你还是努力……让我……撑到现在”"
        a"“…一开始……就不该让你为我吃药的……我没想到……这么久……我们还没获救……”"
        a"“能认识你…我很开心…”"
        a"“抱歉……”"
        a"“我……之前…犯了很多错…”"
        a"“我要求你太多…我对你太刻薄…我不该那么说你…”"
        a"“我…我…我很怀念…和你做游戏的时候…”"
        a"“对不起…我们下辈子…再一起做游戏吧？…我发誓…我不会…那样对你了…好不好？”"
        $ss("dirty no_hat sad_eyebrow tear sad_mouth")
        s"“…”"
        $sh()
        "我沉默。"
        "我只是沉默。"
        "液体从我眼角流溢，但即便是泪水，在废墟之下也是绝对宝贵的。"
        "但我宁愿让它流淌，让它挥霍。"
        $ss("dirty no_hat sad_eyebrow closed_eyes tear")
        s"“Acolas…”"
        $ss("dirty no_hat sad_eyebrow normal_eyes tear sad_mouth")
        s"“求你了…不要死啊……”"
        $sh()
        "我把药掰开，将另一半塞进了他的口中。"
        "……"
        jump despair_end

label lastMed_me:
    stop music
    "……"
    "我深呼吸。"
    "是啊，我早该清楚地意识到，对方已经无力回天了，即便我给他吃药，也只是杯水车薪罢了。"
    "…"
    "我蠕动身体，和往常一样，用饮水机，往纸杯里滴水。"
    "然后将最后一粒药，用食指推进自己的口里。"
    "…"
    jump despair_end


label despair_end:
    stop music fadeout 5
    $clearscreens()
    scene black
    call screen cfreeze(5)
    pause
    scene black with fade
    if p.finalStageDays >= 20:
        $Achievement602.achieve()
        $Achievement.show()
    if p.finalStageDays >= 7 or p.p2.drugfake:
        "……"
        "是震动。"
        scene white with dissolve
        "光。"
        "是光。"
        "是声音。"
        "我分不清了。"
        "我应该是被人救起来了。"
        "被拉拽，被搀扶，被抱起。"
        "液体。"
        "冰冷的液体。"
        "顶着我的嘴。"
        "我吮吸着水。"
        "周围是嘈杂的声音。"
        "我分辨不出。"
        "我的意识快要消散了。"
        "我的大脑已经无法忍耐这种极端的痛苦了。"
        "不，还不能走。"
        "我发出声音，"
        "我努力发出声音。"
        "低语，呻吟，模糊不清的声音。"
        "我要说话，我要喊出来。"
        "我做不到。"
        "我睁眼。"
        "灰暗的色彩流入我的虹膜。"
        if p.p2.drugfake:
            "我获救了。"
            "但我……我很累……"
            "好想休息……"
            "好想……永远地……沉睡下去……"
            "……"
            scene black with dissolve
            call screen cfreeze(5)
            if p.route == 'h':
                jump fe_h
            elif p.route == 'a':
                jump fe_a
            else:
                "出现错误。"
                return
        "我用手指向刚刚的位置。"
        "我看到了。"
        "他们也看到了。"
        "他们试图移动他，但他们才发现他身上插着建筑的钢筋。"
        "他们试图唤醒他。"
        "我看到他蹲下去了。"
        "我看到他触碰他，用水瓶倒水在他嘴边。"
        "我看到他摇头。"
        "我被带走了。"
        "我被带走了。"
        "只有我。"
        "只有我。"
        "只有…"
        "我。"
        "……"
        scene black with dissolve
        call screen cfreeze(5)
        if Sticker59.has(p):
            jump te
        else:
            jump ne
    jump despairBE

