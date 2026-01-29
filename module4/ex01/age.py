#!/usr/bin/env python3

def main():
	try:
		user_input = input("Please tell me your age: ").strip()
		age = int(user_input)

		print(f"You are currently {age} years old.")
		i = 10
		while i <= 30:
			print(f"In {i} years, you'll be {age + i} years old.")
			i += 10

	except ValueError:
		print("Error: enter an integer!")

if __name__ == "__main__":
	main()
