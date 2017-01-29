# hale-hearty-map

## Part 1

Use [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) to scrape
the [Manhattan locations of Hale & Hearty](https://www.haleandheartytogo.com/)
into a CSV file whose columns should be at least:

 - canonical name (e.g. '88th & 3rd')
 - address (e.g. '1562 3rd Avenue')
 - phone number (e.g. '(212) 831-3684')
 - Saturday/Sunday hours (e.g. '11am - 9pm')
 - Weekday hours (e.g. '10am - 10pm')

## Part 2

Put these locations on a map. You could use [CartoDB](http://cartodb.com/) or
Google Maps.

## Bonus points

Write a function that takes as input my location and the time, and tells me
where the nearest _open_ Hale & Hearty location is.
