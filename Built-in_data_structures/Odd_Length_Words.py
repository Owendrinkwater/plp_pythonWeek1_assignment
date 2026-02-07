"""
Create a program that stores a list of words. 
Then, use list comprehension to create a new list 
that contains only the words that have 
an odd number of characters._
"""

words = ["python", "code", "developer", "AI", "fun", "learning"]

odd_length_words = [word for word in words if len(word) % 2 != 0]

print("Original list:", words)
print("Words with odd number of characters:", odd_length_words)
