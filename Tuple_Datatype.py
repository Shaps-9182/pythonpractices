# Creating a tuple
my_tuple = (1, 2, 3, "Hello", [4, 5], (6, 7))
print(my_tuple)
# Accessing elements
print(my_tuple[0])  # outputs 1
print(my_tuple[3])  # outputs Hello
print(my_tuple[4])  # outputs [4, 5]
print(my_tuple[5])  # outputs (6, 7)
# Slicing
print(my_tuple[1:4])  # outputs (2, 3, 'Hello')
print(my_tuple[::2])  # outputs (1, 3, [4, 5])
print(my_tuple[::-1])  # outputs ((6, 7), [4, 5], 'Hello', 3, 2, 1)
print(
    my_tuple * 2
)  # outputs (1, 2, 3, 'Hello', [4, 5], (6, 7), 1, 2, 3, 'Hello', [4, 5], (6, 7))
print(len(my_tuple))  # outputs 6
print(my_tuple[2:1:-1])  # outputs (3, 2)
# Tuples are immutable, so we cannot change their elements
# my_tuple[0] = 10  # This will raise a TypeError
# However, we can change the mutable elements inside the tuple
my_tuple[4][0] = 40  # Changing the first element of the list inside the tuple
print(my_tuple)  # outputs (1, 2, 3, 'Hello', [40, 5], (6, 7))
# we can convert a tuple to a list to modify it and then convert to a tuple again
temp = list(my_tuple)
temp[0] = 10  # changing the first element of the list
my_tuple = tuple(temp)  # converting back to a tuple
print(my_tuple)  # outputs (10, 2, 3, 'Hello', [40, 5], (6, 7))
# tuple operations
# Concatenation
a = (1, 2, 2, 3)
b = (4, 5, 2, 6, 6)
c = a + b
print(c)  # outputs (1, 2, 3, 4, 5, 6)
# Repetition
print(a * 3)  # outputs (1, 2, 3, 1, 2, 3, 1, 2, 3)
# Membership
print(2 in a)  # outputs True
print(7 in b)  # outputs False
# Tuple methods
# count() method
print(a.count(2))  # outputs 2
# index() method
print(b.index(2))  # outputs 2
# Looping through a tuple
colors = ("red", "green", "blue")
for color in colors:
    print(color)
# Indexing
for i in range(len(colors)):
    print(i, colors[i])
# Tuple packing and unpacking
# Packing
person = ("Alice", 25, "Data Scientist")
print(person)
# Unpacking
name, age, career = person
print("Name:", name)  # outputs Alice
print("Age:", age)  # outputs 25
print("Career:", career)  # outputs Data Scientist
