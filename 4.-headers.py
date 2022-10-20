import json
import requests

URL = 'http://httpbin.org/get'

headers = {
    'name': 'Eduardo Ismael'
}

response = requests.get(URL, headers=headers)

if response.status_code == 200:
    payload = response.json()

    # payload = json.dumps(response.text, indent=4, sort_keys=True)

    print(response.history)
    # print(payload.get('headers'))
