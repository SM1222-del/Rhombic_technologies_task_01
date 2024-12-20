import requests
from keys import key2
from weather import*


api_address="http://api.openweathermap.org/data/2.5/weather?q=Lahore&appid=".key2
json_data=requests.get(api_address).json()

def temp():
    temperature=round(json_data["main"]["temperature"]-275,1)
    return temperature

def detail():
    description=json_data["weather"][0]["description"]
    return description
