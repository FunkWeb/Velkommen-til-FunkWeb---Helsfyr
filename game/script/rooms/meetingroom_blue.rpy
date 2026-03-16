
label meetingroom_blue:
    scene temp_meetingroom_blue with fade 

    "Dette er det største møterommet, her holdes det markedsføringsmøter, Funksoftmøter og kurs."
    
    show ingeborg_serious at left

    ingeborg "Hei. Jeg heter Ingeborg og er jobbveileder og prosjektleder i FunkSoft." 
    ingeborg "Noen sier jeg elsker Asana (prosjektstyringsverktøyet vårt)." 
    ingeborg "Det er ikke helt sant, men jeg liker å ha kontroll på hva som skjer i prosjektene."

    # mangler midlertidig bakgrunnsbilde for inne i møterom blå 
    scene temp_meetingroom_blue_inside with fade 
    
    show ingeborg_pointing_right at left
    show jorgen_posing at right 

    # se over dialogen her.
    ingeborg "Dette er Jørgen, og her i dette møterommet møtes vi hver torsdag kl. 10, og avholder FunkSoft-møter, hvor vi diskuterer spillnyheter, hvilke spill vi liker å spille, og i ny og ne jobber med spill-utviklings prosjekter."

    menu:
        "Hvor vil du gå?"
        "sosial-sone":
            jump social_room
        "kjøkkenområdet":
            jump kitchen
