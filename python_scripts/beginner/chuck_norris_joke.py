from pyfiglet import Figlet as figlet
from termcolor import colored
import requests
f = figlet(font="standard")
url = "https://api.chucknorris.io/jokes/random"
print(colored(f.renderText("Chuck Norris Joke"), "yellow"))

categorires = requests.get(
    "https://api.chucknorris.io/jokes/categories").json()
category = input("Choose a category of jokes: ")

while True:
    if category in categorires:
        data = requests.get(url, params={"category": category}).json()
        print(data.get("value"))
        break
    else:
        category = input("Sorry no jokes. Choose another category: ")
