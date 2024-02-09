import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet = {row.letter: row.code for (index, row) in data.iterrows()}

while True:
    user_word = input("Enter a word: ")
    if user_word == "q":
        break
    try:
        nato_words = [alphabet[char] for char in user_word.upper()]
    except KeyError:
        print("Input must be only with letters")
    else:
        print(nato_words)
