from geopy.geocoders import Nominatim
from datetime import datetime, timedelta
import math



def format_coordinates(longitude, latitude):
    # Check if the longitude is east or west
    long_direction = "e" if longitude >= 0 else "w"
    # Check if the latitude is north or south
    lat_direction = "n" if latitude >= 0 else "s"
    
    # Convert the longitude and latitude to positive values for formatting
    longitude = abs(longitude)
    latitude = abs(latitude)
    
    # Format the longitude and latitude as strings with the specified format
    long_str = f"{int(longitude)}{long_direction}{int((longitude - int(longitude)) * 60):02}"
    lat_str = f"{int(latitude)}{lat_direction}{int((latitude - int(latitude)) * 60):02}"
    
    return lat_str, long_str




def getLocation():
    # Input current date
    address=input("Enter City: ")
    geolocator = Nominatim(user_agent="MyApp")
    loc = geolocator.geocode(address)
    long = loc.longitude
    lat = loc.latitude
    #print((loc.latitude, loc.longitude))
    formatted_latitude, formatted_longitude = format_coordinates(long, lat)
    return str(formatted_latitude), str(formatted_longitude)