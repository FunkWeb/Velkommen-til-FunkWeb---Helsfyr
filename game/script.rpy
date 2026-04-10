# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


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

    e "You've created a new Ren'Py game."
    
    e "Once you add a story, pictures, and music, you can release it to the world!"

    menu:
        "\"Hvor er toalettene?\"":
            jump toilets

    # This ends the game.

 return
