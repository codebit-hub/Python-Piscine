#!/usr/bin/env python3
import sys

def main():
	if len(sys.argv) < 3:
		print("none")
	else:
		#for arg in reversed(sys.argv[1:]):
		for arg in sys.argv[:0:-1]:
			print(arg)

if __name__ == "__main__":
	main()
