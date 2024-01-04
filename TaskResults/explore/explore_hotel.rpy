label explore_hotel:


    if p.dep_p == 3:
        jump depline_route_3
    
    scene hotelcheckin with fade
    lady"“欢迎来到A市宾馆。”"
    if HotelBuff_.has(p) or HotelBuff.has(p):
        "我忽略了前台工作人员，直接去往电梯……"
        $p.times+=1
        $Notice.show()
        $p.onOutside = False
        if HotelBuff_.has(p):
            $HotelBuff_.clearByType(p)
            $HotelBuff_.add(p)
        jump after_executing_task_label

    if rrs(p, 20):
        $price = int(p.price * 2 * 0.5 * f() * 0.1) * 10
        lady"“今日单人间有特惠哦，入住整晚仅需[price]元。”"
    else:
        $price = int(p.price * 2 * f() * 0.1) * 10
        lady"“本日单间价格为[price]元。”"
    menu:
        "开一个单人房（[price]元）" if p.money >= price:
            $p.money -= price
            "我支付了开房的钱款，于是前台小姐便为我登记。"
            lady"“欢迎入住A市宾馆！”"
            "我接过她递过来的门牌钥匙，走进了电梯。"
            "……"
        "算了":
            "好贵……还是回家躺着吧。"
            jump GoOutside_result
    
    
    $p.times+=1
    $HotelBuff.add(p)
    $Notice.show()
    $p.onOutside = False
    jump after_executing_task_label