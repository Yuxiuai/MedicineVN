screen screen_objects(player):
    zorder -10


    $cactuses = (DeadCactus, Cactus, WellCactus)
    $showcactus = None
    if any([x.has(player) for x in cactuses]):
        for i in cactuses:
            if i.has(player):
                $showcactus = i.get(player)
    
    if showcactus and not player.onVacation:
        imagebutton idle 'gui/object/shadow.png':
            at disso
            xcenter 0.6
            ycenter 0.65
        imagebutton idle showcactus.sprite():
            at disso
            if type(showcactus) != DeadCactus:
                action Hide("info"), Show(screen="info_confirm", i=showcactus.cond_info(), act=Function(showcactus.water, player), text=_('浇水'), pp=renpy.get_mouse_pos(), width=350, a=showcactus.developer_info(player))
            else:
                action Hide("info"), Show(screen="info_use", i=showcactus.cond_info(), width=350, a=showcactus.developer_info(player))
            hovered Show(screen="info", i=showcactus.cond_info(), width=350, a=showcactus.developer_info(player))
            unhovered Hide("info")
            activate_sound audio.cactus
            xcenter 0.6
            ycenter 0.65

    default toyd = 0

    if ToyDuck.has(player) and not player.onVacation:
        
        imagebutton idle 'gui/object/duck.png':
            if toyd == 0:
                at disso
            elif toyd % 2 == 1:
                at toyduck
            else:
                at toyduck2
            action SetScreenVariable("toyd", toyd+1)
            hovered Show(screen="info", i=_('是的，你很想戳一下它。'), width=250)
            unhovered Hide("info")
            activate_sound audio.duck
            xcenter 0.3
            ycenter 0.65
    
    if PathosDoll.has(player) and player.onVacation and p.times <= 9:
        imagebutton idle 'gui/object/pathos.png':
            at tzoom(0.18), disso
            action NullAction()
            hovered Show(screen="info", i=_('背部有一个按钮。'), width=250)
            unhovered Hide("info")
            activate_sound rcd((audio.pathos_1, audio.pathos_2))
            xcenter 0.8
            ycenter 0.5