
label outside_entrance:
    scene expression Transform("images/rooms/temp_entrance_outside.webp", fit="cover", align=(0.5, 0.5)) with fade
    
    "Velkommen til Funkweb på Helsfyr Panorama!"
    "I dette spillet skal du bli kjent med lokalene våre, menneskene som jobber her, og rommene du kan bruke."
    "Klikk deg rundt for å utforske."

    menu:
        "Gå inn.":
            jump reception

return