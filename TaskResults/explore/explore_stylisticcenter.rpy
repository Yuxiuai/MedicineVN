label explore_center:
    
    $temp = ra(p, 1, 3)
    $jumplabel = 'explore_center_' + str(temp)
    $renpy.jump(jumplabel)
        

label explore_center_1:
    if p.times==12:
        scene theater_night with fade
    else:
        scene theater with fade
    "也许今天可以看看电影……"
    "电影院门口的招牌上印着最新电影《于秀爱旅行记》的海报。"
    menu:
        "买票（60元）" if p.money > 60:
            "进去看看好了……"
            scene movie with fade
            call Task_processing from _call_Task_processing_43
            if p.times==12:
                scene theater_night with fade
            else:
                scene theater with fade
            $TicketRoot.add(p)
            $p.money -= 60
            $p.gain_abi(-0.03, 'sev')
            
            $MovieEffect.add(p)
            $Notice.show()
            "看完了……"
            "让人印象深刻的电影，尤其是最后，于秀爱终于遇见了最爱他的人，令人感动。"
        "离开":
            if p.money > 60:
                "估计也没什么好看的，最讨厌这个叫于秀爱的臭鸡巴杠精了。"
            else:
                "摸了摸口袋，出来好像没带够钱啊……"
                "下次再说吧。"
    jump GoOutside_result

label explore_center_2:
    if p.times==12:
        scene museum_night with fade
    else:
        scene museum with fade
    "市博物馆前聚集了好多人哦，"
    menu:
        "买票（60元）" if p.money > 60:
            "进去看看好了……"
            $TicketRoot.add(p)
            $p.money -= 60
            scene museum_in with fade
            "博物馆内人并不太多，即便展品无聊，我也可以安心在这里呆上一会。"
            call Task_processing from _call_Task_processing_44
            $temp=rd(0,8)
            if temp<4:
                if p.times==12:
                    scene museum_night with fade
                else:
                    scene museum with fade
                $rec = r2(20 * Task.getRecoScale(p))
                $p.gain_mental(rec)
                $MuseumEffect.add(p)
                $Inspiration.add(p)
                $Notice.show()
                
                "主题是末代王储的生活展览。"
                "从头走到尾都是些我不太感兴趣的人文历史。"
                "不差，但是也没很好，至少我可以稍微清净一会。"
            elif temp>=4 and temp<6:
                scene exhibition with dissolve
                $p.gain_abi(-0.02, 'sev')
                $MuseumEffect.add(p)
                $Inspiration.add(p)
                $Notice.show()
                "主题是本国的艺术历史。"
                "虽然我对画画兴趣不大，但是欣赏这些奇奇怪怪的画作也很有趣啊。"
                "还挺有趣的。"

            elif temp>=6 and temp<8:
                if p.times==12:
                    scene museum_night with fade
                else:
                    scene museum with fade
                $p.gain_abi(-0.03, 'sev')
                $MuseumEffect.add(p)
                $Inspiration.add(p)
                $Notice.show()
                "主题是考古挖掘出来的文物图片展。"
                "宝玉，衣服，古代的兵器和文人用的扇子宝剑，还有保存完好的书籍……"
                "那样的东西能越过几千年的历史保存到现在真是个奇迹。"

            elif temp>=8:
                if p.times==12:
                    scene museum_night with fade
                else:
                    scene museum with fade
                $p.gain_abi(0.04, 'wor')
                $MuseumEffect.add(p)
                $Inspiration.add(p)
                $Notice.show()
                "主题是计算机发展史。"
                "不得不说，我真的很喜欢看这些严格又规整的东西，编程本来就是透露着美感的。"
                "只可惜我这样的废物也只能写出乱七八糟的代码罢了……"
                "不过转了一圈还是觉得很棒。"

            
            if p.times==12:
                scene museum_night with fade
            else:
                scene museum with fade
            
            "看完了……"
            "也许可以把看到的东西写进文章里……"
            
        "离开":
            if p.money > 30:
                "估计也没什么好看的，算了。"
            else:
                "摸了摸口袋，出来好像没带够钱啊……"
                "下次再说吧。"
    jump GoOutside_result

label explore_center_3:
    scene stadium with fade
    "突然好想去游个泳哦。"
    "去游泳馆玩一会吧。"
    menu:
        "买票（60元）" if p.money > 60:
            $TicketRoot.add(p)
            $p.money -= 60
            scene pool with dissolve
            call Task_processing from _call_Task_processing_45
            
            
            
            $temp=rd(1,6)
            if temp!=6:
                scene stadium with fade
                $rec = r2(30 * Task.getRecoScale(p))
                $p.gain_mental(rec)
                $p.gain_abi(0.03, 'phy')
                $SwimEffect.add(p)
                $Notice.show()
                "从游泳馆的一边一直游到另一边……"
                "游泳这样的运动也不会弄得满身是汗，还能锻炼到身体……"
                "想起当年在游泳期末考试的时候还呛水了，不过最后还是圆满通关了，给了我80多分。"
                "好怀念……"
                "总之……偶尔来一次也不错啦。"
                "……"
            elif temp==6:
                scene swimshower with fade
                $rec = r2(30 * Task.getRecoScale(p))
                $p.gain_mental(rec)
                $p.gain_abi(-0.04, 'sev')
                $SwimEffect.add(p)
                $Notice.show()
                show pathos naked no_sco no_glasses with dissolve
                pathos"“嗯？你那种眼神是什么意思，医生就不能来游泳了吗？”"
                "在这种奇怪地方偶遇自己的主治医师真是太糟糕了……"
                $ss('naked blush no_hat')
                s"“呃……没……”"
                $sh()
                "幸好我已经游完泳了，出来稍微冲一下身体，而他是刚刚才过来。"
                "不过这还是我第一次看见他的裸体……虽然我只是背对着他淋浴，还有时候还是忍不住偷看一眼。"
                "不行，被他发现我在看他的话肯定糟了，我还是赶紧洗完出去吧……"
                "……"
                $Erection.add(p)
                $Achievement315.achieve()
                $Achievement.show()
            
            $Notice.show()
        "离开":
            if p.money > 60:
                "不游了，万一在水里抽筋了就寄了……"
            else:
                "摸了摸口袋，出来好像没带够钱啊……"
                "下次再说吧。"
    jump GoOutside_result



label explore_center_4:
    scene bar_outside_night with fade
    if p.drinklvl == 0:
        "在文体中心附近的一间酒吧，刚来到这边住的时候好像有个朋友带我去过这里。"
        "倒是很久没来这里，今晚就去稍微喝点好了。"
    elif p.drinklvl == 1:
        "上次来的时候喝得迷迷糊糊的……但感觉头没那么疼了就是……"
    elif p.drinklvl == 2:
        "感觉稍微有点上瘾了……再来几次也没关系吧……"
    elif p.drinklvl == 3:
        "我又来到了这个地方，该不会已经变成酒鬼了吧……"
    elif p.drinklvl == 4:
        "今晚也来喝点好了，额啊……"
    elif p.drinklvl >= 5:
        "看来我已经完全离不开这个地方了呢……"
    
    scene drinkbar with dissolve

    if p.drinklvl == 0:
        "……虽然我不经常喝酒，不过反正今晚没什么要紧事，就来凑个热闹也不错……"
    elif p.drinklvl == 1:
        "这地方形形色色的人太多，以后还是不要再来这里好了……"
    elif p.drinklvl == 2:
        "之前没喝过酒真是我的损失……"
    elif p.drinklvl == 3:
        "管他呢，今晚不醉不归！"
    elif p.drinklvl == 4:
        "看来像我这样的社畜不能没有酒呢……"
    elif p.drinklvl >= 5:
        "今晚还是来这里消磨时间好了……"

    
    



    jump GoOutside_result