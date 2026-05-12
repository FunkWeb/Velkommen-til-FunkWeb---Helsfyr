label aft_candidate_work_area:
        
    scene expression Transform("images/rooms/temp_workspace_aft.webp", fit="cover", align=(0.5, 0.5)) with fade
 
    "Her sitter AFT kandidatene. Her kan du booke deg en plass og jobbe med prosjekter, skrive CV, jobbsøknader, eller kanskje ta noen onlinekurs."
    "Du kan reservere plass på booking.FunkWeb.no"

    show expression Transform("simen_smiling", zoom=0.25, xalign=0.9, yalign=-0.54) with fade 
    
    simen "Hei! Jeg heter Simen og er jobbveileder, og prosjektleder for både lærekandidatene og i internasjonale prosjekter."
    simen "Jeg har mange roller i FunkWeb og har vært med på det meste her i snart 10 år."
    simen "Jeg elsker like mye å få til gode samarbeid med arbeidsgiver og kandidat som det å teste produktene til Sportsmate." 

    menu: 
        "Hvor vil du gå?"
        # "Til det nest største møterommet":
        #    jump scene_for_nest_største_møterommet
        # "Til et mindre møterom":
        #    jump scene_for_mindre_møterommet
        # "Til Sportsmate-lageret":
        #    jump scene_sportsmate_lager

        # Kan eventuelt endres til "Gå til det nest største møterommet"
        "Gå til møterom 8":
            jump multi_purpose_room_and_course_room

        "Tilbake til mellomgangen":
            jump middle_hallway

        "Tilbake til LKO-området":
            jump lko_offices
        
