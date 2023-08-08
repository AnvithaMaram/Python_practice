def sum_of_digits(number):
    if number == 0:
        return 0
    else:
        return number % 10 + sum_of_digits(number // 10)

number = 3281
sum = sum_of_digits(number)
print("Sum of digits:", sum)
