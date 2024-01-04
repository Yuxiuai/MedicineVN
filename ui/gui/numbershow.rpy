init python early:


    class NumberShow:
        num = 1
        maxnum = 20
        
        @classmethod
        def get_num(cls):
            r = cls.num
            cls.num += 1
            if cls.num > cls.maxnum:
                cls.num = 1
            return str(r)

    class Damageshow(NumberShow):
        
        @classmethod
        def show(cls, dmg, crit=False):
            xp, yp = renpy.get_mouse_pos()
            showname = 'damaged_show' + cls.get_num()
            if renpy.get_screen(showname):
                renpy.hide_screen(showname)
                renpy.show_screen(showname, xp, yp-70, showname, dmg, crit)
            else:
                renpy.show_screen(showname, xp, yp-70, showname, dmg, crit) 

            
    
transform damage_show(xp, yp, to = 1):
    ypos yp
    xpos xp
    parallel:
        ease 1.5 yoffset -300 * to
    parallel:
        linear 0.75 alpha 1.0
        linear 0.75 alpha 0.0

screen damaged_show(xp, yp, scr, dmg, crit=False):
    zorder 500
    if not crit:
        text '%s' % dmg:
            style "damage_num"
            at damage_show(xp, yp)
    else:
        text '%s!' % dmg:
            style "crit_damage_num"
            at damage_show(xp, yp)
    timer 1.5 action Hide(scr)


screen damaged_show1(xp, yp, scr, dmg, crit=False):
    use damaged_show(xp, yp, 'damaged_show1', dmg, crit)

screen damaged_show2(xp, yp, scr, dmg, crit=False):
    use damaged_show(xp, yp, 'damaged_show2', dmg, crit)

screen damaged_show3(xp, yp, scr, dmg, crit=False):
    use damaged_show(xp, yp, 'damaged_show3', dmg, crit)

screen damaged_show4(xp, yp, scr, dmg, crit=False):
    use damaged_show(xp, yp, 'damaged_show4', dmg, crit)

screen damaged_show5(xp, yp, scr, dmg, crit=False):
    use damaged_show(xp, yp, 'damaged_show5', dmg, crit)

screen damaged_show6(xp, yp, scr, dmg, crit=False):
    use damaged_show(xp, yp, 'damaged_show6', dmg, crit)

screen damaged_show7(xp, yp, scr, dmg, crit=False):
    use damaged_show(xp, yp, 'damaged_show7', dmg, crit)

screen damaged_show8(xp, yp, scr, dmg, crit=False):
    use damaged_show(xp, yp, 'damaged_show8', dmg, crit)

screen damaged_show9(xp, yp, scr, dmg, crit=False):
    use damaged_show(xp, yp, 'damaged_show9', dmg, crit)

screen damaged_show10(xp, yp, scr, dmg, crit=False):
    use damaged_show(xp, yp, 'damaged_show10', dmg, crit)


screen damaged_show11(xp, yp, scr, dmg, crit=False):
    use damaged_show(xp, yp, 'damaged_show11', dmg, crit)

screen damaged_show12(xp, yp, scr, dmg, crit=False):
    use damaged_show(xp, yp, 'damaged_show12', dmg, crit)

screen damaged_show13(xp, yp, scr, dmg, crit=False):
    use damaged_show(xp, yp, 'damaged_show13', dmg, crit)

screen damaged_show14(xp, yp, scr, dmg, crit=False):
    use damaged_show(xp, yp, 'damaged_show14', dmg, crit)

screen damaged_show15(xp, yp, scr, dmg, crit=False):
    use damaged_show(xp, yp, 'damaged_show15', dmg, crit)

screen damaged_show16(xp, yp, scr, dmg, crit=False):
    use damaged_show(xp, yp, 'damaged_show16', dmg, crit)

screen damaged_show17(xp, yp, scr, dmg, crit=False):
    use damaged_show(xp, yp, 'damaged_show17', dmg, crit)

screen damaged_show18(xp, yp, scr, dmg, crit=False):
    use damaged_show(xp, yp, 'damaged_show18', dmg, crit)

screen damaged_show19(xp, yp, scr, dmg, crit=False):
    use damaged_show(xp, yp, 'damaged_show19', dmg, crit)

screen damaged_show20(xp, yp, scr, dmg, crit=False):
    use damaged_show(xp, yp, 'damaged_show20', dmg, crit)
