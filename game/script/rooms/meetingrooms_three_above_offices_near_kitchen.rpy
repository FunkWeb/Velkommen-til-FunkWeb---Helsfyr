label meetingrooms_three_above_offices_near_kitchen:
    
    scene expression Transform("images/rooms/temp_meetingrooms.webp", fit="cover", align=(0.5, 0.5)) with fade

    "Dette er samtalerom hvor du kan møtes med din veileder, eller samles i mindre grupper for å jobbe sammen."
    "Vi har 6 slike rom: Grønn, Gul, Lilla, Oransje, Rød og Sort."

    "Hvor vil du gå?"
    
    menu: 
        "gå til veileder kontorene":
            jump aft_offices
        
        "gå tilbake til kontoret til Jørgen og Sondre":
            jump jorgen_sondre_offices   
        
        "gå tilbake til kontor 1, 2 og 3":
            jump funkweb_offices_one_two_three     
            
        "gå tilbake til kjøkkenet":
            jump kitchen
        
        "gå tilbake til sosial sone":
            jump social_room
            
        "gå tilbake til toalettene":
            jump toilets
        
        
        
