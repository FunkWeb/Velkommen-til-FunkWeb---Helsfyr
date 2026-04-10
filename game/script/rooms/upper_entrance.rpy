
label upper_entrance:
    scene expression Transform("images/rooms/temp_funkweb_entrance.webp", fit="cover", align=(0.5, 0.5)) with fade
    "Her er inngangen til Funkweb. Ring på døren så slippes du inn."
   
    "Hva vil du gjøre?"
    
    menu:
            "Ring på døren":
                scene expression Transform("images/rooms/temp_hallway_doorbell.webp", fit="cover", align=(0.5, 0.5)) with fade
                "Du ringer på døren."
                scene expression Transform("images/rooms/temp_funkweb_door_open.webp", fit="cover", align=(0.5, 0.5)) with fade
                "Døren åpnes og du blir sluppet inn."
                jump funkweb_offices_entrance

            "Gå tilbake til resepsjonen":
                jump reception


