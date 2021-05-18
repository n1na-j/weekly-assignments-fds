import requests
import json

query = ['thunder', 'sunny']
url = "https://api.chucknorris.io/jokes/search?" 


data_list = []

#Create a query to search specific jokes
for item in query: 
    parameters = {
        "query": item
    }

# Get response from URL 
response = requests.get(url, params=parameters)

# Retrieve data
data = json.loads(response.content)
data_list.append(data)

# Show only jokes with thunder and sunny
print(data_list)

