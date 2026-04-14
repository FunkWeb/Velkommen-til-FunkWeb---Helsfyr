
label canteen:
    # midlertidig bakgrunssbilder, må byttes med endelig bakgrunn.
    scene expression Transform("images/rooms/temp_canteen_entrance.webp", fit="cover", align=(0.5, 0.5)) with fade 
    pause 1
    scene expression Transform("images/rooms/temp_canteen_overview.webp", fit="cover", align=(0.5, 0.5)) with fade
    
    "Kantina er et sosialt samlingspunkt hvor man kan spise lunsj, ta pauser og bli kjent med kollegaer."

    menu canteen_menu:
        "Ta meg tilbake til resepsjonen":
            jump reception
        "Ta meg til 5. etasje og FunkWeb":
            jump upper_entrance

return