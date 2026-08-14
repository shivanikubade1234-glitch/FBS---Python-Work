# Numbers in range divisible by given number 


start = int(input("Enter starting number = "))
end = int(input("Enter ending number = "))
num = int(input("Enter divisor = "))

i = start

while i <= end:
    if i % num == 0:
        print(i)
    i = i + 1