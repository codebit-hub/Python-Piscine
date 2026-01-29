#!/usr/bin/env python3
import sys

def main():
	if len(sys.argv) != 2:
		print("none")
		return

	param = sys.argv[1]
	result = ""

	for char in param:
		if char == 'z':
			result += char

	if result == "":
		print("none")
	else:
		print(result)

if __name__ == "__main__":
	main()
