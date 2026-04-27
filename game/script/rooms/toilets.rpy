
label toilets:

scene expression Transform("rooms/bathrooms.webp", fit="cover", align=(0.5, 0.5))

"Her har vi 1 stort HC-toalett og 2 andre toaletter."

menu:
    "Hvor vil du gå?"
    "sosial-sone":
        jump social_room
    # "videre inn i lokalet":
    #    jump scene_for_videre_i_lokalet
    "det største møterommet":
        jump meetingroom_blue
    "inngangspartiet":
        jump funkweb_offices_entrance
    #retur fra hvor man kom fra. 
    "tilbake til kjøkkenet":
        jump kitchen
return

