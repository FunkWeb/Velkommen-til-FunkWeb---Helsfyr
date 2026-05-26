
label meetingroom_blue:
    scene expression Transform("images/rooms/meetingroom_one_overview_entrance.webp", fit="cover", align=(0.5, 0.5)) with fade
    pause 1
    scene expression Transform("images/rooms/meetingroom_one_entrance.webp", fit="cover", align=(0.5, 0.5)) with fade
    "Dette er det største møterommet, her holdes det markedsføringsmøter, FunkSoftmøter og kurs."
    
    show expression Transform("images/characters/ingeborg_serious.webp", zoom=0.25, xalign=0.1, yalign=-0.54) with fade
    ingeborg "Hei. Jeg heter Ingeborg og er jobbveileder og prosjektleder i FunkSoft." 
    ingeborg "Noen sier jeg elsker Asana (prosjektstyringsverktøyet vårt)." 
    ingeborg "Det er ikke helt sant, men jeg liker å ha kontroll på hva som skjer i prosjektene."

    
    scene expression Transform("images/rooms/meetingroom_one_inside.webp", fit="cover", align=(0.5, 0.5)) with fade 
    
    show expression Transform("ingeborg_pointing_right", zoom=0.25, xalign=0.1, yalign=-0.54) 
    show expression Transform("jorgen_posing", zoom=0.25, xalign=0.9, yalign=-0.54) 
    # se over dialogen her.
    ingeborg "Dette er Jørgen. I dette rommet møtes vi hver torsdag kl. 10, og har FunkSoft møter. Her diskuterer spill i alle former; hvilke spill vi liker å spille, nyheter og i ny og ne jobber med utviklingsprosjekter."

    menu:
        "Hvor vil du gå?"
        "Sosialsona":
            jump social_room
        "Kjøkkenområdet":
            jump kitchen
