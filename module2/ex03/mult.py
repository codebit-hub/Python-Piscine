#! /usr/bin/env python3

user_input1 = input("Enter the first number: ")
user_input2 = input("Enter the second number: ")

nbr1 = int(user_input1)
nbr2 = int(user_input2)
result = nbr1 * nbr2

print(nbr1, "x", nbr2, "=", result)
print(f"{nbr1} x {nbr2} = {result}")
if result > 0:
	print("The result is positive.")
elif result < 0:
	print("The result is negative.")
else:
	print("The result is positive and negative.")
