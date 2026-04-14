label lko_offices:
    #pause 2
    scene expression Transform("images/rooms/temp_lko_workspace.webp", fit="cover", align=(0.5, 0.5)) with fade
    
    "Dette er arbeidsplassen til lærekandidatene."
    
    show expression Transform("images/characters/hans_tore_smiling_one.webp", fit="contain", align=(1.0, 1.0)) at right with fade
    
    hans_tore "Hei, jeg heter Hans Tore og jeg er fagansvarlig for alle lærlinger og lærekandidater som er hos oss innen IT-Driftsfaget og IT-Utviklerfaget."
    
    "Hvor vil du gå videre?"
    
    menu:
        "Gå tilbake til AFT-veileder kontoret":
            jump aft_offices
            
        "Gå til AFT-kandidatene sin arbeidsplass":
            jump aft_candidate_work_area
            
        #"Gå tilbake til mellomgangen":
            #jump middle_hallway
                
