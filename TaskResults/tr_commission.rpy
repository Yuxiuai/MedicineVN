default screen_phone_write_page = 0
default screen_phone_write_inputwords = ''

screen screen_phone_write_(player):
    predict False
    style_prefix "gameUI"
    zorder 600
    
    python:
        def getheight(comm):
            if comm.freewheeling:
                return 110
            h = 110
            
            if comm.needWord == -1 and comm.needInspiration == -1 and comm.du == -1:
                return 135
            else:
                if comm.needWord != -1 :
                    h+=25
                if comm.needInspiration != -1 :
                    h+=25
                if comm.du != -1 :
                    h+=25
            return h

    frame:
        
        
        background None
        xcenter 0.5
        ycenter 0.5
        yoffset -10
        
        use barrier('', 0)

        add "gui/phone/wallpaper/message.webp":
            xcenter 0.5

        text "撰写文稿" xpos 0.92 xanchor 1.0 ypos 0.085 size 40 style "foodname"


        frame:
            
            background None
            xalign 0.5
            yalign 0.55
            ysize 1300
            xsize 582
        

            frame:
                ypos 150
                background None
                
                frame:
                    background None
                    $ comms = list(filter(lambda x: type(x)==UnfinishedCommission, player.items))
                    vbox:
                        text "以下是可编写的委托：" style 'foodname' size 25 color "#383838"
                        frame:
                            background None
                            ypos 0.05
                            viewport:
                                ysize 650
                                xsize 550
                                mousewheel True
                                draggable True
                                vbox:
                                    spacing 2
                                    for i in comms:
                                        

                                        hbox:
                                            $ys = getheight(i.comm)
                                            frame:
                                                background Frame("#00c38b")
                                                xsize 460
                                                ysize ys+110
                                                vbox:
                                                    $price = i.comm.require*100*i.comm.priceFluctuation

                                                    text i.comm.name:
                                                        style 'phonew'
                                                        size 30
                                                        
                                                    text "水平需求：" + str(i.comm.require):
                                                        style 'phonew'
                                                        if i.comm.require > player.writing_grade():
                                                            color "#ff2525"

                                                    text "提出价格：" + str(price) + "/千字":
                                                        style 'phonew'

                                                    text "需求：" style 'phonew'
                                                    if i.comm.needWord == -1 and i.comm.needInspiration == -1 and i.comm.du == -1:
                                                        text " · 无需求" style 'phonew'
                                                    else:
                                                        if i.comm.needWord != -1 :
                                                            text " · 字数需求：" + str(i.comm.needWord) style 'phonew'
                                                        if i.comm.needInspiration != -1 :
                                                            text " · 灵感需求：" + str(i.comm.needInspiration) style 'phonew'
                                                        if i.comm.du != -1 :
                                                            text " · 时间需求：" + str(i.comm.du) style 'phonew'

                                                    $cInfo = i.comm.contentInfo()
                                                    null height 10
                                                    text " > 平均写作技巧：" + str(cInfo[3]) style 'phonew'
                                                    text " > 已完成字数：" + str(cInfo[0]) style 'phonew'
                                                    text " > 文稿总价值：" + str(cInfo[1]) style 'phonew'
                                                    text " > 共消耗灵感：" + str(cInfo[2]) style 'phonew'
                                                    


                                            frame:
                                                yfill True
                                                xsize 80
                                                ysize ys+110
                                                background Frame("#00c38b")
                                                
                                                
                                                
                                                textbutton ">":
                                                    action Hide("info"),Function(player.rtn, i),SetVariable("screen_phone_write_page", 1)
                                                    
                                                    yfill True
                                                    xfill True
                                                    at app_transform
                                                    yalign 1.0
                                                    background Frame("#00a374")
                                                    text_style 'phonew'
                                                    text_xalign 0.5
                                                    text_size 50
                                                    activate_sound audio.card2
                                    null height 100  

                    


screen screen_phone_input_(player, mode='w'):
    $global random_article

    predict False
    style_prefix "gameUI"
    zorder 600
    
    frame:
        
        
        background None
        xcenter 0.5
        ycenter 0.5
        yoffset -10
        
        use barrier('', 0)

        add "gui/phone/wallpaper/message.webp":
            xcenter 0.5
        if mode == 'f':
            text '随笔写作' xpos 0.15 ypos 0.0925 size 30 yanchor 0.5 color "#00a374" style "foodname"
        else:
            text player.retval.comm.name xpos 0.15 ypos 0.0925 size 30 yanchor 0.5 color "#00a374" style "foodname"

        imagebutton idle "images/gui/randg.png":
            action SetVariable("screen_phone_write_inputwords", rcd(random_article))
            xpos 0.8 ypos 0.09 yanchor 0.5
            activate_sound audio.dice
            at app_transform

        imagebutton idle "images/gui/okg.png":
            action [Function(player.rtn1, screen_phone_write_inputwords),SetVariable("screen_phone_write_inputwords", ''),SetVariable("screen_phone_write_page", 0),Return()]
            xpos 0.9 ypos 0.09 yanchor 0.5
            at app_transform

        frame:
            
            background None
            xalign 0.5
            yalign 0.55
            ysize 1300
            xsize 582
        

            frame:
                ypos 150
                background None
                
                frame:
                    background None
                    input:
                        value VariableInputValue("screen_phone_write_inputwords")
                        size 20
                        color "#000"
                        xalign 0.0
                        yalign 0.0
                        length 1000
                        exclude "\"\'[]{}%$@?!#^&*\(\)"
                    
                hbox:
                    xalign 0.5
                    spacing 50

                    
                
    key 'K_KP_ENTER' action SetVariable("screen_phone_write_inputwords", screen_phone_write_inputwords+_('\n        '))
    key 'K_RETURN' action SetVariable("screen_phone_write_inputwords", screen_phone_write_inputwords+_('\n        '))

                    

                    
screen screen_phone_commission(player):
    #tag gamegui
    modal True
    style_prefix "gameUI"
    zorder 600
   
    frame at pickup_phone_transform:
        
        background None
        xalign 0.5
        ypos 0.1
        ysize 1300
        xsize 582
        use screen_phone_desktop(player)
        if screen_phone_write_page == 0:
            use screen_phone_write_(player)
        else:
            use screen_phone_input_(player)
        use screen_phone_header(player)

 
        add "gui/phone/frame.png":
            xalign 0.5
            ypos -8

        frame:
            background None
            xpos 0.03
            ypos 0.06
            imagebutton auto "gui/phone/backw_%s.png":
                if screen_phone_write_page == 0:
                    action Show(screen="screen_tr_commission_confirm",player=player), Hide("info")
                else:
                    action SetVariable("screen_phone_write_page", 0)
                hover_sound audio.cursor
            

                
    
    key 'K_ESCAPE':
        if screen_phone_write_page == 0:
            action Show(screen="screen_tr_commission_confirm",player=player), Hide("info")
        else:
            action SetVariable("screen_phone_write_page", 0)







screen screen_phone_freewheeling(player):
    #tag gamegui
    modal True
    style_prefix "gameUI"
    zorder 600
   
    frame at pickup_phone_transform:
        
        background None
        xalign 0.5
        ypos 0.1
        ysize 1300
        xsize 582
        use screen_phone_desktop(player)
        use screen_phone_input_(player, 'f')
        use screen_phone_header(player)

 
        add "gui/phone/frame.png":
            xalign 0.5
            ypos -8

        frame:
            background None
            xpos 0.03
            ypos 0.06
            imagebutton auto "gui/phone/backw_%s.png":
                action Show(screen="screen_tr_commission_confirm",player=player), Hide("info")
                hover_sound audio.cursor
            

                
    
    key 'K_ESCAPE':
        action Show(screen="screen_tr_commission_confirm",player=player), Hide("info")
        






screen screen_tr_commission_confirm(player, i=_("确定不写委托吗？这将会导致本日程直接结束。"), width=400, pp=renpy.get_mouse_pos()):
    use barrier(screen="screen_tr_commission_confirm")
    style_prefix "info"
    zorder 1000
    $p = pp
    if p[0] < 1500:
        $xc = 0.0
        $trans = trans_toLeft
    else:
        $xc = 1.0
        $trans = trans_toRight
    $xc = 0.0 if p[0] < 1500 else 1.0
    $yc = 0.0 if p[1] < 540 else 1.0
    frame:
        pos pp
        padding (15, 15)
        xanchor xc
        yanchor yc
        at trans()
        vbox:
            align pp
            if i is not None:
                label i:
                    text_style "info_text"
                    xsize width
            null height 30
            hbox:
                xalign 0.5
                spacing 40
                textbutton _("{size=-3}确定{/size}"):
                    action [Hide("screen_tr_commission_confirm"), Function(player.rtn, None),SetVariable("screen_phone_write_inputwords", ''),SetVariable("screen_phone_write_page", 0),Return(None)]
                    activate_sound audio.cursor
                textbutton _("{size=-3}返回{/size}"):
                    action Hide("screen_tr_commission_confirm")
                    activate_sound audio.cursor



init python:
    random_article = [
    _('    当闹钟刺破米勒·奥利维亚的梦境时，他的手完全依靠肌肉记忆无意识地延伸，在按下停止按钮好一会才让意识缓慢清醒。\n\n    迎接他的不是从窗外射入的晨晖，而是他忠诚的中校——雪莉·沙利文的身影，那只褐色毛发的犬兽人的紧身白衬衫完美地勾勒出他壮硕的倒三角躯体，完美地遮挡过窗外光线，不至于让刚刚睡醒的奥利维亚的双目接受过多的日光。'),
    _('    繁琐的文件胡乱分布在床的一边，也正是因为连夜处理它们，让米勒在这个平时能够不感到疲倦而起床的时刻格外地困。\n\n    大脑还未完全清醒，奥利维亚勉强抬眼试图让眼睛开始工作，双臂支撑起半个身躯准备起身，而明显还没有准备好的身体完全使不上劲，便又趴在床上。'),
    _('    一只手平铺着而另一只搭在他自己的头上，眼角酸胀难耐令他再次闭上眼睛贪图更多的休息。'),
    _('    而后奥利维亚的两只手指互相岔开，将那只犬兽人的口打开，黏腻的唾液在上下牙齿间连成条条银丝，沙利文才睁眼，带着无可名状的笑容的奥利维亚的脸庞映入他的眼帘。'),
    _('    然后奥利维亚的两根手指弯曲勾住他的下牙齿向自己的方向施力，将沙利文的身体继续向下压，直到沙利文的身体完全贴紧他的身体，两颗头颅之间仅有十公分，沙利文呼吸过的空气交织新的氧气进入奥利维亚的肺部，而沙利文的肺泡将带着有奥利维亚气息的氧气嵌入静脉血中将其变得鲜红。'),
    _('    沙利文继续将脸部下压，吻上他的中将。奥利维亚没有因为他的私自行动发怒，却变得顺从起来。他们的口腔从此变为一个，互相交织厮磨，两根舌头热烈的流动而又缠绕着，互相搜刮着唾液，舔舐着牙齿，口腔肉壁，淫靡水声回荡，唾液从齿间的缝隙流出，沾满唇边。'),
    _('    仍然没有停止地，沙利文的爪子开始解开奥利维亚的衬衣扣子，露出从下巴延伸至腹部的乳白色毛发，和挺实的胸肌和腹肌。但他们仍然没有停止相吻，这黏腻着似乎永不停歇的吻令他的性器开始膨胀，把深黑色的西装裤的裆部撑出一块空间，液体已经浸湿了那一小块布料。'),
    _('    奥利维亚暂时将身体的主导权让给了这个木头中校，感受着沙利文的手掌正抚摸着他自己的腹部，然后继续向下继续抚摸着欲望的实体，用指腹细细勾勒狼根的形状，轻触那膨胀的成结。而后解开了他紧束的皮带，于是那嫩红色的肉棒就此暴露在视野中。'),
    _('    沙利文似乎是有偷偷学习过性爱技巧，以在每月的那特殊一天服侍好他的中将。他主动选择松开奥利维亚的唇，而那只蓝色的狼一改鄙夷和冷漠，流露出渴望目光的同时伸出舌头舔去银丝，而沙利文也知晓他的意思，伸出舌头在口腔外继续交织，互相磨蹭着舌。'),
    _('    我。\n\n    透过附上层灰的镜子倒映着的这只疲惫的家伙。\n    我瞧着眼周两侧不知道什么时候出现的较重的眼袋，眉头不自觉地扭成一团儿。\n    木梳齿穿过我的黑色鬃毛，将缘由熵增而混乱的互相粘连打结的部分梳理成勉强算是可以被称为“有整理过”的样子，再将额上的刘海梳向一边儿，这应该可以算是我身上最“个性”的部分了。'),
    _('    我咬着头绳，将头后稍长部分的发用爪子收集为一束，被我的两根手指限制着无法散开。而后我捏着他们的根部，解放一只手我才能拿到头绳，进而把它们扎成小小的马尾。这一切都是我看着镜子而作的，再加上每天早晨都要进行一遍，所以还算得心应手，没有花费太多时间。'),
    _('    我捏着随手搭在椅背的昨晚将没有来得及挂好的衬衫的肩部位置，将它垂直提起，悬挂在空中。而后抓着两边向外甩着，利用重力将衣服表面褶皱抻平，然后以最平常不过的方式穿上这件我最常穿的衣服，用就算没有接触过纽扣的人看了之后就学会的方式系好扣子。\n\n    我穿上裤子，然后拉我的吊带，拽着它们以越过我的肩膀，与另一面的裤子上的卡扣结合……'),
    _('    只靠重复那些老掉牙的黄色笑话才有话说的电台有什么好听的？\n\n那只白色的猫儿小声嘟囔着什么，自说自话地发出几声细小的呢喃，单手握住方向盘，而他空闲出来的另一只爪子则努力伸着，然后打开了车载电台的开关，同时拨弄着另一个用来换台的旋钮。\n    '),
    _('    短暂的噪音声响后，那老旧的扩音器极勉强地挤出几句过时的情歌，里面的人像要把嗓子扯破一般嘶吼，反正我是完全欣赏不来这种东西。\n    我的猫已经开车几个小时了，竟然还能对眼前的事物保持专注，可怕的家伙，也许应该找个时间给他休息一会。'),
    _('    我将双爪交叉，越过头顶，垫在靠背的上方，向后躺、枕在自己的爪子上，微微侧身观察着周围环境。\n    不出所料，和几个小时前几乎一模一样。\n    我失去了兴趣。正过身子，把沾满尘土的眼合上。'),
    _('    下层城区的郊野地带，他们把这里称之为废土。\n\n    这里充满了中层排放过来的垃圾和废料，辐射和充满生物毒性的垃圾把这里改造成完全失去生命力的荒野。\n    但这里也是整个下层唯一可以说算是无治安无政府管理的地区。'),
    _('    “流浪者”们在这里组建不同的帮派，对外交易或是做买卖。\n    住在这儿的家伙对于听见枪声这件事已经完全没感觉了。\n\n    这也是我和他自驾游来到这里的目的，体验一把自由开枪的快感。\n    虽说中层并没有禁枪令，但那儿还算说得过去的治安让我真的找不到什么可以开枪的机会。'),
    _('    我释放我脑后的爪子，头顺着重力向后靠在原来的车座靠背上。右爪沿着身体体侧形成的线向下推，直到抵达身躯下方绑在腿部上的皮革包，我捏着边儿扯开按扣，将爪子伸进其中。'),
    _('    我感觉到食指指腹的某点传来一丝冰凉，以及熟悉的金属的坚硬触感。我的爪子继续向里，感受粗糙的握柄，再用掌心的爪垫感受她的完整形状。\n    一把手枪，我的爱枪，我叫她阿贾克斯。'),
    _('    天色从灰融化为深黑，致密的尘云透不进半点月光。\n    我站在崖边，凭着夜视勉强瞧着崖下的灌木和崩塌的石，风从山谷吹到悬崖，再向上流过我的身躯，这儿没有中层满溢的汽油味和其他兽的气息，也不像上层有种让人窒息的压力感。'),
    _('    风直接穿过了我的身躯，将全身的血和骨肉都清洗，同时某种无法言说的快感喷薄而出。\n\n    可惜的是到头来也没遇到被中层吹得可怕至极的恐怖袭击，甚至连个活物都没有，可惜了我为此还准备了一段时间。'),
    _('    我转头，看向那簇跳动的火。\n\n    我刚刚才意识到，在我发呆的时候，他已经停好了车，生了火，甚至已经组装好了帐篷。而现在那只生着黑条纹的白色猫儿坐在石头上，两只爪子抵着大腿，支撑着头对着营火发呆。'),
    _('    他总是那么让人安心，把一切事情都准备妥当。\n    让我想起了刚遇见他的时候，对什么事都过分认真的可爱模样。\n\n    我坐在他身边，他抬起头面朝着我。\n    我只是捏着我的眼镜腿，将它放在一边，而后看着他。\n    他大概明白我的意思了。\n\n    我的头靠近他，他也顺应地闭上眼。\n    于是我和他的唇融合了。'),
    _('    缓慢地，温和地，我的舌进入了那一地界。我的舌轻压他的齿，他没有急切地继续，而是缓慢地微开，像未去糖衣的蜜，存有防备却充满诱惑。回应他他的情趣，挑逗地舔着他齿尖，撬开了他半掩着的齿，紧接着便是充满渴望的进攻。'),
    _('    我径直冲向熟悉的位置，挤压着他舌下的唾液腺以释放更多口涎，臂环绕住他同我一般纤瘦的身躯，在感受到他也因渴望而紧紧缚住我的腰时，某种仅在此刻才产生的独特的快感涌入我的大脑。我越发和他靠近，直至紧密地拥抱在一起。\n\n    我品味着那根带着肉刺的舌，和他的柔软互相缠绕交融。'),
    _('    我感觉到我的那物正在膨胀，顶着内裤向外凸起。\n    朝着斜下方看的他也察觉到了我的欲望，这只发情的猫儿开始主动靠近我的唇，骨。索求第二轮接吻，我没有拒绝的理由。'),
    _('    我的舌品尝着他口腔每一寸肌肤，放肆地搜刮带着他独特气味的唾液，某种鱼的咸味在我口中扩散，我不讨厌鱼，但如果是属于他的，便让我也能对其甘之如饴。'),
    _('    我感觉到他灵巧的小爪子正抚摸着我的裆部，摩挲凸起的顶端。这种欲望强化了我的渴望，我更为粗暴地吮吸占有他的舌，而他也开始试图解开我的皮带，完全是轻车熟路的感觉，他拉下了我的裤子，使我的欲望暴露在外，用那小肉垫温柔地侍弄着龟头。\n\n    这次是我主动松开他的唇。\n    我能观察到此刻的他的眼神充满了渴望。'),
    _('    车窗全部摇下。\n\n    风擦过我的耳边，从他握着方向盘的两只手臂下穿过，再从他那侧的车窗流出。幸好车载电台放出的不再是那个讲着黄色笑话的脑瘫了，也许是被炒了也说不定，现在正放着中层听不到的下层摇滚乐。'),
    _('    虽然那只猫儿嘴上没动静，不过我感觉到了他的尾巴正随着节拍敲击着车底，产生小而低沉的敲击声。\n\n    空气中弥漫着土腥气和令人反胃的酸臭，但没人说过我讨厌这种感觉。\n    这正是我所渴望的，代表放浪的自由气息。'),
    _('    我望着前方。\n\n    两侧的绿植因无可避免的死亡变成黄褐色或是深红色，偶尔能看到被风从枝上吹下的叶子，飞到堆满落叶的人行道上，落叶底部是因潮湿而变成深黑色的地砖，互相紧密贴合着，中间则是黄色的用于盲人行走的盲道，顶端有两条长条状的凸起。'),
    _('    秋天很漂亮。因为充满了死亡，寒冷与绝望的美。\n    无论是植物还是稻米之类的东西，在意识到寒冷和死亡将至时，惊恐地将自己的子嗣产出，保留自己的基因试图逃离灭绝，但却只是供人类们食用，如果植物有意识，那该有多绝望呢？\n呵呵，虽然我也吃它们就是了。\n\n    秋天是如此绝望和美丽的季节，所以我也把自己的死亡安排在秋天。'),
    _('    他扑过来了。\n    是的，我早就知道他会先攻击我的脖子，我用右手预判他的动作，抓住他的衣领，使其向下，把他溢出口水的大嘴按到我的肚子上。\n    他很聪明，开始用牙撕开我的上衣，用舌头开始舔着我涂满了带有引诱性香味的化学物质的腹部。'),
    _('    此时，他就像真正的野生动物那样四足着地，两只腿在我紧闭的双腿两边半跪着，身体在我的上方，用舌头舔着我的乳头和腹部。\n    腹部是仅次于脖子的既脆弱又重要的位置，但被咬坏部分内脏并不会失去意识，如果一上来就被咬断脖子，这一切就没意义了。'),
    _('    昏暗的贝什街道，1920年肮脏而又浑浊的空气在死气沉沉的伦敦中流淌。我时常隔着窗子向望向月，对寡淡无趣的人生感到厌烦。\n\n    18岁的我踩着记事本布满灰尘的医学书中向上攀爬，同时用我的狼尾巴狠狠地抽那群贫民窟里望着我梦想的无知无能的同龄人，我被嘲笑声和鄙视的目光浸泡着，唯有内心的驱动和梦想，在前方拉拽着我，把我从这个浸泡腐尸和染发脓液烂疮的泥潭中分离开来。'),
    _('    5岁的我在来到伦敦之后，也感觉不出这里的空气能好到哪去。大多愚昧的人还保留着医生仍然是上个世纪以四体液平衡作为医学基础的江湖骗子，不仅不愿看诊，还总是鄙视医生。\n\n    我的理想，我的人生，在成为医生之后，还能做什么呢？'),
    _('    我最后睡着了。\n\n    在朦胧的梦境中，我望见了一束光。\n    如同整个只存在黑暗的世界被打开了一扇天窗。\n    可为什么这光如此美妙，如此圣洁，让人感到渴望——\n我的脸上布满喜悦的泪水——那束光逐渐变成了照亮整个梦境的光，要比我所见过的一切事物都要圣洁——它洗刷了我，也一定可以洗刷这个浑浊的伦敦。'),
    _('    光则点亮了一切，虚无的梦境不再，整个空间变成了天堂。\n    我看见了有三个人那么高的金色大门正对着我敞开，我的身上一丝不挂，我的脚爪踩着柔软的云。\n    我踏进天堂，看见随处可见的光芒，闪耀的宝石，具象化的知识和灵感，如同河流一般在云上流淌。'),
    _('    之后我看见了一个湖泊，上有两米宽的荷叶，还有巨大的睡莲。\n    我踩着睡莲，甚至能够细微地感觉到这植物因我的重量而上下颤抖。\n    这条路并不是无尽远的，在湖泊的对岸，坐着一个黑色的身影。\n    他的背后后倚靠着块状的云，双手大开，向两侧搭在他所倚着的云上。'),
    _('    他同样一丝不挂，坐在那里，一只腿盘在体前，另一只腿则向前延伸。我能看见他身上被深黑色毛发覆盖的身材轮廓，深浅肌肉间缝隙描绘出他健壮的身体。\n    他的阴茎挺立着，如同黑色玄武岩搭建的灯塔，矗立在被频繁被狂风暴雨眷顾的海域中。\n    挺拔而优美。\n\n    我不曾对雄性有过兴趣，但我无法控制自己。'),
    _('    …\n\n    我花了一个小时，把昨晚的我写下的写有他曾描述的无形之术的文档藏在袖子内部的夹层里，以及把他的尸体装进从研究所偷的不透风的深黄色裹尸袋。\n    我能解释他的死——他疯了，一头撞死在墙上，回去之后我只需要在墙上抹一点动物的血液，他们不会在意一个精神病人的死活的。\n    无论如何，我总有办法的。')
    ]
