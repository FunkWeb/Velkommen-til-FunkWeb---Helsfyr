
label outside_entrance:
    scene expression Transform("images/bg/helsfyr_panorama_sol.webp", fit="cover", align=(0.5, 0.5)) with fade
    pause 1.8
    scene expression Transform("images/bg/inngangsparti_helsfyr_panorama_sol.webp", fit="cover", align=(0.5, 0.5)) with fade
    
    "Velkommen til FunkWeb på Helsfyr Panorama!"
    "I dette spillet skal du bli kjent med lokalene våre, menneskene som jobber her, og rommene du kan bruke."
    "Klikk deg rundt for å utforske."

    menu:
        "Velkommen inn":
            jump reception
