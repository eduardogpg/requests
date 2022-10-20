import requests

URL = 'https://i.imgur.com/kpP7xp6.jpeg'
response = requests.get(URL, stream=True)

if response.status_code == 200:
    with open('images/dog.jpg', 'wb') as f:
        for chunk in response:
            f.write(chunk)