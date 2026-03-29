# ry:
# a = int(input("Enter the first number:"))
# b = int(input("Enter the second number:"))
# result = a / b
# print("The result of", a, "divided by", b, "is:", result)
# except ValueError:
# print("Error: Please enter valid integers.")

# except ZeroDivisionError:
# print("Error: Division by zero is not allowed.")
# print("Error: Division by zero is not allowed.")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
try:
    results = num1 / num2
    print("The result of", num1, "divided by", num2, "is:", results)
except Exception as e:
    print("An error occurred:", str(e))
except Exception as e:
    print("An error occurred:", str(e))
