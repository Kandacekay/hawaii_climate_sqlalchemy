# Hawaii Climate Analysis API

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
   <img src="https://github.com/Kandacekay/sqlalchemy-challenge/assets/130207643/092104f6-6d34-4030-a917-a266fc7ffaca" alt="precipitation_graph" width="500" align="center">

   - Plotted the results using Matplotlib.
   - Calculated and printed summary statistics for precipitation data:
   <img src="https://github.com/Kandacekay/sqlalchemy-challenge/assets/130207643/bf29062d-0748-42d6-843a-cce107a227bd" alt="summary_statistics" width="500" align="center">

## Exploratory Station Analysis
1. <b> Total Number of Stations </b>
   =Designed a query to calculate the total number of stations in the dataset.
2. <b> Most Active Stations </b>
   - Found the most active stations by listing them in descending order based on the number of rows.
3. <b> Temperature Analysis for Most Active Station </b>
   - Calculated the lowest, highest, and average temperature for the most active station.
   - Plotted a histogram for the last 12 months of temperature observations for this station:
   <img src="https://github.com/Kandacekay/sqlalchemy-challenge/assets/130207643/cd495af0-c5d7-422c-8982-6f78f5f8e1dc" alt="temperature_histogram" width="500" align="center">

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
