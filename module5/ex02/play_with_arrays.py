#!/usr/bin/env python3

def main():
	array1 = [2, 8, 9, 48, 8, 22, -12, 2]
	print(array1)

	array2 = [x + 2 for x in array1 if x > 5]
	print(array2)

if __name__ == "__main__":
	main()
