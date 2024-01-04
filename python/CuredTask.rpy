init python early:
    class CuredTask:
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

    class CuredWork(CuredTask):
        id = 100
        name = _('工作')
        kind = _('日程')
        info = CuredTask.gt()
        ad = CuredTask.gt()

        @classmethod
        def checkAvailable(cls, player, day, time):
            if player.onVacation or time == 2:
                return _('是该休息的时候。')
            return True

        @classmethod
        def executeTask(cls, player):
            player.onOutside = False
            player.onVacation = False
            cons = r2(30 * f())
            a = r2(player.goal * ra(player, 10, 12) * 0.01)
            player.gain_mental(-cons)
            player.achievedGoal += a
            Notice.add(_('消耗了%s点精神状态。') % cons)
            Notice.add(_('完成了%s点工作进度。') % a)
            Notice.show()

    class CuredRest(CuredTask):
        id = 101
        name = _('休息')
        kind = _('日程')
        info = CuredTask.gt()
        ad = CuredTask.gt()

        @classmethod
        def checkAvailable(cls, player, day, time):
            if day==5 and time == 2:
                return _('该买药了。')
            if not player.onVacation and time != 2:
                return _('不是该休息的时候。')
            return True

        @classmethod
        def executeTask(cls, player):
            reco = r2(40 * f())
            player.gain_mental(reco)
            player.gain_abi(-0.05, 'sev')
            Notice.show()

    class CuredHosp(CuredTask):
        id = 102
        name = _('去医院')
        kind = _('日程')
        info = CuredTask.gt()
        ad = CuredTask.gt()

        @classmethod
        def checkAvailable(cls, player, day, time):
            if day==5 and time == 2:
                return True
            return _('不是去医院的时候。')
            
        @classmethod
        def executeTask(cls, player):
            temp = int(player.money / player.price)
            MedicineD.add(p, temp)
            player.money -= temp * player.price
            Notice.show()