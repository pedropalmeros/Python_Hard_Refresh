import requests

def getAPI():
    with open('./apiKey.txt','r') as apiFile:
        Api = apiFile.readline().rstrip()
    return Api



def get_weather_data():
    OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

    weather_params = {
        "lat": 20.588793,
        "lon": -100.389885,
        "appid":getAPI(),
        "cnt": 4
    }
    response = requests.get(OWM_Endpoint, params=weather_params)


    return response.json()