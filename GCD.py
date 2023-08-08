def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a

    return gcd(b, a % b)


num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))

result = gcd(num1, num2)

print("GCD of", num1, "and", num2, "is", result)
