init -505 python early:
    
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

    def sortByID(arr): # 根据id排序
        arr.sort(key=lambda x: x.id)

    def sliceArr(arr): # 将类或对象根据kind切片为[ [kind1obj1, kind1obj2], [kind2obj1, kind2obj2] ]的形式
        val = [list(filter(lambda x: x.kind == i, arr)) for i in list(set([i.kind for i in arr]))]
        val.sort(key=lambda x: x[0].id)
        return val

    
    def getSubclasses(supercls):
        classes = []

        def findSubclasses(subcls): # 递归
            next = subcls.__subclasses__()
            if not bool(next):
                classes.append(subcls)
                return
            for _cls in next:
                findSubclasses(_cls)
            

        findSubclasses(supercls)
        return classes

    def allE(player):
        for i in ALLEFFECTS:
            i.add(player, rd(1,5))
        LifeIsColorless.clearByType(player)
        Despair.clearByType(player)

    def allI(player):
        for i in ALLITEMS:
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
 
        dictDayFormatENG = {
            0:'???',
            1:'Mon.',
            2:'Tue.', 
            3:'Wed.', 
            4:'Thu.', 
            5:'Fri.', 
            6:'Sat.', 
            7:'Sun.'
        }

        if _preferences.language == 'english':
            if day in dictDayFormatENG:
                return dictDayFormatENG[day]
            else:
                return dictDayFormatENG[0]

        if day in dictDayFormat:
            return dictDayFormat[day]
        else:
            return dictDayFormat[0]

    def teweekday():
        
        dictDayFormat = {
            1:'星期一',
            2:'星期二', 
            3:'星期三', 
            4:'星期四',
        }
 
        dictDayFormatENG = {
            1:'Monday',
            2:'Tuesday', 
            3:'Wednesday', 
            4:'Thurday', 
        }

        if _preferences.language == 'english':
            return dictDayFormatENG[persistent.te_weekday]

        return dictDayFormat[persistent.te_weekday]

    def glitchtext(length):
        gt = "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽž"
        output = "{font=arial.ttf}"
        for x in range(length):
            output += rcd(gt)
        output += "{/font}"
        return output

    def sign(n):
        if n>=0:
            return '+' + str(n)
        return str(n)

    def sign_(n):
        if n>=0:
            return green('+' + str(n))
        return red(str(n))

    def red(s):
        return _('{color=#FF4500}')+str(s)+_('{/color}')

    def green(s):
        return _('{color=#7CFC00}')+str(s)+_('{/color}')

    def yellow(s):
        return _('{color=#ffff00}')+str(s)+_('{/color}')

    def gold(s):
        return _('{color=#FFD700}')+str(s)+_('{/color}')

    def num_str(num, l='*', r='%', rev = False):
        n = num
        if l=='*' and r=='%':
            n *= 100
            c = green if n>=100 else red
            l = ''
        elif l=='**' and r=='%':
            n *= 100
            c = green if n>=100 else red
            l= '*'
        elif l=='+' and r=='%': # 0.1 -> 90%
            n = (n-1) * 100
            c = green if n>=0 else red
            l = '+' if n>=0 else ''
        elif l=='++':
            c = green if n>=0 else red
            l = '+' if n>=0 else ''
        elif l==None:
            c = green if n>=0 else red
        
        if rev:
            c = green if c == red else red
        
        if n == 0:
            c = str

        return c(l + str(int(n)) + r)
    
    def return_cutelevi():
        leviathan_list=[audio.l1,audio.l2,audio.l3,audio.l4,audio.l5,audio.l6,audio.l7,audio.l8,audio.l9,audio.l10,audio.l11,audio.l12,audio.l13,audio.l14,audio.l15]
        x=rd(0,200)
        if x==0:
            Achievement309.achieve()
            Notice.show()
            Achievement.show()
            renpy.music.play(audio.Leviathan, channel='music', loop=True, fadeout=None, synchro_start=False, fadein=0, tight=None, if_changed=False)
        elif x==200:
            Achievement309.achieve()
            Notice.show()
            Achievement.show()
            renpy.music.play(audio.Ultimate, channel='music', loop=True, fadeout=None, synchro_start=False, fadein=0, tight=None, if_changed=False)

        return rcd(leviathan_list)

    def CuteLeviathan():
        renpy.music.play(return_cutelevi(), channel='audio', loop=None)
    
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
        Achievement604.achieve()
        Achievement.show()

    def start_plot():
        renpy.block_rollback()
        config.rollback_enabled = True
        if persistent.clearscreenwhenplot:
            clearscreens()
    
    def end_plot():
        config.rollback_enabled = False
        renpy.block_rollback()
        if persistent.clearscreenwhenplot:
            renpy.show_screen(_screen_name='screen_dashboard',player=p)

    def setfold(i, v):
        i[1]=v
    
    def clearscreens():
        renpy.sound.stop(channel="chara_voice")
        renpy.hide('blackmask', layer='mask')
        sh()
        for i in renpy.get_zorder_list('screens'):
            renpy.hide(i[0], layer='screens')
        

    def ss(str=None):
        if persistent.nosolitussprite:
            return
        renpy.transition(Dissolve(0.2, alpha=True), layer='headimage')
        atl =[]
        if not renpy.showing('solitus',layer='headimage'):
            atl = [head_trans]

        if not str:
            renpy.show('solitus', at_list=atl, zorder=1000, layer='headimage')
        else:
            renpy.show('solitus '+str, at_list=atl, zorder=1000, layer='headimage')

    #def inspe():
        #import inspect
        #caller_frame = inspect.currentframe().f_back
        #caller_file = inspect.getfile(caller_frame)
        #caller_line = caller_frame.f_lineno
        #print(caller_file)
        #print(caller_line)

    def sh():
        if persistent.nosolitussprite:
            return
        renpy.transition(Dissolve(0.2), layer='headimage')
        renpy.hide('solitus', layer='headimage')

    def countdown(player):
        if player.cured < 42:
            return _("距离第三次手术还有%s天。") % (42-player.cured)

        if player.cured < 63:
            return _("还有%s天进行第四次手术。") % (63-player.cured)

        if player.cured < 84:
            return _("还有%s天。") % (84-player.cured)
        
        if player.cured < 105:
            return _("%s。") % (105-player.cured)

        if player.cured == 105:
            return _("0。")
    
    def playmusic(pm):
        if renpy.music.get_playing() != pm:
            renpy.music.play(pm, channel='music', loop=True, fadeout=3, fadein=3)

    def routine_music(player):
        

        if player.finalStageDays > -1:
            if player.mental <= 0:
                bgm = audio.impendingdeath
            else:
                bgm = audio.drownedindespair

        elif player.cured > 0:
            

            if player.onVacation:
                if player.cured<21:
                    bgm = audio.rareleisure
                elif player.cured<42:
                    bgm = audio.rl1
                elif player.cured<63:
                    bgm = audio.rl2
                else:
                    bgm = audio.cured
            else:
                if player.cured<21:
                    bgm = audio.survivingdawn
                elif player.cured<42:
                    bgm = audio.sd1
                elif player.cured<63:
                    bgm = audio.sd2
                else:
                    bgm = audio.cured

        else:
            
            if player.mental <= 20:
                bgm = audio.enjoysuffering
                    
            else:
                if ParkBuff.has(player):
                    bgm = audio.lakesidebreeze
                elif HotelBuff.has(player):
                    bgm = audio.locationhotel
                elif CafeBuff.has(player):
                    bgm = audio.locationcafe
                elif BookstoreBuff.has(player):
                    bgm = audio.locationbookstore
                elif player.onVacation:
                    bgm = audio.rareleisure
                else:
                    bgm = audio.survivingdawn

        

        if player.times > 0:
            playmusic(bgm)

        if not Achievement604.has() and len(mr.playlist) == len(mr.unlocked_playlist()):
            Achievement604.achieve()
            Achievement.show()

        blackmask(player)
    
    def blackmask(player):
        if player.mental <= 20:
            renpy.transition(Dissolve(0.5, alpha=True), layer='mask')
            renpy.show('blackmask', layer='mask')
            renpy.transition(None)
                
        else:
            renpy.transition(Dissolve(0.5, alpha=True), layer='mask')
            renpy.hide('blackmask', layer='mask')
            renpy.transition(None)
        

    def funcruntime(fun, *args):
        import time
        before = time.time()
        fun(*args)
        return time.time() - before




    def routine_bg(player):
        if player.finalStageDays > -1:
            return 'ruins'

        bg = 'office'

        if player.times > 9:
            if player.onOutside or not player.onVacation:
                bg = 'nightrun'
            else:
                bg = 'livingroom'
                
        elif player.onVacation:
            bg = 'workarea'

        elif not player.onVacation:
            if rrs(player, 5):
                bg = 'office_'
            else:
                bg = 'office'
                
        if HotelBuff.has(player):
            bg = 'location_hotel'
        if CafeBuff.has(player):
            bg = 'location_cafe'
        if BookstoreBuff.has(player):
            bg = 'location_bookstore'
        
        
        renpy.scene()
        
        atl = [setcolor]
        if player.mental <= 20:
            atl.append(hardcorebe1_transform)
        renpy.show(bg, at_list=atl)
        renpy.with_statement(trans=Fade(0.5, 0.0, 0.5, color=_('#000')))
        
        renpy.transition(None)
        renpy.show('blurred', at_list=[blurr_concentration(p)])
        



    def routine_narrator(p, what):
        if p.cured < 21:
            renpy.say(None, what)
        else:
            renpy.say(None, _("……"))

    def random_color(str=None):
        import random
        rand_color = hex(random.randint(0,16**6)).replace('0x','').upper()
        if(len(rand_color)<6):
            rand_color = '0'*(6-len(rand_color))+rand_color
        if str:
            return '{color=#%s}%s{/color}' % (rand_color, str)
        return '{color=#%s}' % rand_color
    






    '''

    def replaceKeywords(s):
        if persistent.noinfohightlight:
            return s
        def addColor(s, color, seq):
            for name in seq:
                if _('？') in name:
                    continue
                r = _('{color=%s}{u}%s{/color}{/u}')%(color, name)
                s = s.replace(name, r)
            return s

        s = addColor(s, _('#fbd26a'), [i.name for i in getSubclasses(Task)])
        s = addColor(s, _('#ADD8E6'), [i.name for i in getSubclasses(Effect)])
        s = addColor(s, _('#ff38ee'), [i.name for i in getSubclasses(Item)])
        s = addColor(s, _('#2c80ff'), [_('工作类日程'),_('运动类日程'),_('写作类日程'),_('休息类日程'),_('特殊类日程')])
        s = addColor(s, _('#ff2b59'), [_('严重程度'),_('工作能力'),_('身体素质'),_('写作技巧')])
        s = addColor(s, _('#eeff57'), [_('专注度'),_('工作速度')])
        s = addColor(s, _('#4be63d'), [_('精神状态')])

        return s
    '''