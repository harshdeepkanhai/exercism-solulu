// Package weather provides tools to Forecast Current Weather Condition of a city.
package weather

// CurrentCondition variable stores the current weather condition.
var CurrentCondition string
// CurrentLocation variable stores the current city.
var CurrentLocation string

// Forecast returns a formatted string of CurrentLocation and 
// CurrentWeather Condition of a city.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
