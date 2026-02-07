"""
Write a program that accepts user input to create 
two sets of integers. Then, create a new set that 
contains only the elements that are common to both sets.
"""

set1 = set()
set2 = set()

n1 = int(input("How many numbers for the first set? "))
for i in range(n1):
    num = int(input(f"Enter number {i + 1} for set 1: "))
    set1.add(num)

n2 = int(input("\nHow many numbers for the second set? "))
for i in range(n2):
    num = int(input(f"Enter number {i + 1} for set 2: "))
    set2.add(num)

common_elements = set1&set2

print("\nFirst set:", set1)
print("Second set:", set2)
print("Common elements:", common_elements)
