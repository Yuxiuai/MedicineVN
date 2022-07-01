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
        "买票（50元）" if p.money > 50:
            "进去看看好了……"
            scene movie with fade
            "……"
            $TicketRoot.add(p)
            $p.money -= 50
            $p.severity -= 0.03
            $showNotice(['降低了3点严重程度。'])
            if p.times==12:
                scene theater_night with fade
            else:
                scene theater with fade
            "看完了……"
            "让人印象深刻的电影，尤其是最后，于秀爱终于遇见了最爱他的人，令人感动。"
        "离开":
            if p.money > 50:
                "估计也没什么好看的，最讨厌这个叫于秀爱的臭鸡巴杠精了。"
            else:
                "摸了摸口袋，出来好像没带够钱啊……"
                "下次再说吧。"
    jump GoOutside_result

label explore_center_2:
    if p.times==12:
        scene museum with fade
    else:
        scene museum_night with fade
    "市博物馆前聚集了好多人哦，"
    menu:
        "买票（30元）" if p.money > 30:
            "进去看看好了……"
            $TicketRoot.add(p)
            $p.money -= 30
            scene museum_in with fade
            "博物馆内人并不太多，即便展品无聊，我也可以安心在这里呆上一会。"
            "…"
            $temp=rd(0,8)
            if temp<4:
                "主题是末代王室的生活展览。"
                "从头走到尾都是些我不太感兴趣的人文历史。"
                "不差，但是也没很好，至少我可以稍微清净一会。"
                $rec = r2(20 * Task.getRecoScale(p))
                $p.mental += rec
                $showNotice(['恢复了%s点精神状态。' % rec])
            elif temp>=4 and temp<6:
                scene exhibition with dissolve
                "主题是本国的艺术历史。"
                "虽然我对画画兴趣不大，但是欣赏这些奇奇怪怪的画作也很有趣啊。"
                "还挺有趣的。"
                $p.severity -= 0.02
                $showNotice(['降低了2点严重程度。'])
            elif temp>=6 and temp<8:
                "主题是考古挖掘出来的文物图片展。"
                "宝玉，衣服，古代的兵器和文人用的扇子宝剑，还有保存完好的书本……"
                "那样的东西能越过几千年的历史保存到现在真是个奇迹。"
                $p.severity -= 0.03
                $showNotice(['降低了3点严重程度。'])
                pass
            elif temp>=8:
                "主题是计算机发展史。"
                "不得不说，我真的很喜欢看这些严格又规整的东西，编程本来就是透露着美感的。"
                "只可惜我这样的废物也只能写出乱七八糟的代码罢了……"
                "不过转了一圈还是觉得很棒。"
                $p.working += 0.04
                $showNotice(['提升了4点工作能力。'])
            if p.times==12:
                scene museum with fade
            else:
                scene museum_night with fade
            "看完了……"
            "也许可以把看到的东西写进文章里……"
            $Inspiration.add(p)
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
            $temp=rd(0,8)
            if temp<4:
                $rec = r2(30 * Task.getRecoScale(p))
                $p.mental += rec
                $showNotice(['恢复了%s点精神状态。' % rec])
                "在游泳馆了里久违地游了大学游泳课的期末考试100米游泳。"
                "好凉快啊……而且游泳这样的运动也不会弄得满身是汗。"
                "早知道我去A大的时候直奔游泳馆就好了……"
                "哎，那不就遇不到Halluke这只极品小白熊了吗……"
                "嗯嗯……换个方式想，万一他也报了游泳课……"
                "……"
                $p.severity -= 0.02
                $showNotice(['降低了2点严重程度。'])
                "牛子硬了。"
            elif temp>=4 and temp<6:
                "在游泳馆了里久违地游了大学游泳课的期末考试100米游泳。"
                "好凉快啊……而且游泳这样的运动也不会弄得满身是汗。"
                "想起当年在游泳期末考试的时候还呛水了，不过最后还是圆满通关了，给了我80多分。"
                "好怀念……"
                $p.severity -= 0.03
                $showNotice(['降低了3点严重程度。'])
            elif temp>=6 and temp<8:
                $rec = r2(20 * Task.getRecoScale(p))
                $p.mental += rec
                $showNotice(['恢复了%s点精神状态。' % rec])
                "在游泳馆了里久违地游了大学游泳课的期末考试100米游泳。"
                "好凉快啊……而且游泳这样的运动也不会弄得满身是汗。"
                "要么以后健身的时候来这里好了……不过这里一次就要60，那里一天才要50……"
                "偶尔来一次也不错啦。"
            scene stadium with fade
            "好舒服啊……"
            "下次写点游泳池里做爱的小黄文吧。"
            "不对，我怎么突然会这么想！"
            $Inspiration.add(p)
        "离开":
            if p.money > 60:
                "不游了，万一在水里抽筋了就寄了……"
            else:
                "摸了摸口袋，出来好像没带够钱啊……"
                "下次再说吧。"
    jump GoOutside_result