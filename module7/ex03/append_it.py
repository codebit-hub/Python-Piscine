#!/usr/bin/env python3
import sys

def main():
	if len(sys.argv) > 1:
		params = sys.argv[1:]

		for param in params:
			suffix = "ism"
			if suffix in param:
				pos = param.find(suffix)
				if pos == len(param) - len(suffix):
					continue
			print(f"{param}{suffix}")
	else:
		print("none")

if __name__ == "__main__":
	main()
