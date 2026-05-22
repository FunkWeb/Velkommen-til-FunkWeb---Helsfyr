
init python:
    # 1. DATA: List of 16 characters with multiple images
    gallery_items = [
        {"name": "Ingeborg Eikrem", "title": "HR-rådgiver | Jobbspesialist", "desc": "Hei. Jeg heter Ingeborg og er jobbveileder og prosjektleder i FunkSoft. Noen sier jeg elsker Asana (prosjektstyringsverktøyet vårt). Det er ikke helt sant, men jeg liker å ha kontroll på hva som skjer i prosjektene.", "images": ["ingeborg_pointing_up","ingeborg_pointing_down","ingeborg_pointing_right","ingeborg_serious","ingeborg_back","ingeborg_looking_over_shoulder","ingeborg_arms_up"]},
        {"name": "Jørgen Stockfleth Baumann", "title": "Prosjektleder IT | Jobbspesialist", "desc": "Hei, jeg er Jørgen. Som prosjektleder IT i FunkWeb, avholder jeg jevnlige lynkurs, workshops, og utarbeider prosjektbeskrivelser for våres AFT-kandidater.", "images": ["jorgen_posing", "jorgen_pointing_right","jorgen_pointing_left","jorgen_ingeborg_smiling","jorgen_ingeborg_pointing_one","jorgen_ingeborg_pointing_two"]},
        {"name": "Laila Holand", "title": "Tiltaksansvarlig | HR-ansvarlig", "desc": "Jeg heter Laila. Jeg er tiltaksansvarlig og HR-ansvarlig i FunkWeb. Det betyr at jeg har det daglige ansvaret for gjennomføring av tiltakene og personalansvaret for ansatte. Jeg er også veileder. Jeg er veldig glad i de varierte oppgavene jeg har og møte alle fine menneskene.", "images": ["laila_smiling","laila_smiling_two","laila_pointing_left","laila_pointing_left_two","laila_pointing_right","laila_pointing_right_two"]},
        {"name": "Hans Tore Bråten", "title": "Fagansvarlig Lærlinger", "desc": "Hei, jeg heter Hans Tore og jeg er fagansvarlig for alle lærlinger og lærekandidater som er hos oss inne IT-driftsfaget og IT-utviklerfaget.", "images": ["hans_tore_smiling_one","hans_tore_smiling_two","hans_tore_funny","hans_tore_pointing_left","hans_tore_pointing_right"]},
        {"name": "Kristin Svare Nielsen", "title": "Administrasjonskonsulent | HMS-ansvarlig", "desc": "Hei, jeg er Kristin. I tillegg til å være administrasjonskonsulent er jeg verneombud. Det betyr at dere kan kontakte meg dersom dere har tilbakemeldinger i fht arbeidshverdagen i FunkWeb som dere ikke ønsker å ta opp med veileder.", "images": ["kristin_posing","kristin_angry","kristin_pointing_right","kristin_pointing_left"]},
        {"name": "Espen Hermansen", "title": "HR-rådgiver | Jobbspesialist", "desc":"Hei, Espen her! Jeg jobber som veileder og prosjektleder på FunkWeb, og er med på mye forskjellig her. Blant annet jobber jeg med nettbutikken sportsmate.no, er med på FunkSoft og i markedsgruppa.", "images": ["espen_smiling","espen_frustrated","espen_pointing_left","espen_pointing_right_one","espen_pointing_right_two"]},
        {"name": "Ingunn Bøe Hartmann", "title": "Prosjektleder | Webutvikler", "desc": "Fish Enthusiast. Knows too much about trout.", "images": ["ingunn_one", "ingunn_two"]},
        {"name": "Johnny Weseth", "title": "HR-rådgiver | Jobbspesialist", "desc": "Hei, jeg er Johnny. Jeg er veileder her på FunkWeb og jobber i AFT: arbeidforberedende tiltak. Jeg elsker å prate om film, så hvis du ønsker å nerde litt om det, er jeg alltid positiv til det. Jeg snakker også flytende spansk.", "images": ["johnny_smiling_one","johnny_smiling_two","johnny_angry","johnny_frustrated","johnny_pointing_right","johnny_smiling_one"]},
        {"name": "Simen Larsen", "title": "HR-rådgiver | Jobbspesialist", "desc": "Hei! Jeg heter Simen og er jobbveileder i tillegg til prosjektleder for både lærekandidater og i internasjonele prosjekter. Jeg har mange roller i FunkWeb og vært med på det meste her i snart 10 år. Jeg elsker like mye å få til gode samarbeid med arbeidsgiver og kandidat som det å teste produktene til Sportsmate.", "images": ["simen_posing","simen_smiling","simen_angry","simen_cheering_one","simen_cheering_two","simen_pointing_right"]},
        {"name": "Eric Mørk", "title": "HR-rådgiver | Jobbspesialist", "desc": "Jeg heter Eric, og er veileder. Jeg forsøker å få kandidatene våre inn i markedsgruppen for Sportsmate og FunkWeb, og holder noen lynkurs, norskkurs og fotokurs.", "images": ["eric_smiling","eric_posing","eric_smiling_two","eric_pointing"]},
        {"name": "Geir Ivar Nordli", "title": "HR-rådgiver | Jobbspesialist", "desc": "Hei jeg heter Geir Ivar og er veileder her på FunkWeb. Liker å jobbe med mennesker for å avdekke nye muligheter i arbeidslivet. Jeg holder kurs hvordan forbedre oss i telefonsamtalen, intervju, Linkedin og økonomi under ledighet.", "images": ["geir_normal","geir_posing","geir_smiling","geir_talking","geir_open_arms"]},
        {"name": "Reidar Kvam", "title": "HR-rådgiver | Jobbspesialist", "desc": "Jeg heter Reidar og er veileder. Jeg har tidligere jobbet som rekrutterer og med opplæring. Det er en svært god erfaring å ha med seg når jeg bistår kandidater til jobb eller utdanning.", "images": ["reidar_smiling","reidar_smiling_two","reidar_pointing" ]},
        {"name": "Trine-Lise Næssø", "title": "HR-rådgiver | Jobbspesialist", "desc": "Jeg er Trine-Lise. Min største motivasjon er å se våre flotte deltakere lykkes i sin prosess og at de når målene sine. Jeg er glad i å holde kurs, ha gode arbeidsmøter. Spesielt er jeg opptatt av gode CVer og søknader. Si fra om jeg kan gi deg noen gode tips!", "images": ["trine_lise_posing","trine_lise_smiling_three","trine_lise_smiling_two","trine_lise_pointing","trine_lise_pointing_happy"]},
        {"name": "Liv Golbert", "title": "HR-rådgiver | Jobbspesialist", "desc": "Hei, jeg heter Liv. Siden april 2024 har jeg bidratt inn til et godt fellesskap og gode opplevelser for alle i FunkWeb. Jeg har jobbet med tett oppfølging på alt fra CV, søknader, jobbsøk, praksisplasser og jobbintervjuer og språklig og kulturell støtte. Jeg liker å bygge relasjoner, finne løsninger sammen med kandidatene, og kombinere positiv energi med strukturert oppfølging.", "images": ["liv_arms_up", "liv_crossed_arms", "liv_normal", "liv_open_arms", "liv_welcoming", "liv_with_phone"]},
        {"name": "Sondre Benjamin Aasen", "title": "IT-arkitekt", "desc": "Hei, jeg er Sondre: IT-arkitekt og mentor. Kontakt  meg når IT-systemer begynner å knake. For meg handler det ikke først og fremst om teknologi, men om folk. Vi løser ikke dataproblemer, vi løser behovene bak. Jeg bygger og forenkler løsninger som folk faktisk får brukt, og prøver å leve etter et enkelt motto: «gjør kunden til helten i bedriften».", "images": ["sondre_posing"]},
        {"name": "Hans Arnetsen", "title": "Daglig leder", "desc": "Hei. Jeg er 'daglig tjener' i FunkWeb. Jeg jobber for at FunkWeb skal nå visjonen om Sukses for alle. Spennede å møte nye mennesker og jeg prøver å fange opp det vi skal bli bedre i. Ofte er jeg den siste som får høre om en sak, men den eneste som kan gjøre noe med det. Ta gjerne kontakt om stort og smått.", "images": ["hans_normal","hans_welcome","hans_cheering", "hans_celebrate"]},
    ]

screen character_gallery():
    tag menu 
    
    default img_state = {item["name"]: 0 for item in gallery_items}
    # Endret fra "karakter" til "person"
    default active_info = "Velkommen til galleriet! Klikk på en person over for å begynne."

    add Solid("#fab63a") 

    # 1. TITTEL OG TIPS
    text "{b}Persongalleri{/b}" size 45 align (0.5, 0.06) color "#342e57"
    
   
    # KEYBOARD SCROLLING (WASD Support)
    key "w" action Scroll("gallery_vp", "vertical decrease")
    key "W" action Scroll("gallery_vp", "vertical decrease")
    key "s" action Scroll("gallery_vp", "vertical increase")
    key "S" action Scroll("gallery_vp", "vertical increase")

    # The Scrollable Window
    viewport id "gallery_vp": 
        area (40, 140, 1200, 420) 
        scrollbars "vertical"
        mousewheel True      
        draggable True       
        pagekeys True        
        arrowkeys True 
            
        
        
        $ total_rows = max(1, (len(gallery_items) + 3) // 4) 
        
        grid 4 total_rows:
            xalign 0.5
            xfill True
            yalign 0.0
            xspacing 15
            yspacing 25 
            
            for item in gallery_items:

                button:
                    action [
                        SetScreenVariable("active_info", "{b}" + item["title"] + ":{/b} " + item["desc"]),
                        SetDict(img_state, item["name"], (img_state[item["name"]] + 1) % len(item["images"]))
                    ]
                    
                    xsize 250 ysize 420 
                    xalign 0.5
                    background "bg/rectangle_normal.webp"
                    hover_background "bg/rectangle_hover.webp"
                    
                    fixed:
                        xsize 250
                        ysize 420

                        # Bilde – fast posisjon og fast høyde
                        add item["images"][img_state[item["name"]]]:
                            xalign 0.5
                            ypos 10
                            xsize 230
                            ysize 330
                            fit "contain"

                        # Navn – fast posisjon og fast høyde
                        fixed:
                            xpos 0
                            ypos 350
                            xsize 250
                            ysize 60

                            text item["name"]:
                                size 20
                                xalign 0.5
                                text_align 0.5
                                xmaximum 230
                                yalign 0.5
                                color "#342e57"
                            

                            

    # Description Frame
    frame:
        xalign 0.5 ypos 1.0 yanchor 1.0
        xsize 1280 ysize 150
        background Solid("#342e57")
        padding (20, 10)
        text "[active_info]" size 22 xalign 0.5 yalign 0.5 text_align 0.5 color "#ffffff"

    # Return Button
    textbutton "Tilbake":
        align (0.98, 0.03)
        text_size 35
        text_color "#ffffff"
        text_hover_color "#342e57"
        action If(main_menu, ShowMenu("main_menu"), Return())

# The Upgraded Scrollbar
style vscrollbar:
    xsize 25 
    base_bar Solid("#ffffff33") 
    thumb Solid("#ffffff") 
    hover_thumb Solid("#342e57") 
    unscrollable "hide"

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
