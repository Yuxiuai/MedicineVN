label explore_college:
    $temp = ra(p, 1, 7)
    $jumplabel = 'explore_college_' + str(temp)
    $renpy.jump(jumplabel)


label explore_college_1:
    if p.times==4:
        scene gym with fade
    elif p.times==8:
        scene gym with fade
    else:
        scene gym_night with fade
    if p.experience != 'wri':
        $p.gain_abi(0.03, 'wri')
        $Notice.show()
        "去A市大学旁听了一场工作培训机构办的讲座。"
        "虽然大多数都是关于应届大学生就业的问题，以及简历和面试的一些小东西，但我听一听也好。"
        "说不定我哪天想不开就换工作了呢？"
    else:
        $p.gain_abi(0.03, 'wri')
        $Notice.show()
        "去A市大学旁听了一场由四个女生和一个男生组建的文学社办的讲座。"
        "现在的大学还会办校园祭吗？我上学的时候怎么就天天都是无聊的讲座……"
    jump GoOutside_result

label explore_college_2:
    if p.times==4:
        scene gym with fade
    elif p.times==8:
        scene gym with fade
    else:
        scene gym_night with fade
    $p.gain_abi(0.03, 'phy')
    $Notice.show()
    "去A市大学旁听了一节和身体锻炼有关的选修课。"
    "讲了很多关于运动前准备和运动后拉伸的问题，稍微听听也能防止我总受伤。"
    "今天回去就试试好了。"
    jump GoOutside_result


label explore_college_3:
    if p.times==4:
        scene gym with fade
    elif p.times==8:
        scene gym with fade
    else:
        scene gym_night with fade
    $p.gain_abi(0.03, 'wri')
    $Notice.show()
    "去A市大学旁听了一场由四个女生和一个男生组建的文学社办的讲座。"
    "现在的大学还会办校园祭吗？我上学的时候怎么就天天都是无聊的讲座……"
    jump GoOutside_result


label explore_college_4:
    if p.times==4:
        scene gym with fade
    elif p.times==8:
        scene gym with fade
    else:
        scene gym_night with fade
    $p.gain_abi(0.03, 'wri')
    $Notice.show()
    "去A市大学旁听了一场由四个女生和一个男生组建的文学社办的讲座。"
    "现在的大学还会办校园祭吗？我上学的时候怎么就天天都是无聊的讲座……"
    jump GoOutside_result


label explore_college_5:
    scene cafe with fade
    "去校内的奶茶店兼职服务员了。"
    "买冷饮的学生并不太多，还算清闲，我也能偶尔给自己偷偷做一杯柠檬水喝。"
    "轻轻松松赚到了钱。"
    $temp=r2(1.2 * p.price * f())
    $p.money += temp
    $Notice.add('获得%s元报酬' % temp)
    $Notice.show()
    jump GoOutside_result


label explore_college_6:
    scene cashier with fade
    "去校内的超市兼职收银员了。"
    "进出超市的学生很多。"
    "……稍微有点累，但是也赚了不少钱。"
    $temp=r2(1.8 * p.price * f())
    $p.money += temp
    $p.gain_abi(-0.01, 'sev')
    $Notice.add('获得%s元报酬' % temp)
    $Notice.show()
    jump GoOutside_result

label explore_college_7:
    
    if p.experience != 'wri':
        if p.times==4:
            scene gym with fade
        elif p.times==8:
            scene gym with fade
        else:
            scene gym_night with fade
        "在A大校园墙上找到了需要补习的大学生，在教室帮他补习了好久……"
        "虽然都是些简单的知识和工作上完全用不到的知识，不过幸好我还没忘光。"
        $temp=r2(0.9 * p.price * f())
        $p.money += temp
        $p.gain_abi(0.03, 'wor')
        $p.gain_abi(0.01, 'sev')
        $Notice.add('获得%s元报酬' % temp)
        $Notice.show()
    else:
        scene cashier with fade
        "去校内的超市兼职收银员了。"
        "进出超市的学生很多。"
        "……稍微有点累，但是也赚了不少钱。"
        $temp=r2(1.8 * p.price * f())
        $p.money += temp
        $p.gain_abi(0.01, 'sev')
        $Notice.add('获得%s元报酬' % temp)
        $Notice.show()
    jump GoOutside_result