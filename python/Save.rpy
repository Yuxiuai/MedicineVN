init -10 python early:
    class Save:

        @classmethod
        def clear(cls):
            persistent.savefile[0] = None
            persistent.savefile[1] = None

        @classmethod
        def default(cls):
            persistent.savefile = [None, None, None, [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]

        @classmethod
        def save(cls, player):

            if persistent.savefile[0] != None:
                if persistent.savefile[0].today == player.today:
                    return

            persistent.savefile[1] = dcp(persistent.savefile[0])
            persistent.savefile[0] = dcp(player)
            if player.today == 5:
                if type(persistent.savefile[2]) == list:
                    t0 = dcp(persistent.savefile[0])
                    t1 = dcp(persistent.savefile[1])
                    t2 = dcp(persistent.savefile[2])
                    persistent.savefile = [t0, t1, None, t2]
                persistent.savefile[2] = dcp(player)

            renpy.save_persistent()

        @classmethod
        def load(cls, slot):
            global p
            sh()
            slot.restart += 1
            p = dcp(slot)
            persistent.savefile[1] = None
            persistent.savefile[0] = dcp(p)
            renpy.jump_out_of_context("afterload")

        @classmethod
        def record(cls, slot):
            import time
            slot.savetime = time.strftime(_('%Y.%m.%d %H:%M:%S'),time.localtime(time.time()))
            if None not in persistent.savefile[-1]:
                showNotice([_('存档栏位已满！！')])
            else:
                for i in range(len(persistent.savefile[-1])):
                    if not persistent.savefile[-1][i]:
                        persistent.savefile[-1][i] = dcp(slot)
                        break
            renpy.save_persistent()

        @classmethod
        def record_poz(cls, poz):
            import time
            persistent.savefile[-1][poz] = dcp(persistent.savefile[0])
            persistent.savefile[-1][poz].savetime = time.strftime(_('%Y.%m.%d %H:%M:%S'),time.localtime(time.time()))

            renpy.save_persistent()
            

        @classmethod
        def delete(cls, pos):
            persistent.savefile[-1][pos] = None

            renpy.save_persistent()


        @classmethod
        def savecheck(cls):

            if list not in [type(savetype) for savetype in persistent.savefile]:
                cls.default()
                return

            if len(persistent.savefile) == 3:
                t0 = dcp(persistent.savefile[0])
                t1 = dcp(persistent.savefile[1])
                t2 = dcp(persistent.savefile[2])
                persistent.savefile = [t0, t1, None, t2]

            if persistent.savefile[0]:
                cls.save_compatible(persistent.savefile[0])
            if persistent.savefile[1]:
                cls.save_compatible(persistent.savefile[1])
            if persistent.savefile[2]:
                cls.save_compatible(persistent.savefile[2])

            if type(persistent.savefile[-1]) == list:
                for savefile in persistent.savefile[-1]:
                    if savefile:
                        cls.save_compatible(savefile)
                if len(persistent.savefile[-1]) < 20:
                    for i in range(20 - len(persistent.savefile[-1])):
                        persistent.savefile[-1].append(None)
            else:
                temp = dcp(persistent.savefile[-1])
                showNotice(["存档数据丢失，已重置。"])
                if type(temp) == Player:
                    persistent.savefile[-1] = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, temp]
                else:
                    persistent.savefile[-1] = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

        
        @classmethod
        def errorattrs(cls, slot, *arg):
            return list(set(dir(slot))^set(dir(type(slot)(*arg))))

        @classmethod
        def is_compatible(cls, slot):
            if bool(cls.errorattrs(slot)):
                return False
            for i in slot.items:
                if bool(cls.errorattrs(i, slot)):
                    return False
            for i in slot.effects:
                if bool(cls.errorattrs(i)):
                    return False
            return True

        @classmethod
        def uncompatible_reason(cls, slot):
            lostinfo = _("缺少或多余以下属性或方法：\n")
            for i in cls.errorattrs(slot):
                lostinfo += '(Player)%s\n' % (i)
            for i in slot.items:
                for j in cls.errorattrs(i, slot):
                    lostinfo += '(%s)%s\n' % (type(i).__name__, j)
            for i in slot.effects:
                for j in cls.errorattrs(i):
                    lostinfo += '(%s)%s\n' % (type(i).__name__, j)

            return lostinfo.strip()
        
        @classmethod
        def compatible(cls, object, *arg):
            compatible_object = type(object)(*arg)
            for attr in list(set(dir(object)) ^ set(dir(compatible_object))):
                if not hasattr(compatible_object, attr):
                    delattr(object, attr)
                else:
                    setattr(object, attr, getattr(compatible_object, attr))
            

        @classmethod
        def save_compatible(cls, slot):   
            cls.compatible(slot)
            for i in slot.items:
                cls.compatible(i, slot)
            for i in slot.effects:
                cls.compatible(i)
            
            
