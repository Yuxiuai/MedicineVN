init python early:

    def insertToHis(message):
        global _history_list
        h=renpy.character.HistoryEntry()
        h.kind = 'adv'
        h.who = None
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

        @classmethod
        def empty(cls):
            return not bool(cls.messages)

        @classmethod
        def add(cls, message):
            cls.messages.append(message)

        @classmethod
        def show(cls):
            showNotice(cls.messages)
            cls.messages = []

        @classmethod
        def clear(cls):
            cls.messages = []

    


screen screen_notify(messages):

    zorder 100
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

            
