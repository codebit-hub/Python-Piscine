#!/usr/bin/env python3

def find_redheads(family_dict):

	def is_redhead(name):
		color = family_dict[name]
		return color == "red"

	all_names = family_dict.keys()
	filtered = filter(is_redhead, all_names)
	return list(filtered)

if __name__ == "__main__":
	smith_family = {
		"florian": "red",
		"marie": "blond",
		"virginie": "brunette",
		"david": "red",
		"franck": "red"
	}
	print(find_redheads(smith_family))
#filter people with red hair in a list, just first names
