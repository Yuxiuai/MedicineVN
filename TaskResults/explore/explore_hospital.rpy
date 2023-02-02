label explore_hospital:
    $beforemusic=renpy.music.get_playing()
    stop music fadeout 3
    if p.times==12:
        scene nightrun with fade
        if p.today == 5:
            "熟悉的周五晚上，希望医院没有提前关门……"
        else:
            "买完药我就赶快离开这里……"
        scene hospital_night with fade
    else:
        scene afternoonrun with fade
        scene hospital with fade
    play music audio.smellsofdisinfectant
    scene elevator with fade
    "医院的电梯。"
    "每次来到这里我都会被一种恐惧感包围。"
    jump explore_elevator

label explore_elevator:
    if renpy.music.get_playing() != audio.smellsofdisinfectant:
        play music audio.smellsofdisinfectant
    menu:
        "去哪层？"
        "7楼：天台":
            "我暂时还不想自杀。"
            jump explore_elevator
        "6楼：神经科":
            "虽然我头疼，但我至少精神上还没出问题。"
            "暂时还没问题。"
            jump explore_elevator
        "5楼：内科":  
            if PhysPun.has(p):
                jump explore_hospital_internalmedicine
            else:
                "至少我最近没感冒，暂时不用去内科。"
                jump explore_elevator
        "4楼：脑科":
            jump explore_hospital_brain
        "3楼：外科":  
            if Injured.has(p):
                jump explore_hospital_surgery
            else:
                "我又没受伤，去外科干嘛……"
                jump explore_elevator
        "2楼：药房":
            jump explore_hospital_pharmacy
        "1楼：大厅":
            jump explore_hospital_end
        '住院部3楼' if p.aco_p == 7 and p.today in (6, 7):
            jump acolas_route_7
           
    
label explore_hospital_pharmacy:
    if p.times==12:
        scene hospital_corridor_night with fade
    else:
        scene hospital_corridor with fade

    "出电梯口后左拐。"
    "我再熟悉不过的位置了。"
    if p.today == 5 and (p.week == 15 or SteamerTicket.has(p)):
        "等等……"
        "今天好像……有点不太对……"
        $renpy.music.set_pause(True, channel='music')
        scene white with dissolve
        "脑中像是爆炸一般地痛，每次血管鼓动都会让痛苦更甚。"
        "呃呃……啊啊啊啊啊啊啊啊啊！"
        "{color=#ffffff}脑中的嗡鸣{/color}" "“听好了……你这家伙……”"
        "{color=#ffffff}脑中的嗡鸣{/color}" "“金钱已经失去意义了，你必须用你所有的钱尽可能多地购买药物……”"
        "{color=#ffffff}脑中的嗡鸣{/color}" "“如果你没有足够的药……接下来会有十分恐怖的事情发生……”"
        "{color=#ffffff}脑中的嗡鸣{/color}" "“再见了……年轻人……”"
        "什么……？"
        if p.times==12:
            scene hospital_corridor_night
        else:
            scene hospital_corridor
        $renpy.music.set_pause(False, channel='music')
        "啊！我！"
        "我晃了晃头，头已经没有刚才那么疼了。"
        "身边的景物再次重回医院。"
        "什么……刚才那是怎么回事……要我花所有的钱买药？为什么？……"
        nurse"“病人848662号，取药了。”"
        nurse"“需要多少？”"
    $temp = p.money
    call screen screen_buyMed(p)
    if temp != p.money:
        "又花了这么多钱买药……"
        "唉……"
    else:
        "等会再回来买……"
    scene elevator with fade
    jump explore_elevator

label explore_hospital_internalmedicine:
    if p.times==12:
        scene hospital_corridor_night with fade
    else:
        scene hospital_corridor with fade
    "出电梯口后右拐。"
    "记得前段时间被冷风吹了，得了重感冒……"
    "天天都往这里跑……"
    scene consulting_room with fade
    "内科诊疗室到了。"
    "面前身穿白褂的医生穿的应该是Pathos那家伙的同款大褂？"
    "日哦我在想什么，白大褂不都一样的吗……"
    "我坐在他面前的凳子上，他将听诊器塞进我的衣服里……"
    "呃呃……好凉……"
    $d = PhysPun.get(p).duration
    doctor "“嗯……”"
    if d<2:
        doctor "“你的病看上去十分严重啊。”"
        doctor "“如果不尽快治疗的话，可能会对身体造成永久性损伤……”"
        $temp = 3 * p.price * f()
    elif d<4:
        doctor "“你的病看上去……比较严重。”"
        doctor "“幸好你来的及时，一会去打一针病毒唑，休息一下应该就好。”"
        $temp = 2 * p.price * f()
    else:
        doctor "“你的病似乎不是很严重。”"
        doctor "“开点抗病毒口服液喝一下应该就好了。”"
        $temp = p.price * f()

    $temp = r2(temp)
    doctor "“总之大概需要[temp]元。”"
    menu:
        "付钱（[temp]元）" if p.money >= temp:
            call Task_processing from _call_Task_processing_24
            scene consulting_room with fade
            $p.money -= temp
            $PhysPun.clearByType(p)
            doctor"“那么治疗就结束了，回去之后注意多运动，好好休息。”"
            $ss('normal2_eyes sweat')
            s"“好。”"
            $sh()
            "……"
            "我离开诊疗室。"
        "返回":
            "这也太贵了。"
            "估计过两天就自己好了呢？"
            $ss('awkward_eyebrow awkward_eyes awkward_mouth sweat')
            s"“呃啊……那个，我感觉我好多了，应该明天就能自己恢复了。”"
            $sh()
            doctor"“这……没问题吗？”"
            doctor"“好吧，记得多休息。”"
            $ss('normal2_eyes sweat')
            s"“好。”"
            $sh()
            "……"
            "我离开诊疗室。"
    scene elevator with fade
    jump explore_elevator

label explore_hospital_surgery:
    if p.times==12:
        scene hospital_corridor_night with fade
    else:
        scene hospital_corridor with fade
    "出电梯口后直走。"
    "……啊……我的腿好疼……"
    "受外伤了还自己一个人来医院，还有比这更让人难过的吗……"
    scene consulting_room with fade
    "外科诊疗室到了。"
    "面前身穿白褂的医生穿的应该是Pathos那家伙的同款大褂？"
    "日哦我在想什么，白大褂不都一样的吗……"
    "我坐在他面前的床上，将裤管向上拉给他展示。"
    "于是医生拿来了双氧水……"
    "看着都疼……"
    $d = Injured.get(p).duration
    doctor "“嗯……”"
    if d<2:
        doctor "“伤势十分严重啊……再耽误一段时间估计你就要去骨科转转了。”"
        doctor "“怎么伤的这么严重……”"
        $ss('awkward_mouth')
        s"“就……随便跑跑步……”"
        $sh()
        doctor "“像被车撞了一样……”"
        $ss('normal2_eyes sweat')
        s"“好。”"
        $sh()
        $temp = 1.5 * p.price * f()
    elif d<4:
        doctor "“伤势看上去还好。”"
        doctor "“一会我给你清理一下伤口，缠上绷带应该就好了。”"
        $temp = 1 * p.price * f()
    else:
        doctor "“啊，你这，直接贴个创口贴不就好了吗，用的着来医院吗……”"
        doctor "“哦哦哦抱歉，请当我刚才什么也没说吧。我帮你清理一下，贴个稍大一点的创口贴就好了。”"
        $temp = 0.5 * p.price * f()
    $temp = r2(temp)
    doctor "“总之大概需要[temp]元。”"
    menu:
        "付钱（[temp]元）" if p.money >= temp:
            call Task_processing from _call_Task_processing_25
            scene consulting_room with fade
            $p.money -= temp
            $Injured.clearByType(p)
            doctor"“那么治疗就结束了，回去之后要好好休息，不要剧烈运动了。”"
            $ss('normal2_eyes sweat')
            s"“好。”"
            $sh()
            "……"
            "我离开诊疗室。"
        "返回":
            "这也太贵了。"
            "估计过两天就自己好了呢？"
            $ss('awkward_eyebrow awkward_eyes awkward_mouth sweat')
            s"“呃啊……那个，我感觉我好多了，应该明天就能自己恢复了。”"
            $sh()
            doctor"“这……没问题吗？”"
            doctor"“好吧，记得多休息。”"
            $ss('normal2_eyes sweat')
            s"“好。”"
            $sh()
            "……"
            "我离开诊疗室。"
    scene elevator with fade
    jump explore_elevator

label explore_hospital_brain:
    if p.today != 5:
        scene consulting_room with fade
        "Pathos医生今天似乎不在，坐在他的位置的是其他医生。"
        "啊，算了。"
        scene elevator with fade
        jump explore_elevator
    else:
        if p.sol_p == 0 and p.week >=4:
            jump pathos_route_0
        elif p.sol_p == 2 and p.week >=8:
            jump pathos_route_1
        else:
            scene consulting_room with fade
            show pathos at trans_toRight()
            pathos"“啊，是你啊。”"
            show pathos smile_mouth with dissolve
            pathos"“就那个叫什么……[p.name]的？”"
            $ss('awkward_eyes sweat')
            s"“……”"
            $sh()
            show pathos surprised_eyebrow surprised_eyes surprised_mouth with dissolve
            pathos"“有什么事吗？”"
            jump pathos_q_hosp


label explore_hospital_end:
    "终于结束了……我要快点离开这个地方。"
    if p.sol_p == 1:
        $p.sol_p = 2
    if p.sol_p == 3:
        $p.sol_p = 4
    play music beforemusic fadein 5
    jump GoOutside_result


label pathos_q_hosp:
    menu:
        "关于药物使用的疑问":
            show pathos angry_eyebrow angry_eyes angry_mouth anger no_sweat with dissolve
            pathos"“我就知道你没听我说话，算了，谁让我是你的专属医生呢？”"
            show pathos angry_eyebrow normal_eyes saying no_anger with dissolve
            pathos"“使用一次药物后，再次使用相同的药物会降低恢复效率到33\%，使用其他的药物会降低恢复效率到50\%。”"
            pathos"“而隔一段时间后（再一次看到菜单界面），再次使用相同的药物会降低恢复效率到66\%，其他种类的药物的使用效率就不会被降低了。”"
            pathos"“再过一段时间，你就可以使用之前的药物了。”"
            show pathos normal_eyebrow normal_eyes with dissolve
            pathos"“举个例子，早上吃，下午可以再吃；上午吃，睡前可以再吃；如果下午吃了，晚上就只能吃其他种类的药了。”"
            pathos"“不过例外的是，如果你晚上吃药，第二天早上不会受影响。”"
            pathos"“总之自己探索吧，有很多信息可以自己查看，不懂就问问别人？”"
            show pathos normal_eyebrow awkward_eyes smile_mouth with dissolve
            pathos"“哦，我差点忘了，似乎全球只有你有这种病。”"
            pathos"“还有什么想问的吗？”"
            jump pathos_q_hosp
        "生病相关的疑问":
            show pathos angry_eyebrow normal_eyes angry_mouth sweat
            with dissolve
            pathos"“你是刚出生的孩子吗？这都不懂？”"
            show pathos normal_eyebrow awkward_eyes smile_mouth no_sweat with dissolve
            pathos"“算了，可能吃那种药把你脑子都吃坏了。”"
            show pathos normal_eyebrow normal_eyes saying with dissolve
            pathos"“首先生病的来源有两个，一个是平时工作太多，过劳的层数过多，也就是4层及以上，在第二天就会转化成生病。”"
            pathos"“另一个是阴冷天气，如果身体平时不多运动，很容易着凉感冒。”"
            pathos"“生病会降低基础属性，也会影响精神状态的消耗恢复和专注度等，尽量避免自己不要生病。”"
            show pathos normal_eyebrow awkward_eyes smile with dissolve
            pathos"“可以花一笔钱去医院治疗，越早越花的钱越少。”"
            pathos"“但如果生病了的话，也并不一定是坏事。”"
            show pathos normal_eyebrow normal_eyes saying with dissolve
            pathos"“另一种恢复方法便是在床上休息来恢复，以这种方法恢复不仅能重新获得失去的基础属性，还能根据体魄层数获得恢复奖励。”"
            pathos"“消耗良好的运动和良好的睡眠等来提高恢复率，阴天也能让恢复率提升。”"
            show pathos normal_eyebrow normal_eyes saying with dissolve
            pathos"“吃感冒药可以延长生病的时间来减缓病情，每天一片，能够按层数来增加休息治疗的概率。”"
            pathos"“受伤也能根据这个方法来恢复，但是偏执不能靠休息恢复。”"
            show pathos normal_eyebrow normal_eyes normal_mouth with dissolve
            pathos"“还有什么想问的吗？”"
            jump pathos_q_hosp
        "伤痕相关的疑问":
            show pathos normal_eyebrow normal_eyes opened_mouth sweat with dissolve
            pathos"“如果不去管生病的话，病情会恶化直到自愈，但是会给身体留下不可逆的损伤。”"
            pathos"“体弱会百分比降低属性，尽量不要获得。”"
            show pathos normal_eyebrow awkward_eyes normal_mouth sweat with dissolve
            pathos"“另外有时候会莫名其妙多出来伤痕，可能是因为灵感过剩和酸痛堆积导致的，要经常关注一下自己的身体状况哦。”"
            pathos"“还有什么想问的吗？”"
            jump pathos_q_hosp
        "实验药物保质期相关的疑问":
            show pathos awkward_eyebrow awkward_eyes awkward_mouth sweat with dissolve
            with dissolve
            pathos"“为什么保质期只有一周？”"
            pathos"“……这个，以后会告诉你的。”"
            show pathos normal_eyes with dissolve
            pathos"“现在你还不需要知道。”"
            pathos"“还有什么想问的吗？”"
            jump pathos_q_hosp
        "普通药物相关的疑问":
            show pathos normal_eyebrow normal_eyes saying no_sweat with dissolve
            pathos"“普通药物啊……就是普通人也会吃的那些药咯。”"
            pathos"“你所服用的实验药物都是快速见效的那种，正常人吃的药对你来说不仅恢复力弱，见效也慢。”"
            pathos"“反正具体效果自己看说明书吧，要遵循用法用量，一次性吃太多小心第二天下不来床哦。”"
            show pathos normal_eyebrow awkward_eyes smile_mouth with dissolve
            pathos"“如果你喜欢就去药房买点，我已经和下面的人说过了，你买什么处方药都不需要医嘱，只是不要买太多就行。”"
            show pathos normal_eyes with dissolve
            pathos"“还有什么想问的吗？”"
            jump pathos_q_hosp
        "调情":
            $ss()
            s"“……”"
            $ss('scared_mouth normal2_eyes awkward_eyebrow')
            s"“……那个。”"
            $ss('smile_mouth smile_eyes smile_eyebrow blush')
            s"“今晚有时间和我出来吃个晚饭吗？”"
            $sh()
            show pathos normal_eyebrow normal_eyes normal_mouth sweat_e
            with dissolve
            $temp=rd(0,13)
            if temp==0:
                pathos"“没时间。”"
            elif temp==1:
                pathos"“下次。”"
                pathos"“最近很忙。”"
            elif temp==2:
                pathos"“我今晚有约了。”"
            elif temp==3:
                pathos"“如果你的精神状态还算良好，就不要对你的主治医师发情了。”"
            elif temp==4:
                pathos"“其实我有男朋友的。”"
                pathos"“他今晚好不容易有时间陪我。”"
            elif temp==5:
                pathos"“我拒绝。”"
            elif temp==6:
                pathos"“没兴趣。”"
            elif temp==7:
                pathos"“今天不行。”"
            elif temp==8:
                pathos"“……”"
            elif temp==9:
                pathos"“你没有其他的事可以做了吗？”"
            elif temp==10:
                pathos"“别开玩笑，严肃点。”"
            elif temp==11:
                pathos"“下次下次。”"
            elif temp==12:
                pathos"“唉，我现在可是在上班时间诶，能不能说点正经的？”"
            elif temp==13:
                pathos"“下次你这样我就要收费了。”"
            $ss('sweat')
            s"“好吧。”"
            $sh()
            show pathos no_sweat with dissolve
            jump pathos_q_hosp
        "没事了":
            $ss('normal2_eyes')
            s"“没什么想问的了。”"
            $sh()
            show pathos angry_eyebrow angry_eyes angry_mouth with dissolve
            pathos"“你该庆幸我这会恰好没有病人，不过也算是和我聊天解解闷了……”"
            $ss('sweat awkward_eyes awkward_eyebrow')
            s"“无语……”"
            $sh()
            scene elevator with fade
            jump explore_elevator


screen screen_buyMed(player):
    #tag gamegui
    use barrier(screen="screen_buyMed", mode=0)

    python:
        
        commonmeds = (DrugHypnotic, DrugColdrex, DrugIbuprofen, DrugAntibiotic, DrugAntidepressant)
        
        if GameDifficulty1.has(player):
            prescription = (DrugVitamin, DrugStomach, DrugAmphetamine, DrugEtizolam, DrugUnknown)
        elif GameDifficulty5.has(player):
            prescription = (DrugAspirin, Drugdextropropoxyphene, DrugMethylphenidate)
        else:
            prescription = []

        med = [MedicineA]
        if player.sol_p>=1:
            med.append(MedicineB)
        if player.sol_p>=3:
            med.append(MedicineC)

    #modal True
    zorder 200
    drag:
        xcenter 0.5
        ycenter 0.48
        frame:
            at trans_toRight()
            style "translucent_frame"
            xsize 700
            ysize 800
            vbox:
                frame:
                    background None
                    yalign 0.001
                    textbutton '{size=+10}购买药物{/size}':
                        text_style "gameUI"
                        xoffset -5
                        yoffset -5
                        action NullAction()

                    imagebutton auto "gui/exit_%s.png":
                        xalign 1.0
                        action [Hide("screen_buyMed"), Return()]

                    frame:
                        background None
                        ysize 700
                        xsize 650
                        ypos 60
                        xpos 25
                        viewport:
                            mousewheel True
                            draggable True
                            if len(med) + len(commonmeds) +len(prescription)>9:
                                scrollbars "vertical"
                            
                            vbox:
                                if player.today == 5:
                                    if ExaminationReport.has(player):
                                        use screen_buylist(player, med, p=0.85, d=0, ds=False, n='实验药物')
                                        null height 10
                                    else:
                                        use screen_buylist(player, med, p=1, d=0, ds=False, n='实验药物')
                                        null height 10

                                use screen_buylist(player, commonmeds, p=-1, d=15, ds=False, n='普通药物')
                                null height 10

                                use screen_buylist(player, prescription, p=-1, d=25, ds=False, n='处方药')
                                null height 30
                                textbutton ''
                    
