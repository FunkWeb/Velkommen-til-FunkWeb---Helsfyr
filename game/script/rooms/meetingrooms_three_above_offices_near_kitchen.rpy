label meetingrooms_three_above_offices_near_kitchen:
    
    scene expression Transform("images/rooms/temp_meetingrooms.webp", fit="cover", align=(0.5, 0.5)) with fade

    "Dette er samtalerom hvor du kan møtes med din veileder, eller samles i mindre grupper for å jobbe sammen."
    "Vi har seks slike rom: 2, 3, 4, 5 og 6."

    "Hvor vil du gå?"
    
    menu: 
        "Gå til AFT-veileder kontoret":
            jump aft_offices
        
        "Gå til kontoret til Jørgen og Sondre":
            jump jorgen_sondre_offices   
        
        "Gå til ledelses kontoret 1-2-3":
            jump funkweb_offices_one_two_three     
            
        "Gå til kjøkkenet":
            jump kitchen
        
        "Gå til sosialsona":
            jump social_room
            
        "Gå til toalettene":
            jump toilets
