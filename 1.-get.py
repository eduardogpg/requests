import requests

URL = 'http://httpbin.org/get'

response = requests.get(URL)

print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text)
print(response.cookies)

payload = response.json()

print(
    payload.get('args')    
)

print(
    requests.codes.ok
)