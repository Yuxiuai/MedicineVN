define config.name = _("药：绝望的解决手段")

define gui.show_name = False

define config.version = "0.5.33"

define gui.about = _p("""
""")

define build.name = "Medicine"

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve

define config.after_load_transition = None
define config.end_game_transition = None


define config.window = "auto"

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

default preferences.text_cps = 20
default preferences.afm_time = 15

define config.save_directory = "Medicine-1622606859"
define config.window_icon = "gui/window_icon.png"

init python:

    build.archive('images')
    build.archive('audio')
    build.archive('scripts')
    build.archive('fonts')

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    build.classify('game/**.png', 'images')
    build.classify('game/**.jpg', 'images')
    build.classify('game/**.webm', 'images')
    build.classify('game/**.mp3', 'audio')
    build.classify('game/**.ogg', 'audio')
    build.classify('game/**.wav', 'audio')
    build.classify('game/**.flac', 'audio')
    build.classify('game/**.rpy', 'scripts')
    build.classify('game/**.rpyc', 'scripts')
    build.classify('game/**.rpyb', 'scripts')
    build.classify('game/**.rpym', 'scripts')
    build.classify('game/**.rpymc', 'scripts')
    build.classify('game/**.txt', 'scripts')
    build.classify('game/**.ttf', 'fonts')

