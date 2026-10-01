l = int(input("Enter Length: "))
b = int(input("Enter Breadth: "))
h = int(input("Enter Height: "))
rate = int(input("Enter Rate: "))

area = 2 * (l + b) * h
cost = area * rate

print("Painting Cost =", cost)