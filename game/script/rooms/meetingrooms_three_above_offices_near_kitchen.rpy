label meetingrooms_three_above_offices_near_kitchen:
    
    scene expression Transform("images/rooms/temp_meetingrooms.webp", fit="cover", align=(0.5, 0.5)) with fade

    "Dette er samtalerom hvor du kan møtes med din veileder, eller samles i mindre grupper for å jobbe sammen."
    "Vi har 6 slike rom: Grønn, Gul, Lilla, Oransje, Rød og Sort."

    "Hvor vil du gå?"
    
    menu: 
        "Gå til veileder kontorene":
            jump aft_offices
        
        "Gå tilbake til kontoret til Jørgen og Sondre":
            jump jorgen_sondre_offices   
        
        "Gå tilbake til kontor 1, 2 og 3":
            jump funkweb_offices_one_two_three     
            
        "Gå tilbake til kjøkkenet":
            jump kitchen
        
        "Gå tilbake til sosialsona":
            jump social_room
            
        "Gå tilbake til toalettene":
            jump toilets
