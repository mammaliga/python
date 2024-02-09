import requests

url = "https://api.chucknorris.io/jokes/random"

res = requests.get(url, headers={"Accept": "application/json"})
data = res.json()
print(data.get("value"))

