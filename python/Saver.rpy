init -10:
    default persistent.SaverClass = None

init -10 python:
    class Saver:
        if persistent.SaverClass is not None:
            today = dcp(persistent.SaverClass[0])
            yesterday = dcp(persistent.SaverClass[1])
            lastweek = dcp(persistent.SaverClass[2])
        else:
            today = {
                'p':None,
                'resists':[],
                'cds':[]
            }
            yesterday = {
                'p':None,
                'resists':[],
                'cds':[]
            }
            lastweek = {
                'p':None,
                'resists':[],
                'cds':[]
            }
        

        @classmethod
        def clear(cls):
            cls.today = {
                'p':None,
                'resists':[],
                'cds':[]
            }
        
            cls.yesterday = dcp(cls.today)
            cls.lastweek = dcp(cls.today)

            persistent.SaverClass = [dcp(cls.today), dcp(cls.today), dcp(cls.today)]


        @classmethod
        def clsLoad(cls):
            if persistent.SaverClass is not None:
                cls.today= dcp(persistent.SaverClass[0])
                cls.yesterday= dcp(persistent.SaverClass[1])
                cls.lastweek= dcp(persistent.SaverClass[2])


        @classmethod
        def save(cls):
            global p
            if p!=None and cls.today['p']!=None:
                if cls.today['p'].today != p.today: #如果重开本日 防止昨日的存档被覆盖成本日
                    cls.yesterday = dcp(cls.today)

            cls.today['p'] = dcp(p)

            cls.today['resists'] = []
            for i in (MedicineA, MedicineB, MedicineC):
                cls.today['resists'].append(i.resistance_)

            cls.today['cds'] = []
            unsavedItems = list(filter(lambda x: x.maxCd!=0 ,getSubclasses(Item)))
            unsavedItems.sort(key=lambda x: x.id)
            for i in unsavedItems:
                cls.today['cds'].append(i.cd)


            if p.today == 5:
                cls.lastweek = dcp(cls.today)

            persistent.SaverClass = [dcp(cls.today), dcp(cls.yesterday), dcp(cls.lastweek)]

        @classmethod
        def load(cls, slot):

            global p

            cls.clsLoad()

            if 'p' not in slot:
                renpy.error("存档出现错误！(p not in slot.)")
            if slot['p']==None:
                renpy.error("存档出现错误！(p equals None.)")
            p = dcp(slot['p'])



            if 'resists' not in slot:
                renpy.error("存档出现错误！(resists not in slot.)")

            if slot['resists'][0]==None:
                renpy.error("存档出现错误！(resists 0 equals None.)")

            MedicineA.resistance_ = slot['resists'][0]

            if slot['resists'][1]==None:
                renpy.error("存档出现错误！(resists 1 equals None.)")

            MedicineB.resistance_ = slot['resists'][1]

            if slot['resists'][2]==None:
                renpy.error("存档出现错误！(resists 2 equals None.)")

            MedicineC.resistance_ = slot['resists'][2]

            unloadedItems = list(filter(lambda x: x.maxCd!=0 ,getSubclasses(Item)))
            unloadedItems.sort(key=lambda x: x.id)

            if 'cds' not in slot:
                renpy.error("存档出现错误！(cds not in slot.)")

            for i in range(len(unloadedItems)):
                if slot['cds'][i]==None:
                    renpy.error("存档出现错误！(cds %s equals None.)" % i)
                unloadedItems[i].cd = slot['cds'][i]
            

