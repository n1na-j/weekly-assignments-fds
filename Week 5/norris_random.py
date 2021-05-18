import requests
import json

url = "https://api.chucknorris.io/jokes/random"

# Get response from URL 
response = requests.get(url)

# Retrieve data
data = json.loads(response.content)


#print random chuck norris joke
print(data["value"])