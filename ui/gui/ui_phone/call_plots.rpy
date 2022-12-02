label end_call:
    if p.times == 11:
        $p.times = 10
    $renpy.sound.stop(channel="chara_voice")
    call screen screen_index(p)
    hide screen info
    hide screen info2
    hide screen info3
    $p.times+=1
    jump TaskExecuting


label call_parents:
    if p.hadAskedForMoney:
        "算了……"
        "我已经管他们要过钱了。"
    elif p.meds()*p.price+p.money>500:
        "没什么必要还是不要给他们打电话了……"
    else:
        stop music fadeout 5
        "拨通了电话……"
        "……"
        mom"“[p.name]！好久没听到你声音啦！”"
        dad"“你在大城市找了份好工作啊，不愧是我的好儿子。”"
        dad"“爸爸妈妈在家里过的很好，开了一家超市，平时卖一些烟酒零食，也能养活得起自己，不用担心我们啦！”"
        mom"“是啊，我和你爸现在的日子过得很好，你只需要在那边好好上班，养活好自己就行啦！”"
        mom"“过年还回来不？啥时候找个女朋友啊？”"
        dad"“哎呀，你少说几句吧，不然他又不乐意了。”"
        mom"“宝贝打电话给爸妈有什么事呀？心情不好也可以来和妈聊聊，你都挺长时间没和我们说点啥了！”"
        menu:
            "要钱":
                mom"“啊……是这个事啊。”"
                mom"“你在那边工作困难的话，尽管和我们要钱就是，要是丢了工作或者受了欺负，就回家里就行。”"
                mom"“钱打过去了，爸妈不在你身边，你已经是个大人了，在那边照顾好自己啊。”"
                if p.onVacation:
                    $temp = 'normal2_eyebrow'
                else:
                    $temp = 'normal2_eyebrow glasses white no_hat'
                $ss(temp)
                s"“嗯，没什么事我就挂了。”"
                $sh()
                mom"“妈啥也不懂，也就不多问了，怕你被我们问得烦。”"
                mom"“有啥事下次再打电话给我们啊。”"
                if p.onVacation:
                    $temp = 'sad_eyebrow'
                else:
                    $temp = 'sad_eyebrow glasses white no_hat'
                $ss(temp)
                s"“嗯。”"
                $sh()
                play sound audio.interruption
                "……挂断了电话。"
                $p.hadAskedForMoney = True
                $p.money += 2000.0
                $showNotice(['X付宝到账：2000元！'])
    jump end_call

label call_Arnel:
    if p.onVacation:
        "放假了还给他打电话干什么……"
        jump end_call
    if p.times != 2:
        "这个时间给他打电话干什么……要请假还是早上请假好了……"
        jump end_call
    if p.hal_p == 11 and p.today == 6:
        "虽然这个时候要加班肯定是很重要的事情吧……"
        "我可不想因为这种事被那家伙骂一顿……"
        "……"
        "Halluke会原谅我的吧。"
        jump end_call
    "给Arnel打电话。"
    "……"
    ar"“干嘛？又想请假？”"
    jump arnel_q


label arnel_q:
    menu:
        ar"“干嘛？又想请假？”{fast}"
        "请假":
            if p.hadAskedForLeave:
                ar"“你这周不是请过假了吗？”"
                ar"“我看你的工作也没完成多少啊，这么喜欢在家呆着那就去人事处办一下辞职手续吧？”"
                $ss('glasses white no_hat scared_eyebrow awkward_mouth')
                s"“……不……不用了……”"
                $sh()
                ar"“有话快说，我还忙着呢。”"
                jump arnel_q
            $ss('glasses white no_hat normal2_eyebrow smile_eyes awkward_mouth sweat')
            s"“是。”"
            $sh()
            ar"“请假回家睡觉？这样你就不会把口水流到桌子上了，噗哈哈哈。”"
            ar"“请呗？都可以请。”"
            ar"“不过公司不养闲人，也不养在工位上睡觉的人，你要干什么随你便，但是得在周五之前把该干的都给我干完了。”"
            ar"“公司不缺新员工，完不成工作就给我卷铺盖走人。”"
            $ss('glasses white no_hat sad_eyebrow sweat mood')
            s"“说得是说得是……”"
            $sh()
            $ss('glasses white no_hat sad_eyebrow sad_eyes awkward_mouth sweat mood')
            ar"“你这周的工资我已经给你扣了，建议你回去之后有时间把留给你们小组的那几个客户需求都给我写得明明白白的，好自为之吧。”"
            $sh()
            s"“嗯。”"
            "挂断了电话。"
            "呼，可以回家歇一会了。"
            "……"
            
            scene workarea with fade  
            $p.wages = r2(p.wages * 0.9)
            $p.onVacation = True
            $p.stime(55)
            $p.checkTask()
            $p.hadAskedForLeave = True
            $routineMusic(p)
            "光速打车回家了……"
            jump end_call
        "闲聊":
            $ss('glasses white no_hat sad_eyebrow sad_eyes sweat mood blush')
            s"“那个……最近我……在工位上睡觉的事……”"
            $sh()
            ar"“你给我打电话就因为这个？”"
            ar"“说些有用的吧。”"
            jump arnel_q
        "薪资问题":
            ar"“突然问我这个，是想好好工作了吗？”"
            ar"“虽然也指望不上你能超额帮组内分担任务，但是你能问我这个还是让我比较开心。”"
            ar"“那就来谈谈我们的完成度和薪资关系吧？”"
            ar"“超额完成任务时（>=120\%），必定获得成就感，具体薪水为当前面板薪水*完成度*1.1，并额外获得50~200块奖金，下周工资为2000*1.05^周数。”"
            ar"“正常完成任务时（>=100\%），75\%获得成就感，具体薪水为当前面板薪水*完成度，并额外获得0~50块奖金，下周工资为2000*1.03^周数。”"
            ar"“勉强算完成任务时（>=80\%），具体薪水为当前面板薪水*完成度*0.8，下周工资为1900*1.01^周数。”"
            ar"“完成半数任务时（>=50\%），具体薪水为当前面板薪水*完成度*0.6，下周工资为1900*1.00^周数。”"
            ar"“没有完成任务时（<50\%），具体薪水为当前面板薪水*完成度*0.55，下周工资为1900*1.00^周数。”"
            ar"“总结一下就是，尽量完成的越多越好，虽然这句话和废话一样就是了，但完成度超过120\%就可以稍微放松下，毕竟不能把你累死了。”"
            ar"“另外就是，下一周的工资和本周工资关系并不是太大，如果上周工资很少，只要这周努力点，很快就能恢复正常水平。”"
            ar"“就是这样。”"
            ar"“还有什么想问的吗？”"
            jump arnel_q
        "调情":
            $ss('glasses white no_hat')
            s"“……”"
            $ss('glasses white no_hat scared_mouth normal2_eyes awkward_eyebrow')
            s"“……那个。”"
            $ss('glasses white no_hat smile_mouth smile_eyes smile_eyebrow blush')
            s"“今晚有时间和我出来吃个晚饭吗？”"
            $sh()
            $temp=rd(0,13)
            if temp==0:
                ar"“你把你的活都干完了再约我出门吧。”"
            if temp==1:
                ar"“哟，你不是应该很讨厌我吗？”"
                ar"“想不到你也会对我感兴趣啊啊哈哈哈……”"
                ar"“等你长大一点再来约我吃饭吧？”"
            if temp==2:
                ar"“想透我？”"
            if temp==3:
                ar"“有时候看到你请假直接跑去医院，是不是就是着急治脑子啊？”"
            if temp==4:
                ar"“好了，再说就烦了。”"
            if temp==5:
                ar"“说点有用的行吗？”"
            if temp==6:
                ar"“你觉得现在是聊这个的时候吗？”"
            if temp==7:
                ar"“你认真的？”"
                ar"“带我吃楼下的麻辣烫还是扬州炒面啊？”"
            if temp==8:
                ar"“……别吧？”"
            if temp==9:
                ar"“无语，你是不是没事闲的啊。”"
            if temp==10:
                ar"“你给我打电话不会就因为这个吧？”"
            if temp==11:
                ar"“我还不如从咱们的楼层直接跳下去。”"
            if temp==12:
                ar"“呃，你是不是有病啊？”"
            if temp==13:
                ar"“公司帮你缴的电话费不是为了让你打电话和我开玩笑的。”"
            $ss('glasses white no_hat normal2_eyes mood')
            s"“呃……”"
            $sh()
            "我为什么要和这家伙聊这么久……"
            jump arnel_q
        "结束通话":
            $ss('glasses white no_hat normal_eyes mood')
            s"“那个，也没什么事了……”"
            $sh()
            ar"“下次想清楚了自己想说什么再打。”"
            $ss('glasses white no_hat normal_eyes sweat')
            s"“抱歉……”"
            $sh()
            play sound audio.interruption
            "电话中响起嘟嘟声。"
            jump end_call

label call_Pathos:
    "给Pathos打电话。"
    "……"
    pathos"“是我，有什么想问的就说吧，我赶时间。”"
    jump pathos_q


label pathos_q:
    $clothes = ''
    if not p.onVacation:
        $clothes = 'glasses white no_hat '
    
    menu:
        pathos"“是我，有什么想问的就说吧，我赶时间。”{fast}"
        "关于药物使用的疑问":
            pathos"“我就知道你没听我说话，算了，谁让我是你的专属医生呢？”"
            pathos"“使用一次药物后，再次使用相同的药物会降低恢复效率到33\%，使用其他的药物会降低恢复效率到50\%。”"
            pathos"“而隔一段时间后（再一次看到菜单界面），再次使用相同的药物会降低恢复效率到66\%，其他种类的药物的使用效率就不会被降低了。”"
            pathos"“再过一段时间，你就可以使用之前的药物了。”"
            pathos"“举个例子，早上吃，下午可以再吃；上午吃，睡前可以再吃；如果下午吃了，晚上就只能吃其他种类的药了。”"
            pathos"“不过例外的是，如果你晚上吃药，第二天早上不会受影响。”"
            pathos"“总之自己探索吧，有很多信息可以自己查看，不懂就问问别人？”"
            pathos"“哦，我差点忘了，似乎全球只有你有这种病。”"
            pathos"“还有什么想问的吗？”"
            jump pathos_q
        "生病相关的疑问":
            pathos"“你是刚出生的孩子吗？这都不懂？”"
            pathos"“算了，可能吃那种药把你脑子都吃坏了。”"
            pathos"“首先生病的来源有两个，一个是平时工作太多，过劳的层数过多，也就是4层及以上，在第二天就会转化成生病。”"
            pathos"“另一个是阴冷天气，如果身体平时不多运动，很容易着凉感冒。”"
            pathos"“生病会降低基础属性，也会影响精神状态的消耗恢复和专注度等，尽量避免生病。”"
            pathos"“可以花一笔钱去医院治疗，越早越花的钱越少。”"
            pathos"“但如果生病了的话，也并不一定是坏事。”"
            pathos"“另一种恢复方法便是在床上休息来恢复，以这种方法恢复不仅能重新获得失去的基础属性，还能根据体魄层数获得恢复奖励。”"
            pathos"“消耗良好的运动和良好的睡眠等来提高恢复率，阴天也能让恢复率提升。”"
            pathos"“吃感冒药可以延长生病的时间来减缓病情，每天一片，能够按层数来增加休息治疗的概率。”"
            pathos"“受伤也能根据这个方法来恢复，但是偏执不能靠休息恢复。”"
            pathos"“还有什么想问的吗？”"
            jump pathos_q
        "伤痕相关的疑问":
            pathos"“如果不去管生病的话，病情会恶化直到自愈，但是会给身体留下不可逆的损伤。”"
            pathos"“体弱会百分比降低属性，尽量不要获得。”"
            pathos"“另外有时候会莫名其妙多出来伤痕，可能是因为灵感过剩和酸痛堆积导致的，要经常关注一下自己的身体状况哦。”"
            pathos"“还有什么想问的吗？”"
            jump pathos_q
        "实验药物保质期相关的疑问":
            pathos"“为什么保质期只有一周？”"
            pathos"“……这个，以后会告诉你的。”"
            pathos"“现在你还不需要知道。”"
            pathos"“还有什么想问的吗？”"
            jump pathos_q
        "普通药物相关的疑问":
            pathos"“普通药物啊……就是普通人也会吃的那些药咯。”"
            pathos"“你所服用的实验药物都是快速见效的那种，正常人吃的药对你来说不仅恢复力弱，见效也慢。”"
            pathos"“反正具体效果自己看说明书吧，要遵循用法用量，一次性吃太多小心第二天下不来床哦。”"
            pathos"“如果你喜欢就去药房买点，我已经和下面的人说过了，你买什么处方药都不需要医嘱，只是不要买太多就行。”"
            pathos"“还有什么想问的吗？”"
            jump pathos_q
        "调情":

            $ss(clothes)
            s"“……”"
            $ss(clothes+'scared_mouth normal2_eyes awkward_eyebrow')
            s"“……那个。”"
            $ss(clothes+'smile_mouth smile_eyes smile_eyebrow blush')
            s"“今晚有时间和我出来吃个晚饭吗？”"
            $sh()
            $temp=rd(0,13)
            if temp==0:
                pathos"“没时间。”"
            if temp==1:
                pathos"“下次。”"
                pathos"“最近很忙。”"
            if temp==2:
                pathos"“我今晚有约了。”"
            if temp==3:
                pathos"“如果你的精神状态还算良好，就不要对你的主治医师发情了。”"
            if temp==4:
                pathos"“其实我有男朋友的。”"
                pathos"“他今晚好不容易有时间陪我。”"
            if temp==5:
                pathos"“我拒绝。”"
            if temp==6:
                pathos"“没兴趣。”"
            if temp==7:
                pathos"“今天不行。”"
            if temp==8:
                pathos"“……”"
            if temp==9:
                pathos"“你没有其他的事可以做了吗？”"
            if temp==10:
                pathos"“别开玩笑，严肃点。”"
            if temp==11:
                pathos"“下次下次。”"
            if temp==12:
                pathos"“唉，我现在可是在上班时间诶，能不能说点正经的？”"
            if temp==13:
                pathos"“下次你这样我就要收费了。”"
            $ss(clothes+'sweat')
            s"“好吧。”"
            $sh()
            jump pathos_q
        "结束通话":
            $ss(clothes+'normal2_eyes')
            s"“没什么想问的了。”"
            $sh()
            pathos"“耽误我这么久连句谢谢都没有？”"
            $ss(clothes+'sweat awkward_eyes awkward_eyebrow')
            s"“无语……”"
            $sh()
            pathos"“呵呵。”"
            play sound audio.interruption
            "我挂断了电话。"
            jump end_call



label call_Halluke:
    "给Halluke打电话。"
    "……"
    if p.hal_p == 11 and p.today == 6:
        play sound audio.interruption
        "他挂断了电话。"
        jump end_call
    elif p.hal_p > 90:
        stop music
        "“对不起，您拨打的电话是空号。”"
        play sound audio.interruption
        "……"
        jump end_call

    elif not (p.times >= 10 or p.today in (6, 7)):
        play sound audio.interruption
        "他挂断了电话。"
        "可能他还在上课吧？晚上或者周末再打给他吧。"
        jump end_call
    h"“诶，是[p.name]啊，是很紧急的事对吧？”"
    jump halluke_q


label halluke_q:
    $clothes = ''
    if not p.onVacation:
        $clothes = 'glasses white no_hat '
    menu:
        "想了解你更多一点":
            h"“诶……什么……”"
            h"“那个……其实……我不是很擅长……自我介绍……”"
            h"“咳咳，我是Halluke，种族是白熊，20岁，身高是15……不对，自我介绍里好像不需要说这个吧？”"
            h"“现在就读于A市大学计算机系，擅长的运动和爱好都是打羽毛球。”"
            h"“日常的我会因为紧张，不知道如何开口，但在手机上或者文字上就会好一点。”"
            h"“我也很喜欢和别人一起打球……”"
            h"“如果你周六陪我打球的话，我会很开心哦……”"
            h"“[p.name]如果周六比较累的话也没关系哦，下一周再陪我打也好诶……”"
            jump halluke_q
        "运动方面的建议":
            h"“哦哦，你问其他的我可能没有很厉害啦，但是运动我还是了解一些的……”"
            h"“身体素质能够降低每天起床时消耗的精神状态，还能让进行日程的时候消耗的精神状态降低，恢复的精神状态变高。”"
            h"“可以认为是和严重程度相拮抗的属性！”"
            h"“关于运动的重要属性是酸痛和体魄！酸痛虽然是负面的状态，但可以通过拉伸运动转化为十分强力的体魄。”"
            h"“体魄会在每天起床时根据层数恢复很多精神状态，而且还能被动提升身体素质，增加治愈生病和受伤的恢复率，还能提升治愈的奖励等等……”"
            h"“总之是很厉害的东西哦。”"
            h"“我最近正好选修了一门和这个有关的课程，书上是这么说的……。”"
            h"“不过“身体素质”，“精神状态”，“体魄”这些东西……到底是什么呢……”"
            jump halluke_q
        "该选择什么样的运动":
            h"“如果你也想开始锻炼身体的话，我建议先从坚持每天走路开始哦。”"
            h"“等走几千步脚也不会很酸的时候，就去试试慢跑和速跑吧？”"
            h"“慢跑能够放松身心，而速跑可以快速提高身体素质。”"
            h"“如果你觉得跑步也不够了，可以试试去健身房！里面有很多种器械，你可以根据自己想要的效果来选择。”"
            h"“具体效果快速放松，快速增加酸痛，快速提升身体素质，甚至直接获取体魄……等等器械，有很多不同的器械可以选择。”"
            h"“但是最大的问题在于，越是难度高的运动越容易受伤，从15\%~90\%不等。”"
            h"“好消息是这些概率可以被专注度以加算形式降低，需要较高的身体素质来提升运动的专注度，还有各种状态等等……”"
            h"“受伤了也不要担心！多休息，读一些和受伤恢复相关的书，获得的奖励或许比正常运动还要多！”"
            jump halluke_q
        "随便聊聊":
            $talk = rd(1, p.hal_p)
            if talk == 1:
                h"“喜欢羽毛球大概也只是因为自己身体太小没法上足球场，篮球场这样的地方吧？”"
                h"“好像很危险的样子。”"
            if talk == 2:
                h"“关于我的家人吗……我不是很想聊他们……”"
            if talk == 3:
                h"“上次课又被老师表扬了……”"
                h"“哎呀，如果是你的话，努力一点应该也会被表扬的！”"
            if talk == 4:
                h"“我经常和其他班的人打球？哦……那些人是隔壁班的打球比较厉害的……”"
                h"“不过其实也不是我去主动认识他们的，和你一样，他们是把我“捡走”的。”"
            if talk == 5:
                h"“啊……想打球了……但是作业还没写完……”"
                h"“其实我学习成绩没有很好哦，其实我偶尔也会玩点养成类的单机游戏……”"
            if talk == 6:
                h"“在大学的生活其实还好……没有想象中的很差劲的室友，课程也不是很满，也没有什么无聊的社团啊强制参加的活动之类的……”"
                h"“嘿嘿……”"
            if talk == 7:
                h"“抱歉……我……在现实里……说话经常那样，但我在打电话的时候要比现实见面好得多……”"
                h"“请不要在意那些事，你的羽毛球打得很棒哦。”"
            if talk == 8:
                h"“下次再打球的时候要记得带水哦，不然很容易脱水的，你可别觉得我在吓唬你……”"
            if talk == 9:
                h"“衣服都快给我拽掉了……下次一定要让你好好赔我一件！”"
            if talk == 10:
                h"“那个……冰淇淋……很好吃……谢谢你……”"
            if talk == 11:
                h"“体育课这么快就要结课了……在那之后体育馆好像也要重新维修的样子……”"
                h"“总之，周六一定要来哦……”"
            if talk >= 12:
                h"“那个……周末……要出来吃点什么吗……”"
                h"“[p.name]……我们很久没见了吧？没有很久？但我感觉好想你哦……”"
            jump halluke_q
        "调情":
            $ss(clothes)
            s"“……”"
            $ss(clothes+'scared_mouth normal2_eyes awkward_eyebrow')
            s"“……那个。”"
            $ss(clothes+'smile_mouth smile_eyes smile_eyebrow blush')
            s"“今晚有时间和我出来吃个晚饭吗？”"
            $sh()
            $temp=rd(0,7)
            if temp==0:
                h"“哎呀，今天好像不行诶……”"
            if temp==1:
                h"“今晚有课……要不明天再说吧？”"
            if temp==2:
                h"“不行……我的作业马上就要交了……我还没写……”"
            if temp==3:
                h"“诶？”"
            if temp==4:
                h"“噢啊……我也想出来吃点东西，但我已经吃过了。”"
            if temp==5:
                h"“我本来是有时间的！但是我被辅导员抓来看讲座了……”"
            if temp==6:
                h"“抱歉，我吃过饭了诶。”"
            if temp==7:
                h"“今晚不太饿，明晚吧？”"
            $ss(clothes+'sweat')
            s"“好吧。”"
            $sh()
            jump halluke_q
        "结束通话":
            $ss(clothes+'normal2_eyes')
            s"“其实……也没什么事啦~”"
            $sh()
            h"“这样啊……如果想找我的话，发某信就好了嘛……”"
            $ss(clothes+'smile_eyebrow smile_mouth happy')
            s"“嗯嗯……好……”"
            $sh()
            h"“下次的体育课你还来吗？这周六也来打羽毛球吗？”"
            $ss(clothes+'scared_eyebrow smile_eyes smile_mouth blush')
            s"“当然来呀。”"
            $sh()
            h"“额嘿嘿……好……”"
            h"“那我先挂了，我要看书去了……”"
            $ss(clothes+'smile_eyebrow smile_mouth')
            s"“嗯嗯……”"
            $sh()
            play sound audio.interruption
            "他挂断了电话。"
            jump end_call




label call_Acolas:
    "给Acolas打电话。"
    "……"
    if p.aco_p in (9, 10, 11):
        play sound audio.interruption
        "他挂断了电话。"
        jump end_call
    elif p.aco_p > 90:
        stop music
        "“对不起，您拨打的电话是空号。”"
        play sound audio.interruption
        "……"
        jump end_call

    elif not (p.times >= 10 or p.today in (6, 7)):
        play sound audio.interruption
        "他挂断了电话。"
        "现在是上班时间……晚上或者周末再打给他吧。"
        jump end_call

    a"“[p.name]？有什么事吗？”"
    jump acolas_q


label acolas_q:
    $clothes = ''
    if not p.onVacation:
        $clothes = 'glasses white no_hat '
    menu:
        "想了解你更多一点":
            a"“了解我？”"
            a"“我现在是这家公司的属于你们部门的技术总监，也算你的上司吧？”"
            a"“名字是Acolas，25岁，灰狼……”"
            a"“身高？哎呀，这都被你发现我1米83啦？”"
            a"“爱好是喜欢工作，冷门动漫和手办收集，也喜欢健身和去不同的小吃店尝鲜。”"
            a"“[p.name]这周的工作有好好做吗？虽然已经下班了但是我还是想了解一下你的进度哦？开玩笑的。”"
            a"“如果你想我了，就每周都去参加一下周会议吧？”"
            jump acolas_q
        "工作方面的建议":
            a"“关于工作，能聊的就多了。”"
            a"“工作能力能够提高每周获得的工资，也能增加工作时完成的工作进度和专注度。”"
            a"“如果工作能力太低，可能会完不成每周的任务，就会被扣工资，结果很恐怖的。”"
            a"“虽然工作能力只能增强工作方面，但毕竟你每周要做的事情里，工作应该占了很大部分，而且你还要为此赚钱。”"
            a"“虽然只要一直兢兢业业工作，不刻意旷工或者过多地偷懒，是不需要刻意去通过读书来提升工作能力的。”"
            jump acolas_q
        "该怎样进行工作":
            a"“我知道你经常上班摸鱼……虽然我不支持这种行为，但是如果你实在很累的话，适当摸鱼也是可以的。”"
            a"“在偷懒中可以做很多事，这允许你在工作日期间锻炼身体，练习写作，甚至读书。”"
            a"“最主要的应该也是读书了，书本能带来很多增益，但在家里的时间很宝贵，所以把书拿到公司来看也不是不能被接受。”"
            a"“另外，公司里似乎很流行一种……先在工位上睡一上午，午休结束后一直发疯工作到下班……。”"
            a"“看上去似乎比正常上班更有效率？但我好像不适合这种方法。”"
            jump acolas_q
        "每周会议是做什么的":
            a"“你应该比我还清楚吧？毕竟我才刚到这个公司，而你已经在这里工作有一段时间了吧……”"
            a"“不过你应该是想听听我的看法，好吧，那我就大概讲一下。”"
            a"“每周会议只在每周五的下午才能进行，能够以相对于工作更低的精神状态，获得更多的工作能力。”"
            a"“但最重要的是，会议会带来不同的效果。”"
            a"“全面的比如提升你的工作速度、提升你的工作能力……”"
            a"“也有提升你在偷懒时恢复的精神状态的，甚至有能让你在偷懒时看书速度翻倍的效果……”"
            a"“效果强力，但完全随机……持续时间也是比较随机。”"
            a"“除非你完全不想见到我，不然我还是建议每周都去会议。”"
            jump acolas_q
        "随便聊聊":
            $talk = rd(1, p.aco_p)
            if talk == 1:
                a"“没什么特别的事的话我就先去工作了。”"
            if talk == 2:
                a"“关于我的小时候？……以后再讲给你听吧……”"
            if talk == 3:
                a"“是啊……是很喜欢你的……”"
                a"“为什么？喜欢不需要原因哦。”"
            if talk == 4:
                a"“想吃火锅了吗？”"
                a"“等下次我们再在会上被表扬的时候我们就去吃吧？”"
            if talk == 5:
                a"“嗯……虽然我写代码很快，但其实没有你想的那么辛苦。”"
                a"“就像是画家画画，虽然有不喜欢画画的画家，但也存在热爱画画的画家啊？”"
            if talk == 6:
                a"“等哪天带你去尝尝咖啡营地的早餐吧？”"
                a"“感觉你每天早上状态都不是很好的样子，早餐也都是点一些乱七八糟的外卖……”"
            if talk == 7:
                a"“抱歉……让你担心了吧？”"
                a"“但我真的没关系的。”"
            if talk == 8:
                a"“好想你……真的……。”"
                a"“好像我们有段时间没见了吧……”"
            if talk == 9:
                a"“我喜欢的动漫吗……”"
                a"“最近在看一款名叫《城堡与莫梭提斯》的动漫，还没看到结局，但总觉得会发生什么不好的事……”"
            if talk == 10:
                a"“你可要好好对待我的笔记本哦……”"
                a"“按某人的说法，我把记录了这么多东西的本子送给你，就像送钻戒一样珍贵……”"
            if talk >= 11:
                a"“抱歉，我不是很喜欢被人打搅工作……”"
                a"“我为我之前的出口伤人道歉。”"

            jump acolas_q
        "调情":
            $ss(clothes)
            s"“……”"
            $ss(clothes+'scared_mouth normal2_eyes awkward_eyebrow')
            s"“……那个。”"
            $ss(clothes+'smile_mouth smile_eyes smile_eyebrow blush')
            s"“今晚有时间和我出来吃个晚饭吗？”"
            $sh()
            $temp=rd(0,7)
            if temp==0:
                a"“但是我工作还没做完。”"
                a"“下次。”"
            if temp==1:
                a"“我的泡面已经快泡好了。”"
            if temp==2:
                a"“今晚不行……上面有一个重要的会议……”"
            if temp==3:
                a"“不行，虽然我很想和你出来吃点什么。”"
            if temp==4:
                a"“已经吃过晚饭了。”"
            if temp==5:
                a"“今晚要写报告，还有很多东西，下次吧。”"
            if temp==6:
                a"“这周的工作出了很多问题，我要修一下。”"
            if temp==7:
                a"“明晚吧，今晚事情有点多。”"
            $ss(clothes+'sweat')
            s"“好吧。”"
            $sh()
            jump acolas_q
        "结束通话":
            $ss(clothes+'normal2_eyes smile_mouth blush')
            s"“没什么事了，只是想和你随便聊聊……”"
            $sh()
            a"“你真可爱…”"
            $ss(clothes+'smile_eyebrow smile_mouth happy blush')
            s"“哎呀，你这家伙……”"
            $sh()
            a"“那我先挂了。”"
            $ss(clothes+'smile_eyebrow sad_eyes smile_mouth')
            s"“好……”"
            $sh()
            play sound audio.interruption
            "他挂断了电话。"
            jump end_call