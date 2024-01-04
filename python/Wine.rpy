init 5 python early:
    class Wine(Item):
        kind = _('酒类')
        maxCd = 0
        maxDu = -1
        reuse = False
        isUnique = False

        def sound(self):
            renpy.sound.play(audio.itemdrink)
    
    class Wine_Icewater(Wine):
        id = 1000
        name = _('冰水')
        info = _('饮用后恢复0~2点酒量。')
        ad = _('你是来养鱼的吗？')

        def useItemAction(self, player):
            pool = (0,0,1,1,1,1,2)

            drinkhp = rca(player, pool)
            if drinkhp > 0:
                Notice.add("恢复了%s点酒量。" % drinkhp)
            else:
                Notice.add("没有恢复酒量。")

    class Wine_Mojito(Wine):
        id = 1001
        name = _('莫吉托')
        info = _('饮用后消耗0~1点酒量。')
        ad = _('“麻烦给我的爱人来一杯Mojito——我喜欢阅读她微醺时的眼眸——”')

        def useItemAction(self, player):
            pool = (0,0,1,1,1)

            drinkhp = rca(player, pool)
            sev = 0.01
            if drinkhp > 0:
                Notice.add("消耗了%s点酒量。" % drinkhp)
            else:
                Notice.add("没有消耗酒量。")
            player.gain_abi(-sev, 'sev')
    
    class Wine_LongIsland(Wine):
        id = 1002
        name = _('长岛冰茶')
        info = _('饮用后消耗1点酒量，接下来饮用的2杯酒有一定概率降低1点饱腹。')
        ad = _('“给你调一杯冰凉的Long Island Ice Tea——看似甜蜜却藏着危险的后劲——”')

        def useItemAction(self, player):
            pool = (0,0,1,1,1)

            drinkhp = rca(player, pool)
            sev = 0.01
            if drinkhp > 0:
                Notice.add("消耗了%s点酒量。" % drinkhp)
            else:
                Notice.add("没有消耗酒量。")
            player.gain_abi(-sev, 'sev')
    
    class Wine_Martini(Wine):
        id = 1003
        name = _('干马天尼')
        info = _('饮用后消耗2点酒量，接下来饮用的3~5杯酒有概率恢复1点酒量。')
        ad = _('“”')
    
    class Wine_Margaret(Wine):
        id = 1004
        name = _('玛格丽特')
        info = _('饮用后消耗1~2点酒量，接下来饮用的2杯酒恢复的精神状态提升50~100%。')
        ad = _('“”')

    class Wine_Godfather(Wine):
        id = 1005
        name = _('教父')
        info = _('饮用后消耗1~2点酒量，额外恢复5~10点精神状态。')
        ad = _('“”')
    
    class Wine_B52(Wine):
        id = 1006
        name = _('B-52轰炸机')
        info = _('饮用后消耗1~2点酒量，接下来饮用的3杯酒降低的严重程度提升1点。')
        ad = _('“”')
    
    class Wine_Negroni(Wine):
        id = 1007
        name = _('尼格罗尼')
        info = _('饮用后消耗2点酒量，接下来饮用的3杯酒额外消耗1点酒量。')
        ad = _('“”')

    class Wine_BloodyMary(Wine):
        id = 1008
        name = _('血腥玛丽')
        info = _('饮用后消耗3点酒量，仅一次在你即将喝醉时，恢复1点酒量。')
        ad = _('“”')
    
    class Wine_Tequila(Wine):
        id = 1009
        name = _('龙舌兰日出')
        info = _('饮用后消耗4点酒量，额外降低1点严重程度。')
        ad = _('“”')

    class Wine_Serote(Wine):
        id = 1010
        name = _('Serote特调')
        info = _('仅一次饮用后消耗2点酒量，随机产生效果。')
        ad = _('“”')