# Earthquakes
fetches any earthquakes in Syria or Turkey from public data
### Data Acquisition
Takes earthquake data from 
[Earthquakes JSON](https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson) provided by the United States Geological Survey
#### Output
- finds any earthquakes in the country's of Syria or Turkey and outputs to `output.csv`
- follows schema `[time, place, mag, magType, latitude, longitude, depth]`

