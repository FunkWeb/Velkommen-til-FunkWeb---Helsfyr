
label funkweb_offices_entrance:
    scene expression Transform("images/rooms/temp_waitingroom.webp", fit="cover", align=(0.5, 0.5)) with fade
    show expression Transform("images/characters/johnny_smiling_two.webp", zoom=0.25, xalign=0.9, yalign=-0.54) with fade

    johnny "Hei, jeg er Johnny. Jeg er veileder her på FunkWeb og jobber i AFT: arbeidforberedende tiltak." 
    johnny "Jeg elsker å prate om film, så hvis du ønsker å nerde litt om det, er jeg alltid positiv til det." 
    johnny "Jeg snakker også flytende spansk."
    johnny "La meg vise deg rundt."

    "Hvor vil du gå?"
    
    menu:
        
            "Se på persongalleriet":
                show screen character_gallery
            
            "Gå til det største møterommet":
                jump meetingroom_blue

            "Gå til sosial-sone":
                jump social_room

            "Gå til kjøkkenet":
                jump kitchen

            "Gå tilbake til inngangen til FunkWeb":
                jump upper_entrance

            