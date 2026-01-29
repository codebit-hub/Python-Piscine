#!/usr/bin/env python3
import sys

def shrink(str):
	print(str[:8])

def enlarge(str):
	while len(str) < 8:
		str += 'Z'
	print(str)

def main():
	params = sys.argv[1:]
	if not params:
		print("none")

	for param in params:
		length = len(param)
		if length > 8:
			shrink(param)
		elif length < 8:
			enlarge(param)
		else:
			print(param)

if __name__ == "__main__":
	main()
