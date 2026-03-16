
label reception:
    # midlertidig bakgrunssbilder som starter med temp, må byttes med endelig bakgrunn.
    scene temp_entrance_reception with fade
    "Her er er resepsjonen!"
    
    menu reception_menu:
        "Funkweb holder til i 5. etasje, og det er også en kantine her"
        "\"Hvor er trappene?\"":
            scene temp_entrance_staircase with fade 
            "Du finner trapper her"
            jump reception
        "\"Hvor er heisen?\"":
            scene temp_entrance_hall_elevator with fade 
            "Heisen finner du her"
            jump reception
        "Ta meg opp til Funkweb i 5. etasje":
            jump upper_entrance
        "Ta meg til kantina":
            jump canteen
