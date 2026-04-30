
label middle_hallway:
    
    scene expression Transform("images/rooms/temp_middle_hallway.webp", fit="cover", align=(0.5, 0.5)) with fade
    
    "Her er det et stort fint bord hvor man kan sitte sammen, og et garderobeskap hvor man kan henge fra seg ting."
    
    show expression Transform("trine_lise_smiling", zoom=0.25, xalign=0.9, yalign=-0.54) with fade
    
    trine_lise "Jeg er Trine-Lise og har hatt gleden av å jobbe i FunkWeb siden 2013." 
    trine_lise "Har jobbet på flere typer tiltak og nå AFT." 
    trine_lise "Min største motivasjon er å se at våre flotte deltakere lykkes i sin prosess og når de mål vi avklarer sammen." 
    trine_lise "Jeg er glad i å holde kurs, ha gode arbeidsmøter og være opptatt av at CV og søknader er så bra som mulig" 
    trine_lise "slik at vi kan ha fokus på alle de andre virkemidlene vi har for å nå ut til arbeidsgivere."
    
    "Hvor vil du gå videre?"
    
    menu:
        "Gå tilbake til AFT-veileder kontoret":
            jump aft_office
            
        "Gå til lærekandidatene sin arbeidsplass":
            jump lko_offices
            
        "Gå til arbeidsplassen til AFT-kandidatene":
            jump aft_candidate_work_area
            