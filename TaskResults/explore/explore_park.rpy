label explore_park:
    $temp = ra(p,1,7)
    $jumplabel = 'explore_park_' + str(temp)
    $renpy.jump(jumplabel)

label explore_park_1:
    if p.times==4:
        scene morningrun with fade
    elif p.times==8:
        scene afternoonrun with fade
    else:
        scene nightrun with fade
    $p.physical += 0.01
    $Notice.add('升高了1点身体素质。')
    $Notice.show()
    "在室外行走的感觉总比待在室内要好多了。"
    "今天的空气真清新啊……慢慢走在路上感觉什么疲劳都消失了。"
    "或许之后应该像那些老人一样选个环境好的地方散散步。"
    "……啊，地上的这个是什么……"
    "我朝着那个地上疑似钱包的东西移动，在附近假装系鞋带的同时伸手把那东西捡起来。"
    "运气真好诶。"
    "不过我可不是那种会把到手来的钱交给警察的人。"
    "丢钱是自己活该，捡到是我的运气。"
    $temp=r2(p.price * 0.7 * f())
    "打开了钱包，里面居然有[temp]元钱！"
    $p.money += temp
    jump GoOutside_result

label explore_park_2:
    if p.times==4:
        scene morningrun with fade
    elif p.times==8:
        scene afternoonrun with fade
    else:
        scene nightrun with fade
    $p.physical += 0.02
    $Notice.add('升高了2点身体素质。')
    $Notice.show()
    "在室外行走的感觉总比待在室内要好多了。"
    "今天的空气真清新啊……慢慢走在路上感觉什么疲劳都消失了。"
    "或许之后应该像那些老人一样选个环境好的地方散散步。"
    "……啊，地上的这个是什么……"
    "我朝着那个地上疑似钱包的东西移动，在附近假装系鞋带的同时伸手把那东西捡起来。"
    "运气真好诶。"
    "不过我可不是那种会把到手来的钱交给警察的人。"
    "丢钱是自己活该，捡到是我的运气。"
    $temp=r2(p.price * 0.7 * f())
    "打开了钱包，里面居然有[temp]元钱！"
    $p.money += temp
    "……呃，这什么啊？"
    "钱包里似乎还夹着一个东西。"
    $VipCard.add(p)
    $Notice.show()
    "……算了，捡都捡了，收藏起来好了。"
    jump GoOutside_result


label explore_park_3:
    if p.times==4:
        scene morningrun with fade
    elif p.times==8:
        scene afternoonrun with fade
    else:
        scene nightrun with fade
    $p.physical += 0.02
    $Notice.add('升高了2点身体素质。')
    $Notice.show()
    "在室外行走的感觉总比待在室内要好多了。"
    "今天的空气真清新啊……慢慢走在路上感觉什么疲劳都消失了。"
    "或许之后应该像那些老人一样选个环境好的地方散散步。"
    "……啊，地上的这个是什么……"
    "我朝着那个地上疑似钱包的东西移动，在附近假装系鞋带的同时伸手把那东西捡起来。"
    "运气真好诶。"
    "不过我可不是那种会把到手来的钱交给警察的人。"
    "丢钱是自己活该，捡到是我的运气。"
    $temp=r2(p.price * 0.7 * f())
    "打开了钱包，里面居然有[temp]元钱！"
    $p.money += temp
    "……呃，这什么啊？"
    "钱包里似乎还夹着一个东西。"
    $SexyPic.add(p)
    $Notice.show()
    "可以作为今晚的施法材料……嘿嘿嘿……"
    jump GoOutside_result


label explore_park_4:
    if p.times==4:
        scene morningrun with fade
    elif p.times==8:
        scene afternoonrun with fade
    else:
        scene nightrun with fade
    $p.physical += 0.02
    $Notice.add('升高了2点身体素质。')
    $Notice.show()
    $temp=r2(p.price * 1.5 * f())
    $p.money -= temp
    if p.money <0:
        $p.money = 0
    "在室外行走的感觉总比待在室内要好多了。"
    "今天的空气真清新啊……慢慢走在路上感觉什么疲劳都消失了。"
    "或许之后应该像那些老人一样选个环境好的地方散散步。"
    "……啊，旁边有小吃店啊……"
    "买点小吃好了。"
    "我把手伸进口袋。"
    "熟悉的手感不见了。"
    "啊……钱包不会被人偷了吧！"
    "我伸手探过全身的口袋………"
    $showNotice(['遗失了%s元钱！' % temp])
    if p.money==0:
        "身上的口袋都翻过了，什么也没找到，就连随身带着的扣耳勺都被偷了！"
        "早知道来这公园之前就该把钱都放在家里！"
        $p.severity += 0.01
        $showNotice(['升高了2点严重程度。'])
    else:
        "幸好另一个口袋还有钱……不至于打车的钱都没了……"
        "早知道来这公园之前就该把钱都放在家里！"
    jump GoOutside_result


label explore_park_5:
    if p.times==4:
        scene morningrun with fade
    elif p.times==8:
        scene afternoonrun with fade
    else:
        scene nightrun with fade
    $p.severity -= 0.03
    $PhysRezB.add(p)
    $Notice.add('降低了3点严重程度。')
    "去江边的大桥散步了。"
    "听江潮冲刷勾勒出花纹的水泥江岸发出澎湃的响声，感到很放松。"
    $Notice.show()
    jump GoOutside_result


label explore_park_6:
    if p.times==4:
        scene morningrun with fade
    elif p.times==8:
        scene afternoonrun with fade
    else:
        scene nightrun with fade
    $rec = r2(20 * Task.getRecoScale(p))
    $p.severity -= 0.02
    $p.mental += rec
    $Notice.add('恢复了%s点精神状态。' % rec)
    $Notice.add('降低了2点严重程度。')
    $PhysRezB.add(p)
    "在公园慢跑。"
    "稍微出了点汗，感觉还不错。"
    $Notice.show()
    jump GoOutside_result


label explore_park_7:
    if p.times==4:
        scene morningrun with fade
    elif p.times==8:
        scene afternoonrun with fade
    else:
        scene nightrun with fade
    $rec = r2(15 * Task.getRecoScale(p))
    $p.physical += 0.02
    $p.mental += rec
    $Notice.add('恢复了%s点精神状态。' % rec)
    $Notice.add('提升了2点身体素质。')
    $PhysRezB.add(p)
    "在公园快跑。"
    "虽然跑了一会就大喘气了，不过还算是坚持了很久。"
    $Notice.show()
    jump GoOutside_result