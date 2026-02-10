try:
    # Ask user for filename
    filename = input("Enter the name of the file to read: ")

    # Try to open and read the file
    with open(filename, "r") as file:
        content = file.read()

    # Modify the content (example: convert to uppercase)
    modified_content = content.upper()

    # Write modified content to a new file
    with open("modified_output.txt", "w") as file:
        file.write(modified_content)

    print("✅ File processed successfully!")
    print("📄 Modified content saved to 'modified_output.txt'")

except FileNotFoundError:
    print("❌ Error: The file does not exist.")

except PermissionError:
    print("❌ Error: You do not have permission to read this file.")

except Exception as e:
    print("❌ An unexpected error occurred:", e)
