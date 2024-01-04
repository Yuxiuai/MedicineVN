init python:

    import threading
    from time import sleep

    def waitandplayaudio(wait, audio):
        sleep(wait)
        renpy.music.play(audio, channel='audio')



    class Workgame_Block:
        ALLCOLORS = ['1', '2', '3', '4', '5', '6']

        def __init__(self, color):
            #self.number = None
            self.touched = False
            self.color = color
            self.status = 0  # 0 正常 -1 被消除

        @classmethod
        def default(cls):
            c = rcd(cls.ALLCOLORS)
            l = [cls(c) for _ in range(rd(3, 6))]
            
            return l
        
        @property
        def icon(self):
            return 'gui/game/%s_%s.png' % (self.color, '%s')



    class Workgame:
        mintimes = 4
        maxtimes = 6
        def __init__(self):
            self.blocks = []
            self.log = [Workgame_Start(None)]
            self.step = 0
            self.chain = 0
            self.default()

        def default(self):
            self.blocks = []
            for _ in range(rd(self.mintimes, self.maxtimes)):
                sublist = Workgame_Block.default()
                self.blocks[rd(0, len(self.blocks)) : 0] = sublist
            #for i, item in enumerate(self.blocks):
            #    item.number = i

        def next(self, ind):
            for i in range(ind+1, len(self.blocks)):
                if self.blocks[i].status == 0:
                    return i
            return -1
        
        def before(self, ind):
            for i in range(ind-1, -1, -1):
                if self.blocks[i].status == 0:
                    return i
            return -1

        @property
        def win(self):
            return not (0 in [x.status for x in self.blocks])

        def printLog(self):
            for i in self.log:
                i.info()


        def touch(self, ind):  # 将方块状态置为-1

            def search(self, ind, color):
                
                if self.blocks[ind].color != color or self.blocks[ind].status == -1:
                    return
                self.blocks[ind].status = -1
                self.blocks[ind].touched = True
                
                self.addLog(Workgame_Dissovle(ind))
                if self.next(ind) != -1:
                    search(self, self.next(ind), color)
                if self.before(ind) != -1:
                    search(self, self.before(ind), color)

            if len(self.blocks) == 1:
                self.blocks = []
                return

            

            search(self, ind, self.blocks[ind].color)

            self.check()
            

        def check(self):
            located = False
            start = None
            end = None
            touchs = 0
            for i, item in enumerate(self.blocks):
                if item.touched:
                    if not located:
                        located = True
                        start = i
                    item.touched = False
                    touchs += 1
                    end = i
            if located:
                if self.before(start) != -1 and self.next(end) != -1:
                    if self.blocks[self.before(start)].color == self.blocks[self.next(end)].color:
                        self.addLog(Workgame_Waiting(None))
                        self.touch(self.before(start))
            if touchs:
                self.addLog(Workgame_Cleared(None, touchs))

        def end(self):
            score = 0
            chain = -1
            for i in range(len(self.log)-1, -1, -1):
                if type(self.log[i]) == Workgame_Cleared:
                    score += self.log[i].value
                    chain += 1
                elif type(self.log[i]) == Workgame_End:
                    break
            self.step += 1
            self.addLog(Workgame_Score(None, score, chain))
            self.addLog(Workgame_End(None))

            if self.win:
                self.addLog(Workgame_Win(None, self.step))
                #self.printLog()




        def addLog(self, log):
            if not self.log:
                log.time = 0.1
            elif type(log) == Workgame_End:
                pass
            elif type(log) == Workgame_Waiting:
                log.time = self.log[-1].time + 0.33
                threading.Thread(target=waitandplayaudio, args=[log.time, audio.crush]).start()
            elif type(log) == Workgame_Dissovle:
                log.time = self.log[-1].time + 0.1
                threading.Thread(target=waitandplayaudio, args=[log.time, random_bubble()]).start()
            elif type(log) in (Workgame_Leftmove, Workgame_Cleared, Workgame_Win):
                log.time = self.log[-1].time
            elif type(log) == Workgame_Score:
                self.chain += log.chain
                
            self.log.append(log)
            

        
        def transform(self, pos):
            return list(filter(lambda x: x.pos == pos and type(x) == Workgame_Dissovle, self.log))[-1].time

    def random_bubble():
        clist = (audio.bubble1, audio.bubble2, audio.bubble3, audio.bubble4, audio.bubble5, audio.bubble6)
        return rcd(clist)