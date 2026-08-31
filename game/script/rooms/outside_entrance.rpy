
screen arrow_choice_screen_outside():
    default arrow_hovered = False

    imagebutton:
        xalign 0.28
        yalign 0.921
        at Transform(zoom=0.25, rotate=-50)
        idle "images/ui/right_arrow_idle.png"
        hover "images/ui/right_arrow_hover.png"
        focus_mask True
        hovered SetScreenVariable("arrow_hovered", True)
        unhovered SetScreenVariable("arrow_hovered", False)
        action Jump("reception")

    if arrow_hovered:
        text "Velkommen inn!":
            xalign 0.270
            yalign 0.936


label outside_entrance:
    scene expression Transform("images/bg/helsfyr_panorama_sol.webp", fit="cover", align=(0.5, 0.5)) with fade
    pause 1.8
    scene expression Transform("images/bg/inngangsparti_helsfyr_panorama_sol.webp", fit="cover", align=(0.5, 0.5)) with fade
    
    "Velkommen til FunkWeb på Helsfyr Panorama!"
    "I dette spillet skal du bli kjent med lokalene våre, menneskene som jobber her, og rommene du kan bruke."
    "Klikk deg rundt for å utforske."

    call screen arrow_choice_screen_outside



