# Import the dependencies.
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Create a Flask app
app = Flask(__name__)

#################################################
# Database Setup
#################################################

# Create an engine and reflect the database tables
engine = create_engine(("sqlite:///Resources\\hawaii.sqlite"))

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

# Define routes
@app.route("/")
def home():
    return (
        "Welcome to the Hawaii Climate API!<br/>"
        "Avaliable Routes:<br/>"
        "/api/v1.0/precipitation<br/>"
        "/api/v1.0/stations<br/>"
        "/api/v1.0/tobs<br/>"
        "/api/v1.0/&lt;start&gt;<br/>"
        "/api/v1.0/&lt;start&gt;/&lt;end&gt;"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
# Calculate the date one year from the last date in the dataset
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first().date
    last_year = dt.datetime.strptime(last_date, '%Y-%m-%d') - dt.timedelta(days=366)

# Retrieve the last 12 months of precipitation data
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= last_year).all()
    session.close()

# Convert the query results to a dictionary
    precipitation_dict = {date: prcp for date, prcp in results}
    return jsonify(precipitation_dict)

@app.route("/api/v1.0/stations")
def Stations():
    session = Session(engine)

# Retrieve the list of stations
    results = session.query(Station.station, Station.name).all()
    session.close()

# Convert the query results to a list of dictionaries
    station_list = [{"station": station, "name": name} for station, name in results]
    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

# Find the most active station
    most_active_station = session.query(Measurement.station).\
        group_by(Measurement.station).\
        order_by(func.count().desc()).first().station

# Calculate the date one year from the last date in the dataset
    most_recent_date = session.query(Measurement.date).filter(Measurement.station == most_active_station).\
        order_by(Measurement.date.desc()).first().date
    last_year_date = dt.datetime.strptime(most_recent_date, '%Y-%m-%d') - dt.timedelta(days=365)

# Retrieve the temperature observations for the most active station for the last year
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= last_year_date).\
        filter(Measurement.station == most_active_station).all()

    session.close()

# Convert the query results to a list of dictionaries
    tobs_list = [{"date": date, "temperature": tobs} for date, tobs in results]

    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
def temp_by_start(start):
    try:
# Convert the input start date to a datetime.date object
        start_date = dt.datetime.strptime(start, "%Y-%m-%d").date()

 # Query for minimum, average, and maximum temperatures for dates greater than or equal to start_date
        results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
            filter(Measurement.date >= start_date).\
            all()
        
        if results:
            tmin, tavg, tmax = results[0]
            
 # Return the temperature statistics along with start_date and None for end_date
            return jsonify({
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": None,
                "tavg": tavg,
                "tmax": tmax,
                "tmin": tmin
            })
        else:
            return jsonify({"error": "No data found for the given start date."})
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/api/v1.0/<start>/<end>")
def temp_by_start_end(start, end):
    try:
# Convert the input start and end dates to datetime.date objects
        start_date = dt.datetime.strptime(start, "%Y-%m-%d").date()
        end_date = dt.datetime.strptime(end, "%Y-%m-%d").date()
        
# Query for minimum, average, and maximum temperatures for dates within the specified range
        results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
            filter(Measurement.date >= start_date).\
            filter(Measurement.date <= end_date).\
            all()
        
        if results:
            tmin, tavg, tmax = results[0]
# Return the temperature statistics along with start_date and end_date
            return jsonify({
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "tavg": tavg,
                "tmax": tmax,
                "tmin": tmin
            })
        else:
            return jsonify({"error": "No data found for the given date range."})
    except Exception as e:
        return jsonify({"error": str(e)})

#################################################
# Flask Routes
#################################################
if __name__ == "__main__":
# Run the Flask app in debug mode
    app.run(debug=True)
