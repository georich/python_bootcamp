import requests

url = "https://icanhazdadjoke.com/"
# response = requests.get(url, headers={"Accept": "text/plain"})
response = requests.get(url, headers={"Accept": "application/json"})
print(response.text) # type = str
print(response.json())

data = response.json()
print(data["joke"])
