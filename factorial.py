def factorial(n):
    result = 1
    if n < 0:
        print("Enter only positive integers")
    elif n == 0 | n == 1:
        return 1
    else:
        for i in range(2, n + 1):
            result *= i
        return result

n = int(input("Enter a integer: "))
factorial_n = factorial(n)
print(f"The factorial of {n} is {factorial_n}.")

