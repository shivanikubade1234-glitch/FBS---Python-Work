num = int(input("Enter a 3 digit number: "))

first = num // 100
middle = (num // 10) % 10
last = num % 10

reverse = last * 100 + middle * 10 + first

if num == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")