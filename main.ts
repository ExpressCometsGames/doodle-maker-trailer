function A() {
    basic.showLeds(`
        . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    `)
    basic.showLeds(`
        . . . . .
                . . . . .
                . # # . .
                . . . . .
                . . . . .
    `)
    basic.showLeds(`
        . . . . .
                . # . . .
                . # # . .
                . . . . .
                . . . . .
    `)
    basic.showLeds(`
        . . . . .
                # # . . .
                . # # . .
                . . . . .
                . . . . .
    `)
    basic.showLeds(`
        . . . . .
                # # . . #
                . # # . .
                . . . . .
                . . . . .
    `)
    basic.showLeds(`
        . . . . .
                # # . . #
                . # # . .
                . . . . .
                . . . . .
    `)
    basic.showLeds(`
        . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    `)
    basic.showIcon(IconNames.Happy)
    basic.pause(500)
    basic.showLeds(`
        . . # . .
                . # . # .
                . # # # .
                . # . # .
                . . . . .
    `)
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    Opening()
})
function Opening() {
    basic.showLeds(`
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    `)
    basic.showLeds(`
        . . . . .
                . . . . .
                . . . . #
                . . . . #
                . . . . .
    `)
    basic.showLeds(`
        . . . . .
                . . . . .
                . . . # #
                . . . # #
                . . . . .
    `)
    basic.showLeds(`
        . . . . .
                . . # # .
                . . # # #
                . . . . .
                . . . . .
    `)
    basic.showLeds(`
        . . . . .
                . # # # .
                . # # . #
                . . . . .
                . . . . .
    `)
    basic.showLeds(`
        . . . . .
                # # # # .
                # # . . #
                . . . . .
                . . . . .
    `)
    basic.showLeds(`
        . . . . .
                . . # # .
                # # . . #
                # # . . .
                . . . . .
    `)
    basic.showLeds(`
        . . . . .
                . . # # .
                # # . . #
                # # . # .
                . . # . #
    `)
    basic.showLeds(`
        . . . . .
                . . # # .
                # # . . #
                # # . . .
                . . . # .
    `)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    `)
    basic.showLeds(`
        . . . . #
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    `)
    basic.showLeds(`
        . . . . #
                . . . # .
                . . . . .
                . . . . .
                . . . . .
    `)
    basic.showLeds(`
        . . . . #
                . . . # .
                . . # . .
                . . . . .
                . . . . .
    `)
    basic.showLeds(`
        . . . . #
                . . # # .
                . # # # .
                . . # . .
                . . . . .
    `)
    basic.showLeds(`
        . . # . #
                . # . # .
                # . # . #
                . # . # .
                . . # . .
    `)
    basic.showLeds(`
        . # . . #
                # . . # .
                . . # . .
                # . . . #
                . # . # .
    `)
    basic.showLeds(`
        # . . . #
                . . . # .
                . . . . .
                . . . . .
                # . . . #
    `)
    basic.showLeds(`
        . . . . #
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    `)
    basic.showLeds(`
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    `)
    basic.showString("From the team that brought you Galaxy journey")
    basic.showLeds(`
        . . # . .
                . . . . #
                . . . . .
                . . . . .
                . . # . .
    `)
    basic.showLeds(`
        . . . . .
                . . # . .
                . . . . #
                . . # . .
                . . # . .
    `)
    basic.showLeds(`
        . . . . .
                . . . . .
                . . # . .
                . . . . #
                . . # . .
    `)
    basic.showLeds(`
        . . . . .
                . . # . .
                . # . # .
                . . # . .
                . . # . #
    `)
    basic.showLeds(`
        # . . # .
                . . . . .
                . . . . .
                . . . . .
                . . # . .
    `)
    basic.showString("Coming April 1st")
    basic.showLeds(`
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    `)
    basic.showString("Doodle Maker")
    A()
}

basic.showLeds(`
    . . # . .
        . # . # .
        . # # # .
        . # . # .
        . . . . .
`)
