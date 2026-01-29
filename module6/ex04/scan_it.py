#!/usr/bin/env python3
import sys
import re

def main():
	if len(sys.argv) != 3:
		print("none")

	key = sys.argv[1]
	search_string = sys.argv[2]

	matches = re.findall(re.escape(key), search_string)

	if not matches:
		print("none")
	else:
		print(len(matches))

if __name__ == "__main__":
	main()
