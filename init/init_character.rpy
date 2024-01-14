init python:
    renpy.music.register_channel("chara_voice", mixer= "voice", loop=True)

    def say_voice(event, interact, **kwargs):
        if not interact:
            return
        if event == "show" and not persistent.disablecharactervoice:
            renpy.sound.play("audio/sound/say.wav", loop=True, channel="chara_voice")
        elif event == "slow_done":
            renpy.sound.stop(channel="chara_voice")
        #if event == "end":
        #    renpy.sound.play("audio/sound/error.mp3", channel="sound")


define config.character_callback = say_voice
define chara_notice = Character("Notice")

#Solitus
define s = Character("[p.name]", color="#9500ff")

define so = Character('???', color="#9500ff")

#Halluke
define h = Character('Halluke', color="#f5f2eb")
define ha = Character('???', color="#f5f2eb")

#Depline
define d = Character('Depline', color="#FFD700")
define de = Character('???', color="#FFD700")
define aka = Character('Akamatsu', color="#FFD700")

#Acolas
define a = Character('Acolas', color="#f92828")
define ac = Character('???', color="#f92828")

define destot = Character('???', color="#33ffbe")
define des = Character('Destot', color="#33ffbe")




define ar = Character('Arnel', color="#ff0000")
define nurse = Character('Nurse', color="#FFC0CB")
define teac = Character('Teacher', color="#ffffff")
define doctor = Character('Doctor', color="#ffffff")

define lady = Character('Lady', color="#DDA0DD")
define man = Character('Man', color="#6495ED")

define ol1 = Character('OfficeLady1', color="#DDA0DD")
define ol2 = Character('OfficeLady2', color="#DDA0DD")

define mom = Character('Mom', color="#DDA0DD")
define dad = Character('Dad', color="#6495ED")

define zaster = Character('Zaster', color="#f0e68c")

define unk = Character('???', color="#ffffff")
define serote = Character('???', color="#F29855")


define pathos = Character('Pathos', color="#516589")
define decay = Character('Decay', color="#50B097")
define creefo_ = Character('Creefo', color="#8B0000")
define creefo = Character('Creefo', color="#8B0000")

define yxi = Character('聿修', color="#ffffff")