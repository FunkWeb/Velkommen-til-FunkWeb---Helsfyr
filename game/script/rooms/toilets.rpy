label toilets:

scene expression Transform("rooms/bathrooms.webp", fit="cover", align=(0.5, 0.5))

"Her har vi 1 stort HC-toalett og 2 andre toaletter."

menu:
    "Gå tilbake til resepjsonen":
        jump reception
    "Gå til sosialsona":
        jump social_room
    "Gå til kjøkkenet":
        jump kitchen
    "Gå til møterommet":
        jump meetingroom_blue
    
return
