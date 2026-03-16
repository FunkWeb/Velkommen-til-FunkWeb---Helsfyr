
label kitchen:
    scene temp_kitchen_overview with fade
    
    # hvis person skal implementeres
    # show "person_picture_name" at "position"

    "Her kan du ta deg et glass vann, eller lage deg en god kopp kaffe eller te."
    
    scene temp_kitchen_fridge with fade 

    "Det er eget kjøleskap for kandidater hvor du kan oppbevare mat og drikke."
    
    scene temp_kitchen_overview with fade 

    # videre inn i lokalet har ukjent scenenavn. må legges til.
    menu: 
        "Hvor vil du gå?"
        "sosial sone":
            jump social_room
        "toalettene":
            jump toilets
        # "videre inn i lokalet":
        #    jump scene_for_videre_i_lokalet
        "til det største møterommet":
            jump meetingroom_blue
        "inngangspartiet":
            jump funkweb_offices_entrance
