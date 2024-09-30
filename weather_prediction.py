# Install the meteostat library in Google Colab
# !pip install meteostat

# Import necessary libraries
from meteostat import Point, Daily
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Define the location (for example, Mumbai)
location = Point(19.0760, 72.8777)  # Latitude and longitude for Mumbai

# Define the start and end date (from 2018 to 2023)
start = datetime(2018, 1, 1)
end = datetime(2023, 12, 31)

# Fetch the daily weather data for the location
data = Daily(location, start, end)
data = data.fetch()

# Display all the rows and columns (all parameters)
# If data is large, it may truncate the output, so we remove restrictions for display
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Show the entire dataset
print(data)

# Optionally save the data to a CSV file for download
data.to_csv('mumbai_weather_2018_2023.csv')

# Download the CSV file (for Google Colab)
from google.colab import files
files.download('mumbai_weather_2018_2023.csv')
