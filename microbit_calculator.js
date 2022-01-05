let calculate_total = 0
let operator = 0
let number = 0
let total = 0
basic.forever(() => {
  if (input.buttonIsPressed(Button.AB)) {
    if (operator == 0) {
      total = total + number
    }
    if (operator == 1) {
      total = total - number
    }
    if (operator == 2) {
      total = total * number
    }
    if (operator == 3) {
      total = total / number
    }
    basic.showNumber(total)
  } else {
    if (input.buttonIsPressed(Button.A)) {
      number += 1
      calculate_total = 1
      if (number < 0 || number > 9) {
        number = 0
      }
      basic.showNumber(number)
    }
    if (input.buttonIsPressed(Button.B)) {
      if (calculate_total) {
        calculate_total = 0
        if (operator == 0) {
          total = total + number
        }
        if (operator == 1) {
          total = total - number
        }
        if (operator == 2) {
          total = total * number
        }
        if (operator == 3) {
          total = total / number
        }
      }
      operator += 1
      if (operator < 0 || operator > 3) {
        operator = 0
      }
      if (operator == 0) {
        basic.showLeds(`
          . . # . .
          . . # . .
          # # # # #
          . . # . .
          . . # . .
          `)
      }
      if (operator == 1) {
        basic.showLeds(`
          . . . . .
          . . . . .
          # # # # #
          . . . . .
          . . . . .
          `)
      }
      if (operator == 2) {
        basic.showLeds(`
          # . . . #
          . # . # .
          . . # . .
          . # . # .
          # . . . #
          `)
      }
      if (operator == 3) {
        basic.showLeds(`
          . . # . .
          . . . . .
          # # # # #
          . . . . .
          . . # . .
          `)
      }
    }
  }
})