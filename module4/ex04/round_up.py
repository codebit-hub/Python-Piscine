#!/usr/bin/env python3
import math

def main():
	try:
		user_input = input("Give me a number: ").strip()
		num = float(user_input)

		result = math.ceil(num)
		print(result)

	except ValueError:
		print("Error: Enter a valid number.")

if __name__ == "__main__":
	main()
