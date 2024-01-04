init -20:
    default persistent.savefile = []

    default persistent.main_menu_theme = Theme_train


    default persistent.newplayer = True
    default persistent.beforename = ''

    default persistent.nowaiting = False
    default persistent.noloading = False
    default persistent.nosplash = False
    default persistent.nocharacterplot = False
    default persistent.nomedicine = False
    default persistent.unlocktesttask = False
    default persistent.unlockcharacterplot = False


    default persistent.PreciseMedDisplay = False
    default persistent.notifyDuration = 5
    default persistent.PreciseDisplayAbilities = False
    default persistent.PreciseDisplayGoal = False
    default persistent.noBrokenItem = False
    default persistent.disablecharactervoice = False
    default persistent.unlockplan = False
    default persistent.replymessagesquickly = False
    default persistent.actionquickly = False
    default persistent.forbidnostarquickitem = False
    default persistent.noannoyhalluke = False
    default persistent.nosolitussprite = False
    default persistent.allowquitunique = False
    default persistent.clearscreenwhenplot = False
    default persistent.diangunlevi = False

    default persistent.uiItemsSorted = 1



    default persistent.sponsor = False

    default persistent.te_weekday = 3
    default persistent.unlocked_items = []


    default persistent.highestscore2048 = 0

    default persistent.GlobalStatistics = {}
    default persistent.GlobalStatisticso = {}

    default persistent.lastend = None

    default persistent.achievements = {}
    default persistent.runtime = 0
    
    default persistent.highestscore = 0
    default persistent.gametimes = 0

    default persistent.writerendname = None

    define p = None
    define replaying = False
    define replaying_times = None
    define replaying_args = None

    define calling = False

    default persistent.loadslot = None

    define loading = False

    define config.default_music_volume = 0.5
    #define config.quit_action = Quit(False)#[Function(renpy.scene,layer='headimage'),Show(screen='quit_screen')]



init python:
    config.developer = "auto"
    config.has_autosave = False
    config.has_quicksave = False
    config.rollback_enabled = False
    config.autosave_on_choice = False

    config.main_menu_music = audio.themedicine
    config.end_game_transition = dissolve
    config.end_splash_transition = dissolve
    config.enter_transition = dissolve
    config.exit_transition = dissolve
    config.game_main_transition = dissolve
    config.intra_transition = dissolve
    config.main_game_transition = dissolve  
    config.layers = ['master', 'mask', 'transient', 'screens', 'headimage' ,'overlay']
    config.menu_clear_layers = ['headimage']

    ALLEFFECTS = getSubclasses(Effect)
    ALLITEMS = getSubclasses(Item)
    ALLITEMS.remove(UnfinishedCommission)
    ALLITEMS.remove(FinishedCommission)
    #ALLITEMS.remove(Item)
    ALLACHIEVEMENTS = list(filter(lambda x: not x.hide, getSubclasses(Achievement)))
    ALLHIDEACHIEVEMENTS = list(filter(lambda x: x.hide and x.id < 10000, getSubclasses(Achievement)))
    ALLTASKS = getSubclasses(Task)
    ALLGYMTASKS = getSubclasses(GymTask)
    ALLBOOKS = getSubclasses(BookBase)
    PLAYER_DIR = dir(Player())
    ALLBGS = [x for x in renpy.list_files() if 'images/bg/' in x]
    LENALLBGS = len(ALLBGS)


        


   

    def pause(time=None):
        global _windows_hidden
        if not time:
            _windows_hidden = True
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            _windows_hidden = False
            return
        if time <= 0: return
        _windows_hidden = True
        renpy.pause(delay=time,hard=True)
        _windows_hidden = False


screen quit_screen:

    #$renpy.with_statement(None)
    modal True
    tag menu

    zorder 99999

    style_prefix "transparent"


    add "gui/overlay/confirm.png"

    frame:
        xalign .5
        yalign .5
        padding (60, 40)
        background '#0000004f'

        has vbox:
            xalign .5
            yalign .5
            spacing 45

        label "是否退出游戏？":
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 150

            textbutton _("{size=-3}确定{/size}") action Quit(confirm=False)
            textbutton _("{size=-3}取消{/size}") action Hide("quit_screen")


    key "game_menu" action Hide("quit_screen")