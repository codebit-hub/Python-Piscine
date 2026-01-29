#!/usr/bin/env python3

def main():
	print("Enter a number")

	try:
		user_input = input()
		num = int(user_input)

		i = 0
		while i < 10:
			result = i * num
			print(f"{i} x {num} = {result}")
			i += 1
			
	except ValueError:
		print("Error: Please enter a valid integer")

if __name__ == "__main__":
	main()
