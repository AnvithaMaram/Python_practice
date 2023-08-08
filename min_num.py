def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_minimum_number(num):
    sum_of_digits = sum(int(digit) for digit in str(num))

    if is_prime(sum_of_digits):
        return 0

    diff = 1

    while True:
        if is_prime(sum_of_digits + diff):
            return diff
        if is_prime(sum_of_digits - diff):
            return -diff
        
        diff += 1

print(find_minimum_number(44))    

