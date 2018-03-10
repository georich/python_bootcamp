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

if len(data["results"]) > 1:
    print(f"I've got {len(data['results'])} jokes about {search_term}. Here's one:")
    print(choice(data["results"])["joke"])
elif len(data["results"]) == 1:
    print(f"I've got one joke about {search_term}. Here it is:")
    print(data["results"][0]["joke"])
else:
    print(f"Sorry I don't have any jokes about {search_term}! Please try again")
