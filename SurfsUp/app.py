# Import the dependencies.
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask import Flask, jsonify
import datetime as dt
import json as json
import numpy as np

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite", echo=False)

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

@app.route("/")
def welcome():
    return (
        f"Module 10 Challenge Climate App<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/YYYMMDD<start_date><br/>"
        f"/api/v1.0/YYYYMMDD<start_date>/YYYYMMDD<end_date><br/>"
    )


@app.route("/api/v1.0/precipitation/")
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
    
    return jsonify(prcp_dict)

    
@app.route("/api/v1.0/stations/")
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
    
    return jsonify(stations_list)

@app.route("/api/v1.0/tobs/")
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
    return jsonify(station_freq_list)

@app.route("/api/v1.0/<start_date>")
@app.route("/api/v1.0/<start_date>/<end_date>")

def start(start_date=None, end_date=None):

     #create session from Python to the DB
    session = Session(engine)
    #define start date
    start_date = dt.datetime.strptime(start_date, "%Y%m%d")
    end_date = dt.datetime.strptime(end_date, "%Y%m%d")
    
    if not end_date:
   
    #query if there's no end date
        results = session.query(func.min(measurement.tobs),\
            func.avg(measurement.tobs),\
            func.max(measurement.tobs)).\
            filter(measurement.date >= start_date).all()
        
        results_list = list(np.ravel(results))
        print(results_list)
   
    #close session
        session.close()
        
        return jsonify(results_list)

    results = session.query(func.min(measurement.tobs),\
        func.avg(measurement.tobs),\
        func.max(measurement.tobs)).\
        filter(measurement.date >= start_date).\
        filter(measurement.date <= end_date).all() 
   
    results_list = list(np.ravel(results))
    print(results_list)
   
    #close session
    session.close()
        
    return jsonify(results_list)

  
if __name__ == "__main__":
    app.run(debug=True)