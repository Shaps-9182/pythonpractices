numbers = (10, 5, 10, 3, 8, 5, 2)
# To perform operations on the tuple we have first to convert it to list
# which are mutable
a = list(numbers)
# Remove duplicates
b = []
for i in a:
    if i not in b:
        b.append(i)
        print(b)
# Add 10 to each element
for i in range(len(b)):
    b[i] += 10
    print(b)
# Remove 2 from each element
for i in range(len(b)):
    b[i] -= 2
    print(b)
# Arrange the elements  in ascending order
asc = sorted(b)
print(asc)
print(b)
# Arrange in descending order
desc = sorted(b, reverse=True)
print(desc)
print(b)
# Changing back to tuple
numbers = tuple(b)
print(numbers)
# Looping through the turple
for i in range(len(numbers)):
    print(i, "", numbers)
# Accesing elements in the tuple
print(numbers[1:3])
print(numbers[1])
