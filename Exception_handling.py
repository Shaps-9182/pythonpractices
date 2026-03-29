laptops = 15
students = 20

try:
    if laptops >= students:
        share = int(laptops / students)
        print("Each student gets", share, "laptops")
    else:
        print("Not enough laptops for each student")
        print(share)
except Exception as e:
    print("Errors found", e)

# Assertion error is use to deal wih logical error
laptops = "abcd"
students = "qwer"
try:
    assert laptops >= students, "laptops should be greater than or equal to students"
    "Assertion passed "
    share = int(laptops / students)
    print("Each student gets", share, "laptops")
except AssertionError as e:
    print("Assertion error found", e)
except Exception as e:
    print("Errors found", e)
