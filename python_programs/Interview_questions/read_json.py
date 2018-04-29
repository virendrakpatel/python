import json

data = json.load(open("data.json"))

print (data)
print(type(data))

print(type(data["sf"]["order"]))

