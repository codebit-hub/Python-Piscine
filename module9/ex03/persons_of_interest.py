#!/usr/bin/env python3

def get_birth_year(item):
	return item[1]["date_of_birth"]

def famous_births(figures):
	dictionary_items = figures.items()
	sorted_list = sorted(dictionary_items, key=get_birth_year)

	for key, data in sorted_list:
		name = data["name"]
		year = data["date_of_birth"]
		print(f"{name} is a great scientist born in {year}.")

if __name__ == "__main__":
	women_scientists = {
		"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
		"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
		"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
		"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
	}
	famous_births(women_scientists)
