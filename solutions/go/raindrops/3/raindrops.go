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


func Convert(number int) string {
    var sb strings.Builder
	for _, rule := range rules {
		if number%rule.divisor == 0 {
			sb.WriteString(rule.sound)
		}
	}
	if sb.Len() == 0 {
		return strconv.Itoa(number)
	}
	return sb.String()
}
