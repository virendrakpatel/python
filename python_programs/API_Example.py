import requests
import json

req = requests.get('https://httpbin.org/get')

# print(req)

# print(req.cookies)
# print(req.headers)
# print(req.status_code)
print(type(req.text))

print(req.text)
print(type(req))
json_str = json.loads(req.text)

# print(json_str.title())
# print(json_str.capitalize())
# print(json_str.upper())
print(type(json_str))
print(json_str)

print(json_str['headers'])

