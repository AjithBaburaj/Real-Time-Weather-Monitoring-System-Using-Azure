import requests 
import json     


# Getting secret value from Key Vault
weatherapikey = dbutils.secrets.get(scope="key-vault-scope", key="weatherapikey")
location = "Chennai"  # You can replace with city name based on your preference

base_url = "http://api.weatherapi.com/v1/"

current_weather_url = f"{base_url}/current.json" #for fetching current weather info


params = {
    'key': weatherapikey,
    'q': location,
}

response = requests.get(current_weather_url, params=params)

if response.status_code == 200:      #api call success checking
    current_weather = response.json()
    print("Current Weather:")
    print(json.dumps(current_weather, indent=3))
else:
    print(f"Error: {response.status_code}, {response.text}")


"""
request library :for sending request to API
json : format of the data that we recieve from API

"""