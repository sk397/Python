# Builiding the weather app using the Openweather API
# We need to request the api, so we will install the requests module
# pip install requests | this will install the request module

import math
import requests

API_KEY = "e41bc27e66aa599e45343456303dd459"

#Got from the API Docs
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

#Getting the city name input form the user
city = input("Enter a city name: ")

#After the ? we are passing the query parameter which is the api key
# and appending the ampersand & q = city 
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

#Get Request # Retriving data

#Getting the response from the request URL
response = requests.get(request_url)

# if we get the 200 ok response then we get the response
if response.status_code == 200:
    data = response.json()
    # print(data) - this gives the whole json array 
    weather = data['weather'][0]['description'] # selecting the weather key from the returned data
    print(weather)
    temprature = data['main']['temp'] - 273.15 # Temp in Kelvin to celcius
    rounded_temp = round(temprature, 2) # Round to 2 decimal places
    print(f"The Temprature is {rounded_temp} degree celsius")
else:
    print("An Error Occured")


