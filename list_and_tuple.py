# Taking user input as a list of numbers
num_list = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Finding max and min values
max_num = max(num_list)
min_num = min(num_list)

# Reversing the list without using .reverse()
reversed_list = num_list[::-1]

# Removing duplicates before converting to tuple
unique_list = list(set(num_list))

# Converting to tuple
num_tuple = tuple(unique_list)

# Finding the sum of elements in the tuple
sum_tuple = sum(num_tuple)

# Printing results
print(f"Original List: {num_list}")
print(f"Max: {max_num}, Min: {min_num}")
print(f"Reversed List: {reversed_list}")
print(f"Tuple: {num_tuple}")
print(f"Sum of elements in tuple: {sum_tuple}")
