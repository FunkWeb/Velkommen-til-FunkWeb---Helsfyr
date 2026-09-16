
screen funkweb_offices_entrance_arrows():
    default south_arrow_hovered = False
    default east_arrow_hovered = False
    default gallery_hovered = False

    imagebutton:
        xalign 0.90
        yalign -0.54
        idle "images/characters/johnny_smiling_two.webp"
        hover Transform("images/characters/johnny_smiling_two.webp", matrixcolor=BrightnessMatrix(0.15))
        at Transform(zoom=0.25)
        focus_mask True
        hovered SetScreenVariable("gallery_hovered", True)
        unhovered SetScreenVariable("gallery_hovered", False)
        action ShowMenu("character_gallery")

    imagebutton:
        xalign 0.48
        yalign 1.0
        at Transform(zoom=0.25, rotate=90)
        idle "images/ui/right_arrow_idle.png"
        hover "images/ui/right_arrow_hover.png"
        focus_mask True
        hovered SetScreenVariable("south_arrow_hovered", True)
        unhovered SetScreenVariable("south_arrow_hovered", False)
        action Jump("meetingroom_blue")

    if south_arrow_hovered:
        text "Gå til det største møterommet":
            xalign 0.49
            yalign 0.77

    imagebutton:
        xalign 0.64
        yalign 0.43
        at Transform(zoom=0.25, rotate=0)
        idle "images/ui/right_arrow_idle.png"
        hover "images/ui/right_arrow_hover.png"
        focus_mask True
        hovered SetScreenVariable("east_arrow_hovered", True)
        unhovered SetScreenVariable("east_arrow_hovered", False)
        action Jump("upper_entrance")

    if east_arrow_hovered:
        text "Gå til inngangen til FunkWeb":
            xalign 0.427
            yalign 0.45


label funkweb_offices_entrance:
    scene expression Transform("images/bg/funkweb_waitingroom.webp", fit="cover", align=(0.5, 0.5)) with fade
    pause 1.8
    scene expression Transform("images/bg/funkweb_waitingroom_two.webp", fit="cover", align=(0.5, 0.5)) with fade
    show expression Transform("images/characters/johnny_smiling_two.webp", zoom=0.25, xalign=0.9, yalign=-0.54) with fade

    johnny "Hei, jeg er Johnny. Jeg er veileder her på FunkWeb og jobber i AFT: Arbeidforberedende tiltak." 
    johnny "Jeg elsker å prate om film, så hvis du ønsker å nerde litt om det, er jeg alltid positiv til det." 
    johnny "Jeg snakker også flytende spansk."
    johnny "La meg vise deg rundt."
    johnny "Klikk på bildet av meg hvis du vil se persongalleriet."
    "Klikk på en pil for å utforske videre."

    call screen funkweb_offices_entrance_arrows
