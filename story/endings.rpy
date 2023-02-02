label ending0:
    $start_plot()
    scene hospital_corridor with dissolve
    play music audio.impendingdeath
    "是啊。"
    "我已经厌倦了每天吃药了。"
    "这种生活就是完全的折磨。"
    scene elevator with fade
    menu:
        "7楼：天台":
            pass
    scene rooftop with fade
    "所以呢？这就是我的人生？"
    "我深呼吸。"
    "令人意外的是这座医院的天台居然这么容易就可以走楼梯上来。"
    "周边空无一人，不过毕竟这个地方平时怎么会有人呢？"
    "天台的风将我的毛发吹起。"
    "我的痛苦却永无止境，但此刻我就可以解脱了。"
    "所以我就要死了，就要失去对这具身体的掌控权了。"
    "我会觉得可惜吗？"
    "……"
    "去他妈的，这破烂身体，这操蛋的头疼，凭什么我生来就要遭受这样的痛苦。"
    "生在了科技发达的现代，又被告知没有办法治愈。"
    "为什么？为什么我要比别人痛苦啊！"
    "为什么我来到这个世界就要被这样对待啊？"
    "为什么……为什么……"
    "……"
    "我离开了天台。"
    scene falling with dissolve    
    "我喜欢这种被引力完全掌控身体的感觉，我的身躯正在向下坠落。"
    "有那么一瞬间，从头部传来的痛苦消失了。"
    "啊……"
    "是的，这种感觉……太棒{nw}"
    scene black
    play sound audio.suicide
    show screen freeze(5)
    pause
    $Achievement100.achieve()
    $Achievement.show()
    $Notice.show()
    "{color=#FF0000}Bad Ending 0.\n——愿令人怀念的新生的你，能有一个好的结局。{/color}" 
    $end_plot()
    if replaying:
        jump afterreplay
    return

label ending1:
    $start_plot()
    play music audio.impendingdeath
    scene bedroom with dissolve
    "是啊。"
    "我已经厌倦了每天起早吃药了。"
    "这种生活就是完全的折磨。"
    "我放下手中的药瓶，望向出租房的落地窗。"
    scene suicide
    "微亮的天空将星光和晨曦倒进屋内。"
    "深呼吸。"
    "是的，这个世界真的很美，不是吗？"
    "但是她带给我的恶意实在太大了，我已经无法承受这些了。"
    "小时候的自己的形象突然浮现于脑海中，还有在餐桌旁聊天的父母，一起吃着精致的饭菜。"
    "现在他们都不在我身边了，而现在的我也只能在这小小的出租屋里独活。"
    "生命和死亡的意义已经不重要了，重要的是，我真的已经受够了。"
    "大脑深处开始浮现某种熟悉的痛苦。"
    "像被切开头骨，用带刺的木棍反复打击大脑。"
    "……"
    "即便是这种疼痛，我也能轻而易举地忍受住了啊。"
    "不过我最好快点动身。"
    "我走下床，打开窗户。"
    "还未迎来黎明的空气是如此冰冷。"
    "但黎明总会到来，我的痛苦却永无止境，不是吗？"
    "我踩着窗台，从窗口伸出头来。"
    "是的，钢铁丛林。"
    "22层，相当于多高的树呢？"
    "不过这都不重要了。"
    "一切都不重要了。"
    "我深呼吸，然后爬出窗口。"
    "大概是冷风的原因，头疼似乎正在逐渐缓解。"
    $ss("naked no_hat smile_mouth")
    s"“现在我离这个世界更近了。”"
    $sh()
    "所以我就要死了，就要失去对这具身体的掌控权了。"
    "我会觉得可惜吗？"
    "……"
    "去他妈的，这破烂身体，这操蛋的头疼，凭什么我生来就要遭受这样的痛苦。"
    "生在了科技发达的现代，又被告知没有办法治愈。"
    "为什么？为什么我要比别人痛苦啊！"
    "为什么我来到这个世界就要被这样对待啊？"
    "为什么……为什么……"
    "……"
    "我离开了平台。"
    "我喜欢这种被引力完全掌控身体的感觉，我的身躯正在向下坠落。"
    "有那么一瞬间，从头部传来的痛苦消失了。"
    "啊……"
    "是的，这种感觉……太棒{nw}"
    scene black
    play sound audio.suicide
    show screen freeze(5)
    pause
    $Achievement101.achieve()
    $Achievement.show()
    $Notice.show()
    "{color=#FF0000}Bad Ending 1.\n——死亡是最好的解药。{/color}" 
    $end_plot()
    if replaying:
        jump afterreplay
    return


label ending2:
    $start_plot()
    stop music
    scene bedroom with dissolve
    "我把手伸向闹钟边的药瓶。"
    "当爪子握住塑料瓶身时，某种奇怪的感觉从爪心传递至大脑。"
    "怎么回事。"
    "怎么，怎么会如此地轻，为什么握在手里的时候没有发出熟悉的药片互相碰撞的响声。"
    "甚至，甚至连一粒都不剩了吗？"
    play music audio.impendingdeath
    "汗液迅速分泌，紧迫感让困意瞬间全无。"
    "某种恐惧感突然缠绕整个身躯。"
    "大脑深处开始浮现某种熟悉的痛苦。"
    "像被切开头骨，用带刺的木棍反复打击大脑。"
    "而我却已经没有任何手段回应这种从小至大折磨我的痛苦。"
    "不，不不不不不…"
    "为什么，为什么会这样…"
    "……"
    "冷静，冷静。"
    "怎么可能吃完了，怎么可能。"
    "昨天就没有了吗？还是我吃药的时候不小心弄丢了…"
    "不对，这…我……"
    "我还可以买，买一点…"
    "现在是周几？……"
    "不，没有意义了，就算是周五，现在的我要想爬起床，抱着随时都会昏迷的危险出门也是不可能的。"
    "不…不该是这样的…我…"
    "大脑内核传来的痛苦愈发扩大，像生了千万只蛆虫在内部啃咬。"
    "不不不不不不不不不不不不不不不不不不不不…"
    "啊……啊啊啊………！"
    "痛苦越来越强大，逐渐蔓延全身。"
    "…"
    "不…不行…我还有要做的事…"
    "坚持，就坚持一小会…坚持到医院急诊…"
    "我抓起手机，突然意识到自己的手正在发抖。"
    "和死亡擦肩而过的感觉并不好，但我已经习惯了那种恐惧。"
    "可当它真真切切贴近时，这种熟悉感便如同巨兽将整个精神吞噬。"
    "我拿起手机。点开紧急拨号。"
    "颤抖的手指已经不听使唤，强忍住想要撕裂大脑的痛苦拨下急救电话。"
    "…"
    $_skipping=False
    "“这里是急救中心。”"
    "“请问你的位…{nw}”"
    play music audio.interruption
    scene black
    play sound audio.drop
    show screen freeze(5)
    stop music fadeout 10
    pause
    $Achievement102.achieve()
    $Achievement.show()
    $Notice.show()
    "{color=#FF0000}Bad Ending 2.\n——你失去了活着的权利。{/color}"
    $end_plot()
    $_skipping=True
    if replaying:
        jump afterreplay
    return

label ne:
    $start_plot()
    stop music
    scene black
    pause
    play music audio.afterdesperation fadein 5.0

    "…"
    "距离那场事故，已经过去一年多了。"
    "那场特大地震摧毁了整个A市，但她的人民们也在努力重建她。"
    "即便医院没有为所有伤员收费，我还是开心不起来。"
    "我在病榻上醒来那天，正是深夜。"
    "我的目光透过病房的巨大玻璃窗正对着天空的群星，无可自拔地哭了起来。"
    "一切都结束了，我又重新回到孤独了。"
    "很多人失去了亲人，一蹶不振。"
    "我不知道我会不会那样，但我现在正走在已经面目全非的儿时街道上。"
    "小学的时候我就自己一个人上下学了，一直到成年了，工作了，也是一个人上下班。"
    "父母早就离开了A市，回了僻静的老家生活，没有被地震波及到。"
    "即便在我恢复之后，我们短暂地团聚了几日，我还是没有感觉到有多温馨。"
    "我当时，为什么那么想要活下来呢？"
    "哈哈哈哈…"
    "如果他也活下来了，我们会迎来怎样的生活呢？"
    "…"
    "但他还是没有和我一起离开废墟之下。"
    "都怪我。"
    "现在一想，在那样的毁灭性大灾难里死了，也并不丢人吧。"
    "如果我也死了，现在也不会这么难过了吧。"
    pause
    "…"
    "这个世界的庸常，"
    "这世界上一切的理所当然，"
    "一切秩序与美好，"
    "都是一场盛大的想象。"
    "用来衬托，"
    "那些极致的荒诞，"
    "刺骨的荒诞。"
    "绝望的荒诞。"
    show screen freeze(3)
    pause
    stop music fadeout 5
    $Achievement400.achieve()
    $Achievement.reachAnyEnd(p)
    $Notice.show()
    $Achievement.show()
    "{color=#9500ff}Normal End.\n——希望我们已经死去，那样我们就将不会彼此吞食。{/color}" 
    if replaying:
        jump afterreplay
    $persistent.ne = True
    $persistent.lastend = 'ne'
    $end_plot()
    
    return

label te:
    $start_plot()
    stop music
    scene black
    pause
    play music audio.painfultruth fadein 5.0
    "那场特大地震摧毁了整个A市，这个高楼林立的城市现在已经看不到五层以上的建筑了。"
    "所有伤员都被安置到了临近的b市医院，也包括我。"
    "政府拨款付了所有伤员的治疗费用，本就没多少钱的我也能被分配到一个单人病房。"
    "我是在那件事件发生的三天之后的深夜中醒来的。"
    "逃离梦魇的我如同于极度缺氧中苏醒的溺水者，大口呼吸着可能转瞬即逝的氧气。"
    "直到我慌乱的目光扫过自身所处的环境后才逐渐平静，却又在视线越过病房的巨大玻璃窗，注视着天空的群星时。"
    "也许是想到了什么，也许是因为痛苦，或者是什么乱七八糟的东西。"
    "才无可自拔地大哭了起来。"
    scene sickbed with fade
    "第二天的下午，一只灰狼进入了我的病房，提着一袋水果和一大束鲜花。"
    "正是那位把我救起来的消防员。"
    "我对水果并不感兴趣，对花也是。"
    "我赶他出去，但他执意要呆在这里，坐在我床边的木凳子上，拿小刀帮我一圈一圈地削着苹果。"
    "他说他叫Decay，第一次作为消防员出任务就赶上如此可怕的大灾难。"
    "经验不足的他不如其他消防员那样能迅速地找到伤员。"
    "但只有他找到了我，而且他在这场救援之中也就只拯救了我一个人。"
    "他说，他听到了我的心跳。"
    "可笑，那么远，怎么能听到我的心跳声呢？"
    s"“那我可真要谢谢你啊，我的救命恩人。你想从我这里得到什么呢，我已经什么都没有了。”"
    decay"“…我知道你现在心情不好。”"
    "他递给我削好的苹果。"
    "他说他很珍视我，因为我是他唯一救起来的人，虽然被救的人千千万，但他坚持认为，我对于他有什么特殊的意义。"
    "所以希望我快点好起来。"
    "我并没有受太重的伤，在重新补充了能量和水之后就没有大碍了。"
    "我接过苹果，挪到嘴边，开始咀嚼。"
    "他说，在把我从废墟下抱出来后，发现我即便神志不清也要用手指着废墟中的另一人。"
    "或者说，尸体。"
    "那具和我一起躺着的尸体已经死亡了好几天了，死亡原因是建筑碎片断裂的钢筋条插进下腹部导致的失血而死，但检查过后，他发现那尸体口中有混杂着白色药物颗粒的液体。"
    "他这次来也有一部分原因是调查这药物具体是什么。"
    s"“我没有给他下毒！我……不是我的错……”"
    decay"“冷静一点，[p.name]！……”"
    "我要进监狱了吗？喂他吃过期的药？从而害死了他？"
    s"“……那是强效止痛药。”"
    "……"
    s"“看看我的病历应该就知道了，我患有严重的头疼，随时都会带很多止痛药。”"
    s"“我以为他还活着，于是每天都给他灌一粒，怕他先于痛苦而不是失血而死。”"
    decay"“可他死亡怎么说也应该有一周多了，而把你救起来那天，他的嘴里还有没有融化完全的药。”"
    s"“……”"
    "我不知道该说什么。"
    "复杂的情绪在我脑髓中散开，刺痛每条和我一同幸存的神经。"
    s"“……应该是我不知道，或者不相信他早就死了的这个事实吧。”"
    s"“就连我都差点没能捡回自己这条命，更别说伤势那么重的他了。”"
    decay"“他是你的，同事吗？”"
    "…"
    "我思考了一会，看向他。"
    s"“是，仅仅是今天才认识的同事，他才第一天来我们公司。”"
    decay"“可怜。但地震也是没办法的事，没必要因为一个无关的普通人那么伤心，要重新打起精神来啊。”"
    "我把苹果核放在桌子上。"
    s"“总之，谢谢你的苹果。”"
    s"“也谢谢你。”"
    decay"“不用谢，这都是我应该做的。”"
    "灰狼起身，离开了这囚禁着我的59号病房。"
    "……"
    "那么，现在的我能做什么呢？"
    "已经失去了一切的我，如此残缺，时刻被折磨着的我，还能做什么呢。"
    pause
    scene black
    "……"
    "“Do the candles look forward to being used?”\n（蜡烛是否正期待着被使用？）"
    "“Enjoy bidding adieu, adieu?”\n（是否正争相期待着告别时刻？）"
    "“Every word I have saved for you came out wrong afterwards.”\n（每一句为你而留的话语都成为了谬言。）"
    "“Would you say,”\n（你认为，）"
    "“That someone who had every intention to be brave was a coward?”\n（那无时无刻不期待着成为勇者的人，会是个懦夫吗？）"
    "“Must be great being you,”\n（如果能成为你就好了，）"
    "“Power comes as second nature,”\n（勇气就如同你的天性，）"
    "“Must feel amazing to be longed for, longed for.”\n（如果能成为你就好了。）"
    "“So which home should someone as weak as I go?”\n（像我这样懦弱的人，又有哪里可做归宿呢？）"
    "“And which sky should I aim for when I\'ve only been low?”\n（当我消沉的时候，又该去往哪一片天空之下呢？）"
    scene bluesky with fade
    "我看向蔚蓝的天空，仿佛现在还是四五年前。"
    "那时的我正坐在大学教室的最后一排，对着和现在一样蓝的天空，做不切实际的白日梦。"
    window hide
    show screen freeze(3)
    pause
    stop music fadeout 5
    $Achievement401.achieve()
    $Achievement.reachAnyEnd(p)
    $Notice.show()
    $Achievement.show()
    "{color=#9500ff}True End.\n——在列车中，我牵着你的尸体的手，一同走到车厢尽头。{/color}" 
    if replaying:
        jump afterreplay
    $persistent.te = True
    $persistent.lastend = 'te'
    $end_plot()
    return

label CureEndingBeginning:
    stop music
    $p.onOutside = True
    $p.stime(9,11)
    scene elevator with fade
    menu:
        "6楼：神经科":
            pass
    scene sickbed with fade
    "我能闻到的只有消毒水味。"
    "至少我应该乐观一点？"
    "头疼很快就要消失了，我终于可以像正常人那样活着了。"
    "再也不用买那么贵的药，再也不用每天精打细算维持自己的状态，再也不用…"
    "但我为什么会感到恐惧呢？"
    "我在恐惧什么？"
    "躺在手术室床上的我思考着。"
    "Pathos医生并不在手术室里。"
    "刚刚被注射过麻醉药的身体逐渐变得疲倦，视野也变得昏暗。"
    "睡吧。"
    "睡醒了之后，就好了。"
    scene black with fade
    "…"
    $pause(5)
    $p.stime(23,54)
    play music audio.solitus fadein 5
    $clearE(p)
    $clearI(p)
    $p.severity = 1.0
    $p.severityRegarded = 1.0
    $MedicineD.add(p, 10)
    $p.mental = 100.0
    $p.cured = 0
    $p.plan = [NoTask, NoTask, NoTask]
    scene incar with fade
    "手术结束了。"
    "可以说我的头疼确实是减轻了不少，但是却感觉有点，奇怪。"
    "我好像丢掉了什么东西。"
    "某种曾经似乎十分重要的东西。"
    "我透过出租车上的车窗看着外面，随着车子的颠簸，在我口袋中的药瓶也叮当作响。"
    "这是免费提供给我的十粒名为德尔塔的新药。"
    "等明早起床的时候试试效果好了。"
    $p.onVacation = False
    $p.onOutside = False
    jump dayEnd

screen ce_choice:
    style_prefix "choice"

    vbox:
        textbutton "不跳" action Return()

        textbutton "跳":
            action NullAction()
            if renpy.variant("pc"):
                hovered Show(screen='ce_block')
                unhovered Hide('ce_block')
    if not renpy.variant("pc"):
        use ce_block

screen ce_block:
    hbox:
        
        imagebutton idle "solitus_eyes_chaos":
            xcenter 0.47
            ycenter 0.35
        

label CE:
    stop music
    $start_plot()
    
    if not replaying:
        $LifeIsColorless.add(p)
        $p.severity = 0.0
        $p.mental = 200.0
        $p.stime(15,54)
        $_skipping = False
        $p.onOutside = True
        
    scene black with fade
    "…"
    "最后一次手术结束了。"
    "于是我的病真正意义上地痊愈了。"
    if not replaying:
        $LifeIsColorless.add(p)
    "我再也不会头疼了。"
    "我现在是正常人了。"
    if not replaying:
        $LifeIsColorless.add(p)
    "于是，我的故事终于要落下帷幕了。"
    "那么我该开心吗？或者我该怎样去开心？"
    hide screen screen_dashboard
    $p.color = 1.0
    show screen screen_dashboard(p)
    play music audio.impendingdeath fadein 5
    scene rooftop with dissolve
    "……"
    "我喜欢天台，或者是任何高的地方。"
    "高的地方的风吹起来很舒服。"
    if not replaying:
        $LifeIsColorless.add(p)
    "俯瞰下面的风景又让我有种莫名的掌控感。"
    "而另一个极端，便是我可以藉由这种方法快速终结生命。"
    if not replaying:
        $LifeIsColorless.add(p)
    "那么一直到现在，我得到了什么呢？"
    "头不疼了，一点都不疼了，甚至什么都感觉不到了。"
    if not replaying:
        $LifeIsColorless.add(p)
    "就像是一根水管被堵死了一般。"
    "这就是我想要的吗？"
    "我曾听人说，要尽可能抓住一切机会远离会让你感到痛苦的事物。"
    "现在看来，也许当时将手术往后推才是明智的选择也说不定。"
    if not replaying:
        $LifeIsColorless.add(p)
    "至少在几个月前，生活还是充满色彩的。"
    "我捏着手中的香烟，看着顶端的烟雾随着天台的风飘散。"
    if not replaying:
        $LifeIsColorless.add(p)
    "就连烟草对我也没什么效果了，我只觉热辣的烟雾填充我的呼吸道，却不觉得有任何爽快之感…或许我已经忘记了什么叫做“爽快”。"
    "他们破坏了我的前额叶？将我的所有多巴胺受体填满？"
    if not replaying:
        $LifeIsColorless.add(p)
    "我不想知道他们在手术的时候对我做了什么，至少每次手术都让痛苦减轻了。"
    "但为了抛去痛苦，这份代价是合适的吗？"
    if not replaying:
        $LifeIsColorless.add(p)
    "我的脑内突然浮现出一只羽毛球场上跑动的白熊的影像，或是一只红色眼睛的灰狼。"
    "庆幸我仍然能记起什么东西，但仔细搜寻记忆，却完全没有关于他们是谁，他们做了什么的信息。"
    if not replaying:
        $LifeIsColorless.add(p)
    "也许我们曾经有机会做些什么，也许我不应该抛弃一切，只为了逃离痛苦。"
    "也许我触犯了命运，我就应该被头疼折磨，如果我免去这份痛苦，那么神就会夺走我的一切。"
    if not replaying:
        $LifeIsColorless.add(p)
    "回到那个问题，为了让自己不再痛苦，我坚持了到现在，是正确的吗？"
    menu:
        "是正确的":
            pass
        "是错误的":
            if not replaying:
                $LifeIsColorless.add(p)
            pass
    if not replaying:
        $LifeIsColorless.add(p)
    "存在还有什么意义吗？没有了感情和欲望的我已经残破不堪了。"
    menu:
        "有意义":
            pass
        "没有意义":
            if not replaying:
                $LifeIsColorless.add(p)
            pass
    if not replaying:
        $LifeIsColorless.add(p)
    "……"
    "我把燃尽的烟丢掉。"
    "是时候了。"
    "…"
    if not replaying:
        $LifeIsColorless.add(p)
    "那么，他们努力了这么久，几个月的心血，就要白费了。"
    "他们的研究成果，在我身上做的实验，也都将化为一具不会说话的尸体。"
    "是我过于自私，还是这一切的结果都是因为他们？"
    if not replaying:
        $LifeIsColorless.add(p)
    "我本应该和以前一样对生命充满希望的，而我现在却感受不到活着的丝毫美好。"
    "每天都只是在倒计时下一次手术而已，当全部手术都做完了，我该何去何从？"
    stop music
    show pathos with dissolve
    pathos"“别跳。”"
    "我的身体已经快离开天台，但我还是选择回头。"
    "Pathos就在我的身后，但他并没有伸出手拉住我，大概是对我关于求死的意向表示尊重。"
    "……"
    call screen ce_choice with dissolve
    play music audio.ihavelosteverything
    show pathos smile_mouth with dissolve
    "注视着我的黑色狮子微笑着向我伸出了手。"
    "于是我不再思考，只是握住他的手，任由他带我去任何地方。"
    scene black with dissolve
    "是的，不重要了，什么都不重要了。"
    "无论我丢掉了什么，无论活着有多么痛苦。"
    "只要有他，那么一切都不重要了。"
    show screen freeze(2)
    pause
    $Achievement402.achieve()
    $Achievement.reachAnyEnd(p)
    $Notice.show()
    $Achievement.show()
    "{color=#9500ff}Cured End.\n——即使我被焚烧，我依然如此愉快。{/color}" 
    $end_plot()
    if replaying:
        jump afterreplay
    $persistent.ce = True
    $persistent.lastend = 'ce'
    jump credits

label earthquakeBE:
    $start_plot()
    stop music
    scene ruins with dissolve
    "摇晃仍然没有停止。"
    "整个世界都因崩裂发出嘈杂的响声。"
    "我好害怕。"
    "谁来…谁来救救我…"
    if p.route == 'h':
        h"“[p.name]…！”"
    if p.route == 'a':
        a"“[p.name]…！”"
    "冷静…冷静…越是这种情况越要冷静…"
    $ss("dirty no_hat scared_eyebrow scared_eyes scared_mouth")
    s"“来…来这里…桌子底下！”"
    $sh()
    "我伸手，试图在正在剧烈摇晃的世界中抓住他的手。"
    "当我看向他时。"
    "眼中所见的景色上一刻还是他的样子。"
    "但下一刻，在一声崩塌的巨响后。"
    "变成了一片漆黑。"
    "更准确地说，他被楼上一块厚度比桌子还高的水泥完全压住了。"
    "我呆住了。"
    play music audio.impendingdeath
    "骨肉被碾碎的声音在我脑内反复播放着，属于他的血液混合被碾碎的肉体碎渣因挤压而四散飞溅，浓烈的血腥味被迫灌入了我的鼻腔。"
    "一种我无法阻拦的力量碾压着我的精神。"
    "足以撑开食管至整个口腔宽度的呕吐物如同破了个洞的气球一般从我的口中大量涌出。"
    "胃部扭曲疼痛，我没法停止这个行为，只是呕吐。"
    "呕吐物和血液混合在一起。"
    "不。"
    "这不是真的。"
    "这不是真的，不可能的。"
    "他死了，在我面前死了。"
    "没可能了，没救了，我要死了，我马上就要死了。"
    "像是被控制了四肢，我只是无意识地放任身体向后蜷缩，因冰冷止不住地颤抖。"
    "这只是一场噩梦，而我很快就会醒来。"
    "我闭眼，等待死亡的降临。"
    $_skipping=False
    show screen freeze(3)
    pause
    $Achievement103.achieve()
    $Achievement.show()
    $Notice.show()
    "{color=#FF0000}Bad Ending 3.\n——这只是一场噩梦，而你很快就会醒来。{/color}"
    $end_plot()
    $_skipping=True
    if replaying:
        jump afterreplay
    return

label despairBE:
    $start_plot()
    stop music
    scene black
    pause
    play music audio.concretejungle fadein 5.0
    "…"
    "距离那场事故，已经过去五年多了。"
    "那场特大地震摧毁了整个A市，但她的人民们也在努力重建她。"
    "幸运的是，当时的医院由于优秀的结构，或者仅仅是因为运气好，并没有倒塌，我也活了下来。"
    "当时的我…好像在准备手术。"
    "嗯…手术…是给谁来着的？"
    "好像是一个头疼很严重的人吧。"
    "哦…好像还以他的名字命名成了什么…S型综合征？"
    "我在整理手中的病历簿时，看到了夹在中间的他的照片。"
    "可惜的是，他并没有活过这场地震，死在了倒塌的废墟之中。"
    "我还记得，当我也加入了救援行动时，看见了在废墟下掩埋着的他的尸体。"
    "看上去他曾努力用药来维持…一个和他一起被困的伤者不被疼痛杀死的家伙？"
    "虽然并不清楚他们之间的关系，但这家伙还真是天真啊。"
    "这药只对他的病有效，对其他人的话，要么完全没有效果，要么就是致命的毒药…"
    "算了，我又何必因为一个死人多想呢。"
    "虽然很可惜，但…"
    "这个神秘的病症，随着他和这场地震，都一同成为了无法回溯的历史了。"
    "我看向窗外。"
    "高楼再次建起，街上行人如同蚂蚁般蠕动。"
    "无论是满地破败的建筑废墟，还是弥漫的尸体腐烂的臭气，都仿佛从未发生过。"
    "钢铁丛林倒塌，仍会再次升起。"
    "那些无人知晓的生命，都无声无息地成为了这片丛林的养料。"
    $_skipping=False
    show screen freeze(3)
    pause
    $Achievement104.achieve()
    $Achievement.show()
    $Notice.show()
    "{color=#FF0000}Bad Ending 4.\n——潮起潮落，银色的月光抹去我的足迹。{/color}"
    $end_plot()
    $_skipping=True
    if replaying:
        jump afterreplay
    return


label CuredBE:
    $Notice.show()
    play sound audio.g1
    if not replaying:
        python:
            for i in range(105 - p.cured):
                p.newDay()
    scene black with fade
    if not replaying:
        $p.severity = 0.0
        $_skipping = False
    play music audio.ce
    "最后一次手术结束了。"
    "我的病好了。"
    "我再也不会头疼了。"
    "我现在是正常人了。"
    "是的，我是一个正常人。"
    "我是一个正常人。"
    "我非常正常。"
    "我是个正常人。"
    "我好兴奋。"
    "我好兴奋！"
    "我好开心。"
    "我是一个正常人。"
    "我不是病人。"
    "我不是怪物。"
    "我的病治好了。"
    "我是正常人。"
    s"“你是不是嫉妒我是正常人？”"
    s"“你说啊！”"
    s"“你在看什么？”"
    s"“你在监视什么？”"
    s"“你嫉妒我，你嫉妒我治好了病。”"
    s"“你嫉妒我是个正常人。”"
    s"“我看到你了。”"
    s"“我要杀了你。”"
    window hide
    stop music
    play sound audio.g1
    show solitus angry_eyebrow scared_eyes normal_mouth at jumpscare
    call screen cfreeze(2)
    play sound audio.noise
    show solitus_g0
    call screen cfreeze(1)
    hide solitus_g0
    hide solitus
    play sound audio.noise
    play music audio.beep
    show solitus_g
    call screen cfreeze(3)
    $Achievement105.achieve()
    $Achievement.show()
    $Notice.show()
    "{color=#ff0000}Bad Ending 5.\n——我的意愿锁于桎梏之中，只有你的时间一分一秒地流逝。{/color}" 
    if replaying:
        jump afterreplay
    return