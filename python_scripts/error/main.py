fruits = ["apple", "pear", "orange"]


def make_pie(idx):
    try:
        fruit = fruits[idx]
        print(fruit + " pie")
    except IndexError:
        print(f"There is no such a fruit under {idx} index")


make_pie(4)
