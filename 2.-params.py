import requests

URL = 'http://httpbin.org/get?name=eduardo_gpg&email=eduardo78d@gmail.com'

params = {
    'name': 'eduardo_gpg',
    'email': 'eduardo78d@gmail.com'
}

# response = requests.get(URL, params=params)

response = requests.get(URL)

if response.status_code == 200:
    payload = response.json()

    print(response.url)
    print(payload.get('args'))

"""
Query parameters are a defined set of parameters attached to the end of a url. 
They are extensions of the URL that are used to help define specific content or actions based on the data being passed.
To append query params to the end of a URL, 
a ‘?’ Is added followed immediately by a query parameter.
"""