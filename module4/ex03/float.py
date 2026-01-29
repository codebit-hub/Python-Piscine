#!/usr/bin/env python3

def main():
	try:
		user_input = input("Give me a number: ").strip()
		num = float(user_input)

		if num.is_integer():
			print("This number is an integer.")
		else:
			print("This number is a decimal.")

	except ValueError:
		print("Error: That's not a valid number.")

if __name__ == "__main__":
	main()
