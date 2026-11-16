label intro_video:

    scene black
    # Starts intro video showing the pathway from Helsfyr T to Panorama.
    $ renpy.movie_cutscene("videos/Fra Helsfyr til Panorama med Tid.webm", stop_music=True)

    # After the video ends, jump to the outside_entrance label.
    jump outside_entrance

    return