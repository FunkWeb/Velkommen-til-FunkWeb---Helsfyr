
label funkweb_offices_one_two_three:
    scene expression Transform("images/rooms/temp_offices_management.webp", fit="cover", align=(0.5, 0.5)) with fade

    "Her sitter ledelsen. Du kan banke på hvis du trenger hjelp eller har spørsmål."

    # Vi må finne ut av hvem som sitter hvor før endelig plassering av personer.

    "Hvilket kontor vil du gå til?"

    menu:
        "Kontoret til Laila":
            jump office_laila

        "Kontoret til Hans":
            jump office_hans
    
        "Kontoret til Hans Tore":
            jump office_hans_tore
        
        "Kontoret til Jørgen og Sondre":
            jump jorgen_sondre_offices

        "Gå til kjøkkenet":
            jump kitchen
        
        "Gå til samtalerom":
            jump meetingrooms_three_above_offices_near_kitchen


label office_laila:
    scene expression Transform("images/rooms/temp_offices_management.webp", fit="cover", align=(0.5, 0.5)) with fade
    
    show expression Transform("images/characters/laila_smiling.webp", zoom=0.25, xalign=0.9, yalign=-0.54) with fade
    laila "Her er mitt kontor. Jeg jobber som Tiltaksansvarlig og HR-ansvarlig i FunkWeb."
    
    "Hvor vil du gå videre?"
    
    menu:
        "Gå til ledelses kontoret 1-2-3":
            jump funkweb_offices_one_two_three
        
        "Kontoret til Hans":
            jump office_hans
    
        "Kontoret til Hans Tore":
            jump office_hans_tore
            
        "Kontoret til Jørgen og Sondre":
            jump jorgen_sondre_offices
            
        "Gå til kjøkkenet":
            jump kitchen
            
        "Gå til samtalerom":
            jump meetingrooms_three_above_offices_near_kitchen
   

label office_hans:
    scene expression Transform("images/rooms/temp_offices_management.webp", fit="cover", align=(0.5, 0.5)) with fade
    
    show expression Transform("images/characters/hans_welcome.webp", zoom=0.25, xalign=1.15, yalign=-0.25) with fade

    hans "Hei, jeg heter Hans."
    hans "Jeg driver med daglig drift, karriereveiledning, arbeidsinkludering, undervisning og opplæring."
    hans "Jeg deltar også i styrer og verv innen inkluderingskompetanse."

    "Hvor vil du gå videre?"
        
    menu:
        "Gå til ledelses kontoret 1-2-3":
            jump funkweb_offices_one_two_three

        "Kontor til Laila":
            jump office_laila

        "Kontor til Hans Tore":
            jump office_hans_tore

        "Kontoret til Jørgen og Sondre":
            jump jorgen_sondre_offices

        "Gå til kjøkkenet":
            jump kitchen
                
        "Gå til samtalerom":
            jump meetingrooms_three_above_offices_near_kitchen


 
label office_hans_tore:
    scene expression Transform("images/rooms/temp_offices_management.webp", fit="cover", align=(0.5, 0.5)) with fade
    
    show expression Transform("hans_tore_smiling_two", zoom=0.25, xalign=0.9, yalign=-0.54) with fade 
hans_tore "Hei, jeg heter Hans Tore og er fagansvarlig for alle lærlingene." 
   
"Hvor vil du gå videre?"
   
menu:
    "Gå til ledelses kontoret 1-2-3":
        jump funkweb_offices_one_two_three
            
    "Kontor til Hans":
        jump office_hans
            
    "Kontor til Laila":
            jump office_laila
            
    "Kontoret til Jørgen og Sondre":
        jump jorgen_sondre_offices
            
    "Gå til kjøkkenet":
        jump kitchen
            
    "Gå til samtalerom":
        jump meetingrooms_three_above_offices_near_kitchen
