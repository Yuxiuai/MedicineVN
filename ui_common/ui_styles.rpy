init python:
    style.gameUI = Style(style.button_text)
    style.gameUI.color = "#FFFFFF"
    style.gameUI.hover_color = "#9370db"
    style.gameUI.selected_color = "#FFFFFF"
    style.gameUI.size=24
    style.gameUI.font="C.ttf"
    style.gameUI.outlines=[(1,"444444",0,0)]

    style.gameUIL = Style(style.gameUI)
    style.gameUIL.size=30
    style.gameUIL.outlines=[(0,"ffffff",0,0)]

    style.info_text = Style(style.gameUI)
    style.info_text.color = "#FFFFFF"
    style.info_text.size=23

    style.admonition_text = Style(style.gameUI)
    style.admonition_text.color = "#d6d6d6"
    style.admonition_text.size=19

    style.meda_text = Style(style.gameUI)
    style.meda_text.color = "#fe6363"
    style.meda_text.hover_color = "#9370db"

    style.medb_text = Style(style.gameUI)
    style.medb_text.color = "#7881e8"
    style.medb_text.hover_color = "#9370db"

    style.medc_text = Style(style.gameUI)
    style.medc_text.color = "#e4f06f"
    style.medc_text.hover_color = "#9370db"

    style.medd_text = Style(style.gameUI)
    style.medd_text.color = "#ff60cd"
    style.medd_text.hover_color = "#9370db"

    style.white = Style(style.gameUI)
    style.white.color = "#FFFFFF"
    style.white.hover_color = "#FFFFFF"

    style.food = Style(style.white)
    style.food.color = "#F2C34E"
    style.food.hover_color = "#F2C34E"
    style.food.outlines=[(0,"ffffff",0,0)]
   

    style.gameL = Style(style.button_text)
    style.gameL.color = "#4B0082"
    style.gameL.hover_color = "#4B0082"
    style.gameL.selected_color = "#4B0082"
    style.gameL.size=30
    style.gameL.font="C.ttf"
    style.gameL.outlines=[(1,"bcbcbc",0,0)]

    style.gameUIM = Style(style.gameUI)
    style.gameUIM.text_align=0.5

    style.gameUIR = Style(style.gameUI)
    style.gameUIR.text_align=1.0
    
    style.handwrite = Style(style.button_text)
    style.handwrite.color = "#000"
    style.handwrite.hover_color = "#9370db"
    style.handwrite.selected_color = "#FFFFFF"
    style.handwrite.font="handwriting.ttf"
    style.handwrite.size=41

    style.handwriteL = Style(style.gameL)
    style.handwriteL.font="handwriting.ttf"

    style.handwriteM = Style(style.handwrite)
    style.handwriteM.text_align=0.5

    style.effectLayer = Style(style.button_text)
    style.effectLayer.color = "#FFFFFF"
    style.effectLayer.hover_color = "#FFFFFF"
    style.effectLayer.selected_color = "#FFFFFF"
    style.effectLayer.size=20
    style.effectLayer.font="C.ttf"
    style.effectLayer.text_align=0.5

style transparent_frame is gui_frame
style translucent_frame is gui_frame
style noback_frame is gui_frame
style grey_frame is gui_frame
style info_frame is gui_frame
style info_prompt_text is gui_prompt_text

style info_prompt_text:
    text_align 0.5
    layout "subtitle"

style transparent_frame:
    background Frame("gui/style/transparent.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)

style translucent_frame:
    background Frame("gui/style/translucent.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)

style noback_frame:
    background Frame("gui/style/clear.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)

style info_frame:
    background Frame("gui/style/info.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)

style grey_frame:
    background Frame("gui/style/grey_[prefix_]background.png", Borders(0, 0, 0, 0), tile=gui.frame_tile)

