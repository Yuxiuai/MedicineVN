label DefaultRead_beginning:
    scene workarea with fade
    "看看时下比较流行的小说吧，说不定能获得什么灵感……"
    call Task_processing from _call_Task_processing_16
    $p.times+=1
    $DefaultRead.executeTask(p)

label DefaultRead_result_exce:
    scene workarea with fade
    $Notice.show()
    "我看了这部小说的唯一念头就是。"
    "写的这么牛逼，卧槽。"
    $p.times+=1
    jump TaskExecuting

label DefaultRead_result_good:
    scene workarea with fade
    $Notice.show()
    "一本不错的小说能给读者带来灵感。"
    "或许里面的对剧情的处理方式可以让我借鉴一下。"
    $p.times+=1
    jump TaskExecuting

label DefaultRead_result_norm:
    scene workarea with fade
    $Notice.show()
    "看完了，感觉只是比较普通的那种小说。"
    "至于有没有对我有什么影响，就看未来我会不会想起来这本书的内容了吧。"
    $p.times+=1
    jump TaskExecuting

label DefaultRead_result_bad:
    scene workarea with fade
    $Notice.show()
    "老套庸俗的小说。"
    "讲述了主角在朋友们的帮助下取得了美好人生的故事。"
    "很无聊，但是装帧简约精美，也许主创应该换一个创作的角度？"
    "……不论怎样，这本书都刚刚登上畅销榜。"
    $p.times+=1
    jump TaskExecuting






label SentimentalRead_beginning:
    scene workarea with fade
    "听说这本小说在圈子里有很多很好的评价，有很多刀子……什么的。"
    "浅尝一下吧，让我看看是不是真有那么刀……"
    call Task_processing from _call_Task_processing_17
    $p.times+=1
    $SentimentalRead.executeTask(p)

label SentimentalRead_result_exce:
    scene workarea with fade
    $Notice.show()
    "好久没读到过这种能够影响我情绪的小说了……"
    "主角好可怜，我什么时候能写出这样可歌可泣的主人公呢？"
    $p.times+=1
    jump TaskExecuting

label SentimentalRead_result_good:
    scene workarea with fade
    $Notice.show()
    "刀子就应该这样写才对嘛……"
    "可惜的是现在大部分小说都没有这篇的功底。"
    "这算是自嘲吧，真让人难过。"
    $p.times+=1
    jump TaskExecuting

label SentimentalRead_result_norm:
    scene workarea with fade
    $Notice.show()
    "看完了……"
    "我并不能感觉到全篇的感情，或许他确实没有击中我的泪点？"
    $p.times+=1
    jump TaskExecuting

label SentimentalRead_result_bad:
    scene workarea with fade
    $Notice.show()
    "一本无法评价的书。"
    "或许只是流水账罢了，它怎么配得上伤感这个词呢，不过确实让我休息了一会——毕竟我读的都睡着了。"
    $p.times+=1
    jump TaskExecuting




label TraditionalRead_beginning:
    scene workarea with fade
    "听说这本小说在圈子里有很多很好的评价，使用了偏近代文学的手法……"
    "浅尝一下吧，让我看看是不是真有那么好……"
    call Task_processing from _call_Task_processing_18
    $p.times+=1
    $TraditionalRead.executeTask(p)

label TraditionalRead_result_exce:
    scene workarea with fade
    $Notice.show()
    "笔调冷峻，字里行间透露出讽刺的意味。"
    "语言质朴无华，十分平实，但形象生动……"
    "不错的小说，感觉回到了几十年前……"
    $p.times+=1
    jump TaskExecuting

label TraditionalRead_result_good:
    scene workarea with fade
    $Notice.show()
    "看起来有点平淡，但是我大概理解了作者想要表达什么。"
    "总体来说还是挺棒的故事。"
    $p.times+=1
    jump TaskExecuting

label TraditionalRead_result_norm:
    scene workarea with fade
    $Notice.show()
    "看完了……"
    "或许是我的水平不够，我并没有感受到那种读近代小说的感觉……"
    "今天就读到这里吧。"
    $p.times+=1
    jump TaskExecuting

label TraditionalRead_result_bad:
    scene workarea with fade
    $Notice.show()
    "看不懂……"
    "头好痛，这本书的人物关系和名称又复杂又多变……"
    "就不该看这东西……"
    $p.times+=1
    jump TaskExecuting





label FreewheelingWriting_beginning:
    scene workarea with fade
    "超降噪耳机准备完毕——"
    "白噪音歌单就绪——"
    "手机关机——"
    "写作是表达想法的手段，以这种方式表达一些有趣的灵感是一种放松的手段……"
    "就写点之前一直没写过的那个好了……"
    call screen screen_tr_commission_inputs(p)
    call Task_processing from _call_Task_processing_19
    $p.times+=1
    $FreewheelingWriting.executeTask(p)

label FreewheelingWriting_result_exce:
    scene workarea with fade
    $Notice.show()
    "简直像是灵感迸发！文思泉涌行云流水妙笔生花奋笔疾书学富五车！"
    "我想这篇文章大概能被《文学》刊登，如果它不是一篇小黄文的话。"
    $p.times+=1
    jump TaskExecuting

label FreewheelingWriting_result_good:
    scene workarea with fade
    $Notice.show()
    "或许我有新的点子了。"
    "至少是一篇能看的文，也许应该再修饰一下。"
    "得慢慢雕磨才行。"
    $p.times+=1
    jump TaskExecuting

label FreewheelingWriting_result_norm:
    scene workarea with fade
    $Notice.show()
    "一次随笔，或许大概是记录日常生活的那种？"
    "总之不是很重要的内容罢了，随便写一写"
    $p.times+=1
    jump TaskExecuting

label FreewheelingWriting_result_bad:
    scene workarea with fade
    $Notice.show()
    "胡乱的文字组成不通顺的语句。"
    "至少未来可以来翻一翻我现在的所思所想。"
    "好烦，就这样吧，把笔放下然后去做其他事情。"
    $p.times+=1
    jump TaskExecuting




label NormalWriting_beginning:
    scene workarea with fade
    "该写委托了。"
    "写哪个委托？"
    call screen screen_tr_commission(p)
    if p.retval is not None:
        "那就这个好了。"
        call screen screen_tr_commission_inputs(p)
        call Task_processing from _call_Task_processing_20
        $p.times+=1
        $NormalWriting.executeTask(p)
    else:
        "下次再写吧，摸会鱼去。"
        $Notice.show()
        $p.times+=2
        jump TaskExecuting

label NormalWriting_result_exce:
    scene workarea with fade
    $Notice.show()
    "一篇堪称完美的委托！"
    "我想金主看完一定会给我多打些小费的！"
    $p.times+=1
    jump TaskExecuting

label NormalWriting_result_good:
    scene workarea with fade
    $Notice.show()
    "在练习的基础上完成的作品。"
    "离完美只差一步，但是也很令人满意了。"
    "以后要保持这样的水平呢。"
    $p.times+=1
    jump TaskExecuting

label NormalWriting_result_norm:
    scene workarea with fade
    $Notice.show()
    "完成了委托。"
    "或许得再练习一下，虽然看起来没什么大问题，但是一些地方的措辞还是很奇怪。"
    "不过，只要金主不发现就没事啦～"
    $p.times+=1
    jump TaskExecuting

label NormalWriting_result_bad:
    scene workarea with fade
    $Notice.show()
    "不太想写……灵感不够，就单纯的凑一凑字数吧……"
    "过一会再来改吧……现在该做其他事情了……"
    $p.times+=1
    jump TaskExecuting




label FocusWriting_beginning:
    scene workarea with fade
    "要稍微认真对待一下了。"
    "写哪个委托？"
    call screen screen_tr_commission(p)
    if p.retval is not None:
        "那就这个好了。"
        call screen screen_tr_commission_inputs(p)
        call Task_processing from _call_Task_processing_21
        $p.times+=1
        $FocusWriting.executeTask(p)
    else:
        "……扫兴。"
        $Notice.show()
        $p.times+=2
        jump TaskExecuting

label FocusWriting_result_exce:
    scene workarea with fade
    $Notice.show()
    "这样认真写作的时光十分短暂。"
    "但是十分有利于我提升自己的写作水平，哦，还有这个……应该这样写。"
    $p.times+=1
    jump TaskExecuting

label FocusWriting_result_good:
    scene workarea with fade
    $Notice.show()
    "运用之前积累的写作技巧来写一篇文章还是挺费脑子的。"
    "不过这样不是挺好的吗？也确实得到了一些进步。"
    $p.times+=1
    jump TaskExecuting

label FocusWriting_result_norm:
    scene workarea with fade
    $Notice.show()
    "一次写作锻炼，大概会让我的写作水平有一个量的提升……吧。"
    "不过其实强度也没有当年写毕业论文那么高啦，洒洒水啦。"
    $p.times+=1
    jump TaskExecuting

label FocusWriting_result_bad:
    scene workarea with fade
    $Notice.show()
    "这样消耗脑力的工作还是少做……"
    "真是太消耗精力了，在头疼的时候写作带来的收益真的太小了……"
    $p.times+=1
    jump TaskExecuting




label ReadingBook_beginning:
    scene workarea with fade
    "买来的书也确实堆在书架上好久了，现在就看一看好了。"
    "选哪本看呢？"
    call screen screen_tr_readingbook(p)
    if p.retval is not None:
        "那就看这本书好了。"
        call Task_processing from _call_Task_processing_22
        $p.times+=1
        $ReadingBook.executeTask(p)
    else:
        "算了，突然又不是很想看书了，摸会鱼去。"
        $Notice.show()
        $p.times+=2
        jump TaskExecuting
    

label ReadingBook_result_exce:
    scene workarea with fade
    $Notice.show()
    "比平时读到的小说有趣得多，也学到了很多东西。"
    $p.times+=1
    jump TaskExecuting

label ReadingBook_result_good:
    scene workarea with fade
    $Notice.show()
    "或许我该买些新书了，这些看过的并不能让我提起什么兴趣……"
    $p.times+=1
    jump TaskExecuting

label ReadingBook_result_norm:
    scene workarea with fade
    $Notice.show()
    "或许我该买些新书了，这些看过的并不能让我提起什么兴趣……"
    $p.times+=1
    jump TaskExecuting

label ReadingBook_result_bad:
    scene workarea with fade
    $Notice.show()
    "把书盖在脸上睡觉的日子一去不复返啦——不过我现在还是很享受看书的时光的。"
    $p.times+=1
    jump TaskExecuting



label WriteDownInspiration_beginning:
    scene workarea with fade
    "稍微整理一下脑袋里的想法好了……用在之后的委托里。"
    call Task_processing from _call_Task_processing_23
    $p.times+=1
    $WriteDownInspiration.executeTask(p)

label WriteDownInspiration_result_exce:
    scene workarea with fade
    $Notice.show()
    "……一个流落外乡的中世纪王子，他对真实的世界一无所知却又过分自信，稚气未脱地放纵自己的行为，主观臆断别人好坏，漠视别人的付出……"
    "……最后当他后悔时，即便神明给他时空穿越的能力，也难以逃离命运的玩弄，最终无力地溺死在无法挽回的现实之中……"
    "……"
    "这个题材不错，以此写一篇小说吧。"
    $p.times+=1
    jump TaskExecuting

label WriteDownInspiration_result_good:
    scene workarea with fade
    $Notice.show()
    "……一个生活在大都市的平凡社畜，他十分热心想去帮助别人，因为他自己被病痛折磨，所以希望别人也不要像他那样痛苦……"
    "……他享受孤独，却又不甘于孤独，他渴望建立关系，即便他与所谓爱人的身体和心只差零点几公分的距离，却仍然如同相隔万里的两座孤岛……"
    "……"
    "这个题材不错，以此写一篇小说吧。"
    $p.times+=1
    jump TaskExecuting

label WriteDownInspiration_result_norm:
    scene workarea with fade
    $Notice.show()
    "……一个穿越时空到魔幻世界的现代高中生，当他意识到自己穿越到rpg世界时狂喜不已，但真实的生命和刀剑，死亡和苦难都不是电子游戏轻描淡写出的那副样子的……"
    "……他渴望别人的帮助，但这样做却频频连累了他人，孤身一人的他来到最终Boss面前时，迎接他的居然是……"
    "……"
    "这个题材不错，以此写一篇小说吧。"
    $p.times+=1
    jump TaskExecuting

label WriteDownInspiration_result_bad:
    scene workarea with fade
    $Notice.show()
    "总觉得好像忘记了一些十分优秀的题材……是什么来着？"
    $p.times+=1
    jump TaskExecuting