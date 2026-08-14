n = int(input("Enter a three-digit number: "))

a = n // 100
b = (n // 10) % 10
c = n % 10

sum = a + b + c

print("Sum of digits =", sum)