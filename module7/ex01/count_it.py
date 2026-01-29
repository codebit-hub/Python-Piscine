#!/usr/bin/env python3
import sys

def main():
	params = sys.argv[1:]

	if len(params) > 1:
		print(f"parameters: {len(params)}")
		for param in params:
			print(f"{param}: {len(param)}")
	else:
		print("none")

if __name__ == "__main__":
	main()
