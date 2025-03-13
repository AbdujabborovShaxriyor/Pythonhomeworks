import requests

base_url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": "Tashkent",          
    "appid": "42bf160486e72c23065e7c120947f07c",   
    "units": "metric"
}
response = requests.get(base_url,params=params)
weather_data = response.json()
city = weather_data.get("name",{})
humidity = weather_data.get("main",{}).get("humidity","N/A")
wind = weather_data.get("main",{}).get("wind","N/A")
pressure = weather_data.get("main",{}).get("pressure","N/A")
weather_list = [city,humidity,pressure,wind]
for item in weather_list:
    print(item)