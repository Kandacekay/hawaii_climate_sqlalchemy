# Hawaii Climate Analysis API

## Overview
This project involves the analysis of climate data from Hawaii, focusing on precipitation, station activity, and temperature observations. The data is sourced from a SQLite database, and the analysis includes exploratory data analysis, visualizations, and the creation of a Flask API to provide climate information through various endpoints.

## Languages and Packages Used
- <b> Python: </b> The primary programming language used for data analysis and API development.
- <b>SQLAlchemy:</b> Used to interact with the SQLite database and reflect tables into SQLAlchemy ORM.
- <b> Pandas: </b> Utilized for data manipulation, analysis, and the creation of data structures.
Matplotlib: Employed for data visualization, including plotting precipitation and temperature histograms.
Flask: Used to create a web API to serve climate information.
Exploratory Precipitation Analysis
1. Most Recent Date
Found the most recent date in the dataset.
2. Precipitation Analysis
Retrieved the last 12 months of precipitation data.
Plotted the results using Matplotlib.
Calculated and printed summary statistics for precipitation data.
Exploratory Station Analysis
1. Total Number of Stations
Designed a query to calculate the total number of stations in the dataset.
2. Most Active Stations
Found the most active stations by listing them in descending order based on the number of rows.
3. Temperature Analysis for Most Active Station
Calculated the lowest, highest, and average temperature for the most active station.
Plotted a histogram for the last 12 months of temperature observations for this station.
Flask API Endpoints
1. /api/v1.0/precipitation
Returns a JSON representation of precipitation data for the last 12 months.
2. /api/v1.0/stations
Returns a JSON list of stations.
3. /api/v1.0/tobs
Returns a JSON list of temperature observations for the most active station in the last 12 months.
4. /api/v1.0/<start>
Returns a JSON representation of temperature statistics for a given start date.
5. /api/v1.0/<start>/<end>
Returns a JSON representation of temperature statistics for a date range.
How to Run
Ensure you have Python, Flask, SQLAlchemy, and the required dependencies installed.
Run the provided Python script to start the Flask app.
Access the API endpoints as described above.
Note: The SQLite database file (hawaii.sqlite) is required for the code to function correctly. Make sure it is available in the specified path.
