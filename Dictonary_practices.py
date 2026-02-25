student = {
    "name": "Leisi",
    "age": 21,
    "city": "Meru Town",
    "course": "Data Science",
    "Marks": {"Maths": 85, "Python": 90, "Database": 80},
}
print(student)
# Print the student name
print(student["name"])
# Print student marks
print(student["Marks"])
# print a specific value in marks
print(student["Marks"]["Python"])
# Add a new key-value pair to the student dictionary
student.update({"Gender": "Male"})
print(student)
# we can also add a new key-value pair by directly assigning
# a value to a new key
# student["Gender"] = "Male"
# print(student)
# Update the student's age
student.update({"age": 22})
print(student)
# we can also update the student's age by directly assigning
# a new value to the existing key
# student["age"] = 22
# print(student)
# Remove a key-value pair from the student dictionary
# student.pop("Database")  # This will raise a KeyError because
# "Database" is not a key in student
# print(student)
# we can also remove a key-value pair using del
# del student["Database"]  # This will raise a KeyError because
# "Database" is not a key in student
# print(student)
# we can also remove a key-value pair using popitem
student.popitem()  # This will remove the last key-value pair added to student
print(student)
# Looping through the student dictionary
for key in student:
    print(key, student[key])
# Looping through keys and values using items()
for key, value in student.items():
    print(key, value)
# find the average marks of the student
marks = student["Marks"]
average_marks = sum(marks.values()) / len(marks)
print("Average Marks:", average_marks)
# loop through the marks and print the subject and marks
for Marks, value in student.items():
    print(Marks, "", value)
