label ending0:
    $start_plot()
    scene hospital_corridor with dissolve
    play music audio.impendingdeath
    "是啊。"
    "我已经厌倦了。"
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
    scene rooftop2 with dissolve
    "去他妈的，这破烂身体，这操蛋的头疼，凭什么我生来就要遭受这样的痛苦。"
    "生在了科技发达的现代，又被告知没有办法治愈。"
    "为什么？为什么我要比别人痛苦啊！"
    "为什么我来到这个世界就要被这样对待啊？"
    "为什么……为什么……"
    "……"
    scene rooftop3 with dissolve
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
    if not replaying:
        $Achievement100.achieve()
        $Achievement.show()
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
    if not replaying:
        $Achievement101.achieve()
        $Achievement.show()
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
    if not replaying:
        $Achievement102.achieve()
        $Achievement.show()
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
    if not replaying:
        $Achievement400.achieve()
        $Achievement.reachAnyEnd(p)
        $Achievement.show()
    "{color=#9500ff}Normal Ending.\n——希望我们已经死去，那样我们就将不会彼此吞食。{/color}" 
    
    if replaying:
        jump afterreplay
    $persistent.lastend = Sticker59
    $end_plot()
    jump credits

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
    $ss("patient no_hat agony_eyebrow normal_eyes")
    s"“那我可真要谢谢你啊，我的救命恩人。你想从我这里得到什么呢，我已经什么都没有了。”"
    $sh()
    decay"“…我知道你现在心情不好。”"
    "他递给我削好的苹果。"
    $ss("patient no_hat agony_eyebrow normal2_eyes")
    s"“今天是…星期几…”"
    $sh()
    if not replaying:
        $persistent.te_weekday = rs(p, 1, 4)
    $teweekdayformat = teweekday()
    decay"“…[teweekdayformat]。”"
    $ss("patient no_hat sad_eyebrow")
    s"“哦…”"
    $sh()
    "我为什么会问这个问题呢，日期的观念对于现在的我已经被逐渐淡化，不具有什么意义了。"
    "他看上去有些拘谨，像是要说什么，不知道该如何开口的样子。"
    "他说他很珍视我，因为我是他唯一救起来的人，虽然被救的人千千万，但他坚持认为，我对于他有什么特殊的意义。"
    "所以希望我快点好起来。"
    "我并没有受太重的伤，在重新补充了能量和水之后就没有大碍了。"
    "我接过苹果，挪到嘴边，开始咀嚼。"
    "说实话，我没有在听他具体说了些什么，奇怪的是，只有[teweekdayformat]这三个字一直回荡…我为什么会一直思考这个呢？"
    "我听见他呼唤我名字的声音，当我意识到，我已经举着苹果半晌后，才茫然地看向他。"
    "无法言语说的酸痛感从我的手臂肌腱中传来，掌心苹果被我咬过的部分也已经被氧化。"
    decay"“[p.name]…精神状态有些差吗？…抱歉…我…”"
    $ss("patient no_hat agony_eyebrow")
    s"“不…我没关系，你继续说吧…”"
    $sh()
    "我不知道我的大脑还有没有任何可以容纳他字句的空间，只是它塞满了很多东西…"
    "我记得他深红色的血液，在昏暗的废墟下也如此恐怖，仅剩的过期面包，带有土腥味的水，还有哭声，求救声，最后一切都安静了…"
    "以及…挥之不去的…[teweekdayformat]…"
    "不…我…我应该听他说话…把那些记忆丢到脑后吧…"
    "我的大脑变得空白，为何我现在连集中注意力这件小事都难以达成…"
    "我看向他，我的双眼一定很空洞吧。"
    "他看上去有点沮丧，像是他知道我根本没有在听他说话一样。"
    $ss("patient no_hat agony_eyebrow normal2_eyes")
    s"“我…我在听，请你继续。”"
    $sh()
    "他说，在把我从废墟下抱出来后，发现我即便神志不清也要用手指着废墟中的另一人。"
    "或者说，尸体。"
    "那具和我一起躺着的尸体已经死亡了好几天了，死亡原因是建筑碎片断裂的钢筋条插进下腹部导致的失血而死，但检查过后，他发现那尸体口中有混杂着白色药物颗粒的液体。"
    "他这次来也有一部分原因是调查这药物具体是什么。"
    $ss("patient no_hat angry_eyebrow scared_eyes angry_mouth")
    s"“我没有给他下毒！我……不是我的错……”"
    $sh()
    decay"“冷静一点，[p.name]！……”"
    "我要进监狱了吗？喂他吃过期的药？从而害死了他？"
    $ss("patient no_hat sad_eyebrow closed_eyes")
    s"“……那是强效止痛药。”"
    $sh()
    "……"
    $ss("patient no_hat")
    s"“看看我的病历应该就知道了，我患有严重的头疼，随时都会带很多止痛药。”"
    $ss("patient no_hat sad_eyebrow sad_eyes")
    s"“我以为他还活着，于是每天都给他灌一粒，怕他先于痛苦而不是失血而死。”"
    $sh()
    decay"“可他死亡怎么说也应该有一周多了，而把你救起来那天，他的嘴里还有没有融化完全的药。”"
    $ss("patient no_hat sad_eyebrow scared_eyes")
    s"“……”"
    $sh()
    "我不知道该说什么。"
    "复杂的情绪在我脑髓中散开，刺痛每条和我一同幸存的神经。"
    $ss("patient no_hat sad_eyebrow normal2_eyes")
    s"“……应该是我不知道，或者不相信他早就死了的这个事实吧。”"
    $ss("patient no_hat sad_eyebrow closed_eyes tear")
    s"“就连我都差点没能捡回自己这条命，更别说伤势那么重的他了。”"
    $sh()
    decay"“他和你……是什么关系……”"
    "…"
    "当他提到这两个字时，我只感觉迷茫。"
    "我爱他？他爱我？恋人？朋友？仇人？互相讨厌？"
    "是什么能够确定我和他是什么关系呢？"
    "往事在我的思绪中飞速流转，以比走马灯还要快上无数倍的速度在我面前快速变换。"
    $ss("patient no_hat sad_eyebrow closed_eyes")
    s"“……”"
    $ss("patient no_hat sad_eyebrow normal2_eyes")
    s"“我……我不认识他。”"
    $sh()
    "怎么可能不认识他呢。"
    "我咬着牙，强缩着鼻子，只觉得眼泪要流出来，为什么我要克制呢。"
    "只是，他已经死了，再也没有机会回来了，和他所经历的一切又一切的东西，也都没有意义了。"
    "就像是，素不相识的人一样。"
    "亦或是，我只是不想让他开启更深的话题，我已经不想再回忆，不想再去思考，有关于他的事了。"
    decay"“这样啊……没必要因为一个无关的普通人那么伤心，要重新打起精神来啊。”"
    "我把苹果核放在桌子上。"
    $ss("patient no_hat sad_eyebrow closed_eyes")
    s"“……”"
    $ss("patient no_hat sad_eyebrow")
    s"“谢谢你的苹果。”"
    $ss("patient no_hat sad_eyebrow normal2_eyes")
    $sh()
    decay"“这都是我应该做的。”"
    "他笑着，像是努力让自己变成我的阳光。"
    "我也应该对他微笑的，但我无论如何都没法让我的嘴角弯曲。"
    "灰狼起身，离开了这囚禁着我的59号病房。"
    "……"
    "那么，现在的我能做什么呢？"
    "已经失去了一切的我，如此残缺，时刻被折磨着的我，还能做什么呢。"
    scene bluesky with fade
    "……"
    "我看向蔚蓝的天空，仿佛现在还是四五年前。"
    "那时的我正坐在大学教室的最后一排，对着和现在一样蓝的天空，做不切实际的白日梦。"
    if not replaying:
        $Achievement401.achieve()
        
        $Achievement.reachAnyEnd(p)
        $Achievement.show()
        show screen freeze(3)
    "{color=#9500ff}True Ending.\n——在列车中，我牵着你的手，一同走到车厢尽头。{/color}" 
    if replaying:
        jump afterreplay
    $persistent.lastend = OldPic
    $end_plot()
    jump credits

label se_h:
    $start_plot()
    $quick_menu = False
    $_game_menu_screen = None
    play music audio.travelofsolitude fadein 5
    scene setrain with fade
    "十分拥挤的长途火车。"
    "我拖拽着一个表皮已经破损的深蓝色拉杆箱，肩膀上还挂着一个电脑包，装着我三四斤的电脑，随着人流挤着只有一人宽的过道一直往前去。"
    "只说拉杆箱好像过于简单，实际上在我的拉杆箱两根金属拉杆的根部，还各系着两个塑料袋。一个装着三桶泡面——我这三天在火车上的粮食，一个装着我的洗浴用品——差点忘记带了。"
    "除此之外还有一个大布袋，里面装着极占空间的膨化食品零食，还有几瓶盐汽水，便宜的大桶冰红茶，以及一些水果干和辣的熟食。"
    "我不知道我是否有胃口吞下这么些东西，现在想来或许就把这些东西留在那里也不错。"
    "前面的人继续向前，我一边施以极扭曲的力气推动拉杆箱和一大堆寄生在上面的塑料袋和布包，一边扫视卧铺车厢，寻觅着车厢的座位号到底是被印在了什么地方。"
    "不知道我该感谢还是感到厌烦，我前面的一对情侣明明可以往卧铺车厢里走一步，把走廊让出来，却还在这极窄的走廊里站着，努力把他的大行李箱塞进下铺下方的空档里。"
    "我在等小情侣的这段时间里找到了左手边的卧铺床位座位号，在窗户的上方有两个极小的金属数字，56和57。而我也得到了时间检查自己手机上车票的座位号——59，那就是小情侣下一格的卧铺车间了。"
    "也好在他们似乎是听到了我心里的暗骂，男青年使劲一塞，把那个大到出奇的粉色行李箱哐当推进下铺床底，我也因此得到空间继续向前。"
    "飞机票仍然很贵，或许我有很多钱，但我很久以前就想试一试坐长途火车的感觉了，虽然听上去只是给自己一个坐牢的机会，还是那种望风都不允许的大牢。"
    "我被分到的是中铺，这么一看虽然有两个人高的车厢，被分为三份之后，空间也变得紧巴巴的。"
    "因为我带的东西比较多，就先走进自己的卧铺车厢中间的空位，让我身后的人先过去，同时把我系在拉杆上的塑料袋解开。"
    scene se with dissolve
    "整理完毕后，走廊也没有人通过了。"
    "我把走廊的小座位翻下来，坐在上面。"
    "火车逐渐开动，能看到眼前的风景正在向后方流淌，整个身体也开始随着火车运行而轻微晃动着。"
    "…"
    "我辞掉了工作，强行退了没到合同日期的房子，甚至连家里人都没告诉。"
    "我也没有告诉Halluke，我不知道我这样做是否正确。"
    "我知道，因为原生家庭导致的安全感缺失让他的内心还是一个彻头彻尾的孩子，因为要存活下去就要变成大人，但当他找到一根救命稻草时，他的内心就完全显露出来了。"
    "或许我可以关心他，帮助他，但我始终不能作为一个父亲面对他。"
    "他所要求的爱无边无际，我会因为他对爱的索取而承受不住的。"
    "…关于他的所作所为，我全都理解，但我并没有教育他如何去爱的义务，我已经承受了足够多的痛苦，面对他，我已经不再有最初的冲动了。"
    "我没法解决他的问题，只能逃避。"
    "逃避人生，逃避爱情，逃避自己。"
    "我不知道自己要去往何方，坐上这列长途火车也只是为了逃避。"
    "我的头还在隐隐作痛，但或许也已经没有那么痛了。"
    "在这段时间里，我达成了很多我从没有达成过的成就，成为了一个小有名气的网上作者，身体也算不错，脑袋似乎也比以前转的快了一点。"
    "但我不想再做程序员了，也许我的能力已经能让我在某些互联网公司做个一官半职，但我想了想，或许我最爱的还是写作。"
    "想用没有买药而省下来的这笔钱去旅行，四处看一看。"
    "Solitus这个网名我也用腻了，既然我有能力拥有那么多的粉丝，再重新建一个账号然后再拿一次平台的金牌作家证明也不是难事。"
    "…"
    "我活到了现在，光靠自己我肯定是没法做到这么多的。"
    
    if persistent.writerendname:
        $inputname = persistent.writerendname
        "我知道，是[inputname]在帮助我吧？"
        "再一次谢谢你，[inputname]。"
    else:
        "我知道，是“你”在帮助我吧？"
        $inputname = renpy.input("请告诉我，你的名字吧？", length=20, exclude="\"\'[]{}%$@?!#^&*\(\)")
        $inputname = inputname.strip()
        if not inputname:
            $persistent.writerendname = None
            "嗯…不想说也没关系…但我不会忘记我和你的这段时光。"
        else:
            $persistent.writerendname = inputname
            "是…[inputname]吗…好，我会永远记住的。"
            "无论如何，谢谢你。"
    if persistent.writerendname:
        "再见了，[persistent.writerendname]，我要去找自己的新生活了。"
    "也许，我们还会再见面的。"
    if not replaying:
        $Achievement404.achieve()
        $Achievement.reachAnyEnd(p)
        $Achievement.show()
    show screen freeze(3)
    "{color=#9500ff}Solitary Ending.\n——为我带来终点之人又身在何处？{/color}" 
    if replaying:
        jump afterreplay
    $persistent.lastend = TrainTicket
    $end_plot()
    jump credits

label se_a:
    $start_plot()
    $quick_menu = False
    $_game_menu_screen = None
    play music audio.travelofsolitude fadein 5
    scene setrain with fade
    "十分拥挤的长途火车。"
    "我拖拽着一个表皮已经破损的深蓝色拉杆箱，肩膀上还挂着一个电脑包，装着我三四斤的电脑，随着人流挤着只有一人宽的过道一直往前去。"
    "只说拉杆箱好像过于简单，实际上在我的拉杆箱两根金属拉杆的根部，还各系着两个塑料袋。一个装着三桶泡面——我这三天在火车上的粮食，一个装着我的洗浴用品——差点忘记带了。"
    "除此之外还有一个大布袋，里面装着极占空间的膨化食品零食，还有几瓶盐汽水，便宜的大桶冰红茶，以及一些水果干和辣的熟食。"
    "我不知道我是否有胃口吞下这么些东西，现在想来或许就把这些东西留在那里也不错。"
    "前面的人继续向前，我一边施以极扭曲的力气推动拉杆箱和一大堆寄生在上面的塑料袋和布包，一边扫视卧铺车厢，寻觅着车厢的座位号到底是被印在了什么地方。"
    "不知道我该感谢还是感到厌烦，我前面的一对情侣明明可以往卧铺车厢里走一步，把走廊让出来，却还在这极窄的走廊里站着，努力把他的大行李箱塞进下铺下方的空档里。"
    "我在等小情侣的这段时间里找到了左手边的卧铺床位座位号，在窗户的上方有两个极小的金属数字，56和57。而我也得到了时间检查自己手机上车票的座位号——59，那就是小情侣下一格的卧铺车间了。"
    "也好在他们似乎是听到了我心里的暗骂，男青年使劲一塞，把那个大到出奇的粉色行李箱哐当推进下铺床底，我也因此得到空间继续向前。"
    "飞机票仍然很贵，或许我有很多钱，但我很久以前就想试一试坐长途火车的感觉了，虽然听上去只是给自己一个坐牢的机会，还是那种望风都不允许的大牢。"
    "我被分到的是中铺，这么一看虽然有两个人高的车厢，被分为三份之后，空间也变得紧巴巴的。"
    "因为我带的东西比较多，就先走进自己的卧铺车厢中间的空位，让我身后的人先过去，同时把我系在拉杆上的塑料袋解开。"
    scene se with dissolve
    "整理完毕后，走廊也没有人通过了。"
    "我把走廊的小座位翻下来，坐在上面。"
    "火车逐渐开动，能看到眼前的风景正在向后方流淌，整个身体也开始随着火车运行而轻微晃动着。"
    "…"
    "我辞掉了工作，强行退了没到合同日期的房子，甚至连家里人都没告诉。"
    "我也没有告诉Acolas，我不知道我这样做是否正确。"
    "我知道，他是一个极度自负又极度自卑的人，同时还难以信任别人。当我为了他的项目焦头烂额之时，他本人又何尝不是如此呢。"
    "或许他还想着向我展示一个他亲手制造的世界，也许在他眼里我只是一个不努力的笨蛋吧，没有像他一样努力，所以才完不成他的任务。"
    "而在最后，褪下了一切的那一刻，我知道他也不过是一个孩子。"
    "…关于他的所作所为，我全都理解，但我并没有教育他如何去爱的义务，我已经承受了足够多的痛苦，面对他，我已经不再有最初的冲动了。"
    "我没法解决他的问题，只能逃避。"
    "逃避人生，逃避爱情，逃避自己。"
    "我不知道自己要去往何方，坐上这列长途火车也只是为了逃避。"
    "我的头还在隐隐作痛，但或许也已经没有那么痛了。"
    "在这段时间里，我达成了很多我从没有达成过的成就，成为了一个小有名气的网上作者，身体也算不错，脑袋似乎也比以前转的快了一点。"
    "但我不想再做程序员了，也许我的能力已经能让我在某些互联网公司做个一官半职，但我想了想，或许我最爱的还是写作。"
    "想用没有买药而省下来的这笔钱去旅行，四处看一看。"
    "Solitus这个网名我也用腻了，既然我有能力拥有那么多的粉丝，再重新建一个账号然后再拿一次平台的金牌作家证明也不是难事。"
    "…"
    "我活到了现在，光靠自己我肯定是没法做到这么多的。"

    if persistent.writerendname:
        $inputname = persistent.writerendname
        "我知道，是[inputname]在帮助我吧？"
        "再一次谢谢你，[inputname]。"
    else:
        "我知道，是“你”在帮助我吧？"
        $inputname = renpy.input("请告诉我，你的名字吧？", length=20, exclude="\"\'[]{}%$@?!#^&*\(\)")
        $inputname = inputname.strip()
        if not inputname:
            $persistent.writerendname = None
            "嗯…不想说也没关系…但我不会忘记我和你的这段时光。"
        else:
            $persistent.writerendname = inputname
            "是…[inputname]吗…好，我会永远记住的。"
            "无论如何，谢谢你。"

    
    if persistent.writerendname:
        "再见了，[persistent.writerendname]，我要去找自己的新生活了。"
    "也许，我们还会再见面的。"
    if not replaying:
        $Achievement404.achieve()
        $Achievement.reachAnyEnd(p)
        $Achievement.show()
    show screen freeze(3)
    "{color=#9500ff}Solitary Ending.\n——为我带来终点之人又身在何处？{/color}" 
    if replaying:
        jump afterreplay
    $persistent.lastend = TrainTicket
    $end_plot()
    jump credits

label fe_h:
    $start_plot()
    $quick_menu = False
    $_game_menu_screen = None
    stop music
    scene black
    pause
    "Halluke的声音将我唤醒。"
    "我只感觉眼皮十分沉重，它们互相黏连着，仿佛恩爱的恋人。"
    scene febed with dissolve
    "几乎是用尽全力，我将眼皮睁开，于是光芒便像是拥挤着钻进地铁车厢的人群一般点亮我的视野。"
    play music audio.phonysunrise fadein 5
    show halluke naked glitch_eyes no_glasses with dissolve
    h"“早啊，亲爱的。”"
    show halluke naked glitch_eyes no_glasses smile_mouth with dissolve
    h"“快起床，我知道我们的新家的床很舒服，但你得来尝尝我亲手做的早餐。”"
    "吃…早餐吗？"
    "好像…好像是有点饿。"
    "我伸出爪子，用力揉搓着眼皮，用物理方式强迫自己睁眼。"
    "不，不是有点，是很饿。"
    "我的整个身体被柔软的床垫支撑着，我坐起身，让卧室的模样进入我的双眼。"
    "我们的，新家？…"
    $ss('naked no_hat chaos_eyes none_mouth')
    s"“早饭吃什么？”"
    $sh()
    $gt = glitchtext(rd(5, 10))
    show halluke naked awkward_eyebrow glitch_eyes no_glasses with dissolve
    h"“八分熟的煎蛋，热培根，还有[gt]。”"
    "我抬高鼻子，煎肉的香味便流入了我的鼻腔。"
    "好香啊…"
    show halluke naked normal_eyebrow glitch_eyes no_glasses normal_mouth with dissolve
    h"“虽然手术治好了你的头疼，但你看上去为什么还是闷闷不乐的？”"
    $ss('naked no_hat chaos_eyes none_mouth')
    s"“嗯？…”"
    $sh()
    "哦…好像，我的头确实一点都不痛了。"
    $ss('naked no_hat chaos_eyes none_mouth')
    s"“…嗯…不知道…”"
    $sh()
    show halluke naked awkward_eyebrow glitch_eyes no_glasses smile_mouth with dissolve
    h"“吃完饭我们就出去散散步吧。”"
    $ss('naked no_hat chaos_eyes none_mouth')
    s"“行啊。”"
    $sh()
    "外出…外出走走吧，应该会让我好点…"
    "Halluke从餐桌前站起，走到床前——我的身边，他的毛发因太阳光而闪耀着，映照出{color=#f5f2eb}\{color=\#f5f2eb\}{/color}的光芒。"
    "我们自然地接吻，像每一对深爱着对方的情侣一样。"
    scene fe with dissolve
    "我看向窗外的日出，橘黄色的光将整个城市染上舒缓的颜色。"
    "也许，这就是我幻想的最美好的结局吧。"
    "我很幸福，是的，我很幸福。"
    "非常幸福。"
    if not replaying:
        $Achievement403.achieve()
        $Achievement.reachAnyEnd(p)
        $Achievement.show()
    show screen freeze(3)
    "{color=#ff0000}Fake Ending.\n——所以我躺在这里，躺在我们完美的天堂之中。{/color}" 
    if replaying:
        jump afterreplay
    $persistent.lastend = TransparentBottle
    $end_plot()
    jump credits


label fe_a:
    $start_plot()
    $quick_menu = False
    $_game_menu_screen = None
    stop music
    scene black
    pause
    "Acolas的声音将我唤醒。"
    "我只感觉眼皮十分沉重，它们互相黏连着，仿佛恩爱的恋人。"
    scene febed with dissolve
    "几乎是用尽全力，我将眼皮睁开，于是光芒便像是拥挤着钻进地铁车厢的人群一般点亮我的视野。"
    play music audio.phonysunrise fadein 5
    show acolas naked glitch_eyes with dissolve
    a"“早啊，亲爱的。”"
    show acolas naked normal_eyebrow glitch_eyes smile_mouth with dissolve
    a"“快起床，我知道我们的新家的床很舒服，但你得来尝尝我亲手做的早餐。”"

    "吃…早餐吗？"
    "好像…好像是有点饿。"
    "我伸出爪子，用力揉搓着眼皮，用物理方式强迫自己睁眼。"
    "不，不是有点，是很饿。"
    "我的整个身体被柔软的床垫支撑着，我坐起身，让卧室的模样进入我的双眼。"
    "我们的，新家？…"
    $ss('naked no_hat chaos_eyes none_mouth')
    s"“早饭吃什么？”"
    $sh()
    $gt = glitchtext(rd(5, 10))
    show acolas naked smile_eyebrow glitch_eyes smile_mouth with dissolve
    a"“八分熟的煎蛋，热培根，还有[gt]。”"
    "我抬高鼻子，煎肉的香味便流入了我的鼻腔。"
    "好香啊…"
    show acolas naked normal_eyebrow glitch_eyes normal_mouth with dissolve
    a"“虽然手术治好了你的头疼，但你看上去为什么还是闷闷不乐的？”"
    $ss('naked no_hat chaos_eyes none_mouth')
    s"“嗯？…”"
    $sh()
    "哦…好像，我的头确实一点都不痛了。"
    $ss('naked no_hat chaos_eyes none_mouth')
    s"“…嗯…不知道…”"
    $sh()
    show acolas naked smile_eyebrow glitch_eyes smile_mouth with dissolve
    a"“吃完饭我们就出去散散步吧。”"
    $ss('naked no_hat chaos_eyes none_mouth')
    s"“行啊。”"
    $sh()
    "外出…外出走走吧，应该会让我好点…"
    "Acolas从餐桌前站起，走到床前——我的身边，他的眼瞳如同红宝石，反射着{color=#f92828}\{color=\#f92828\}{/color}的光芒。"
    "我们自然地接吻，像每一对深爱着对方的情侣一样。"
    scene fe with dissolve
    "我看向窗外的日出，橘黄色的光将整个城市染上舒缓的颜色。"
    "也许，这就是我幻想的最美好的结局吧。"
    "我很幸福，是的，我很幸福。"
    "非常幸福。"
    if not replaying:
        $Achievement403.achieve()
        $Achievement.reachAnyEnd(p)
        $Achievement.show()
    show screen freeze(3)
    "{color=#ff0000}Fake Ending.\n——所以我躺在这里，躺在我们完美的天堂之中。{/color}" 
    if replaying:
        jump afterreplay
    $persistent.lastend = TransparentBottle
    $end_plot()
    jump credits

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
    if p.experience == 'wri':
        $clearscreens()
        play music audio.ce
        "手术失败了。"
        "我本该有机会{color=#ff0000}{u}完成我的作品{/u}{/color}，之后再死去的。"
        "但我没有。"
        "{color=#ff0000}{u}为什么，为什么没有让我写完呢？{/u}{/color}"
        "这都是因为你。"
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
        show screen freeze(3)
        "{color=#ff0000}Bad Ending ？.\n——不……他并不是被选中的那个。{/color}" 
        return

    
    $p.stime(23,54)
    play music audio.solitus fadein 5
    $clearE(p)
    $clearI(p)
    $WeatherUnknown.add(p)
    $p.severity = 1.0
    $p.severityRegarded = 1.0
    $MedicineD.add(p, 10)
    $p.mental = 100.0
    $p.cured = 0
    $p.plan = [NoTask, NoTask, NoTask]
    $p.des_p = -1
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
    default setting = False
    style_prefix "choice"

    vbox:
        textbutton "不跳" action Return()

        textbutton "跳":
            action NullAction()
            if renpy.variant("pc"):
                hovered SetLocalVariable("setting", True)
    
    if setting:
        timer 1.0/30.0 repeat True action Function(RigMouse)
        timer 0.5 action SetLocalVariable("setting", False)

screen ce_choice_android:
    default setting = False
    style_prefix "choice"

    vbox:
        box_reverse setting
        textbutton "不跳" action Return()

        textbutton "跳":
            action SetLocalVariable("setting", not setting)
    

init -1 python:
    def RigMouse():
        currentpos = renpy.get_mouse_pos()
        targetpos = [960, 0]
        renpy.display.draw.set_mouse_pos(currentpos[0], (currentpos[1] * 9 + targetpos[1]) / 10.0)



label ce:
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
    $clearscreens()
    $p.color = 1.0
    if not replaying:
        show screen screen_dashboard(p)
    play music audio.impendingdeath fadein 5
    scene rooftop with dissolve
    "……"
    "我喜欢天台，或者是任何高的地方。"
    "高的地方的风吹起来很舒服。"
    if not replaying:
        $LifeIsColorless.add(p)
    scene rooftop2 with dissolve
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
    scene rooftop3 with dissolve
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
    scene rooftop with dissolve
    show pathos with dissolve
    pathos"“别跳。”"
    "我的身体已经快离开天台，但我还是选择回头。"
    "Pathos就在我的身后，但他并没有伸出手拉住我，大概是对我关于求死的意向表示尊重。"
    "……"
    "不……我不会听他的，我已经受够了这个世界……"
    "求死的捷径就在身后，我……"
    if renpy.variant("pc"):
        call screen ce_choice()
    else:
        call screen ce_choice_android()
    play music audio.ihavelosteverything
    show pathos smile_mouth with dissolve
    "……"
    "他如同清楚我不会跳一样，嘴角十分得意地上扬。"
    "……我，为什么我……"
    "黑色狮子向我伸出了手。"
    "于是我不再思考，只是握住他的手。"
    scene black with dissolve
    "是的，不重要了，什么都不重要了。"
    "无论我丢掉了什么，无论活着有多么痛苦。"
    "一切都不重要了。"
    show screen freeze(2)
    pause
    if not replaying:
        $Achievement402.achieve()
        
        $Achievement.reachAnyEnd(p)
        $Achievement.show()
    "{color=#9500ff}Cured Ending.\n——即使我被焚烧，我依然如此愉快。{/color}" 
    $end_plot()
    if replaying:
        jump afterreplay
    $persistent.lastend = ExaminationReport
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
    play sound audio.suicide
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
    scene be3 with dissolve
    "不。"
    "这不是真的。"
    "这不是真的，不可能的。"
    "他死了，在我面前死了。"
    "没可能了，没救了，我要死了，我马上就要死了。"
    "像是被控制了四肢，我只是无意识地放任身体向后蜷缩，因冰冷止不住地颤抖。"
    "这只是一场噩梦，而我很快就会醒来。"
    "我闭眼，等待死亡的降临。"
    $_skipping=False
    $Achievement103.achieve()
    $Achievement.show()
    show screen freeze(3)
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
    if not replaying:
        $Achievement104.achieve()
        $Achievement.show()
    show screen freeze(3)
    "{color=#FF0000}Bad Ending 4.\n——潮起潮落，银色的月光抹去我的足迹。{/color}"
    $end_plot()
    if replaying:
        jump afterreplay
    return


label CuredBE:
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
    show screen freeze(3)
    if not replaying:
        $Achievement105.achieve()
        $Achievement.show()
        $Notice.messages = []
    "{color=#ff0000}Bad Ending 5.\n——我的意愿锁于桎梏之中，只有你的时间一分一秒地流逝。{/color}" 
    if replaying:
        jump afterreplay
    return



transform hardcorebe1_transform:
    parallel:
        xcenter 0.5
        ycenter 0.5
        easein 0.5 zoom 1.01
        easein 0.5 zoom 1.0
        0.5
        repeat
    parallel:
        easein 0.2 xoffset 1
        easeout 0.2 xoffset 0
        easein 0.2 xoffset -1
        repeat
    parallel:
        easein 0.2 yoffset 1
        easeout 0.2 yoffset 0
        easein 0.2 yoffset -1
        repeat
    

transform hardcorebe2_transform:
    easein 0.5 matrixcolor HueMatrix(-360)
    easein 0.5 matrixcolor HueMatrix(360)
    repeat


label hardcorebe1:
    $clearscreens()
    $start_plot()
    stop music
    scene black
    pause
    scene hardcorebe at hardcorebe1_transform with fade
    play music audio.afterdesperation fadein 5.0
    "我醒来了。"

    "但我没法止住咳嗽，比生过最重的流感的咳嗽时还要用力，每次咳嗽都让喉咙剧痛。"
    "痛苦传递至胸腔，随着震动波及到全身，只感觉整个身体都要散架了一样。"
    "痰液有时候是黄色的，有时候带着血液，有时候只有血液。"
    "我能看见的事物模糊不清，但幸好我还能思考，我还能回忆。"
    "我的全身都在哀嚎，我比活着的任何时候都痛苦，我的双手每动一寸都会加剧疼痛，我的全身无意识地颤抖。"
    "我感到反胃，从我的口中涌出未消化的东西，灼烧感攻击着我的喉咙和舌头，我像是被人拽着嘴里的一根线头，随后被扯出来一大堆东西一样。"

    "也许这就是我的终结吧，这种病不可能只是软绵绵地让我头疼而已，它就像耐心等待的猎手，而我已经踩上了他的圈套。"
    "在那之后，身体没有缘由地越来越差，浑身无力，恣意涌出的虚汗总是打湿我的衬衫。"
    "再往后，头疼加剧，随之疼痛扩散到了全身，已经没有药物能够拯救我了。"
    "就像骨头里长满了刺，轻微的挪动都会产生剧痛。"

    "病房里只有我一个人，只有一张床。"
    "白色的被子沉重如山，我没法将它移开，我想踢开被子，但我的双腿似乎已经退化，不听使唤。"
    "光线从百叶窗的缝隙中流入房间，我已然无法分清外面的光是太阳还是彻夜开启的路灯。"
    scene black with fade
    "痛苦让我无法入睡，但我还是睡着了。"
    "生命即将走向尽头，身体里的空隙也将被泥土和腐水填满。"

    "他们会在哪里将我找见呢？"

    if not replaying:
        $Achievement106.achieve()
        $Achievement.show()
    show screen freeze(3)
    "{color=#FF0000}Bad Ending 6.\n——那风摇动窗框，冲入钢铁丛林之中，而后消失无闻。{/color}"
    $end_plot()
    if replaying:
        jump afterreplay
    return

label hardcorebe2:
    $clearscreens()
    $start_plot()
    stop music
    scene black
    pause
    scene hardcorebe at hardcorebe2_transform with fade
    play music audio.afterdesperation fadein 5.0
    "我醒来了。"

    "但我没法止住咳嗽，比生过最重的流感的咳嗽时还要用力，每次咳嗽都让喉咙剧痛。"
    "痛苦传递至胸腔，随着震动波及到全身，只感觉整个身体都要散架了一样。"
    "痰液有时候是黄色的，有时候带着血液，有时候只有血液。"
    "我能看见的事物模糊不清，但幸好我还能思考，我还能回忆。"
    "我的全身都在哀嚎，我比活着的任何时候都痛苦，我的双手每动一寸都会加剧疼痛，我的全身无意识地颤抖。"
    "我感到反胃，从我的口中涌出未消化的东西，灼烧感攻击着我的喉咙和舌头，我像是被人拽着嘴里的一根线头，随后被扯出来一大堆东西一样。"

    "也许这就是我的终结吧，这种病不可能只是软绵绵地让我头疼而已，它就像耐心等待的猎手，而我已经踩上了他的圈套。"
    "在那之后，大概是脑袋里负责某些东西的区域被损坏了吧，到现在连愉悦都没法理解是什么感觉了。"
    "梦境频繁在现实中重现，或者我们应该将其称之为幻象？直到现在，我再也辨不出什么是真实，什么不是。"
    "唯有痛苦仍在。"

    "病房里只有我一个人，只有一张床。"
    "白色的被子沉重如山，我没法将它移开，我想踢开被子，但我的双腿似乎已经退化，不听使唤。"
    "光线从百叶窗的缝隙中流入房间，我已然无法分清外面的光是太阳还是彻夜开启的路灯。"
    scene black with fade
    "痛苦让我无法入睡，但我还是睡着了。"
    "生命即将走向尽头，身体里的空隙也将被泥土和腐水填满。"

    "他们会在哪里将我找见呢？"

    if not replaying:
        $Achievement106.achieve()
        $Achievement.show()
    show screen freeze(3)
    "{color=#FF0000}Bad Ending 6.\n——那风摇动窗框，冲入钢铁丛林之中，而后消失无闻。{/color}"
    $end_plot()
    if replaying:
        jump afterreplay
    return

label hardcorebe3:
    $clearscreens()
    $start_plot()
    stop music
    scene black
    pause
    scene hardcorebe with fade
    show blurred:
        alpha 0.3
    play music audio.afterdesperation fadein 5.0
    "我醒来了。"

    "但我没法止住咳嗽，比生过最重的流感的咳嗽时还要用力，每次咳嗽都让喉咙剧痛。"
    "痛苦传递至胸腔，随着震动波及到全身，只感觉整个身体都要散架了一样。"
    "痰液有时候是黄色的，有时候带着血液，有时候只有血液。"
    "我能看见的事物模糊不清，但幸好我还能思考，我还能回忆。"
    "我的全身都在哀嚎，我比活着的任何时候都痛苦，我的双手每动一寸都会加剧疼痛，我的全身无意识地颤抖。"
    "我感到反胃，从我的口中涌出未消化的东西，灼烧感攻击着我的喉咙和舌头，我像是被人拽着嘴里的一根线头，随后被扯出来一大堆东西一样。"

    "也许这就是我的终结吧，这种病不可能只是软绵绵地让我头疼而已，它就像耐心等待的猎手，而我已经踩上了他的圈套。"

    "在那之后，我的身体没法忍住对那种特别药物的成瘾性，总是不自觉地过量，把钱都花光了也没有改善，甚至头比以前更疼了。"
    "药物的作用也不明显了，因为没钱买药，多次出现戒断反应后，我便总是晕倒，或是沉入幻觉之中无法自理，最后只能来到这里。"

    "病房里只有我一个人，只有一张床。"
    "白色的被子沉重如山，我没法将它移开，我想踢开被子，但我的双腿似乎已经退化，不听使唤。"
    "光线从百叶窗的缝隙中流入房间，我已然无法分清外面的光是太阳还是彻夜开启的路灯。"
    scene black with fade
    "痛苦让我无法入睡，但我还是睡着了。"
    "生命即将走向尽头，身体里的空隙也将被泥土和腐水填满。"

    "他们会在哪里将我找见呢？"

    if not replaying:
        $Achievement106.achieve()
        $Achievement.show()
    show screen freeze(3)
    "{color=#FF0000}Bad Ending 6.\n——那风摇动窗框，冲入钢铁丛林之中，而后消失无闻。{/color}"
    $end_plot()
    if replaying:
        jump afterreplay
    return

label we:
    $clearscreens()
    $start_plot()
    stop music
    scene black
    pause
    scene rooftop at hardcorebe1_transform with fade
    play music audio.noattachmentanymore fadein 5.0
    "我终于来到了这个地方。"
    "……"
    if persistent.writerendname:
        $inputname=persistent.writerendname
        "[inputname]。"
    "请告诉我。"
    "我为什么要活着，为什么要坚持下去？"
    "人们未被同意地被带到了这个世界，跟随常识的通路逐渐获得精神与智慧，随后投入到一些事情中。"
    "我猜，活着的目的就是做一些事。"
    "不管这些事有没有意义，有没有结果，只是想要去做，想知道做完了之后会怎样。"
    "也许这就是基因进化到现在的结果，这便是基因的意愿。"
    "但是事情是做不完的，所以人们为了让自己获得虚伪的永生，让下一代人去做那些事情。"
    "随后他们继续做一些事，一些符合他们社会身份和年龄的事。"
    "直到死去。"
    "但是，如果没有想做的事，也觉得做那些事情无趣的话，简单的死亡是否也是可以的呢？"
    "如果已经做完了想要做的事情，体验了所有想体验的东西，是否也该是时候解脱了呢？"
    "无尽的远方，无尽的人们，都与我有关吗？"
    "…"
    "我已经做完我应该做的事了，可以让我去死吗？"
    "我已经受够了。"
    scene rooftop2 at hardcorebe1_transform with dissolve
    "不仅仅是头疼，我已经受够了我身边的人们一刻不停地折磨我了。"
    "那是爱吗，是陪伴吗？快乐的回忆之后便是苦涩的回忆，然快乐不会持续太久，而苦涩却反复折磨着我。"
    "我写完了那本书。"
    "也许不会有人在我死后去翻动那些荒唐的言论，那些故事或许会永远被淹没于尘埃之中。"
    "但我已经厌倦了，从一开始的兴趣，到烦闷，到厌恶，我只觉得恶心。"
    "翻阅回忆，然后把它们呈现于文字之上，就像是把吃进去的东西挖出来，再混合一些颜料，一股脑涂抹在画布上。"
    "写一个自己的故事，观赏着自己，评价着自己，分析着自己，反问着自己，嘲笑着自己，摒弃自己。"
    "为什么…为什么会变成这样呢？"
    "但思考这个问题已经没有意义了，在那之后，所有的存在也都没有意义了。"
    "我已经完成了不是吗？"
    "我已经完成了小时候的我的所有愿望。"
    "我在这个遗弃了我的世界中留下了痕迹。"
    "可是，是为了什么呢？为什么要这样做呢？"
    "对活着的我和死去的我来说有什么意义？"
    "当我的思绪离开了躯壳之时，世界还是否存在？"
    "当我闭上双眼时，人偶们是否也会停止移动？"
    "在世界之外有人注视着，观察着，凝视着我吗？"
    "这是一个只属于我的世界吗？"
    "当世界失去了意义之后，它还仍然存在吗？"
    "当“我”的意识消散，还会有另一个我吗？"
    "“我”是谁？"
    "…"
    "不，我不能再想了。"
    "我的脑袋，好疼，要炸了。"
    "它鼓胀着，在脑脊液中翻涌，挤压着头骨。"
    "它收缩，它膨胀，它痉挛，它压迫。"
    "碎裂的冰锥刺入了我的脑髓，随后被绞肉机的百千滚轮碾压崩解割裂。"
    "我没法再想出什么形容词了。"
    "它是在催促着我吗？"
    scene rooftop3 at hardcorebe1_transform with dissolve
    "也许我该露出一个笑容？"
    scene black
    play sound audio.suicide
    show screen freeze(5)
    if not replaying:
        $Achievement405.achieve()
        $Achievement.reachAnyEnd(p)
        $Achievement.show()
    show screen freeze(3)
    "{color=#9500ff}Writer Ending.\n——我再也无法忍受。再也不能。{/color}"
    $end_plot()
    if replaying:
        jump afterreplay
    $persistent.lastend = TheBook
    jump credits