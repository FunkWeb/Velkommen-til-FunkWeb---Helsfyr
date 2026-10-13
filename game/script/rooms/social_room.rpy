
label social_room:
    scene expression Transform("images/rooms/social_zone_one.webp", fit="cover", align=(0.5, 0.5)) with fade
    pause 1.0
    scene expression Transform("images/rooms/social_zone_two.webp", fit="cover", align=(0.5, 0.5)) with fade
    "Her kan du sosialisere og ta deg en pause sammen med de andre på huset. "
    
    show expression Transform("images/characters/laila_smiling.webp", zoom=0.25, xalign=0.9, yalign=-0.54) with fade
    laila "Hei, jeg heter Laila." 
    laila "Jeg er tiltaksansvarlig og HR-ansvarlig i FunkWeb." 
    laila "Det betyr at jeg har det daglige ansvaret for gjennomføring av tiltakene, og jeg har personalansvaret for ansatte." 
    laila "Jeg er også veileder noen ganger."
    laila "Jeg er veldig glad i de varierte oppgavene jeg har, og jeg føler meg priviligert."
    laila "Jeg liker spesielt å møte alle fine mennesker som av ulike grunner er  tilknyttet FunkWeb."
    
    # videre inn i lokalet har ukjent scenenavn. må legges til.
    menu: 
        "Hvor vil du gå?"
        "Gå til kjøkkenet":
            jump kitchen
        "Gå til samtalerommene":
            jump meetingrooms_three_above_offices_near_kitchen
        "Til det største møterommet":
            jump meetingroom_blue
        "Gå til inngangspartiet":
            jump funkweb_offices_entrance
        