// Package weather provides weather forecast functionality.
package weather

// CurrentCondition represents the current weather condition.
var CurrentCondition string

// CurrentLocation represents the current location.
var CurrentLocation string

// Forecast returns the weather condition for a given city.
func Forecast(city, condition string) string {
	return city + " - current weather condition: " + condition
}