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
        name = '工作'
        kind = '日程'
        info = CuredTask.gt()
        ad = CuredTask.gt()

        @classmethod
        def checkAvailable(cls, player, day, time):
            if player.onVacation or time == 2:
                return '是该休息的时候。'
            return True

        @classmethod
        def executeTask(cls, player):
            player.onOutside = False
            player.onVacation = False
            cons = r2(30 * f())
            a = r2(player.goal * 0.12)
            player.mental -= cons
            player.achievedGoal += a
            Notice.add('消耗了%s点精神状态。' % cons)
            Notice.add('完成了%s点工作进度。' % a)
            Notice.show()

    class CuredRest(CuredTask):
        id = 101
        name = '休息'
        kind = '日程'
        info = CuredTask.gt()
        ad = CuredTask.gt()

        @classmethod
        def checkAvailable(cls, player, day, time):
            if not player.onVacation and time != 2:
                return '不是该休息的时候。'
            return True

        @classmethod
        def executeTask(cls, player):
            reco = r2(40 * f())
            player.mental += reco
            Notice.add('恢复了%s点精神状态。' % reco)
            Notice.show()

    class CuredHosp(CuredTask):
        id = 102
        name = '去医院'
        kind = '日程'
        info = CuredTask.gt()
        ad = CuredTask.gt()

        @classmethod
        def checkAvailable(cls, player, day, time):
            if day==5 and time == 2:
                return True
            return '不是去医院的时候。'
            
        @classmethod
        def executeTask(cls, player):
    
            player.money = 0.0
            MedicineD.add(p, 10)
            Notice.show()