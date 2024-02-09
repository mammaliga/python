# def extract_full_name(lst):
# 	return 


names = [{'first': "Xaliq", 'last': "Kulebjakoff"}, {"first": "Nikita", "last": "Gondonoff"}]

niggas = list(map(lambda item: item["first"] + " " + item["last"], names))
print(niggas)

niggas = [item["first"] + " " + item["last"] for item in names]
print(niggas)

# print(extract_full_name(names)) # ['Elie Schoppik', 'Colt Steele']
