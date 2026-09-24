
# ============================================================
# GENERIC NAVIGATION ARROW
# ============================================================


screen navigation_arrow(x, y, rotation, destination, tooltip):

    default hovered = False

    imagebutton:
        xalign x
        yalign y

        at Transform(
            zoom=0.25,
            rotate=rotation
        )

        idle "images/ui/right_arrow_idle.png"
        hover "images/ui/right_arrow_hover.png"

        focus_mask True

        hovered SetScreenVariable("hovered", True)
        unhovered SetScreenVariable("hovered", False)

        action Jump(destination)
        tooltip tooltip

    if hovered:

        text tooltip:
            xalign x
            yalign y - 0.06


# ============================================================
# NAVIGATION DATA
# ============================================================

# 
define navigation_arrows_data = {

    "upper_entrance": [
        (
            0.52, 0.59, -90,
            "ring_doorbell",
            "Ring på døren"
        ),
        (
            0.69, 0.55, 0,
            "reception",
            "Tilbake til resepsjonen"
        )
    ],
    
    "funkweb_offices_entrance": [
        (
            0.50, 1.0, 90,
            "meetingroom_blue",
            "Gå til det største møterommet"),

        (
            0.80, 0.43, 0,
            "upper_entrance",
            "Gå til inngangen til FunkWeb"),

        (
            0.20, 0.43, 180,
            "social_room",
            "Gå til sosialsona"),
    ],

    "meetingroom_blue": [
        (
            0.90, 0.50, 0,
            "kitchen",
            "Gå til kjøkkenet"),
        (
            0.50, 0.90, 90,
            "funkweb_offices_entrance",
            "Gå til inngangspartiet")
    ],

    "social_room": [
        (
            0.30, 0.50, 315,
            "meetingrooms_three_above_offices_near_kitchen",
            "Gå til samtalerommene"),

        (
            0.30, 0.90, 45,
            "kitchen",
            "Gå til kjøkkenet"),

        (
            0.10,0.90,135,
            "funkweb_offices_entrance",
            "Gå til inngangspartiet"),

        (
            0.10, 0.50, 180,
            "meetingroom_blue",
            "Gå til det største møterommet")
    ],

    "meetingrooms_three_above_offices_near_kitchen": [
        (
            0.10, 0.99, 80,
            "social_room",
            "Gå til sosialsona"),

        (
            0.10,0.70,345,
            "aft_candidate_work_area",
            "Gå til arbeidsområdet for kandidater"), 
    ]
}


# ============================================================
# GENERIC NAVIGATION PLACEMENT
# ============================================================

screen navigation_placement(room):

    for x, y, rotation, destination, tooltip in navigation_arrows_data[room]:

        use navigation_arrow(
            x,
            y,
            rotation,
            destination,
            tooltip
        )
        $ current_tooltip = GetTooltip()

    if current_tooltip:

        frame:
            xalign 0.5
            yalign 0.6

            background "#000000cc"
            padding (15, 8)

            text current_tooltip:
                color "#ffffff"
                size 24
                text_align 0.5
