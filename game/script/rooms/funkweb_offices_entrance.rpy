
label funkweb_offices_entrance:
    scene temp_waitingroom with fade
    show johnny_smiling_two at right with fade

    johnny "Hei, jeg er Johnny. Jeg er veileder her på funkweb og jobber i AFT: arbeidforberedende tiltak." 
    johnny "Jeg elsker å prate om film, så hvis du ønsker å nerde litt om det, er jeg alltid positiv til det." 
    johnny "Jeg snakker også flytende spansk."
    johnny "La meg vise deg rundt."

    menu:
        "Hvor vil du gå?":
            "Se på persongalleriet":
                show screen character_gallery
            
             "Gå til møterommet":
                jump meetingroom_blue

            "Gå til sosial-sone":
                jump social_room

            "Gå til kjøkkenområdet":
                jump kitchen

            "Gå tilbake til inngangen til Funkweb":
                jump upper_entrance

            