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

    def defaultAllClass():
        for i in getSubclasses(Effect):
            i.defaultClass()
        for i in getSubclasses(Item):
            i.defaultClass()
        for i in getSubclasses(Task):
            i.defaultClass()
        for i in getSubclasses(GymTask):
            i.defaultClass()

    

init -2:
    define config.layers = [ 'master', 'transient', 'screens', 'headimage' ,'overlay']

    default persistent.newplayer = True

    default persistent.nowaiting = False
    default persistent.nosplash = False
    default persistent.noplot = True
    default persistent.nomedicine = False


    default persistent.PreciseDisplay = False
    default persistent.notifyDuration = 5
    default persistent.PreciseDisplayAbilities = False
    default persistent.PreciseDisplayGoal = False



    default persistent.highestscore2048 = 0

    

    default persistent.HallukeEnding = False
    default persistent.AcolasEnding = False
    default persistent.DeplineEnding = False
    default persistent.ne = False
    default persistent.te = False

    default persistent.t = 0

    define replaying = False