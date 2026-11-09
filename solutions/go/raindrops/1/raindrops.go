package raindrops

import "strconv"
func Convert(number int) string {
    var FizzBuzz string = ""
	if (number % 3 == 0) {
        FizzBuzz += "Pling"
    }
    if (number % 5 == 0) {
        FizzBuzz += "Plang"
    }
    if (number % 7 == 0) {
        FizzBuzz += "Plong"
    }
    if (FizzBuzz == "") {
        return strconv.Itoa(number)
    } else {
        return FizzBuzz
    }
}
