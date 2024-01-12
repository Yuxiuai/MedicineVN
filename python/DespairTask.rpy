init python early:
    class DespairTask:
        id = None
        name = None
        kind = None
        info = None
        ad = None

        @classmethod
        def checkAvailable(cls, player, day, time):
            return True

        @classmethod
        def hasplot(cls, player):
            return False

        @classmethod
        def executeTask(cls, player):
            pass

        @classmethod
        def isUnlocked(cls, player):
            return True

        @staticmethod
        def gt():
            import random
            length=random.randint(15, 45)
            gt = "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽž"
            output = "{font=arial.ttf}"
            for x in range(length):
                output += random.choice(gt)
            output += "{/font}"
            return output

    class DespairWaiting(DespairTask):
        id = 100
        name = _('等待')
        kind = _('日程')
        info = _('恢复少量精神状态。')
        ad = _('没人会救你们的。')

        @classmethod
        def executeTask(cls, player):
            reco = r2(-0.25 * player.mental + 35)
            
            
            player.gain_mental(reco, stat=cls.name)
            player.updateAfterTask(cls)
            if player.p2:
                player.p2.updateAfterTask(cls)
            renpy.jump("DespairWaiting_result")

    class DespairObserve(DespairTask):
        id = 101
        name = _('观察状况')
        kind = _('日程')
        info = _('检查对方的状态，或是聊聊天。')
        ad = _('放任他的死亡对你也没有害处，你不是一直讨厌他吗？')

        @classmethod
        def executeTask(cls, player):
            player.updateAfterTask(cls)
            if player.p2:
                player.p2.updateAfterTask(cls)
            renpy.jump("DespairObserve_result")

    class DespairDistribute(DespairTask):
        id = 102
        name = _('分发药物')
        kind = _('日程')
        info = _('对他使用药物以减轻对方的痛苦。')
        ad = _('你只有这些药了，而他只是个将死之人，分给他的话，你很可能撑不到救援哦？')
            
        @classmethod
        def executeTask(cls, player):            
            player.updateAfterTask(cls)
            if player.p2:
                player.p2.updateAfterTask(cls)
            renpy.jump("DespairDistribute_result")