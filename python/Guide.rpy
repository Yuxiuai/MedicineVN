init -20:

    default persistent.guide = {}

init python early:

    
    class GuideI:

        @classmethod
        def unlock(cls, a):
            if a not in persistent.guide:
                import time
                persistent.guide[a] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

        @classmethod
        def done(cls):
            l = list(filter(lambda x: x in persistent.guide, getSubclasses(Item)))
            sortByID(l)
            return l
        
        @classmethod
        def undone(cls):
            l = list(filter(lambda x: x not in persistent.guide, getSubclasses(Item)))
            sortByID(l)
            return l

        @classmethod
        def time(cls, a):
            if a not in persistent.guide:
                return 0
            return persistent.guide[a]
        
        @classmethod
        def clear(cls):
            persistent.guide = {}
        
        @classmethod
        def all(cls):
            for i in getSubclasses(Item):
                i.achieve()
                
        @classmethod
        def has(cls, a):
            return a in persistent.guide
    

    class GuideE:

        @classmethod
        def unlock(cls, a):
            if a not in persistent.guide:
                import time
                persistent.guide[a] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

        @classmethod
        def done(cls):
            l = list(filter(lambda x: x in persistent.guide, getSubclasses(Effect)))
            sortByID(l)
            return l
        
        @classmethod
        def undone(cls):
            l = list(filter(lambda x: x not in persistent.guide, getSubclasses(Effect)))
            sortByID(l)
            return l

        @classmethod
        def time(cls, a):
            if a not in persistent.guide:
                return 0
            return persistent.guide[a]
        
        @classmethod
        def clear(cls):
            persistent.guide = {}
        
        @classmethod
        def all(cls):
            for i in getSubclasses(Effect):
                i.achieve()
                
        @classmethod
        def has(cls, a):
            return a in persistent.guide