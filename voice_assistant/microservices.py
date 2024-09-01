import os, requests, json
from dotenv import load_dotenv

load_dotenv('bot.env')

def temperatura():

    api_key = os.getenv("OPENWEATHERMAP_KEY")

    # URL of OpenWeather
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
 
    # City
    city_name = "Palermo"
 
    # esta es la URL completa con la informacion concatenada para realizar la petición correcta
    # complete_url = os.path.join(base_url , "appid=" , api_key , "&q=" , city_name , "&units=metric"	)
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"	

    # Request
    response = requests.get(complete_url)
    info = response.json()["main"]
    output = "🌡 Temperatura: {} °C\n💨 Presión: {} hPa\n💧 Humedad: {} %". format(info["temp"], info["pressure"], info["humidity"])
    return output