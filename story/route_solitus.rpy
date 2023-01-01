label solitus_route_3:
    #第二周周一固定触发
    $start_plot()
    scene bathroom with fade
    stop music fadeout 5
    "呼吸。"
    "深呼吸。"
    "然后闭眼睛。"
    "就像被石头卡住的排水管道，意识正从思维的狭小罅隙中互相推搡挤压着流出。"
    "疲倦，困倦，眩晕，沉重如铁的大脑，以及毫无频率的头疼。"
    "像定了五六个相差五分钟的闹钟，像尖锐刺耳的消防演习警报。"
    "让我想起浓烟还有塑胶融化的二氧化硫气味儿。"
    play music audio.debilitatinganxiety
    "我讨厌焦虑。"
    "我也讨厌自己。"
    "早起就像是个敏感而脆弱的天平，当一颗灰尘降落在一侧，这座天平便立刻倾倒了。"
    "我也曾早睡早起过，比如早于闹钟一整个小时起床，这样就有了很多时间可以用来刷手机，还能绕个弯在上班之前去买喜欢喝的奶茶。"
    "谁不想保持这份美好呢？"
    "但仅仅是一次稍微有些过火的加班，一次看喜欢的电视剧直到凌晨，或是一次单纯的难以入眠。"
    "就足以使这个平衡分崩离析。"
    "总有无形的焦虑扼住我的精神，恐惧着自己是否能早些起床。"
    "但越是害怕，越是想要睡眠，就越睡不着，越对睡眠这件事产生畏惧。"
    "睡眠是温馨的，解脱的。"
    "又是可怕的，未知的。"
    "在睡眠后我们的精神去往何处，做什么样的梦，或者经历几个小时的沉默，甚至就此直接死去。"
    "我畏惧死亡吗？"
    "也许畏惧，因为我还有很多事情没做，很多梦想没有完成。"
    "我需要活着。"
    "我必须睡下去。"
    "于是，在床上紧闭着眼，徒熬无穷的时间，才将自己推进无意识的深渊。"
    "我也很爱自己，即便我总是害怕自己起不来，但我总是能够起来。"
    "就像现在。"
    "我伸手，插进睡衣的口袋里，把手机掏出来。"
    "我还有半个小时可以拿来整理自己。"
    "但我只觉得自己快要死了，像是丧尸一般神志不清，在无意识的情况下挪动身体，做着一百年后也不会改变的事。"
    "牙膏，牙刷，热水，上下移动，挤压，泡沫，喝水，漱口，吐水。"
    "洗脸。"
    "我打开水龙头，看着冷水哗哗冲进冒着热气的水盆中，在白雾中呼吸潮湿的空气。"
    "我看着镜子。"
    "我很久没有刮胡子了。"
    "倒不如说是自己很久没有仔细看镜子了。"
    "门口玄关那里有一面穿衣镜，我在穿好衣服的时候都会瞟一眼自己的大致模样，然后匆匆离开。"
    "我居然已经长了这么多胡子了吗。"
    "我关掉水龙头，用左手摸着自己的下巴。"
    "柔软的，毛茸茸的一层。"
    "我看向镜子里的自己。"
    "已经是半个大叔了，即便我明明才刚毕业不久。"
    "唉。"
    "我清楚我并没有那么多闲工夫欣赏自己，现在可能只剩下二十分钟了。"
    "早餐？那是什么，弱者才需要吃早餐。"
    "我捧起水，泼到脸上，还有脑袋上。"
    "热水也许并不能让我清醒，凉水应该也不行。"
    "洗面奶，护毛素。"
    "这些去油的东西让人觉得舒适。"
    "我拽下毛巾架上的毛巾，简单擦干后把吹风机插在插座上。"
    "热乎乎的风吹过来了。"
    stop music fadeout 5
    "…"
    if not replaying:
        $rec = r2(15 * Task.getRecoScale(p) * p.sleepRecovery)
        $Notice.add('恢复了%s点精神状态。' % rec)
        $p.mental += rec
        $Notice.show()
    "也许不那么迷糊了。"
    "但我知道，我的身体肯定已经被这种作息摧残了。"
    "周末多睡一会好了…。"

    $end_plot()
    if replaying:
        jump afterreplay
    $Achievement200.achieve()
    $Notice.show()
    return



label solitus_route_4:
    #第二周以后，使用梅子酒，同时拥有焦虑
    hide screen screen_phone_food
    hide screen screen_phone_bg
    $start_plot()
    scene workarea with fade
    stop music fadeout 5
    "酒精，吸烟，或者是用极端的方法都是为了一个目的。"
    "让自己变成孩子。"
    play music audio.debilitatinganxiety
    "孩子不会想太多乱七八糟的事，孩子做事不会在意后果，孩子的世界只有快乐。"
    "过得太久，想得也就太多，压力也越大就是了。"
    "我其实对酒并没有什么想法。"
    "也许是好奇他们口中所说的“借酒消愁”到底是什么感觉，还有一醉方休具体是个什么样。"
    "我对普通的粮食酒没什么兴趣，也讨厌啤酒花的味道。"
    "所以我偶尔会买一些花里胡哨的果酒。"
    "传统的梅子，葡萄，也有比较新颖的荔枝，加了柠檬口味的清酒。"
    "结果是，在喝过之后完全没法让我感觉一点儿喝醉的感觉。"
    "不过我倒是很喜欢那种火热感。"
    "从口腔到喉咙，到胃。"
    "仅仅是它所经过的地方，都如同被点燃一般，烧起来了。"
    "或许是酒精杀死了什么细胞，与什么蛋白质产生了什么样的反应。"
    "但这都和我无关，而且仅仅是这种奇妙的感受还不足以让我上瘾。"
    "我仍然会买一些用很漂亮的瓶子装着的果酒，当饮料一个人对着电脑喝下之后，在体验过这种火热的温暖后，把瓶子放在我的柜子里收藏。"
    "也许这些收藏完全不算是收藏，更像是收酒瓶的垃圾场一角。"
    "某天我就会清理掉那些东西吧。"
    "也许。"
    "我看着矗立于我面前的喝了半瓶的梅子果酒的深黄色圆柱酒瓶。"
    "再次拎起黄色的瓶身把酒味四溢的液体灌进口腔。"
    "不能太急，有些难以下咽。"
    "在一点点舔食中，我再一次体验到了那种熟悉的灼热感。"
    if not replaying:
        $Notice.add('获得了2层精神的释放。')
        $MentRezA.add(p, 2)
        $Notice.show()
    "……"
    "很棒，是的，很棒。…"
    "至少此刻……我能缓解一些来自内心深处的焦虑。"
    stop music fadeout 5

    $end_plot()
    if replaying:
        jump afterreplay
    $p.s4=True
    $Achievement201.achieve()
    $Notice.show()
    jump TaskExecuting


label solitus_route_5:
    #week>=2, writing>1.3, task=='读传统文学', 下一个task=='随笔写作'
    $start_plot()
    scene workarea with fade
    stop music fadeout 5
    "是的，那本小说。"
    "我已经看完全部了，从第一页到第六百零二页。"
    "现在我终于可以心安理得地把它放在书柜最左侧了，它接下来的生活便是作为背景板的一平方米区域的色块。"
    "和其他五颜六色，有些用巨大字号写上去的文字的书脊排列在一起。"
    "也许某日还会有人来翻看它，或者未来几年后的我突然想起了它。"
    "否则他就已经算是结束他的使命了。"
    "作者把他的细腻心思灌输进这些纸张之中，以白纸与油墨作为载体，组合成为一本美丽的书，来到我的眼前。"
    "我再通过阅读，将作者想要表达出来的苦痛吸收，感受。"
    if not replaying:
        $Notice.add('降低了3点严重程度。')
        $p.severity -= 0.03
        $Notice.show()
    play music audio.debilitatinganxiety
    "很多人总是希望看到美好的结局，可是创作本身就是一种情绪的喷发，快乐仅仅是其中的一种，同时也并不激烈。"
    "而激烈的快乐便是幸福，可幸福又来源于苦难。"
    "没有强烈的情绪是没法写出小说的，仅仅是一瞬间的念头，也需要聚集起来，成为一大块情绪聚合物之后。"
    "才能被写成小说。"
    "所以这块巨大的聚合物必然不可能全是由正面情绪组合成的，总会带着悲伤和遗憾。"
    "小说是一种什么样的载体？"
    "人类，情绪，矛盾。"
    "我曾认为没有冲突就不会有故事，如果你想要写出两个人之间的纽带多么坚韧，就要写一个反派试图割裂他们。"
    "到冲突不一定必须是人，也许是没有说出口的话，没有写完的诗，还有没有送出的信。"
    "而我最倾佩的则是困难与挫折所带来的对人的改变。"
    "也许我们写一位士兵经过严刑拷打后不屈不从，最后战争胜利。"
    "但如果写胸怀斗志，踌躇满志的年轻人，遭受无穷的挫折和背叛，经历命运的玩弄之后崩溃的故事，仍然也是一个有趣的题材。"
    "歌颂人的勇气与意志，或是控诉命运的不公与无情。"
    "这些事情很多情况下并不会在一个真人身上发生，但可能发生在不同的人身上。"
    "现代人的生活枯燥无味，单调的生活和闭塞的人际关系交流让活人变成两点一线的行尸走肉。"
    "但总会发生一点一滴的趣事，再加上一点点的幻想。"
    "小说的故事便就有了。"
    "写点东西吧，怎么样？"
    "我坐在电脑前的旋转椅上，从笔筒里随手抽出一根塑料中性笔。"
    $p.s5=True
    $Achievement202.achieve()
    $Notice.show()
    stop music fadeout 5

    $end_plot()
    if replaying:
        jump afterreplay
    call screen screen_tr_commission_inputs(p)
    call Task_processing from _call_Task_processing_34
    $p.times+=1
    $FreewheelingWriting.executeTask(p)
    return



label solitus_route_6:
    #week>=2, 睡眠后, 灵感大于5
    $Notice.show()
    $start_plot()
    scene bedroom with fade
    stop music fadeout 5
    "我马上就会醒来。"
    "在梦中的我的脑内浮现出了这样的言语。"
    "我的意识面对着棕褐色的牢狱，但几乎是一瞬间，我的眼前便变成完全的黑。"
    "某种奇怪的感觉出现，就像将电器的插头插在插座上，电子流入大脑准备开机的感觉。"
    "我再次获得掌管这具躯壳的意识的权力。"
    "…"
    "我醒了。"
    "黑色方格被子，深蓝色的天花板还有遮光性很差的窗帘。"
    play music audio.debilitatinganxiety
    "这种从让人的意识完全沉浸的梦中醒来给予我的昏沉感，让我对这些本应该十分熟悉的物件感到莫名的陌生感。"
    "甚至让如此简单的记忆调用行为都花费数秒。"
    "噢…"
    "不是被闹钟吵醒的，屋子是昏暗的，到并非完全的漆黑…"
    "现在，现在是什么时候？"
    "我脑内相互咬合的齿轮好像上了锈，它们本应该快点转起来的。"
    "大概是因为，梦境太混乱又太真实吧。"
    "我深呼吸，从枕头底下摸出来手机，还有插在手机耳机孔上的乱成一团的耳机线。"
    "荧幕亮起。"
    "在意识到现在仍然是合法的休息日后松了口气。"
    "…"
    if not replaying:
        $Notice.add('降低了3%的额外严重程度倍率。')
        $p.severityRegarded -= 0.03
        $Notice.show()
    "随着陌生感一同褪去的是梦境中的记忆。"
    "我努力回忆梦境的具体内容，却只记得一些零散的画面碎片。"
    "比如我站在什么样的地方，躺在病床上，和谁聊了聊天…"
    "也仅仅能想起一点点。"
    "为了生存，那些来自梦境的记忆是不可取的，不现实的，所以大脑要尽快从海马体中把虚构的不真实记忆消灭掉。"
    "但可以确定的是，这梦又长又美妙，我的意识已经习惯于认知自己为梦境中的角色了。"
    "因此才在梦境的泡泡破碎之后，反倒不那么适应现实的意识了。"
    "…"
    "不过这种体验很有趣。"
    "意识和回忆从空白被逐渐灌入的感觉，像电流通过内存和硬盘。"
    "我喜欢在各种奇怪的时候睡觉，不仅仅是为了享受这种对现实的疏离感，也能让我暂时摆脱头疼的折磨，"
    "至少在我刚刚起床这段时间，我的头还不会太痛。"
    "…"
    stop music fadeout 5
    "不能像这样单纯地躺在床上浪费时间了。"
    "该去做点有意义的事了…"

    $end_plot()
    if replaying:
        jump afterreplay
    $p.times+=1
    $p.s6=True
    $Achievement203.achieve()
    $Notice.show()
    jump TaskExecuting



label solitus_route_7:
    #week>=2, 在家工作，带有过劳，时间为晚上
    $Notice.show()
    $start_plot()
    scene workarea with fade
    stop music fadeout 5
    "我将笔记本电脑合上。"
    "现在已经这么晚了吗…"
    "不管工作完成的如何，我已经把大部分要做的事都简单地处理一遍了，明天上班的时候应该会更轻松点。"
    play music audio.debilitatinganxiety
    "早知道就不堆那么多工作了，就算自己头疼，谋生的事该做还是要做啊…"
    "在这片钢铁丛林里，一个像我这样的普通人的可代替性实在是太强了。"
    "不加倍努力，就会被人从树枝顶端丢下去吧。"
    "我突然想起自己还在大学的时候的事情。"
    "那时候的我面对能用自己能力解决或是实现的想法时，都格外有动力。"
    "为了脑袋里灵光一现的想法编程，写一些赛博朋克风水学占卜小插件，或是方便查找当时我玩的那款对战游戏里，面对对面的英雄胜率最高的那个。"
    "我甚至花了很多时间，用回合制游戏重现一些mmorpg里已经被删除的职业和技能组。"
    "也许是怀念，也许单纯是为了好玩。"
    "每写一个职业都花费我大量的时间和精力，不过我倒也乐此不疲就是了。"
    "不过在发给朋友试玩的时候，他们基本上都不太感兴趣的样子。"
    "真让人挫败啊…"
    "不过后来我也清楚了，这些东西也只是以及排解无聊而做的一堆垃圾而已…"
    "也并不是花费时间精力做出来的东西就一定会被人喜欢。"
    "看看现在的我，连建一个独属于自己的新项目的力气都没有了。"
    "每次意识到自己已经不是小孩子的时候，都有种让人想哭的感觉。"
    if not replaying:
        $Notice.add('睡眠消耗的精神状态降低了5%。')
        $p.deteriorateConsumption -= 0.05
        $Notice.show()
    "…"
    "大人的生活…真无趣啊。"
    stop music fadeout 5

    $end_plot()
    if replaying:
        jump afterreplay
    $p.times+=1
    $p.s7=True
    $Achievement204.achieve()
    $Notice.show()
    jump TaskExecuting


label solitus_route_8:
    #week>=2, 睡前 一天不吃饭
    $Notice.show()
    $start_plot()
    scene bedroom with fade

    play music audio.debilitatinganxiety
    "饥饿。"
    "如果饥饿是一种带有类型的伤害，那应该不是物理，也不是魔法，而是一种“无”属性伤害。"
    "和用来测试游戏而写就的造成瞬间伤害的代码造成的伤害应该是同一个属性的。"
    "为什么我突然想这种事，大概是因为今天一直都没什么胃口，所以基本上也没吃什么东西，最后躺在床上，肚子才想起来饿。"
    "它就在我的腹部用咕咕声提前警告，随后像拧干抹布的水一样扭着胃袋，偶尔还让一些掺了水的胃酸回流到嗓子眼。"
    "胃疼并不比头疼差多少，但幸好我的胃还没有差到那个地步——我应该庆幸才对。"
    "毕竟从小我便不怎么乖乖吃饭，长大了之后，也总是忙着手上的，或者是其他的原因，甚至单纯是因为烂而不去吃饭。"
    "到了现在，虽然肠子有些这样那样的问题，但吃一段时间药也会恢复。"
    "饥饿更可怕的是头疼，没有了燃料，这个耗电量最大的装置便以为你施加无法忍受的头疼提醒你吃饭。"
    "但我现在就算饿了也不会因为头疼而困扰，毕竟我已经习惯头疼了，这到底是好事还是坏事呢。"
    "…现在点外卖的话，应该还能送过来吧…"
    if not replaying:
        $Notice.add('精神状态恢复率提升了5%。')
        $p.basicRecovery += 0.05
        $Notice.show()
    "算了，省一顿是一顿，睡睡觉就不饿了。"

    stop music fadeout 5

    $end_plot()
    if replaying:
        jump afterreplay
    $p.s8=True
    $Achievement205.achieve()
    $Notice.show()
    jump dayEnd