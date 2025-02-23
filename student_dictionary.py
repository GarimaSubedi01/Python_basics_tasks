# Taking input for number of students
n = int(input("Enter the number of students: "))

# Creating dictionary to store student marks
student_dict = {}

for _ in range(n):
    name = input("Enter student name: ")
    marks = int(input(f"Enter marks for {name}: "))
    student_dict[name] = marks

# Finding student with highest marks
topper = max(student_dict, key=student_dict.get)

# Sorting dictionary by marks in descending order
sorted_students = dict(sorted(student_dict.items(), key=lambda x: x[1], reverse=True))

# Printing results
print("\nStudent Dictionary:", student_dict)
print(f"Top Scorer: {topper} with {student_dict[topper]} marks")
print("Sorted by marks (descending):", sorted_students)