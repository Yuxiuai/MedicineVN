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

    def solitus_voice(event, interact, **kwargs):
        if not interact:
            return
        if event == "show" and not persistent.disablecharactervoice:
            renpy.sound.play("audio/sound/voice_solitus.mp3", loop=True, channel="chara_voice")
        elif event == "slow_done":
            renpy.sound.stop(channel="chara_voice")
        #if event == "end":
        #    renpy.sound.play("audio/sound/error.mp3", channel="sound")
    
    def halluke_voice(event, interact, **kwargs):
        if not interact:
            return
        if event == "show" and not persistent.disablecharactervoice:
            renpy.sound.play("audio/sound/voice_halluke.mp3", loop=True, channel="chara_voice")
        elif event == "slow_done":
            renpy.sound.stop(channel="chara_voice")
        #if event == "end":
        #    renpy.sound.play("audio/sound/error.mp3", channel="sound")

    def acolas_voice(event, interact, **kwargs):
        if not interact:
            return
        if event == "show" and not persistent.disablecharactervoice:
            renpy.sound.play("audio/sound/voice_acolas.mp3", loop=True, channel="chara_voice")
        elif event == "slow_done":
            renpy.sound.stop(channel="chara_voice")
        #if event == "end":
        #    renpy.sound.play("audio/sound/error.mp3", channel="sound")
    
    def pathos_voice(event, interact, **kwargs):
        if not interact:
            return
        if event == "show" and not persistent.disablecharactervoice:
            renpy.sound.play("audio/sound/voice_pathos.mp3", loop=True, channel="chara_voice")
        elif event == "slow_done":
            renpy.sound.stop(channel="chara_voice")
        #if event == "end":
        #    renpy.sound.play("audio/sound/error.mp3", channel="sound")

define config.character_callback = say_voice


#Solitus
define s = Character("[p.name]", color="#9500ff", callback=solitus_voice)

define so = Character('???', color="#9500ff", callback=solitus_voice)

#Halluke
define h = Character('Halluke', color="#f5f2eb", callback=halluke_voice)
define ha = Character('???', color="#f5f2eb", callback=halluke_voice)

#Depline
define d = Character('Depline', color="#FFD700")
define de = Character('???', color="#FFD700")
define aka = Character('Akamatsu', color="#FFD700")

#Acolas
define a = Character('Acolas', color="#f92828", callback=acolas_voice)
define ac = Character('???', color="#f92828", callback=acolas_voice)

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


define pathos = Character('Pathos', color="#516589", callback=pathos_voice)
define decay = Character('Decay', color="#50B097")


