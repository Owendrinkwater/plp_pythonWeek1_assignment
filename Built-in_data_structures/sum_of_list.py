"""
Write a program that accepts user 
input to create a list of integers. 
Then, compute the sum of all the integers in the list.
"""
numbers = []

n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

total = sum(numbers)

print("\nList of numbers:", numbers)
print("Sum of the integers:", total)
