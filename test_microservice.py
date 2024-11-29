import requests
from pprint import pprint


url = 'http://127.0.0.1:5002/create_quarters'

payload = {
    "startSeason": 0,
    "startYear": 2022,
    "endSeason": 1,
    "endYear": 2024,
}

response = requests.post(url, json=payload)

pprint(response.json())