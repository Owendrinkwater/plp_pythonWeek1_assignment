"""
Write a program that uses a dictionary to store information 
about a person, such as their name, age, and favorite color. 
Ask the user for input and store the information in the dictionary. 
Then, print the dictionary to the console.
"""

person = {}

person["name"] = input("Enter your name: ")
person["age"] = int(input("Enter your age: "))
person["favorite_color"] = input("Enter your favorite color: ")

print("\nPerson information:")
print(person)
