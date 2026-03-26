label lko_offices:
    #pause 2
    scene temp_lko_workspace with fade
    
    show hans_tore_smiling_one at right
    
    hans_tore "Hei, jeg heter Hans Tore og jeg er fagansvarlig for alle lærlinger og lærekandidater som er hos oss innen IT-Driftsfaget og IT-Utviklerfaget."
    
    menu:
        "Hvor vil du gå videre?":
            
            "Gå tilbake til AFT veileder kontor":
                jump aft_offices
            
            "Gå til AFT-kandidatene sin arbeidsplass":
                jump aft_candidate_work_area
                
    return