label toilets:

scene expression Transform("rooms/bathrooms.webp", fit="cover", align=(0.5, 0.5))

"Her har vi et stort HC-toalett og to andre toaletter."

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
