# Call by value
# Only the value of the variable is passed to the function, not the
# variable itself.
def calc_area(radius):
    area = 3.142 * radius**2
    radius *= 2
    return area


r = int(input("Enter the radius of the circle: "))
print(r)
area = calc_area(r)
print(f"The area of the circle is: {area}")
print(r)


# call by reference
# The reference to the variable is passed to the function, allowing the
# function to modify the original
def calc_vol(args):
    volume = 3.142 * args[0] ** 2 * args[1]
    print(f"Volume of the cylinder is: {volume}")
    args[0] *= 2
    args[1] *= 2
    return volume


dimensions = [5, 10]  # radius and height of the cylinder
print(dimensions)
calc_vol(dimensions)
print(dimensions)
