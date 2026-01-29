#!/usr/bin/env python3

def add_one(n):
	n = n + 1
	return n

if __name__ == "__main__":
	my_var = 42
	print(f"Before: {my_var}")

	add_one(my_var)
	#my_var = add_one(my_var)
	print(f"After: {my_var}")
