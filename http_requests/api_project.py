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

jokes = data["total_jokes"]
if jokes > 1:
    print(f"I've got {jokes} jokes about {search_term}. Here's one:")
    print(choice(data["results"])["joke"])
elif jokes == 1:
    print(f"I've got one joke about {search_term}. Here it is:")
    print(data["results"][0]["joke"])
else:
    print(f"Sorry I don't have any jokes about {search_term}! Please try again")
