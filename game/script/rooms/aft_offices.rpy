
label aft_offices:
    
    scene expression Transform("images/rooms/temp_office_aft_staff.webp", fit="cover", align=(0.5, 0.5)) with fade

    "Her sitter veilederne. Send gjerne en chat eller bank på om du lurer på noe."
    
    show expression Transform("kristin_posing", zoom=0.25, xalign=0.7, yalign=-0.54) with fade 

    
    kristin "Hei, jeg er Kristin. I tillegg til å være administrasjonskonsulent er jeg verneombud."
    kristin "Det betyr at dere kan kontakte meg dersom dere har tilbakemeldinger i fht arbeidshverdagen i FunkWeb som dere ikke ønsker å ta opp med veileder."
    
    "Hvor vil du gå videre?"

    menu:
            "Gå tilbake til samtalerommene":
                jump meetingrooms_three_above_offices_near_kitchen
                
            "Gå til mellomgangen":
                jump middle_hallway
                
            "Gå til området for LKO-området":
                jump lko_offices
                
    return
