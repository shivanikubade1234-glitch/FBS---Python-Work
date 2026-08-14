length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))
radius = int(input("Enter radius: "))

area_rectangle = length * breadth
area_semicircle = 3.14 * radius * radius / 2

area = area_rectangle + area_semicircle

perimeter = breadth + length + length + 3.14 * radius

print("Area =", area)
print("Perimeter =", perimeter)