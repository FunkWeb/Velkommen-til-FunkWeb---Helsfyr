label aft_candidate_work_area:

    scene temp_workspace_aft

    "Her sitter AFT kandidatene. Her kan du booke deg en plass og jobbe med prosjekter, skrive CV, jobbsøknader, eller kanskje ta noen onlinekurs."
    "Du kan reservere plass på booking.FunkWeb.no"

    show simen_smiling at right

    simen "Hei! Jeg heter Simen og er jobbveileder, og prosjektleder for både lærekandidatene og i internasjonale prosjekter."
    simen "Jeg har mange roller i FunkWeb og har vært med på det meste her i snart 10 år."
    simen "Jeg elsker like mye å få til gode samarbeid med arbeidsgiver og kandidat som det å teste produktene til Sportsmate." 

    # videre inn i lokalet eller nærliggende områdener har ukjent scenenavn. må legges til.
    menu: 
        "Hvor vil du gå?"
        "sosial sone":
            jump social_room
        "toalettene":
            jump kitchen
        # "videre inn i lokalet":
        #    jump scene_for_videre_i_lokalet
        #"til nærliggende områdener":
        #    jump nærliggende_områdene
        
