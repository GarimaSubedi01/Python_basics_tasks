# Taking user input
text = input("Enter a string: ")

# Writing to a file
with open("output.txt", "w") as file:
    file.write(text)

# Reading from file
with open("output.txt", "r") as file:
    content = file.read()

# Counting words and characters
word_count = len(content.split())
char_count = len(content)

# Printing results
print("\nContent of file:", content)
print(f"Word Count: {word_count}")
print(f"Character Count: {char_count}")
