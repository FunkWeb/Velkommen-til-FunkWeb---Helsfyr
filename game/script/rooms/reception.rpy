



label reception:
    # midlertidig bakgrunssbilder som starter med temp, må byttes med endelig bakgrunn.
    scene expression Transform("rooms/temp_entrance_reception.webp", fit="cover", align=(0.5, 0.5)) with fade
    "Her er er resepsjonen!"
    
    menu reception_menu:
        "Funkweb holder til i 5. etasje, og det er også en kantine her"
        
        "Hvor er trappene?":
            scene expression Transform("bg/temp_staircase.webp", fit="cover", align=(0.5, 0.5)) with fade
            pause 1.5
            scene expression Transform("bg/temp_staircase_open_door.webp", fit="cover", align=(0.5, 0.5)) with Dissolve(1.0)
            "Du finner trapper her"
            jump reception

            
        "Hvor er heisen?":
            scene expression Transform("rooms/temp_entrance_hall_elevator.webp", fit="cover", align=(0.5, 0.5)) with fade
            "Heisen finner du her"
            jump reception
            
        "Ta meg opp til Funkweb i 5. etasje":
            jump upper_entrance
            
        "Ta meg til kantina":
            jump canteen
            
        "Gå ut":
            jump outside_entrance
