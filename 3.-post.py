import json
import requests

URL = 'http://httpbin.org/post'

data = {
    'name': 'eduardo_gpg',
    'email': 'eduardo78d@gmail.com'
}

response = requests.post(URL, data=data)

if response.status_code == 200:
    payload = response.json()

    # payload = json.dumps(response.text, indent=4, sort_keys=True)
    print(payload.get('form'))
