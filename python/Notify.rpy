init python early:


    def insertToHis(message):
        global _history_list
        h=renpy.character.HistoryEntry()
        h.kind = 'adv'
        h.who = chara_notice
        h.who_args = {'color': '#b8b8b8b4', 'style':'say_label','substitute':False}
        h.what = message
        _history_list.append(h)

    def showNotice(messages):
        for i in messages:
            insertToHis(i)
        if renpy.get_screen("screen_notify"):
            renpy.hide_screen("screen_notify")
            renpy.show_screen("screen_notify", messages)
        else:
            renpy.show_screen("screen_notify", messages) 
    
    class Notice:
        messages = []
        longmessages = []

        @classmethod
        def empty(cls):
            return not bool(cls.messages)

        @classmethod
        def add(cls, message):
            cls.messages.append(message)

        @classmethod
        def ladd(cls, message):
            cls.longmessages.append(message)

        @classmethod
        def show(cls):
            showNotice(cls.messages)
            cls.messages = []

        @classmethod
        def clear(cls):
            cls.messages = []

    


screen screen_notify(messages):

    zorder 12000
    style_prefix "info"

    vbox:
        spacing 10
        for i in range(len(messages)):
            $mes = messages[i]
            frame at screen_notify_appear(0.2 * i):
                padding (10, 5)
                text mes
                ypos gui.notify_ypos

    timer (0.2 * len(messages) + persistent.notifyDuration) action Hide('screen_notify')



transform screen_long_notify_trans:
    yoffset 600
    easein 0.5 yoffset 0

transform screen_long_notify_hide: 
    easeout 0.5 yoffset -600


screen screen_long_notify(mes):

    use barrier('screen_long_notify')
    style_prefix "info"
    zorder 12000
    
    add "gui/longnotice.png" at screen_long_notify_trans

    frame at screen_long_notify_trans:
        padding (10, 5)
        background None
        text mes text_align 0.5
        xcenter 0.5
        ycenter 0.47

label longtest:
    'start'
    $insertToHis('12345')
    call screen screen_long_notify('12345')
    'end'
    jump longtest