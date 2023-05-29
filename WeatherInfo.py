# TZ, 20.05.23 
import json
import requests

def weatherInformation(apiKey,location,units="metric",language="en"):
    baseUrl = "https://api.openweathermap.org/data/2.5/weather?q="
    info = requests.get(baseUrl + location + "&appid=" + apiKey + "&units=" + units + "&lang=" +language)
    weatherInf = info.json()
    return weatherInf
    

if __name__ == "__main__":
    flag=1
    #apiKey = "a8215a9de00e4455d82b2a1e73057ae9" #might not be updated, get your own! 
    while flag == 1:  
        apiKey = input("Enter API key from openweathermap.org:")
        location = input("Enter [city] or [city,state]:")
        units = input("Choose units ([C] for Celsius, [F] for Fahrenheit, or [K] for Kelvin:")
        language = "en"
        
        if units.upper() == "C":
            unt = "metric"
        elif units.upper() == "F":
            unt = "imperial"
        else:
            unt = "standard"
            
        try:
            weatherInfo = weatherInformation(apiKey,location,unt,language)
            if weatherInfo["cod"] == "404":
                print("404: City not Found")
            else:
                print("City: " + weatherInfo["name"]+ ", " + weatherInfo["sys"]["country"])
                print("Temperature: " + str(weatherInfo["main"]["temp"]) + units)
                print("Feels like: " + str(weatherInfo["main"]["feels_like"]) + units)
                print("Himidity of: " + str(weatherInfo["main"]["humidity"]) + "%")
                print((weatherInfo["weather"][0]['description']))
        except:
            print("Something went wrong. Check your API key or try again later.")
            break
        
        try:
            okSignal = input("To leave, press x. To try again, press y\n")
            if okSignal.upper() != "Y":
                flag = 0
        except:
                flag = 0

    
 
    