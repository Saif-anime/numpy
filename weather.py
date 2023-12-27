import requests

api_key = "YOUR_API_KEY"
city = input("Enter city name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
response = requests.get(url)
data = response.json()

if data["cod"] == 200:
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]
    print(f"Weather in {city}: {description}, Temperature: {temperature}°C")
else:
    print("City not found.")
