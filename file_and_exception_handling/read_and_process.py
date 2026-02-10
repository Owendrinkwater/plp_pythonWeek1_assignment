import os
print("Running from:", os.getcwd())

# Read the contents of input.txt
with open("input.txt", "r") as file:
    content = file.read()

# Count the number of words
word_count = len(content.split())

# Convert text to uppercase
processed_text = content.upper()

# Write processed text and word count to output.txt
with open("output.txt", "w") as file:
    file.write("PROCESSED TEXT:\n")
    file.write(processed_text)
    file.write("\n\nWORD COUNT:\n")
    file.write(str(word_count))

# Success message
print("✅ File processed successfully! 'output.txt' has been created.")
