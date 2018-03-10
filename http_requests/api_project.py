import requests
from random import choice

url = "https://icanhazdadjoke.com/search"
search_term = input("Let me tell you a joke! Give me a topic: ")

response = requests.get(
    url, 
    headers={"Accept": "application/json"},
    params={"term": f"{search_term}"}
)

data = response.json()
# print(len(data["results"]))
if len(data["results"]) > 1:
    print(f"I've got {len(data['results'])} jokes about {search_term}. Here's one:")
elif len(data["results"]) == 1:
    print(f"I've got one joke about {search_term}. Here it is:")
else:
    print(f"Sorry I don't have any jokes about {search_term}! Please try again")
print(choice(data["results"])["joke"])

# print(data["results"])
