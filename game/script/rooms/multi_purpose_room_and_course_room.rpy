
label multi_purpose_room_and_course_room:
    scene expression Transform("rooms/temp_meetingroom_grey.webp", fit="cover", align=(0.5, 0.5)) with fade

    "Dette er det andre møterommet. Her er det plass for flere personer. Her holdes det kurs, møter og du kan jobbe sammen i større grupper."
    
    show expression Transform("eric_posing", zoom=0.25, xalign=0.1, yalign=-0.54) with fade 
    eric "Hei! Jeg heter Eric, og er veileder."
    eric "Jeg forsøker å få kandidatene våre inn i markedsgruppen for Sportsmate og FunkWeb, og holder noen lynkurs."
    eric "Og fotokurs."

    "Vil du spille igjen? Gå tilbake til inngangspartiet."
    
    menu:
        "Gå tilbake til inngangspartiet":
            jump funkweb_offices_entrance
        "Avslutt":
            $ MainMenu(confirm=True)()
return
