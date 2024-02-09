from pyfiglet import Figlet as figlet
from termcolor import colored


colors = ("black", "red", "green", "yellow", "blue", "magenta", "cyan", "white",
          "light_grey", "dark_grey", "light_red", "light_green", "light_yellow", "light_blue")

f = figlet(font="standard")
output = input("What do you want to print? ")
color = input("Choose a color of the text: ")

while True:
	if (color in colors):
		text = colored(f.renderText(output), color)
		print(text)
		break;
	else:
		color = input("please, choose another color: ")
