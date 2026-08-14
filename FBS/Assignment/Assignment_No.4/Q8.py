# Divisible by 7 and multiple of 5

start = int(input("Enter starting number = "))
end = int(input("Enter ending number = "))

for i in range(start, end + 1):
    if i % 7 == 0 and i % 5 == 0:
        print(i)