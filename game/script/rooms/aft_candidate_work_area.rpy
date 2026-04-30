label aft_candidate_work_area:

    scene temp_workspace_aft with fade

    "Her sitter AFT-kandidatene. Her kan du booke deg en plass og jobbe med prosjekter, skrive CV, jobbsøknader, eller kanskje ta noen onlinekurs."
    "Du kan reservere plass på booking.FunkWeb.no"

    show expression Transform("simen_smiling", zoom=0.25, xalign=0.9, yalign=-0.54) with fade 
    
    simen "Hei! Jeg heter Simen og er jobbveileder, og prosjektleder for både lærekandidatene og i internasjonale prosjekter."
    simen "Jeg har mange roller i FunkWeb og har vært med på det meste her i snart 10 år."
    simen "Jeg elsker like mye å få til gode samarbeid med arbeidsgiver og kandidat som det å teste produktene til Sportsmate." 

    # følgende har ukjent scenenavn og må legges til. 
    # scene_for_nest_største_møterommet, scene_for_mindre_møterommet, scene_sportsmate_lager og scene_mellomgang
    menu: 
        "Hvor vil du gå?"
        "sosial-sone":
            jump social_room
        "toalettene":
            jump kitchen
        # "til det nest største møterommet":
        #    jump scene_for_nest_største_møterommet
        # "til det mindre møterommet":
        #    jump scene_for_mindre_møterommet
        # "til Sportsmate-lageret":
        #    jump scene_sportsmate_lager
        # "tilbake til mellomgangen":
        #    jump scene_mellomgang
        "tilbake til lko-området":
            jump lko
        
