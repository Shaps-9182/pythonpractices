# Required arguments
def add(a, b):
    return a + b


add(5, 3)


# Keyword arguments
def cal_vol(r, h):
    volume = 3.142 * r**2 * h
    print(f"Volume of the cylinder is {volume}")
    return volume


cal_vol(h=10, r=5)


# Default arguments
def cal_vol(r, h=10):
    volume = 3.142 * r**2 * h
    print(f"Volume of the cylinder is {volume}")
    return volume


cal_vol(7)


# variable-length arguments
def cal_vol(r, *heights):
    for h in heights:
        volume = 3.142 * r**2 * h
        print(f"The volume of the cylinder with {h} height is {volume}")
        return volume


cal_vol(5, 10, 15, 20)
