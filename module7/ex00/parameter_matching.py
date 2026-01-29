#!/usr/bin/env python3
import sys

def main():
	if len(sys.argv) == 2:
		user_input = input("What was the parameter? ")
		if user_input == sys.argv[1]:
			print("Good job!")
		else:
			print("Nope, sorry...")
	else:
		print("none")


if __name__ == "__main__":
	main()
