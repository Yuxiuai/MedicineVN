define config.name = _("药：绝望的解决手段")

define gui.show_name = False

define config.version = "0.4.2.1400"

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

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    build.classify('game/images/**.png', 'archive')
    build.classify('game/images/**.jpg', 'archive')
    build.classify('game/audio/**.mp3', 'archive')
    build.classify('game/audio/**.ogg', 'archive')
    build.classify('game/audio/**.wav', 'archive')
    build.classify('game/audio/**.flac', 'archive')
    build.classify('game/**.rpy', 'archive')
    build.classify('game/**.rpyc', 'archive')
    build.classify('game/**.ttf', 'archive')

    build.documentation('*.html')
    build.documentation('*.txt')
