def withdraw(balance, amount):
    balance = int(input("Enter the account balance:"))
    amount = int(input("Enter the amount you want to withdraw::"))
    assert balance <= amount, "You have insufiecient funds to withdraw"
    result = balance - amount
    print(
        "The bank balance ",
        balance,
        "after withdrawing this amonut",
        amount,
        "is:",
        result,
    )
    return result


try:
    withdraw(1000, 500)
except AssertionError as e:
    print("Assertion Error:", str(e))
