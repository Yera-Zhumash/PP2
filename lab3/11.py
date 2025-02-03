def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [10, 15, 3, 7, 21, 29, 31]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print(prime_numbers)  # Output: [3, 7, 29, 31]
