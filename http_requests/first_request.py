import requests

url = "https://www.google.com"
response = requests.get(url)
print(response)
print(response.ok)
print(response.headers)
# print(res.text)
print(f"Your request to {url} came back w/ status code {response.status_code}")
