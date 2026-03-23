
label funkweb_offices_one_two_three:
    scene temp_offices_management with fade

"Her sitter ledelsen. Du kan banke på hvis du trenger hjelp eller har spørsmål."

    # Vi må finne ut av hvem som sitter hvor før endelig plassering av personer.

menu:
    "Hvilket kontor vil du gå til?":
        "Kontor 1 (Hans)":
            jump funkweb_offices_one

        "Kontor 2 (ukjent)":
            jump funkweb_offices_two

        "Kontor 3 (ukjent)":
            jump funkweb_offices_three

        "Kontor: Jørgen og Sondre":
            jump jorgen_sondre_offices

        "Gå tilbake til kjøkkenet":
            jump kitchen

        "Gå til samtalerom"
            jump meetingrooms_three_above_offices_near_kitchen
return


label office_hans:
    scene temp_office_hans with fade
    show hans at right

    hans "Hei, jeg heter Hans."
    hans "Jeg driver med daglig drift, karriereveiledning, arbeidsinkludering, undervisning og opplæring."
    hans "Jeg deltar også i styrer og verv innen inkluderingskompetanse."

    menu:
        "Hvor vil du gå videre?":

            "Tilbake til ledelseskontorene":
                jump funkweb_offices_one_two_three

            "Kontor 2 (ukjent)":
                jump office_unknown_two

            "Kontor 3 (ukjent)":
                jump office_unknown_three

            "Kontor: Jørgen og Sondre":
                jump jorgen_sondre_offices

            "Gå tilbake til kjøkkenet":
                jump kitchen
                
            "Gå til samtalerom"
            jump meetingrooms_three_above_offices_near_kitchen
    return

label office_unknown_two:
    scene temp_office_unknown_two with fade
    

    menu:
        "Hvor vil du gå videre?":
            "Tilbake til ledelseskontorene":
                jump funkweb_offices_one_two_three
            "Kontor 1 (Hans)":
                jump office_hans
            "Kontor 3 (ukjent)":
                jump office_unknown_three
            "Kontor: Jørgen og Sondre":
                jump jorgen_sondre_offices
            "Gå tilbake til kjøkkenet":
                jump kitchen
            "Gå til samtalerom"
            jump meetingrooms_three_above_offices_near_kitchen
    return

label office_unknown_three:
    scene temp_office_unknown_three with fade
    
   
    menu:
        "Hvor vil du gå videre?":
            "Tilbake til ledelseskontorene":
                jump funkweb_offices_one_two_three
            "Kontor 1 (Hans)":
                jump office_hans
            "Kontor 2 (ukjent)":
                jump office_unknown_two
            "Kontor: Jørgen og Sondre":
                jump jorgen_sondre_offices
            "Gå tilbake til kjøkkenet":
                jump kitchen
            "Gå til samtalerom"
            jump meetingrooms_three_above_offices_near_kitchen
    return  