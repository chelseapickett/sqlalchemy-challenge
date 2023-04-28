# Import the dependencies.
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect
from flask import Flask, jsonify
import datetime as dt
import json as json

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///./Resources/hawaii.sqlite", echo=False)

# reflect an existing database into a new model
Base = automap_base()
Base.prepare(autoload_with=engine)
Base.classes.keys()

# reflect the tables, save references to each table 
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB

#session = Session(engine) 
#################################################
# Flask Setup
#################################################

app = Flask(__name__)
#################################################
# Flask Routes
#################################################


@app.route("/precipitation/")
def precip():
    #create session from Python to the DB
    session = Session(engine)
    #Query
    year_ago = dt.date(2017, 8 ,23) - dt.timedelta(days=365)
   
    prcp = session.query(measurement.date, measurement.prcp).\
    filter(measurement.date>=year_ago).all()
   

    prcp_dict = {}
    for (date, prcp) in prcp:
        prcp_dict[date] = prcp
    
    
    #close session
    session.close()
    
    print("Server received request for 'precipitation' page...")
    return jsonify(prcp_dict)

    
@app.route("/stations/")
def stats():

     #create session from Python to the DB
    session = Session(engine)
    #Return a JSON list of stations from the dataset
    list_stations = session.query(measurement.station).\
        group_by(measurement.station).all()
    
    stations_list = []
    for stations in list_stations:
        stations_list.append(stations[0])
    #close session
    session.close()
    
    print("Server received request for 'stations' page...")
    return jsonify(stations_list)

@app.route("/tobs/")
def tobs():

     #create session from Python to the DB
    session = Session(engine)
    #return 
    first_date = dt.date(2016, 8, 23)

    station_freq = session.query(measurement.tobs).\
    filter(measurement.date>= first_date).filter(measurement.station == "USC00519281").all()
   
    station_freq_list = []
    for freq in station_freq:
        station_freq_list.append(freq[0])
    
    #close session
    session.close()
    print("Server received request for 'tobs' page...")
    return jsonify(station_freq_list)

# @app.route("/jsonified")
# def jsonified():
#     return 

    
if __name__ == "__main__":
    app.run(debug=True)