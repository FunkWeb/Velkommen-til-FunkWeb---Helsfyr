
label reception:
    # midlertidig bakgrunssbilder som starter med temp, må byttes med endelig bakgrunn.
    scene expression Transform("rooms/temp_entrance_reception.webp", fit="cover", align=(0.5, 0.5)) with fade
    "Her er resepsjonen!"
    
    menu reception_menu:
        "FunkWeb holder til i 5. etasje, og det er også en kantine her."
        "Hvor er trappene?":
            scene temp_entrance_staircase with fade 
            "Du finner trappen her."
            jump reception
        "Hvor er heisen?":
            scene expression Transform("rooms/temp_entrance_hall_elevator.webp", fit="cover", align=(0.5, 0.5)) with fade
            "Heisen finner du her."
            jump reception
        "Ta meg opp til FunkWeb i 5. etasje":
            jump upper_entrance
        "Ta meg til kantina":
            jump canteen
        "Gå ut":
            jump outside_entrance
