label pathos_route_0:
    $start_plot()
    scene consulting_room with fade
    play music audio.solitus
    show pathos at trans_toRight()
    pathos"“很高兴你还能来到我的诊疗室。”"
    show pathos smile_mouth
    if p.times==4:
        pathos"“上午好，[p.name]先生。”"
        pathos"“今天没有工作吗？还是头太痛了所以请假来到这里的？”"
        $ss('smile_eyes')
        s"“你说得对。那什么，Pasos医生。”"
    elif p.times==8:
        pathos"“下午好啊，[p.name]先生。”"
        pathos"“下班这么早？还是头太痛了所以请假来到这里的？”"
        $ss('smile_eyes')
        s"“你说得对。那什么，Pasos医生。”"
    else:
        pathos"“[p.name]先生。”"
        pathos"“你来得太晚了，我还有一个小时就下班了。”"
        $ss('smile_eyes smile_mouth')
        s"“来得早不如来得巧。”"
        $ss('normal_mouth')
        s"“晚上好。那什么，Pasos医生。”"
    $sh()
    show pathos angry_eyebrow angry_mouth angry_eyes anger
    with dissolve
    pathos"“我的名字是Pathos，希望你记清楚，我们还要在一起相处很长一段时间。”"
    show pathos angry_eyebrow normal_mouth angry_eyes anger
    with dissolve
    pathos"“不管你喜不喜欢我，我都会是你的主治医师，至少在你病好或者死在家里之前都是。”"
    $ss('scared_eyes scared_eyebrow sweat')
    s"“现在的医生说话都这个样子的么……”"
    $sh()
    show pathos surprised_eyebrow normal_mouth surprised_eyes no_anger
    with dissolve
    pathos"“咳咳，回归正题。”"
    show pathos normal_eyebrow saying normal_eyes
    with dissolve
    pathos"“和之前一样，你的病情仍然在恶化，但出现了一点点小小的转机。”"
    pathos"“恶化的速度稍微变慢了一些，这可能是你个人生活节奏的改变导致的。”"
    show pathos surprised_eyebrow surprised_eyes
    with dissolve
    pathos"“无论你做了什么，继续保持，也许，只是也许，你的病状会因此转好。”"
    show pathos normal_eyebrow normal_mouth normal_eyes
    with dissolve
    "……"
    "我从没想过自己的病如果真的可以治好的话，那样我的生活会变成什么模样。"
    "但他说的话真的能够相信吗？"
    "还是说，仅仅只是一个医生用语言习惯性地对病人投喂廉价的安慰剂呢？"
    "无论如何，我也许应该为此开心吧。"
   
    show pathos normal_mouth angry_eyebrow angry_eyes
    with dissolve
    pathos"“还有一件事。”"
    "我抬头看他。"
    show pathos saying
    with dissolve
    pathos"“你现在在吃的药，也就是Alpha药，你应该已经对它形成了很强的抗药性了吧。”"
    pathos"“作为你的主治医师，我决定让你使用另一种药。”"
    show pathos surprised_eyebrow surprised_eyes
    with dissolve
    pathos"“Beta药，这种药在你头疼到飞起的时候用效果会更好，而不是太疼的情况下，效果就比较一般。”"
    pathos"“不过最重要的是，你对这种新药没有抗药性。”"
    show pathos normal_eyebrow normal_eyes
    with dissolve
    pathos"“顺便也能作为实验对象为我们的药物研发提供宝贵的数据……”"
    $ss('angry_eyes scared_eyebrow sweat mood')
    s"“……我是小白鼠吗？”"
    $sh()
    show pathos surprised_eyebrow surprised_eyes angry_mouth
    with dissolve
    pathos"“毕竟你的病难得一见，而且大多数得了你这样病的人都已经……那个了……”"
    "他突然笑的很渗人……"
    show pathos normal_eyebrow normal_eyes smile_mouth
    with dissolve
    pathos"“你很幸运，你应该清楚这件事。”"
    pathos"“所以，尽量活下去吧。”"
    "狮子起身，我因他的动作而将目光定位于他鼻梁上的眼镜。"
    "他伸出手来……"
    "呃……他刚刚是在搓我的头吗？"
    "天……为什么突然这么煽情。"
    $ss('surprised_eyes scared_eyebrow surprised_mouth sweat blush mood')
    s"“……等下，别这样……太亲密了……”"
    $ss('normal_eyes')
    s"“我可不想和我的主治医师有什么关系……”"
    $sh()
    "他也许……似乎并没有大我多少，做男朋友大概…也不是…不可以…"
    show pathos surprised_eyebrow surprised_eyes smile_mouth blush
    with dissolve
    pathos"“哈哈哈，你明明不像表面上那么难接触啊。”"
    pathos"“那么，接下来，你再去药房的时候，就可以买到Beta药了。”"
    pathos"“无论是使用哪种药，决定权在你，因为我尚不明晰你使用药物时的具体感受，我也要依靠你的更换药物时间段来完成我的博士生论文……”"

    "看来我真要永远做他的小白鼠了……"
    stop music fadeout 4
    if p.sol_p == 0:
        $p.sol_p = 1
    $end_plot()
    if replaying:
        jump afterreplay
    $showNotice(['已解锁新药物！{color=#7881e8}药物{font=arial.ttf}β{/font}{/color}！','可以在医院二楼的药房购买到该药物！'])
    play sound audio.getmedicine
    scene elevator with fade
    jump explore_elevator


label pathos_route_1:
    $start_plot()
    scene consulting_room with fade
    play music audio.solitus
    show pathos at trans_toRight()
    pathos"“又是你啊。”"
    show pathos smile_mouth
    with dissolve
    if p.times==4:
        pathos"“窗户是打开的，多呼吸几口清晨的新鲜空气，怎么样？[p.name]先生。”"
    elif p.times==8:
        pathos"“你看外面的夕阳吧，[p.name]先生。”"
    else:
        pathos"“今晚夜色多美啊，[p.name]先生。”"
    $ss('awkward_eyes sweat')
    s"“？”"
    $sh()
    pathos"“言归正传。”"
    show pathos awkward_eyebrow awkward_eyes awkward_mouth
    with dissolve
    pathos"“其实我很意外，当时在诊断你这样的病情时，我个人的预计是完全活不到两个月。”"
    show pathos awkward_eyebrow normal_eyes awkward_mouth
    with dissolve
    pathos"“而现在已经是第三个月了！”"
    pathos"“我拿到了你的体检报告和一些其他的数据，发现你的情况甚至要比上个月还要好。”"
    show pathos smile_mouth
    with dissolve
    pathos"“你看上去比我第一次见到你的时候强壮多了。”"
    "我能看到他的眼神正上下打量着我。"
    pathos"“多锻炼就是有好处，我没说错吧？”"
    show pathos normal_eyebrow normal_eyes normal_mouth
    with dissolve
    pathos"“总之，关于你的病，已经成为这几家医院亟待解决的共同难题之一。”"
    $ss('angry_eyes sad_eyebrow sad_mouth sweat mood')
    s"“意思是说之前都没把我放在眼里咯。”"
    $sh()
    show pathos surprised_eyebrow surprised_eyes surprised_mouth
    with dissolve
    pathos"“咳咳，也不是这个意思，但毕竟研究进度还是很慢的……”"
    pathos"“如果没有什么突破性进展，也不会特意来找你。”"
    $ss('scared_eyes scared_eyebrow')
    s"“所以？”"
    $sh()
    show pathos normal_eyebrow normal_eyes normal_mouth
    with dissolve
    pathos"“是的，我们打算再过一阵子，大概第15周的时候，计划为你做手术。”"
    pathos"“费用并不高，只有几十万块的样子。”"
    $ss('mood')
    s"“这还叫不高……”"
    $sh()
    show pathos angry_eyebrow angry_eyes angry_mouth
    with dissolve
    pathos"“相对于其他的手术不高了。”"
    show pathos normal_mouth
    with dissolve
    pathos"“在这次手术之后，应该还有几次手术，间隔大概都是一个月左右，这段时间好好休息，多赚钱。”"
    show pathos normal_eyebrow normal_eyes smile_mouth
    with dissolve
    pathos"“别死掉了。”"
    $ss('smile_eyebrow smile_eyes smile_mouth')
    s"“我就当你在安慰我好了……我哪里付得起这么多钱啊……”"
    $ss('normal2_eyebrow normal2_eyes normal2_mouth')
    s"“那么，还有什么其他事情吗？”"
    $sh()
    show pathos normal_mouth
    with dissolve
    pathos"“当然。”"
    show pathos surprised_eyebrow surprised_eyes saying
    with dissolve
    pathos"“估计你对现在在吃的beta药的抗药性也很强了。”"
    pathos"“最新研发出的gamma药也终于通过上面的审核了，你可以在药房里购买了。”"
    show pathos normal_eyebrow normal_eyes saying
    with dissolve
    pathos"“大量测试表明这三种药物都是可以一起吃的，但还是得尽量隔开着吃。”"
    $ss()
    s"“…怎样都行，只要能活下去就行。”"
    $ss('mood')
    s"“已经完全是药罐子了呢。”"
    $sh()
    show pathos awkward_eyebrow normal_eyes smile_mouth
    with dissolve
    pathos"“……你第一次来这里的时候，完全是一副颓废的，混吃等死的样子。”"
    show pathos awkward_eyebrow surprised_eyes smile_mouth
    with dissolve
    pathos"“……你变了好多。”"
    $ss()
    s"“……”"
    $ss('normal2_eyes')
    s"“人总会变的。”"
    $sh()
    pathos"“好，祝你好运。”"
    $ss('normal2_eyebrow normal2_eyes normal2_mouth')
    s"“嗯。”"
    $ss('smile_eyebrow smile_eyes smile_mouth')
    s"“谢谢你，Pathos医生。”"
    $sh()
    show pathos blush
    with dissolve
    pathos"“嘛……这孩子还是挺可爱的……”"
    stop music fadeout 4
    if p.sol_p == 2:
        $ p.sol_p = 3
    if replaying:
        jump afterreplay
    $showNotice(['已解锁新药物！{color=#e4f06f}药物{font=arial.ttf}γ{/font}{/color}！','可以在医院二楼的药房购买到该药物！'])
    play sound audio.getmedicine
    $end_plot()
    scene elevator with fade
    jump explore_elevator


label pathos_route_2:
    $start_plot()
    scene consulting_room with fade
    play music audio.solitus
    show pathos smile_mouth at trans_toRight()
    pathos"“你来了。”"
    $ss('agony_eyebrow normal2_eyes')
    s"“不欢迎？”"
    $sh()
    "我靠近他的桌子，在桌前熟悉的位置坐下。"
    "虽然说熟悉，但其实我也没来过几次，但一想到我第一次来的时候，距离现在已经过去了半年，就觉得有点不可思议。"
    "…Pathos医生，是我在半年前第一次来到这个医院检查头疼时认识的。"
    "虽然在很久以前，家里人就带着年幼的我奔走各大医院，但都没有结果。"
    "年老的专家对我的病都没什么头绪，他一个还在读博士的家伙能有什么高见？"
    "当时他说对我的头疼很感兴趣，同时他现在也是主要研究一些世上不多见的头疼病，所以见到我就像看到蜜糖的蚂蚁。"
    "因为痛苦，对活着都没什么想法的我也就同意了他的研究。"
    "虽然在刚开始的三个月里，他几乎没什么进度，可能也和我不太来找他的原因有关。"
    "不过四月中旬的时候他突然和我打电话说有急事，让我去医院。"
    "那么在来到医院之后，我也就获得了他所谓的α药。"
    "药的效果其实还行，但我总觉得我这么年轻就要靠药物维持生命的话，还不如死了算了。"
    "…"
    "四月末，Pathos医生再次招呼我来到医院，那段时间我几乎满脑子都是抑郁的情绪，看什么都不顺眼。"
    "明明当时要来医院就是要打算自杀的，顺便看看这个所谓的主治医生想说些什么。"
    "…"
    "我放弃了计划，直到现在。"
    "我的身体改善了很多，写作也略有小成，有了不少粉丝，工作能力也变得出彩，一再升职加薪…"
    "头疼虽然还是像家门前的小河一样，稍不留神就可能会被打湿裤腿，但也和最初那段时间带给我的痛苦不同了。"
    "我坚持到了现在，我活下来了。"
    "Pathos医生，我没有辜负你对我的期望，没错吧？"
    show pathos awkward_eyebrow awkward_eyes
    with dissolve
    pathos"“当然没有，我也要祝贺你，一直坚持到了现在。”"
    show pathos angry_eyebrow angry_eyes
    with dissolve
    pathos"“关于你的病情研究有了极大的进步，相信再过几周就可以准备手术了。”"
    show pathos surprised_eyebrow angry_eyes angry_mouth
    with dissolve
    pathos"“关于手术费…希望你也不用过于担心，我已经向医院申请了，如果成功的话可能会免除大部分费用。”"
    $ss('smile_mouth normal2_eyes')
    s"“真的？”"
    $sh()
    show pathos awkward_eyebrow awkward_eyes awkward_mouth
    with dissolve
    pathos"“是啊，不过你还是得攒一些钱的，毕竟手术不一定具体是哪天可以，可能过两周，可能过两月，甚至过两年？”"
    $ss('scared_eyebrow scared_mouth scared_eyes')
    s"“啊？”"
    $sh()
    show pathos awkward_eyebrow surprised_eyes smile_mouth
    with dissolve
    pathos"“开个玩笑，不会那么久的。”"
    show pathos awkward_eyebrow awkward_eyes smile_mouth
    with dissolve
    pathos"“总之在这段时间里，你就继续你之前的生活方式就行，饮食清淡，注意安全。”"
    $ss()
    s"“哦。”"
    $sh()
    show pathos normal_eyebrow normal_eyes smile_mouth
    with dissolve
    pathos"“除此之外，手术之后你有什么打算吗？”"
    "手术之后的打算啊…"
    "如果手术真的能把我的头疼完全抹除，我和现在又会有什么不同呢？"
    "这片钢铁丛林已经将我塑造成了千人一面的模样，等我不再头疼，所做之事不也只是普通人，也就是之前的我会做的事吗…"
    $ss('normal2_eyes')
    s"“…没什么打算，就那样活着吧。”"
    $sh()
    show pathos normal_eyebrow normal_eyes saying
    with dissolve
    pathos"“好吧，不想和我说也没关系，不过你得清楚，手术也不能瞬间让你变成正常人。”"
    pathos"“你可能需要经历多次手术，甚至手术之后还得再修养很久等等。”"
    show pathos awkward_eyebrow awkward_eyes saying
    with dissolve
    pathos"“因为我们还没有完全清楚你的疾病，我们也无法确定后果……总之…”"
    stop music
    $ss('agony_eyebrow normal2_eyes')
    s"“这是不是代表…手术成功率不高？…”"
    $sh()
    show pathos surprised_eyebrow surprised_eyes surprised_mouth
    with dissolve
    "我打断他，但我为什么会说出这种话？前段时间我还满怀自尽的想法，怎么会怕小小的手术失败？"
    "眼前的狮子因为被我打断也有些惊住，转而变得严肃起来。"
    show pathos normal_eyebrow normal_eyes normal_mouth
    with dissolve
    pathos"“没错，手术确实有风险，但你也一定会同意的吧？”"
    pathos"“正好，这次来也是要签署手术知情书。”"
    play sound audio.itempaper
    "Pathos从他的抽屉中抽出那张知情书，放在我的面前，最下方写着“患者在此签名：”。"
    "他怎么会如此坚定我会同意？"
    $ss()
    s"“我…”"
    $sh()
    menu:
        "同意手术":
            pass
        "不同意手术":
            jump pathos_route_2_1
    play music audio.smellsofdisinfectant
    $ss('scared_eyebrow normal2_eyes')
    s"“我…同意手术…”"
    "我拿起笔，在知情书的底端签上了我的名字。"
    $sh()
    show pathos normal_eyebrow normal_eyes smile_mouth
    with dissolve
    pathos"“换做是我也会同意的。”"
    show pathos awkward_eyebrow awkward_eyes smile_mouth
    with dissolve
    pathos"“等到手术有消息了，我会给你打电话的。”"
    $ss('scared_eyebrow')
    s"“…明白了。”"
    $sh()
    scene elevator with fade
    "有些奇怪，但我说不出来哪里奇怪。"
    "我总是有种不好的预感…"
    "但我能为此做些什么呢？"
    "如果我不手术，我还能怎样呢？"
    if p.sol_p == 4:
        $ p.sol_p = 5
    $end_plot()
    if replaying:
        jump afterreplay
    
    jump explore_elevator


label pathos_route_2_1:
    $clearscreens()
    play music audio.beep
    $_confirm_quit = False
    $_game_menu_screen = None
    $ _skipping = False
    scene white with None
    show pathos ghost none_eyebrow none_eyes none_mouth no_glasses no_sco
    $pause()
    play sound audio.noise
    show pathos at jumpscare_p
    pause 0.35
    $renpy.quit()
