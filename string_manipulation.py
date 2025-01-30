def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in s if char in vowels)
    consonant_count = sum(1 for char in s if char.isalpha() and char not in vowels)
    return vowel_count, consonant_count

def is_palindrome(s):
    return s == s[::-1]  # Checks if the string is the same when reversed

def most_frequent_char(s):
    s = s.replace(" ", "")  # Removing spaces
    char_count = {char: s.count(char) for char in set(s)}
    most_frequent = max(char_count, key=char_count.get)
    return most_frequent, char_count[most_frequent]

# Taking input
user_string = input("Enter a string: ")

# Performing string operations
reversed_string = user_string[::-1]
uppercase_string = user_string.upper()
lowercase_string = user_string.lower()
vowel_count, consonant_count = count_vowels_consonants(user_string)
palindrome_check = is_palindrome(user_string)
hyphenated_string = user_string.replace(" ", "-")
split_words = user_string.split()

# Displaying results
print("\n--- String Manipulation Results ---")
print(f"Original String: {user_string}")
print(f"Reversed String: {reversed_string}")
print(f"Uppercase: {uppercase_string}")
print(f"Lowercase: {lowercase_string}")
print(f"Number of Vowels: {vowel_count}")
print(f"Number of Consonants: {consonant_count}")
print(f"Is Palindrome? {'Yes' if palindrome_check else 'No'}")
print(f"String with spaces replaced by hyphens: {hyphenated_string}")
print(f"Split words: {split_words}")

# Finding most frequent character
most_frequent, frequency = most_frequent_char(user_string)
print(f"Most frequent character (excluding spaces): '{most_frequent}' (appears {frequency} times)")
