"""Test POST request to microservice C"""

import requests

# URL for the pdf microservice
url_1 = 'http://127.0.0.1:5002/get_business_news'
url_2 = 'http://127.0.0.1:5002/get_bbc_news'

# Request includes url
response1 = requests.post(url_1)
response2 = requests.post(url_2)


# Print contents of JSON response
print(response1.json())
print(response2.json())