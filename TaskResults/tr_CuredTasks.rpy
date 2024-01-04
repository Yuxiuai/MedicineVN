init python:
    def curedsettime(t):
        if t <= 3:
            return 3
        if 3 < t <= 7:
            return 7
        if 7 < t < 11:
            return 11
        if t >= 11:
            return 12


label CuredWork_beginning:
    $p.onOutside = False
    $p.onVacation = False
    scene office at setcolor with fade
    if p.cured >= 84:
        show blurred:
            alpha (1-(-0.048 * p.cured + 5))
    if p.cured <= 91:
        "工作。"
    else:
        $renpy.say(None, CuredTask.gt())
    call Task_processing from _call_Task_processing_26
    
    $p.times+=1
    $CuredWork.executeTask(p)
    jump CuredWork_result

label CuredWork_result:
    scene office at setcolor with fade
    if p.cured >= 84:
        show blurred:
            alpha (1-(-0.048 * p.cured + 5))
    if p.cured <= 91:
        "……"
    else:
        $renpy.say(None, CuredTask.gt())
    
    $p.times+=1
    if p.cured >= 84:
        $p.time = curedsettime(p.times)
        jump curedRoutine
    jump before_operate_screen_label


label CuredRest_beginning:
    $p.onOutside = False
    $p.onVacation = True
    scene bedroom at setcolor with fade
    if p.cured >= 84:
        show blurred:
            alpha (1-(-0.048 * p.cured + 5))
    if p.cured <= 91:
        "休息。"
    else:
        $renpy.say(None, CuredTask.gt())
    
    call Task_processing from _call_Task_processing_27
    
    $p.times+=1
    $CuredRest.executeTask(p)
    jump CuredRest_result

label CuredRest_result:
    scene bedroom at setcolor with fade
    if p.cured >= 84:
        show blurred:
            alpha (1-(-0.048 * p.cured + 5))
    if p.cured <= 91:
        "……"
    else:
        $renpy.say(None, CuredTask.gt())
    $p.times+=1
    if p.cured >= 84:
        $p.time = curedsettime(p.times)
        jump curedRoutine
    jump before_operate_screen_label

label CuredHosp_beginning:
    $p.onOutside = True
    $p.onVacation = True
    scene hospital_corridor at setcolor with fade
    if p.cured >= 84:
        show blurred:
            alpha (1-(-0.048 * p.cured + 5))
    
    if p.cured <= 91:
        "买药。"
    else:
        $renpy.say(None, CuredTask.gt())
    $p.times+=1
    $CuredHosp.executeTask(p)
    jump CuredHosp_result

label CuredHosp_result:
    scene hospital_corridor at setcolor with fade
    if p.cured >= 84:
        show blurred:
            alpha (1-(-0.048 * p.cured + 5))
    if p.cured <= 91:
        "……"
    else:
        $renpy.say(None, CuredTask.gt())
    $p.times+=1
    $p.onOutside = False
    if p.cured >= 84:
        $p.time = curedsettime(p.times)
        jump curedRoutine
    jump before_operate_screen_label