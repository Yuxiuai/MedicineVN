
define -500 audio.themedicine = "<from 0.5>audio/music/The_Medicine.mp3"
define -500 audio.concretejungle = "<from 0.5>audio/music/Concrete_Jungle.mp3"
define -500 audio.solitus = "<from 0.4>audio/music/Solitus.mp3"
define -500 audio.depline = "<from 0.4>audio/music/Depline.mp3"
define -500 audio.halluke = "<from 0.6>audio/music/Halluke.mp3"
define -500 audio.acolas = "<from 0.7>audio/music/Acolas.mp3"
define -500 audio.nameyourself = "<from 0.5>audio/music/Name_Yourself.mp3"
define -500 audio.survivingdawn = "audio/music/Surviving_Dawn.mp3"
define -500 audio.rareleisure = "audio/music/Rare_Leisure.mp3"
define -500 audio.impendingdeath = "<from 0.6>audio/music/Impending_Death.mp3"
define -500 audio.varsitylife = "audio/music/Varsity_Life.mp3"
define -500 audio.brightanticipations = "audio/music/Bright_Anticipations.mp3"
define -500 audio.sliceoflife = "audio/music/Slice_of_Life.mp3"
define -500 audio.smellsofdisinfectant = "<from 7>audio/music/Smells_of_Disinfectant.mp3"
define -500 audio.meaninglessemotion = "audio/music/Meaningless_Emotion.mp3"

define -500 audio.credits = "audio/music/Credits.mp3"

define -500 audio.cursor = "audio/sound/cursor.mp3"
define -500 audio.error = "audio/sound/error.mp3"
define -500 audio.getmedicine = "audio/sound/getmedicine.ogg"
define -500 audio.unlocking = "audio/sound/unlocking.wav"
define -500 audio.suicide = "audio/sound/suicide.wav"
define -500 audio.alarm = "audio/sound/alarm.mp3"
define -500 audio.button = "audio/sound/button.mp3"
define -500 audio.loading = "audio/sound/loading.mp3"
define -500 audio.interruption = "audio/sound/interruption.mp3"
define -500 audio.drop = "audio/sound/drop.mp3"
define -500 audio.insist = "audio/sound/insist.mp3"
define -500 audio.finishclass = "audio/sound/finishclass.mp3"
define -500 audio.knocktable = "audio/sound/knocktable.wav"
define -500 audio.sfx2048 = "audio/sound/2048.wav"
define -500 audio.masturbation = "audio/sound/masturbation.ogg"
define -500 audio.door = "audio/sound/door.mp3"
define -500 audio.heartbeat = "audio/sound/heartbeat.ogg"
define -500 audio.pee = "audio/sound/pee.wav"
define -500 audio.badminton = "audio/sound/badminton.mp3"

define -500 audio.increase = "audio/sound/increase.mp3"
define -500 audio.decrease = "audio/sound/decrease.mp3"

define -500 audio.l1 = "audio/sound/leviathan/leviathan1.wav"
define -500 audio.l2 = "audio/sound/leviathan/leviathan2.wav"
define -500 audio.l3 = "audio/sound/leviathan/leviathan3.wav"
define -500 audio.l4 = "audio/sound/leviathan/leviathan4.wav"
define -500 audio.l5 = "audio/sound/leviathan/leviathan5.wav"
define -500 audio.l6 = "audio/sound/leviathan/leviathan6.wav"
define -500 audio.l7 = "audio/sound/leviathan/leviathan7.wav"
define -500 audio.l8 = "audio/sound/leviathan/leviathan8.wav"
define -500 audio.l9 = "audio/sound/leviathan/leviathan9.wav"
define -500 audio.l10 = "audio/sound/leviathan/leviathan10.wav"
define -500 audio.l11 = "audio/sound/leviathan/leviathan11.wav"
define -500 audio.l12 = "audio/sound/leviathan/leviathan12.wav"
define -500 audio.l13 = "audio/sound/leviathan/leviathan13.wav"
define -500 audio.l14 = "audio/sound/leviathan/leviathan14.wav"
define -500 audio.l15 = "audio/sound/leviathan/leviathan15.wav"
define -500 audio.Leviathan = "audio/sound/leviathan/Leviathan.mp3"
define -500 audio.Ultimate = "audio/sound/leviathan/Ultimate.mp3"

init python:
    mr= MusicRoom(fadein=1.0, loop=True, single_track=True, shuffle=False)
    mr.add(audio.themedicine, always_unlocked=True)
    mr.add(audio.solitus)
    mr.add(audio.halluke)
    mr.add(audio.depline)
    mr.add(audio.acolas)
    mr.add(audio.nameyourself)
    mr.add(audio.survivingdawn)
    mr.add(audio.rareleisure)
    mr.add(audio.impendingdeath)
    mr.add(audio.concretejungle)
    mr.add(audio.varsitylife)
    mr.add(audio.brightanticipations)
    mr.add(audio.sliceoflife)
    mr.add(audio.smellsofdisinfectant)
    mr.add(audio.meaninglessemotion)
    mr.add(audio.credits)



init python:
    dictMusicCommet={
        'Acolas':'阿克拉斯\n也许放纵自己的自毁倾向也算是一种放纵吧。',
        'Bright Anticipations':'美好的期望\n最痛苦的人给予了最真诚的爱，重压之下也有美好的期望。',
        'City Sunshine':'都市阳光\n这座城市也是有美好的阳光存在的，抬头看看天空吧。',
        'Concrete Jungle':'水泥森林\n我们需要的是真正的森林，是可以自由呼吸的森林。',
        'Depline':'德普林\n名气越大，内心也就越空虚，越是要用某些不正当的手段获取存在感。',
        'Halluke':'哈卢克\n整个世界都是一场盛大的幻觉，即便是所谓的爱。',
        'Surviving Dawn':'幸存的黎明\n你又一次成功地活了下来，但这是好事，还是坏事？',
        'Impending Death':'逼近的死亡\n生乃一条无尽危路，唯有死在尽头停驻。',
        'Name Yourself':'取名\n欢快活泼的音乐，想必这个游戏也是一样快乐的吧？',
        'Rare Leisure':'难得的空闲\n至少你还有双休日，更多的打工人甚至全年无休。',
        'Solitus':'索利图斯\n存在主义和参与感，即便付出大于回报也让他感到生命的可贵。',
        'The Medicine':'药\n绝望迫近之时，只有它是你和他之间的的唯一解药。',
        'Varsity Life':'大学生活\n虽然Solitus明明可以假装自己是个游泳课的学生，不过估计他没这个胆。',
        'Slice of Life':'生活的一部分\n虽然Solitus肯定希望他的周末是在床上度过的，但最好还是把他拉出去溜达溜达。',
        'Smells of Disinfectant':'消毒水的气味\n你害怕这里吗？但你不得不来。',
        'Meaningless Emotion':'无意义的感情\n收起无聊的自我感动吧，在他眼里你什么也不是。',
        'Credits':'鸣谢\n感谢游玩本作，今后也请多多指教。'
    }