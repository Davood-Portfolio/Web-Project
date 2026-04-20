package booking

import "time"

// Schedule returns a time.Time from a string containing a date.
func Schedule(date string) time.Time {
	layouts := []string{
		"Monday, January 2, 2006 15:04:05",
		"January 2, 2006 15:04:05",
		"1/2/2006 15:04:05",
	}

	for _, layout := range layouts {
		if t, err := time.Parse(layout, date); err == nil {
			return t
		}
	}
	return time.Time{}
}

// HasPassed returns whether a date has passed.
func HasPassed(date string) bool {
	t := Schedule(date)
	return t.Before(time.Now())
}

// IsAfternoonAppointment returns whether a time is in the afternoon.
func IsAfternoonAppointment(date string) bool {
	t := Schedule(date)
	hour := t.Hour()
	return hour >= 12 && hour < 18
}

// Description returns a formatted string of the appointment time.
func Description(date string) string {
	t := Schedule(date)
	return "You have an appointment on " +
		t.Format("Monday, January 2, 2006, at 15:04.")
}

// AnniversaryDate returns a Time with this year's anniversary.
func AnniversaryDate() time.Time {
	now := time.Now()
	return time.Date(now.Year(), time.September, 15, 0, 0, 0, 0, time.UTC)
}