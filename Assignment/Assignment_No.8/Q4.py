#Python program in sum of all odd numbers 

def sum_of_odd(num):
    total = 0

    for i in range(1, num + 1, 2):
        total += i

    return total

num = int(input("Enter num: "))
print("sum of odd numbers:", sum_of_odd(num))