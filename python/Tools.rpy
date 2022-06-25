init -505 python:
    
    def rd(a, b):  # 单纯的随机数
        import random
        random.seed()
        return random.randint(int(a), int(b))


    def rs(player, a, b):  # 使用seed 不更改safe
        import random
        random.seed(player.seed)
        return random.randint(int(a), int(b))

    def rh(hashable, player, a, b):  # 使用seed 不更改safe 使用hash
        import random
        random.seed(player.seed * hashable)
        return random.randint(int(a), int(b))


    def ra(player, a, b):  # 使用seed 更改safe
        import random
        random.seed(player.seed + player.safe)
        player.afterUseSeed()
        return random.randint(int(a), int(b))


    def rra(player, chance, a=1, b=100):  # 根据chance返回True或False 使用seed 更改safe
        if chance > b:
            return True
        if chance < a:
            return False
        if ra(player, a, b) < chance:
            return True
        return False

    def rrs(player, chance, a=1, b=100):  # 根据chance返回True或False 使用seed 不更改safe
        if chance > b:
            return True
        if chance < a:
            return False
        if rs(player, a, b) < chance:
            return True
        return False

    def rrd(chance, a=1, b=100):  # 根据chance返回True或False 单纯的随机数
        if chance > b:
            return True
        if chance < a:
            return False
        if rd(a, b) < chance:
            return True
        return False
    
    def rcd(seq):  # 单纯的随机数
        import random
        random.seed()
        return random.choice(seq)

    def rcs(player, seq):  # 使用seed 不更改safe
        import random
        random.seed(player.seed)
        return random.choice(seq)


    def rca(player, seq):  # 使用seed 更改safe
        import random
        random.seed(player.seed + player.safe)
        player.afterUseSeed()
        return random.choice(seq)


    def r2(r):  # 保留两位小数
        return round(r, 2)


    def r4(r):  # 保留4位小数
        return round(r, 4)


    def r2s(r):  # 保留两位小数的同时返回字符串，方便在print中使用
        return str(r2(r))


    def f():
        return rd(9500, 10500) * 0.0001

    def sortArr(domain):
        domain.sort(key=lambda x: type(x).id)


    def rsortArr(domain):
        return sorted(domain, key=lambda x: type(x).id)

    def sliceArr(d):
        val = [list(filter(lambda x: type(x).kind == i, d)) for i in list(set([type(i).kind for i in d]))]
        val.sort(key=lambda x: type(x[0]).id)
        return val

    def sliceTypeArr(d):
        val = [list(filter(lambda x: x.kind == i, d)) for i in list(set([i.kind for i in d]))]
        val.sort(key=lambda x: x[0].id)
        return val

    
    def getSubclasses(supercls):
        l = list(globals())
        v = [globals()[i] for i in l]
        def getSubclsNoChild(subcls): # 是否为类，是否为参数超类的子类 自己是否有子类
            import types
            if not isinstance(subcls, (type, types.ClassType)):
                return False
            if not issubclass(subcls, supercls):
                return False
            if bool(subcls.__subclasses__()):
                return False
            return True
        fl = list(filter(getSubclsNoChild,v))
        return fl

    def allE(player):
        for i in getSubclasses(Effect):
            i.add(player, rd(1,5))

    def allI(player):
        for i in getSubclasses(Item):
            i.add(player)

    def weekdayFormat(day):
        dictDayFormat = {
            0:'???',
            1:'星期一',
            2:'星期二', 
            3:'星期三', 
            4:'星期四', 
            5:'星期五', 
            6:'星期六', 
            7:'星期日'
        }

        return dictDayFormat[day] if dictDayFormat != None else dictDayFormat[0]

    def glitchtext(length):
        gt = "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽž"
        output = "{font=arial.ttf}"
        for x in range(length):
            output += rcd(gt)
        output += "{/font}"
        return output

    def nega(list, index):
        list[index] = not list[index]

    def sign(n):
        if n>=0:
            return '+' + str(n)
        return str(n)

    def sign_(n):
        if n>=0:
            return green('+' + str(n))
        return red(str(n))

    def red(s):
        return '{color=#FF4500}'+str(s)+'{/color}'

    def green(s):
        return '{color=#7CFC00}'+str(s)+'{/color}'

    def yellow(s):
        return '{color=#ffff00}'+str(s)+'{/color}'

    def gold(s):
        return '{color=#FFD700}'+str(s)+'{/color}'

    def num_str(num, l='*', r='%', rev = False):
        n = num
        if l=='*' and r=='%':
            n *= 100
            c = green if n>=100 else red
            l = ''
        if l=='**' and r=='%':
            n *= 100
            c = green if n>=100 else red
            l= '*'
        if l=='+' and r=='%':
            n = (n-1) * 100
            c = green if n>=0 else red
            l = '+' if n>=0 else ''
        if l=='++' and r=='%':
            c = green if n>=0 else red
            l = '+' if n>=0 else ''
        
        if rev == True:
            cb = c
            cb = green if c == red else red
            c = cb
        
        if n == 0:
            c = str

        return c(l + str(int(n)) + r)
    
    def return_cutelevi():
        leviathan_list=[audio.l1,audio.l2,audio.l3,audio.l4,audio.l5,audio.l6,audio.l7,audio.l8,audio.l9,audio.l10,audio.l11,audio.l12,audio.l13,audio.l14,audio.l15]
        x=rd(0,200)
        if x==0:
            renpy.music.play(audio.Leviathan, channel='music', loop=True, fadeout=None, synchro_start=False, fadein=0, tight=None, if_changed=False)
        elif x==200:
            renpy.music.play(audio.Ultimate, channel='music', loop=True, fadeout=None, synchro_start=False, fadein=0, tight=None, if_changed=False)

        return rcd(leviathan_list)

    def CuteLeviathan():
        renpy.music.play(return_cutelevi(), channel='audio', loop=None)
        x=rd(0,200)
        if x==0:
            renpy.music.play(audio.Leviathan, channel='music', loop=True)
        elif x==200:
            renpy.music.play(audio.Ultimate, channel='music', loop=True)
    
    def play_sound(name):
        renpy.music.play(name, channel='sound', loop=None)

    def play_audio(name):
        renpy.music.play(name, channel='audio', loop=None)

    def dcp(x):
        import copy
        return copy.deepcopy(x)

    def musicFormat(str):
        import re

        str = re.compile(r"a.*/").sub('', str)
        str = re.compile(r"<.*>").sub('', str)
        str = re.compile(r"\..*").sub('', str)
        str = str.replace("_", " ")
        
        return str

    def unlockallmusic():
        before = renpy.music.get_playing()
        for i in mr.playlist:
            renpy.music.play(i)
        renpy.music.play(before)

    def rollback_switch():
        renpy.block_rollback()
        if config.rollback_enabled == False:
            config.rollback_enabled = True
        else:
            config.rollback_enabled = False

    def setfold(i, v):
        i[1]=v

    def ss(str=None):
        renpy.transition(Dissolve(0.2, alpha=True), layer='headimage')
        atl =[]
        if not renpy.showing('solitus',layer='headimage'):
            atl = [head_trans]
            
        if str!=None:
            renpy.show('solitus '+str, at_list=atl, zorder=1000, layer='headimage')
        else:
            renpy.show('solitus', at_list=atl, zorder=1000, layer='headimage')
        renpy.transition(None)

    def sh():
        renpy.transition(Dissolve(0.2), layer='headimage')
        renpy.hide('solitus', layer='headimage')