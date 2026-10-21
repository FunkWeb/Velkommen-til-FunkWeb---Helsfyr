

screen reception_door_screen():
    default door_hovered = False

    imagebutton:
        xalign 0.621
        yalign 1.04
        at Transform(zoom=0.25, rotate=-90)
        idle "images/ui/right_arrow_idle.png"
        hover "images/ui/right_arrow_hover.png"
        focus_mask True
        hovered SetScreenVariable("door_hovered", True)
        unhovered SetScreenVariable("door_hovered", False)
        action Jump("reception_choices")

    if door_hovered:
        text "Gå gjennom døren":
            xalign 0.61
            yalign 0.80


label reception:
    # midlertidig bakgrunssbilder som starter med temp, må byttes med endelig bakgrunn.
    scene expression Transform("rooms/temp_entrance_reception.webp", fit="cover", align=(0.5, 0.5)) with fade
    "Her er resepsjonen."
    "FunkWeb holder til i 5. etasje, og det er også en kantine her."
    "Klikk på døren for å utforske videre."
    call screen reception_door_screen

label reception_choices:
    menu:
        
        "Hvor er trappene?":
            scene expression Transform("rooms/staircase_close_door.webp", fit="cover", align=(0.5, 0.5)) with fade
            pause 1.5
            scene expression Transform("rooms/staircase_open_door.webp", fit="cover", align=(0.5, 0.5)) with Dissolve(1.0)
            "Du finner trapper her."
            jump reception

            
        "Hvor er heisen?":
            scene expression Transform("bg/entrance_hall_elevator.webp", fit="cover", align=(0.5, 0.5)) with fade
            "Heisen finner du her."
            jump reception
                 
        "Ta meg til kantina":
            jump canteen
            
        "Ta meg opp til FunkWeb i 5. etasje":
            jump upper_entrance

        "Gå ut":
            jump outside_entrance
