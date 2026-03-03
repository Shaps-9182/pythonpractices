person = dict(name="leisi", Age=21, country="kenya")
print(person)
# accessing values
# values are acces using values and keys
print(person["name"])
print(person["Age"])
print(person["country"])
# using key
print(person.get("age"))
print(person.keys())
# check if value exits in person
print("age" in person)
print("name" in person)
# update values in the dictonary
person["name"] = "isaac"
person.update({"Age": 22})
person.update({"hobby": "football"})
print(person)
# Removing values using pop function
# person.pop("country")
# print(person)
# Removing the last element using pop item function
# person.popitem()
# print(person)
# Removing the whole elements
# person.clear()
# print(person)
# using del keyword
del person["name"]
print(person)
# Return keys and values
person.update({"course": "Data Science"})
print(person)
print(person.items())
# loop
for keys, values in person.items():
    print(keys, "", values)
# Example002
students = {
    "stu001": {"name": "Alice", "marks": {"Python": 78, "Math": 65}},
    "stu002": {"name": "Bob", "marks": {"Python": 55, "Math": 72}},
    "stu003": {"name": "Carol", "marks": {"Python": 90, "Math": 88}},
}
# update each student's marks by 5
for student in students.values():
    student["marks"]["Python"] = min(student["marks"]["Python"] + 5, 100)
    print(student)
    # Math
    for student in students.values():
        student["marks"]["Math"] = min(student["marks"]["Math"] + 5, 100)
        print(student)
# Remove students that have math below 70
students = {
    sid: data for sid, data in students.items()
    if data["marks"]["Math"] >= 70
}
print(students)
