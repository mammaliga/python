from tkinter import *
from csv import reader, writer
from random import choice
my_timer = None
FR = 0
ENG = 1
BACKGROUND_COLOR = "#B1DDC6"

try:
    with open("words_to_learn.csv") as data:
        words = reader(data)
        word_list = [[word[0], word[1]] for word in words]
except FileNotFoundError:
    with open("./data/french_words.csv") as data:
        words = reader(data)
        word_list = [[word[0], word[1]] for word in words]


def flip_card(pair):
    word = pair[1]
    canvas.itemconfig(card_word, text=word)
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(canvas_text, text="English", fill='white')
    canvas.itemconfig(card_word, fill="white")


def next_card():
    random_pair = choice(word_list)
    word = random_pair[0]
    canvas.itemconfig(card_word, text=word)
    canvas.itemconfig(card_word, text=word)
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(canvas_text, text="French", fill='black')
    canvas.itemconfig(card_word, fill="black")
    root.after(3000, flip_card, random_pair)
    print(random_pair)
    return random_pair


def update_data(pair):
    words = pair()
    word_list.remove(words)
    with open("words_to_learn.csv", "w") as data:
        csv_writer = writer(data)
        for word in word_list:
            csv_writer.writerow(word)


root = Tk()
root.title("Flashy")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Images
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
right_btn_img = PhotoImage(file="./images/right.png")
wrong_btn_img = PhotoImage(file="./images/wrong.png")


canvas = Canvas(
    width=800,
    height=526,
    highlightthickness=0,
    bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=card_front_img)
canvas_text = canvas.create_text(
    400, 150, text="French", font=(
        "Ariel", 40, "italic"))
card_word = canvas.create_text(
    400, 263, text="", font=(
        "Ariel", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)
# Buttons
right_btn = Button(
    image=right_btn_img,
    highlightthickness=0,
    border=0,
    command=lambda: update_data(next_card))
wrong_btn = Button(
    image=wrong_btn_img,
    highlightthickness=0,
    border=0,
    command=next_card)
right_btn.grid(column=1, row=1)
wrong_btn.grid(column=0, row=1)

next_card()
root.mainloop()
