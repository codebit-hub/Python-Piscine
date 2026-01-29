#!/usr/bin/env python3
import sys

def downcase_it(param):
	return param.lower()

def main():
	params = sys.argv[1:]
	if params:
		for param in params:
			print(downcase_it(param))
	else:
		print("none")

if __name__ == "__main__":
	main()
