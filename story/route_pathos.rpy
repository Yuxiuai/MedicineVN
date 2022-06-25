label pathos_route_0:
    $rollback_switch()
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
    $rollback_switch()
    if replaying:
        jump afterreplay
    $showNotify(['已解锁新药物！{color=#7881e8}药物{font=arial.ttf}β{/font}{/color}！','可以在医院二楼的药房购买到该药物！'])
    play sound audio.getmedicine
    scene elevator with fade
    jump explore_elevator


label pathos_route_1:
    $rollback_switch()
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
    pathos"“费用并不高，只有几千元。”"
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
    s"“我就当你在安慰我好了……”"
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
    $showNotify(['已解锁新药物！{color=#e4f06f}药物{font=arial.ttf}γ{/font}{/color}！','可以在医院二楼的药房购买到该药物！'])
    play sound audio.getmedicine
    $rollback_switch()
    scene elevator with fade
    jump explore_elevator