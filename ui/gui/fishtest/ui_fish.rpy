init python:
    
    class FishGame:
        pool = {
            'pond':(50,300,0),
            'lake':(100,100,10),
            'trash':(0,1000,0),
            'treasure':(1000,0,0),
            'gold':(0,0,1000),
        }


        def __init__(self, player):
            self.pos = 0
            self.direction = rcd((1.0, -1.0))
            self.hard = ra(player, 5, 25)*0.1
            self.time = 0
            self.point = ra(player, 20, 50)

            self.fishpower = player.fishpower
            self.fishpoint = player.fishpoint
            self.fishcrit = player.fishcrit
            self.hasA1 = FishingAccessory1.has(player)
            self.hasA4 = FishingAccessory4.has(player)
            self.linebreak = False
            self.gamelose = False
            self.gamewin = False

            
        @property
        def speed(self):
            return 0.75*(1+0.01*self.fishpower)/self.hard

        def timef(self):
            self.time += 1

        def prob(self, pos):
            treasure, trash, legendary = self.pool[pos]
            
            if self.hasA4:
                treasure *= 1.33
                trash *= 0.67
                legendary *= 1.33
            
            treasure *= 1 + self.fishpower*0.01
            trash *= 1 - self.fishpower*0.01
            legendary *= 1 + self.fishpower*0.01


            return treasure/10, trash/10, legendary/10, (1000-treasure-trash-legendary)/10


        def getfish(self, player, pos):
            treasure, trash, legendary = self.pool[pos]
            
            if self.hasA4:
                treasure *= 1.33
                trash *= 0.67
                legendary *= 1.33
            
            treasure *= 1 + player.fishpower*0.01
            trash *= 1 - player.fishpower*0.01
            legendary *= 1 + player.fishpower*0.01

            fishpool = ['treasure'] * int(treasure) + ['trash'] * int(trash) + ['legendary'] * int(legendary) + ['fish'] * int(1000-treasure-trash-legendary)
            fish = rca(player, fishpool)
            

            if fish == 'treasure':
                treasureitems = [FishingAccessory1,FishingAccessory2,FishingAccessory3,FishingAccessory4,FishingItem1,FishingItem2]
                oktreasureitems = list(filter(lambda x: not x.has(player), treasureitems))
                if not oktreasureitems:
                    oktreasureitems = [FishingItem4, FishingItem3]
                fish = rca(player, oktreasureitems)
            elif fish == 'trash':
                trashitems = [FishingTrash1,FishingTrash2,FishingTrash3,FishingTrash4,FishingTrash5]
                fish = rca(player, trashitems)
            elif fish == 'legendary':
                fish = GoldFish
            else:
                fish = RawFish(player)
                fish.qty = self.weight()


            return fish


        def touch(self):
            crit = False
            point = rca(p, (1,1,1,1,2,2,2,3))
            point += self.fishpoint
            if rra(p, self.fishcrit):
                point *= 2
                crit = True
            Damageshow.show(point, crit)
            self.point += point
            if not self.hasA1:
                if rra(p, 0.5+self.time*0.1):
                    self.linebreak = True
            if self.point >= 99:
                self.gamewin = True
            

        def pointdown(self):
            self.point -= 1
            if self.point <= 0:
                self.gamelose = True

        def weight(self):
            return r2(self.hard*(1+0.01*self.fishpower))


        def move(self):
            import random
            if random.randint(0, 4) == 0:
                pass
            elif self.direction == -1:
                self.pos = max(-500, random.uniform(self.pos-self.hard*150, self.pos-self.hard*20))
            elif self.direction == 1:
                self.pos = min(500, random.uniform(self.pos+self.hard*20, self.pos+self.hard*150))
            return self.pos

        def face(self):
            import random
            min_distance = -500
            max_distance = 500
            self.pos = max(min(self.pos, max_distance), min_distance)
            probability = (self.pos - min_distance) / (max_distance - min_distance)
            if random.random() < probability:
                self.direction = -1.0
            else:
                self.direction = 1.0
            return self.direction

        def fish(self, player):
            f = RawFish(player)
            f.qty = self.hard
            GuideI.unlock(RawFish)
            player.items.append(f)
            Notice.add(_('获得新物品：生鱼！\n质量为%s！') % self.hard)
            Notice.show()
        
        def harden(self):
            self.hard += 0.1
        
        def simplify(self):
            self.hard -= 0.1
            
    
    def random_control():
        clist = (audio.control1, audio.control2, audio.control3, audio.control4, audio.control5, audio.control6)
        play_audio(rcd(clist))

    def random_fish():
        clist = (audio.fish1, audio.fish2, audio.fish3, audio.fish4, audio.fish5, audio.fish6)
        play_audio(rcd(clist))

    def fish_bar_color(value):
        if value < 0:
            value = 0
        elif value > 100:
            value = 100
        red = int((100 - value) * 255 / 100)
        green = int(value * 255 / 100)
        return '#{:02x}{:02x}00'.format(red, green)



transform fish_trans(fishgame):
    xzoom fishgame.face()
    easein fishgame.speed xoffset fishgame.move()
    easein 0.1 xzoom fishgame.face()
    easein fishgame.speed xoffset fishgame.move()
    easein 0.1 xzoom fishgame.face()
    easein fishgame.speed xoffset fishgame.move()
    easein 0.1 xzoom fishgame.face()
    easein fishgame.speed xoffset fishgame.move()
    easein 0.1 xzoom fishgame.face()
    easein fishgame.speed xoffset fishgame.move()
    easein 0.1 xzoom fishgame.face()
    easein fishgame.speed xoffset fishgame.move()
    easein 0.1 xzoom fishgame.face()
    easein fishgame.speed xoffset fishgame.move()
    easein 0.1 xzoom fishgame.face()
    easein fishgame.speed xoffset fishgame.move()
    easein 0.1 xzoom fishgame.face()
    easein fishgame.speed xoffset fishgame.move()
    easein 0.1 xzoom fishgame.face()
    easein fishgame.speed xoffset fishgame.move()
    easein 0.1 xzoom fishgame.face()
    easein fishgame.speed xoffset fishgame.move()
    easein 0.1 xzoom fishgame.face()
    easein fishgame.speed xoffset fishgame.move()
    easein 0.1 xzoom fishgame.face()
    easein fishgame.speed xoffset fishgame.move()
    easein 0.1 xzoom fishgame.face()
    easein fishgame.speed xoffset fishgame.move()
    easein 0.1 xzoom fishgame.face()
    easein fishgame.speed xoffset fishgame.move()
    easein 0.1 xzoom fishgame.face()
    easein fishgame.speed xoffset fishgame.move()
    easein 0.1 xzoom fishgame.face()
    easein fishgame.speed xoffset fishgame.move()
    easein 0.1 xzoom fishgame.face()
    easein fishgame.speed xoffset fishgame.move()
    easein 0.1 xzoom fishgame.face()
    easein fishgame.speed xoffset fishgame.move()
    easein 0.1 xzoom fishgame.face()
    easein fishgame.speed xoffset fishgame.move()
    easein 0.1 xzoom fishgame.face()
    easein fishgame.speed xoffset fishgame.move()
    easein 0.1 xzoom fishgame.face()
    easein fishgame.speed xoffset fishgame.move()
    easein 0.1 xzoom fishgame.face()
    easein fishgame.speed xoffset fishgame.move()
    easein 0.1 xzoom fishgame.face()
    easein fishgame.speed xoffset fishgame.move()
    easein 0.1 xzoom fishgame.face()
    easein fishgame.speed xoffset fishgame.move()
    easein 0.1 xzoom fishgame.face()
    easein fishgame.speed xoffset fishgame.move()
    easein 0.1 xzoom fishgame.face()
    easein fishgame.speed xoffset fishgame.move()
    easein 0.1 xzoom fishgame.face()
    easein fishgame.speed xoffset fishgame.move()
    easein 0.1 xzoom fishgame.face()
    easein fishgame.speed xoffset fishgame.move()
    easein 0.1 xzoom fishgame.face()
    easein fishgame.speed xoffset fishgame.move()
    easein 0.1 xzoom fishgame.face()


        
    repeat



transform trans_fish_bar_color(point):
    matrixcolor TintMatrix(fish_bar_color(point))

screen screen_fishing(player, fishgame, poz):
    default rightpos = False
    

    textbutton '点击游动的鱼！' style 'white':
        action Function(fishgame.harden)
        alternate Function(fishgame.simplify)
        xcenter 0.5
        ycenter 0.4
        text_size 35
    
    imagebutton idle 'gui/object/fish.png' at fish_trans(fishgame):
        action Function(fishgame.touch), Function(random_control)
        hovered SetLocalVariable('rightpos', True)
        unhovered SetLocalVariable('rightpos', False)
        xcenter 0.5  
        ycenter 0.5

    bar:
        value fishgame.point
        range 100
        xcenter 0.5
        ycenter 0.6
        xsize 1000
        style 'solid_bar'
        at trans_fish_bar_color(fishgame.point)

    textbutton '放弃' style 'white':
        action Return(),Hide('screen_fishing',transition=dissolve),Function(player.rtn, 0)
        xcenter 0.5
        ycenter 0.7
    
    timer fishgame.speed:
        action [
            Function(fishgame.pointdown), 
            If(fishgame.linebreak, true=[Return(),Hide('screen_fishing',transition=dissolve),Function(player.rtn, -2)]), 
            If(fishgame.gamelose, true=[Return(),Hide('screen_fishing',transition=dissolve),Function(player.rtn, -1)]),
            If(fishgame.gamewin, true=[Return(),Hide('screen_fishing',transition=dissolve),Function(player.rtn, fishgame.getfish(player, poz))]),
            ]
        repeat True

    timer 1 action Function(fishgame.timef) repeat True

    if rightpos:
        key 'K_SPACE' action Function(fishgame.touch), Function(random_control)


