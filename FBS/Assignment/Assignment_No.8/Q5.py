#Python program in sum of all prime numbers 


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def sum_of_prime(n):
    total = 0

    for i in range(1, n + 1):
        if is_prime(i):
            total += i

    return total


n = int(input("Enter n: "))
print("Sum of prime numbers:", sum_of_prime(n))