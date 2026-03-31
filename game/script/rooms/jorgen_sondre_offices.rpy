
label jorgen_sondre_offices:
    scene expression Transform("images/rooms/temp_office_jorgen_sondre.webp", fit="cover", align=(0.5, 0.5)) with fade

    show expression Transform("images/characters/jorgen_posing.webp", fit="contain", xsize=600, align=(0.0, 1.0)) at left with fade
    
    jorgen "Hei. Jeg er Jørgen, og som Prosjektleder IT i FunkWeb avholder jeg jevnlige lynkurs, workshops, og utarbeider prosjektbeskrivelser for våres AFT-kandidater."

    # sondre_default mangler, og må byttes inn med riktig bilde.
    show expression Transform("images/characters/sondre_posing.webp", fit="contain", xsize=600, align=(1.0, 1.0)) at right with fade

    sondre "Hei, Jeg heter Sondre." 
    sondre "Jeg er IT-arkitekt og jobber med IT-Utvikling og er veileder for jobbsøkere og samarbeidspartnere."

    # scene_tilbake_i_lokalet og mellomgangen har ukjent scenenavn. må legges til.
    
    "Hvor vil du gå?"
    
    menu:
        "Gå til veileder kontorene":
            jump aft_offices
            
        # "til mellomgangen":
        #    jump scene_for_mellomgang    
        
        "Gå til LKO-området":
            jump lko_offices
            
        "Gå tilbake til kontor 1-2-3":
            jump funkweb_offices_one_two_three
        
        

