
label meetingroom_blue:
    scene expression Transform("images/rooms/temp_meetingroom_blue.webp", fit="cover", align=(0.5, 0.5)) with fade
    "Dette er det største møterommet, her holdes det markedsføringsmøter, Funksoftmøter og kurs."
    
    show expression Transform("images/characters/ingeborg_serious.webp", zoom=0.25, xalign=0.1, yalign=-0.54) with fade
    ingeborg "Hei. Jeg heter Ingeborg og er jobbveileder og prosjektleder i FunkSoft." 
    ingeborg "Noen sier jeg elsker Asana (prosjektstyringsverktøyet vårt)." 
    ingeborg "Det er ikke helt sant, men jeg liker å ha kontroll på hva som skjer i prosjektene."

    # mangler midlertidig bakgrunnsbilde for inne i møterom blå 
    scene temp_meetingroom_blue_inside with fade 
    
    show expression Transform("ingeborg_pointing_right", zoom=0.25, xalign=0.1, yalign=-0.54) with fade 
    show expression Transform("jorgen_posing", zoom=0.25, xalign=0.9, yalign=-0.54) with fade 
    # se over dialogen her.
    ingeborg "Dette er Jørgen, og her i dette møterommet møtes vi hver torsdag kl. 10, og avholder FunkSoft-møter, hvor vi diskuterer spillnyheter, hvilke spill vi liker å spille, og i ny og ne jobber med spill-utviklings prosjekter."

    menu:
        "Hvor vil du gå?"
        "sosial-sone":
            jump social_room
        "kjøkkenområdet":
            jump kitchen
