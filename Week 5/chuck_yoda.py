import requests
import json
import urllib.parse

# Chuck norris joke
url_random_joke = "https://api.chucknorris.io/jokes/random?category=science"

# Get response from URL 
response = requests.get(url_random_joke)

# Retrieve data
data = json.loads(response.content)


# Print random Chuck Norris joke
print("This is the original Chuck Norris joke:", data["value"])

# Talk Yodish
base_url = "http://yoda-api.appspot.com/api/v1/yodish?text="
text = data["value"]
text = text.replace("Chuck Norris", "I am")
text = urllib.parse.quote(text)
url = base_url + text

response = requests.get(url)

# Retrieve data
data = json.loads(response.content)

# Print the random Chuck Norris joke in Yodish
print('But Yoda says the joke like this:', data['yodish'])

