
label aft_offices:
    
    scene temp_office_aft_staff with fade
    
    "Her sitter veilederne, gjerne send en chat eller bank på om du lurer på noe.
    
    show kristin_posing at right
    
    kristin "Hei, jeg er Kristin. I tillegg til å være administrasjonskonsulent er jeg verneombud."
    kristin "Det betyr at dere kan kontakte meg dersom dere har tilbakemeldinger i fht arbeidshverdagen i FunkWeb som dere ikke ønsker å ta opp med veileder"
    
    menu:
        "Hvor vil du gå videre?":

            "Gå tilbake til samtalerommene":
                jump meetingrooms_three_above_offices_near_kitchen
                
            "Gå til mellomgang":
                jump #mellomgang
                
            "Gå til området for lærekandidatene":
                jump lko_offices
                
    return