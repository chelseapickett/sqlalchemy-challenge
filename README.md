# sqlalchemy-challenge
 In this challenge a climate analysis is completed on Honolulu, Hawaii at a specific time range to analyze temperature information for the the area.  

# Precipitation Analysis
  In this section queries were created to find the most recent date in the data set and collect only the date and precipitation data for the last year of data. The results were saved to a Pandas dataframe where date and preciptation columns were created. After the dataframe was sorted by date the resulted were plotted and the summary statistics for the precipitation data was calculated. [analysis notebook](https://github.com/chelseapickett/sqlalchemy-challenge/blob/main/SurfsUp/climate_starter.ipynb)

# Station Analysis
  In this section queries were created that counted the number of stations in the dataset, sorted in descending order and found the most active station as well as found the minimum, maximum and average temperatures for the most active station. The previous twelve months of data was found and filtered by the most active station. This data was saved to a dataframe and plotted with a histogram with the temperature observations ('tobs') as the column count. [analysis notebook](https://github.com/chelseapickett/sqlalchemy-challenge/blob/main/SurfsUp/climate_starter.ipynb)

# API SQLite Connection & Landing Page
  The flask application successfully generates the connection between the python app and the database and displays the available routes on the landing page. [climate app](https://github.com/chelseapickett/sqlalchemy-challenge/blob/main/SurfsUp/app.py)

# API Static Routes
This flask application includes the following routes:
- precipitation route
- stations route
- tobs route

# API Dynamic Route
The flask application also includes the following dynamic routes:
 - start route
 - start/end route
