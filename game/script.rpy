# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    # 1. DATA: List of 16 characters with multiple images
    gallery_items = [
        {"name": "Ingeborg Eikrem", "title": "HR-rådgiver / jobbspesialist", "desc": "Hei. Jeg heter Ingeborg og er jobbveileder og prosjektleder i FunkSoft. Noen sier jeg elsker Asana (prosjektstyringsverktøyet vårt). Det er ikke helt sant, men jeg liker å ha kontroll på hva som skjer i prosjektene. ", "images": ["ingeborg_arms_up", "ingeborg_back","ingeborg_looking_over_shoulder"]},
        {"name": "Jørgen Stockfleth Baumann", "title": "Coffee Demon", "desc": "Don't talk to her before 10am.", "images": ["char2_a", "char2_b"]},
        {"name": "Laila Holand", "title": "Flight Risk", "desc": "Often forgets gravity exists.", "images": ["char3_a", "char3_b"]},
        {"name": "Hans Tore Bråten", "title": "Snack Thief", "desc": "Will sell your soul for a strawberry.", "images": ["char4_a", "char4_b"]},
        {"name": "Kristin Svare Nielsen", "title": "Chaos Element", "desc": "Banned from the library for thinking too loud.", "images": ["char5_a", "char5_b"]},
        {"name": "Espen Hermansen", "title": "The Only Adult", "desc": "Tired of everyone's nonsense.", "images": ["char6_a", "char6_b"]},
        {"name": "Ingunn Bøe Hartmann", "title": "Fish Enthusiast", "desc": "Knows too much about trout.", "images": ["char7_a", "char7_b"]},
        {"name": "Johnny Weseth", "title": "Main Character", "desc": "The world revolves around her.", "images": ["char8_a", "char8_b"]},
        {"name": "Simen Larsen", "title": "Edge Lord", "desc": "Wears hoodies in the summer to look cool.", "images": ["char9_a", "char9_b"]},
        {"name": "Eric Mørk", "title": "Small But Mighty", "desc": "Don't mention his height.", "images": ["char10_a", "char10_b"]},
        {"name": "Geir Ivar Nordli", "title": "Professional Hater", "desc": "Has a list of things she finds annoying.", "images": ["char11_a", "char11_b"]},
        {"name": "Reidar Kvam", "title": "Certified Himbo", "desc": "Strong as an ox, twice as confused.", "images": ["char12_a", "char12_b"]},
        {"name": "Trine-Lise Næssø", "title": "Tech Wizard", "desc": "Jeg er Trine-Lise og har hatt gleden av å jobbe i FunkWeb siden 2013. Har jobbet på flere typer tiltak og nå AFT. Min største motivasjon er å se våre flotte deltakere lykkes i sin prosess og når de mål vi avklarer sammen. Er glad i å holde kurs, ha gode arbeidsmøter og liker å være opptatt av at CV og søknader er så bra som mulig slik at vi kan ha fokus på alle de andre virkemidlene vi har for å nå ut til arbeidsgivere. ", "images": ["char13_a", "char13_b"]},
        {"name": "Liv Golbert", "title": "Plant Mom", "desc": "Talks to her ferns. They talk back.", "images": ["char14_a", "char14_b"]},
        {"name": "Sondre Benjamin Aasen", "title": "Speed Demon", "desc": "Only moves at one speed: Sprint.", "images": ["char15_a", "char15_b"]},
    ]

# 2. SCREEN: The interactive 4x4 Grid (180x150)
screen character_gallery():
    # Track which image index is active for each character
    default img_state = {item["name"]: 0 for item in gallery_items}
    default active_info = "Click a character to cycle images and see their profile!"

    add Solid("#00f7ff") # Dark blue background

    vbox:
        align (0.5, 0.02)
        spacing 20
        text "Character Gallery" size 40 xalign 0.5 color "#ffffff"

        grid 4 4:
            xalign 0.5
            spacing 8
            for item in gallery_items:
                $ current_idx = img_state[item["name"]]
                $ current_img = item["images"][current_idx]

                button:
                    # Clicking updates text AND cycles the image
                    action [
                        SetScreenVariable("active_info", "{b}" + item["title"] + ":{/b} " + item["desc"]),
                        SetDict(img_state, item["name"], (current_idx + 1) % len(item["images"]))
                    ]
                    
                    xsize 180 ysize 130
                    background Solid("#ff0000")
                    hover_background Solid("#00fc00")
                    
                    vbox:
                        align (0.5, 0.5)
                        add current_img size (120, 100) xalign 0.5
                        text item["name"] size 18 xalign 0.5 color "#ffffff"
            null
    # Info frame at the bottom
    frame:
        xalign 0.5 ypos 1.0 yanchor 1.0
        xsize 1280 ysize 90
        background Solid("#316ff7")
        padding (20, 20)
        text "[active_info]" size 16 xalign 0.5 yalign 0.5 text_align 0.5 color "#ffffff"

    textbutton "Return" action Return() align (0.95, 0.05) text_color "#ffffff"




define ingeborg = Character("Ingeborg")
define jorgen = Character("Jørgen")
define laila = Character("Laila")
define eric = Character("Eric")
define simen = Character("Simen")
define johnny = Character("Johnny")
define hans = Character("Hans")
define hans_tore = Character("Hans Tore")
define kristin = Character("Kristin")
define espen = Character("Espen")
define ingunn = Character("Ingunn")
define geir = Character("Geir")
define reidar = Character("Reidar")
define trine_lise = Character("Trine-Lise")
define liv = Character("Liv")
define sondre = Character("Sondre")
# The game starts here.

label start:
jump outside_entrance
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    

    # These display lines of dialogue.

   
    # This ends the game.

return
