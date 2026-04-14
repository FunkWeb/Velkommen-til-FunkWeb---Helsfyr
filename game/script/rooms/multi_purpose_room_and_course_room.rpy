
label multi_purpose_room_and_course_room:
    scene expression Transform("rooms/temp_meetingroom_grey.webp", fit="cover", align=(0.5, 0.5)) with fade

    "Dette er det andre møterommet. Her er det plass for flere personer. Her holdes det kurs, møter og du kan jobbe sammen i større grupper."
    
    show eric_posing at left

    eric "Hei! Jeg heter Eric, og er veileder."
    eric "Jeg forsøker å få kandidatene våre inn i markedsgruppen for Sportsmate og FunkWeb, og holder noen lynkurs."
    eric "Og fotokurs."

    menu:
        "Hvor vil du gå?"
        "til sosial-sone":
            jump social_room
        "til kjøkkenet":
            jump kitchen
        "til toalettene":
            jump toilets
        "til det største møterommet":
            jump meetingroom_blue
        "til inngangspartiet":
            jump funkweb_offices_entrance

return