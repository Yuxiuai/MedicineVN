init:
    image black = "#000"
    image white = "#FFFFFF"

    image blurred:
        "noise_bg/noise1.webp"
        0.1
        "noise_bg/noise2.webp"
        0.1
        "noise_bg/noise3.webp"
        0.1
        "noise_bg/noise4.webp"
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
        align (0.95, 0.9)
        "loading/loading/1.webp"
        0.1
        "loading/loading/2.webp"
        0.1
        "loading/loading/3.webp"
        0.1
        "loading/loading/4.webp"
        0.1
        "loading/loading/5.webp"
        0.1
        "loading/loading/6.webp"
        0.1
        "loading/loading/7.webp"
        0.1
        "loading/loading/8.webp"
        0.1
        "loading/loading/9.webp"
        0.1
        "loading/loading/10.webp"
        0.1
        "loading/loading/11.webp"
        0.1
        "loading/loading/12.webp"
        0.1
        "loading/loading/13.webp"
        0.1
        "loading/loading/14.webp"
        0.1
        "loading/loading/15.webp"
        0.1
        "loading/loading/16.webp"
        0.1
        "loading/loading/17.webp"
        0.1
        "loading/loading/18.webp"
        0.1
        "loading/loading/19.webp"
        0.1
        "loading/loading/20.webp"
        0.1
        "loading/loading/21.webp"
        0.1

    image loading_hal:
        zoom 0.2
        "loading_before"
        2.1
        align (0.95, 0.9)
        "loading/hal/1.webp"
        0.1
        "loading/hal/2.webp"
        0.1
        "loading/hal/3.webp"
        0.1
        block:
            "loading/hal/4.webp"
            0.1
            "loading/hal/5.webp"
            0.1
            "loading/hal/6.webp"
            0.1
            "loading/hal/7.webp"
            0.1
            "loading/hal/8.webp"
            0.1
            "loading/hal/9.webp"
            0.1
            "loading/hal/10.webp"
            0.1
            "loading/hal/11.webp"
            0.1
            "loading/hal/12.webp"
            0.1
            "loading/hal/13.webp"
            0.1
            "loading/hal/14.webp"
            0.1
            "loading/hal/15.webp"
            0.1
            "loading/hal/16.webp"
            0.1
            "loading/hal/17.webp"
            0.1
            "loading/hal/18.webp"
            0.1
            "loading/hal/19.webp"
            0.1
            repeat

    image loading_sol:
        zoom 0.2
        "loading_before"
        2.1
        align (0.95, 0.9)
        "loading/sol/1.webp"
        0.1
        "loading/sol/2.webp"
        0.1
        block:
            "loading/sol/3.webp"
            0.1
            "loading/sol/4.webp"
            0.1
            "loading/sol/5.webp"
            0.1
            "loading/sol/6.webp"
            0.1
            "loading/sol/7.webp"
            0.1
            "loading/sol/8.webp"
            0.1
            "loading/sol/9.webp"
            0.1
            "loading/sol/10.webp"
            0.1
            "loading/sol/11.webp"
            0.1
            "loading/sol/12.webp"
            0.1
            repeat

    image loading_aco:
        zoom 0.2
        "loading_before"
        2.1
        align (0.95, 0.9)
        "loading/aco/1.webp"
        0.1
        "loading/aco/2.webp"
        0.1
        "loading/aco/3.webp"
        0.1
        "loading/aco/4.webp"
        0.1
        block:
            "loading/aco/5.webp"
            0.1
            "loading/aco/6.webp"
            0.1
            "loading/aco/7.webp"
            0.1
            "loading/aco/8.webp"
            0.1
            "loading/aco/9.webp"
            0.1
            "loading/aco/10.webp"
            0.1
            repeat

    image loading_pa:
        zoom 0.2
        "loading_before"
        2.1
        align (0.95, 0.9)
        "loading/pa/1.webp"
        0.1
        "loading/pa/2.webp"
        0.1
        block:
            "loading/pa/3.webp"
            0.1
            "loading/pa/4.webp"
            0.1
            "loading/pa/5.webp"
            0.1
            "loading/pa/6.webp"
            0.1
            "loading/pa/7.webp"
            0.1
            "loading/pa/8.webp"
            0.1
            "loading/pa/9.webp"
            0.1
            "loading/pa/10.webp"
            0.1
            "loading/pa/11.webp"
            0.1
            "loading/pa/12.webp"
            0.1
            "loading/pa/13.webp"
            0.1
            "loading/pa/14.webp"
            0.1
            repeat


    image pixel_sol0:
        xcenter 0.5
        ycenter 0.5
        "loading/Solitus0-01.webp"
        0.1
        "loading/Solitus0-04.webp"
        0.1
        "loading/Solitus0-05.webp"
        0.1
        "loading/Solitus0-04.webp"
        0.1
        "loading/Solitus0-01.webp"
        0.1
        "loading/Solitus0-02.webp"
        0.1
        "loading/Solitus0-03.webp"
        0.1
        "loading/Solitus0-02.webp"
        0.1
        "loading/Solitus0-01.webp"
        0.1
        "loading/Solitus0-04.webp"
        0.1
        "loading/Solitus0-05.webp"
        0.1
        "loading/Solitus0-04.webp"
        0.1
        "loading/Solitus0-01.webp"
        0.1
        "loading/Solitus0-04.webp"
        0.1
        "loading/Solitus0-05.webp"
        0.1
        "loading/Solitus0-04.webp"
        0.1
        repeat

    image pixel_sol1:
        xcenter 0.5
        ycenter 0.5
        "loading/Solitus1-01.webp"
        0.5
        "loading/Solitus1-02.webp"
        0.15
        "loading/Solitus1-03.webp"
        0.15
        "loading/Solitus1-04.webp"
        0.15
        "loading/Solitus1-03.webp"
        0.15
        "loading/Solitus1-04.webp"
        0.15
        "loading/Solitus1-03.webp"
        0.15
        "loading/Solitus1-04.webp"
        0.15
        "loading/Solitus1-05.webp"
        0.1
        "loading/Solitus1-06.webp"
        0.1
        "loading/Solitus1-05.webp"
        0.1
        "loading/Solitus1-06.webp"
        0.1
        repeat
    
    image pixel_sol2:
        xcenter 0.5
        ycenter 0.5
        "loading/Solitus2-01.webp"
        0.1
        "loading/Solitus2-04.webp"
        0.1
        "loading/Solitus2-05.webp"
        0.1
        "loading/Solitus2-04.webp"
        0.1
        "loading/Solitus2-01.webp"
        0.1
        "loading/Solitus2-02.webp"
        0.1
        "loading/Solitus2-03.webp"
        0.1
        "loading/Solitus2-02.webp"
        0.1
        "loading/Solitus2-01.webp"
        0.1
        "loading/Solitus2-04.webp"
        0.1
        "loading/Solitus2-05.webp"
        0.1
        "loading/Solitus2-04.webp"
        0.1
        "loading/Solitus2-01.webp"
        0.1
        "loading/Solitus2-04.webp"
        0.1
        "loading/Solitus2-05.webp"
        0.1
        "loading/Solitus2-04.webp"
        0.1
        repeat

    image pixel_sol3:
        xcenter 0.5
        ycenter 0.5
        "loading/Solitus3-01.webp"
        2.5
        "loading/Solitus3-02.webp"
        0.2
        "loading/Solitus3-01.webp"
        2.5
        "loading/Solitus3-02.webp"
        0.2
        "loading/Solitus3-01.webp"
        2.0
        "loading/Solitus3-03.webp"
        2.0
        "loading/Solitus3-02.webp"
        0.5
        "loading/Solitus3-04.webp"
        0.5
        repeat

    image pixel_hal:
        xcenter 0.5
        ycenter 0.5
        "loading/Halluke-01.webp"
        1
        "loading/Halluke-02.webp"
        0.1
        "loading/Halluke-03.webp"
        0.1
        "loading/Halluke-02.webp"
        0.1
        "loading/Halluke-01.webp"
        1
        "loading/Halluke-02.webp"
        0.1
        "loading/Halluke-03.webp"
        0.1
        "loading/Halluke-02.webp"
        0.1
        "loading/Halluke-04.webp"
        1
        "loading/Halluke-01.webp"
        0.1
        "loading/Halluke-02.webp"
        0.1
        "loading/Halluke-03.webp"
        0.1
        "loading/Halluke-02.webp"
        0.1
        repeat

    image pixel_hal0:
        xcenter 0.5
        ycenter 0.5
        "loading/Halluke0-01.webp"
        1
        "loading/Halluke0-02.webp"
        0.1
        "loading/Halluke0-03.webp"
        0.1
        "loading/Halluke0-02.webp"
        0.1
        "loading/Halluke0-01.webp"
        1
        "loading/Halluke0-02.webp"
        0.1
        "loading/Halluke0-03.webp"
        0.1
        "loading/Halluke0-02.webp"
        0.1
        "loading/Halluke0-04.webp"
        1
        "loading/Halluke0-01.webp"
        0.1
        "loading/Halluke0-02.webp"
        0.1
        "loading/Halluke0-03.webp"
        0.1
        "loading/Halluke0-02.webp"
        0.1
        repeat
    
    image pixel_hal1:
        xcenter 0.5
        ycenter 0.5
        "loading/Halluke1-01.webp"
        1
        "loading/Halluke1-02.webp"
        0.1
        "loading/Halluke1-03.webp"
        0.1
        "loading/Halluke1-02.webp"
        0.1
        "loading/Halluke1-01.webp"
        1
        "loading/Halluke1-02.webp"
        0.1
        "loading/Halluke1-03.webp"
        0.1
        "loading/Halluke1-02.webp"
        0.1
        "loading/Halluke1-04.webp"
        1
        "loading/Halluke1-01.webp"
        0.1
        "loading/Halluke1-02.webp"
        0.1
        "loading/Halluke1-03.webp"
        0.1
        "loading/Halluke1-02.webp"
        0.1
        repeat

    image pixel_dep:
        xcenter 0.5
        ycenter 0.5
        "loading/Depline-01.webp"
        0.125
        "loading/Depline-02.webp"
        0.125
        "loading/Depline-03.webp"
        0.125
        "loading/Depline-02.webp"
        0.125
        "loading/Depline-01.webp"
        0.125
        "loading/Depline-04.webp"
        0.125
        "loading/Depline-05.webp"
        0.125
        "loading/Depline-04.webp"
        0.125
        "loading/Depline-01.webp"
        0.125
        "loading/Depline-04.webp"
        0.125
        "loading/Depline-05.webp"
        0.125
        "loading/Depline-04.webp"
        0.125
        repeat

    image pixel_aco0:
        xcenter 0.5
        ycenter 0.5
        "loading/Acolas0-01.webp"
        0.7
        "loading/Acolas0-02.webp"
        0.075
        "loading/Acolas0-03.webp"
        0.075
        "loading/Acolas0-04.webp"
        0.075
        "loading/Acolas0-05.webp"
        0.15
        "loading/Acolas0-06.webp"
        0.15
        repeat
    
    image pixel_aco1:
        xcenter 0.5
        ycenter 0.5
        "loading/Acolas1-01.webp"
        0.7
        "loading/Acolas1-02.webp"
        0.075
        "loading/Acolas1-03.webp"
        0.075
        "loading/Acolas1-04.webp"
        0.075
        "loading/Acolas1-05.webp"
        0.15
        "loading/Acolas1-06.webp"
        0.15
        repeat


    image pixel_pa:
        xcenter 0.5
        ycenter 0.5
        "loading/Pathos-01.webp"
        0.7
        "loading/Pathos-02.webp"
        0.15
        "loading/Pathos-03.webp"
        0.1
        "loading/Pathos-04.webp"
        0.1
        "loading/Pathos-03.webp"
        0.1
        "loading/Pathos-02.webp"
        0.15
        "loading/Pathos-01.webp"
        0.15
        "loading/Pathos-05.webp"
        0.075
        "loading/Pathos-06.webp"
        0.075
        "loading/Pathos-07.webp"
        0.075
        "loading/Pathos-06.webp"
        0.075
        "loading/Pathos-05.webp"
        0.075
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
        choice:
            "pixel_pa"

    image loading_image:
        choice:
            "loading_sol"
        choice:
            "loading_hal"
        choice:
            "loading_aco"
        choice:
            "loading_pa"
