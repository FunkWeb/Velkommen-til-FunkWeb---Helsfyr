label kitchen:
    scene expression Transform("images/rooms/temp_kitchen_overview.webp", fit="cover", align=(0.5, 0.5)) with fade
    # hvis person skal implementeres
    # show "person_picture_name" at "position"

    "Her kan du ta deg et glass vann, eller lage deg en god kopp kaffe eller te."
     
    scene expression Transform("images/rooms/temp_kitchen_fridge.webp", fit="cover", align=(0.5, 0.5)) with fade
    "Det er eget kjøleskap for kandidater hvor du kan oppbevare mat og drikke."
    
    scene expression Transform("images/rooms/temp_kitchen_overview.webp", fit="cover", align=(0.5, 0.5)) with fade 

    # videre inn i lokalet har ukjent scenenavn. må legges til.
    menu: 
        "Hvor vil du gå?"
        "sosial sone":
            jump social_room
        "toalettene":
            jump toilets
        "til det største møterommet":
            jump meetingroom_blue
        "inngangspartiet":
            jump funkweb_offices_entrance
        # vei inover i lokalet 
        "mellomgangen":
            jump middle_hallway
        #er ikke sikker på hva dette er ment for, men sletter det ikke for nå
         # "videre inn i lokalet":
        #    jump scene_for_videre_i_lokalet

