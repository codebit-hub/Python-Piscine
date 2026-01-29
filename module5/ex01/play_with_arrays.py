#!/usr/bin/env python3

def main():
	array1 = [2, 8, 9, 48, 8, 22, -12, 2]
	print(f"Original array: {array1}")

	array2 = [var + 2 for var in array1]
	print(f"New array: {array2}")

if __name__ == "__main__":
	main()
