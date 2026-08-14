# python program in 5 Subject Marks and Display Grade

m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
m4 = int(input("Enter marks of subject 4: "))
m5 = int(input("Enter marks of subject 5: "))

average = (m1 + m2 + m3 + m4 + m5) / 5

if average >= 60:
    print("First Class")
elif average >= 50:
    print("Second Class")
elif average >= 35:
    print("Pass Class")
else:
    print("Fail")