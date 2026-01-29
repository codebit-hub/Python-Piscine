#! /usr/bin/env python3

user_data = input()

try:
	nbr = int(user_data)
	if nbr < 0:
		print("This number is negative.")
	elif nbr > 0:
		print("This number is positive.")
	else:
		print("This number is both positive and negative.")
except ValueError:
	print("It is not a number.")
