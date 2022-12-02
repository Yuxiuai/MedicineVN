init -10 python early:
    class Save:

        @classmethod
        def clear(cls):
            persistent.savefile[0] = None
            persistent.savefile[1] = None

        @classmethod
        def default(cls):
            persistent.savefile = [None, None, [None, None, None, None, None, None, None, None, None, None]]

        @classmethod
        def save(cls, player):
            t = r2(renpy.get_game_runtime())
            persistent.runtime += t
            renpy.clear_game_runtime()

            if persistent.savefile[0] != None:
                if persistent.savefile[0].today == player.today:
                    return

            persistent.savefile[1] = dcp(persistent.savefile[0])
            persistent.savefile[0] = dcp(player)

            renpy.save_persistent()

        @classmethod
        def load(cls, slot):
            global p
            sh()
            p = dcp(slot)
            cls.clear()
            persistent.savefile[0] = dcp(p)
            renpy.jump_out_of_context("afterload")

        @classmethod
        def record(cls, slot):
            import time
            slot.savetime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            if None not in persistent.savefile[2]:
                persistent.savefile[2][-1] = dcp(slot)
            else:
                for i in range(len(persistent.savefile[2])):
                    if not persistent.savefile[2][i]:
                        persistent.savefile[2][i] = dcp(slot)
                        break
            renpy.save_persistent()

        @classmethod
        def record_poz(cls, poz):
            import time
            persistent.savefile[2][poz] = dcp(persistent.savefile[0])
            persistent.savefile[2][poz].savetime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

            renpy.save_persistent()
            

        @classmethod
        def delete(cls, pos):
            persistent.savefile[2][pos] = None

            renpy.save_persistent()

