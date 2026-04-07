
label upper_entrance:
    scene temp_funkweb_entrance with fade
     "Her er inngangen til Funkweb. Ring på døren så slippes du inn."
   
    menu:
        "Hva vil du gjøre?":
            "Ring på døren":
                scene temp_hallway_doorbell with fade
                "Du ringer på døren."
                scene temp_funkweb_door_open with fade
                "Døren åpnes og du blir sluppet inn."
                jump funkweb_offices_entrance

            "Gå tilbake til resepsjonen":
                jump reception


