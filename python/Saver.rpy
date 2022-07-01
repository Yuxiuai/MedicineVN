init -10 python early:
    class Saver:

        @classmethod
        def clear(cls):
            persistent.SaverClass = [None, None, None]

        @classmethod
        def save(cls, player):

            if persistent.SaverClass[0] != None:
                if persistent.SaverClass[0].today == player.today:
                    return

            persistent.SaverClass[1] = dcp(persistent.SaverClass[0])

            persistent.SaverClass[0] = dcp(player)

            if player.today == 5:
                persistent.SaverClass[2] = dcp(player)
