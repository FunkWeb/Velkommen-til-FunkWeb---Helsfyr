screen arrow_choice_screen():
    default door_arrow_hovered = False
    default elevator_arrow_hovered = False
    
    # Define arrow positions as variables for easy moving
    default door_arrow_x = 0.52
    default door_arrow_y = 0.59
    default elevator_arrow_x = 0.69
    default elevator_arrow_y = 0.55
    
    # Text offsets from arrow position
    default door_text_y_offset = 0.09
    default elevator_text_x_offset = 0.020
    default elevator_text_y_offset = 0.065

    imagebutton:
        xalign door_arrow_x
        yalign door_arrow_y
        at Transform(zoom=0.25, rotate=-90)
        idle "images/ui/right_arrow_idle.png"
        hover "images/ui/right_arrow_hover.png"
        focus_mask True
        hovered SetScreenVariable("door_arrow_hovered", True)
        unhovered SetScreenVariable("door_arrow_hovered", False)
        action Jump("ring_doorbell")

    if door_arrow_hovered:
        text "Ring på døren":
            xalign door_arrow_x
            yalign door_arrow_y + door_text_y_offset

    imagebutton:
        xalign elevator_arrow_x
        yalign elevator_arrow_y
        at Transform(zoom=0.25, rotate=0)
        idle "images/ui/right_arrow_idle.png"
        hover "images/ui/right_arrow_hover.png"
        focus_mask True
        hovered SetScreenVariable("elevator_arrow_hovered", True)
        unhovered SetScreenVariable("elevator_arrow_hovered", False)
        action Jump("reception")

    if elevator_arrow_hovered:
        text "Tilbake til resepsjonen":
            xalign elevator_arrow_x + elevator_text_x_offset
            yalign elevator_arrow_y + elevator_text_y_offset

label upper_entrance:
    scene expression Transform("bg/funkweb_entrance.webp", fit="cover", align=(0.5, 0.5)) with fade
    "Her er inngangen til FunkWeb. Ring på døren så slippes du inn."
   
    "Hva vil du gjøre?"
    
    call screen arrow_choice_screen

label ring_doorbell:
    scene expression Transform("images/bg/funkweb_door_bell.webp", fit="cover", align=(0.5, 0.5)) with fade
    "Du ringer på døren."
    scene expression Transform("images/bg/funkweb_door_open_entrance.webp", fit="cover", align=(0.5, 0.5)) with fade
    "Døren åpnes og du blir sluppet inn."
    jump funkweb_offices_entrance
