def A():
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . # # . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . # . . .
                . # # . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                # # . . .
                . # # . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                # # . . #
                . # # . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                # # . . #
                . # # . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    """)
    basic.show_icon(IconNames.HAPPY)
    basic.pause(500)
    basic.show_leds("""
        . . # . .
                . # . # .
                . # # # .
                . # . # .
                . . . . .
    """)

def on_button_pressed_a():
    Opening()
input.on_button_pressed(Button.A, on_button_pressed_a)

def Opening():
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . #
                . . . . #
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . # #
                . . . # #
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . # # .
                . . # # #
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . # # # .
                . # # . #
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                # # # # .
                # # . . #
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . # # .
                # # . . #
                # # . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . # # .
                # # . . #
                # # . # .
                . . # . #
    """)
    basic.show_leds("""
        . . . . .
                . . # # .
                # # . . #
                # # . . .
                . . . # .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . #
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . #
                . . . # .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . #
                . . . # .
                . . # . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . #
                . . # # .
                . # # # .
                . . # . .
                . . . . .
    """)
    basic.show_leds("""
        . . # . #
                . # . # .
                # . # . #
                . # . # .
                . . # . .
    """)
    basic.show_leds("""
        . # . . #
                # . . # .
                . . # . .
                # . . . #
                . # . # .
    """)
    basic.show_leds("""
        # . . . #
                . . . # .
                . . . . .
                . . . . .
                # . . . #
    """)
    basic.show_leds("""
        . . . . #
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_string("From the team that brought you Galaxy journey")
    basic.show_leds("""
        . . # . .
                . . . . #
                . . . . .
                . . . . .
                . . # . .
    """)
    basic.show_leds("""
        . . . . .
                . . # . .
                . . . . #
                . . # . .
                . . # . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # . .
                . . . . #
                . . # . .
    """)
    basic.show_leds("""
        . . . . .
                . . # . .
                . # . # .
                . . # . .
                . . # . #
    """)
    basic.show_leds("""
        # . . # .
                . . . . .
                . . . . .
                . . . . .
                . . # . .
    """)
    basic.show_string("Coming April 1st")
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_string("Doodle Maker")
    A()
basic.show_leds("""
    . . # . .
        . # . # .
        . # # # .
        . # . # .
        . . . . .
""")