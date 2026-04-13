
label social_room:
    # midlertidig bakgrunssbilde som starter med temp, må byttes med endelig bakgrunn.
    scene expression Transform("images/rooms/temp_social_zone.webp", fit="cover", align=(0.5, 0.5)) with fade
    "Her kan du sosialisere og ta deg en pause sammen med de andre på huset. "
    
    show expression Transform("images/characters/laila_smiling.webp", zoom=0.25, xalign=0.1, yalign=-0.54) with fade
    laila "Hei, jeg heter Laila." 
    laila "Jeg er Tiltaksansvarlig og HR-ansvarlig i FunkWeb." 
    laila "Det betyr at jeg har det daglige ansvaret for gjennomføring av tiltakene, og jeg har personalansvaret for ansatte." 
    laila "Jeg er også veileder noen ganger."
    laila "Jeg er veldig glad i de varierte oppgavene jeg har, og jeg føler meg priviligert."
    laila "Jeg liker spesielt å møte alle fine mennesker som av ulike grunner er  tilknyttet FunkWeb."
    
    # videre inn i lokalet har ukjent scenenavn. må legges til.
    menu: 
        "Hvor vil du gå?"
        "kjøkken":
            jump kitchen
        # "videre inn i lokalet":
        #    jump scene_for_videre_i_lokalet
        "til det største møterommet":
            jump meetingroom_blue
        "inngangspartiet":
            jump funkweb_offices_entrance

