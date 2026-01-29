#!/usr/bin/env python3

def main():
	i = 0
	while i <= 10:
		print(f"Table of {i}:", end="")
		j = 0
		while j <= 10:
			result = i * j
			print(f" {result}", end="")
			j +=1
		print()
		i += 1

if __name__ == "__main__":
	main()
