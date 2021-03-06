image solitus_eyes_normal:
    "images/sprite/Solitus/eyes/Solitus_eyes_normal_eyes_blink1.png"
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
    "images/sprite/Solitus/eyes/Solitus_eyes_normal_eyes_blink2.png"
    pause 0.05
    "images/sprite/Solitus/eyes/Solitus_eyes_normal_eyes_blink3.png"
    pause 0.05
    "images/sprite/Solitus/eyes/Solitus_eyes_normal_eyes_blink4.png"
    pause 0.05
    "images/sprite/Solitus/eyes/Solitus_eyes_normal_eyes_blink3.png"
    pause 0.05
    "images/sprite/Solitus/eyes/Solitus_eyes_normal_eyes_blink2.png"
    pause 0.05  
    repeat

image solitus_eyes_normal2:
    "images/sprite/Solitus/eyes/Solitus_eyes_normal2_eyes_blink1.png"
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
    "images/sprite/Solitus/eyes/Solitus_eyes_normal2_eyes_blink2.png"
    pause 0.05
    "images/sprite/Solitus/eyes/Solitus_eyes_normal2_eyes_blink3.png"
    pause 0.05
    "images/sprite/Solitus/eyes/Solitus_eyes_normal2_eyes_blink4.png"
    pause 0.05
    "images/sprite/Solitus/eyes/Solitus_eyes_normal2_eyes_blink3.png"
    pause 0.05
    "images/sprite/Solitus/eyes/Solitus_eyes_normal2_eyes_blink2.png"
    pause 0.05  
    repeat
 
image solitus_eyes_sad:
    "images/sprite/Solitus/eyes/Solitus_eyes_sad_eyes_blink1.png"
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
    "images/sprite/Solitus/eyes/Solitus_eyes_sad_eyes_blink2.png"
    pause 0.05
    "images/sprite/Solitus/eyes/Solitus_eyes_sad_eyes_blink3.png"
    pause 0.05
    "images/sprite/Solitus/eyes/Solitus_eyes_sad_eyes_blink4.png"
    pause 0.05
    "images/sprite/Solitus/eyes/Solitus_eyes_sad_eyes_blink3.png"
    pause 0.05
    "images/sprite/Solitus/eyes/Solitus_eyes_sad_eyes_blink2.png"
    pause 0.05  
    repeat

image solitus_eyes_awkward:
    "images/sprite/Solitus/eyes/Solitus_eyes_awkward_eyes_blink1.png"
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
    "images/sprite/Solitus/eyes/Solitus_eyes_awkward_eyes_blink2.png"
    pause 0.05
    "images/sprite/Solitus/eyes/Solitus_eyes_awkward_eyes_blink3.png"
    pause 0.05
    "images/sprite/Solitus/eyes/Solitus_eyes_awkward_eyes_blink4.png"
    pause 0.05
    "images/sprite/Solitus/eyes/Solitus_eyes_awkward_eyes_blink3.png"
    pause 0.05
    "images/sprite/Solitus/eyes/Solitus_eyes_awkward_eyes_blink2.png"
    pause 0.05  
    repeat

image solitus_eyes_surprised:
    "images/sprite/Solitus/eyes/Solitus_eyes_surprised_eyes_blink1.png"
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
    "images/sprite/Solitus/eyes/Solitus_eyes_surprised_eyes_blink2.png"
    pause 0.05
    "images/sprite/Solitus/eyes/Solitus_eyes_surprised_eyes_blink3.png"
    pause 0.05
    "images/sprite/Solitus/eyes/Solitus_eyes_surprised_eyes_blink4.png"
    pause 0.05
    "images/sprite/Solitus/eyes/Solitus_eyes_surprised_eyes_blink3.png"
    pause 0.05
    "images/sprite/Solitus/eyes/Solitus_eyes_surprised_eyes_blink2.png"
    pause 0.05  
    repeat

image solitus_eyes_angry:
    "images/sprite/Solitus/eyes/Solitus_eyes_angry_eyes_blink1.png"
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
    "images/sprite/Solitus/eyes/Solitus_eyes_angry_eyes_blink2.png"
    pause 0.05
    "images/sprite/Solitus/eyes/Solitus_eyes_angry_eyes_blink3.png"
    pause 0.05
    "images/sprite/Solitus/eyes/Solitus_eyes_angry_eyes_blink4.png"
    pause 0.05
    "images/sprite/Solitus/eyes/Solitus_eyes_angry_eyes_blink3.png"
    pause 0.05
    "images/sprite/Solitus/eyes/Solitus_eyes_angry_eyes_blink2.png"
    pause 0.05  
    repeat

image solitus_happy1:
    animation
    align (.85,.55)
    rotate 0
    "images/sprite/Solitus/parts/Solitus_happy_happy.png"
    linear 2 rotate 360
    repeat

image solitus_happy2:
    animation
    zoom 0.7
    align (.3,1.2)
    rotate 0
    "images/sprite/Solitus/parts/Solitus_happy_happy.png"
    linear 2 rotate -360
    repeat

image solitus_happy:
    contains:
        "solitus_happy1"
    contains:
        "solitus_happy2"

image solitus_mood:
    "images/sprite/Solitus/parts/Solitus_mood_mood1.png"
    pause 0.2
    "images/sprite/Solitus/parts/Solitus_mood_mood2.png"
    pause 0.2
    "images/sprite/Solitus/parts/Solitus_mood_mood3.png"
    pause 0.2
    "images/sprite/Solitus/parts/Solitus_mood_mood4.png"
    pause 0.2
    repeat


layeredimage solitus:

    zoom 0.3
    yalign 1.1
    xalign -0.11

    always:
        "images/sprite/Solitus/Solitus_naked.png"

    group outfit:
        attribute normal default
        attribute naked
        attribute white

    group hat:
        attribute hat default
        attribute no_hat null

    group eyebrow:
        attribute normal_eyebrow default
        attribute normal2_eyebrow
        attribute awkward_eyebrow
        attribute agony_eyebrow
        attribute angry_eyebrow
        attribute sad_eyebrow
        attribute scared_eyebrow
        attribute surprised_eyebrow
        attribute smile_eyebrow


    group eyes:
        attribute normal_eyes default:
            "solitus_eyes_normal"
        attribute normal2_eyes:
            "solitus_eyes_normal2"
        attribute awkward_eyes:
            "solitus_eyes_awkward"
        attribute sad_eyes:
            "solitus_eyes_sad"
        attribute angry_eyes:
            "solitus_eyes_angry"
        attribute surprised_eyes:
            "solitus_eyes_surprised"

        attribute agony_eyes
        attribute scared_eyes
        attribute smile_eyes

        attribute closed_eyes

    group mouth:
        attribute normal_mouth default
        attribute normal2_mouth
        attribute awkward_mouth
        attribute agony_mouth
        attribute angry_mouth
        attribute sad_mouth
        attribute scared_mouth
        attribute surprised_mouth
        attribute smile_mouth

    group blush:
        attribute no_blush null default
        attribute blush

    group glasses:
        attribute no_glasses null default
        attribute glasses

    group sweat:
        attribute sweat
        attribute sweat_e
        attribute no_sweat null default

    group anger:
        attribute anger
        attribute no_anger null default

    

    group mood:
        attribute no_mood null default
        attribute mood:
            "solitus_mood"

    group happy:
        attribute happy:
            "solitus_happy"
        attribute no_happy null default

    group em:
        attribute no_em null default
        attribute em 
        attribute ques




init python:
    solitus_attrs = [
        [
            '??????', False, [
                ['?????????', 'normal'],
                ['?????????','white'],
                ['??????','naked']
            ]
        ],

        [
            '??????', False, [
                ['??????', 'hat'],
                ['???', 'no_hat']
            ]
        ],
                
        [
            '??????', False, [
                ['??????', 'normal_eyebrow'],
                ['??????2', 'normal2_eyebrow'],
                ['??????', 'awkward_eyebrow'],
                ['??????', 'agony_eyebrow'],
                ['??????', 'angry_eyebrow'],
                ['??????', 'sad_eyebrow'],
                ['??????', 'scared_eyebrow'],
                ['??????', 'surprised_eyebrow'],
                ['??????', 'smile_eyebrow']
            ]
        ],

        [
            '??????', False, [
                ['??????', 'normal_eyes'],
                ['??????2', 'normal2_eyes'],
                ['??????', 'awkward_eyes'],
                ['??????', 'agony_eyes'],
                ['??????', 'angry_eyes'],
                ['??????', 'sad_eyes'],
                ['??????', 'scared_eyes'],
                ['??????', 'surprised_eyes'],
                ['??????', 'smile_eyes'],
                ['??????', 'closed_eyes']
            ]
        ],
        
        [
            '???', False, [
                ['??????', 'normal_mouth'],
                ['??????', 'awkward_mouth'],
                ['??????', 'agony_mouth'],
                ['??????', 'angry_mouth'],
                ['??????', 'sad_mouth'],
                ['??????', 'scared_mouth'],
                ['??????', 'surprised_mouth'],
                ['??????', 'smile_mouth']
            ]
        ],
        
        [
            '??????', False, [
                ['???', 'no_glasses'],
                ['??????', 'glasses']
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
                ['???', 'no_happy'],
                ['???', 'happy']
            ]
        ],

        [
            '??????', False, [
                ['???', 'no_blush'],
                ['???', 'blush']
            ]
        ],

        [
            '?????????', False, [
                ['???', 'no_mood'],
                ['???', 'mood']
            ]
        ],

        [
            '??????', False, [
                ['???', 'no_em'],
                ['??????', 'em'],
                ['??????', 'ques']
            ]
        ],
    ]
