import requests

API_KEY = "key"

url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={API_KEY}"

response = requests.get(url)
response.raise_for_status()

data = response.json()

lat = data["location"]["lat"]
lng = data["location"]["lng"]
accuracy = data["accuracy"]

print("Latitude:", lat)
print("Longitude:", lng)
print("Accuracy (meters):", accuracy)
