# TZ, 20.05.23 
import json
import requests

def weatherInformation(apiKey,location,units="metric",language="en"):
    baseUrl = "https://api.openweathermap.org/data/2.5/weather?q="
    info = requests.get(baseUrl + location + "&appid=" + apiKey + "&units=" + units + "&lang=" +language)
    weatherInf = info.json()
    return weatherInf
    

if __name__ == "__main__":
    
    apiKey = "a8215a9de00e4455d82b2a1e73057ae9"
    location = input("Enter [city] or [city,state]:")
    units = "metric"
    language = "en"
    
    weatherInfo = weatherInformation(apiKey,location,units,language)
    
    if weatherInfo["cod"] != "404":
        print("City: " + weatherInfo["name"])
        print("Temperature: " + str(weatherInfo["main"]["temp"]))
    else:
        print("404: City not Found") 
    