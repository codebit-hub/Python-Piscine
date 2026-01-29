#!/usr/bin/env python3

def main():
	try:
		user_input1 = input("Give me the first number: ").strip()
		user_input2 = input("Give me the second number: ").strip()
		nbr1 = float(user_input1)
		nbr2 = float(user_input2)
		print("Thank you!")

		print(f"{nbr1:g} + {nbr2:g} = {nbr1 + nbr2:g}")
		print(f"{nbr1:g} - {nbr2:g} = {nbr1 - nbr2:g}")
		if nbr2 == 0:
			print(f"{nbr1:g} / {nbr2:g} = Error: Division by zero")
		else:
			print(f"{nbr1:g} / {nbr2:g} = {nbr1 / nbr2:g}")
		print(f"{nbr1:g} * {nbr2:g} = {nbr1 * nbr2:g}")

	except ValueError:
		print("Error: Enter an integer!")

if __name__ == "__main__":
	main()
