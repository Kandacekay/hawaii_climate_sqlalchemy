[summary_statistics.csv](https://github.com/Kandacekay/sqlalchemy-challenge/files/13745445/summary_statistics.csv)# Hawaii Climate Analysis API

## Overview
This project involves the analysis of climate data from Hawaii, focusing on precipitation, station activity, and temperature observations. The data is sourced from a SQLite database, and the analysis includes exploratory data analysis, visualizations, and the creation of a Flask API to provide climate information through various endpoints.

## Languages and Packages Used
- <b> Python: </b> The primary programming language used for data analysis and API development.
- <b>SQLAlchemy:</b> Used to interact with the SQLite database and reflect tables into SQLAlchemy ORM.
- <b> Pandas: </b> Utilized for data manipulation, analysis, and the creation of data structures.
- <b> Matplotlib: </b> Employed for data visualization, including plotting precipitation and temperature histograms.
= <b> Flask: </b> Used to create a web API to serve climate information.

## Exploratory Precipitation Analysis
1. <b> Most Recent Date </b>
   - Found the most recent date in the dataset.
2. <b> Precipitation Analysis </b>
   - Retrieved the last 12 months of precipitation data:
![precipitation_graph](https://github.com/Kandacekay/sqlalchemy-challenge/assets/130207643/3e1eb534-1bce-4a9e-9d82-969d690563e8)
   - Plotted the results using Matplotlib.
   - Calculated and printed summary statistics for precipitation data:
   - [Uploading summaryPrecipitation
365.0
0.16998727984344422
0.29572180763925376
0.0
0.008571428571428572
0.06999999999999999
0.19166666666666665
2.3800000000000003
_statistics.csv…]()


## Exploratory Station Analysis
1. <b> Total Number of Stations </b>
   =Designed a query to calculate the total number of stations in the dataset.
2. <b> Most Active Stations </b>
   - Found the most active stations by listing them in descending order based on the number of rows.
3. <b> Temperature Analysis for Most Active Station </b>
   - Calculated the lowest, highest, and average temperature for the most active station.
   - Plotted a histogram for the last 12 months of temperature observations for this station.
![temperature_histogram](https://github.com/Kandacekay/sqlalchemy-challenge/assets/130207643/345d75ce-f54a-420f-ad70-68a5aa632671)


## Flask API Endpoints
1. <b> /api/v1.0/precipitation </b>
  - Returns a JSON representation of precipitation data for the last 12 months.
2. <b> /api/v1.0/stations </b>
  - Returns a JSON list of stations.
3. <b> /api/v1.0/tobs </b>
  - Returns a JSON list of temperature observations for the most active station in the last 12 months.
4. <b> /api/v1.0/<start> </b>
  - Returns a JSON representation of temperature statistics for a given start date.
5. <b> /api/v1.0/<start>/<end> </b>
 - Returns a JSON representation of temperature statistics for a date range.

## How to Run
- Ensure you have Python, Flask, SQLAlchemy, and the required dependencies installed.
- Run the provided Python script to start the Flask app.
- Access the API endpoints as described above.
<b> Note: </b> The SQLite database file (hawaii.sqlite) is required for the code to function correctly. Make sure it is available in the specified path.
