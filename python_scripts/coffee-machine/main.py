# from turtle import Turtle, Screen
# mamaliga = Turtle()
# mamaliga.shape("turtle")
# mamaliga.color("slateblue3", "red")
# mamaliga.forward(100)
# mamaliga.left(120)
# mamaliga.forward(100)
# mamaliga.left(120)
# mamaliga.forward(100)


# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.align = "l"
table.field_names = ["Pokemon name", "type"]
table.add_row(["Kakuna", "Bug"])
table.add_row(["Pikachu", "Electric"])
table.add_row(["Panpour", "Water"])

print(table)