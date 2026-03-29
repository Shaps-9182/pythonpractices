def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Example usage
if __name__ == "__main__":
    num = int(input("Enter number to calculate factorial:"))
    print(f"The factorial of {num} is {factorial(num)}")
