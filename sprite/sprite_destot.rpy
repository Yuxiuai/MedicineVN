layeredimage destot:

    zoom 0.40
    xcenter 0.5
    yalign 1.0

    always:
        "images/sprite/Destot/destot_wip.png"

    group outfit:
        attribute wip null default



init python:
    destot_attrs = [
        [
            '外观', False, [
                ['剪影', 'wip'],
            ]
        ],
    ]
    '''
    destot_attrs = [
        [
            '外观', False, [
                ['平常', 'normal'],
                ['外出', 'shirt'],
                ['睡衣', 'pajamas'],
                ['露出腹部', 'belly'],
                ['内裤','pants'],
                ['上衣和内裤','normalpants'],
                ['拉下内裤1','normalpee'],
                ['拉下内裤2','pantspee'],
                ['裸体','naked']
            ]
        ],

        [
            '下体', False, [
                ['平常', 'soft'],
                ['勃起','erect']
            ]
        ],

        [
            '眉毛', False, [
                ['平常', 'normal_eyebrow'],
                ['生气', 'angry_eyebrow'],
                ['尴尬', 'awkward_eyebrow'],
                ['微笑', 'smile_eyebrow'],
                ['流泪', 'cry_eyebrow']
            ]
        ],

        [
            '眼睛', False, [
                ['平常', 'normal_eyes'],
                ['平常2', 'normal2_eyes'],
                ['微笑', 'smile_eyes'],
                ['生气', 'angry_eyes'],
                ['尴尬', 'awkward_eyes'],
                ['害羞', 'shy_eyes'],
                ['流泪', 'cry_eyes'],
                ['闭眼', 'closed_eyes'],
            ]
        ],
        
        [
            '嘴', False, [
                ['平常', 'normal_mouth'],
                ['微笑', 'smile_mouth'],
                ['生气', 'angry_mouth'],
                ['流泪', 'cry_mouth'],
                ['张嘴', 'opened_mouth'],
                ['张嘴2', 'opened2_mouth']
            ]
        ],
        
        [
            '眼镜', False, [
                ['佩戴', 'glasses'],
                ['无', 'no_glasses']
            ]
        ],


        [
            '汗液', False, [
                ['无', 'no_sweat'],
                ['有', 'sweat']
            ]
        ],



        [
            '脸红', False, [
                ['无', 'no_blush'],
                ['有', 'blush']
            ]
        ],

        [
            '眼泪', False, [
                ['无', 'no_tear'],
                ['有', 'tear']
            ]
        ],

        [
            '尿液', False, [
                ['无', 'no_ura'],
                ['有', 'ura']
            ]
        ]
    ]
    '''