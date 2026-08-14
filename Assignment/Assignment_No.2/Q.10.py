num = int(input("Enter a three-digit number: "))

hundred = num // 100
tens = (num // 10) % 10
ones = num % 10

reverse = ones * 100 + tens * 10 + hundred

print("Reverse =", reverse)