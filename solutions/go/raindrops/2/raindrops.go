package raindrops

import (
    "strconv"
    "strings"
)

var rules = []struct {
	divisor int
	sound   string
}{
	{3, "Pling"},
	{5, "Plang"},
	{7, "Plong"},
}

func writeFizzbuzz(fizzBuzz *strings.Builder, number int, divisor int, addedWord string) {
    if number % divisor == 0 {
    	fizzBuzz.WriteString(addedWord)
    }
}

func Convert(number int) string {
    var fizzBuzz strings.Builder
	for _, rule := range rules {
		if number%rule.divisor == 0 {
			fizzBuzz.WriteString(rule.sound)
		}
	}
	if fizzBuzz.Len() == 0 {
		return strconv.Itoa(number)
	}
	return fizzBuzz.String()
}
