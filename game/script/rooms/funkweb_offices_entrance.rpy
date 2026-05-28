
label funkweb_offices_entrance:
    scene expression Transform("images/bg/funkweb_waitingroom.webp", fit="cover", align=(0.5, 0.5)) with fade
    pause 1.8
    scene expression Transform("images/bg/funkweb_waitingroom_two.webp", fit="cover", align=(0.5, 0.5)) with fade
    show expression Transform("images/characters/johnny_smiling_two.webp", zoom=0.25, xalign=0.9, yalign=-0.54) with fade

    johnny "Hei, jeg er Johnny. Jeg er veileder her på FunkWeb og jobber i AFT: Arbeidforberedende tiltak." 
    johnny "Jeg elsker å prate om film, så hvis du ønsker å nerde litt om det, er jeg alltid positiv til det." 
    johnny "Jeg snakker også flytende spansk."
    johnny "La meg vise deg rundt."
label .choice_menu:
    "Hvor vil du gå?"
    
    menu:
        
            "Se på persongalleriet":
                call screen character_gallery
                jump .choice_menu
                
            "Gå til det største møterommet":
                jump meetingroom_blue

            "Gå til sosialsona":
                jump social_room

            "Gå til mellomgangen":
                jump middle_hallway

            "Gå tilbake til inngangen til FunkWeb":
                jump upper_entrance
