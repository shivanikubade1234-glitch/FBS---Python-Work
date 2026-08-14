import random

userid = input("Enter User ID: ")
password = input("Enter Password: ")

if userid == "utkarsh" and password == "1234":
    num = random.randint(1000, 9999)
    print("Your number is:", num)

    n = int(input("Enter the number: "))

    if n == num:
        print("Success")
    else:
        print("Failed")
else:
    print("Wrong User ID or Password")