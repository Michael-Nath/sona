# import requests library 
import requests
# we will be using https://random-data-api.com as the sample api
API_URI = "https://random-data-api.com/api/"

# making a get request
response = requests.get(f"{API_URI}/name/random_name")
print(response.json())

# exercise
# using this api, write code below that retreives information about n users (where n ~ 100,000) and prints out the top 5 states in the US that they hail from.
# Note: if for some reason, an user is not from the US, then suppose their "state" is simply the string "Intl". This should also be included in the top 5 ranking if frequent.
