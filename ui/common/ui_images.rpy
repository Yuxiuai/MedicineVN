init:
    image black = "#000"
    image white = "#FFFFFF"

    image blurred:
        "noise_bg/noise1.jpg"
        0.1
        "noise_bg/noise2.jpg"
        0.1
        "noise_bg/noise3.jpg"
        0.1
        "noise_bg/noise4.jpg"
        0.1
        repeat

    image splash:
        "black.png" with Dissolve(1.0, alpha=True)
        0.5
        "white.png" with Dissolve(1.0, alpha=True)
        1
        "gui/preloading.png" with Dissolve(1.0, alpha=True)
        3
        "white.png" with Dissolve(1.0, alpha=True)
        1.5

    image loading_before:
        align (0.9, 0.9)
        "loading/loading/1.png"
        0.1
        "loading/loading/2.png"
        0.1
        "loading/loading/3.png"
        0.1
        "loading/loading/4.png"
        0.1
        "loading/loading/5.png"
        0.1
        "loading/loading/6.png"
        0.1
        "loading/loading/7.png"
        0.1
        "loading/loading/8.png"
        0.1
        "loading/loading/9.png"
        0.1
        "loading/loading/10.png"
        0.1
        "loading/loading/11.png"
        0.1
        "loading/loading/12.png"
        0.1
        "loading/loading/13.png"
        0.1
        "loading/loading/14.png"
        0.1
        "loading/loading/15.png"
        0.1
        "loading/loading/16.png"
        0.1
        "loading/loading/17.png"
        0.1
        "loading/loading/18.png"
        0.1
        "loading/loading/19.png"
        0.1
        "loading/loading/20.png"
        0.1
        "loading/loading/21.png"
        0.1

    image loading_hal:
        zoom 0.2
        "loading_before"
        2.1
        align (0.9, 0.9)
        "loading/hal/1.png"
        0.1
        "loading/hal/2.png"
        0.1
        "loading/hal/3.png"
        0.1
        block:
            "loading/hal/4.png"
            0.1
            "loading/hal/5.png"
            0.1
            "loading/hal/6.png"
            0.1
            "loading/hal/7.png"
            0.1
            "loading/hal/8.png"
            0.1
            "loading/hal/9.png"
            0.1
            "loading/hal/10.png"
            0.1
            "loading/hal/11.png"
            0.1
            "loading/hal/12.png"
            0.1
            "loading/hal/13.png"
            0.1
            "loading/hal/14.png"
            0.1
            "loading/hal/15.png"
            0.1
            "loading/hal/16.png"
            0.1
            "loading/hal/17.png"
            0.1
            "loading/hal/18.png"
            0.1
            "loading/hal/19.png"
            0.1
            repeat

    image loading_sol:
        zoom 0.2
        "loading_before"
        2.1
        align (0.9, 0.9)
        "loading/sol/1.png"
        0.1
        "loading/sol/2.png"
        0.1
        block:
            "loading/sol/3.png"
            0.1
            "loading/sol/4.png"
            0.1
            "loading/sol/5.png"
            0.1
            "loading/sol/6.png"
            0.1
            "loading/sol/7.png"
            0.1
            "loading/sol/8.png"
            0.1
            "loading/sol/9.png"
            0.1
            "loading/sol/10.png"
            0.1
            "loading/sol/11.png"
            0.1
            "loading/sol/12.png"
            0.1
            repeat

    image loading_aco:
        zoom 0.2
        "loading_before"
        2.1
        align (0.9, 0.9)
        "loading/aco/1.png"
        0.1
        "loading/aco/2.png"
        0.1
        "loading/aco/3.png"
        0.1
        "loading/aco/4.png"
        0.1
        block:
            "loading/aco/5.png"
            0.1
            "loading/aco/6.png"
            0.1
            "loading/aco/7.png"
            0.1
            "loading/aco/8.png"
            0.1
            "loading/aco/9.png"
            0.1
            "loading/aco/10.png"
            0.1
            repeat

    image loading_pa:
        zoom 0.2
        "loading_before"
        2.1
        align (0.9, 0.9)
        "loading/pa/1.png"
        0.1
        "loading/pa/2.png"
        0.1
        block:
            "loading/pa/3.png"
            0.1
            "loading/pa/4.png"
            0.1
            "loading/pa/5.png"
            0.1
            "loading/pa/6.png"
            0.1
            "loading/pa/7.png"
            0.1
            "loading/pa/8.png"
            0.1
            "loading/pa/9.png"
            0.1
            "loading/pa/10.png"
            0.1
            "loading/pa/11.png"
            0.1
            "loading/pa/12.png"
            0.1
            "loading/pa/13.png"
            0.1
            "loading/pa/14.png"
            0.1
            repeat


    image pixel_sol:
        align (0.9, 0.9)
        "loading/Solitus-01.png"
        0.1
        "loading/Solitus-02.png"
        0.1
        "loading/Solitus-03.png"
        0.1
        "loading/Solitus-02.png"
        0.1
        "loading/Solitus-01.png"
        0.1
        "loading/Solitus-04.png"
        0.1
        "loading/Solitus-05.png"
        0.1
        "loading/Solitus-04.png"
        0.1
        "loading/Solitus-01.png"
        0.1
        "loading/Solitus-04.png"
        0.1
        "loading/Solitus-05.png"
        0.1
        "loading/Solitus-04.png"
        0.1
        repeat

    image pixel_hal:
        align (0.9, 0.9)
        "loading/Halluke-01.png"
        1
        "loading/Halluke-02.png"
        0.1
        "loading/Halluke-03.png"
        0.1
        "loading/Halluke-02.png"
        0.1
        "loading/Halluke-01.png"
        1
        "loading/Halluke-02.png"
        0.1
        "loading/Halluke-03.png"
        0.1
        "loading/Halluke-02.png"
        0.1
        "loading/Halluke-04.png"
        1
        "loading/Halluke-01.png"
        0.1
        "loading/Halluke-02.png"
        0.1
        "loading/Halluke-03.png"
        0.1
        "loading/Halluke-02.png"
        0.1
        repeat


    image pixel_dep:
        align (0.9, 0.9)
        "loading/Depline-01.png"
        0.125
        "loading/Depline-02.png"
        0.125
        "loading/Depline-03.png"
        0.125
        "loading/Depline-02.png"
        0.125
        "loading/Depline-01.png"
        0.125
        "loading/Depline-04.png"
        0.125
        "loading/Depline-05.png"
        0.125
        "loading/Depline-04.png"
        0.125
        "loading/Depline-01.png"
        0.125
        "loading/Depline-04.png"
        0.125
        "loading/Depline-05.png"
        0.125
        "loading/Depline-04.png"
        0.125
        repeat

    image pixel_aco:
        align (0.9, 0.9)
        "loading/Acolas-01.png"
        0.7
        "loading/Acolas-02.png"
        0.075
        "loading/Acolas-03.png"
        0.075
        "loading/Acolas-04.png"
        0.075
        "loading/Acolas-05.png"
        0.15
        "loading/Acolas-06.png"
        0.15
        repeat

    image loading_pixel:
        choice:
            "pixel_sol"
        choice:
            "pixel_hal"
        choice:
            "pixel_aco"
        choice:
            "pixel_dep"

    image loading_image:
        choice:
            "loading_sol"
        choice:
            "loading_hal"
        choice:
            "loading_aco"
        choice:
            "loading_pa"
