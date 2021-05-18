import requests
import json

# Encode URLS in python:
import urllib.parse

# Write a sentence 
user_input = input("Write a sentence: ")

# Get the base 
base_url = "http://yoda-api.appspot.com/api/v1/yodish?text="
text = user_input

text = urllib.parse.quote(text)

url = base_url + text


# Get response from URL 
response = requests.get(url)

# Retrieve data
data = json.loads(response.content)


print('Yoda would say:', data['yodish'])

