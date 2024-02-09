import tkinter

window = tkinter.Tk()
window.title("Mile to Km calculator")
window.minsize(width=240, height=50)
window.config(padx=50, pady=50)


def calculate(num):
    return float(num) * 1.609


miles_input = tkinter.Entry(width=10)
miles_input.grid(column=1, row=0, pady=20)

miles_label = tkinter.Label(text="Miles", pady=20, font=40)
miles_label.grid(column=2, row=0)

is_equal_label = tkinter.Label(text="is equal", font=40)
is_equal_label.grid(column=0, row=1)

result_label = tkinter.Label(text=0, font=40)
result_label.grid(column=1, row=1)

km_label = tkinter.Label(text="km", font=40)
km_label.grid(column=2, row=1)

calc_btn = tkinter.Button(text="Calculate", command=lambda: result_label.config(text=calculate(miles_input.get())))
calc_btn.grid(column=1, row=2)









# window = tkinter.Tk()
# window.title("Mile to Km calculator")
# window.minsize(width=320, height=130)
# window.config(padx=20, pady=20)

# # Label

# my_label = tkinter.Label(text="Miles")
# my_label.grid(column=3, row=0)

# # Button

# button1 = tkinter.Button(
#     text="Calculate")
# button1.grid(column=1, row=2)


# # Entry

# input = tkinter.Entry(width=10)
# input.grid(column=2, row=0)
# input.get()













window.mainloop()
