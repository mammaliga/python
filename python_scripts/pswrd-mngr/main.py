from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_pswrd():
    letters_list = [choice(letters) for char in range(randint(8, 10))]
    symbol_list = [choice(symbols) for char in range(randint(2, 4))]
    number_list = [choice(numbers) for char in range(randint(2, 4))]

    pswrd_list = [*letters_list, *symbol_list, *number_list]
    shuffle(pswrd_list)
    password = "".join(pswrd_list)
    pswrd_entry.delete(0, END)
    pswrd_entry.insert(0, password)
    return password


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = site_entry.get()
    username = username_entry.get()
    password = pswrd_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    if not len(website) > 0 or not len(password) > 0:
        messagebox.showinfo(
            title="Oops",
            message="None of the fields must not be empty")

    else:
        isok = messagebox.askokcancel(
            title=website,
            message=f"this are the details entered: {website}\n{username}\n{password}")
        if isok:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                pswrd_entry.delete(0, END)
                site_entry.delete(0, END)


def find_password():
    web_entry = site_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
            website = data[web_entry]
            username = website["username"]
            password = website["password"]
    except KeyError:
        messagebox.showerror(title=web_entry,
                             message=f"No details for the website exists")
    except FileNotFoundError:
        messagebox.showerror(title=web_entry, message=f"No Data File Found")
    else:
        messagebox.showinfo(
            title=web_entry,
            message=f"Email/Username: {username}\nPassword: {password}")


# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Password Manager")
root.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(135, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website input
site_label = Label(text="Website:")
site_label.grid(column=0, row=1)
site_entry = Entry(width=44)
site_entry.grid(column=1, row=1)
site_entry.focus()

search_btn = Button(text="Search", width=15, command=find_password)
search_btn.grid(column=2, row=1)

# Email/Username input
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
username_entry = Entry(width=63)
username_entry.grid(column=1, row=2, columnspan=2, pady=10)
username_entry.insert(0, "example@mail.com")

# Password input
pswrd_label = Label(text="Password:")
pswrd_label.grid(column=0, row=3)
pswrd_entry = Entry(width=44)
pswrd_entry.grid(column=1, row=3)

# Generate password
gen_pwrd_btn = Button(text="Generate Password", command=generate_pswrd)
gen_pwrd_btn.grid(column=2, row=3)

# Submit button
submit_btn = Button(text="Add", width=42, command=save_data)
submit_btn.grid(column=1, row=4, columnspan=2, pady=20)


root.mainloop()
