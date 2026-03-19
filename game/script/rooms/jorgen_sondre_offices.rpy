
label jorgen_sondre_offices:
    scene temp_office_jorgen_sondre with fade

    show jorgen_posing at left
    
    jorgen "Hei. Jeg er Jørgen, og som Prosjektleder IT i FunkWeb avholder jeg jevnlige lynkurs, workshops, og utarbeider prosjektbeskrivelser for våres AFT-kandidater."

    # sondre_default mangler, og må byttes inn med riktig bilde.
    show sondre_default at right 

    sondre "Hei, Jeg heter Sondre." 
    sondre "Jeg er IT-arkitekt og jobber med IT-Utvikling og er veileder for jobbsøkere og samarbeidspartnere. (TBD)"

    # videre inn i lokalet og scene_tilbake_i_lokalet har ukjent scenenavn. må legges til.
    menu: 
        "Hvor vil du gå?"
        "til veileder kontorene":
            jump advisor_offices 
        # "videre inn i lokalet":
        #    jump scene_for_videre_i_lokalet
        #"tilbake i lokalet":
        #    jump scene_tilbake_i_lokalet
        
return
