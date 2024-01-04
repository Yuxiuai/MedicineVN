init -11 python early:

    class WineEffect(Effect):
        maxDuration = 1
        kind = _('酒类作用')

    class WineEffect_LongIsland(WineEffect):
        id = 1000
        name = _('长岛冰茶')
        maxStacks = 2
        info = _('接下来饮用的酒有33%的概率减少1层饱腹。')
