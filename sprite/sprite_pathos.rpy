image pathos_eyes_normal:
    "images/sprite/Pathos/eyes/Pathos_eyes_normal_eyes_blink1.png"
    choice:
        pause 2
    choice:
        pause 2.5
    choice:
        pause 3
    choice:
        pause 3.5
    choice:
        pause 4
    choice:
        pause 4.5
    choice:
        pause 5
    choice:
        pause 5.5
    "images/sprite/Pathos/eyes/Pathos_eyes_normal_eyes_blink2.png"
    pause 0.05
    "images/sprite/Pathos/eyes/Pathos_eyes_normal_eyes_blink3.png"
    pause 0.05
    "images/sprite/Pathos/eyes/Pathos_eyes_normal_eyes_blink4.png"
    pause 0.05
    "images/sprite/Pathos/eyes/Pathos_eyes_normal_eyes_blink3.png"
    pause 0.05
    "images/sprite/Pathos/eyes/Pathos_eyes_normal_eyes_blink2.png"
    pause 0.05  
    repeat
 
image pathos_eyes_angry:
    "images/sprite/Pathos/eyes/Pathos_eyes_angry_eyes_blink1.png"
    choice:
        pause 2
    choice:
        pause 2.5
    choice:
        pause 3
    choice:
        pause 3.5
    choice:
        pause 4
    choice:
        pause 4.5
    choice:
        pause 5
    choice:
        pause 5.5
    "images/sprite/Pathos/eyes/Pathos_eyes_angry_eyes_blink2.png"
    pause 0.05
    "images/sprite/Pathos/eyes/Pathos_eyes_angry_eyes_blink3.png"
    pause 0.05
    "images/sprite/Pathos/eyes/Pathos_eyes_angry_eyes_blink4.png"
    pause 0.05
    "images/sprite/Pathos/eyes/Pathos_eyes_angry_eyes_blink3.png"
    pause 0.05
    "images/sprite/Pathos/eyes/Pathos_eyes_angry_eyes_blink2.png"
    pause 0.05  
    repeat

image pathos_eyes_awkward:
    "images/sprite/Pathos/eyes/Pathos_eyes_awkward_eyes_blink1.png"
    choice:
        pause 2
    choice:
        pause 2.5
    choice:
        pause 3
    choice:
        pause 3.5
    choice:
        pause 4
    choice:
        pause 4.5
    choice:
        pause 5
    choice:
        pause 5.5
    "images/sprite/Pathos/eyes/Pathos_eyes_awkward_eyes_blink2.png"
    pause 0.05
    "images/sprite/Pathos/eyes/Pathos_eyes_awkward_eyes_blink3.png"
    pause 0.05
    "images/sprite/Pathos/eyes/Pathos_eyes_awkward_eyes_blink4.png"
    pause 0.05
    "images/sprite/Pathos/eyes/Pathos_eyes_awkward_eyes_blink3.png"
    pause 0.05
    "images/sprite/Pathos/eyes/Pathos_eyes_awkward_eyes_blink2.png"
    pause 0.05  
    repeat

image pathos_eyes_surprised:
    "images/sprite/Pathos/eyes/Pathos_eyes_surprised_eyes_blink1.png"
    choice:
        pause 2
    choice:
        pause 2.5
    choice:
        pause 3
    choice:
        pause 3.5
    choice:
        pause 4
    choice:
        pause 4.5
    choice:
        pause 5
    choice:
        pause 5.5
    "images/sprite/Pathos/eyes/Pathos_eyes_surprised_eyes_blink2.png"
    pause 0.05
    "images/sprite/Pathos/eyes/Pathos_eyes_surprised_eyes_blink3.png"
    pause 0.05
    "images/sprite/Pathos/eyes/Pathos_eyes_surprised_eyes_blink4.png"
    pause 0.05
    "images/sprite/Pathos/eyes/Pathos_eyes_surprised_eyes_blink3.png"
    pause 0.05
    "images/sprite/Pathos/eyes/Pathos_eyes_surprised_eyes_blink2.png"
    pause 0.05  
    repeat

image pathos_eyes_annoy:
    "images/sprite/Pathos/eyes/Pathos_eyes_annoy_eyes_blink1.png"
    choice:
        pause 2
    choice:
        pause 2.5
    choice:
        pause 3
    choice:
        pause 3.5
    choice:
        pause 4
    choice:
        pause 4.5
    choice:
        pause 5
    choice:
        pause 5.5
    "images/sprite/Pathos/eyes/Pathos_eyes_annoy_eyes_blink2.png"
    pause 0.05
    "images/sprite/Pathos/eyes/Pathos_eyes_annoy_eyes_blink3.png"
    pause 0.05
    "images/sprite/Pathos/eyes/Pathos_eyes_annoy_eyes_blink4.png"
    pause 0.05
    "images/sprite/Pathos/eyes/Pathos_eyes_annoy_eyes_blink3.png"
    pause 0.05
    "images/sprite/Pathos/eyes/Pathos_eyes_annoy_eyes_blink2.png"
    pause 0.05  
    repeat

image pathos_mouth_saying:
    "images/sprite/Pathos/mouth/Pathos_mouth_normal_mouth.png"
    pause 0.5
    "images/sprite/Pathos/mouth/Pathos_mouth_surprised_mouth.png"
    pause 0.1
    "images/sprite/Pathos/mouth/Pathos_mouth_say_mouth.png"
    pause 0.1  
    "images/sprite/Pathos/mouth/Pathos_mouth_opened_mouth.png"
    pause 0.1
    "images/sprite/Pathos/mouth/Pathos_mouth_say_mouth.png"
    pause 0.1  
    "images/sprite/Pathos/mouth/Pathos_mouth_surprised_mouth.png"
    pause 0.1
    "images/sprite/Pathos/mouth/Pathos_mouth_say_mouth.png"
    pause 0.1  
    "images/sprite/Pathos/mouth/Pathos_mouth_opened_mouth.png"
    pause 0.1
    repeat

image headani:
    contains:
        "images/sprite/Pathos/Pathos_head_head.png"
        parallel:
            choice:
                linear 0.01 yoffset 20
                linear 0.01 yoffset -20
            choice:
                linear 0.01 yoffset -20
                linear 0.01 yoffset 20
            choice:
                linear 0.01 xoffset 20
                linear 0.01 xoffset -20
            choice:
                linear 0.01 xoffset -20
                linear 0.01 xoffset 20

        repeat

layeredimage pathos:

    zoom 0.45
    xcenter 0.5
    yalign 1.0

    always:
        "images/sprite/Pathos/Pathos_naked.png"

    group penis:
        attribute soft null default
        attribute erect

    group outfit:
        attribute normal default
        attribute pants
        attribute naked null

    group eyebrow:
        attribute normal_eyebrow default
        attribute angry_eyebrow
        attribute awkward_eyebrow
        attribute surprised_eyebrow
        attribute annoy_eyebrow

    group eyes:
        attribute normal_eyes default:
            "pathos_eyes_normal"
        attribute surprised_eyes:
            "pathos_eyes_surprised"
        attribute angry_eyes:
            "pathos_eyes_angry"
        attribute awkward_eyes:
            "pathos_eyes_awkward"
        attribute annoy_eyes:
            "pathos_eyes_annoy"
        attribute closed_eyes

    group mouth:
        attribute normal_mouth default
        attribute smile_mouth
        attribute angry_mouth
        attribute awkward_mouth
        attribute surprised_mouth
        attribute opened_mouth
        attribute annoy_mouth
        attribute saying:
            "pathos_mouth_saying"

    group blush:
        attribute no_blush null default
        attribute blush

    group glasses:
        attribute glasses default
        attribute no_glasses null

    group sweat:
        attribute sweat
        attribute sweat_e
        attribute no_sweat null default

    group anger:
        attribute anger
        attribute no_anger null default

    group sco:
        attribute sco default
        attribute no_sco null

    group head:
        attribute head:
            "headani"
        attribute no_head null default


init python:
    pathos_attrs = [
        [
            '??????', False, [
                ['??????', 'normal'],
                ['??????','pants'],
                ['??????','naked']
            ]
        ],

        [
            '??????', False, [
                ['??????', 'soft'],
                ['??????','erect']
            ]
        ],

        [
            '??????', False, [
                ['??????', 'normal_eyebrow'],
                ['??????', 'angry_eyebrow'],
                ['??????', 'awkward_eyebrow'],
                ['??????', 'surprised_eyebrow']
            ]
        ],

        [
            '??????', False, [
                ['??????', 'normal_eyes'],
                ['??????', 'angry_eyes'],
                ['??????', 'awkward_eyes'],
                ['??????', 'surprised_eyes'],
                ['??????', 'closed_eyes'],
            ]
        ],
        
        [
            '???', False, [
                ['??????', 'normal_mouth'],
                ['??????', 'smile_mouth'],
                ['??????', 'angry_mouth'],
                ['??????', 'awkward_mouth'],
                ['??????', 'surprised_mouth'],
                ['??????', 'opened_mouth'],
                ['?????????', 'saying']
            ]
        ],
        
        [
            '??????', False, [
                ['??????', 'glasses'],
                ['???', 'no_glasses']
            ]
        ],

        [
            '?????????', False, [
                ['??????', 'sco'],
                ['???', 'no_sco']
            ]
        ],

        [
            '??????', False, [
                ['???', 'no_sweat'],
                ['???', 'sweat'],
                ['Emoji', 'sweat_e']
            ]
        ],

        [
            '??????', False, [
                ['???', 'no_anger'],
                ['???', 'anger']
            ]
        ],

        [
            '??????', False, [
                ['???', 'no_blush'],
                ['???', 'blush']
            ]
        ]
    ]
