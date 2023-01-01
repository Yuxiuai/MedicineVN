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
            l = list(filter(lambda x: x in persistent.guide, ALLITEMS))
            sortByID(l)
            return l
        
        @classmethod
        def undone(cls):
            l = list(filter(lambda x: x not in persistent.guide, ALLITEMS))
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
            for i in ALLITEMS:
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
            l = list(filter(lambda x: x in persistent.guide, ALLEFFECTS))
            sortByID(l)
            return l
        
        @classmethod
        def undone(cls):
            l = list(filter(lambda x: x not in persistent.guide, ALLEFFECTS))
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
            for i in ALLEFFECTS:
                i.achieve()
                
        @classmethod
        def has(cls, a):
            return a in persistent.guide