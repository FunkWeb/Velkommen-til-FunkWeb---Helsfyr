
label canteen:
    # midlertidig bakgrunssbilder, må byttes med endelig bakgrunn.
    scene temp_canteen_entrance with fade 
    pause 1
    scene temp_canteen_overview with fade 
    
    "Kantina er et sosialt samlingspunkt hvor man kan spise lunsj, ta pauser og bli kjent med kollegaer."

    menu canteen_menu:
        "Ta meg tilbake til resepsjon":
            jump reception
        "Ta meg til 5. etasje og FunkWeb":
            jump upper_entrance

return