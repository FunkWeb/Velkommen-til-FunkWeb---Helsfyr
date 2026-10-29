label meetingrooms_three_above_offices_near_kitchen:
    
    scene expression Transform("images/rooms/meetingrooms.webp", fit="cover", align=(0.5, 0.5)) with fade

    "Dette er samtalerom hvor du kan møtes med din veileder, eller samles i mindre grupper for å jobbe sammen."
    "Vi har seks slike rom: 2, 3, 4, 5, 6 og 7."

    "Hvor vil du gå?"
    
    call screen navigation_placement("meetingrooms_three_above_offices_near_kitchen")
