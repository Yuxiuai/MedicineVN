init -20:
    default persistent.savefile = [None, None, [None, None, None, None, None, None, None, None, None, None]]

    

    default persistent.newplayer = True
    default persistent.beforename = ''

    default persistent.nowaiting = False
    default persistent.nosplash = False
    default persistent.nocharacterplot = False
    default persistent.nomedicine = False
    default persistent.unlocktesttask = False


    default persistent.PreciseDisplay = False
    default persistent.notifyDuration = 5
    default persistent.PreciseDisplayAbilities = False
    default persistent.PreciseDisplayGoal = False
    default persistent.quickAlarm = False
    default persistent.disablecharactervoice = False
    default persistent.unlockplan = False



    default persistent.highestscore2048 = 0

    default persistent.GlobalStatistics = {}

    default persistent.HallukeEnding = False
    default persistent.AcolasEnding = False
    default persistent.DeplineEnding = False
    default persistent.ne = False
    default persistent.te = False
    default persistent.ce = False
    default persistent.lastend = None

    default persistent.achievements = {}
    default persistent.runtime = 0

    define p = None
    define replaying = False
    define replaying_times = None
    define replaying_labelname = None




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
    config.layers = [ 'master', 'mask', 'transient', 'screens', 'headimage' ,'overlay']

   

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
