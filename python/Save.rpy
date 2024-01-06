init -10 python early:


    class Save:
        
        def __init__(self, name, p):
            self.name = name
            self.p = dcp(p)
            self.exception = False

        def rename(self, name):
            self.name = name

        def delete(self):
            for i in range(len(persistent.savefile)):
                for j in range(len(persistent.savefile[i])):
                    if persistent.savefile[i][j] == self:
                        if len(persistent.savefile[i]) == 1:
                            del persistent.savefile[i]
                            return
                        del persistent.savefile[i][j]
                        return


    class Saver:

        @classmethod
        def save(cls, player):
            import time
            player.savetime = time.strftime(_('%Y.%m.%d %H:%M:%S'),time.localtime(time.time()))
            saved = False
            for i in persistent.savefile:
                if i[0].p.timestamp == player.timestamp:
                    i.append(Save('存档' + str(len(i)), player))
                    saved = True
            if not saved:
                persistent.savefile.append([Save('存档0', player)])


        @classmethod
        def load(cls, slot):
            global p
            sh()
            slot.restart += 1
            p = dcp(slot)
            renpy.jump_out_of_context("afterload")
        
        @classmethod
        def get_today(cls):
            global p
            if not p:
                return -1
            for i in range(len(persistent.savefile)-1,-1,-1):
                for j in range(len(persistent.savefile[i])-1,-1,-1):
                    if persistent.savefile[i][j].p.today == p.today:
                        return persistent.savefile[i][j].p
            return None

        @classmethod
        def get_newest(cls):
            try:
                return persistent.savefile[-1][-1].p
            except Exception:
                return None

        @classmethod
        def export(cls, slot):
            code = cls.dumps(slot)
            pygame_sdl2.scrap.put(pygame_sdl2.SCRAP_TEXT, code)
            showNotice(['已导出存档至剪贴板！', '你可以粘贴该给其他人，点击右上角的加号可导入其他人的存档。'])

        @classmethod
        def inport(cls):
            code = pygame_sdl2.scrap.get(pygame_sdl2.SCRAP_TEXT)
            code = code.replace('\r','')
            slot = None
            if not code:
                showNotice(['剪贴板为空或无法访问剪贴板！'])
                return
            if code[:9] != 'ccopy_reg':
                showNotice(['格式错误！'])
                return
            slot = cls.loads(code)
            if not slot:
                showNotice(['读取失败，请检查是否复制完整！'])
            else:
                showNotice(['成功导入存档！！'])
            cls.save(slot)


        @classmethod
        def dumps(cls, slot):
            import pickle
            return pickle.dumps(slot)
        
        @classmethod
        def loads(cls, text):
            import pickle
            return pickle.loads(text)

        @classmethod
        def savecheck(cls, console=False):
            allsaves = 0
            badsaves = 0
            exceptsaves = 0
            exceptok = 0
            haveempty = False
            for saves in range(len(persistent.savefile)):
                if not persistent.savefile[saves]:
                    haveempty = True
                    continue
                for save in persistent.savefile[saves]:
                    allsaves += 1
                    compatible = False
                    try:
                        compatible = cls.is_compatible(save.p)
                    except Exception:
                        save.exception = True
                        exceptsaves += 0
                        continue
                    else:
                        save.exception = False
                    if not compatible:
                        badsaves += 1
                        try:
                            cls.save_compatible(save.p)
                            exceptok += 1
                        except Exception:
                            pass
                    
            if haveempty:
                for i in range(len(persistent.savefile)-1,-1,-1):
                    if not persistent.savefile[i]:
                        persistent.savefile.pop(i)

            if console:
                print('已完成对%s个存档的检查，其中有%s个存档被修复。' % (allsaves, badsaves))
                if exceptsaves:
                    print('其中有%s个存档出现异常，其中有%s个存档被修复。' % (exceptsaves, exceptok))

        
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
            if len(slot.plan) == 3:
                slot.plan.append(NoTask)

init python:     
            
    import pickle

    def cc(p):
        serialized_p = pickle.dumps(p)
        pygame_sdl2.scrap.put(pygame_sdl2.SCRAP_TEXT, serialized_p)

    def pp():
        serialized_p = pygame_sdl2.scrap.get(pygame_sdl2.SCRAP_TEXT)
        if serialized_p:
            p = pickle.loads(serialized_p)
            return p
        else:
            return None