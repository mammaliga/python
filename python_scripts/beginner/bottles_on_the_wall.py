def make_song(i=99, beverage="soda"):
    bottles = "bottles"
    while i >= 0:
        if i != 0:
        	yield f"{i} {bottles} of {beverage} on the wall"
        else:
        	yield "No more bottles"
        i -= 1
        if i == 1:
            bottles = "bottle"


kombucha_song = make_song(5, "kombucha")
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))


default_song = make_song()
