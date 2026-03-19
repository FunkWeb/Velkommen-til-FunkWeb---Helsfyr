label meetingrooms_three_above_offices_near_kitchen:
    
    scene temp_meetingrooms with fade

    "Dette er samtalerom hvor du kan møtes med din veileder, eller samles i mindre grupper for å jobbe sammen."
    "Vi har 6 slike rom: Grønn, Gul, Lilla, Oransje, Rød og Sort."

    # videre inn i lokalet har ukjent scenenavn. må legges til.
    menu: 
        "Hvor vil du gå?"
        "sosial sone":
            jump social_room
        "toalettene":
            jump kitchen
        # "videre inn i lokalet":
        #    jump scene_for_videre_i_lokalet
        "til kontor 1, 2 og 3":
            jump funkweb_offices_one_two_three
return