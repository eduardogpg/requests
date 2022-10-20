import json
import requests

URL = 'http://httpbin.org/cookies'

cookies = {
    'id': '1234',
    'name': 'eduardo',
}

response = requests.get(URL, cookies=cookies)

if response.status_code == 200:
    payload = response.json()

    print(response.headers)
    print(payload)