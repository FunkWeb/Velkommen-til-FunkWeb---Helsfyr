define j = Character("Jørgen", color="#4A90E2")
define s = Character("Sondre", color="#50E3C2")  
image bg temp_office_jorgen_sondre = "images/bg/temp_office_jorgen_sondre.webp"
image jorgen = "images/characters/jorgen_posing.webp"

label velkommen_funkweb_helsfyr:

    scene bg temp_office_jorgen_sondre with fade

    show jorgen at left
    j "Hei! Jeg heter Jørgen, og som Prosjektleder IT i FunkWeb avholder jeg jevnlige lynkurs og workshops, og utarbeider prosjektbeskrivelser for våre AFT-kandidater."

    show jorgen at right
    s "Hei! Jeg heter Sondre. Jeg er IT-arkitekt og jobber med IT-utvikling. Jeg fungerer også som veileder for jobbsøkere og samarbeidspartnere (TBD)."

    hide jorgen

    return