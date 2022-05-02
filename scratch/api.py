import requests, json

# response = requests.get("http://api.open-notify.org/astros.json")
# pretty = json.dumps(response.json(), indent=4)

response = requests.get("https://www.boredapi.com/api/activity")
print(response.text)
print(json.dumps(response.json(), indent=4))
_ = input("Press ENTER to exit the program.")
